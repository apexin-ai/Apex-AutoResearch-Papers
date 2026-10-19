import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert is_Diff (12345) == False

def test_case_1():
    assert is_Diff(1212112) == True

def test_case_2():
    assert is_Diff(1212) == False
