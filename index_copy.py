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

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from datetime import datetime

cred = credentials.Certificate(r"D:\_robota_ojciec\iot-modbus-v1-firebase-adminsdk-be4xd-93cd841318.json")
firebase_admin.initialize_app(cred)
print("Connected to Firebase Firestore.")


def send_data_to_firebase(data):
    db = firestore.client()
    doc_ref = db.collection('energy-meter-rut3').document()
    doc_ref.set(data)
    print("Data successfully added to Firestore.")
    # ref = db.reference('/your/firebase/data/path')
    # ref.set(json.loads(json.dumps(data)))


# Constants for Register Addresses
VOLTAGE_L1 = 0x00
VOLTAGE_L2 = 0x02
VOLTAGE_L3 = 0x04
CURRENT_L1 = 0x06
CURRENT_L2 = 0x08
CURRENT_L3 = 0x0A
POWER=0x0B
FREQUENCY_SUPPLY = 0x46

# Modified Register Map
REGISTER_MAP = {
POWER: {
        "description": "Power",
        "unit": "kW",
        "sign": "float",
        "multiplier": 1
    },
    VOLTAGE_L1: {
        "description": "Napięcie fazowe L1 (L-N)",
        "unit": "V",
        "sign": "float",
        "multiplier": 1
    },
    VOLTAGE_L2: {
        "description": "Napięcie fazowe L2 (L-N)",
        "unit": "V",
        "sign": "float",
        "multiplier": 1
    },
    VOLTAGE_L3: {
        "description": "Napięcie fazowe L3 (L-N)",
        "unit": "V",
        "sign": "float",
        "multiplier": 1
    },
    CURRENT_L1: {
        "description": "Natężenie prądu L1",
        "unit": "A",
        "sign": "float",
        "multiplier": 1
    },
    CURRENT_L2: {
        "description": "Natężenie prądu L2",
        "unit": "A",
        "sign": "float",
        "multiplier": 1
    },
    CURRENT_L3: {
        "description": "Natężenie prądu L3",
        "unit": "A",
        "sign": "float",
        "multiplier": 1
    },
    FREQUENCY_SUPPLY: {
        "description": "Częstotliwość napięć zasilania",
        "unit": "Hz",
        "sign": "float",
        "multiplier": 1
    }
}

# list = [0x00, 0x02, 0x04, 0x06, 0x08, 0x0A, 0x46]
list = [0x00, 0x06,0x0B,0x1A,0x1B,0x1C,0x2,0x25,0x31, 0x46,]


# def process_registers(start_address, registers):
#     """Process Modbus registers and return list of values with descriptions."""
#     values = []
#     for i in range(0, len(registers), 2):
#         current_address = start_address + i // 2
#
#         if current_address not in REGISTER_MAP:
#             continue  # Skip this register if not found
#
#         # Fetch the description, unit, and variable type
#         reg_info = REGISTER_MAP.get(current_address, ("Unknown", "", None))
#         description, unit, var_type = reg_info if len(reg_info) == 3 else (*reg_info, None)
#
#         raw_value = struct.pack('>HH', registers[i], registers[i + 1])
#
#         scaled_value=struct.unpack('>f', raw_value)[0]
#         values.append(f"{description}: {scaled_value:.2f} {unit}")
#
#     return values
def process_registers_into_json_data(start_address, registers):
    """Process Modbus registers and return dictionary of values with descriptions."""
    data = {}
    for i in range(0, len(registers), 2):
        current_address = start_address + i

        if current_address not in REGISTER_MAP:
            continue  # Skip this register if not found

        reg_info = REGISTER_MAP[current_address]
        description = reg_info["description"]
        unit = reg_info["unit"]
        sign = reg_info["sign"]
        multiplier = reg_info["multiplier"]

        raw_value = struct.pack('>HH', registers[i], registers[i + 1])

        if sign == "Uint":
            scaled_value = struct.unpack('>H', raw_value[:2])[0] * multiplier
        elif sign == "int":
            scaled_value = struct.unpack('>h', raw_value[:2])[0] * multiplier
        elif sign == "float":
            scaled_value = struct.unpack('>f', raw_value)[0] * multiplier
        else:
            raise ValueError(f"Unsupported sign type: {sign}")

        data[current_address] = {
            "description": description,
            "value": scaled_value,
            "unit": unit
        }

    return data


def format_data_for_database(processed_data):
    """Format the processed data into the database JSON structure."""
    timestamp = datetime.now().isoformat()  # Get the current timestamp in ISO 8601 format
    formatted_data = {timestamp: {}}  # Create a dictionary with a timestamped key

    for address, values in processed_data.items():
        # Ensure address is a string to avoid JSON serialization issues
        formatted_data[timestamp][str(address)] = values

    return formatted_data


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
            framer=framer.RTU,
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
        all_data = {}  # Dictionary to accumulate all readable data
        while True:
            for start_address in address_list:  # List of starting addresses
                rr = await client.read_input_registers(start_address, 2, slave=1)
                if rr.isError() or isinstance(rr, ExceptionResponse):
                    print(f"Error or Exception while Reading data at address {start_address}: {rr}")
                    continue

                processed_data = process_registers_into_json_data(start_address, rr.registers)
                all_data.update(processed_data)
                # Update all_data with the new database_data
            database_data = format_data_for_database(all_data)
            # send data to firebase:
            # send_data_to_firebase(database_data)
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


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    asyncio.run(
        run_async_simple_client("tcp", port="503", host='192.168.1.3', address_list=list), debug=False
    )  # pragma: no cover
