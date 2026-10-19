import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert check(70) == False

def test_case_1():
    assert check(23) == False

def test_case_2():
    assert check(73) == True
