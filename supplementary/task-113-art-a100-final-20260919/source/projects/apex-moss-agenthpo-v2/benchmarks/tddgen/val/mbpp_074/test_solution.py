import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True

def test_case_1():
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False

def test_case_2():
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False
