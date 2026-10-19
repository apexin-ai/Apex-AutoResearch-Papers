import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert bell_number(2)==2

def test_case_1():
    assert bell_number(10)==115975

def test_case_2():
    assert bell_number(56)==6775685320645824322581483068371419745979053216268760300
