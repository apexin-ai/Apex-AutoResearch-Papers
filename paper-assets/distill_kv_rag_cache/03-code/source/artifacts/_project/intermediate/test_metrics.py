"""Unit tests for compresslink.metrics."""

import unittest

from compresslink.metrics import compute_exact_match, compute_f1, normalize_answer


class TestNormalizeAnswer(unittest.TestCase):
    def test_lowercase(self):
        self.assertEqual(normalize_answer("Barack Obama"), "barack obama")

    def test_articles(self):
        self.assertEqual(normalize_answer("the United States of America"), "united states of america")

    def test_punctuation(self):
        self.assertEqual(normalize_answer("hello, world!"), "hello world")

    def test_whitespace(self):
        self.assertEqual(normalize_answer("  foo   bar  "), "foo bar")

    def test_combined(self):
        self.assertEqual(normalize_answer("The cat's pajamas!"), "cats pajamas")

    def test_empty(self):
        self.assertEqual(normalize_answer(""), "")


class TestExactMatch(unittest.TestCase):
    def test_exact(self):
        self.assertEqual(compute_exact_match("Barack Obama", ["Barack Obama"]), 1.0)

    def test_case_insensitive(self):
        self.assertEqual(compute_exact_match("barack obama", ["Barack Obama"]), 1.0)

    def test_article_removal(self):
        self.assertEqual(compute_exact_match("the president", ["president"]), 1.0)

    def test_no_match(self):
        self.assertEqual(compute_exact_match("George Bush", ["Barack Obama"]), 0.0)

    def test_multiple_answers(self):
        self.assertEqual(
            compute_exact_match("NYC", ["New York City", "NYC", "New York"]), 1.0
        )

    def test_multiple_no_match(self):
        self.assertEqual(
            compute_exact_match("LA", ["New York City", "NYC"]), 0.0
        )


class TestF1(unittest.TestCase):
    def test_perfect(self):
        self.assertAlmostEqual(compute_f1("Barack Obama", ["Barack Obama"]), 1.0)

    def test_partial(self):
        f1 = compute_f1("Barack Hussein Obama", ["Barack Obama"])
        self.assertGreater(f1, 0.5)
        self.assertLess(f1, 1.0)

    def test_no_overlap(self):
        self.assertAlmostEqual(compute_f1("cat", ["dog"]), 0.0)

    def test_multiple_answers(self):
        f1 = compute_f1("New York", ["New York City", "NYC"])
        self.assertGreater(f1, 0.5)

    def test_empty_prediction(self):
        self.assertAlmostEqual(compute_f1("", ["Barack Obama"]), 0.0)

    def test_subset_tokens(self):
        # "obama" is 1 of 2 answer tokens → precision=1.0, recall=0.5, F1=0.667
        f1 = compute_f1("obama", ["Barack Obama"])
        self.assertAlmostEqual(f1, 2 / 3, places=3)


if __name__ == "__main__":
    unittest.main()
