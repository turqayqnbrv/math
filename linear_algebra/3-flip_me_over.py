#!/usr/bin/env python3
"""Transpose function to check a new matrix transposed"""


def matrix_transpose(matrix):
    """
    Returns a new matrix transposed

    Args:
        matrix: given list of lists

    Returns:
        new_matrix: Transposed matrix
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
