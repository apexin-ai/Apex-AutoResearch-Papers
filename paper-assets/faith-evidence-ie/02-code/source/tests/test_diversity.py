"""Tests for diversity computation in monitoring and analysis code.

Verifies that triple-set diversity is computed correctly:
- diversity = number of unique triple-sets among N generations for one doc
- triple-set comparison is based on semantic content (normalized tuple set)
- JSON key order, whitespace, and case do not affect deduplication
"""

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


class TestAllDifferent:
    """8 completely different outputs → diversity = 8."""

    def test_unique_triple_sets(self):
        gens = []
        for i in range(8):
            gens.append([
                {"head": f"Entity_{i}", "relation": f"rel_{i}", "tail": f"Target_{i}"}
            ])
        result = compute_doc_diversity(gens)
        assert result["unique_count"] == 8
        assert result["total_count"] == 8
        assert result["diversity_ratio"] == pytest.approx(1.0)

    def test_unique_multi_triple(self):
        gens = []
        for i in range(8):
            gens.append([
                {"head": f"H{i}", "relation": "R", "tail": "T"},
                {"head": "X", "relation": "R", "tail": f"Y{i}"},
            ])
        result = compute_doc_diversity(gens)
        assert result["unique_count"] == 8


class TestAllIdentical:
    """8 completely identical outputs → diversity = 1."""

    def test_same_single_triple(self):
        same = [{"head": "Alice", "relation": "born_in", "tail": "NYC"}]
        gens = [same] * 8
        result = compute_doc_diversity(gens)
        assert result["unique_count"] == 1
        assert result["total_count"] == 8
        assert result["diversity_ratio"] == pytest.approx(1 / 8)

    def test_same_multi_triple(self):
        same = [
            {"head": "A", "relation": "R1", "tail": "B"},
            {"head": "C", "relation": "R2", "tail": "D"},
        ]
        gens = [same] * 8
        result = compute_doc_diversity(gens)
        assert result["unique_count"] == 1

    def test_all_empty(self):
        gens = [[] for _ in range(8)]
        result = compute_doc_diversity(gens)
        assert result["unique_count"] == 1  # all map to frozenset()


class TestMixed:
    """Partial duplicates → diversity = expected value."""

    def test_half_unique(self):
        gens = []
        for i in range(4):
            gens.append([{"head": f"H{i}", "relation": "R", "tail": "T"}])
        for i in range(4):
            gens.append([{"head": f"H{i}", "relation": "R", "tail": "T"}])
        result = compute_doc_diversity(gens)
        assert result["unique_count"] == 4
        assert result["total_count"] == 8

    def test_one_different_rest_same(self):
        same = [{"head": "A", "relation": "R", "tail": "B"}]
        diff = [{"head": "X", "relation": "R", "tail": "Y"}]
        gens = [same] * 7 + [diff]
        result = compute_doc_diversity(gens)
        assert result["unique_count"] == 2

    def test_empty_vs_nonempty(self):
        gens = [
            [{"head": "A", "relation": "R", "tail": "B"}],
            [],  # empty parse → frozenset()
            [{"head": "A", "relation": "R", "tail": "B"}],
            [],
            [{"head": "C", "relation": "R", "tail": "D"}],
            [],
            [{"head": "C", "relation": "R", "tail": "D"}],
            [],
        ]
        result = compute_doc_diversity(gens)
        # unique: frozenset(), {A-R-B}, {C-R-D} = 3
        assert result["unique_count"] == 3


class TestJsonKeyOrder:
    """JSON key order should not affect diversity (content-based comparison)."""

    def test_key_order_same_content(self):
        gen1 = [{"head": "A", "relation": "R", "tail": "B"}]
        gen2 = [{"tail": "B", "head": "A", "relation": "R"}]
        gen3 = [{"relation": "R", "tail": "B", "head": "A"}]
        result = compute_doc_diversity([gen1, gen2, gen3])
        assert result["unique_count"] == 1

    def test_key_order_with_extra_fields(self):
        gen1 = [{"head": "A", "relation": "R", "tail": "B", "evidence": [0]}]
        gen2 = [{"evidence": [1, 2], "tail": "B", "relation": "R", "head": "A"}]
        result = compute_doc_diversity([gen1, gen2])
        assert result["unique_count"] == 1  # evidence is ignored in triple-set


class TestNormalization:
    """Case, whitespace, and type handling."""

    def test_case_insensitive(self):
        gen1 = [{"head": "ALICE", "relation": "BORN_IN", "tail": "NYC"}]
        gen2 = [{"head": "alice", "relation": "born_in", "tail": "nyc"}]
        result = compute_doc_diversity([gen1, gen2])
        assert result["unique_count"] == 1

    def test_whitespace_stripped(self):
        gen1 = [{"head": " Alice ", "relation": " R ", "tail": " B "}]
        gen2 = [{"head": "Alice", "relation": "R", "tail": "B"}]
        result = compute_doc_diversity([gen1, gen2])
        assert result["unique_count"] == 1

    def test_triple_order_in_generation(self):
        gen1 = [
            {"head": "A", "relation": "R1", "tail": "B"},
            {"head": "C", "relation": "R2", "tail": "D"},
        ]
        gen2 = [
            {"head": "C", "relation": "R2", "tail": "D"},
            {"head": "A", "relation": "R1", "tail": "B"},
        ]
        result = compute_doc_diversity([gen1, gen2])
        assert result["unique_count"] == 1  # frozenset is order-independent


class TestFromFile:
    """Test compute_diversity_from_file with JSONL data."""

    def _write_jsonl(self, records):
        f = tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False)
        for r in records:
            f.write(json.dumps(r) + "\n")
        f.close()
        return f.name

    def test_all_unique(self):
        records = []
        for gen_idx in range(8):
            records.append({
                "doc_id": "doc_0",
                "generation_idx": gen_idx,
                "output": "ignored",
                "parsed_triples": [
                    {"head": f"H{gen_idx}", "relation": "R", "tail": "T"}
                ],
            })
        path = self._write_jsonl(records)
        try:
            result = compute_diversity_from_file(path)
            assert result["mean_diversity"] == 8.0
        finally:
            os.unlink(path)

    def test_all_identical(self):
        records = []
        for gen_idx in range(8):
            records.append({
                "doc_id": "doc_0",
                "generation_idx": gen_idx,
                "output": "ignored",
                "parsed_triples": [
                    {"head": "Same", "relation": "R", "tail": "T"}
                ],
            })
        path = self._write_jsonl(records)
        try:
            result = compute_diversity_from_file(path)
            assert result["mean_diversity"] == 1.0
        finally:
            os.unlink(path)

    def test_multi_doc_mean(self):
        records = []
        # doc_0: all unique → 8
        for gen_idx in range(8):
            records.append({
                "doc_id": "doc_0",
                "generation_idx": gen_idx,
                "output": "x",
                "parsed_triples": [
                    {"head": f"H{gen_idx}", "relation": "R", "tail": "T"}
                ],
            })
        # doc_1: all identical → 1
        for gen_idx in range(8):
            records.append({
                "doc_id": "doc_1",
                "generation_idx": gen_idx,
                "output": "x",
                "parsed_triples": [
                    {"head": "Same", "relation": "R", "tail": "T"}
                ],
            })
        path = self._write_jsonl(records)
        try:
            result = compute_diversity_from_file(path)
            assert result["mean_diversity"] == pytest.approx(4.5)  # (8+1)/2
            assert result["n_docs"] == 2
        finally:
            os.unlink(path)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
