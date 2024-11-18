#!/usr/bin/python3

"""
rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Parameters:
    matrix (list of list of int): The input 2D matrix to rotate.

    Modifies:
    The input matrix is modified in-place to achieve the rotation.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to achieve the clockwise rotation
    for i in range(n):
        matrix[i].reverse()
