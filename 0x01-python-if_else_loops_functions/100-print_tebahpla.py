#!/usr/bin/python3

for rev_alt in range(122, 96, -1):
    if (rev_alt % 2 != 0):
        rev_alt = rev_alt - 32
    print("{}".format(chr(rev_alt)), end="")
