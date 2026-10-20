"""Convergence-theoretic adaptive contamination reweighting.

Implements the effective authenticity rate α_eff(b) and related quantities
for importance-weighted pretraining on contaminated corpora.

Key idea: given a detector that outputs per-sample synthetic probability q_i,
assign weight w_i = (1 − q_i)^b. The parameter b controls the bias-variance
tradeoff: higher b downweights suspected synthetic data more aggressively
but reduces effective sample size (ESS).

Core quantities:
  α_eff(b) = Σ (1−q_i)^{b+1} / Σ (1−q_i)^b    — effective authenticity rate
  ESS(b)   = (Σ w_i)² / Σ w_i²                  — effective sample size
  b*       = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b*) ≥ n_min

References:
  - arXiv 2602.16065 (convergence bounds for weighted pretraining)
  - Drayson et al., EMNLP 2025 (grid-search weighting baseline)

Inputs:  q_scores ∈ [0,1]^N (synthetic probabilities from detector)
Outputs: weights w ∈ R_+^N (normalized to sum to N)
"""

import math
import torch


def compute_alpha_eff(q_scores: torch.Tensor, b: float) -> float:
    """Effective authenticity rate α_eff(b) = Σ (1−q)^{b+1} / Σ (1−q)^b.

    Properties:
      α_eff(0) = 1 − ρ̂  (unweighted authenticity)
      α_eff(b) → 1 as b → ∞
      α_eff(b) is monotonically non-decreasing in b
    """
    q = q_scores.clamp(0.0, 1.0).double()
    one_minus_q = 1.0 - q

    if b == 0.0:
        return float(one_minus_q.mean())

    log_omq = torch.log(one_minus_q.clamp(min=1e-30))
    log_w = b * log_omq
    log_w_shift = log_w - log_w.max()
    w = torch.exp(log_w_shift)

    numerator = (w * one_minus_q).sum()
    denominator = w.sum()

    if denominator < 1e-30:
        return 1.0

    return float(numerator / denominator)


def compute_ess(q_scores: torch.Tensor, b: float) -> float:
    """Effective sample size ESS(b) = (Σ w_i)² / Σ w_i².

    ESS = N when b=0 (uniform weights), decreases as b increases.
    """
    if b == 0.0:
        return float(q_scores.numel())

    q = q_scores.clamp(0.0, 1.0).double()
    one_minus_q = 1.0 - q

    log_omq = torch.log(one_minus_q.clamp(min=1e-30))
    log_w = b * log_omq
    log_w_shift = log_w - log_w.max()
    w = torch.exp(log_w_shift)

    sum_w = w.sum()
    sum_w2 = (w * w).sum()

    if sum_w2 < 1e-30:
        return 0.0

    return float((sum_w * sum_w) / sum_w2)


def find_optimal_b(
    q_scores: torch.Tensor,
    tau: float,
    n_min: int,
    b_max: float = 20.0,
    resolution: int = 1000,
) -> float:
    """Find b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b*) ≥ n_min.

    When the batch is clean enough (ρ̂ < 1 − τ), returns b=0 (uniform).
    When the ESS constraint conflicts with the α_eff threshold, returns
    b* = argmax_b α_eff(b) s.t. ESS(b) ≥ n_min.
    """
    alpha_0 = compute_alpha_eff(q_scores, 0.0)
    if alpha_0 >= tau:
        return 0.0

    n = q_scores.numel()
    if n_min > n:
        n_min = n

    # Phase 1: grid search to find the feasible region
    grid = torch.linspace(0.0, b_max, resolution + 1).tolist()

    best_feasible_b = 0.0
    best_feasible_alpha = alpha_0
    threshold_b = None

    for b_val in grid:
        ess = compute_ess(q_scores, b_val)
        if ess < n_min:
            break

        alpha = compute_alpha_eff(q_scores, b_val)

        if alpha > best_feasible_alpha:
            best_feasible_alpha = alpha
            best_feasible_b = b_val

        if alpha >= tau and threshold_b is None:
            threshold_b = b_val

    if threshold_b is not None:
        # Phase 2: refine with bisection
        lo = max(0.0, threshold_b - b_max / resolution)
        hi = threshold_b
        for _ in range(50):
            mid = (lo + hi) / 2.0
            if compute_alpha_eff(q_scores, mid) >= tau:
                hi = mid
            else:
                lo = mid
        b_star = hi
        if compute_ess(q_scores, b_star) >= n_min:
            return b_star

    return best_feasible_b


def find_ess_only_b(
    q_scores: torch.Tensor,
    n_min: int,
    b_max: float = 20.0,
    tol: float = 0.01,
) -> float:
    """Find b* = max{b : ESS(b) >= n_min} (ESS-only, no alpha_eff constraint).

    ESS(b) is monotonically non-increasing in b, so binary search works.
    Returns b_max if ESS(b_max) >= n_min; returns 0.0 if ESS(0) < n_min.
    """
    if compute_ess(q_scores, 0.0) < n_min:
        return 0.0

    if compute_ess(q_scores, b_max) >= n_min:
        return b_max

    lo, hi = 0.0, b_max
    while hi - lo > tol:
        mid = (lo + hi) / 2.0
        if compute_ess(q_scores, mid) >= n_min:
            lo = mid
        else:
            hi = mid
    return lo


def compute_sample_weights(q_scores: torch.Tensor, b: float) -> torch.Tensor:
    """Per-sample weights w_i = (1−q_i)^b, normalized to sum to N."""
    n = q_scores.numel()

    if b == 0.0:
        return torch.ones_like(q_scores)

    q = q_scores.clamp(0.0, 1.0)
    one_minus_q = 1.0 - q

    log_omq = torch.log(one_minus_q.clamp(min=1e-30))
    log_w = b * log_omq
    log_w = log_w - log_w.max()
    w = torch.exp(log_w)

    w = w * (n / w.sum().clamp(min=1e-30))
    return w.to(q_scores.dtype)


def compute_concentration_bound(
    q_scores: torch.Tensor, b: float, delta: float = 0.05
) -> float:
    """Concentration bound |α̂_eff − α_eff| ≤ O(√(w_max / (ESS · Σw))) · log(1/δ)).

    Returns the upper bound on estimation error for α_eff with probability 1−δ.
    """
    if b == 0.0:
        n = q_scores.numel()
        return float(math.sqrt(math.log(2.0 / delta) / (2.0 * n)))

    q = q_scores.clamp(0.0, 1.0).double()
    one_minus_q = 1.0 - q
    log_omq = torch.log(one_minus_q.clamp(min=1e-30))
    log_w = b * log_omq
    log_w = log_w - log_w.max()
    w = torch.exp(log_w)

    sum_w = w.sum()
    w_max = w.max()
    ess = compute_ess(q_scores, b)

    if ess < 1e-10 or sum_w < 1e-30:
        return float("inf")

    bound = float(torch.sqrt(w_max / (ess * sum_w))) * math.log(2.0 / delta)
    return bound


if __name__ == "__main__":
    torch.manual_seed(42)
    n = 1000

    # Simulate: 80% human (low q), 20% synthetic (high q)
    q_human = torch.rand(800) * 0.2
    q_synth = 0.7 + torch.rand(200) * 0.3
    q_scores = torch.cat([q_human, q_synth])
    q_scores = q_scores[torch.randperm(n)]

    print(f"N = {n}, mean q = {q_scores.mean():.4f}")
    print(f"True contamination ≈ 20%\n")

    for b in [0.0, 0.5, 1.0, 2.0, 5.0, 10.0]:
        alpha = compute_alpha_eff(q_scores, b)
        ess = compute_ess(q_scores, b)
        bound = compute_concentration_bound(q_scores, b)
        print(f"b={b:5.1f}  α_eff={alpha:.4f}  ESS={ess:8.1f}  bound={bound:.6f}")

    print()

    tau = 0.95
    n_min = 100
    b_star = find_optimal_b(q_scores, tau=tau, n_min=n_min)
    alpha_star = compute_alpha_eff(q_scores, b_star)
    ess_star = compute_ess(q_scores, b_star)
    print(f"Optimal b* = {b_star:.4f}  (tau={tau}, n_min={n_min})")
    print(f"  α_eff(b*) = {alpha_star:.4f}")
    print(f"  ESS(b*)   = {ess_star:.1f}")

    weights = compute_sample_weights(q_scores, b_star)
    print(f"\nWeights: sum={weights.sum():.1f}, min={weights.min():.4f}, "
          f"max={weights.max():.4f}, std={weights.std():.4f}")

    # Verify monotonicity of α_eff
    bs = [i * 0.5 for i in range(21)]
    alphas = [compute_alpha_eff(q_scores, b) for b in bs]
    monotone = all(alphas[i] <= alphas[i + 1] + 1e-10 for i in range(len(alphas) - 1))
    print(f"\nα_eff monotonicity check: {'PASS' if monotone else 'FAIL'}")
