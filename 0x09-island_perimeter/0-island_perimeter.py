#!/usr/bin/python3
""" define a function """


def island_perimeter(grid):
    """ calculates the perimeter of the island in the given grid """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                adjacent_cells = [
                    (row - 1, col),
                    (row, col + 1),
                    (row + 1, col),
                    (row, col - 1),
                ]
                for adjacent_row, adjacent_col in adjacent_cells:
                    if (
                        adjacent_row < 0
                        or adjacent_col < 0
                        or adjacent_row >= rows
                        or adjacent_col >= cols
                        or grid[adjacent_row][adjacent_col] == 0
                    ):
                        perimeter += 1
    return perimeter
