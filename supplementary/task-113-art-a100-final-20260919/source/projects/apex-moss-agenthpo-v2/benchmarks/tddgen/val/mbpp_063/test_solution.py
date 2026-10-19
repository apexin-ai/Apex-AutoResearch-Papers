import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7

def test_case_1():
    assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15

def test_case_2():
    assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23
