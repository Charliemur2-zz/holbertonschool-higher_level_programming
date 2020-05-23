#!/usr/bin/python3
"""
Creation date: May 21, 2020.

Author: Carlos Andres Murcia Muñoz

Function that adds 2 integers.

"""


def add_integer(a, b=98):
    """
    Functions that adds 2 integers.
    return: the result of a + b.
    """
    if type(a) not in [int, float] or a == float("inf") or a != a:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b == float("inf") or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
