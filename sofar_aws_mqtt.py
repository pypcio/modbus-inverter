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

# Constants for Register Addresses
# INPUT DATA
# STATUS_LOW_BYTE = 0x0000
# MESSAGE_1 = 0x0001
# MESSAGE_2 = 0x0002
# MESSAGE_3 = 0x0003
# MESSAGE_4 = 0x0004
# MESSAGE_5 = 0x0005
# GRID_1_INPUT_VOLTAGE = 0x0006
# GRID_1_INPUT_CURRENT = 0x0007
# GRID_2_INPUT_VOLTAGE = 0x0008
# GRID_2_INPUT_CURRENT = 0x0009
# GRID_1_INPUT_POWER = 0x000A
# GRID_2_INPUT_POWER = 0x000B
# # OPUTPUT DATA
# OUTPUT_ACTIVE_POWER = 0x000C
# OUTPUT_REACTIVE_POWER = 0x000D
# GRID_FREQUENCY = 0x000E
# A_PHASE_VOLTAGE = 0x000F
# A_PHASE_CURRENT = 0x0010
# B_PHASE_VOLTAGE = 0x0011
# B_PHASE_CURRENT = 0x0012
# C_PHASE_VOLTAGE = 0x0013
# C_PHASE_CURRENT = 0x0014
# # INVERTER GENERATOR MESSAGE
# TOTAL_PRODUCTION_HIGH_BYTE = 0x0015
# TOTAL_PRODUCTION_LOW_BYTE = 0x0016
# TOTAL_GENERATION_TIME_HIGH_BYTE = 0x0017
# TOTAL_GENERATION_TIME_LOW_BYTE = 0x0018
# TODAY_PRODUCTION = 0x0019
# TODAY_GENERATION_TIME = 0x001A
# # INVERTER INNER MESSAGE
# INVERTER_MODULE_TEMPERATURE = 0x001B
# INVERTER_INNER_TEMPERATURE = 0x001C
# INVERTER_BUS_VOLTAGE = 0x001D
# PV1_VOLTAGE_SAMPLE = 0x001E
# PV1_CURRENT_SAMPLE = 0x001F
# COUNT_DOWN_TIME = 0x0020
# INVERTER_ALERT_MESSAGE = 0x0021
# INPUT_MODE_LOW_BYTE = 0x0022
# COMMUNICATION_BOARD_INNER_MESSAGE = 0x0023
# INSULATION_PV1_PLUS_GROUND_1 = 0x0024  # Assuming there's a typo and these should be different
# INSULATION_PV1_PLUS_GROUND_2 = 0x0025  # Assuming there's a typo and these should be different
# INSULATION_PV_MINUS_GROUND = 0x0026
# COUNTRY = 0x0027
STATUS_LOW_BYTE = 0x9C41
MESSAGE_1 = 0x9C42
MESSAGE_2 = 0x9C43
MESSAGE_3 = 0x9C44
MESSAGE_4 = 0x9C45
MESSAGE_5 = 0x9C46
GRID_1_INPUT_VOLTAGE = 0x9C47
GRID_1_INPUT_CURRENT = 0x9C48
GRID_2_INPUT_VOLTAGE = 0x9C49
GRID_2_INPUT_CURRENT = 0x9C4A
GRID_1_INPUT_POWER = 0x9C4B
GRID_2_INPUT_POWER = 0x9C4C
# OUTPUT DATA
OUTPUT_ACTIVE_POWER = 0x9C4D
OUTPUT_REACTIVE_POWER = 0x9C4E
GRID_FREQUENCY = 0x9C4F
A_PHASE_VOLTAGE = 0x9C50
A_PHASE_CURRENT = 0x9C51
B_PHASE_VOLTAGE = 0x9C52
B_PHASE_CURRENT = 0x9C53
C_PHASE_VOLTAGE = 0x9C54
C_PHASE_CURRENT = 0x9C55
# INVERTER GENERATOR MESSAGE
TOTAL_PRODUCTION_HIGH_BYTE = 0x9C56
TOTAL_PRODUCTION_LOW_BYTE = 0x9C57
TOTAL_GENERATION_TIME_HIGH_BYTE = 0x9C58
TOTAL_GENERATION_TIME_LOW_BYTE = 0x9C59
TODAY_PRODUCTION = 0x9C5A
TODAY_GENERATION_TIME = 0x9C5B
# INVERTER INNER MESSAGE
INVERTER_MODULE_TEMPERATURE = 0x9C5C
INVERTER_INNER_TEMPERATURE = 0x9C5D
INVERTER_BUS_VOLTAGE = 0x9C5E
PV1_VOLTAGE_SAMPLE = 0x9C5F
PV1_CURRENT_SAMPLE = 0x9C60
COUNT_DOWN_TIME = 0x9C61
INVERTER_ALERT_MESSAGE = 0x9C62
INPUT_MODE_LOW_BYTE = 0x9C63
COMMUNICATION_BOARD_INNER_MESSAGE = 0x9C64
INSULATION_PV1_PLUS_GROUND_1 = 0x9C65
INSULATION_PV1_PLUS_GROUND_2 = 0x9C66
INSULATION_PV_MINUS_GROUND = 0x9C67
COUNTRY = 0x9C68







# Mapping of register addresses to their descriptions and units
REGISTER_MAP = {
    STATUS_LOW_BYTE: {
        "description": "Status",
        "unit": "",
        "sign": "None",
        "multiplier": None,
        'bytes': 'low',
    },
    MESSAGE_1: {
        "description": "Message 1",
        "unit": "",
        "sign": "None",
        "multiplier": None,
        'bytes': 'None',
    },
    MESSAGE_2: {
        "description": "Message 2",
        "unit": "",
        "sign": "None",
        "multiplier": None,
        'bytes': 'None',
    },
    MESSAGE_3: {
        "description": "Message 3",
        "unit": "",
        "sign": "None",
        "multiplier": None,
        'bytes': 'None',
    },
    MESSAGE_4: {
        "description": "Message 4",
        "unit": "",
        "sign": "None",
        "multiplier": None,
        'bytes': 'None',
    },
    MESSAGE_5: {
        "description": "Message 5",
        "unit": "",
        "sign": "None",
        "multiplier": None,
        'bytes': 'None',
    },
    GRID_1_INPUT_VOLTAGE: {
        "description": "Grid A Voltage",
        "unit": "V",
        "sign": "Uint",
        "multiplier": 0.1,
        'bytes': 'None',
    },
    GRID_1_INPUT_CURRENT: {
        "description": "Grid A Current",
        "unit": "A",
        "sign": "int",
        "multiplier": 0.01,
        'bytes': 'None',
    },
    GRID_2_INPUT_VOLTAGE: {
        "description": "Grid B Voltage",
        "unit": "V",
        "sign": "Uint",
        "multiplier": 0.1,
        'bytes': 'None',
    },
    GRID_2_INPUT_CURRENT: {
        "description": "Grid B Current",
        "unit": "A",
        "sign": "int",
        "multiplier": 0.01,
        'bytes': 'None',
    },
    GRID_1_INPUT_POWER: {
        "description": "Grid C Voltage",
        "unit": "V",
        "sign": "Uint",
        "multiplier": 0.01,
        'bytes': 'None',
    },
    GRID_2_INPUT_POWER: {
        "description": "Grid C Current",
        "unit": "A",
        "sign": "int",
        "multiplier": 0.01,
        'bytes': 'None',
    },
    OUTPUT_ACTIVE_POWER: {
        "description": "Output active power",
        "unit": "kW",
        "sign": "Uint",
        "multiplier": 0.01,
        'bytes': 'None',
    },
    OUTPUT_REACTIVE_POWER: {
        "description": "Output reactive power",
        "unit": "kVar",
        "sign": "int",
        "multiplier": 0.01,
        'bytes': 'None',
    },
    A_PHASE_VOLTAGE: {
        "description": "A-phase voltage",
        "unit": "V",
        "sign": "Uint",
        "multiplier": 0.1,
        'bytes': 'None',
    },
    A_PHASE_CURRENT: {
        "description": "A-phase current",
        "unit": "A",
        "sign": "Uint",
        "multiplier": 0.01,
        'bytes': 'None',
    },
    B_PHASE_VOLTAGE: {
        "description": "B-phase voltage",
        "unit": "V",
        "sign": "Uint",
        "multiplier": 0.1,
        'bytes': 'None',
    },
    B_PHASE_CURRENT: {
        "description": "B-phase current",
        "unit": "A",
        "sign": "Uint",
        "multiplier": 0.01,
        'bytes': 'None',
    },
    C_PHASE_VOLTAGE: {
        "description": "C-phase voltage",
        "unit": "V",
        "sign": "Uint",
        "multiplier": 0.1,
        'bytes': 'None',
    },
    C_PHASE_CURRENT: {
        "description": "C-phase current",
        "unit": "A",
        "sign": "Uint",
        "multiplier": 0.01,
        'bytes': 'None',
    },
    TOTAL_PRODUCTION_HIGH_BYTE: {
        "description": "Total production high-byte",
        "unit": "kWh",
        "sign": "Uint",
        "multiplier": 1,
        'bytes': 'high',
    },
    TOTAL_PRODUCTION_LOW_BYTE: {
        "description": "Total production low-byte",
        "unit": "kWh",
        "sign": "Uint",
        "multiplier": 1,
        'bytes': 'low',
    },
    TOTAL_GENERATION_TIME_HIGH_BYTE: {
        "description": "Total generation time high-byte",
        "unit": "hour",
        "sign": "Uint",
        "multiplier": 1,
        'bytes': 'high',
    },
    TOTAL_GENERATION_TIME_LOW_BYTE: {
        "description": "Total generation time low-byte",
        "unit": "hour",
        "sign": "Uint",
        "multiplier": 1,
        'bytes': 'low',
    },
    TODAY_PRODUCTION: {
        "description": "Today production",
        "unit": "kWh",
        "sign": "Uint",
        "multiplier": 0.01
    },
    TODAY_GENERATION_TIME: {
        "description": "Today generation time",
        "unit": "Minute",
        "sign": "Uint",
        "multiplier": 1
    },
    INVERTER_MODULE_TEMPERATURE: {
        "description": "Inverter module temperature",
        "unit": "°C",
        "sign": "int",
        "multiplier": 1  # Assuming a direct representation without multiplier
    },
    INVERTER_INNER_TEMPERATURE: {
        "description": "Inverter inner temperature",
        "unit": "°C",
        "sign": "int",
        "multiplier": 1
    },
    INVERTER_BUS_VOLTAGE: {
        "description": "Inverter Bus voltage",
        "unit": "V",
        "sign": "Uint",
        "multiplier": 0.1
    },
    PV1_VOLTAGE_SAMPLE: {
        "description": "PV1 voltage sample by slave CPU",
        "unit": "V",
        "sign": "Uint",
        "multiplier": 0.1
    },
    PV1_CURRENT_SAMPLE: {
        "description": "PV1 current sample by slave CPU",
        "unit": "A",
        "sign": "Uint",
        "multiplier": 0.01
    },
    COUNT_DOWN_TIME: {
        "description": "Count-down time",
        "unit": "",  # Unit not specified
        "sign": "Uint",
        "multiplier": 1  # Assuming a direct representation without multiplier
    },
    INVERTER_ALERT_MESSAGE: {
        "description": "Inverter alert message",
        "unit": "",  # Unit not specified
        "sign": "None",
        "multiplier": None  # Assuming a direct representation without multiplier
    },
    INPUT_MODE_LOW_BYTE: {
        "description": "Input mode",
        "unit": "",  # Unit not specified, could be enumeration
        "sign": "None",
        "multiplier": None,
        'bytes': 'low',
    },
    COMMUNICATION_BOARD_INNER_MESSAGE: {
        "description": "Communication board inner message",
        "unit": "",  # Unit not specified
        "sign": "None",
        "multiplier": None  # Assuming a direct representation without multiplier
    },
    # CHARGE_DISCHARGE_POWER: {
    #     "description": "Charge/Discharge Power",
    #     "unit": "kW",
    #     "sign": "int",
    #     "multiplier": 1
    # },
    # BATTERY_VOLTAGE: {
    #     "description": "Battery Voltage",
    #     "unit": "V",
    #     "sign": "int",
    #     "multiplier": 1
    # },
    # BATTERY_CHARGE_DISCHARGE_CURRENT: {
    #     "description": "Battery Charge/Discharge Current",
    #     "unit": "A",
    #     "sign": "",
    #     "multiplier": None
    # },
    # THE_RESIDUAL: {
    #     "description": "The Residual",
    #     "unit": "%",
    #     "sign": "",
    #     "multiplier": None
    # },
    # FAULT_MESSAGE: {
    #     "description": "Fault message",
    #     "unit": "",
    #     "sign": "",
    #     "multiplier": None
    # },
    # HEAT_SINK_VALUE: {
    #     "description": "Heat Sink Value",
    #     "unit": "C",
    #     "sign": "",
    #     "multiplier": None
    # }
}

error_codes = {
    # Fault 1
    MESSAGE_1: {
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
    # Fault 2
    MESSAGE_2: {
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
    # Fault 3
    MESSAGE_3: {
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
    # Fault 4
    MESSAGE_4: {
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
    # Fault 5
    MESSAGE_5: {
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
    # Inverter alert message Message
    INVERTER_ALERT_MESSAGE: {
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
    # STATUS_LOW_BYTE: {
    #     0x00: "wait",
    #     0x01: "check",
    #     0x02: 'normal',
    #     0x03: 'Fault',
    #     0x04: 'Permanent'
    # },
    # INPUT_MODE_LOW_BYTE: {
    #     0x00: "in parallel",
    #     0x01: "in dependent",
    # },
    COMMUNICATION_BOARD_INNER_MESSAGE: {
        # Communication board inner message
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
        # Communication board inner message
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

byte_messages={
    STATUS_LOW_BYTE: {
        0x00: "wait",
        0x01: "check",
        0x02: 'normal',
        0x03: 'Fault',
        0x04: 'Permanent'
    },
    INPUT_MODE_LOW_BYTE: {
        0x00: "in parallel",
        0x01: "in dependent",
    },
}
# Note: Continue to add entries for each byte and bit as per your error message table.
# List of addresses to read
# address_list = [0x0000, 0x0039]
address_list = [0x9C41]


def process_registers_into_json_data(start_address, registers):
    """Process Modbus registers and return dictionary of values with descriptions,
    including handling of messages and alerts, distinguishing between high, low, or both bytes,
    and decoding messages based on both bitwise and byte-level information."""
    # global scaled_value
    data = {}
    for i in range(len(registers)):
        current_address = start_address + i

        if current_address not in REGISTER_MAP:
            continue  # Skip if the register address is not found in the map

        reg_info = REGISTER_MAP[current_address]
        description = reg_info["description"]
        unit = reg_info["unit"]
        sign = reg_info.get("sign", "None")
        multiplier = reg_info.get("multiplier", 1)
        byte_orientation = reg_info.get('bytes', 'None')  # Default to 'None' if not specified

        # Prepare the raw_value for unpacking based on byte orientation
        raw_value = struct.pack('>H', registers[i])

        if sign in ["Uint", "int"]:
            fmt = '>B' if byte_orientation in ['low', 'high'] else '>H'
            if byte_orientation == 'low':
                value = struct.unpack_from(fmt, raw_value, 0)[0]  # Unpack low byte
            elif byte_orientation == 'high':
                value = struct.unpack_from(fmt, raw_value, 1)[0]  # Unpack high byte
            else:
                value = struct.unpack(fmt, raw_value)[0]  # Unpack full 16-bit register
            scaled_value = value * multiplier
        elif sign == "float":
            # Placeholder for float handling; may require combining registers
            scaled_value = "Float handling needs multi-register context"
        elif sign == 'None':
            if byte_orientation in ['low', 'high']:
                # Process entire byte messages
                byte_index = 0 if byte_orientation == 'low' else 1
                byte_value = struct.unpack_from('>B', raw_value, byte_index)[0]
                if current_address in byte_messages:
                    scaled_value = byte_messages[current_address].get(byte_value, "Unknown message")
                    unit = ""  # Reset unit for messages
            else:
                messages = []
                # Unpack the register into two separate bytes for detailed bitwise checking
                byte0, byte1 = struct.unpack('>BB', raw_value)  # Unpack register into two bytes

                # Check both bytes (byte0 and byte1) for messages
                for byte_index, byte_value in enumerate([byte0, byte1]):
                    for bit_index in range(8):
                        if byte_value & (1 << bit_index):
                            # Construct the key with byte_index and bit_index to match the error_codes structure
                            key = (byte_index, bit_index)
                            # Check if this specific bit in this byte has a corresponding message
                            if key in error_codes.get(current_address, {}):
                                messages.append(error_codes[current_address][key])

                scaled_value = "; ".join(messages) if messages else "No errors"
                unit = ""  # Reset unit for messages

        else:
            continue  # Skip if sign type is unsupported

        data[current_address] = {
            "description": description,
            "value": scaled_value,
            "unit": unit,
            'byte_orientation': byte_orientation,
        }

    return data


def format_data_for_database(processed_data):
    """Format the processed data into the database JSON structure."""
    timestamp = datetime.now().isoformat()
    formatted_data = {timestamp: {}}

    for address, values in processed_data.items():
        formatted_data[timestamp][address] = values

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
    liczba = 0
    print("connected,parsing data")
    try:
        all_data = {}  # Dictionary to accumulate all readable data
        while True:
            for start_address in address_list:  # List of starting addresses
                rr = await client.read_holding_registers(start_address, 12, slave=7)
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


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()

    asyncio.run(
        run_async_simple_client("tcp", port="502", host='192.168.1.9', address_list=address_list), debug=False
    )  # pragma: no cover
