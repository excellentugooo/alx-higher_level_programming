#!/usr/bin/python3
def to_subtract(num_list):
    subtract = 0
    max_num = max(num_list)
    for num in num_list:
        if max_num > num:
            subtract += num
    return max_num - subtract

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    numbers = []
    prev_num = 0

    for char in roman_string:
        if char in roman_numerals:
            current_num = roman_numerals[char]
            if current_num > prev_num:
                numbers.append(to_subtract(numbers))
                numbers = [current_num]
            else:
                numbers.append(current_num)
            prev_num = current_num

    numbers.append(to_subtract(numbers))
    return sum(numbers)
