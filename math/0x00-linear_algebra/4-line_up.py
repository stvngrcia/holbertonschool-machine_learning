#!/usr/bin/env python3
"""Implements the addition of arrays"""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise
    :param arr1: First array
    :param arr2: Second array
    :return: New array representing the sum of arr1 and arr2
    """
    if len(arr1) != len(arr2):
        return None

    return [arr1[idx] + arr2[idx] for idx, _ in enumerate(arr1)]
