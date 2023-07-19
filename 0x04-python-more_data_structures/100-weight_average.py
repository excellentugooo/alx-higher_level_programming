#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    dense = 0

    for i in my_list:
        number += i[0] * i[1]
        dense += i[1]

    return (number / dense)
