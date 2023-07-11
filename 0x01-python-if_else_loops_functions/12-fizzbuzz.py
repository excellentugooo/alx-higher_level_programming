#!/usr/bin/python3
def fizzbuzz():
    for numba in range(1, 101):
        if (numba % 3 == 0 and numba % 5 == 0):
            print("{}".format("FizzBuzz"), end=" ")
        elif (numba % 3 == 0):
            print("{}".format("Fizz"), end=" ")
        elif (numba % 5 == 0):
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(numba), end=" ")
