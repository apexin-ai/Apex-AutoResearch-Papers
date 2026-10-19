import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
from unittest.mock import patch
import matplotlib.pyplot as plt
import os

class TestCases(unittest.TestCase):
    """Test cases for task_func."""

    def tearDown(self):
        """Clean up by removing files created during tests."""
        plt.close()
        if os.path.exists('test_output.png'):
            os.remove('test_output.png')

    @patch('pandas.read_csv')
    def test_display_plot(self, mock_read_csv):
        """
        Test if the function displays a plot correctly when no save path is provided.
        """
        mock_read_csv.return_value = pd.DataFrame({'Text': ['word1 word2 word3', 'word2 word3 word4']})
        result = task_func('dummy_path.csv')
        print(result)
        self.assertIsNotNone(result)
