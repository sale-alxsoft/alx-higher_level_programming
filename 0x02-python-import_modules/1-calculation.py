#!/usr/bin/python3
if (__name__ == "__main__"):
    import calculator_1 as calc
    a = 10
    b = 5
    res_add = calc.add(a, b)
    res_sub = calc.sub(a, b)
    res_mul = calc.mul(a, b)
    res_div = calc.div(a, b)

    print("{} + {} = {}".format(a, b, res_add))
    print("{} - {} = {}".format(a, b, res_sub))
    print("{} * {} = {}".format(a, b, res_mul))
    print("{} / {} = {}".format(a, b, res_div))
