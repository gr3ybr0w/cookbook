# converts to bytes despite being given strings or bytes


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8', errors='strict')
    else:
        value = bytes_or_str

    # instance of bytes
    return value
