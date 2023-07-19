#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    MatrixCopy = matrix.copy()

    for i in range(len(matrix)):
        MatrixCopy[i] = list(map(lambda x: x**2, matrix[i]))

    return (MatrixCopy)
