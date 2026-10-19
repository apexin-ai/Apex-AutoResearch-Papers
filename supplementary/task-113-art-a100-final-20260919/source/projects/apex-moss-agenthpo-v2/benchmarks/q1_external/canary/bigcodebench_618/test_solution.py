import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import matplotlib

class TestCases(unittest.TestCase):

    def test_case_1(self):
        df, plots = task_func(5, 3)
        self.assertEqual(df.shape, (5, 3))
        self.assertListEqual(list(df.columns), ['Team', 'Goals', 'Penalty Cost'])
        self.assertTrue((df['Goals'] <= 5).all())
        self.assertTrue((df['Penalty Cost'] <= 3000).all())
        self.assertIsInstance(plots[0], matplotlib.axes.Axes)
        self.assertIsInstance(plots[1], matplotlib.axes.Axes)
