#!/usr/bin/env python3
"""Implementation of a method to transpose a 2D matrix"""


def matrix_transpose(matrix):
    """Transposes a matrix
    :param matrix: The given matrix to transpose
    :return: A transposed matrix
    """
    new_matrix = []
    flat_matrix = sum(matrix, [])
    level_size = len(matrix[0]) if matrix else 0
    start = 0
    new_level = True
    tracker = start
    while start != level_size:
        if tracker >= len(flat_matrix):
            new_matrix.append(transpose)
            new_level = True
            start += 1
        if new_level:
            tracker = start
            transpose = []
            new_level = False
        transpose.append(flat_matrix[tracker])
        tracker += level_size

    return new_matrix
