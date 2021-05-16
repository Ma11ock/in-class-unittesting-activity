#!/usr/bin/env python

import string

# Palindrome calculator.

def getInput():
    return input("Enter a string:")

def formatStr(the_string):
    return "".join(filter(str.isalnum, the_string)).lower()


def isPalindrome(the_string):
    return the_string == the_string[::-1]

