"""Smoke tests for CSS binarization and consensus module."""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from css import binarize_scores, compute_css_matrix, circus_score, generate_nonnested_configs


def test_topn_basic():
    scores = {f"e{i}": float(i) for i in range(10)}
    result = binarize_scores(scores, "topn", n=3)
    assert result == {"e9", "e8", "e7"}, f"Expected top 3, got {result}"


def test_topn_block_vote_problem():
    """Demonstrate the IFR block-vote problem with topn.
    36 IFR edges share the same score (simulating same src,dst_layer).
    topn=5 arbitrarily picks 5 of the 36, wasting quota on a single group.
    """
    scores = {}
    for i in range(36):
        scores[f"ifr_head_{i}"] = 0.8
    scores["eap_important_1"] = 0.75
    scores["eap_important_2"] = 0.70
    scores["ep_important_1"] = 0.65

    result = binarize_scores(scores, "topn", n=5)
    assert len(result) == 5
    eap_ep_in = result & {"eap_important_1", "eap_important_2", "ep_important_1"}
    assert len(eap_ep_in) == 0, "topn=5 fills quota with tied IFR edges, excludes EAP/EP"


def test_percentile_threshold_handles_ties():
    """percentile_threshold treats 36 tied IFR edges as 1 unique score value.
    With 4 unique values and percentile=50, cutoff is at index 2 of sorted uniques.
    """
    scores = {}
    for i in range(36):
        scores[f"ifr_head_{i}"] = 0.8
    for i in range(10):
        scores[f"mid_{i}"] = 0.5
    for i in range(20):
        scores[f"low_{i}"] = 0.2
    for i in range(5):
        scores[f"noise_{i}"] = 0.01

    # unique scores: [0.01, 0.2, 0.5, 0.8] (4 values)
    # percentile=75 → cutoff_idx = int(4 * 75/100) = 3 → cutoff = 0.8
    result = binarize_scores(scores, "percentile_threshold", percentile=75)
    assert len(result) == 36, f"All 36 tied IFR edges should be included, got {len(result)}"

    # percentile=50 → cutoff_idx = int(4 * 50/100) = 2 → cutoff = 0.5
    result2 = binarize_scores(scores, "percentile_threshold", percentile=50)
    assert all(f"ifr_head_{i}" in result2 for i in range(36))
    assert all(f"mid_{i}" in result2 for i in range(10))
    assert len(result2) == 46, f"Expected 36+10=46, got {len(result2)}"


def test_unique_score_rank_handles_ties():
    """unique_score_rank with n=2 selects the top 2 unique score values,
    then includes ALL edges at those values.
    """
    scores = {}
    for i in range(36):
        scores[f"ifr_{i}"] = 0.8
    for i in range(10):
        scores[f"eap_{i}"] = 0.6
    for i in range(5):
        scores[f"low_{i}"] = 0.1

    result = binarize_scores(scores, "unique_score_rank", n=2)
    assert len(result) == 46, f"Top 2 unique scores → 36+10=46 edges, got {len(result)}"
    assert all(f"ifr_{i}" in result for i in range(36))
    assert all(f"eap_{i}" in result for i in range(10))
    assert all(f"low_{i}" not in result for i in range(5))


def test_css_matrix_3methods():
    """3 methods with known overlaps."""
    A = {"e1", "e2", "e3", "e4"}
    B = {"e2", "e3", "e5"}
    C = {"e3", "e4", "e5", "e6"}
    all_edges = {"e1", "e2", "e3", "e4", "e5", "e6", "e7"}

    result = compute_css_matrix({"A": A, "B": B, "C": C}, all_edges)

    assert result["css_core"] == {"e3"}, f"Only e3 is in all 3, got {result['css_core']}"

    assert "e7" not in result["off_diagonal"]
    assert "e3" not in result["off_diagonal"]

    expected_off = {"e1", "e2", "e4", "e5", "e6"}
    assert result["off_diagonal"] == expected_off, f"Expected {expected_off}, got {result['off_diagonal']}"

    assert result["per_method_counts"] == {"A": 4, "B": 3, "C": 4}


def test_off_diagonal_pct():
    """off_diagonal_pct = off_diag / (off_diag + core)."""
    A = {"e1", "e2", "e3"}
    B = {"e1", "e2", "e3"}
    all_edges = {"e1", "e2", "e3"}

    result = compute_css_matrix({"A": A, "B": B}, all_edges)
    assert result["off_diagonal_pct"] == 0.0, "Perfect agreement → 0% off-diagonal"

    A2 = {"e1", "e2"}
    B2 = {"e2", "e3"}
    result2 = compute_css_matrix({"A": A2, "B": B2}, {"e1", "e2", "e3"})
    # core={e2}, off_diag={e1,e3}, pct = 2/3
    assert abs(result2["off_diagonal_pct"] - 2 / 3) < 1e-9


def test_circus_score():
    circuits = {"A": {"e1", "e2"}, "B": {"e2", "e3"}, "C": {"e2"}}
    assert circus_score(circuits, "e2") == 1.0
    assert abs(circus_score(circuits, "e1") - 1 / 3) < 1e-9
    assert circus_score(circuits, "e99") == 0.0


def test_empty_scores():
    assert binarize_scores({}, "topn") == set()
    assert binarize_scores({}, "percentile_threshold") == set()


def test_nonnested_antichain_property():
    """Any two configs must be incomparable: no dominance relation."""
    configs = generate_nonnested_configs([0.3, 0.5, 0.7, 0.9], [0.3, 0.5, 0.7, 0.9], B=9)
    assert len(configs) == 9, f"Expected 9 configs, got {len(configs)}"
    for i in range(len(configs)):
        for j in range(len(configs)):
            if i == j:
                continue
            ni, ei = configs[i]
            nj, ej = configs[j]
            dominates = (ni <= nj and ei <= ej)
            assert not dominates, (
                f"Config {i} ({ni:.3f},{ei:.3f}) dominates config {j} ({nj:.3f},{ej:.3f})"
            )


def test_nonnested_respects_range():
    """Output configs stay within the provided threshold ranges."""
    configs = generate_nonnested_configs([0.2, 0.8], [0.1, 0.9], B=5)
    for n, e in configs:
        assert 0.2 <= n <= 0.8, f"Node threshold {n} out of range [0.2, 0.8]"
        assert 0.1 <= e <= 0.9, f"Edge threshold {e} out of range [0.1, 0.9]"


def test_nonnested_deterministic():
    """Same inputs produce same outputs."""
    c1 = generate_nonnested_configs([0.3, 0.9], [0.3, 0.9], B=7, seed=42)
    c2 = generate_nonnested_configs([0.3, 0.9], [0.3, 0.9], B=7, seed=42)
    assert c1 == c2


def test_nonnested_b1():
    """B=1 should return a single config."""
    configs = generate_nonnested_configs([0.3, 0.9], [0.3, 0.9], B=1)
    assert len(configs) == 1


def test_nonnested_large_b():
    """Anti-chain property holds for larger B."""
    configs = generate_nonnested_configs([0.1, 0.5, 0.9], [0.1, 0.5, 0.9], B=20)
    assert len(configs) == 20
    for i in range(len(configs)):
        for j in range(i + 1, len(configs)):
            ni, ei = configs[i]
            nj, ej = configs[j]
            assert not (ni <= nj and ei <= ej), f"Dominance: {configs[i]} ≤ {configs[j]}"
            assert not (nj <= ni and ej <= ei), f"Dominance: {configs[j]} ≤ {configs[i]}"


if __name__ == "__main__":
    tests = [
        test_topn_basic,
        test_topn_block_vote_problem,
        test_percentile_threshold_handles_ties,
        test_unique_score_rank_handles_ties,
        test_css_matrix_3methods,
        test_off_diagonal_pct,
        test_circus_score,
        test_empty_scores,
        test_nonnested_antichain_property,
        test_nonnested_respects_range,
        test_nonnested_deterministic,
        test_nonnested_b1,
        test_nonnested_large_b,
    ]
    for t in tests:
        t()
        print(f"  PASS: {t.__name__}")
    print(f"\nAll {len(tests)} tests passed.")
