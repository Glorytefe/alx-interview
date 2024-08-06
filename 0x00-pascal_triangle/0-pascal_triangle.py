#!/usr/bin/python3

"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []
    triangle = [[1]]
    if n == 1:
        return triangle
    while len(triangle) < n:
        row = [1]
        prevRow = triangle[-1]
        row.extend(prevRow[i] + prevRow[i + 1] for i in range(len(prevRow) - 1))
        row.append(1)
        triangle.append(row)
    return triangle
