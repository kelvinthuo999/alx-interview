#!/usr/bin/env python3
"""Function to unlock all the boxes"""


def canUnlockAll(boxes):
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