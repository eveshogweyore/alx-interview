#!/usr/bin/python3
"""Prime Game."""


def isWinner(x, nums):
    """Prime Game function."""
    if x < 1 or not nums:
        return None
    m_win, b_win = 0, 0

    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        b_win += primes_count % 2 == 0
        m_win += primes_count % 2 == 1
    if m_win == b_win:
        return None
    return 'Maria' if m_win > b_win else 'Ben'
