#!/usr/bin/env python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    '''
    This is a function that adds two integers
    If floats are passed as argumenst, they are casted into integers
    '''
    
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a)+ int(b))
