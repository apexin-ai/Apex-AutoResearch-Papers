"""Tests for RABA: Restoration-Aware Bit Allocation."""

import sys
from pathlib import Path

import torch
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from compresslink.raba import (
    compute_restoration_weighted_eigenvalues,
    get_position_prior_probs,
    dp_bit_allocation,
    greedy_bit_allocation,
    raba_bit_allocation,
)


def test_weighted_eigenvalues_all_boundary():
    """All boundary (p_r=1) -> all weights = 0."""
    T, D = 100, 32
    coeffs = torch.randn(T, D)
    p_r = torch.ones(T)
    w_eig = compute_restoration_weighted_eigenvalues(coeffs, p_r)
    assert torch.allclose(w_eig, torch.zeros(D))


def test_weighted_eigenvalues_no_boundary():
    """No boundary (p_r=0) -> weighted = standard variance."""
    T, D = 100, 32
    coeffs = torch.randn(T, D)
    p_r = torch.zeros(T)
    w_eig = compute_restoration_weighted_eigenvalues(coeffs, p_r)
    standard = (coeffs**2).mean(dim=0)
    assert torch.allclose(w_eig, standard)


def test_weighted_eigenvalues_partial_boundary():
    """Partial boundary -> weighted < standard."""
    T, D = 100, 16
    torch.manual_seed(42)
    coeffs = torch.randn(T, D).abs() + 0.1

    p_r = torch.zeros(T)
    p_r[:20] = 1.0

    w_eig = compute_restoration_weighted_eigenvalues(coeffs, p_r)
    standard = (coeffs**2).mean(dim=0)

    assert (w_eig <= standard + 1e-6).all()
    assert (w_eig < standard - 1e-4).any()


def test_position_prior_probs():
    probs = get_position_prior_probs(100, [0, 50])
    assert probs[0] == 1.0
    assert probs[50] == 1.0
    assert probs[25] == 0.0
    assert probs.sum() == 2.0


def test_position_prior_probs_empty():
    probs = get_position_prior_probs(100, [])
    assert probs.sum() == 0.0


def test_dp_budget_constraint():
    """Total allocated bits should not exceed budget."""
    eigenvalues = torch.rand(32) * 10 + 0.1
    budget = 128
    widths = dp_bit_allocation(eigenvalues, budget, max_bits=16)
    assert widths.sum() <= budget
    assert (widths >= 0).all()
    assert (widths <= 16).all()


def test_dp_zero_budget():
    eigenvalues = torch.rand(16) * 5
    widths = dp_bit_allocation(eigenvalues, 0, max_bits=16)
    assert widths.sum() == 0


def test_greedy_budget_constraint():
    eigenvalues = torch.rand(32) * 10 + 0.1
    budget = 128
    widths = greedy_bit_allocation(eigenvalues, budget, max_bits=16)
    assert widths.sum() <= budget
    assert (widths >= 0).all()
    assert (widths <= 16).all()


def test_greedy_allocates_to_high_variance():
    """Higher-variance components should get more bits."""
    eigenvalues = torch.tensor([100.0, 1.0, 0.01, 0.001])
    widths = greedy_bit_allocation(eigenvalues, bit_budget=8, max_bits=16)
    assert widths[0] >= widths[1] >= widths[2] >= widths[3]


def test_greedy_matches_dp():
    """Greedy and DP should produce similar total error for small problems."""
    torch.manual_seed(42)
    eigenvalues = torch.rand(16) * 5 + 0.1
    budget = 64

    dp_widths = dp_bit_allocation(eigenvalues, budget, max_bits=16)
    gr_widths = greedy_bit_allocation(eigenvalues, budget, max_bits=16)

    # Compute total error for each
    def total_error(eig, widths):
        err = 0.0
        for i in range(len(eig)):
            b = int(widths[i])
            v = float(eig[i])
            err += v if b == 0 else v / (4.0**b)
        return err

    dp_err = total_error(eigenvalues, dp_widths)
    gr_err = total_error(eigenvalues, gr_widths)

    # Greedy error should be close to or equal to DP
    assert gr_err <= dp_err * 1.01 + 1e-6


def test_raba_shifts_bits():
    """RABA should redistribute bits compared to standard allocation."""
    T, D = 200, 32
    torch.manual_seed(42)
    # Non-uniform variance across components to ensure bit allocation differs
    coeffs = torch.randn(T, D)
    coeffs[:, :8] *= 5.0  # high-variance components
    coeffs[:40, :8] *= 0.1  # boundary tokens have low variance on these components
    budget = D * 3  # non-uniform budget forces differentiation

    standard_eig = (coeffs**2).mean(dim=0)
    standard_widths = greedy_bit_allocation(standard_eig, budget)

    p_r = torch.zeros(T)
    p_r[:40] = 1.0
    raba_widths = raba_bit_allocation(coeffs, p_r, budget, use_greedy=True)

    # Total bits should be similar (same budget)
    assert abs(standard_widths.sum().item() - raba_widths.sum().item()) <= 2
    # RABA down-weights boundary tokens → changes effective variance → different allocation
    assert not torch.equal(standard_widths, raba_widths)
