import struct
import crcmod.predefined

def calculate_modbus_crc(message):
    crc16 = crcmod.predefined.Crc('modbus')
    crc16.update(message)
    return crc16.digest()

def create_modbus_request(slave_id, function_code, start_address, quantity):
    # Create the request without CRC
    # Format: Slave ID (8 bit) | Function Code (8 bit) | Start Address (16 bit) | Quantity (16 bit)
    request = struct.pack('>BBHH', slave_id, function_code, start_address, quantity)
    # Calculate and append CRC
    crc = calculate_modbus_crc(request)
    return request + crc

# --------  --------  CONFIG --------  --------
# Slave ID for the inverter (typically 1 for Modbus)
slave_id = 1

# Function code for reading input registers
function_code = 0x03

# Define the register addresses (start at 0x0206, end at 0x020C)
registers = range(0x0206, 0x020D)
#      --------  --------  --------  --------
def format_request(request):
    # Convert the request to a hex string and insert spaces between bytes
    return ' '.join(f'{b:02X}' for b in request)

# Generate and print formatted raw Modbus RTU requests for each register
for reg in registers:
    request = create_modbus_request(slave_id, function_code, reg, 1)
    formatted_request = format_request(request)
    print(f"Formatted Modbus RTU request for register {hex(reg)}: {formatted_request}")

