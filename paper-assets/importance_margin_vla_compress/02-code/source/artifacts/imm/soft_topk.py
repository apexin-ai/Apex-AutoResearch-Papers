"""Differentiable Top-K selection for importance-based token compression.

Three methods:
  - 'sigmoid': Temperature-scaled sigmoid mask around a soft threshold (simple, reliable).
  - 'sinkhorn': Optimal-transport-inspired soft top-k via Sinkhorn iterations (theoretically tighter).
  - 'implicit_diff': Binary-search shift + implicit function theorem for exact top-k gradients.

Inputs:  (B, N) importance scores, integer k.
Outputs: (B, N) soft mask, s_{(k)}, s_{(k+1)} — all differentiable.
Depends: torch.
"""

from __future__ import annotations

import torch
import torch.nn as nn
from torch import Tensor
from typing import Tuple


class SoftTopK(nn.Module):
    def __init__(self, temperature: float = 1.0, method: str = "sigmoid"):
        super().__init__()
        self.temperature = temperature
        assert method in ("sigmoid", "sinkhorn", "implicit_diff"), f"Unknown method: {method}"
        self.method = method
        self._sinkhorn_iters = 20
        self._bisect_iters = 32

    def forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:
        """
        Args:
            scores: (B, N) importance scores.
            k: number of tokens to retain.
        Returns:
            mask:       (B, N) soft selection mask in [0, 1].
            s_k:        (B,)   differentiable k-th largest score.
            s_k_plus_1: (B,)   differentiable (k+1)-th largest score.
        """
        if self.method == "sigmoid":
            return self._sigmoid_forward(scores, k)
        if self.method == "implicit_diff":
            return self._implicit_diff_forward(scores, k)
        return self._sinkhorn_forward(scores, k)

    # ------------------------------------------------------------------
    # Method A: Temperature-based sigmoid
    # ------------------------------------------------------------------
    def _sigmoid_forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:
        B, N = scores.shape
        assert 0 < k < N, f"k={k} must be in (0, {N})"

        sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)
        s_k = sorted_scores[:, k - 1]          # (B,)
        s_k_plus_1 = sorted_scores[:, k]       # (B,)

        # Soft threshold: midpoint between s_{(k)} and s_{(k+1)}
        threshold = 0.5 * (s_k + s_k_plus_1)   # (B,)

        tau = self.temperature + 1e-8
        mask = torch.sigmoid((scores - threshold.unsqueeze(-1)) / tau)  # (B, N)

        return mask, s_k, s_k_plus_1

    # ------------------------------------------------------------------
    # Method B: Sinkhorn-based optimal transport
    # ------------------------------------------------------------------
    def _sinkhorn_forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:
        B, N = scores.shape
        assert 0 < k < N

        # Extract s_k, s_{k+1} the same way (needed for margin loss)
        sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)
        s_k = sorted_scores[:, k - 1]
        s_k_plus_1 = sorted_scores[:, k]

        # OT formulation: row marginals = [k, N-k], col marginals = 1 each
        # Cost matrix C: higher score -> lower cost to be "selected"
        tau = self.temperature + 1e-8
        log_alpha = scores / tau  # (B, N) — log-potential for selection

        # Sinkhorn in log-space for numerical stability
        # We solve for a (B, N) assignment where sum = k
        # Using a simplified 1D Sinkhorn: iteratively project onto simplex with sum=k
        log_mask = log_alpha.clone()
        for _ in range(self._sinkhorn_iters):
            # Normalize so that sum of exp(log_mask) = k
            log_sum = torch.logsumexp(log_mask, dim=-1, keepdim=True)
            log_mask = log_mask - log_sum + torch.log(torch.tensor(k, dtype=scores.dtype, device=scores.device))
            # Clamp individual entries to [0, 1] in probability space
            log_mask = log_mask - torch.nn.functional.softplus(log_mask)  # ≈ min(log_mask, 0)

        mask = torch.exp(log_mask).clamp(0.0, 1.0)

        return mask, s_k, s_k_plus_1

    # ------------------------------------------------------------------
    # Method C: Implicit differentiation (binary search + IFT)
    # ------------------------------------------------------------------
    def _implicit_diff_forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:
        B, N = scores.shape
        assert 0 < k < N

        sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)
        s_k = sorted_scores[:, k - 1]
        s_k_plus_1 = sorted_scores[:, k]

        mask = _ImplicitTopK.apply(scores, k, self.temperature, self._bisect_iters)

        return mask, s_k, s_k_plus_1


class _ImplicitTopK(torch.autograd.Function):
    """Binary-search shift t s.t. sum(sigma((x_i + t) / tau)) = k, with IFT backward."""

    @staticmethod
    def forward(ctx, scores: Tensor, k: int, temperature: float, bisect_iters: int) -> Tensor:
        tau = temperature + 1e-8
        B, N = scores.shape

        # Binary search for shift t per sample
        lo = -scores.max(dim=-1).values - 10.0  # (B,)
        hi = -scores.min(dim=-1).values + 10.0   # (B,)

        for _ in range(bisect_iters):
            mid = 0.5 * (lo + hi)
            val = torch.sigmoid((scores + mid.unsqueeze(-1)) / tau).sum(dim=-1)
            lo = torch.where(val < k, mid, lo)
            hi = torch.where(val >= k, mid, hi)

        t_star = 0.5 * (lo + hi)  # (B,)
        mask = torch.sigmoid((scores + t_star.unsqueeze(-1)) / tau)  # (B, N)

        ctx.save_for_backward(scores, mask, t_star)
        ctx.tau = tau
        return mask

    @staticmethod
    def backward(ctx, grad_output: Tensor):
        scores, mask, t_star = ctx.saved_tensors
        tau = ctx.tau

        # sigma'(z) = sigma(z) * (1 - sigma(z))
        sigma_prime = mask * (1.0 - mask)  # (B, N)
        denom = sigma_prime.sum(dim=-1, keepdim=True).clamp(min=1e-8)  # (B, 1)

        # IFT: dt/dx_i = -sigma'_i / sum_j sigma'_j
        # d mask_i / d x_j = sigma'_i / tau * (delta_{ij} - sigma'_j / sum sigma')
        # => grad_scores = grad_output * sigma'/ tau - (sigma'/tau) * (sum(grad_output * sigma') / sum(sigma'))
        g_weighted = (grad_output * sigma_prime).sum(dim=-1, keepdim=True)  # (B, 1)
        grad_scores = (sigma_prime / tau) * (grad_output - g_weighted / denom)

        return grad_scores, None, None, None


if __name__ == "__main__":
    torch.manual_seed(42)
    B, N, k = 4, 64, 16
    scores = torch.randn(B, N, requires_grad=True)

    for method in ("sigmoid", "sinkhorn", "implicit_diff"):
        topk = SoftTopK(temperature=0.5, method=method)
        mask, s_k, s_k1 = topk(scores, k)
        loss = mask.sum()
        loss.backward()
        print(f"[{method}] mask: {mask.shape}, sum~={mask.sum(-1).tolist()}, "
              f"s_k={s_k.tolist()}, grad OK={scores.grad is not None}")
        scores.grad = None
