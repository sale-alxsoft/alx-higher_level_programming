#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_list = len(my_list)
    len_list -= 1
    new_list = []
    while (len_list >= 0):
        new_list.append(my_list[len_list])
        len_list -= 1
    for i in new_list:
        print("{:d}".format(i))
