#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) != str) or (roman_string is None):
        return 0
    num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    num_dict['D'] = 500
    num_dict['M'] = 1000
    total = 0
    i = 0
    while(i < len(roman_string)):
        if (i + 1) < len(roman_string):
            key1 = roman_string[i]
            key2 = roman_string[i + 1]
            if (num_dict[key1] < num_dict[key2]):
                num = num_dict[key2] - num_dict[key1]
                total += num
                i += 1
            else:
                key = roman_string[i]
                total += num_dict[key]
        else:
            key = roman_string[i]
            total += num_dict[key]
        i += 1
    return total
