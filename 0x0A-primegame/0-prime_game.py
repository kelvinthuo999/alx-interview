#!/usr/bin/python3
"""
A prime game between Maria and Ben
"""


def isWinner(x, nums):
    """
    Determine the winner after x rounds of the game.
    """
    if not nums or x <= 0:
        return None

    max_num = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Create a cumulative count of primes up to each index
    prime_count = [0] * (max_num + 1)
    count = 0
    for i in range(1, max_num + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    maria_victor = 0
    ben_victor = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_victor += 1
        else:
            maria_victor += 1

    if maria_victor > ben_victor:
        return "Maria"
    elif ben_victor > maria_victor:
        return "Ben"
    else:
        return None
