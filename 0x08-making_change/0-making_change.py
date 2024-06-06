#!/usr/bin/python3
"""Change making module."""

def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total < 0:
        return -1
    elif total == 0:
        return 0
    else:
        # Sort the coins in descending order to prioritize larger denominations
        coins.sort(reverse=True)

        # Initialize counters
        count = 0
        i = 0

        # Loop until the total is reached or exceeded
        while total > 0:
            # Check if the current coin value is less than or equal to the remaining total
            if coins[i] <= total:
                # Subtract the coin value from the total and increment the counter
                total -= coins[i]
                count += 1
            else:
                # Move to the next coin if the current one is too large
                i += 1

            # Break the loop if all coins have been considered and the total is still positive
            if i == len(coins) and total > 0:
                return -1

        return count
