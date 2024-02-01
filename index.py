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


async def run_async_simple_client(comm, host, port, framer=Framer.SOCKET):
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
    print("get and verify data")
    try:
        while True:
            rr = await client.read_input_registers(2, 2, slave=1)
            rr1 = await client.read_input_registers(14, 2, slave=1)
            rr2 = await client.read_input_registers(2, 2, slave=1)
            rr3 = await client.read_input_registers(14, 2, slave=1)
            rr = await client.read_input_registers(2, 2, slave=1)
            rr1 = await client.read_input_registers(14, 2, slave=1)
            # hex_registers = ''.join(format(register, '04x') for register in rr.registers + rr1.registers)
            # print("Hex Data from Registers:", hex_registers)
            if rr.isError() or rr1.isError():
                print(f"Error while Reading data")
                client.close()
                return
            if isinstance(rr, ExceptionResponse):
                print(f"Received Modbus library exception ({rr})")
                client.close()
                return
            if isinstance(rr1, ExceptionResponse):
                print(f"Received Modbus library exception ({rr1})")
                client.close()
                return
            # Processing and converting the response to 32-bit float
            combined_registers = rr.registers + rr1.registers
            # Processing and converting the combined response to 32-bit float
            floats = []


            for i in range(0, len(combined_registers), 2):
                # Combine two consecutive registers and unpack as 32-bit float
                raw = struct.pack('>HH', combined_registers[i], combined_registers[i + 1])
                floats.append(struct.unpack('>f', raw)[0])
            liczba += 1
            print("Combined Data:", floats)
            await asyncio.sleep(2)
    except ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
    finally:
        print("close connection")
        client.close()


if __name__ == "__main__":
    asyncio.run(
        run_async_simple_client("tcp", port="503", host='192.168.1.3'), debug=True
    )  # pragma: no cover

