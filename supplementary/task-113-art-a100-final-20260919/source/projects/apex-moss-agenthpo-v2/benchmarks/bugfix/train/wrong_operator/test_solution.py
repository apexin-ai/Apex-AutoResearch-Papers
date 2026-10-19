import math
from solution import circle_area


def test_unit_circle():
    assert abs(circle_area(1) - math.pi) < 1e-9


def test_radius_5():
    assert abs(circle_area(5) - 25 * math.pi) < 1e-9


def test_radius_0():
    assert circle_area(0) == 0.0
