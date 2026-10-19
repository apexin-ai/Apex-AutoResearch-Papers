from solution import find_max


def test_find_max_positive():
    assert find_max([1, 5, 3, 9, 2]) == 9


def test_find_max_negative():
    assert find_max([-10, -3, -7]) == -3


def test_find_max_single():
    assert find_max([42]) == 42


def test_find_max_duplicates():
    assert find_max([4, 4, 4, 8, 8]) == 8
