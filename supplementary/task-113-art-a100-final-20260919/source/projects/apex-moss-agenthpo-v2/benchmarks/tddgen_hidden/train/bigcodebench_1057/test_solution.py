import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import random

class TestCases(unittest.TestCase):
    """Tests for the function task_func."""

    def test_default_input(self):
        """Test with default inputs for animals and foods."""
        random.seed(0)
        result = task_func()
        self.assertEqual(result.shape, (10, 7), 'The shape of the DataFrame with default inputs is not as expected.')
