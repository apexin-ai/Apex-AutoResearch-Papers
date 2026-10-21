"""Tests for diversity_metrics module."""

import json
import os
import sys
import tempfile

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from training.diversity_metrics import (
    normalize_triple_key,
    build_triple_set,
    compute_doc_diversity,
    compute_diversity_from_file,
)


# --- normalize_triple_key ---

def test_normalize_basic():
    t = {"head": "John Smith", "relation": "born in", "tail": "New York"}
    assert normalize_triple_key(t) == ("john smith", "born in", "new york")


def test_normalize_case_insensitive():
    t1 = {"head": "ALICE", "relation": "Works At", "tail": "Google"}
    t2 = {"head": "alice", "relation": "works at", "tail": "google"}
    assert normalize_triple_key(t1) == normalize_triple_key(t2)


def test_normalize_strips_whitespace():
    t = {"head": " Bob ", "relation": " lives in ", "tail": " Paris "}
    assert normalize_triple_key(t) == ("bob", "lives in", "paris")


def test_normalize_missing_fields():
    t = {"head": "X", "tail": "Y"}
    assert normalize_triple_key(t) == ("x", "", "y")


def test_normalize_non_string_values():
    t = {"head": 123, "relation": None, "tail": ["a", "b"]}
    result = normalize_triple_key(t)
    assert result == ("123", "", "['a', 'b']")


# --- build_triple_set ---

def test_build_triple_set_basic():
    triples = [
        {"head": "A", "relation": "R1", "tail": "B"},
        {"head": "C", "relation": "R2", "tail": "D"},
    ]
    ts = build_triple_set(triples)
    assert ts == frozenset({("a", "r1", "b"), ("c", "r2", "d")})


def test_build_triple_set_deduplicates():
    triples = [
        {"head": "A", "relation": "R1", "tail": "B"},
        {"head": "A", "relation": "R1", "tail": "B"},
    ]
    ts = build_triple_set(triples)
    assert len(ts) == 1


def test_build_triple_set_empty():
    assert build_triple_set([]) == frozenset()


def test_build_triple_set_ignores_evidence():
    t1 = [{"head": "A", "relation": "R", "tail": "B", "evidence": [0]}]
    t2 = [{"head": "A", "relation": "R", "tail": "B", "evidence": [1, 2]}]
    assert build_triple_set(t1) == build_triple_set(t2)


# --- compute_doc_diversity ---

def test_all_identical_outputs():
    """8 identical generations → diversity = 1."""
    same_triples = [{"head": "A", "relation": "R", "tail": "B"}]
    gens = [same_triples] * 8
    result = compute_doc_diversity(gens)
    assert result["unique_count"] == 1
    assert result["total_count"] == 8
    assert result["diversity_ratio"] == pytest.approx(1 / 8)


def test_all_different_outputs():
    """8 completely different generations → diversity = 8."""
    gens = []
    for i in range(8):
        gens.append([{"head": f"H{i}", "relation": "R", "tail": f"T{i}"}])
    result = compute_doc_diversity(gens)
    assert result["unique_count"] == 8
    assert result["total_count"] == 8
    assert result["diversity_ratio"] == pytest.approx(1.0)


def test_mixed_diversity():
    """4 unique + 4 duplicates → diversity = 4."""
    unique = [
        [{"head": "A", "relation": "R", "tail": "B"}],
        [{"head": "C", "relation": "R", "tail": "D"}],
        [{"head": "E", "relation": "R", "tail": "F"}],
        [{"head": "G", "relation": "R", "tail": "H"}],
    ]
    gens = unique + unique  # 4 unique repeated twice = 4 unique total
    result = compute_doc_diversity(gens)
    assert result["unique_count"] == 4
    assert result["total_count"] == 8


def test_empty_parse_failures():
    """All parse failures (empty lists) → diversity = 1 (all produce same empty frozenset)."""
    gens = [[]] * 8
    result = compute_doc_diversity(gens)
    assert result["unique_count"] == 1
    assert result["total_count"] == 8


def test_mix_of_valid_and_empty():
    """Some valid, some empty → counts correctly."""
    gens = [
        [{"head": "A", "relation": "R", "tail": "B"}],
        [],  # parse failure
        [{"head": "C", "relation": "R", "tail": "D"}],
        [],  # parse failure (same empty frozenset as above)
        [{"head": "A", "relation": "R", "tail": "B"}],  # same as gen 0
        [{"head": "E", "relation": "R", "tail": "F"}],
        [],  # parse failure
        [{"head": "G", "relation": "R", "tail": "H"}],
    ]
    result = compute_doc_diversity(gens)
    # unique: {A-R-B}, {}, {C-R-D}, {E-R-F}, {G-R-H} = 5
    assert result["unique_count"] == 5
    assert result["total_count"] == 8


def test_single_generation():
    gens = [[{"head": "A", "relation": "R", "tail": "B"}]]
    result = compute_doc_diversity(gens)
    assert result["unique_count"] == 1
    assert result["total_count"] == 1
    assert result["diversity_ratio"] == pytest.approx(1.0)


def test_empty_generations_list():
    result = compute_doc_diversity([])
    assert result["unique_count"] == 0
    assert result["total_count"] == 0
    assert result["diversity_ratio"] == 0.0


def test_order_independence():
    """Triple order within a generation doesn't affect diversity."""
    gen1 = [
        {"head": "A", "relation": "R1", "tail": "B"},
        {"head": "C", "relation": "R2", "tail": "D"},
    ]
    gen2 = [
        {"head": "C", "relation": "R2", "tail": "D"},
        {"head": "A", "relation": "R1", "tail": "B"},
    ]
    result = compute_doc_diversity([gen1, gen2])
    assert result["unique_count"] == 1  # same set


def test_case_insensitive_dedup():
    """Same triples with different case → same set."""
    gen1 = [{"head": "Alice", "relation": "Born In", "tail": "NYC"}]
    gen2 = [{"head": "ALICE", "relation": "born in", "tail": "nyc"}]
    result = compute_doc_diversity([gen1, gen2])
    assert result["unique_count"] == 1


# --- compute_diversity_from_file ---

def test_diversity_from_file():
    """Test file-based diversity computation."""
    records = []
    for doc_idx in range(3):
        for gen_idx in range(8):
            records.append({
                "doc_id": f"doc_{doc_idx}",
                "generation_idx": gen_idx,
                "output": "ignored",
                "parsed_triples": [
                    {"head": f"H{doc_idx}_{gen_idx}", "relation": "R", "tail": "T"}
                ],
            })

    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
        tmp_path = f.name

    try:
        result = compute_diversity_from_file(tmp_path)
        assert result["n_docs"] == 3
        assert result["mean_diversity"] == 8.0  # all unique per doc
        assert result["n_generations"] == 8
    finally:
        os.unlink(tmp_path)


def test_diversity_from_file_identical_gens():
    """All generations produce the same triples."""
    records = []
    for doc_idx in range(2):
        for gen_idx in range(8):
            records.append({
                "doc_id": f"doc_{doc_idx}",
                "generation_idx": gen_idx,
                "output": "ignored",
                "parsed_triples": [
                    {"head": "Same", "relation": "R", "tail": "T"}
                ],
            })

    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
        tmp_path = f.name

    try:
        result = compute_diversity_from_file(tmp_path)
        assert result["n_docs"] == 2
        assert result["mean_diversity"] == 1.0  # all identical
    finally:
        os.unlink(tmp_path)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
