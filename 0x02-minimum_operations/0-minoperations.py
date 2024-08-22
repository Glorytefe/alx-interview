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

    paste = 1
    min = 2
    count = 2

    while count < n:
        bal = n - count
        if bal % min:
            min += 1
            count += paste
        else:
            paste = count
            count += paste
            min += 2
    if count == n:
        return min
    else:
        return 0
