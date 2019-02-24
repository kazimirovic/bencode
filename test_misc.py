import unittest

from bencode.misc import *


class MiscEncodingTestCase(unittest.TestCase):
    def test_pack_compact_peer(self):
        self.assertEqual(pack_compact_peer('127.0.0.1', 8080), b'\x7f\x00\x00\x01\x1f\x90')

    def test_pack_compact_peers_list(self):
        self.assertEqual(pack_compact_peers_list((('127.0.0.1', 8080), ('127.0.0.1', 9090))),
                         b'\x7f\x00\x00\x01\x1f\x90\x7f\x00\x00\x01#\x82')

    def test_unpack_compact_peer(self):
        self.assertEqual(unpack_compact_peer(b'\x7f\x00\x00\x01\x1f\x90'), ('127.0.0.1', 8080))

    def test_unpack_compact_peers_list(self):
        self.assertEqual(unpack_compact_peers_list(b'\x7f\x00\x00\x01\x1f\x90\x7f\x00\x00\x01#\x82'),
                         (('127.0.0.1', 8080), ('127.0.0.1', 9090)))

    def test_group(self):
        self.assertListEqual(list(group(b'12341234', group_size=4)), [b'1234', b'1234'])
