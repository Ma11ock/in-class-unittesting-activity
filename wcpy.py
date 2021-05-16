#!/usr/bin/env python

from wc import getSomeInput,split_str,wc


def test_splitStr1():
    assert split_str("This is a string") == ["This", "is", "a", "string"]

def test_splitStr2():
    assert split_str("") == []

def test_wc():
    assert wc("This is a string") == 4

def test_wc1():
    assert wc("") == 0
