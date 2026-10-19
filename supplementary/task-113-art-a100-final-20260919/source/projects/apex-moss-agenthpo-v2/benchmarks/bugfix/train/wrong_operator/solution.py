import math


def circle_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * (radius * 2)  # BUG: should be radius ** 2 (squared), not radius * 2 (doubled)
