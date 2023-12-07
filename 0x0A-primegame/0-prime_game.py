#!/usr/bin/python3
""" define a function """


def is_prime(num):
    """ checks for prime numbers """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """ plays the game for the specified number of rounds """
    wins_maria, wins_ben = 0, 0

    for i in range(x):
        n = nums[i]
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        total_primes = len(primes)

        if total_primes % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1

    if wins_maria > wins_ben:
        return "Maria"
    elif wins_ben > wins_maria:
        return "Ben"
    else:
        return None
