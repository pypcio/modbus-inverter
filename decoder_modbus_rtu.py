import struct

def hex_to_floats(hex_string):
    # Convert the hex string to bytes
    byte_data = bytes.fromhex(hex_string)

    # Skip the first 3 bytes (function code and byte count)
    float_bytes = byte_data[3:]

    # Calculate the number of complete 4-byte chunks
    num_floats = len(float_bytes) // 4

    # Iterate over the bytes in chunks of 4 and unpack each to a float
    floats = []
    for i in range(num_floats):
        # Unpack the bytes to a float (big-endian format)
        unpacked_float = struct.unpack('>f', float_bytes[i*4:(i+1)*4])[0]
        floats.append(unpacked_float)

    return floats

# Example usage
# Example usage
hex_data = "010404436aa6e0b434"

if __name__ == "__main__":
    decoded_floats = hex_to_floats(hex_data)
    print(f"Decoded floats: {decoded_floats}")
