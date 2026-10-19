import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert find_Max_Num([1,2,3],3) == 321

def test_case_1():
    assert find_Max_Num([4,5,6,1],4) == 6541

def test_case_2():
    assert find_Max_Num([1,2,3,9],4) == 9321
