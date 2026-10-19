import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert dif_Square(5) == True

def test_case_1():
    assert dif_Square(10) == False

def test_case_2():
    assert dif_Square(15) == True
