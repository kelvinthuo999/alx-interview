#!/usr/bin/python3
"""Function to return the min num of operation to achieve required results"""


def minOperations(n):
    """Function to determine minimum operations"""
    if n < 2:
        return 0

    operations = 0
    root = 2

    while root <= n:
        if n % root == 0:
            operations += root
            n //= root
            root -= 1
        root += 1

    return operations
