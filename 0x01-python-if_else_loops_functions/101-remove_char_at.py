#!/usr/bin/python3
def remove_char_at(str, n):
    len_str = len(str)
    if (n >= len_str or n < 0):
        return (str)
    temp = list(str)
    temp.remove(temp[n])
    return ("{}".format("".join(temp)))
