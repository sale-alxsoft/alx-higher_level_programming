#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new_list = []
    for x in my_list:
        if x in new_list:
            continue
        result += x
        new_list.append(x)
    return result
