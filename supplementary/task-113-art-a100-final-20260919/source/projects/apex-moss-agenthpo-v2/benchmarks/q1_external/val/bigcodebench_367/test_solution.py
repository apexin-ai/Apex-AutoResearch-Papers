import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        activities = [datetime(2023, 10, 23), datetime(2023, 10, 24)]
        ax = task_func(activities)
        bars = ax.patches
        self.assertEqual(ax.get_title(), 'Weekly Activity')
        self.assertEqual(ax.get_xlabel(), 'Day of the Week')
        self.assertEqual(ax.get_ylabel(), 'Number of Activities')
        self.assertEqual(bars[0].get_height(), 1)
        self.assertEqual(bars[1].get_height(), 1)
        for i in range(2, 7):
            self.assertEqual(bars[i].get_height(), 0)
