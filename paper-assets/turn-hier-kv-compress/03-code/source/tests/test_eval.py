"""Tests for eval metrics — pure logic, no GPU required.
Run: python tests/test_eval.py
"""

import os
import sys
import unittest

_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _root not in sys.path:
    sys.path.insert(0, _root)

from eval.metrics import check_info_retained, compute_kirr, compute_summary


# ---------------------------------------------------------------------------
# check_info_retained
# ---------------------------------------------------------------------------


class TestCheckInfoRetained(unittest.TestCase):
    def test_exact_match(self):
        self.assertTrue(check_info_retained("sk-test-abc123", "sk-test-abc123"))

    def test_substring(self):
        self.assertTrue(
            check_info_retained("The key is sk-test-abc123 ok", "sk-test-abc123")
        )

    def test_case_insensitive(self):
        self.assertTrue(
            check_info_retained("The KEY is SK-Test-ABC123", "sk-test-abc123")
        )

    def test_whitespace_normalization(self):
        self.assertTrue(
            check_info_retained("rate_limit=100  req/min", "rate_limit=100 req/min")
        )

    def test_no_match(self):
        self.assertFalse(
            check_info_retained("The key is sk-test-xyz", "sk-test-abc123")
        )

    def test_empty_expected(self):
        self.assertTrue(check_info_retained("anything", ""))

    def test_empty_generated(self):
        self.assertFalse(check_info_retained("", "something"))

    def test_multiline(self):
        self.assertTrue(
            check_info_retained(
                "line1\nline2\nsk-test-abc123\nline4", "sk-test-abc123"
            )
        )

    def test_leading_trailing_spaces(self):
        self.assertTrue(
            check_info_retained("  sk-test-abc123  ", "  sk-test-abc123  ")
        )

    def test_tabs_and_newlines_in_expected(self):
        self.assertTrue(
            check_info_retained("rate limit 100 req", "rate\tlimit\n100 req")
        )


# ---------------------------------------------------------------------------
# compute_kirr
# ---------------------------------------------------------------------------


class TestComputeKirr(unittest.TestCase):
    def test_basic_grouping(self):
        results = [
            {"method": "full", "compression_ratio": 0.0, "case_type": "standard", "retained": True},
            {"method": "full", "compression_ratio": 0.0, "case_type": "standard", "retained": True},
            {"method": "full", "compression_ratio": 0.0, "case_type": "standard", "retained": False},
            {"method": "uniform_ea", "compression_ratio": 0.7, "case_type": "standard", "retained": True},
            {"method": "uniform_ea", "compression_ratio": 0.7, "case_type": "standard", "retained": False},
        ]
        out = compute_kirr(results)
        self.assertAlmostEqual(out["standard"][("full", 0.0)]["kirr"], 2 / 3)
        self.assertAlmostEqual(out["standard"][("uniform_ea", 0.7)]["kirr"], 0.5)
        self.assertEqual(out["standard"][("full", 0.0)]["n"], 3)

    def test_multiple_case_types(self):
        results = [
            {"method": "turnkv", "compression_ratio": 0.7, "case_type": "standard", "retained": True},
            {"method": "turnkv", "compression_ratio": 0.7, "case_type": "adversarial", "retained": False},
        ]
        out = compute_kirr(results)
        self.assertEqual(out["standard"][("turnkv", 0.7)]["kirr"], 1.0)
        self.assertEqual(out["adversarial"][("turnkv", 0.7)]["kirr"], 0.0)

    def test_empty(self):
        self.assertEqual(compute_kirr([]), {})


# ---------------------------------------------------------------------------
# compute_summary
# ---------------------------------------------------------------------------


def _make_pass_results():
    """Two traces, TurnKV clearly better -> PASS."""
    rows = []
    for tid, ct in [("t1", "standard"), ("t2", "adversarial")]:
        ppl_full = 5.0 if ct == "standard" else 5.5
        rows.append(
            {
                "trace_id": tid, "case_type": ct, "method": "full",
                "compression_ratio": 0.0, "kirr": 1.0,
                "ppl_full": ppl_full, "ppl_compressed": ppl_full, "ppl_ratio": 1.0,
                "num_planted": 5, "num_retained": 5,
            }
        )
        for cr in [0.7, 0.85]:
            ea_kirr = 0.6
            tk_kirr = 0.92
            ea_ppl = ppl_full * 1.3
            tk_ppl = ppl_full * 1.2
            for method, kirr, ppl in [
                ("uniform_ea", ea_kirr, ea_ppl),
                ("turnkv", tk_kirr, tk_ppl),
            ]:
                rows.append(
                    {
                        "trace_id": tid, "case_type": ct, "method": method,
                        "compression_ratio": cr, "kirr": kirr,
                        "ppl_full": ppl_full, "ppl_compressed": ppl,
                        "ppl_ratio": ppl / ppl_full,
                        "num_planted": 5, "num_retained": int(kirr * 5),
                    }
                )
    return rows


class TestComputeSummary(unittest.TestCase):
    def test_structure(self):
        summary = compute_summary(_make_pass_results(), [0.7, 0.85])
        self.assertIn("compression_ratio_0.7", summary)
        self.assertIn("compression_ratio_0.85", summary)
        self.assertIn("mvp_verdict", summary)

        cr07 = summary["compression_ratio_0.7"]
        self.assertIn("standard", cr07)
        self.assertIn("adversarial", cr07)
        self.assertIn("overall", cr07)

        overall = cr07["overall"]
        for key in ["full", "uniform_ea", "turnkv", "kirr_diff_pp", "ppl_ratio"]:
            self.assertIn(key, overall)

    def test_kirr_diff(self):
        summary = compute_summary(_make_pass_results(), [0.7, 0.85])
        overall_07 = summary["compression_ratio_0.7"]["overall"]
        # turnkv kirr_mean = 0.92, uniform_ea kirr_mean = 0.6 -> diff = 32pp
        self.assertAlmostEqual(overall_07["kirr_diff_pp"], 32.0, places=0)

    def test_ppl_ratio(self):
        summary = compute_summary(_make_pass_results(), [0.7, 0.85])
        overall_07 = summary["compression_ratio_0.7"]["overall"]
        # turnkv_ppl / ea_ppl = 1.2/1.3
        self.assertAlmostEqual(overall_07["ppl_ratio"], 1.2 / 1.3, places=3)

    def test_mvp_pass(self):
        summary = compute_summary(_make_pass_results(), [0.7, 0.85])
        v = summary["mvp_verdict"]
        self.assertEqual(v["overall"], "PASS")
        self.assertTrue(v["kirr_pass"])
        self.assertTrue(v["ppl_pass"])

    def test_mvp_kill(self):
        """All CRs have kirr_diff < 5pp -> KILL."""
        rows = []
        for tid in ["t1", "t2"]:
            rows.append(
                {
                    "trace_id": tid, "case_type": "standard", "method": "full",
                    "compression_ratio": 0.0, "kirr": 1.0,
                    "ppl_full": 5.0, "ppl_compressed": 5.0, "ppl_ratio": 1.0,
                    "num_planted": 5, "num_retained": 5,
                }
            )
            for cr in [0.7, 0.85]:
                rows.append(
                    {
                        "trace_id": tid, "case_type": "standard",
                        "method": "uniform_ea", "compression_ratio": cr,
                        "kirr": 0.6, "ppl_full": 5.0,
                        "ppl_compressed": 6.0, "ppl_ratio": 1.2,
                        "num_planted": 5, "num_retained": 3,
                    }
                )
                rows.append(
                    {
                        "trace_id": tid, "case_type": "standard",
                        "method": "turnkv", "compression_ratio": cr,
                        "kirr": 0.62, "ppl_full": 5.0,
                        "ppl_compressed": 5.9, "ppl_ratio": 1.18,
                        "num_planted": 5, "num_retained": 3,
                    }
                )
        summary = compute_summary(rows, [0.7, 0.85])
        self.assertEqual(summary["mvp_verdict"]["overall"], "KILL")

    def test_mvp_inconclusive(self):
        """kirr_diff between 5pp and 10pp -> INCONCLUSIVE."""
        rows = []
        for tid in ["t1", "t2"]:
            rows.append(
                {
                    "trace_id": tid, "case_type": "standard", "method": "full",
                    "compression_ratio": 0.0, "kirr": 1.0,
                    "ppl_full": 5.0, "ppl_compressed": 5.0, "ppl_ratio": 1.0,
                    "num_planted": 5, "num_retained": 5,
                }
            )
            for cr in [0.7, 0.85]:
                rows.append(
                    {
                        "trace_id": tid, "case_type": "standard",
                        "method": "uniform_ea", "compression_ratio": cr,
                        "kirr": 0.6, "ppl_full": 5.0,
                        "ppl_compressed": 6.0, "ppl_ratio": 1.2,
                        "num_planted": 5, "num_retained": 3,
                    }
                )
                rows.append(
                    {
                        "trace_id": tid, "case_type": "standard",
                        "method": "turnkv", "compression_ratio": cr,
                        "kirr": 0.68, "ppl_full": 5.0,
                        "ppl_compressed": 5.9, "ppl_ratio": 1.18,
                        "num_planted": 5, "num_retained": 3,
                    }
                )
        summary = compute_summary(rows, [0.7, 0.85])
        self.assertEqual(summary["mvp_verdict"]["overall"], "INCONCLUSIVE")

    def test_no_adversarial_traces(self):
        """When all traces are standard, adversarial section is absent."""
        rows = []
        for tid in ["t1", "t2"]:
            rows.append(
                {
                    "trace_id": tid, "case_type": "standard", "method": "full",
                    "compression_ratio": 0.0, "kirr": 1.0,
                    "ppl_full": 5.0, "ppl_compressed": 5.0, "ppl_ratio": 1.0,
                    "num_planted": 5, "num_retained": 5,
                }
            )
            for method, kirr, ppl_c in [("uniform_ea", 0.6, 6.5), ("turnkv", 0.95, 6.4)]:
                rows.append(
                    {
                        "trace_id": tid, "case_type": "standard",
                        "method": method, "compression_ratio": 0.7,
                        "kirr": kirr, "ppl_full": 5.0,
                        "ppl_compressed": ppl_c, "ppl_ratio": ppl_c / 5.0,
                        "num_planted": 5, "num_retained": int(kirr * 5),
                    }
                )
        summary = compute_summary(rows, [0.7])
        self.assertNotIn("adversarial", summary["compression_ratio_0.7"])
        self.assertIn("standard", summary["compression_ratio_0.7"])


if __name__ == "__main__":
    unittest.main()
