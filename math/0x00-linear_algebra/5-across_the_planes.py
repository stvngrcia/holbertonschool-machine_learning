#!/usr/bin/env python3
"""Implements the addition of 2D matrices"""


def add_matrices2D(mat1, mat2):
    """Adds 2D matrices
    :param mat1: First matrix
    :param mat2: Second matrix
    :return: The addition of mat1 and mat2
    """

    if len(mat1) != len(mat2):
        return None
    new_matrix = [add_arrays(mat1[idx], mat2[idx])
                  for idx, _ in enumerate(mat1)]
    return new_matrix if new_matrix[0] else None


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise
    :param arr1: First array
    :param arr2: Second array
    :return: New array representing the sum of arr1 and arr2
    """
    if len(arr1) != len(arr2):
        return None

    return [arr1[idx] + arr2[idx] for idx, _ in enumerate(arr1)]
