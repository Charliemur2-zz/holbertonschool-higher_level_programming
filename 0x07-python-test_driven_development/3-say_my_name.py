#!/usr/bin/python3
"""
Say my name function.

Creation Date: May 22, 2020.

Author: Carlos Murcia.
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints 'My name is' and tow given names.

    Arguments:
    first_name: fiste name.
    last_name: last name.

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
