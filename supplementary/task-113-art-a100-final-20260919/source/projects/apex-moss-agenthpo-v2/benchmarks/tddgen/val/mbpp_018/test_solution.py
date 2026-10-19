import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(10)

def test_case_0():
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'

def test_case_1():
    assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'

def test_case_2():
    assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'
