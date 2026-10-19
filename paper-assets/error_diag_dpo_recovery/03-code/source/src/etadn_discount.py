#!/usr/bin/env python3
"""ETADN error-type-aware temporal discount for DMPO.

Core formula:
    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)

Where:
    t = current timestep (0-indexed)
    T = total trajectory length
    γ = gamma_e (error-type-specific discount factor)

γ_e mapping:
    action errors      → γ_a = 0.85 (short correction span, concentrated credit)
    verification errors → γ_v = 0.92 (medium span, moderate spread)
    planning errors     → γ_p = 1.0 (long span, uniform credit)

Integration with DPO/DMPO:
    Standard DPO loss: L = -log σ(β · (log π(y_w|x) - log π(y_l|x)))
    DMPO adds per-step weighting: replace uniform sum with φ-weighted sum
    ETADN: γ in φ varies by error_type of the (chosen, rejected) pair

Dependencies: torch only
"""
import torch
import torch.nn.functional as F
from dataclasses import dataclass


@dataclass
class ETADNConfig:
    gamma_action: float = 0.85
    gamma_verification: float = 0.92
    gamma_planning: float = 1.0
    beta: float = 0.1
    label_smoothing: float = 0.0


def phi(t: int, T: int, gamma: float) -> float:
    """DMPO credit assignment weight for timestep t of T.

    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)

    Sums to 1 over t ∈ [0, T-1] for any γ ∈ (0, 1).
    """
    if T <= 0:
        return 0.0
    if abs(gamma - 1.0) < 1e-8:
        return 1.0 / T
    if abs(gamma) < 1e-12:
        return 1.0 if t == 0 else 0.0
    numerator = (gamma ** t) * (1.0 - gamma ** (T - t))
    denominator = 1.0 - gamma ** T
    return numerator / denominator


def compute_discount_weights(T: int, gamma: float) -> torch.Tensor:
    """φ weight vector of length T. Returns shape (T,) float32 tensor."""
    if T <= 0:
        return torch.tensor([], dtype=torch.float32)
    if abs(gamma - 1.0) < 1e-8:
        return torch.full((T,), 1.0 / T, dtype=torch.float32)
    if abs(gamma) < 1e-12:
        w = torch.zeros(T, dtype=torch.float32)
        w[0] = 1.0
        return w
    t = torch.arange(T, dtype=torch.float64)
    g = torch.tensor(gamma, dtype=torch.float64)
    numerator = g.pow(t) * (1 - g.pow(T - t))
    denominator = 1 - g.pow(torch.tensor(T, dtype=torch.float64))
    w = (numerator / denominator).float()
    return w / w.sum()


def get_gamma_for_error_type(error_type: str, config: ETADNConfig) -> float:
    """Look up γ_e by error type string."""
    mapping = {
        "action": config.gamma_action,
        "verification": config.gamma_verification,
        "planning": config.gamma_planning,
    }
    return mapping.get(error_type, config.gamma_verification)


# ---------------------------------------------------------------------------
# DPO loss variants
# ---------------------------------------------------------------------------

def _dpo_loss_from_logratios(
    chosen_logratios: torch.Tensor,
    rejected_logratios: torch.Tensor,
    beta: float,
    label_smoothing: float = 0.0,
) -> torch.Tensor:
    """Standard DPO loss from per-sample log-ratio scalars.

    L = -log σ(β · (chosen_logratio - rejected_logratio))
    """
    logits = beta * (chosen_logratios - rejected_logratios)
    if label_smoothing > 0:
        loss = (
            (1 - label_smoothing) * F.logsigmoid(logits)
            + label_smoothing * F.logsigmoid(-logits)
        )
    else:
        loss = F.logsigmoid(logits)
    return -loss.mean()


def uniform_dpo_loss(
    chosen_logps: torch.Tensor,
    rejected_logps: torch.Tensor,
    ref_chosen_logps: torch.Tensor,
    ref_rejected_logps: torch.Tensor,
    lengths: torch.Tensor,
    beta: float = 0.1,
    label_smoothing: float = 0.0,
) -> torch.Tensor:
    """Standard DPO with uniform per-token weighting (baseline).

    Args:
        chosen_logps: (batch, max_len) per-token log probs for chosen
        rejected_logps: (batch, max_len) per-token log probs for rejected
        ref_chosen_logps: (batch, max_len) reference model per-token log probs
        ref_rejected_logps: (batch, max_len) reference model per-token log probs
        lengths: (batch,) valid token count per sample
        beta: DPO temperature
        label_smoothing: label smoothing factor
    """
    batch_size, max_len = chosen_logps.shape
    mask = torch.arange(max_len, device=chosen_logps.device).unsqueeze(0) < lengths.unsqueeze(1)
    mask = mask.float()

    chosen_sums = (chosen_logps * mask).sum(dim=1)
    rejected_sums = (rejected_logps * mask).sum(dim=1)
    ref_chosen_sums = (ref_chosen_logps * mask).sum(dim=1)
    ref_rejected_sums = (ref_rejected_logps * mask).sum(dim=1)

    chosen_logratios = chosen_sums - ref_chosen_sums
    rejected_logratios = rejected_sums - ref_rejected_sums

    return _dpo_loss_from_logratios(
        chosen_logratios, rejected_logratios, beta, label_smoothing
    )


def single_gamma_dpo_loss(
    chosen_logps: torch.Tensor,
    rejected_logps: torch.Tensor,
    ref_chosen_logps: torch.Tensor,
    ref_rejected_logps: torch.Tensor,
    lengths: torch.Tensor,
    gamma: float = 0.92,
    beta: float = 0.1,
    label_smoothing: float = 0.0,
) -> torch.Tensor:
    """DMPO with a single shared γ for all samples (ablation baseline)."""
    batch_size, max_len = chosen_logps.shape
    device = chosen_logps.device

    results_chosen = torch.zeros(batch_size, device=device)
    results_rejected = torch.zeros(batch_size, device=device)
    results_ref_chosen = torch.zeros(batch_size, device=device)
    results_ref_rejected = torch.zeros(batch_size, device=device)

    for i in range(batch_size):
        T = int(lengths[i].item())
        if T <= 0:
            continue
        w = compute_discount_weights(T, gamma).to(device)
        results_chosen[i] = (chosen_logps[i, :T] * w).sum()
        results_rejected[i] = (rejected_logps[i, :T] * w).sum()
        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()
        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()

    chosen_logratios = results_chosen - results_ref_chosen
    rejected_logratios = results_rejected - results_ref_rejected

    return _dpo_loss_from_logratios(
        chosen_logratios, rejected_logratios, beta, label_smoothing
    )


def etadn_dpo_loss(
    chosen_logps: torch.Tensor,
    rejected_logps: torch.Tensor,
    ref_chosen_logps: torch.Tensor,
    ref_rejected_logps: torch.Tensor,
    error_types: list[str],
    lengths: torch.Tensor,
    config: ETADNConfig,
) -> torch.Tensor:
    """ETADN-aware DPO loss with per-error-type temporal discount.

    For each sample in the batch:
    1. Look up γ_e based on error_type
    2. Compute φ(t, T, γ_e) weights for sequence length T
    3. Compute weighted sum of per-token log prob differences
    4. Apply standard DPO loss with β
    """
    batch_size, max_len = chosen_logps.shape
    device = chosen_logps.device

    results_chosen = torch.zeros(batch_size, device=device)
    results_rejected = torch.zeros(batch_size, device=device)
    results_ref_chosen = torch.zeros(batch_size, device=device)
    results_ref_rejected = torch.zeros(batch_size, device=device)

    for i in range(batch_size):
        T = int(lengths[i].item())
        if T <= 0:
            continue
        gamma = get_gamma_for_error_type(error_types[i], config)
        w = compute_discount_weights(T, gamma).to(device)
        results_chosen[i] = (chosen_logps[i, :T] * w).sum()
        results_rejected[i] = (rejected_logps[i, :T] * w).sum()
        results_ref_chosen[i] = (ref_chosen_logps[i, :T] * w).sum()
        results_ref_rejected[i] = (ref_rejected_logps[i, :T] * w).sum()

    chosen_logratios = results_chosen - results_ref_chosen
    rejected_logratios = results_rejected - results_ref_rejected

    return _dpo_loss_from_logratios(
        chosen_logratios, rejected_logratios, config.beta, config.label_smoothing
    )


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def _test_phi_weights_properties():
    """φ weights: positive, monotonically decreasing for γ<1, γ=1 is uniform."""
    for gamma in [0.5, 0.85, 0.92, 0.97, 0.99]:
        for T in [1, 3, 5, 10, 20]:
            w = compute_discount_weights(T, gamma)
            assert len(w) == T
            assert (w > 0).all(), f"gamma={gamma}, T={T}: non-positive weights"
            for i in range(1, T):
                assert w[i] <= w[i - 1] + 1e-6, (
                    f"gamma={gamma}, T={T}: not monotonically decreasing at {i}"
                )
    # γ=1 → uniform
    w_uniform = compute_discount_weights(5, 1.0)
    assert abs(w_uniform.sum().item() - 1.0) < 1e-5
    assert abs(w_uniform[0].item() - 0.2) < 1e-5
    # scalar φ matches vectorized
    for gamma in [0.85, 0.97]:
        T = 8
        w = compute_discount_weights(T, gamma)
        for t in range(T):
            assert abs(w[t].item() - phi(t, T, gamma)) < 1e-5, (
                f"phi mismatch at t={t}, T={T}, gamma={gamma}"
            )
    print("  phi weights properties: PASS")


def _test_phi_shape_by_gamma():
    """Lower γ → steeper decay; higher γ → more uniform."""
    T = 10
    w_low = compute_discount_weights(T, 0.85)
    w_high = compute_discount_weights(T, 0.97)

    # φ(0,T,γ) = 1 for all γ, so first weight is the same
    assert abs(w_low[0].item() - 1.0) < 1e-5
    assert abs(w_high[0].item() - 1.0) < 1e-5
    # Lower γ decays faster → last weight should be smaller
    assert w_low[-1] < w_high[-1], "Low gamma should decay faster at the tail"
    # γ=0.97 should be more uniform (smaller max-min spread)
    spread_low = (w_low.max() - w_low.min()).item()
    spread_high = (w_high.max() - w_high.min()).item()
    assert spread_low > spread_high, "High gamma should be more uniform"
    print("  phi shape by gamma: PASS")


def _test_dpo_loss_gradients():
    """All three loss variants should produce finite loss and valid gradients."""
    torch.manual_seed(42)
    batch_size, max_len = 4, 8
    config = ETADNConfig()

    chosen = torch.randn(batch_size, max_len, requires_grad=True)
    rejected = torch.randn(batch_size, max_len, requires_grad=True)
    ref_chosen = torch.randn(batch_size, max_len)
    ref_rejected = torch.randn(batch_size, max_len)
    lengths = torch.tensor([6, 8, 5, 7])
    error_types = ["action", "verification", "planning", "action"]

    # Uniform DPO
    loss_u = uniform_dpo_loss(chosen, rejected, ref_chosen, ref_rejected, lengths)
    loss_u.backward(retain_graph=True)
    assert torch.isfinite(loss_u), f"uniform loss not finite: {loss_u}"
    assert chosen.grad is not None
    chosen.grad.zero_()

    # Single-gamma DMPO
    loss_s = single_gamma_dpo_loss(
        chosen, rejected, ref_chosen, ref_rejected, lengths, gamma=0.92
    )
    loss_s.backward(retain_graph=True)
    assert torch.isfinite(loss_s), f"single_gamma loss not finite: {loss_s}"
    chosen.grad.zero_()

    # ETADN
    loss_e = etadn_dpo_loss(
        chosen, rejected, ref_chosen, ref_rejected, error_types, lengths, config
    )
    loss_e.backward()
    assert torch.isfinite(loss_e), f"etadn loss not finite: {loss_e}"

    print(f"  uniform_dpo_loss:      {loss_u.item():.4f}")
    print(f"  single_gamma_dpo_loss: {loss_s.item():.4f}")
    print(f"  etadn_dpo_loss:        {loss_e.item():.4f}")
    print("  gradient check: PASS")


def _test_gamma_lookup():
    """get_gamma_for_error_type should return correct values."""
    config = ETADNConfig()
    assert get_gamma_for_error_type("action", config) == 0.85
    assert get_gamma_for_error_type("verification", config) == 0.92
    assert get_gamma_for_error_type("planning", config) == 1.0
    assert get_gamma_for_error_type("unknown", config) == 0.92  # fallback
    print("  gamma lookup: PASS")


if __name__ == "__main__":
    print("ETADN discount module self-tests")
    print("=" * 40)
    _test_phi_weights_properties()
    _test_phi_shape_by_gamma()
    _test_gamma_lookup()
    _test_dpo_loss_gradients()
    print("=" * 40)
    print("All tests passed.")
