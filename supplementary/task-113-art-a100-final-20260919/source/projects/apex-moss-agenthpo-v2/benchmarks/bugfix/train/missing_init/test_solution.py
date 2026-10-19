from solution import Counter


def test_default_start():
    c = Counter()
    assert c.get_value() == 0


def test_custom_start():
    c = Counter(start=10)
    assert c.get_value() == 10


def test_increment():
    c = Counter()
    c.increment()
    c.increment(5)
    assert c.get_value() == 6
