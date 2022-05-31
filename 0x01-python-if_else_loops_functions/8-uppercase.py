#!/usr/bin/python3
def uppercase(str):
    for x in str:
        x_ord = ord(x)
        if (x_ord >= 97 and x_ord < 123):
            i = 65
            for j in range(97, 123):
                if (j == x_ord):
                    print("{}".format(chr(i)), end="")
                i += 1
        else:
            print(x, end="")
    print('')
