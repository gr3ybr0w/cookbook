# function that returns a string instance despite being given
# strings or bytes


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8', errors='strict')
    else:
        value = bytes_or_str

    # Instance of str
    return value
