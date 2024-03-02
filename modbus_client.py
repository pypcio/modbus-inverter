#!/usr/bin/env python3
"""Asynchronous Modbus client for reading data."""

from sofar_solar_modbus_map import register_mask_list, register_map, error_codes
from config import config as settingsConfiguration
import asyncio
import struct
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
)


class AsyncModbusSlave:
    def __init__(self, config):
        self.port = config.get("port", "502")
        self.host = config.get("host", "localhost")
        self.slave_id = config.get("slave_id", 0)
        self.comm = config.get("comm", "tcp")
        self.framer = config.get("framer", Framer.SOCKET)
        self.debug = config.get("debug", False)
        self.client = None
        self.temporary_list = config["desired_addresses_list"].copy()
        self.__counter = 0
        self.last_processed_mask_index = 0
        self.decoded_data = {}
        # self.instructiones

    async def handle_error(self, error, action="default", **kwargs):
        """
        Handles errors that occur during Modbus operations.

        :param error: The exception that was caught.
        :param action: The action to take in response to the error. This could be 'retry', 'log', 'alert', etc.
        :param kwargs: Additional keyword arguments that might be necessary for handling specific actions.
        """
        if action == "retry":
            retries = kwargs.get("retries", 3)
            delay = kwargs.get("delay", 1)  # Delay between retries in seconds
            operation = kwargs.get("operation")
            operation_kwargs = kwargs.get("operation_kwargs", {})

            for attempt in range(retries):
                try:
                    await asyncio.sleep(delay)
                    await operation(**operation_kwargs)
                    print(f"Operation succeeded on attempt {attempt + 1}")
                    return
                except Exception as retry_error:
                    print(f"Retry {attempt + 1}/{retries} failed with error: {retry_error}")

            print("All retries failed.")
        elif action == "log":
            # Log the error to a file or logging system
            print(f"Logging error: {error}")
        elif action == "alert":
            # Send an alert (email, SMS, etc.) about the error
            print(f"Alerting: {error}")
        else:
            # Default error handling
            print(f"Error encountered: {error}")

    async def connect(self):
        try:
            if self.debug:
                pymodbus_apply_logging_config("DEBUG")
                print("get client")
            if self.comm == "tcp":
                self.client = ModbusClient.AsyncModbusTcpClient(
                    host=self.host,
                    port=self.port,
                    framer=self.framer
                    # timeout=10,
                    # retries=3,
                    # retry_on_empty=False,
                    # close_comm_on_error=False,
                    # strict=True,
                    # source_address=("localhost", 0),
                )
            elif self.comm == "udp":
                self.client = ModbusClient.AsyncModbusUdpClient(
                    host=self.host,
                    port=self.port,
                    framer=self.framer
                    # timeout=10,
                    # retries=3,
                    # retry_on_empty=False,
                    # close_comm_on_error=False,
                    # strict=True,
                    # source_address=None,
                )
            elif self.comm == "serial":
                self.client = ModbusClient.AsyncModbusSerialClient(
                    port=self.port,
                    framer=self.framer,
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
            elif self.comm == "tls":
                self.client = ModbusClient.AsyncModbusTlsClient(
                    host=self.host,
                    port=self.port,
                    framer=self.framer,
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
                self.client = None
                print(f"Unknown client {self.comm} selected")
                return
            connection_result = await self.client.connect()
            if connection_result and self.debug:
                print("Connected, parsing data")
            else:
                self.client = None  # Explicitly indicate failure
                # Decide on further action: retry, alert, etc.
                await self.handle_error(error="Failed to connect", action="alert")

        except Exception as e:
            self.client = None
            await self.handle_error(error=e, action="alert")


def get_counter(self):
    return self.__counter


@staticmethod
def combine_registers_to_u64(registers):
    """Combine four 16-bit registers into a single U64 value, assuming big-endian byte order."""
    return (registers[0] << 48) | (registers[1] << 32) | (registers[2] << 16) | registers[3]


async def read_and_process_address_masks(self, mask_addresses, mask_length=4, delay=0.1):
    """Read and process address masks to update the list of active addresses."""
    active_addresses = set()
    total_addresses = 64
    for index, mask_start_address in enumerate(mask_addresses[self.last_processed_mask_index:],
                                               start=self.last_processed_mask_index):

        rr = await self.client.read_holding_registers(address=mask_start_address, count=mask_length, slave=self.slave_id)
        if not rr.isError():
            mask_value = self.combine_registers_to_u64(rr.registers)
            for i in range(total_addresses):
                if mask_value & (1 << i):
                    active_address = mask_start_address + i
                    active_addresses.add(active_address)
            self.last_processed_mask_index = index  # Update the last successfully processed index
        else:
            print(f"Error reading address mask at {mask_start_address}")
            break  # Stop processing further if an error occurs
        await asyncio.sleep(delay=delay)
    self.temporary_list = [addr for addr in self.temporary_list if addr in active_addresses]
    # Reset the index if all addresses have been processed successfully
    if self.last_processed_mask_index + 1 == len(mask_addresses):
        self.last_processed_mask_index = 0


async def read_registers(self, start_address, count):
    """Read and process registers starting from a given address."""
    if self.client is None or not self.client.connected:
        response = await self.client.read_holding_registers(start_address, count=count, slave=self.slave_id)
        if not response.isError():
            return response.registers
        else:
            print(f"Error reading registers starting at address {start_address}: {response}")
    else:
        print("Modbus client is not connected.")
    return []


def decode_registers(self, start_address, registers):
    """Read and process registers starting from a given addresess"""

    # Assuming register_map and error_codes are defined outside if not passed
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
        multiplier_value = reg_info.get("multiplier", 1)
        multiplier = float(multiplier_value if multiplier_value else 1)
        # data_type = reg_info.get('data_type', 'None')  # Assuming U16 if not specified

        # Handling for U32 data type
        if sign == 'U32':
            if i + 1 < len(registers):
                packed_value = struct.pack('>HH', registers[i], registers[i + 1])
                raw_value_combined = struct.unpack('>I', packed_value)[0]
                scaled_value = raw_value_combined * multiplier
                i += 2  # Increment i based on the number of registers read
            else:
                print(f"Insufficient data for U32 at address {current_address}")
                break

        # Handling for U16 data type, including error/fault codes
        elif sign == "U16" or current_address in error_codes:
            packed_value = struct.pack('>H', registers[i])
            if current_address in error_codes:
                messages = []
                byte0, byte1 = struct.unpack('>BB', packed_value)
                # Check both bytes (byte0 and byte1) for messages
                for byte_index, byte_value in enumerate([byte0, byte1]):
                    for bit_index in range(8):
                        if byte_value & (1 << bit_index):
                            key = (byte_index, bit_index)
                            if key in error_codes.get(current_address, {}):
                                messages.append(error_codes[current_address][key])

                scaled_value = "; ".join(messages) if messages else "No errors"
                unit = ""  # Reset unit for messages
            else:
                raw_value = struct.unpack('>H', packed_value)[0]
                scaled_value = raw_value * multiplier
            i += 1  # Increment i for single register

        elif sign == "I16":
            # For signed 16-bit integers
            packed_value = struct.pack('>H', registers[i])
            raw_value = struct.unpack('>h', packed_value)[0]  # Unpack as signed
            scaled_value = raw_value * multiplier
            i += 1

        else:
            scaled_value = "Unsupported data type or reserved for masks"
            i += 1  # Increment i appropriately

        data[current_address] = {
            "description": description,
            "value": scaled_value,
            "unit": unit,
        }
    self.decoded_data.update(data)


def process_instruction(self, instruction):
    # do some processing stuff
    print('Siema, procesuje')
    address = instruction['address']
    value = instruction['value']
    return address, value


async def read(self):
    """Read data from the Inverter."""
    await self.connect()
    if self.client is None or not self.client.connected:
        print("Unable to connect to the client.")
        return
    if self.__counter == 0:
        try:
            # checking address status using mask
            await self.read_and_process_address_masks(register_mask_list)
        except Exception as e:
            print(f"Error processing address masks: {e}")
            await self.handle_error(
                error=e,
                action="retry",
                retries=2,
                delay=1,
                operation=self.read_and_process_address_masks,
                operation_kwargs={'register_mask_list': register_mask_list, 'slave_id': self.slave_id, 'delay': 1}
            )
    else:
        for address in self.temporary_list:
            try:
                response_read = await self.read_registers(address, count=6)  # <----------------------- count
                self.decode_registers(address, response_read)
            except Exception as e:
                print(f"Error reading or decoding registers at address {address}: {e}")
                # Handle or log this error, possibly continue to the next address
        self.__counter += 1
        print("\nComplete Data:")
        for address, data in self.decoded_data.items():
            print(f"  {address}: {data}")

        await asyncio.sleep(10)
        # Further operations based on updated self.temporary_list


async def write_registers(self, start_address, count):
    """Write and process registers starting from a given address."""
    if self.client:
        response = await self.client.write_holding_registers(start_address, count=count, slave=self.slave_id)
        if not response.isError():
            return response.registers
        else:
            print(f"Error reading registers starting at address {start_address}: {response}")
    else:
        print("Modbus client is not connected.")
    return []


async def write(self, instructions):
    """write data from Inverter."""
    await self.connect()
    if self.client is None or not self.client.connected:
        return
    for instructions in instructions:
        # process instruction to get:
        address, value = self.process_instruction()
        response_write = await self.write_registers()


# poza klasa!!@!@!@!@!@
async def main(config):
    # for slave in config["slaves"]:
    reader1 = AsyncModbusSlave(config)
    await reader1.read()


if __name__ == "__main__":
    asyncio.run(main(settingsConfiguration))
