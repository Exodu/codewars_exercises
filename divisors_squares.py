# Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42.
# These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764.
# The sum of the squared divisors is 2500 which is 50 * 50, a square!

# Given two integers m, n (1 <= m <= n) we want to find all integers
# between m and n whose sum of squared divisors is itself a square. 42 is such a number.

# #Examples:

# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]


def get_divisors(n):
    i = 1
    while (i <= n**0.5):
        if (n % i == 0):
            if (n // i == i):
                yield i
            else:
                yield i
                yield n // i
        i = i + 1


def list_squared(m, n):
    results = []
    for i in range(m, n + 1):
        divisors = get_divisors(i)
        squares = [i * i for i in divisors]
        summa = sum(squares)
        if ((summa**0.5).is_integer()):
            results.append([i, summa])

    return results
