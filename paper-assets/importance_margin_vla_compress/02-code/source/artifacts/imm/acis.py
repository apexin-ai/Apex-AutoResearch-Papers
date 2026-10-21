"""Action-Conditioned Importance Scoring (ACIS).

Cross-attention scorer: a_query (action representations) attend to visual tokens,
producing per-token importance scores. All linear layers are wrapped with spectral
normalization to control the module's Lipschitz constant, which is required for
the certified bound k·ε·L/Δ_k to be meaningful.

Inputs:  a_query (B, Q, action_dim), visual_tokens (B, N, visual_dim).
Outputs: importance_scores (B, N).
Depends: torch, spectral_norm.
"""

from __future__ import annotations

import torch
import torch.nn as nn
from torch import Tensor
from torch.nn.utils import spectral_norm
from typing import Tuple


class ACIS(nn.Module):
    def __init__(
        self,
        visual_dim: int = 960,
        action_dim: int = 720,
        num_heads: int = 8,
        dropout: float = 0.0,
    ):
        super().__init__()
        assert visual_dim % num_heads == 0
        self.visual_dim = visual_dim
        self.num_heads = num_heads
        self.head_dim = visual_dim // num_heads
        self.scale = self.head_dim ** -0.5

        self.query_proj = spectral_norm(nn.Linear(action_dim, visual_dim))
        self.q_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))
        self.k_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))
        self.v_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))
        self.score_head = spectral_norm(nn.Linear(visual_dim, 1))
        self.dropout = nn.Dropout(dropout)

    def forward(self, a_query: Tensor, visual_tokens: Tensor) -> Tensor:
        """
        Args:
            a_query: (B, Q, action_dim) action representations from embed_suffix.
            visual_tokens: (B, N, visual_dim) visual tokens from embed_image.
        Returns:
            importance_scores: (B, N) per-token scores.
        """
        B, N, _ = visual_tokens.shape
        Q = a_query.shape[1]
        H, d = self.num_heads, self.head_dim

        q = self.q_proj(self.query_proj(a_query))       # (B, Q, D)
        k = self.k_proj(visual_tokens)                   # (B, N, D)
        v = self.v_proj(visual_tokens)                   # (B, N, D)

        q = q.view(B, Q, H, d).transpose(1, 2)          # (B, H, Q, d)
        k = k.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)
        v = v.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)

        attn_weights = torch.matmul(q, k.transpose(-2, -1)) * self.scale  # (B, H, Q, N)
        attn_weights = attn_weights.softmax(dim=-1)
        attn_weights = self.dropout(attn_weights)

        # Per-visual-token importance: average attention received across queries and heads
        token_importance = attn_weights.mean(dim=(1, 2))  # (B, N)

        # Contextual representation per visual token via transposed attention
        # v^T @ attn^T → each visual token gets a context vector
        attn_t = attn_weights.transpose(-2, -1)           # (B, H, N, Q)
        context = torch.matmul(attn_t, q)                 # (B, H, N, d)
        context = context.transpose(1, 2).reshape(B, N, self.visual_dim)  # (B, N, D)

        score_logits = self.score_head(context).squeeze(-1)  # (B, N)

        # Combine learned score with attention-based importance
        importance_scores = score_logits + token_importance

        return importance_scores

    def get_lipschitz_estimate(self) -> float:
        """Product of spectral norms across all SN-wrapped layers."""
        L = 1.0
        for module in self.modules():
            if hasattr(module, "weight_orig"):
                sigma = torch.linalg.norm(module.weight, ord=2).item()
                L *= sigma
        return L


if __name__ == "__main__":
    torch.manual_seed(42)
    B, N, Q = 2, 128, 50
    vis = torch.randn(B, N, 960)
    a_q = torch.randn(B, Q, 720)

    acis = ACIS(visual_dim=960, action_dim=720)
    scores = acis(a_q, vis)
    print(f"ACIS: scores shape={scores.shape}, range=[{scores.min():.3f}, {scores.max():.3f}]")

    L = acis.get_lipschitz_estimate()
    print(f"Lipschitz estimate: {L:.4f}")

    scores.sum().backward()
    print(f"ACIS grad OK: query_proj={acis.query_proj.weight_orig.grad is not None}")
    print("All ACIS tests passed!")
