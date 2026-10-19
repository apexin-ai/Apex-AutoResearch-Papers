from solution import get_last_element


def test_last_of_many():
    assert get_last_element([10, 20, 30]) == 30


def test_last_of_single():
    assert get_last_element([7]) == 7


def test_last_of_strings():
    assert get_last_element(["a", "b", "c"]) == "c"
