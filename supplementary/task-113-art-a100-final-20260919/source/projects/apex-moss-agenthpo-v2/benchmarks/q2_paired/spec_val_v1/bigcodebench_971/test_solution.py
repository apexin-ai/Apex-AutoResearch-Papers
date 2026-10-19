import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import tempfile
import os
from datetime import datetime, timezone, timedelta

class TestCases(unittest.TestCase):

    def setUp(self):
        self.before_creation = datetime.now(timezone.utc) - timedelta(seconds=1)
        self.test_dir = tempfile.TemporaryDirectory()
        self.files = {'empty.txt': 0, 'small.txt': 5, 'medium.txt': 50, 'large.txt': 500, 'utc_test.txt': 10}
        for file_name, size in self.files.items():
            path = os.path.join(self.test_dir.name, file_name)
            with open(path, 'wb') as f:
                f.write(os.urandom(size))

    def tearDown(self):
        self.test_dir.cleanup()

    def test_case_1(self):
        result = task_func(self.test_dir.name)
        self.assertEqual(len(result), len(self.files))
