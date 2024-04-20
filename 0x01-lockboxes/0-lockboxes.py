#!/usr/bin/python3

"""
Module for determining if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each sublist represents a box and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    seen = set()
    queue = [0]

    while queue:
        box = queue.pop(0)
        seen.add(box)
        for key in boxes[box]:
            if key not in seen and key < n:
                queue.append(key)

    return len(seen) == n
