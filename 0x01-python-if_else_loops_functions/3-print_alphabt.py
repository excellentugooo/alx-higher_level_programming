#!/usr/bin/python3
for letters_alpha in range(97, 123):
    if (letters_alpha == 101 or letters_alpha == 113):
        continue
    print("{}".format(chr(letters_alpha)), end="")
