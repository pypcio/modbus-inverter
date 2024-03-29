#!/usr/bin/env python3
import asyncio
import struct
# from pymodbus.client import AsyncModbusTcpClient as ModbusClient
from datetime import datetime
import json
import paho.mqtt.client as mqtt
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse,
    Framer,
    ModbusException,
    pymodbus_apply_logging_config,
)

# MQTT Broker Settings
MQTT_BROKER = 'localhost'  # Example: 'localhost' or 'broker.hivemq.com'
MQTT_PORT = 1883  # Default port for MQTT
MQTT_TOPIC = 'energy_meter_rut3/data'

# Constants for Register Addresses
VOLTAGE_L1 = 0x00
VOLTAGE_L2 = 0x02
VOLTAGE_L3 = 0x04
CURRENT_L1 = 0x06
CURRENT_L2 = 0x08
CURRENT_L3 = 0x0A
FREQUENCY_SUPPLY = 0x46

# Modified Register Map
REGISTER_MAP = {
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
list = [0x00, 0x06, 0x46]

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
        if sign == "float":
            scaled_value = struct.unpack('>f', raw_value)[0] * multiplier
        else:
            continue  # Simplified for example; extend as needed
        data[current_address] = {
            "description": description,
            "value": scaled_value,
            "unit": unit
        }
    return data

def format_data_for_database(processed_data):
    """Format the processed data into the database JSON structure."""
    timestamp = datetime.now().isoformat()
    formatted_data = {timestamp: processed_data}
    return formatted_data

def mqtt_publish(client, topic, message):
    """Publish data to MQTT topic."""
    client.publish(topic, message)
    print(f"Data published to MQTT topic {topic}")


async def run_async_simple_client(comm, host, port, framer=Framer.SOCKET, address_list=[]):
    """Run async client and publish data to MQTT."""
    # MQTT Client setup
    mqtt_client = mqtt.Client()
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    print("Connecting to mqtt server")

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
                rr = await client.read_input_registers(start_address, 6, slave=1)
                if rr.isError() or isinstance(rr, ExceptionResponse):
                    print(f"Error or Exception while Reading data at address {start_address}: {rr}")
                    continue

                processed_data = process_registers_into_json_data(start_address, rr.registers)
                all_data.update(processed_data)
                # Update all_data with the new database_data
            database_data = format_data_for_database(all_data)
            json_data = json.dumps(database_data)
            mqtt_publish(mqtt_client, MQTT_TOPIC, json_data)
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
        mqtt_client.disconnect()

if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    asyncio.run(
        run_async_simple_client("tcp", port="503", host='192.168.1.3', address_list=list), debug=False
    )  # pragma: no cover
