#!/usr/bin/env python3
"""Calculates the shape of a matrix"""


def matrix_shape(matrix):
    """Returns the shape of a matrix as a list of integers"""
    if not isinstance(matrix[0], list):
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
