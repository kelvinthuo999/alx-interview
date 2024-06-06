#!/usr/bin/python3
"""This module demonstrates a function to calculate the fewest coins needed."""


def make_change(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of coin values.
        total (int): Target total amount.

    Returns:
        int: Fewest num of coins needed to meet the total,
        or -1 if impossible.
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[total] if dp[total] <= total else -1
