#!/usr/bin/python3
"""
This module contains a function to determine the fewest number of coins
needed to meet a given total amount.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): List of coin values available.
        total (int): The total amount to be met.

    Returns:
        int: The fewest number of coins needed, or -1 if total cannot be met,
        or 0 if total is 0 or less.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Base case: no coins are needed to make 0

    # Dynamic programming approach to find the fewest coins
    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins[amount] = min(min_coins[amount],
                                    min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
