#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Generate a list of booleans indicating prime status and cumulative prime count up to n."""
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0], primes[1] = False, False  # 0 and 1 are not primes

    # Create a cumulative count of primes up to each index
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if primes[i]:
            count += 1
        prime_count[i] = count
    
    return primes, prime_count

def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    _, prime_count = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

