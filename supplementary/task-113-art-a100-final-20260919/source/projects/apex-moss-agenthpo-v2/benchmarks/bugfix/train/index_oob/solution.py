def get_last_element(arr):
    """Return the last element of a non-empty list."""
    return arr[len(arr)]  # BUG: should be arr[len(arr) - 1] or arr[-1]
