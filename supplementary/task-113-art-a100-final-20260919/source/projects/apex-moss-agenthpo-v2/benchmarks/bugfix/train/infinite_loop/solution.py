def sum_until(limit):
    """Return the sum of integers 1, 2, 3, ... up to and including limit."""
    total = 0
    i = 1
    while i <= limit:
        total += i
        # BUG: forgot i += 1, so the loop never terminates
    return total
