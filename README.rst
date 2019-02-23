Bencode
======================================

An implementation of Bencode encoding in Python 3

Installation
------------------
From PyPI:

.. code-block:: bash

    pip install torrent-bencode


Usage
------------------

.. code-block:: python

    import bencode
    bencode.encode([b'spam', b'eggs'])
    bencode.decode(b'l4:spam4:eggse')
   

Types
------------------
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

If an OrderedDict is passed rather than a plain dict, the order of items will be preserved.
