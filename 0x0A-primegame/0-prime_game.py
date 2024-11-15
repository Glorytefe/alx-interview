#!/usr/bin/python3

"""
isWinner
"""


def isWinner(x, nums):
    """
    Determines the winner of x rounds of a game played between Maria and Ben.

    given a set of consecutive integers from 1 to n, players take turns
    choosing a prime num and removing that num and its multiples from the set.
    The player who cannot make a move loses.
    Maria always starts first, and both players play optimally.

    Parameters:
    x (int): Number of rounds.
    nums (list): List of integers rep the upper bound of num for each round.

    Returns:
    str: name of the player with the most wins, or None if there
         is a tie.
    """

    if x < 1 or not nums:
        return None

    # Find the maximum number in nums to limit the sieve
    max_n = max(nums)

    # Create a prime number sieve up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Create a prefix array of prime counts up to each index
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each game round
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
