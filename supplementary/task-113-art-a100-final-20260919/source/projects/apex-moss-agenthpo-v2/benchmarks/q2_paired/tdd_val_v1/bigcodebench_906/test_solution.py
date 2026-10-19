import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.source_dir = 'task_func_data/'
        self.target_dir = 'task_func_data_target/'
        if os.path.exists(self.source_dir):
            shutil.rmtree(self.source_dir)
        if os.path.exists(self.target_dir):
            shutil.rmtree(self.target_dir)
        os.makedirs(self.source_dir)
        os.makedirs(self.target_dir)

    def tearDown(self):
        if os.path.exists(self.source_dir):
            shutil.rmtree(self.source_dir)
        if os.path.exists(self.target_dir):
            shutil.rmtree(self.target_dir)

    def test_case_1(self):
        test_files = ['file1.txt', 'file2_processed.txt']
        for file in test_files:
            with open(os.path.join(self.source_dir, file), 'w') as f:
                f.write(f'This is {file}')
        archive_path = task_func(self.source_dir, self.target_dir)
        with zipfile.ZipFile(archive_path, 'r') as archive:
            self.assertIn('file2_processed.txt', archive.namelist())
