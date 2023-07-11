#!/usr/bin/python3
def print_last_digit(number):
    LastNum = abs(number) % 10
    print("{}".format(LastNum), end="")
    return LastNum
