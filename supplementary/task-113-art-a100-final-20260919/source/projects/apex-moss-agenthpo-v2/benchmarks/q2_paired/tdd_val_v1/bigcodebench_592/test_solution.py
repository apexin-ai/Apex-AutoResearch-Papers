import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import os
import shutil
FILE_PATH = os.path.join(OUTPUT_DIR, 'sensor_data.csv')

class TestCases(unittest.TestCase):

    def tearDown(self):
        """Clean up any files created during the tests."""
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)

    def test_csv_file_creation(self):
        """Test if the CSV file is successfully created."""
        task_func(1)
        self.assertTrue(os.path.exists(FILE_PATH))
