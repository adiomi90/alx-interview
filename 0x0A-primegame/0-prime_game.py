#!/usr/bin/python3
""" Prime Game """


def primes(n):
    """
    Generate a list of prime numbers up to n using the
    Sieve of Eratosthenes algorithm.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to n.
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determine the winner of a prime game.

    Args:
        x (int): The number of rounds in the game.
        nums (list): A list of integers representing the
        numbers for each round.

    Returns:
        str: The name of the winner ('Maria', 'Ben') or
        None if there is no winner.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
