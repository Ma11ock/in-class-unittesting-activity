#!/usr/bin/env python

def getSomeInput():
    return input("Give me a string: ")


def split_str(the_str):
    return the_str.split()

def wc(the_str):
    return len(split_str(the_str))


