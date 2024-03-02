#!/usr/bin/env python3
"""Asynchronous Modbus client for reading data."""

from sofar_solar_modbus_map import register_mask_list, register_map, error_codes
from config import config as settingsConfiguration
from pymodbus.client.tcp import AsyncModbusTcpClient
from pymodbus.client.udp import AsyncModbusUdpClient
from pymodbus.client.serial import AsyncModbusSerialClient
from pymodbus.client.tls import AsyncModbusTlsClient
from dataConext import DataBlock, DataContextList
import asyncio
import struct
import pymodbus.client as ModbusClient
from pymodbus import (
    ExceptionResponse, Framer, ModbusException,
    pymodbus_apply_logging_config)

# params
MAX_COUNT = 15
MAX_RECONNECT_DELAY= 20
TIMEOUT = 3
RETRIES = 3


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
        self.last_processed_mask_address = None
        self.decoded_data = {}
        self.groupCheck = []
        # self.log_error =[]
        # self.log_critical = []
        # self.instructiones

    def get_counter(self):
        return self.__counter

    def set_counter(self, new_counter):
        self.__counter = new_counter

    def increment_counter(self):
        self.__counter += 1

    def log_error(self):
        pass

    def log_critical(self):
        pass

    async def handle_error(self, error, action="default", **kwargs):
        """
        Handles errors that occur during Modbus operations.

        :param error: The exception that was caught.
        :param action: The action to take in response to the error. This could be 'retry', 'log', 'alert', etc.
        :param kwargs: Additional keyword arguments that might be necessary for handling specific actions.
        """
        if action == "retry":
            retries = kwargs.get("retries", RETRIES)
            timeout = kwargs.get("timeout", TIMEOUT)  # Ensure TIMEOUT is defined somewhere
            reconnect_delay = kwargs.get("reconnect_delay", 1)  # Assuming this is your backoff strategy's initial delay
            operation = kwargs.get("operation")
            operation_kwargs = kwargs.get("operation_kwargs", {})
            for attempt in range(retries):
                await asyncio.sleep(reconnect_delay)
                reconnect_delay = min(reconnect_delay * 2, MAX_RECONNECT_DELAY)
                # print("Attempt: ", attempt)
                try:
                    if not self.client.connected or attempt == 1:
                        #reconnect:
                        self.client.close()
                        await self.connect(timeout=timeout, retries=retries, reconnect_delay=reconnect_delay)
                        await operation(**operation_kwargs)
                        return  # Operation successful, exit retry loop
                    else:
                            await operation(**operation_kwargs)
                            return  # Operation successful, exit retry loop
                except Exception as retry_error:
                    # self.log_error(retry_error)  # Implement this method for appropriate logging

                    if attempt == retries - 1:
                        print("To sie porobilo")
                        # Handle the final failure case here
                        # self.log_critical(f"All retries failed. Last error: {retry_error}")

        elif action == "log":
            # Log the error to a file or logging system
            print(f"Logging error: {error}")
        elif action == "alert":
            # Send an alert (email, SMS, etc.) about the error
            print(f"Alerting: {error}")
        else:
            # Default error handling
            print(f"Error encountered: {error}")

    async def connect(self, timeout=1, retries=3, retry_on_empty=False, close_comm_on_error=False, reconnect_delay=0.1):
        try:
            if self.debug and self.get_counter() == 0:
                pymodbus_apply_logging_config("DEBUG")
                print("get client")
            if self.comm == "tcp":
                self.client = AsyncModbusTcpClient(
                    host=self.host,
                    port=self.port,
                    framer=self.framer,
                    timeout=timeout,
                    retries=retries,
                    retry_on_empty=retry_on_empty,
                    close_comm_on_error=close_comm_on_error,
                    reconnect_delay=reconnect_delay,
                    # strict=True,
                    # source_address=("localhost", 0),
                )
            elif self.comm == "udp":
                self.client = AsyncModbusUdpClient(
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
                self.client = AsyncModbusSerialClient(
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
                self.client = AsyncModbusTlsClient(
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
                print(f"Unknown client {self.comm} selected")
                return
            await self.client.connect()
            if self.client.connected and self.debug:
                print("Connected, parsing data")
            else:
                # Decide on further action: retry, alert, etc.
                await self.handle_error(error="Failed to connect", action="alert")

        except Exception as e:
            await self.handle_error(error=e, action="alert")

    async def read_registers(self, start_address, count):
        if self.client is None or not self.client.connected:
            print("Modbus client is not connected.")
            return []
        response = await self.client.read_holding_registers(start_address, count=count, slave=self.slave_id)
        if not response.isError():
            return response.registers
        else:
            print(f"Error reading registers starting at address {start_address}: {response}")
            return []

    def group_addresses(self):
        if self.get_counter() == 0:
            self.temporary_list.sort()
        groups = []
        start = self.temporary_list[0]
        last = start

        for address in self.temporary_list[1:]:
            if address - last > 1 or (address - start) >= MAX_COUNT:
                groups.append((start, last - start + 1))
                start = address
            last = address
        groups.append((start, last - start + 1))
        return groups

    async def schedule_transactions(self):
        groups = self.group_addresses()
        """ filter out successful transactions for another retry """
        if len(self.groupCheck) != 0:
            groups = [item for item in self.groupCheck if item not in groups]

        for start_address, count in groups:
            response_read = await self.read_registers(start_address, count)
            self.decode_registers(start_address, response_read)  # <--- maybe try decode using threads
            self.groupCheck.append((start_address, count))
        if self.debug:
            print("\nComplete Data:")
            for address, data in self.decoded_data.items():
                print(f"  {address}: {data}")
        # await asyncio.sleep(10)

    async def read_and_process_address_masks(self, mask_length=4):
        """Read and process address masks to update the list of active addresses."""
        active_addresses = set()
        if self.last_processed_mask_address is None:
            start_index = 0
        else:
            try:
                start_index = register_mask_list.index(self.last_processed_mask_address) + 1
            except ValueError:
                start_index = 0  # Reset to 0 if last_processed_mask_address not in list

        for mask_start_address in register_mask_list[start_index:]:
            try:
                rr = await self.client.read_holding_registers(address=mask_start_address, count=mask_length,
                                                              slave=self.slave_id)
                if not rr.isError():
                    mask_value = self.combine_registers_to_u64(rr.registers)
                    for i in range(64):
                        if mask_value & (1 << i):
                            active_address = mask_start_address + i  # Adjust this line if the calculation of active_address is different
                            active_addresses.add(active_address)
                    self.last_processed_mask_address = mask_start_address
            except Exception as e:
                # self.log_error(e)
                print(f"Failed reading address mask at {mask_start_address}. Error: {e}")
                break  # Exit the loop on error
            # await asyncio.sleep(delay)
        # Update temporary_list with active addresses only
        self.temporary_list = [addr for addr in self.temporary_list if addr in active_addresses]

        # Reset last_processed_mask_address if we've reached the end of register_mask_list
        if self.last_processed_mask_address == register_mask_list[-1]:
            self.last_processed_mask_address = None

    async def read(self):
        """Read data from the Inverter."""
        await self.connect()
        if self.client is None or not self.client.connected:
            print("Unable to connect to the client.")
            return
        elif self.get_counter() == 0:
            try:
                # checking address status using mask
                await self.read_and_process_address_masks()
            except Exception as e:
                print(f"Error processing address masks: {e}")
                await self.handle_error(
                    error=e,
                    action="retry",
                    timeout=TIMEOUT,
                    retry=RETRIES,
                    operation=self.read_and_process_address_masks,
                    # operation_kwargs={'timeout': TIMEOUT, 'retries': RETRIES}
                )
        try:
            # group, read, and process addreses:
            await self.schedule_transactions()
            self.increment_counter()
            self.groupCheck.clear()
            self.client.close()
            # await asyncio.sleep(10)
        except Exception as e:
            print(f"Error reading address: {e}")
            await self.handle_error(
                error=e,
                action="retry",
                timeout=TIMEOUT,
                retry=RETRIES,
                operation=self.schedule_transactions,
                # operation_kwargs={'delay': TIMEOUT}
            )

        # Further operations based on updated self.temporary_list

    def process_instruction(self, instruction):
        # do some processing stuff
        print('Siema, procesuje')
        address = instruction['address']
        value = instruction['value']
        return address, value

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

    @staticmethod
    def combine_registers_to_u64(registers):
        """Combine four 16-bit registers into a single U64 value, assuming big-endian byte order."""
        return (registers[0] << 48) | (registers[1] << 32) | (registers[2] << 16) | registers[3]


# poza klasa!!@!@!@!@!@
async def main(config):
    # for slave in config["slaves"]:
    reader1 = AsyncModbusSlave(config)
    while True:
        await reader1.read()
        print("counter: ", reader1.get_counter())
        await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(main(settingsConfiguration))
