#!/usr/bin/python3
for alpha_ord in range(97, 123):
    if (alpha_ord == 113 or alpha_ord == 101):
        continue
    print("{}".format(chr(alpha_ord)), end="")
