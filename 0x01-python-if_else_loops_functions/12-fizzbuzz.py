#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 100):
        if (number % 3 == 0):
            print("Fizz", end=" ")
        elif (number % 5 == 0):
            print("Buzz", end=" ")
        else:
            print(number, end=" ")