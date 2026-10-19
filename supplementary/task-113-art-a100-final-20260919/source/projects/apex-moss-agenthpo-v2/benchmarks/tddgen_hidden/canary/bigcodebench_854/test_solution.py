import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result, perm = task_func([1, 2])
        expected = [3, 3]
        expected_perm = [(2, 1), (1, 2)]
        self.assertEqual(result, expected)
        self.assertCountEqual(perm, expected_perm)
