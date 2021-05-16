#!/usr/bin/env python

from palindrome import getInput,formatStr,isPalindrome


def test_format1():
    assert formatStr("\n\n\n\n\n") == ""

def test_format2():
    assert formatStr("123\n\rlol90") == "123lol90"

def test_format3():
    assert formatStr("02/02/2020") == "02022020"

def test_palin1():
    assert isPalindrome("02022020")

# Fails on purpose    
def test_palin2():
    assert isPalindrome("Able was I ere I saw Elba")

def test_palin3():
    assert isPalindrome("1111111111")
