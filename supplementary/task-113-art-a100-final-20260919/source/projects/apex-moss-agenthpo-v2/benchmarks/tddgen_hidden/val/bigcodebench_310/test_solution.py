import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import os
import csv
from statistics import mean

class TestCases(unittest.TestCase):

    def tearDown(self):
        """Remove the generated CSV file after each test."""
        os.remove(self.filename)

    def test_file_creation(self):
        """Test if the file is created successfully."""
        random.seed(0)
        self.filename = 'test_file_creation.csv'
        path = task_func(self.filename)
        self.assertTrue(os.path.exists(path))
