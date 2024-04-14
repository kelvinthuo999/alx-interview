#!/usr/bin/python3
'''Solution to Pascal's triangle'''

def pascal_triangle(n):
    '''
    Parameters:
        n (int): The number of row's of Pascal's triangle

    Returns:
        pTriangle (list): Pascal's Triangle up to the nth row
    '''
    pTriangle = []

    if n <= 0:
        return pTriangle

    # Add rows to Pascal's Triangle
    for i in range(n):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1, 1  # Set first and last elements to 1

        for j in range(1, len(row)-1):
            row[j] = pTriangle[i-1][j-1] + pTriangle[i-1][j]

        pTriangle.append(row)

    return pTriangle
