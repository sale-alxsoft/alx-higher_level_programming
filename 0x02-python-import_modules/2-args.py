#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    len_a = len(argv)
    if (len_a == 1):
        print("{} arguments.".format(len_a - 1))
    elif (len_a == 2):
        print("{} argument:".format(len_a - 1))
        print("{}: {}".format(len_a - 1, argv[1]))
    else:
        print("{} arguments:".format(len_a - 1))
        for i in range(1, len_a):
            print("{}: {}".format(i, argv[i]))
