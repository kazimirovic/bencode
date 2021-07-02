from collections import OrderedDict
from io import BytesIO
from typing import Union, List, Any, BinaryIO, Tuple


def encode(value: Union[int, dict, bytes, List[Any], Tuple[Any]]) -> bytes:
    # noinspection PyTypeChecker
    """
    Recursively encodes any supported value, raises ValueError if a value of an unsupported type is supplied.

    >>> encode(3)
    b'i3e'

    >>> encode(b'spam')
    b'4:spam'

    >>> encode([b'spam', b'eggs'])
    b'l4:spam4:eggse'

    >>> encode(OrderedDict(((b'cow', b'moo'), (b'spam', b'eggs'))))
    b'd3:cow3:moo4:spam4:eggse'

    >>> encode("python strings are not supported, supply bytes")
    Traceback (most recent call last):
    ...
    ValueError: Only int, bytes, list or dict can be encoded, got str

    :param value:
    :return: bencoded string
    """
    if isinstance(value, dict):
        return b'd%be' % b''.join([encode(k) + encode(v) for k, v in value.items()])
    if isinstance(value, list) or isinstance(value, tuple):
        return b'l%be' % b''.join([encode(v) for v in value])
    if isinstance(value, int):
        return b'i%ie' % value
    if isinstance(value, bytes):
        return b'%i:%b' % (len(value), value)

    raise ValueError("Only int, bytes, list or dict can be encoded, got %s" % type(value).__name__)


def decode(data: bytes):
    """
    Tries to decode bencoded data. Raises InvalidBencode.

    >>> decode(b'i3e')
    3

    >>> decode(b'4:spam')
    b'spam'

    >>> decode(b'l4:spam4:eggse')
    [b'spam', b'eggs']

    >>> decode(b'd3:cow3:moo4:spam4:eggse')
    OrderedDict([(b'cow', b'moo'), (b'spam', b'eggs')])

    >>> decode(b"d3:cow3:m")
    Traceback (most recent call last):
    ...
    bencode.InvalidBencode: EOF reached while parsing


    :param data:
    :return:
    """
    return decode_from_io(BytesIO(data))


def decode_from_io(f: BinaryIO):
    """
    Tries to decode bencoded data from a file-like object. Raises InvalidBencode.
    :param f: file-like object
    :return:
    """
    char = f.read(1)
    if char == b'd':
        dict_ = OrderedDict()
        while True:
            position = f.tell()
            char = f.read(1)
            if char == b'e':
                return dict_
            if char == b'':
                raise InvalidBencode.eof()

            f.seek(position)
            key = decode_from_io(f)
            dict_[key] = decode_from_io(f)

    if char == b'l':
        list_ = []
        while True:
            position = f.tell()
            char = f.read(1)
            if char == b'e':
                return list_
            if char == b'':
                raise InvalidBencode.eof()
            f.seek(position)
            list_.append(decode_from_io(f))

    if char == b'i':
        digits = b''
        while True:
            char = f.read(1)
            if char == b'e':
                break
            if char == b'':
                raise InvalidBencode.eof()
            if not char.isdigit():
                # Allow '-' as the first character
                if char != b'-' or digits != b'':
                    raise InvalidBencode.at_position('Expected int, got %s' % str(char), f.tell())
            digits += char
        return int(digits)

    if char.isdigit():
        digits = char
        while True:
            char = f.read(1)
            if char == b':':
                break
            if char == b'':
                raise InvalidBencode
            digits += char
        length = int(digits)
        string = f.read(length)
        return string

    raise InvalidBencode.at_position('Unknown type : %s' % char, f.tell())


class InvalidBencode(Exception):
    @classmethod
    def at_position(cls, error, position):
        return cls("%s at position %i" % (error, position))

    @classmethod
    def eof(cls):
        return cls("EOF reached while parsing")
