#!/usr/bin/env python3
"""Pymodbus asynchronous client example.

An example of a single threaded synchronous client.

usage: simple_client_async.py

All options must be adapted in the code
The corresponding server must be started before e.g. as:
    python3 server_sync.py
"""
import asyncio
import struct
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
)

# Mapping of register addresses to their descriptions and units
REGISTER_MAP = {
    0x0000: ("Status", " "),
    0x0006: ("Grid A Voltage", "V","Uint"),
    0x0007: ("Grid A Current", "A","int"),
    0x0008: ("Grid B Voltage", "V","Uint"),
    0x0009: ("Grid B Current", "A","int"),
    0x000A: ("Grid C Voltage", "V","Uint"),
    0x000B: ("Grid C Current", "A","int"),
    0x000C: ("Grid Frequency", "Hz"),
    0x000D: ("Charge/Discharge Power", "kW","int"),
    0x000E: ("Battery Voltage", "V","int"),
    0x000F: ("Battery Charge/Discharge Current", "A"),
    0x0010: ("The Residual", "%"),  # Assuming "The Residual" refers to battery charge state or similar.
    0x002B: ("Fault message", " "),
    0x0039:  ("heat sink Value", "C"),
}
UNIT_MAP = {
    'Uint' : 0.1,
    'int' : 0.01,
}
# List of addresses to read
# address_list = [0x0000, 0x0039]
address_list=[0x0000]

def process_registers_float(start_address, registers):
    """Process Modbus registers and return list of 32-bit floats with descriptions."""
    floats = []
    for i in range(0, len(registers), 2):
        if start_address + i not in REGISTER_MAP:
            continue
        raw = struct.pack('>HH', registers[i], registers[i + 1])
        float_value = struct.unpack('>f', raw)[0]
        description, unit = REGISTER_MAP.get(start_address + i, ("Unknown", ""))
        floats.append(f"{description}: {float_value:.2f} {unit}")
    return floats


def process_registers(start_address, registers):
    """Process Modbus registers and return 16-bit  values with descriptions."""
    values = []
    for i, register in enumerate(registers):
        if start_address + i not in REGISTER_MAP:
            continue
        description, unit = REGISTER_MAP.get(start_address + i, ("Unknown", ""))
        if unit == "V" or unit == "Hz" or unit == "kW" or unit == "%":  # Assuming these are Uint
            value = register
        elif unit == "A":  # Assuming these are int
            value = struct.unpack('>h', struct.pack('>H', register))[0]  # Convert unsigned to signed
        else:
            value = register  # Default case if no specific unit is matched

        values.append(f"{description}: {value} {unit}")
    return values


async def run_async_simple_client(comm, host, port, framer=Framer.SOCKET, address_list=[]):
    """Run async client."""
    # activate debugging
    pymodbus_apply_logging_config("DEBUG")

    print("get client")
    if comm == "tcp":
        client = ModbusClient.AsyncModbusTcpClient(
            host,
            port=port,
            framer=Framer.RTU,
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
    liczba = 0
    print("connected,parsing data")
    try:
        all_data = []  # List to accumulate all readable data
        while True:
            for start_address in address_list:  # List of starting addresses
                rr = await client.read_holding_registers(start_address, 2, slave=1)
                if rr.isError() or isinstance(rr, ExceptionResponse):
                    print(f"Error or Exception while Reading data at address {start_address}: {rr}")
                    continue

                # readable_data = process_registers_int(start_address, rr.registers)
                readable_data = rr.registers
                all_data.extend(readable_data)
                # joined_string= '\t'.join(rr.registers)


            # Print all accumulated data
            print("\nComplete Data:")
            for data in all_data:
                print(data)

            await asyncio.sleep(2)
            all_data = []

    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
    finally:
        print("close connection")
        client.close()


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()

    asyncio.run(
        run_async_simple_client("tcp", port="502", host='192.168.1.3', address_list=address_list), debug=False
    )  # pragma: no cover
