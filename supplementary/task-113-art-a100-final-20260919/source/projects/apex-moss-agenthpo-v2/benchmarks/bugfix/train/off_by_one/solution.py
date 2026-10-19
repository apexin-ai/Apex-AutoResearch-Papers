def sum_1_to_n(n):
    """Return the sum of all integers from 1 to n inclusive."""
    total = 0
    for i in range(n):  # BUG: should be range(1, n + 1) or range(n + 1)
        total += i
    return total
