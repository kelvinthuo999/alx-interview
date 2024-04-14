#!/usr/bin/python3
'''Module to find Pascal's Triangle integers'''

def pascal_triangle(n):
    '''
    Function to find Pascal's Triangle integers

    Parameters:
        n (int): The number of row's of Pascal's triangle

    Returns:
        pascal_triangle (list): Pascal's Triangle up to the nth row
    '''
    pascal_triangle = []

    if n <= 0:
        return pascal_triangle

    # Add rows to Pascal's Triangle
    for i in range(n):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1, 1  # Set first and last elements to 1

        for j in range(1, len(row)-1):
            row[j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]

        pascal_triangle.append(row)

    return pascal_triangle
