def reverse_list(lst):
    """Return a new list with elements in reverse order."""
    reversed_lst = []
    n = len(lst)
    for i in range(n - 1, -1, -1):  # BUG: crashes when lst is empty — n-1 is -1, but range(-1,-1,-1) is empty so no crash there
        reversed_lst.append(lst[i])
    return reversed_lst


def first_of_reversed(lst):
    """Return the first element of the reversed list."""
    return reverse_list(lst)[0]  # BUG: crashes on empty input with IndexError
