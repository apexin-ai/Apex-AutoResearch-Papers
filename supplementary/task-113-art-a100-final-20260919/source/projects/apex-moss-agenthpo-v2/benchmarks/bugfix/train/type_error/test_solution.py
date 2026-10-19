from solution import build_label


def test_basic_label():
    assert build_label("Alice", 30) == "Name: Alice, Age: 30"


def test_zero_age():
    assert build_label("Baby", 0) == "Name: Baby, Age: 0"


def test_large_age():
    assert build_label("Elder", 105) == "Name: Elder, Age: 105"
