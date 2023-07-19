#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    List = list(a_dictionary.keys())
    List.sort()
    for x in List:
        print("{}: {}".format(x, a_dictionary.get(x)))
