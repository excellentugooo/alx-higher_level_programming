#!/usr/bin/python3
def to_sub(List):
    subtract = 0
    MaxList = max(List)

    for i in List:
        if MaxList > i:
            subtract += i
    return (MaxList - subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    RomanNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(RomanNum.keys())

    number = 0
    last_rom = 0
    list_num = [0]

    for i in roman_string:
        for r_num in list_keys:
            if r_num == i:
                if RomanNum.get(i) <= last_rom:
                    number += to_sub(list_num)
                    list_num = [RomanNum.get(i)]
                else:
                    list_num.append(RomanNum.get(i))

                last_rom = RomanNum.get(i)

    number += to_sub(list_num)

    return (number)
