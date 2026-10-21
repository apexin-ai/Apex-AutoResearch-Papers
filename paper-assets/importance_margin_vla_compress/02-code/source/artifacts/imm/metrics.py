"""Evaluation metrics for importance-margin token compression.

compute_margin:              gap between k-th and (k+1)-th largest scores.
topk_preservation_rate:      Jaccard overlap of top-k sets under perturbation.
kendall_tau_distance:        rank correlation of top-k ordering under perturbation.
certified_bound:             probabilistic upper bound on top-k set change.
margin_statistics:           summary stats of margins across a batch.
compute_empirical_lipschitz: empirical Lipschitz constant via input perturbation.
l_eps_delta_ratio:           L·ε/Δ_k gate metric for IMM vs baseline comparison.

All functions are pure (no nn.Module state), operate on detached tensors.
"""

from __future__ import annotations

import torch
import torch.nn as nn
from torch import Tensor
from torch.utils.data import DataLoader
from typing import Callable, Dict, Optional


def compute_margin(scores: Tensor, k: int) -> Tensor:
    """Delta_k = s_{(k)} - s_{(k+1)}.

    Args:
        scores: (B, N) importance scores.
        k: retention count, must satisfy 0 < k < N.
    Returns:
        (B,) margin values.
    """
    sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)
    return sorted_scores[:, k - 1] - sorted_scores[:, k]


def topk_preservation_rate(scores_clean: Tensor, scores_perturbed: Tensor, k: int) -> Tensor:
    """Jaccard similarity |A ∩ B| / |A ∪ B| of top-k index sets.

    Args:
        scores_clean:     (B, N).
        scores_perturbed: (B, N).
        k: retention count.
    Returns:
        (B,) Jaccard similarities in [0, 1].
    """
    _, idx_clean = torch.topk(scores_clean, k, dim=-1)
    _, idx_pert = torch.topk(scores_perturbed, k, dim=-1)

    B, N = scores_clean.shape
    mask_clean = torch.zeros(B, N, device=scores_clean.device)
    mask_pert = torch.zeros(B, N, device=scores_clean.device)
    mask_clean.scatter_(1, idx_clean, 1.0)
    mask_pert.scatter_(1, idx_pert, 1.0)

    intersection = (mask_clean * mask_pert).sum(-1)
    union = (mask_clean + mask_pert).clamp(max=1.0).sum(-1)
    return intersection / union.clamp(min=1.0)


def kendall_tau_distance(scores_clean: Tensor, scores_perturbed: Tensor, k: int) -> Tensor:
    """Kendall tau-b correlation of top-k rankings.

    Only considers the union of top-k indices from both sets.
    Returns values in [-1, 1]; +1 = identical ranking.

    Args:
        scores_clean:     (B, N).
        scores_perturbed: (B, N).
        k: retention count.
    Returns:
        (B,) correlation values.
    """
    B, N = scores_clean.shape
    _, idx_clean = torch.topk(scores_clean, k, dim=-1)
    _, idx_pert = torch.topk(scores_perturbed, k, dim=-1)

    # Union of top-k indices
    mask_union = torch.zeros(B, N, device=scores_clean.device)
    mask_union.scatter_(1, idx_clean, 1.0)
    mask_union.scatter_(1, idx_pert, 1.0)

    taus = []
    for b in range(B):
        union_idx = mask_union[b].nonzero(as_tuple=True)[0]
        n_union = union_idx.numel()
        if n_union < 2:
            taus.append(torch.tensor(1.0, device=scores_clean.device))
            continue

        r1 = scores_clean[b, union_idx]
        r2 = scores_perturbed[b, union_idx]

        # Pairwise concordance
        diff1 = r1.unsqueeze(0) - r1.unsqueeze(1)  # (n, n)
        diff2 = r2.unsqueeze(0) - r2.unsqueeze(1)
        sign_prod = torch.sign(diff1) * torch.sign(diff2)

        # Upper triangle only
        n_pairs = n_union * (n_union - 1) // 2
        tau = sign_prod.triu(diagonal=1).sum() / max(n_pairs, 1)
        taus.append(tau)

    return torch.stack(taus)


def certified_bound(margin: Tensor, lipschitz_const: float, epsilon: float, k: int) -> Tensor:
    """Upper bound on probability of top-k set change: P <= k * eps * L / Delta_k.

    Args:
        margin:         (B,) Delta_k values (must be > 0 for meaningful bound).
        lipschitz_const: Lipschitz constant L of the scoring function.
        epsilon:        perturbation budget (L_inf or L_2 radius).
        k:              retention count.
    Returns:
        (B,) upper bound probabilities, clamped to [0, 1].
    """
    bound = k * epsilon * lipschitz_const / margin.clamp(min=1e-8)
    return bound.clamp(0.0, 1.0)


def margin_statistics(scores: Tensor, k: int) -> Dict[str, Tensor]:
    """Summary statistics of Delta_k across a batch.

    Args:
        scores: (B, N).
        k: retention count.
    Returns:
        dict with median, mean, std, min, max of margins.
    """
    m = compute_margin(scores, k)
    return {
        "median": m.median(),
        "mean": m.mean(),
        "std": m.std(),
        "min": m.min(),
        "max": m.max(),
    }


@torch.no_grad()
def compute_empirical_lipschitz(
    acis_module: nn.Module,
    visual_tokens: Tensor,
    a_query: Tensor,
    num_samples: int = 100,
    epsilon: float = 0.001,
) -> float:
    """Empirical Lipschitz constant: max ||s(x') - s(x)|| / ||x' - x|| over perturbations.

    Perturbs visual_tokens by random directions of norm epsilon.
    Restores training mode after measurement to avoid breaking spectral norm updates.
    """
    was_training = acis_module.training
    acis_module.eval()
    s_clean = acis_module(a_query, visual_tokens)  # (B, N)

    max_ratio = 0.0
    for _ in range(num_samples):
        delta = torch.randn_like(visual_tokens)
        delta = delta / delta.norm(dim=-1, keepdim=True).clamp(min=1e-8) * epsilon
        s_pert = acis_module(a_query, visual_tokens + delta)

        score_diff = (s_pert - s_clean).norm(dim=-1)  # (B,)
        input_diff = delta.flatten(1).norm(dim=-1)     # (B,)
        ratio = (score_diff / input_diff.clamp(min=1e-8)).max().item()
        max_ratio = max(max_ratio, ratio)

    if was_training:
        acis_module.train()
    return max_ratio


def l_eps_delta_ratio(
    lipschitz_const: float, epsilon: float, margin: Tensor, k: int
) -> Tensor:
    """L·ε·k/Δ_k — gate metric. Values < 1 mean the certified bound holds.

    Args:
        lipschitz_const: Lipschitz constant L of the scoring function.
        epsilon: perturbation budget.
        margin: (B,) Δ_k values.
        k: retention count.
    Returns:
        (B,) ratio values.
    """
    return lipschitz_const * epsilon * k / margin.clamp(min=1e-8)


if __name__ == "__main__":
    torch.manual_seed(42)
    B, N, k = 4, 64, 16
    scores = torch.randn(B, N)
    scores_noisy = scores + 0.1 * torch.randn_like(scores)

    m = compute_margin(scores, k)
    print(f"Margin: {m}")

    pr = topk_preservation_rate(scores, scores_noisy, k)
    print(f"Preservation rate: {pr}")

    kt = kendall_tau_distance(scores, scores_noisy, k)
    print(f"Kendall tau: {kt}")

    cb = certified_bound(m, lipschitz_const=1.0, epsilon=0.01, k=k)
    print(f"Certified bound: {cb}")

    stats = margin_statistics(scores, k)
    print(f"Stats: { {k: v.item() for k, v in stats.items()} }")

    # L·ε/Δ_k ratio
    ratio = l_eps_delta_ratio(1.0, 0.01, m, k)
    print(f"L*eps*k/Delta_k ratio: {ratio}")

    # Empirical Lipschitz (needs ACIS)
    from .acis import ACIS
    acis = ACIS(visual_dim=64, action_dim=32, num_heads=4)
    vis = torch.randn(2, 16, 64)
    aq = torch.randn(2, 8, 32)
    L_emp = compute_empirical_lipschitz(acis, vis, aq, num_samples=20, epsilon=0.001)
    print(f"Empirical Lipschitz: {L_emp:.4f}")
