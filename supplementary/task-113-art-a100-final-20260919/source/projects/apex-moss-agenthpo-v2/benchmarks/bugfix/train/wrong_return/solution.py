def find_max(numbers):
    """Return the maximum value in a list of numbers."""
    if not numbers:
        return None
    result = numbers[0]
    for num in numbers[1:]:
        if num < result:  # BUG: should be num > result
            result = num
    return result
