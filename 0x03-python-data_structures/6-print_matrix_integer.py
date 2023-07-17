#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for colums in rows:
            print("{:d}".format(colums), end=" " if colums != rows[-1] else "")
        print()
