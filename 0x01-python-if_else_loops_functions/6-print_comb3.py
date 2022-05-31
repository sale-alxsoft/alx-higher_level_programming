#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if (i == j or i == 8):
            continue
        print("{}{}".format(i, j), end=", ")
    if (i == 8):
        print("{}{}".format(i, j))
