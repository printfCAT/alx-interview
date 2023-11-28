#!/usr/bin/python3
""" define a function """


def island_perimeter(grid):
    """ calculates the perimeter of the island in the given grid """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Initialize with 4 sides

                # Check adjacent cells and deduct for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct for adjacent land cell above
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct for adjacent land cell to the left

    return perimeter
