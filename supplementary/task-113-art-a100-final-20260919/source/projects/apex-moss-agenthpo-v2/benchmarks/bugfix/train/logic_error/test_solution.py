from solution import is_prime


def test_prime_numbers():
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(13) is True


def test_non_prime_numbers():
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(15) is False


def test_edge_cases():
    assert is_prime(0) is False
    assert is_prime(1) is False
