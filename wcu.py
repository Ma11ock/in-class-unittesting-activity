#!/usr/bin/env python

# Unittest

from wc import getSomeInput,split_str,wc

import unittest

class TestStringMethods(unittest.TestCase):
    def test_splitStr1(self):
        self.assertEqual(split_str("This is a string"), ["This", "is", "a", "string"])

    def test_splitStr2(self):
        self.assertEqual(split_str(""), [])

    def test_wc(self):
        self.assertEqual(wc("This is a string"), 4)

    def test_wc1(self):
        self.assertEqual(wc(""), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
