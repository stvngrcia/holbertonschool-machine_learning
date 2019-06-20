#!/usr/bin/env python3
"""This file implements the a function to get the shape of a matrix"""
def matrix_shape(matrix):
    """Gets the shape of a matrix
    :param matrix: The matrix for which this method is getting the shape
    :return: A list of integers representing the shape of the matrix
    """
    shape = []
    while matrix:
        shape.append(len(matrix))
        matrix = matrix[0] if type(matrix[0]) == list else None
    return shape
