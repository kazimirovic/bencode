Bencode
======================================
An implementation of Bencode encoding in Python 3

Usage
------------------
.. code-block:: python

    import bencode
    bencode.encode(OrderedDict((1, 2), (b'eggs', b'spam')))
    bencode.decode(b'i3e')


Type mapping for encoding:

+--------------+--------------+
| Bencode type | Python type  |
+==============+==============+
| Dictionary   | OrderedDict  |
+--------------+--------------+
| List         | list         |
+--------------+--------------+
| Byte string  | bytes        |
+--------------+--------------+
| Integer      | int          |
+--------------+--------------+

Type mapping for decoding:

+--------------+--------------+
| Python type  | Bencode type |
+==============+==============+
| dict         | Dictionary   |
+--------------+--------------+
| list or tuple| List         |
+--------------+--------------+
| bytes        | Byte string  |
+--------------+--------------+
| int          |  Integer     |
+--------------+--------------+

If OrderedDict is passed instead of plain dict, the order will be preserved.

Compact peer encoding
----------------------
This package also includes functions for 'compact' peer encoding as per bep 0023. Though not part of bencode itself, compact peer encoding is often used with it. Mainline DHT and most trackers encode peer information in this format.

Usage:

.. code-block:: python
    from bencode.misc import pack_compact_peers_list, unpack_compact_peers_list

    pack_compact_peers_list((('127.0.0.1', 8080), ('127.0.0.1', 9090)))
    b'\x7f\x00\x00\x01\x1f\x90\x7f\x00\x00\x01#\x82'

    unpack_compact_peers_list(b'\x7f\x00\x00\x01\x1f\x90\x7f\x00\x00\x01#\x82')
    (('127.0.0.1', 8080), ('127.0.0.1', 9090))


