#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make change for a
    given total.

    Args:
        coins (list): List of coin denominations available.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: The minimum number of coins needed to make change for the
        given total.
             Returns -1 if it is not possible to make change with the
             given coins.

    """

    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for i in coins:
        if total % i == 0:
            coin_count += int(total / i)
            return coin_count
        if total - i >= 0:
            if int(total / i) > 1:
                coin_count += int(total / i)
                total = total % i
            else:
                coin_count += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
