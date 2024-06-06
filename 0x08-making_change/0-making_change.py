#!/usr/bin/python3
"""
This module demonstrates a function to calculate the fewest coins needed
"""
from collections import deque


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
    if total <= 0:
        return 0

    queue = deque([(0, 0)])
    visited = set()

    while queue:
        current, num_coins = queue.popleft()

        # Try each coin to see if we can reach the total
        for coin in coins:
            new_total = current + coin

            if new_total == total:
                return num_coins + 1
            elif new_total < total and new_total not in visited:
                visited.add(new_total)
                queue.append((new_total, num_coins + 1))

    return -1
