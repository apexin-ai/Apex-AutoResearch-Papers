"""Smoke tests for the 4 run_circus.py fixes (D007 GPU guard, D010 binarize, css import, metric_fn).

Runs without GPU/torch by mocking heavy dependencies.
"""

import os
import sys
import types

# Ensure artifacts/ is on the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Mock torch and model_adapter so we can import run_circus without GPU
_torch_mock = types.ModuleType("torch")
_torch_mock.Tensor = type("Tensor", (), {})
_torch_mock.manual_seed = lambda x: None
sys.modules["torch"] = _torch_mock

_ma_mock = types.ModuleType("model_adapter")
_ma_mock.CANONICAL_VERSION = "v0.3"
_ma_mock.ModelAdapter = type("ModelAdapter", (), {})
sys.modules["model_adapter"] = _ma_mock


def test_fix1_gpu_guard():
    """Fix 1: GPU guard sets CUDA_VISIBLE_DEVICES before torch import."""
    import run_circus
    assert "CUDA_VISIBLE_DEVICES" in os.environ, "CUDA_VISIBLE_DEVICES not set"
    assert run_circus.DEFAULT_CONFIG["gpu_id"] == "5", "gpu_id missing from config"
    print("PASS: GPU guard — CUDA_VISIBLE_DEVICES set, gpu_id in config")


def test_fix2_binarize_d010():
    """Fix 2: Per-method binarize defaults, IFR uses unique_score_rank (D010)."""
    import run_circus
    bconf = run_circus.DEFAULT_CONFIG["binarize"]

    assert bconf["eap_ig"]["strategy"] == "topn", f"eap_ig strategy wrong: {bconf['eap_ig']}"
    assert bconf["eap_ig"]["n"] == 200

    assert bconf["edge_pruning"]["strategy"] == "topn", f"edge_pruning strategy wrong: {bconf['edge_pruning']}"
    assert bconf["edge_pruning"]["n"] == 200

    assert bconf["ifr"]["strategy"] == "unique_score_rank", f"ifr strategy wrong: {bconf['ifr']}"
    assert bconf["ifr"]["n"] == 50

    # Test _binarize_method dispatches correctly for IFR-style tied scores
    tied_scores = {f"L0.H{h}->L1.H{h2}": 0.5 for h in range(8) for h2 in range(8)}
    tied_scores["L0.H0->L2.H0"] = 0.9
    tied_scores["L0.H1->L2.H1"] = 0.8
    cfg = {"binarize": {"ifr": {"strategy": "unique_score_rank", "n": 2}}}
    result = run_circus._binarize_method(tied_scores, "ifr", cfg)
    assert "L0.H0->L2.H0" in result, "unique_score_rank should include 0.9 edge"
    assert "L0.H1->L2.H1" in result, "unique_score_rank should include 0.8 edge"
    tied_count = sum(1 for e in result if "L1" in e)
    assert tied_count == 0, f"unique_score_rank n=2 should not include tied 0.5 edges, got {tied_count}"
    print("PASS: Binarize D010 — IFR uses unique_score_rank, tied scores handled correctly")


def test_fix3_css_import():
    """Fix 3: css.py functions imported, no inline binarize()."""
    import run_circus

    from css import binarize_scores, compute_css_matrix, circus_score
    assert callable(binarize_scores)
    assert callable(compute_css_matrix)
    assert callable(circus_score)

    assert not hasattr(run_circus, "binarize"), "Old inline binarize() should be removed"
    assert hasattr(run_circus, "_binarize_method"), "_binarize_method should exist"
    print("PASS: css.py imported, inline binarize removed")


def test_fix4_metric_fn():
    """Fix 4: make_metric_fn returns non-None callable."""
    import run_circus

    assert hasattr(run_circus, "make_metric_fn"), "make_metric_fn should exist"

    class MockTokenizer:
        def encode(self, text, add_special_tokens=False):
            return [hash(text) % 1000]

    tok = MockTokenizer()

    fn_ioi = run_circus.make_metric_fn("ioi", tok)
    assert fn_ioi is not None, "metric_fn for ioi should not be None"
    assert callable(fn_ioi), "metric_fn should be callable"

    fn_gt = run_circus.make_metric_fn("greater_than", tok)
    assert fn_gt is not None, "metric_fn for greater_than should not be None"
    assert callable(fn_gt), "metric_fn should be callable"

    try:
        run_circus.make_metric_fn("unknown_task", tok)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    print("PASS: metric_fn — non-None, callable for ioi and greater_than")


if __name__ == "__main__":
    test_fix1_gpu_guard()
    test_fix2_binarize_d010()
    test_fix3_css_import()
    test_fix4_metric_fn()
    print("\nAll 4 fix smoke tests passed.")
