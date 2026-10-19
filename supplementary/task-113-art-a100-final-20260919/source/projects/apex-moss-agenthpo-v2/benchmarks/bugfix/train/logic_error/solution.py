def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True  # BUG: should return False when divisible
    return False  # BUG: should return True when no divisors found
