#!/usr/bin/python3
"""Change making module."""

def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    sorted_coins = sorted(coins, reverse=True)
    for coin in sorted_coins:
        if rem >= coin:
            rem -= coin
            coins_count += 1
    return coins_count if rem == 0 else -1
