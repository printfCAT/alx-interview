#!/usr/bin/python3
""" define a function """


def rotate_2d_matrix(matrix):
    """ rotates a 2d array clockwise by 90 degrees """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
