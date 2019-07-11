import base64
import struct


def pack_structure(*args, url_safe=False, structure_pattern=None, encode_encoding=None, decode_encoding=None):
    if structure_pattern is not None:
        bytes_result = struct.pack(structure_pattern, *args)
    else:
        bytes_result = b''
        str_encode = (lambda x: x.encode(encode_encoding)) if encode_encoding else (lambda x: x.encode())
        for arg in args:
            if isinstance(arg, int):
                bytes_result += struct.pack('<q', arg)
            elif isinstance(arg, float):
                bytes_result += struct.pack('<d', arg)
            elif isinstance(arg, bool):
                bytes_result += struct.pack('<?', arg)
            elif isinstance(arg, str):
                bytes_result += str_encode(arg)
            else:
                bytes_result += str_encode(str(arg))

    bytes_base64 = base64.urlsafe_b64encode(bytes_result) if url_safe else base64.b64encode(bytes_result)
    return bytes_base64.decode(decode_encoding) if decode_encoding is not None else bytes_base64
