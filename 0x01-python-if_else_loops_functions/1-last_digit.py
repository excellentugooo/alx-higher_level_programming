#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastN = abs(number) % 10
if number < 0:
    LastN = -LastN
print("Last digit of {} is {} and is ".format(number, LastN), end="")
if LastN > 5:
    print("greater than 5")
elif LastN == 0:
    print("0")
else:
    print("less than 6 and not 0")
