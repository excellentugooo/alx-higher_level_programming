#!/usr/bin/python3
def number_keys(a_dictionary):
    numbers = 0
    listKeys = list(a_dictionary.keys())

    for i in listKeys:
        numbers += 1
    return (numbers)
