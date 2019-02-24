import struct
from socket import inet_ntoa, inet_aton
from typing import Tuple, Sequence


def pack_compact_peer(ip: str, port: int):
    ip = inet_aton(ip)
    return struct.pack('!4sH', ip, port)


def pack_compact_peers_list(peers_list):
    return b''.join([pack_compact_peer(*peer) for peer in peers_list])


def unpack_compact_peer(data: bytes) -> Tuple[str, int]:
    ip, port = struct.unpack('!4sH', data)
    ip = inet_ntoa(ip)
    return ip, port


def unpack_compact_peers_list(data: bytes) -> Sequence[Tuple[str, int]]:
    return tuple(unpack_compact_peer(data) for data in group(data, 6))


def group(sequence, group_size):
    return (sequence[i:i + group_size] for i in range(0, len(sequence), group_size))
