import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import os
import csv
import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        """Set up test environment; create the directory and file."""
        self.file_path = 'task_func_data/Output.txt'
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Temperature', 'Humidity'])

    def tearDown(self):
        """Clean up after tests; remove the file and directory."""
        os.remove(self.file_path)
        os.rmdir('task_func_data')

    def test_return_value(self):
        self.assertEqual(task_func(), self.file_path)
