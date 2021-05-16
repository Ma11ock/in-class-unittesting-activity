#!/usr/bin/env python

from palindrome import getInput,formatStr,isPalindrome

import unittest

class TestStringMethods(unittest.TestCase):

    def test_format_str1(self):
        self.assertEqual(formatStr("\n\n\n\n\n"), "")

    def test_format_str2(self):
        self.assertEqual(formatStr("123\n\rlol90"), "123lol90")

    def test_format_str3(self):
        self.assertEqual(formatStr("02/02/2020"), "02022020")

    def test_isPalindrome1(self):
        self.assertTrue(isPalindrome("02022020"))

    # This should fail.    
    def test_isPalindrome2(self):
        self.assertTrue(isPalindrome("Able was I ere I saw Elba"))
    
    def test_isPalindrome3(self):
        self.assertTrue(isPalindrome("1111111111"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
