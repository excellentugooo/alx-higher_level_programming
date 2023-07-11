#!/usr/bin/python3
for n1 in range(10):
    for n2 in range(n1 + 1, 10):
        if (n1 == 8 and n2 == 9):
            print("{1:d}{0:d}".format(n2, n1))
            continue
        print("{0:d}{1:d}".format(n1, n2), end=", ")
