"""Importance Margin Maximization losses.

MarginMaximizationLoss: hinge loss  max(0, delta - (s_{(k)} - s_{(k+1)})).
IMMTotalLoss:           L_action + lambda * L_margin  with linear lambda warmup.

Inputs:  (B, N) importance scores, integer k.
Depends: soft_topk.SoftTopK.
"""

from __future__ import annotations

import torch
import torch.nn as nn
from torch import Tensor
from typing import Dict, Tuple

from .soft_topk import SoftTopK


class MarginMaximizationLoss(nn.Module):
    """Hinge loss: L_margin = mean(max(0, delta - (s_{(k)} - s_{(k+1)})))."""

    def __init__(self, delta: float = 1.0, temperature: float = 1.0, method: str = "sigmoid"):
        super().__init__()
        self.delta = delta
        self.soft_topk = SoftTopK(temperature=temperature, method=method)

    def forward(self, importance_scores: Tensor, k: int) -> Tuple[Tensor, Dict[str, Tensor]]:
        """
        Args:
            importance_scores: (B, N) per-token importance scores.
            k: number of tokens to retain.
        Returns:
            loss: scalar hinge loss.
            info: dict with margin, s_k, s_k_plus_1, mask for logging.
        """
        mask, s_k, s_k_plus_1 = self.soft_topk(importance_scores, k)

        margin = s_k - s_k_plus_1  # (B,)
        hinge = torch.clamp(self.delta - margin, min=0.0)  # (B,)
        loss = hinge.mean()

        info = {
            "margin": margin.detach(),
            "s_k": s_k.detach(),
            "s_k_plus_1": s_k_plus_1.detach(),
            "hinge": hinge.detach(),
            "mask": mask.detach(),
        }
        return loss, info


class IMMTotalLoss(nn.Module):
    """L_total = L_action + lambda * L_margin, with linear lambda warmup."""

    def __init__(
        self,
        lambda_margin: float = 0.1,
        delta: float = 1.0,
        warmup_steps: int = 1000,
        temperature: float = 1.0,
        method: str = "sigmoid",
    ):
        super().__init__()
        self.lambda_margin = lambda_margin
        self.warmup_steps = warmup_steps
        self.margin_loss = MarginMaximizationLoss(delta=delta, temperature=temperature, method=method)

    def _get_lambda(self, step: int) -> float:
        if self.warmup_steps <= 0:
            return self.lambda_margin
        return self.lambda_margin * min(1.0, step / self.warmup_steps)

    def forward(
        self, action_loss: Tensor, importance_scores: Tensor, k: int, step: int
    ) -> Tuple[Tensor, Dict[str, Tensor]]:
        """
        Args:
            action_loss: scalar task loss (e.g. action prediction).
            importance_scores: (B, N).
            k: retention count.
            step: current training step (for warmup).
        Returns:
            total_loss: scalar.
            info: dict with all sub-losses and diagnostics.
        """
        lam = self._get_lambda(step)
        margin_loss, margin_info = self.margin_loss(importance_scores, k)
        total = action_loss + lam * margin_loss

        info = {
            **margin_info,
            "action_loss": action_loss.detach(),
            "margin_loss": margin_loss.detach(),
            "total_loss": total.detach(),
            "lambda": torch.tensor(lam),
        }
        return total, info


if __name__ == "__main__":
    torch.manual_seed(42)
    B, N, k = 4, 64, 16
    scores = torch.randn(B, N, requires_grad=True)
    action_loss = torch.tensor(1.5, requires_grad=True)

    mmr = MarginMaximizationLoss(delta=0.5, temperature=0.5)
    loss, info = mmr(scores, k)
    loss.backward()
    print(f"MMR: loss={loss.item():.4f}, margin_mean={info['margin'].mean().item():.4f}, "
          f"grad OK={scores.grad is not None}")
    scores.grad = None

    total_loss_fn = IMMTotalLoss(lambda_margin=0.1, delta=0.5, warmup_steps=100, temperature=0.5)
    total, tinfo = total_loss_fn(action_loss, scores, k, step=50)
    total.backward()
    print(f"Total: loss={total.item():.4f}, lambda={tinfo['lambda'].item():.4f}, "
          f"grad OK={scores.grad is not None}")
