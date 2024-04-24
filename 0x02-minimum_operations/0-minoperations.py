#!/usr/bin/python3
"""Function to return the min num of operation to achieve required results"""


def minOperations(n):
    """Function to determine minimum operations"""
    if n <= 1:
        return n

    operations = 0
    current_chars = 1
    clipboard = 0

    while current_chars < n:
        if n % current_chars == 0:
            clipboard = current_chars
            operations += 1
        current_chars += clipboard
        operations += 1

    return operations
