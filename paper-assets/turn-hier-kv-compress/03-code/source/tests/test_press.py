"""Tests for TurnKV press — EASS aggregation, budget computation, and score mapping.

No torch/kvpress/GPU required. Uses a numpy-backed torch shim.
Run: python3 tests/test_press.py
"""

import sys
import os
import unittest
from unittest.mock import MagicMock

# Insert our shim as "torch" before any turnkv imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import torch_shim
sys.modules["torch"] = torch_shim

# Now src/ imports will resolve "import torch" to our shim
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from turnkv.eass import (
    Segment,
    compute_budget,
    compute_eass,
    map_budget_to_scores,
    _get_b_prior,
)
from turnkv.press import TurnKVPress

torch = torch_shim


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_segments():
    """3-turn conversation: system(0), user(1), assistant(1), tool_result(2), thinking(2)."""
    return [
        Segment("SYSTEM_PROMPT",     start_idx=0,  end_idx=10,  turn_index=0),
        Segment("USER_MESSAGE",      start_idx=10, end_idx=25,  turn_index=1),
        Segment("ASSISTANT_MESSAGE", start_idx=25, end_idx=40,  turn_index=1),
        Segment("TOOL_RESULT",       start_idx=40, end_idx=55,  turn_index=2),
        Segment("THINKING_TRACE",    start_idx=55, end_idx=70,  turn_index=2),
    ]


def _make_ea_scores(seq_len=70, batch=1, heads=2):
    t = torch.linspace(0.1, 1.0, seq_len)
    return t.unsqueeze(0).unsqueeze(0).expand(batch, heads, seq_len).clone()


# ---------------------------------------------------------------------------
# EASS aggregation
# ---------------------------------------------------------------------------

class TestComputeEASS(unittest.TestCase):

    def test_shape(self):
        eass = compute_eass(_make_ea_scores(), _make_segments())
        self.assertEqual(eass.shape, (1, 2, 5))

    def test_mean_correctness(self):
        ea = _make_ea_scores()
        segments = _make_segments()
        eass = compute_eass(ea, segments)
        for i, seg in enumerate(segments):
            expected = ea[0, 0, seg.start_idx:seg.end_idx].mean().item()
            actual = eass[0, 0, i].item()
            self.assertAlmostEqual(actual, expected, places=5,
                                   msg=f"Segment {i}")

    def test_empty_segment(self):
        seg = [Segment("USER_MESSAGE", start_idx=5, end_idx=5, turn_index=0)]
        eass = compute_eass(_make_ea_scores(seq_len=10), seg)
        self.assertEqual(eass[0, 0, 0].item(), 0.0)


# ---------------------------------------------------------------------------
# Budget computation
# ---------------------------------------------------------------------------

class TestComputeBudget(unittest.TestCase):

    def test_shape(self):
        segments = _make_segments()
        eass = torch.rand(1, 2, len(segments))
        budgets = compute_budget(segments, eass)
        self.assertEqual(budgets.shape, eass.shape)

    def test_clipping(self):
        segments = _make_segments()
        eass = torch.rand(1, 2, len(segments))
        budgets = compute_budget(segments, eass, b_min=0.1, b_max=1.0)
        self.assertGreaterEqual(budgets.min().item(), 0.1 - 1e-6)
        self.assertLessEqual(budgets.max().item(), 1.0 + 1e-6)

    def test_system_prompt_highest_prior(self):
        segments = _make_segments()
        eass = torch.ones(1, 1, len(segments))
        budgets = compute_budget(segments, eass, beta=0.0)
        self.assertAlmostEqual(budgets[0, 0, 0].item(), 1.0, places=5)

    def test_bucket_recency_via_b_prior(self):
        """Recency is encoded in B_prior buckets, not continuous decay."""
        segments = [
            Segment("TOOL_RESULT", start_idx=0,  end_idx=10, turn_index=0),  # older
            Segment("TOOL_RESULT", start_idx=10, end_idx=20, turn_index=5),  # recent
        ]
        eass = torch.ones(1, 1, 2)
        budgets = compute_budget(segments, eass, beta=0.0, max_turn=5)
        # older TOOL_RESULT=0.5, recent TOOL_RESULT=0.8
        self.assertAlmostEqual(budgets[0, 0, 0].item(), 0.5, places=3)
        self.assertAlmostEqual(budgets[0, 0, 1].item(), 0.8, places=3)

    def test_thinking_trace_old_low_prior(self):
        self.assertEqual(_get_b_prior("THINKING_TRACE", turn_index=0, max_turn=5), 0.15)
        self.assertEqual(_get_b_prior("THINKING_TRACE", turn_index=4, max_turn=5), 0.4)

    def test_beta_sensitivity(self):
        segments = _make_segments()
        eass = torch.tensor([[[0.1, 0.5, 0.5, 0.5, 0.9]]])
        b_low = compute_budget(segments, eass, beta=0.0)
        b_high = compute_budget(segments, eass, beta=2.0)
        spread_low = (b_low.max().item() - b_low.min().item())
        spread_high = (b_high.max().item() - b_high.min().item())
        self.assertGreaterEqual(spread_high, spread_low)


# ---------------------------------------------------------------------------
# Score mapping
# ---------------------------------------------------------------------------

class TestMapBudgetToScores(unittest.TestCase):

    def test_shape_preserved(self):
        ea = _make_ea_scores()
        segments = _make_segments()
        budgets = torch.ones(1, 2, len(segments))
        out = map_budget_to_scores(ea, segments, budgets)
        self.assertEqual(out.shape, ea.shape)

    def test_budget_one_preserves_scores(self):
        ea = _make_ea_scores()
        segments = _make_segments()
        budgets = torch.ones(1, 2, len(segments))
        out = map_budget_to_scores(ea, segments, budgets)
        self.assertTrue(torch.allclose(out, ea))

    def test_higher_budget_higher_scores(self):
        ea = torch.ones(1, 1, 20)
        segments = [
            Segment("SYSTEM_PROMPT", start_idx=0,  end_idx=10, turn_index=0),
            Segment("USER_MESSAGE",  start_idx=10, end_idx=20, turn_index=0),
        ]
        budgets = torch.tensor([[[1.0, 0.2]]])
        out = map_budget_to_scores(ea, segments, budgets)
        self.assertGreater(out[0, 0, 0].item(), out[0, 0, 10].item())

    def test_relative_ordering_within_segment(self):
        ea = _make_ea_scores()
        segments = _make_segments()
        budgets = torch.rand(1, 2, len(segments)).clamp(0.1, 1.0)
        out = map_budget_to_scores(ea, segments, budgets)
        for seg in segments:
            s, e = seg.start_idx, seg.end_idx
            original = ea[0, 0, s:e]
            modulated = out[0, 0, s:e]
            self.assertTrue(torch.equal(original.argsort(), modulated.argsort()))


# ---------------------------------------------------------------------------
# TurnKVPress.score() integration
# ---------------------------------------------------------------------------

class TestTurnKVPressScore(unittest.TestCase):

    def _make_press(self, segments=None):
        mock_ea = MagicMock()
        mock_ea.score = MagicMock(return_value=_make_ea_scores())
        press = TurnKVPress(compression_ratio=0.5)
        press._ea_press = mock_ea
        if segments:
            press.set_segments(segments)
        return press, mock_ea

    def test_no_segments_returns_raw_ea(self):
        press, mock_ea = self._make_press(segments=None)
        result = press.score(None, None, None, None, None, {})
        mock_ea.score.assert_called_once()
        self.assertTrue(torch.equal(result, mock_ea.score.return_value))

    def test_with_segments_modulates_scores(self):
        segments = _make_segments()
        press, mock_ea = self._make_press(segments=segments)
        result = press.score(None, None, None, None, None, {})
        mock_ea.score.assert_called_once()
        raw = mock_ea.score.return_value
        self.assertEqual(result.shape, raw.shape)
        self.assertFalse(torch.equal(result, raw))

    def test_set_segments(self):
        press, _ = self._make_press()
        self.assertIsNone(press.segments)
        segments = _make_segments()
        press.set_segments(segments)
        self.assertIs(press.segments, segments)

    def test_compression_ratio_field(self):
        press = TurnKVPress(compression_ratio=0.7)
        self.assertEqual(press.compression_ratio, 0.7)

    def test_is_dataclass(self):
        from dataclasses import fields
        press = TurnKVPress(compression_ratio=0.5)
        field_names = {f.name for f in fields(press)}
        self.assertIn("compression_ratio", field_names)
        self.assertIn("beta", field_names)


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main(verbosity=2)
