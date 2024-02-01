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
    0x0000: ("Status", "", 'status'),
    0x0001: ("message 1", "", 'status'),
    0x0002: ("message 2", "", 'status'),
    0x0003: ("message 3", "", 'status'),
    0x0004: ("message 4", "", 'status'),
    0x0005: ("message 5", "", 'status'),
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
error_codes = {
    #Fault 1
    0x0001: {
# Fault Message: Byte 0
    (0, 0): "ID01 Grid Over Voltage Protection",
    (0, 1): "ID02 Grid Under Voltage Protection",
    (0, 2): "ID03 Grid Over Frequency Protection",
    (0, 3): "ID04 Grid Under Frequency Protection",
    (0, 4): "ID05 PV Under Voltage Protection",
    (0, 5): "ID06 Grid Low Voltage Ride through",
# Reserved bits (0, 6) and (0, 7)
# Fault Message: Byte 1
    (1, 0): "ID09 PV Over Voltage Protection",
    (1, 1): "ID10 PV Input Current Unbalance",
    (1, 2): "ID11 PV Input Mode Configure wrong",
    (1, 3): "ID12 Ground-Fault circuit interrupters Fault",
    (1, 4): "ID13 Phase sequence Fault",
    (1, 5): "ID14 hardware boost over current protection",
    (1, 6): "ID15 Hardware AC over current protection",
    (1, 7): "ID16 The Grid current is too high",
},
    #Fault 2
    0x0002: {
    # Byte2 error messages
    (0, 0): "ID17 The Grid current sampling is error",
    (0, 1): "ID18 The DCI sampling is error",
    (0, 2): "ID19 The Grid voltage sampling is error",
    (0, 3): "ID20 GFCI device sampling is error",
    (0, 4): "ID21 Main chip fault",
    (0, 5): "ID22 Hardware auxiliary power fault",
    (0, 6): "ID23 Bus voltage zero fault",
    (0, 7): "ID24 The output current is not balanced",

    # Byte3 error messages
    (1, 0): "ID25 Bus under voltage protection",
    (1, 1): "ID26 Bus over voltage protection",
    (1, 2): "ID27 Bus voltage unbalance",
    (1, 3): "ID28 The DCI is too high",
    (1, 4): "ID29 The Grid current is too high",
    (1, 5): "ID30 The input current is too high",
    # Bits 6 and 7 in Byte3 are reserved
},
    #Fault 3
    0x0003: {
    # Byte4 reserved messages
    (0, 0): "Reserved 33/41",
    (0, 1): "Reserved 34/42",
    (0, 2): "Reserved 35/43",
    (0, 3): "Reserved 36/44",
    (0, 4): "Reserved 37/45",
    (0, 5): "Reserved 38/46",
    (0, 6): "Reserved 39/47",
    (0, 7): "Reserved 40/48",

    # Byte5 reserved messages
    (1, 0): "Reserved 41/49",
    (1, 1): "Reserved 42/50",
    (1, 2): "Reserved 43/51",
    (1, 3): "Reserved 44/52",
    (1, 4): "Reserved 45/53",
    (1, 5): "Reserved 46/54",
    (1, 6): "Reserved 47/55",
    (1, 7): "Reserved 48/56",
},
    0x0004: {
    # Byte6 error messages
    (0, 0): "ID49 The grid voltage sampling value between the master and slave DSP is Vary widely",
    (0, 1): "ID50 The grid frequency sampling value between the master and slave DSP is Vary widely",
    (0, 2): "ID51 The DCI sampling value between the master and slave DSP is Vary widely",
    (0, 3): "ID52 The GFCI sampling value between the master and slave DSP is Vary widely",
    (0, 4): "ID53 The communication between the master and slave DSP is fail",
    (0, 5): "ID53 The communication between the slave and communication board is fail",
    (0, 6): "ID55 The relay is fault",
    (0, 7): "ID56 The insulation resistance between the PV array and the earth is too low",

    # Byte7 error messages
    (1, 0): "ID57 The inverter temp is too high",
    (1, 1): "ID58 The boost temp is too high",
    (1, 2): "ID59 The environment temp is too high",
    (1, 3): "ID60 The inverter is not connect the PE wire",
    # Bits 4 to 7 in Byte7 are reserved
    (1, 4): "Reserved ID61",
    (1, 5): "Reserved ID62",
    (1, 6): "Reserved ID63",
    (1, 7): "Reserved ID64",
},
    0x0005: {
    # Byte8 error messages
    (0, 0): "ID65 The grid current is too high, and has caused an unrecoverable fault",
    (0, 1): "ID66 The bus voltage is too high, and has caused an unrecoverable fault",
    (0, 2): "ID67 The grid current is unbalanced, and has caused an unrecoverable fault",
    (0, 3): "ID68 The input current is unbalanced, and has caused an unrecoverable fault",
    (0, 4): "ID69 The bus voltage is unbalanced, and has caused an unrecoverable fault",
    (0, 5): "ID70 The grid current is too high, and has caused an unrecoverable fault",
    (0, 6): "ID65 PV Input Mode Configure wrong, and has caused an unrecoverable fault",
    # Bit7 in Byte8 is reserved
    (0, 7): "Reserved 72",

    # Byte9 error messages
    # Bit0 in Byte9 is reserved
    (1, 0): "Reserved 73",
    (1, 1): "ID74 The input current is too high, and has caused an unrecoverable fault",
    (1, 2): "ID75 The EEPROM is faulty",
    (1, 3): "ID76 The EEPROM is faulty",
    (1, 4): "ID77 The relay is faulty, and has caused an unrecoverable fault",
    # Bits 5 to 7 in Byte9 are reserved
    (1, 5): "Reserved ID78",
    (1, 6): "Reserved ID79",
    (1, 7): "Reserved ID80",
    },
    0x0021: {
    # Inverter alert messages for byte0
    (0, 0): "ID81 The inverter has derated because the temperature is too high",
    (0, 1): "ID82 Inverter has derated because the grid frequency is too high",
    (0, 2): "ID83 Inverter has derated by remote control",
    (0, 3): "ID84 Inverter has shut down by remote control",
    # Bits 4 to 7 in byte0 are reserved
    (0, 4): "Reserved ID85",
    (0, 5): "Reserved ID86",
    (0, 6): "Reserved ID87",
    (0, 7): "Reserved ID88",
    # Inverter alert messages for byte1
    (1, 0): "Reserved Reserved",
    (1, 1): "Reserved Reserved",
    (1, 2): "Reserved Reserved",
    (1, 3): "Reserved Reserved",
    (1, 4): "Reserved Reserved",
    (1, 5): "Reserved Reserved",
    (1, 6): "Reserved Reserved",
    (1, 7): "Reserved Reserved",
    },
    0x0022: {
    #Input mode

    },
    0x0023: {
    #Communication board inner message
    # Inverter alert messages for byte0
    (0, 0): "ID81 The inverter has derated because the temperature is too high",
    (0, 1): "ID82 Inverter has derated because the grid frequency is too high",
    (0, 2): "ID83 Inverter has derated by remote control",
    (0, 3): "ID84 Inverter has shut down by remote control",
    # Bits 4 to 7 in byte0 are reserved
    (0, 4): "Reserved ID85",
    (0, 5): "Reserved ID86",
    (0, 6): "Reserved ID87",
    (0, 7): "Reserved ID88",
    #Communication board inner message
    # Inverter alert messages for byte0
    (1, 0): "ID81 The inverter has derated because the temperature is too high",
    (1, 1): "ID82 Inverter has derated because the grid frequency is too high",
    (1, 2): "ID83 Inverter has derated by remote control",
    (1, 3): "ID84 Inverter has shut down by remote control",
    # Bits 4 to 7 in byte0 are reserved
    (1, 4): "Reserved ID85",
    (1, 5): "Reserved ID86",
    (1, 6): "Reserved ID87",
    (1, 7): "Reserved ID88",
    },
}

# Note: Continue to add entries for each byte and bit as per your error message table.
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
    """Process Modbus registers and return values with descriptions."""
    values = []
    for i in range(len(registers)):
        current_address = start_address + i

        if current_address not in REGISTER_MAP:
            continue

        reg_info = REGISTER_MAP.get(current_address, ("Unknown", "", None))
        description, unit, var_type = reg_info

        # Handling unit-less data (e.g., error or alert messages)
        if var_type is None:
            byte0 = registers[i] & 0xFF  # Lower byte
            byte1 = (registers[i] >> 8) & 0xFF  # Higher byte
            values.append(f"{description}: Byte0={byte0}, Byte1={byte1}")
            continue

        # Interpret the register value based on its type
        if var_type in UNIT_MAP:
            if var_type == "Uint":
                real_value = registers[i] * UNIT_MAP[var_type]
            elif var_type == "int":
                real_value = struct.unpack('>h', struct.pack('>H', registers[i]))[0] * UNIT_MAP[var_type]
            values.append(f"{description}: {real_value} {unit}")

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
                rr = await client.read_holding_registers(start_address, 36, slave=1)
                if rr.isError() or isinstance(rr, ExceptionResponse):
                    print(f"Error or Exception while Reading data at address {start_address}: {rr}")
                    continue
                readable_data = process_registers(start_address, rr.registers)
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
