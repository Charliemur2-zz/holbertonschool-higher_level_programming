#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_item = max(list(a_dictionary))
        return max_item
    else:
        return None
