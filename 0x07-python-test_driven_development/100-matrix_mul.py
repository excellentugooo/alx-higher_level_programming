#!/usr/bin/python3
'''Contains a get_matrix_size and a matrix_mul function for a TDD project.
'''


def get_matrix_sizes(mat_1, mat_2, name1, name2):
    '''Computes the size of a matrix and performs some
    matrix validation.
    Args:
        matrix (list): The matrix.
        name (str): The name of the matrix.
    Returns:
        list. The rows and columns of the given matrix.
    '''
    funcs = (
        lambda txt: '{} must be a list'.format(txt),
        lambda txt: '{} can\'t be empty'.format(txt),
        lambda txt: '{} must be a list of lists'.format(txt),
        lambda txt: '{} should contain only integers or floats'.format(txt),
        lambda txt: 'each row of {} must be of the same size'.format(txt),
        lambda l: all(map(lambda n: isinstance(n, (int, float)), l)),
    )
    size0 = [0, 0]
    size1 = [0, 0]
    if not isinstance(mat_1, list):
        raise TypeError(funcs[0](name1))
    if not isinstance(mat_2, list):
        raise TypeError(funcs[0](name2))
    size0[0] = len(mat_1)
    size1[0] = len(mat_2)
    if size0[0] == 0:
        raise ValueError(funcs[1](name1))
    if size1[0] == 0:
        raise ValueError(funcs[1](name2))
    if not all(map(lambda x: isinstance(x, list), mat_1)):
        raise TypeError(funcs[2](name1))
    if not all(map(lambda x: isinstance(x, list), mat_2)):
        raise TypeError(funcs[2](name2))
    if all(map(lambda x: len(x) == 0, mat_1)):
        raise ValueError(funcs[1](name1))
    if all(map(lambda x: len(x) == 0, mat_2)):
        raise ValueError(funcs[1](name2))
    if not all(map(lambda x: funcs[5](x), mat_1)):
        raise TypeError(funcs[3](name1))
    if not all(map(lambda x: funcs[5](x), mat_2)):
        raise TypeError(funcs[3](name2))
    size0[1] = len(mat_1[0])
    size1[1] = len(mat_2[0])
    if not all(map(lambda x: len(x) == size0[1], mat_1)):
        raise TypeError(funcs[4](name1))
    if not all(map(lambda x: len(x) == size1[1], mat_2)):
        raise TypeError(funcs[4](name2))
    return size0, size1


def matrix_mul(m_a, m_b):
    '''Multiplies 2 matrices.
    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.
    Returns:
        list: A list of lists of the products of the two given matrices.
    Raises:
        ValueError: If m_a's column count isn't equal to m_b's row count.
    '''
    a_sz, b_sz = get_matrix_sizes(m_a, m_b, 'm_a', 'm_b')
    # AB only works iff column_count in A == row_count in B
    if a_sz[1] != b_sz[0]:
        raise ValueError('m_a and m_b can\'t be multiplied')
    else:
        result = []
        for row_a in m_a:
            row_res = []
            for i in range(b_sz[1]):
                arg = zip(range(a_sz[1]), row_a)
                value = map(lambda x: x[1] * m_b[x[0]][i], arg)
                row_res.append(sum(list(value)))
            result.append(row_res)
        return result
