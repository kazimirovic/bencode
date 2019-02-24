import bencode

import doctest

doctest.testmod(bencode)

import unittest
import test_misc

if __name__ == '__main__':
    unittest.main(defaultTest='test_misc')
