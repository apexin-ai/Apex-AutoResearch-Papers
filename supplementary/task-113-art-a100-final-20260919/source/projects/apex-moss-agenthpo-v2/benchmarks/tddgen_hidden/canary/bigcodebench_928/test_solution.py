import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = task_func('abcdef')
        self.assertEqual(result['ab'], 1)
        self.assertEqual(result['ac'], 0)
        self.assertEqual(result['bc'], 1)
        self.assertEqual(result['cb'], 0)
        self.assertEqual(result['zz'], 0)
