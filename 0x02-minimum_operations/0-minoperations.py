#!/usr/bin/python3

"""
Minimum Operations
"""


def minOperations(n):
    """
    Given a number n, minOperations calculates the
    fewest number of operations needed to result
    in exactly n H characters in the file
    """
    if n < 2:
        return 0

    min_operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            min_operations += factor
            n //= factor
        factor += 1

    return min_operations
