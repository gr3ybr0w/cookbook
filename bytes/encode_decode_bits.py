# encode text into bytes
def encode_string_to_bits(string: str):
    return bin(int.from_bytes(string.encode(), 'big'))


# decode bytes to text
def decode_bits_to_string(bits: str):
    n = int(bits, 2)
    o = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return o

