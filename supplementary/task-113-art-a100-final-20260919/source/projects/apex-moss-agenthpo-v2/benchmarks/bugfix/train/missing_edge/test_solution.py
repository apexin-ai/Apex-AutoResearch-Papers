from solution import first_of_reversed


def test_reverse_normal():
    assert first_of_reversed([1, 2, 3]) == 3


def test_reverse_single():
    assert first_of_reversed([42]) == 42


def test_reverse_empty():
    # Should return None for empty list instead of crashing
    assert first_of_reversed([]) is None
