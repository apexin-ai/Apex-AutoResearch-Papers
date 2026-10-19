import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertTrue(ax.get_legend() is not None)
