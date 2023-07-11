#!/usr/bin/python3
def uppercase(str):
    for up in str:
        if (ord(up) >= 97 and ord(up) <= 122):
            up = chr(ord(up) - 32)
        print("{}".format(up), end='')
    print('')
