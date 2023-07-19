#!/usr/bin/python3
def uniq_add(my_list=[]):
    List = set(my_list)
    numbers = 0

    for x in List:
        numbers += x
    return (numbers)
