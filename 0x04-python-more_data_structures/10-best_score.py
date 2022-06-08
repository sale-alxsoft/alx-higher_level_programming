#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return None
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    values = list(a_dictionary.values())
    keys = list(a_dictionary.keys())
    max_val = values[0]
    max_key = values[0]
    for key, value in a_dictionary.items():
        if max_val < value:
            max_val = value
            max_key = key
    return max_key
