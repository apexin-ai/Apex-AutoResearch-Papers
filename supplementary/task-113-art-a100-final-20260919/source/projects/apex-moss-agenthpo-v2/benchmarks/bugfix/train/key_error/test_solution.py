from solution import get_full_name


def test_full_name():
    assert get_full_name({"first_name": "Alice", "last_name": "Smith"}) == "Alice Smith"


def test_missing_last_name():
    assert get_full_name({"first_name": "Alice"}) == "Alice"


def test_empty_dict():
    assert get_full_name({}) == "Unknown"


def test_missing_first_name():
    assert get_full_name({"last_name": "Smith"}) == "Unknown Smith"
