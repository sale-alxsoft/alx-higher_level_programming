#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if (idx < 0):
        for i in my_list:
            new_list.append(i)
        return new_list
    elif (idx >= len(my_list)):
        for i in my_list:
            new_list.append(i)
        return new_list
    else:
        for i in my_list:
            new_list.append(i)
        new_list[idx] = element
        return new_list
