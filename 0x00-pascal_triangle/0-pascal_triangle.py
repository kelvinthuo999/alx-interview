#!/usr/bin/env python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    - n: An integer representing the number of rows in Pascal's Triangle.

    Returns:
    - A list of lists containing the values of Pascal's Triangle.
    """
    def generate_row(row_num, prev_row):
        if row_num == 0:
            return []
        elif row_num == 1:
            return [1]
        else:
            new_row = [1]
            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i-1] + prev_row[i])
            new_row.append(1)
            return new_row

    triangle = []
    for i in range(1, n + 1):
        triangle.append(generate_row(i, triangle[-1] if triangle else []))

    return triangle