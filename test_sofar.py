#!/usr/bin/env python3
"""Pymodbus asynchronous client example.

An example of a single threaded synchronous client.

usage: simple_client_async.py

All options must be adapted in the code
The corresponding server must be started before e.g. as:
    python3 server_sync.py
"""
from config import config
from sofar_solar_modbus_map import register_mask_list, register_map, error_codes
import asyncio
import struct
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
)
from datetime import datetime

global temporary_list
temporary_list = config["desired_addresses_list"].copy()


def combine_registers_to_u64(registers):
    """Combine four 16-bit registers into a single U64 value, assuming big-endian byte order."""
    return (registers[0] << 48) | (registers[1] << 32) | (registers[2] << 16) | registers[3]


async def read_and_process_address_masks(client, mask_addresses, mask_length=4, slave=0):
    """Read multiple U64 address masks and update the global temporary_list to only include active addresses.

    Args:
        :param client: The Modbus client instance.
        :param mask_addresses: A list of starting addresses for the U64 address masks, typically the first register of each mask section.
        :param mask_length: The number of registers that each U64 mask spans, typically 4 for U64.
        :param slave:
    """
    global temporary_list
    active_addresses = set()
    total_addresses = 64
    for mask_start_address in mask_addresses:
        rr = await client.read_holding_registers(address=mask_start_address, count=mask_length, slave=slave)
        if not rr.isError():
            mask_value = combine_registers_to_u64(rr.registers)
            for i in range(total_addresses):
                if mask_value & (1 << i):
                    active_address = mask_start_address + i
                    active_addresses.add(active_address)
        else:
            print(f"Error reading address mask at {mask_start_address}")
        await asyncio.sleep(0.1)
    # Filter the temporary_list based on active addresses
    temporary_list = [addr for addr in temporary_list if addr in active_addresses]


def process_registers_into_json_data(start_address, registers):
    data = {}
    i = 0  # Use i to manually control the loop index for multi-register values
    while i < len(registers):
        current_address = start_address + i

        if current_address not in register_map:
            i += 1
            continue  # Skip if the register address is not found in the map

        reg_info = register_map[current_address]
        description = reg_info.get("description", '')
        unit = reg_info.get("unit", '')
        sign = reg_info.get("sign", None)
        multiplier = float(reg_info.get("multiplier", 1))
        data_type = reg_info.get('data_type', 'U16')  # Assuming U16 if not specified

        # Handling for U32 data type
        if data_type == 'U32':
            if i + 1 < len(registers):
                # Using struct to pack and then unpack as U32 (big-endian)
                packed_value = struct.pack('>HH', registers[i], registers[i + 1])
                raw_value_combined = struct.unpack('>I', packed_value)[0]
                scaled_value = raw_value_combined * multiplier
                i += 2  # Increment i based on the number of registers read
            else:
                print(f"Insufficient data for U32 at address {current_address}")
                break

        # Handling for U16 data type, including error/fault codes
        elif sign in ["U16", "I16"] or current_address in error_codes:
            packed_value = struct.pack('>H', registers[i])
            raw_value = struct.unpack('>H', packed_value)[0]

            if current_address in error_codes:
                # Processing bitwise to detect set bits for error/fault codes
                messages = []
                for bit_index in range(16):
                    byte_index = bit_index // 8  # Determine byte index (0 or 1)
                    bit_in_byte = bit_index % 8  # Determine bit position within the byte
                    key = (byte_index, bit_in_byte)
                    if key in error_codes[current_address]:
                        fault_info = error_codes[current_address][key]
                        messages.append(f"{fault_info['label']}: {fault_info['description']}")
                scaled_value = "; ".join(messages) if messages else "No errors"
                unit = ""  # Reset unit for error messages
            else:
                # Apply multiplier for non-error data
                scaled_value = raw_value * multiplier
            i += 1  # Increment i for single register

        else:
            # Placeholder for handling other data types or skipping unsupported types
            scaled_value = "Unsupported data type or reserved for masks"
            i += 1  # Increment i appropriately

        data[current_address] = {
            "description": description,
            "value": scaled_value,
            "unit": unit,
        }

    return data


def format_data_for_database(processed_data):
    """Format the processed data into the database JSON structure."""
    timestamp = datetime.now().isoformat()
    formatted_data = {timestamp: {}}

    for address, values in processed_data.items():
        formatted_data[timestamp][address] = values

    return formatted_data


async def read_async_client(comm, host, port, framer=Framer.SOCKET,slave=0):
    """Run async client."""
    # activate debugging
    pymodbus_apply_logging_config("DEBUG")

    print("get client")
    if comm == "tcp":
        client = ModbusClient.AsyncModbusTcpClient(
            host=host,
            port=port,
            framer=Framer.SOCKET,
            # timeout=10,
            # retries=3,
            # retry_on_empty=False,
            # close_comm_on_error=False,
            # strict=True,
            # source_address=("localhost", 0),
        )
    elif comm == "udp":
        client = ModbusClient.AsyncModbusUdpClient(
            host,
            port=port,
            framer=framer,
            # timeout=10,
            # retries=3,
            # retry_on_empty=False,
            # close_comm_on_error=False,
            # strict=True,
            # source_address=None,
        )
    elif comm == "serial":
        client = ModbusClient.AsyncModbusSerialClient(
            port,
            framer=Framer.RTU,
            # timeout=10,
            # retries=3,
            # retry_on_empty=False,
            # close_comm_on_error=False,
            # strict=True,
            baudrate=9600,
            bytesize=8,
            parity="N",
            stopbits=1,
            timeout=5
            # handle_local_echo=False,
        )
    elif comm == "tls":
        client = ModbusClient.AsyncModbusTlsClient(
            host,
            port=port,
            framer=Framer.TLS,
            # timeout=10,
            # retries=3,
            # retry_on_empty=False,
            # close_comm_on_error=False,
            # strict=True,
            # sslctx=sslctx,
            certfile="../examples/certificates/pymodbus.crt",
            keyfile="../examples/certificates/pymodbus.key",
            # password="none",
            server_hostname="localhost",
        )
    else:  # pragma no cover
        print(f"Unknown client {comm} selected")
        return

    print("connect to server")
    await client.connect()
    # test client is connected
    assert client.connected
    print("connected,parsing data")
    try:
        all_data = {}  # Dictionary to accumulate all readable data

        # Initially check the status of every address based on the mask
        # Make sure to pass register_mask_list containing the mask addresses
        await read_and_process_address_masks(client, register_mask_list, slave=slave)

        # Use the filtered temporary_list after processing masks
        address_list = temporary_list.copy()  # Ensure temporary_list is defined and filled previously

        while True:
            for start_address in address_list:  # List of starting addresses
                rr = await client.read_holding_registers(start_address, count=2, slave=slave)  # Adjust unit as needed
                if rr.isError() or isinstance(rr, ExceptionResponse):
                    print(f"Error or Exception while Reading data at address {start_address}: {rr}")
                    continue

                processed_data = process_registers_into_json_data(start_address, rr.registers)
                all_data.update(processed_data)
                # Update all_data with the new database_data

            database_data = format_data_for_database(all_data)

            # Print all accumulated data
            print("\nComplete Data:")
            for timestamp, values in database_data.items():
                print(f"{timestamp}:")
                for address, data in values.items():
                    print(f"  {address}: {data}")

            await asyncio.sleep(10)
            all_data = {}  # Reset the dictionary for the next loop

    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
    finally:
        print("close connection")
        client.close()


def main():
    # loop = asyncio.get_event_loop()
    asyncio.run(read_async_client(comm=config["comm"], port=config["port"], host=config["host"], slave=12), debug=False)
    # pragma: no cover


if __name__ == "__main__":
    main()
