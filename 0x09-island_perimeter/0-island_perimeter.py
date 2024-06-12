#!/usr/bin/python3
"""
Funct to calc perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island represented by the grid.
    
    Args:
    grid (list[list[int]]): A list of lists representing the island grid.
    
    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    
    # Iterate over each row in the grid
    for i in range(len(grid)):
        # Iterate over each column in the current row
        for j in range(len(grid[i])):
            # Check if the current cell is land (1) and has a neighboring water cell (0)
            if grid[i][j] == 1:
                # Check top cell
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom cell
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left cell
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right cell
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                
    return perimeter
