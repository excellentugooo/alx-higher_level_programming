#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    Dict = a_dictionary.copy()
    listKeys = list(Dict.keys())

    for x in listKeys:
        Dict[x] *= 2
    return (Dict)
