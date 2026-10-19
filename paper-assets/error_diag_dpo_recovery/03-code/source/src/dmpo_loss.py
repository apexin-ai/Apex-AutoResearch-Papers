#!/usr/bin/env python3
"""DMPO loss module -- bridge between etadn_discount.py and train_dpo.py.

Provides phi-weighted DPO loss using discount weights from etadn_discount.
phi weights from compute_discount_weights are already normalized (sum=1).

Input: per-token log probabilities from policy and reference models
Output: scalar DPO loss with temporal discount weighting

Dependencies: etadn_discount (sibling module), torch
"""
import sys
from pathlib import Path

import torch
import torch.nn.functional as F

sys.path.insert(0, str(Path(__file__).resolve().parent))
from etadn_discount import compute_discount_weights


def compute_phi_weights(T: int, gamma: float) -> torch.Tensor:
    """phi weight vector of length T. phi(0)=1 for all gamma, decays for t>0.

    Wraps etadn_discount.compute_discount_weights.
    """
    return compute_discount_weights(T, gamma)


def phi_weighted_logps(logps: torch.Tensor, weights: torch.Tensor) -> torch.Tensor:
    """Phi-weighted sum of per-token log probabilities.

    Args:
        logps: (T,) per-token log probs
        weights: (T,) phi discount weights
    Returns:
        scalar weighted sum
    """
    return (logps * weights).sum()


def dmpo_loss(
    policy_chosen_logps: torch.Tensor,
    policy_rejected_logps: torch.Tensor,
    ref_chosen_logps: torch.Tensor,
    ref_rejected_logps: torch.Tensor,
    weights_chosen: torch.Tensor,
    weights_rejected: torch.Tensor,
    beta: float = 0.1,
) -> torch.Tensor:
    """Phi-weighted DPO loss for a single sample.

    L = -log sigma(beta * (sum phi_c * logr_chosen - sum phi_r * logr_rejected))
    where logr = log pi_policy - log pi_ref
    """
    chosen_logratio = (
        phi_weighted_logps(policy_chosen_logps, weights_chosen)
        - phi_weighted_logps(ref_chosen_logps, weights_chosen)
    )
    rejected_logratio = (
        phi_weighted_logps(policy_rejected_logps, weights_rejected)
        - phi_weighted_logps(ref_rejected_logps, weights_rejected)
    )
    logits = beta * (chosen_logratio - rejected_logratio)
    return -F.logsigmoid(logits)


def dmpo_loss_batch(
    policy_chosen_logps: torch.Tensor,
    policy_rejected_logps: torch.Tensor,
    ref_chosen_logps: torch.Tensor,
    ref_rejected_logps: torch.Tensor,
    chosen_resp_lens: list[int],
    rejected_resp_lens: list[int],
    prompt_lens: list[int],
    gammas: list[float],
    beta: float = 0.1,
) -> tuple[torch.Tensor, dict]:
    """Batched phi-weighted DPO loss.

    Per-token logps are padded tensors of shape (B, max_len). Response tokens
    for sample i span [prompt_lens[i], prompt_lens[i] + resp_len).

    Returns (mean_loss, metrics_dict).
    """
    B = policy_chosen_logps.shape[0]
    device = policy_chosen_logps.device
    losses = []
    chosen_rewards = []
    rejected_rewards = []

    for i in range(B):
        pl = prompt_lens[i]
        c_rl = chosen_resp_lens[i]
        r_rl = rejected_resp_lens[i]

        if c_rl <= 0 or r_rl <= 0:
            continue

        gamma = gammas[i]
        w_c = compute_phi_weights(c_rl, gamma).to(device)
        w_r = compute_phi_weights(r_rl, gamma).to(device)

        loss_i = dmpo_loss(
            policy_chosen_logps[i, pl : pl + c_rl],
            policy_rejected_logps[i, pl : pl + r_rl],
            ref_chosen_logps[i, pl : pl + c_rl],
            ref_rejected_logps[i, pl : pl + r_rl],
            w_c,
            w_r,
            beta,
        )
        losses.append(loss_i)

        with torch.no_grad():
            cr = phi_weighted_logps(
                policy_chosen_logps[i, pl : pl + c_rl], w_c
            ) - phi_weighted_logps(ref_chosen_logps[i, pl : pl + c_rl], w_c)
            rr = phi_weighted_logps(
                policy_rejected_logps[i, pl : pl + r_rl], w_r
            ) - phi_weighted_logps(ref_rejected_logps[i, pl : pl + r_rl], w_r)
            chosen_rewards.append(cr)
            rejected_rewards.append(rr)

    if not losses:
        return torch.tensor(0.0, device=device, requires_grad=True), {}

    loss = torch.stack(losses).mean()
    cr_t = torch.stack(chosen_rewards)
    rr_t = torch.stack(rejected_rewards)
    metrics = {
        "chosen_reward": cr_t.mean().item(),
        "rejected_reward": rr_t.mean().item(),
        "reward_margin": (cr_t - rr_t).mean().item(),
        "reward_accuracy": (cr_t > rr_t).float().mean().item(),
    }
    return loss, metrics
