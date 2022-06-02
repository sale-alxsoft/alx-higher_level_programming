#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    import calculator_1 as calc
    len_a = len(argv)
    if (len_a != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    ops_str = "+-*/"
    if operator not in ops_str:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if (operator == ops_str[0]):
        res = calc.add(a, b)
        print("{} + {} = {}".format(a, b, res))
    elif (operator == ops_str[1]):
        res = calc.sub(a, b)
        print("{} - {} = {}".format(a, b, res))
    elif (operator == ops_str[2]):
        res = calc.mul(a, b)
        print("{} * {} = {}".format(a, b, res))
    else:
        res = calc.div(a, b)
        print("{} / {} = {}".format(a, b, res))
