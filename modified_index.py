
#!/usr/bin/env python3
import asyncio
import struct
import pymodbus.client as ModbusClient
from pymodbus import ExceptionResponse, ModbusException, pymodbus_apply_logging_config
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
)

async def run_async_modbus_client(host, port,framer=Framer.SOCKET):
    pymodbus_apply_logging_config("DEBUG")

    # Connect to the inverter using Modbus TCP with RTU framer
    client = ModbusClient.AsyncModbusTcpClient(
        host,
        port=port,
        framer=Framer.RTU,
        timeout=10
    )

    await client.connect()
    assert client.connected

    try:
        # Define the register addresses and their respective types
        registers = {
            0x0206: ('Grid A Voltage', 'uint', 0.1),
            0x0207: ('Grid A Current', 'int', 0.01),
            0x0208: ('Grid B Voltage', 'uint', 0.1),
            0x0209: ('Grid B Current', 'int', 0.01),
            0x020A: ('Grid C Voltage', 'uint', 0.1),
            0x020B: ('Grid C Current', 'int', 0.01),
            0x020C: ('Grid Frequency', 'uint', 0.01)
        }

        # Read and process data from each register
        for address, (name, data_type, scale) in registers.items():
            response = await client.read_input_registers(address, 1, unit=1)
            if response.isError():
                print(f"Error reading {name}: {response}")
                continue

            # Decode response based on data type
            decoder = BinaryPayloadDecoder.fromRegisters(response.registers, byteorder=Endian.Big)
            if data_type == 'uint':
                value = decoder.decode_16bit_uint() * scale
            else:  # int
                value = decoder.decode_16bit_int() * scale

            print(f"{name}: {value}")

    except ModbusException as exc:
        print(f"Modbus Exception: {exc}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(run_async_modbus_client("192.168.1.3", 502))
