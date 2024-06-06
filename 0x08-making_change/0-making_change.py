#!/usr/bin/python3
"""Change making module.
"""

from collections import deque

def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    # Queue for BFS, starting with (0, 0) which means (current total, number of coins used)
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
