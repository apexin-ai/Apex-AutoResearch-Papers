from solution import sum_1_to_n


def test_sum_1_to_5():
    assert sum_1_to_n(5) == 15


def test_sum_1_to_1():
    assert sum_1_to_n(1) == 1


def test_sum_1_to_100():
    assert sum_1_to_n(100) == 5050
