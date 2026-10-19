import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert is_Monotonic([6, 5, 4, 4]) == True

def test_case_1():
    assert is_Monotonic([1, 2, 2, 3]) == True

def test_case_2():
    assert is_Monotonic([1, 3, 2]) == False
