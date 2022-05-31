#!/usr/bin/python3
def uppercase(str):
    len_str = len(str)
    temp = list(str)
    for i in range(len_str):
        low_ord = ord(str[i])
        if (low_ord > 96):
            upp_ord = low_ord - 32
            temp[i] = chr(upp_ord)
    print("{}".format("".join(temp)))
