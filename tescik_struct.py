
import struct

# Example response value read from the Modbus register
response_value = 0x000000000000FFFF  # Example value, replace with the actual value you read

# Convert the response value to a list of bits (0s and 1s)
# '>' indicates big-endian, 'Q' is for unsigned long long (U64)
bits = bin(struct.unpack('>Q', struct.pack('>Q', response_value))[0])[2:].zfill(64)

# Iterate over each bit and check the status
for i, bit in enumerate(bits):
    address = 1100 + i  # Calculate the actual Modbus address
    status = "Valid" if bit == '1' else "Invalid"
    print(f"Address {address} is {status}")

# This will print the status of each address in the range based on the bitmask
