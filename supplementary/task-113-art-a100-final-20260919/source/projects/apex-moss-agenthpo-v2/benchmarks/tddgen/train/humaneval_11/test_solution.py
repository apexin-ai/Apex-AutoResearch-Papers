import pytest

from solution import string_xor as candidate

pytestmark = pytest.mark.timeout(10)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_solution():
    check(candidate)
