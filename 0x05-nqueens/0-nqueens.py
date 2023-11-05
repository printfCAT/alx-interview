#!/usr/bin/python3
""" define a function """


import sys

def is_safe(board, row, col):
    """ check if there is a queen in the same column """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def nqueens(N):
    """ solves the N Queens puzzle """
    def solve(board, row):
        """ function to solve the puzzle """
        if row == N:
            result.append([[i, board[i].index(1)] for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    result = []
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve(board, 0)
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = nqueens(N)
        for solution in solutions:
            print(solution)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
