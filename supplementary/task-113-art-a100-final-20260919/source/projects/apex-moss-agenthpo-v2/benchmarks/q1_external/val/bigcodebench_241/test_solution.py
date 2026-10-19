import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        original = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
        arr, norm_arr, ax = task_func(original)
        np.testing.assert_array_equal(arr, np.array([1, 2, 3, 4]))
        np.testing.assert_allclose(norm_arr, np.array([0.18257419, 0.36514837, 0.54772256, 0.73029674]))
        self.assertEqual(ax.get_title(), 'Original vs. Normalized Data')
        self.assertTrue('Original' in [line.get_label() for line in ax.lines])
        self.assertTrue('Normalized' in [line.get_label() for line in ax.lines])
