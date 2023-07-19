#!/usr/bin/python3
def to_subtract(list_number):
    to_subs = 0
    max_lists = max(list_number)

    for i in list_number:
        if max_lists > i:
            to_subs += i

    return (max_lists - to_subs)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':
                100, 'D': 500, 'M': 1000}
    list_keys = list(rom_numbers.keys())

    number = 0
    last_roman = 0
    list_number = [0]

    for ch in roman_string:
        for r_num in list_key:
            if r_num == ch:
                if rom_numbers.get(ch) <= last_roman:
                    number += to_subtract(list_number)
                    list_number = [rom_numbers.get(ch)]
                else:
                    list_number.append(rom_numbers.get(ch))

                last_roman = rom_numbers.get(ch)

    number += to_subtract(list_number)

    return (number)
