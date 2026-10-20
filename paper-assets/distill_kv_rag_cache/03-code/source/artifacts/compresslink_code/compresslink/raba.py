"""RABA: Restoration-Aware Bit Allocation.

Modifies KVTC's error function to account for token restoration probability:
  E(i, b) = weighted_lambda_i / 4^b
where weighted_lambda_i down-weights tokens likely to be restored (p_r -> 1).
"""

import torch
from torch import Tensor
from typing import List, Optional


def compute_restoration_weighted_eigenvalues(
    pca_coeffs: Tensor,
    restoration_probs: Tensor,
) -> Tensor:
    """Compute RABA weighted eigenvalues.

    weighted_lambda_i = mean_t[(1 - p_r(t)) * pca_coeffs[t,i]^2]

    Boundary tokens (p_r=1.0) contribute weight=0 (compression error irrelevant).
    Non-boundary tokens (p_r=0.0) contribute weight=1 (normal contribution).

    Args:
        pca_coeffs: [num_tokens, dim] PCA-transformed coefficients
        restoration_probs: [num_tokens] per-token restoration probability

    Returns:
        [dim] weighted variance per PCA component
    """
    weights = (1.0 - restoration_probs).unsqueeze(1)  # [T, 1]
    weighted_var = (weights * pca_coeffs**2).mean(dim=0)  # [dim]
    return weighted_var


def get_position_prior_probs(
    num_tokens: int,
    boundary_indices: List[int],
    device: torch.device = None,
) -> Tensor:
    """MVP position prior: boundary tokens p_r=1.0, others p_r=0.0."""
    if device is None:
        device = torch.device("cpu")
    probs = torch.zeros(num_tokens, device=device)
    if boundary_indices:
        idx = torch.tensor(boundary_indices, device=device, dtype=torch.long)
        probs[idx] = 1.0
    return probs


# ---------------------------------------------------------------------------
# Bit allocation algorithms (re-implemented from KVTC for standalone use)
# ---------------------------------------------------------------------------


def dp_bit_allocation(
    eigenvalues: Tensor,
    bit_budget: int,
    max_bits: int = 16,
    group_size: int = 1,
) -> Tensor:
    """DP optimal bit allocation (KVTC quantize.py).

    Error function: E(i, b) = lambda_i / 4^b (b > 0), else lambda_i.
    Finds per-component bit widths minimizing total MSE under budget constraint.

    Args:
        eigenvalues: [dim] per-component variance (or RABA-weighted variance)
        bit_budget: total bit budget across all components
        max_bits: maximum bits per component
        group_size: components per group (default 1)

    Returns:
        [dim] per-component bit widths (int64)
    """
    values = eigenvalues.detach().to(torch.float64).flatten()
    num_components = len(values)

    # Build groups
    if group_size > 1:
        groups = []
        for i in range(0, num_components, group_size):
            groups.append(values[i : i + group_size])
    else:
        groups = [values[i : i + 1] for i in range(num_components)]

    max_budget = max(int(bit_budget), 0)
    num_groups = len(groups)
    inf = float("inf")

    dp = [[inf] * (max_budget + 1) for _ in range(num_groups + 1)]
    back = [[0] * (max_budget + 1) for _ in range(num_groups + 1)]
    dp[0][0] = 0.0

    for idx in range(1, num_groups + 1):
        group = groups[idx - 1]
        variance = float(group.sum().item())
        width = group.numel()

        for used in range(max_budget + 1):
            if dp[idx - 1][used] == inf:
                continue
            for bits in range(0, max_bits + 1):
                cost = used + bits * width
                if cost > max_budget:
                    continue
                error = variance if bits == 0 else variance / (4.0**bits)
                candidate = dp[idx - 1][used] + error
                if candidate < dp[idx][cost]:
                    dp[idx][cost] = candidate
                    back[idx][cost] = bits

    # Find best feasible budget
    best_budget = min(range(max_budget + 1), key=lambda b: dp[num_groups][b])

    # Backtrack
    widths_per_group = [0] * num_groups
    b = best_budget
    for idx in range(num_groups, 0, -1):
        widths_per_group[idx - 1] = back[idx][b]
        b -= back[idx][b] * groups[idx - 1].numel()

    # Expand to per-component
    widths = []
    for i, group in enumerate(groups):
        widths.extend([widths_per_group[i]] * group.numel())

    return torch.tensor(widths[:num_components], dtype=torch.int64)


def greedy_bit_allocation(
    eigenvalues: Tensor,
    bit_budget: int,
    max_bits: int = 16,
) -> Tensor:
    """Greedy bit allocation (KVTC gpu_ops).

    Allocates bits by marginal gain: gain(i, b) = lambda_i * 3 / 4^b.
    Optimal for separable convex problems (equivalent to DP solution).

    Args:
        eigenvalues: [dim] per-component variance
        bit_budget: total bit budget
        max_bits: maximum bits per component

    Returns:
        [dim] per-component bit widths (int64)
    """
    values = eigenvalues.detach().to(torch.float64).flatten()
    dim = len(values)
    max_budget = max(int(bit_budget), 0)

    # Marginal gain of bit b for component i: lambda_i * 3 / 4^b
    gains = []
    for i in range(dim):
        v = float(values[i])
        if v <= 0:
            continue
        for b in range(1, max_bits + 1):
            gain = v * 3.0 / (4.0**b)
            gains.append((gain, i, b))

    gains.sort(key=lambda x: x[0], reverse=True)

    widths = torch.zeros(dim, dtype=torch.int64)
    budget_used = 0

    for gain_val, i, b in gains:
        if budget_used >= max_budget:
            break
        if widths[i] == b - 1:
            widths[i] = b
            budget_used += 1

    return widths


def raba_bit_allocation(
    pca_coeffs: Tensor,
    restoration_probs: Tensor,
    bit_budget: int,
    max_bits: int = 16,
    use_greedy: bool = True,
) -> Tensor:
    """RABA end-to-end: compute weighted eigenvalues, then allocate bits.

    Args:
        pca_coeffs: [num_tokens, dim] PCA coefficients from current input
        restoration_probs: [num_tokens] per-token restoration probability
        bit_budget: total bit budget
        max_bits: max bits per component
        use_greedy: use greedy (True) or DP (False) allocation

    Returns:
        [dim] per-component bit widths
    """
    weighted_eig = compute_restoration_weighted_eigenvalues(pca_coeffs, restoration_probs)

    if use_greedy:
        return greedy_bit_allocation(weighted_eig, bit_budget, max_bits)
    else:
        return dp_bit_allocation(weighted_eig, bit_budget, max_bits)
