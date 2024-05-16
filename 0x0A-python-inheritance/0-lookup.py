#!/usr/bin/env = python3
"""
    This module has a function that returns the 
    list of available attributes and methods of an object 
"""

def lookup(obj):
    return list(dir(obj))
