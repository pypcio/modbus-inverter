
import struct
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder

def generate_modbus_request(address, data_type, value=None, scale=1):
    # Create a payload builder
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG)

    # Add data to the payload based on the data type
    if data_type == 'uint':
        if value is not None:
            builder.add_16bit_uint(int(value / scale))
        else:
            builder.add_16bit_uint(0)  # Dummy value for request example
    else:  # int
        if value is not None:
            builder.add_16bit_int(int(value / scale))
        else:
            builder.add_16bit_int(0)  # Dummy value for request example

    # Get the payload
    payload = builder.to_registers()
    request = struct.pack('>HH', address, payload[0])
    return request

# Define the register addresses and their respective types
registers = {
    0x0024: ('Grid A Voltage', 'uint', 0.1),
    0x0207: ('Grid A Current', 'int', 0.01),
    0x0208: ('Grid B Voltage', 'uint', 0.1),
    0x0209: ('Grid B Current', 'int', 0.01),
    0x020A: ('Grid C Voltage', 'uint', 0.1),
    0x020B: ('Grid C Current', 'int', 0.01),
    0x020C: ('Grid Frequency', 'uint', 0.01)
}
if __name__ == '__main__':
    # Generate and print example requests for each register
    for address, (name, data_type, scale) in registers.items():
        request = generate_modbus_request(address, data_type)
        print(f"Example request for {name} (Address: {hex(address)}): {request}")
