"""Tests for pipeline components and integration."""

import sys
from pathlib import Path

import torch
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


def test_pca_compressor_round_trip():
    from compresslink.pipeline import SimplePCACompressor

    L, B, H, T, D = 2, 1, 4, 64, 32
    data = torch.randn(L, B, H, T, D)

    compressor = SimplePCACompressor(head_dim=D)
    compressor.calibrate(data, kind="keys")

    compressed = compressor.compress(data, bit_budget_ratio=0.5, kind="keys")
    reconstructed = compressor.decompress(compressed, data.shape, kind="keys")

    mse = ((data - reconstructed) ** 2).mean().item()
    assert mse < 1.0, f"Round-trip MSE too high: {mse}"


def test_pca_higher_budget_lower_error():
    from compresslink.pipeline import SimplePCACompressor

    L, B, H, T, D = 2, 1, 4, 64, 16
    torch.manual_seed(42)
    data = torch.randn(L, B, H, T, D)

    compressor = SimplePCACompressor(head_dim=D)
    compressor.calibrate(data, kind="keys")

    comp_high = compressor.compress(data, bit_budget_ratio=0.8, kind="keys")
    comp_low = compressor.compress(data, bit_budget_ratio=0.2, kind="keys")

    recon_high = compressor.decompress(comp_high, data.shape, kind="keys")
    recon_low = compressor.decompress(comp_low, data.shape, kind="keys")

    mse_high = ((data - recon_high) ** 2).mean().item()
    mse_low = ((data - recon_low) ** 2).mean().item()

    assert mse_low > mse_high, "Lower bit budget should have higher MSE"


def test_pca_raba_changes_allocation():
    """RABA should produce different bit allocation than standard."""
    from compresslink.pipeline import SimplePCACompressor

    L, B, H, T, D = 1, 1, 1, 64, 16
    torch.manual_seed(42)
    data = torch.randn(L, B, H, T, D)

    compressor = SimplePCACompressor(head_dim=D)
    compressor.calibrate(data, kind="keys")

    # Standard
    comp_std = compressor.compress(data, bit_budget_ratio=0.25, kind="keys")

    # RABA with first 10 tokens as boundary
    p_r = torch.zeros(T)
    p_r[:10] = 1.0
    comp_raba = compressor.compress(
        data, bit_budget_ratio=0.25, kind="keys", restoration_probs=p_r
    )

    # Bit allocations should differ
    std_bits = comp_std[0]["bit_widths"]
    raba_bits = comp_raba[0]["bit_widths"]
    assert not torch.equal(std_bits, raba_bits)


def test_cegr_with_compression_error():
    from compresslink.pipeline import SimplePCACompressor
    from compresslink.cegr import CEGRSelector

    T, D = 64, 16
    data = torch.randn(1, 1, 1, T, D)

    compressor = SimplePCACompressor(head_dim=D)
    compressor.calibrate(data, kind="keys")
    compressed = compressor.compress(data, bit_budget_ratio=0.25, kind="keys")
    recon = compressor.decompress(compressed, data.shape, kind="keys")

    error = ((data.squeeze() - recon.squeeze()) ** 2).mean(dim=-1)
    relevance = torch.rand(T)

    cegr = CEGRSelector(beta=1.0)
    non_boundary = list(range(10, T))
    selected = cegr.select_restoration_tokens(
        relevance, error, non_boundary, num_to_select=5
    )

    assert len(selected) == 5
    assert all(s in non_boundary for s in selected)


def test_budget_pipeline_integration():
    """Budget manager + CEGR + boundary work together correctly."""
    from compresslink.budget_manager import RecomputationBudgetManager
    from compresslink.cegr import CEGRSelector
    from compresslink.raba import get_position_prior_probs

    num_tokens = 1024
    chunk_boundaries = [512]

    mgr = RecomputationBudgetManager(total_budget=0.2, block_size=32)
    budget = mgr.allocate(num_tokens, chunk_boundaries)

    assert budget["boundary_budget"] + budget["cegr_budget"] <= 0.2 + 1e-6

    # RABA probs
    p_r = get_position_prior_probs(num_tokens, budget["boundary_indices"])
    boundary_p_r = p_r[budget["boundary_indices"]]
    assert boundary_p_r.sum() == len(budget["boundary_indices"])
    non_boundary_p_r = p_r[budget["non_boundary_indices"]]
    assert non_boundary_p_r.sum() == 0.0

    # CEGR selection should only pick from non-boundary
    relevance = torch.rand(num_tokens)
    error = torch.rand(num_tokens)
    cegr = CEGRSelector(beta=1.0)
    selected = cegr.select_restoration_tokens(
        relevance, error, budget["non_boundary_indices"], budget["cegr_num_tokens"]
    )

    boundary_set = set(budget["boundary_indices"])
    assert all(s not in boundary_set for s in selected)
    assert len(selected) <= budget["cegr_num_tokens"]


def test_query_probe_compute_relevance():
    """QueryRelevanceProbe computes correct shape from attention weights."""
    from compresslink.query_probe import QueryRelevanceProbe

    B, H, Q, KV = 1, 8, 16, 128
    num_layers = 4
    attns = tuple(
        torch.softmax(torch.randn(B, H, Q, KV), dim=-1) for _ in range(num_layers)
    )

    relevance = QueryRelevanceProbe.compute_relevance(attns)
    assert relevance.shape == (KV,)
    assert (relevance >= 0).all()


def test_cegr_empty_candidates():
    """CEGR with no candidates or zero budget returns empty."""
    from compresslink.cegr import CEGRSelector

    cegr = CEGRSelector(beta=1.0)

    # Zero budget
    result = cegr.select_restoration_tokens(
        torch.rand(100), torch.rand(100), list(range(100)), 0
    )
    assert result == []

    # Empty candidates
    result = cegr.select_restoration_tokens(
        torch.rand(100), torch.rand(100), [], 10
    )
    assert result == []
