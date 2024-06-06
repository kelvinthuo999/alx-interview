#!/usr/bin/python3
"""
This module demonstrates a function to calculate the fewest coins needed.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of coin values.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total,
        or -1 if impossible.
    """
    if total < 0:
        return -1
    elif total == 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    i = 0

    while total > 0:
        if coins[i] <= total:
            total -= coins[i]
            count += 1
        else:
            i += 1
        if i == len(coins) and total > 0:
            return -1

    return count
