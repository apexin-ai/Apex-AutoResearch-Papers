import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import matplotlib

class TestCases(unittest.TestCase):

    def test_non_empty_lists(self):
        """Test with valid non-empty lists."""
        ax = task_func([1, 2, 3], ['A', 'B', 'C'])
        self.assertIsInstance(ax, matplotlib.axes.Axes)
