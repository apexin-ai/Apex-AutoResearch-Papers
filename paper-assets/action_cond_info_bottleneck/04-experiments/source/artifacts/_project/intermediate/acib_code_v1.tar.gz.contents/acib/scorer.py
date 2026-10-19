# ACIB Scorer: token-level relevance scoring conditioned on action context.
# Operates on visual tokens (B, N, D) after PixelShuffle + Linear Proj,
# before they enter the VLM transformer layers.
# Outputs per-token scores used for soft reweighting or hard pruning.

import torch
import torch.nn as nn
import torch.nn.functional as F

from acib.config import ACIBConfig


class ACIBScorer(nn.Module):
    """Score each visual token's action-relevance given a conditioning signal.

    Args:
        config: ACIBConfig with architecture and mode settings.

    Forward:
        visual_tokens: (B, N, D_v) — PixelShuffle output, N=64, D_v=960
        condition: (B, D_c) — pooled language embedding or robot state
    Returns:
        weights: (B, N) — per-token importance weights
        scores_logits: (B, N) — raw logits before sigmoid (for loss computation)
    """

    def __init__(self, config: ACIBConfig):
        super().__init__()
        self.config = config
        self.mode = config.mode

        input_dim = config.visual_dim + config.condition_dim

        self.mlp = nn.Sequential(
            nn.Linear(input_dim, config.hidden_dim),
            nn.GELU(),
            nn.Linear(config.hidden_dim, 1),
        )

    def forward(
        self,
        visual_tokens: torch.Tensor,
        condition: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        B, N, D_v = visual_tokens.shape

        # Expand condition to match each token: (B, D_c) -> (B, N, D_c)
        condition_expanded = condition.unsqueeze(1).expand(-1, N, -1)

        # Concatenate visual + condition per token: (B, N, D_v + D_c)
        combined = torch.cat([visual_tokens, condition_expanded], dim=-1)

        # Score each token: (B, N, 1) -> (B, N)
        logits = self.mlp(combined).squeeze(-1)

        if self.mode == "soft":
            weights = torch.sigmoid(logits)
        elif self.mode == "hard":
            weights = self._hard_topk(logits)
        else:
            raise ValueError(f"Unknown mode: {self.mode}")

        return weights, logits

    def _hard_topk(self, logits: torch.Tensor) -> torch.Tensor:
        """Top-k selection with straight-through gradient estimator."""
        B, N = logits.shape
        k = max(1, int(N * self.config.top_k_ratio))

        _, topk_indices = logits.topk(k, dim=-1)
        mask = torch.zeros_like(logits)
        mask.scatter_(-1, topk_indices, 1.0)

        # Straight-through: forward uses hard mask, backward uses sigmoid
        soft = torch.sigmoid(logits)
        return mask - soft.detach() + soft

    def apply_weights(
        self, visual_tokens: torch.Tensor, weights: torch.Tensor
    ) -> torch.Tensor:
        """Reweight visual tokens by scorer output.

        Args:
            visual_tokens: (B, N, D)
            weights: (B, N)
        Returns:
            weighted_tokens: (B, N, D) — element-wise scaled tokens
        """
        return visual_tokens * weights.unsqueeze(-1)
