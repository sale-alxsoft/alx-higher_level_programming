#!/usr/bin/python3
def no_c(my_string):
    my_list = []
    for i in my_string:
        if (i == 'c' or i == "C"):
            continue
        my_list.append(i)
    new_string = "".join(my_list)
    return new_string
