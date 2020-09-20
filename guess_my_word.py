# Riddler Classic @ https://fivethirtyeight.com/features/can-you-break-a-very-expensive-centrifuge/

from pprint import pprint


def optimal_guesses(n):
    """
    builds the optimal guessing strategy for n words
    :param n: nr. of words, >= 1
    :return: list of nr. of optimal-strategy guesses needed for each possible word

    >>> optimal_guesses(1)
    [1]

    >>> optimal_guesses(9)
    [4, 3, 2, 3, 1, 4, 3, 2, 3]
    """
    if n == 1:
        return [1]
    elif n == 2:
        return [2, 1]
    n2 = n // 2
    head = optimal_guesses(n2)
    if n % 2:
        tail = head[:]
    else:
        tail = optimal_guesses(n2 - 1)
    head, tail = [el + 1 for el in head], [el + 1 for el in tail]
    return head + [1] + tail


def avg_guesses_naive(n):
    """
    computes the avg. nr. of optimal-strategy guesses needed with n words

    >>> avg_guesses_naive(10)
    2.9
    """
    return sum(optimal_guesses(n)) / n


def avg_guesses_smart(n):
    """
    computes the avg. nr. of optimal-strategy guesses needed with n words

    >>> avg_guesses_naive(100) - avg_guesses_smart(100)
    0.0
    """
    if n == 1:
        return 1
    pow2, k, sum_pow2, sum_guesses = 1, 1, 1, 1
    while True:
        rest = n - sum_pow2
        pow2 *= 2
        k += 1
        if rest < pow2:
            sum_guesses += rest * k
            break
        else:
            sum_pow2 += pow2
            sum_guesses += pow2 * k
    return sum_guesses / n, sum_guesses


n = 267751
avg_guesses, numerator = avg_guesses_smart(n)
print(f'The expected number of guesses is {avg_guesses:.6f}, or more precisely: {numerator} / {n}')

# OUTPUT:
# The expected number of guesses is 17.041957, or more precisely: 4563001 / 267751


