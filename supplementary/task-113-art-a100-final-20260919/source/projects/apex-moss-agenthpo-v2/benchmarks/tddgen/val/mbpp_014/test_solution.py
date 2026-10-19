import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert find_Volume(10,8,6) == 240

def test_case_1():
    assert find_Volume(3,2,2) == 6

def test_case_2():
    assert find_Volume(1,2,1) == 1
