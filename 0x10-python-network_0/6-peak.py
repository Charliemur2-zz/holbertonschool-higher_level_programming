#!/usr/bin/python3
"""
function that returns the peak of a list
"""
def find_peak(list_of_integers):
    if list_of_integers > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
