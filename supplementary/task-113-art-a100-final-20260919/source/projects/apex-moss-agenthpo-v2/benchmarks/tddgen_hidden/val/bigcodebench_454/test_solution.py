import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch

class TestCases(unittest.TestCase):

    def setUp(self):
        self.src_dir = TemporaryDirectory()
        self.dest_dir = TemporaryDirectory()

    def tearDown(self):
        self.src_dir.cleanup()
        self.dest_dir.cleanup()

    def test_move_no_files(self):
        files_moved = task_func(self.src_dir.name, self.dest_dir.name, 'txt')
        self.assertEqual(len(files_moved), 0, 'Should return an empty list when no files are moved.')

    def create_temp_file(self, directory, filename, content=''):
        """Helper method to create a temporary file with specified content."""
        path = os.path.join(directory, filename)
        with open(path, 'w') as f:
            f.write(content)
        return path
