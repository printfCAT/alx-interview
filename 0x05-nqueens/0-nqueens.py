#!/usr/bin/python3
"""function module to solve the N queens puzzle"""


import sys

def nqueens(N):
    """N queens function"""
    def is_safe_to_place_queen(board, row, col):
        """helper function to check if it is safe to place the queen"""
        # check the column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # check the upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # check the upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j] == 1:
                return False

        return True

    def solve(row):
        """helper function to solve the N queens puzzle"""
        # base case
        if row == N:
            solutions.append([list(row) for row in board])
            return

        for col in range(N):
            if is_safe_to_place_queen(board, row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0  # backtracking happes here

    # entry point to the backtracking algorithm
    # initialize the board
    board = [[0 for _ in range(N)] for _ in range(N)]
    # solutions array
    solutions = []
    # call the backtracking helper function with the first row
    solve(0)
    return solutions


if __name__ == "__main__":
    # check for right number of arguments
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # check if the argument is a number
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    # check if the argument is greater than 4
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens = int(sys.argv[1])

    def print_coordinates(queen_row):
        """function to print the coordinates of the queens"""
        coordinates = []
        for row_index, row in enumerate(queen_row):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    coordinates.append([row_index, col_index])
        print(coordinates)

    Solutions = nqueens(queens)
    for solution in Solutions:
        print_coordinates(solution)
