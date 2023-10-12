#!/usr/bin/python3
""" define a function """


def minOperations(n):
    """ find lowest no. of ops to print 'n' no. of H characters """
    if n < 2:
        return 0
    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            operations += root
            n = n / root
            root -= 1
        root += 1

    return operations
