#!/usr/bin/env python3
"""Implements the concatenation of 2D arrays"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    :param mat1:
    :param mat2:
    :param axis:
    :return:
    """
    new_mat1 = []
    new_mat2 = []
    if axis == 0:
        for idx, _ in enumerate(mat1):
            new_mat1.append(mat1[idx][:])
        for idx, _ in enumerate(mat2):
            new_mat2.append(mat2[idx][:])
        return new_mat1 + new_mat2

    return [mat1[idx] + mat2[idx] for idx, _ in enumerate(mat1)]

