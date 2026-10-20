"""Tests for budget allocation logic."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from compresslink.budget_manager import RecomputationBudgetManager


def test_basic_allocation():
    mgr = RecomputationBudgetManager(total_budget=0.2, block_size=32)
    result = mgr.allocate(1024, [512])

    assert len(result["boundary_indices"]) == 32
    assert result["boundary_budget"] == pytest.approx(32 / 1024, abs=1e-6)
    assert result["cegr_budget"] == pytest.approx(0.2 - 32 / 1024, abs=1e-6)
    assert result["cegr_num_tokens"] == int(result["cegr_budget"] * 1024)
    assert len(result["non_boundary_indices"]) == 1024 - 32


def test_multiple_boundaries():
    mgr = RecomputationBudgetManager(total_budget=0.2, block_size=32)
    result = mgr.allocate(2048, [512, 1024, 1536])

    assert len(result["boundary_indices"]) == 32 * 3
    boundary_budget = 96 / 2048
    assert result["boundary_budget"] == pytest.approx(boundary_budget, abs=1e-6)
    assert result["cegr_budget"] == pytest.approx(0.2 - boundary_budget, abs=1e-6)


def test_no_overlap_complete_partition():
    """Boundary and non-boundary should partition all tokens."""
    mgr = RecomputationBudgetManager(total_budget=0.2, block_size=32)
    result = mgr.allocate(1024, [512])

    boundary_set = set(result["boundary_indices"])
    non_boundary_set = set(result["non_boundary_indices"])

    assert boundary_set & non_boundary_set == set()
    assert boundary_set | non_boundary_set == set(range(1024))


def test_no_chunks():
    mgr = RecomputationBudgetManager(total_budget=0.2, block_size=32)
    result = mgr.allocate(1024, [])

    assert len(result["boundary_indices"]) == 0
    assert result["boundary_budget"] == 0.0
    assert result["cegr_budget"] == 0.2
    assert result["cegr_num_tokens"] == int(0.2 * 1024)
    assert len(result["non_boundary_indices"]) == 1024


def test_boundary_near_end():
    mgr = RecomputationBudgetManager(total_budget=0.2, block_size=32)
    result = mgr.allocate(1024, [1010])

    # Only 14 tokens remain (1010..1023)
    assert len(result["boundary_indices"]) == 14


def test_overlapping_boundaries():
    """Adjacent chunk boundaries should not double-count tokens."""
    mgr = RecomputationBudgetManager(total_budget=0.2, block_size=32)
    result = mgr.allocate(1024, [500, 510])

    expected = set(range(500, 532)) | set(range(510, 542))
    assert set(result["boundary_indices"]) == expected
    # Verify total partition
    assert len(result["boundary_indices"]) + len(result["non_boundary_indices"]) == 1024


def test_budget_exceeds_total():
    """If boundary budget exceeds total, CEGR budget should be 0."""
    mgr = RecomputationBudgetManager(total_budget=0.05, block_size=32)
    result = mgr.allocate(256, [0, 64, 128, 192])

    # 4 boundaries * 32 = 128 tokens (50% of 256)
    assert result["boundary_budget"] == pytest.approx(128 / 256, abs=1e-6)
    assert result["cegr_budget"] == 0.0
    assert result["cegr_num_tokens"] == 0


def test_default_chunk_boundary_pattern():
    """Typical pattern: chunk_size=512, block_size=32, 2048 tokens."""
    mgr = RecomputationBudgetManager(total_budget=0.2, block_size=32)
    boundaries = [512, 1024, 1536]
    result = mgr.allocate(2048, boundaries)

    # 3 * 32 = 96 boundary tokens
    assert len(result["boundary_indices"]) == 96
    # ~4.7% boundary budget
    assert result["boundary_budget"] == pytest.approx(96 / 2048, abs=1e-6)
    # ~15.3% for CEGR
    assert result["cegr_budget"] == pytest.approx(0.2 - 96 / 2048, abs=1e-6)
    # Verify all boundary indices are first 32 tokens of each chunk
    for b in boundaries:
        for offset in range(32):
            assert b + offset in result["boundary_indices"]


def test_zero_tokens():
    """Edge case: zero tokens."""
    mgr = RecomputationBudgetManager(total_budget=0.2, block_size=32)
    result = mgr.allocate(0, [])

    assert result["boundary_indices"] == []
    assert result["non_boundary_indices"] == []
    assert result["boundary_budget"] == 0.0
    assert result["cegr_budget"] == 0.2
    assert result["cegr_num_tokens"] == 0
