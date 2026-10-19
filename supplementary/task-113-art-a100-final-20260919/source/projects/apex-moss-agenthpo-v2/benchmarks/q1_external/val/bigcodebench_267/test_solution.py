import pytest

from solution import *  # noqa: F401,F403

pytestmark = pytest.mark.timeout(20)

import unittest
import doctest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = {'key1': 1, 'key2': 2, 'key3': 3}
        fft, ax = task_func(data)
        self.assertIn('a', data)
        self.assertIsInstance(fft, np.ndarray)
        self.assertEqual(ax.get_title(), 'FFT of the Signal')
        self.assertEqual(ax.get_xlabel(), 'Frequency [Hz]')
        self.assertEqual(ax.get_ylabel(), 'Frequency Spectrum Magnitude')
