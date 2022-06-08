#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary == None):
        return None
    for key in a_dictionary:
        max_val = a_dictionary[i]
        for j in a_dictionary:
            if (max_val < a_dictionary[j]):
                max_val = a_dictionary[j]
                key = j
        return key
