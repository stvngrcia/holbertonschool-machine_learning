#!/usr/bin/env python3
def matrix_shape(matrix):
    size = []
    while matrix:
        size.append(len(matrix))
        matrix = matrix[0] if type(matrix[0]) == list else None
    return size
