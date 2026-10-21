"""Margin-aware token selection: soft masking (train) / hard prune+merge (inference).

Training: applies soft sigmoid mask to visual tokens (fully differentiable).
Inference: three-partition — preserve (top-k), prune (bottom), merge (borderline) —
           borderline tokens are weighted-averaged into their nearest preserved token.

Inputs:  (B, N) scores, (B, N, D) visual tokens, integer k.
Depends: soft_topk.SoftTopK.
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from typing import Dict, Tuple, Optional

from .soft_topk import SoftTopK


class MarginAwareTokenSelector(nn.Module):
    def __init__(self, temperature: float = 1.0, merge_weight_temp: float = 0.5):
        super().__init__()
        self.soft_topk = SoftTopK(temperature=temperature, method="sigmoid")
        self.merge_weight_temp = merge_weight_temp

    def forward(
        self,
        importance_scores: Tensor,
        visual_tokens: Tensor,
        k: int,
        training: bool = True,
    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:
        """
        Args:
            importance_scores: (B, N) per-token scores.
            visual_tokens:     (B, N, D) visual token embeddings.
            k: number of tokens to retain.
            training: soft mask (True) or hard prune/merge (False).
        Returns:
            selected_tokens: (B, N, D) soft-masked  or  (B, K', D) hard-selected.
            selection_mask:  (B, N) soft or binary mask.
            info: dict with diagnostic stats.
        """
        if training:
            return self._soft_forward(importance_scores, visual_tokens, k)
        return self._hard_forward(importance_scores, visual_tokens, k)

    # ------------------------------------------------------------------
    def _soft_forward(
        self, scores: Tensor, tokens: Tensor, k: int
    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:
        mask, s_k, s_k1 = self.soft_topk(scores, k)
        selected = tokens * mask.unsqueeze(-1)  # (B, N, D)
        info = {
            "mode": torch.tensor(0),  # 0 = soft
            "mask_sum": mask.sum(-1).detach(),
            "margin": (s_k - s_k1).detach(),
        }
        return selected, mask, info

    # ------------------------------------------------------------------
    def _hard_forward(
        self, scores: Tensor, tokens: Tensor, k: int
    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:
        B, N, D = tokens.shape

        sorted_scores, sorted_idx = torch.sort(scores, dim=-1, descending=True)
        s_k = sorted_scores[:, k - 1]          # (B,) k-th largest score
        s_k_plus_1 = sorted_scores[:, k]       # (B,) (k+1)-th largest score
        delta_k = s_k - s_k_plus_1             # (B,) margin

        threshold_high = (s_k + delta_k / 2).unsqueeze(-1)   # (B, 1)
        threshold_low = (s_k - delta_k / 2).unsqueeze(-1)    # (B, 1)

        preserve_idx = sorted_idx[:, :k]                                 # (B, k)
        is_topk = torch.zeros(B, N, device=scores.device, dtype=torch.bool)
        is_topk.scatter_(1, preserve_idx, True)

        borderline_mask = ~is_topk & (scores >= threshold_low) & (scores <= threshold_high)
        prune_mask = ~is_topk & (scores < threshold_low)

        binary_mask = is_topk.float()
        selected = tokens * binary_mask.unsqueeze(-1)  # (B, N, D) — same shape as soft

        info = {
            "mode": torch.tensor(1),  # 1 = hard
            "num_preserved": is_topk.sum(-1).float().detach(),
            "num_pruned": prune_mask.sum(-1).float().detach(),
            "num_merged": borderline_mask.sum(-1).float().detach(),
            "delta_k": delta_k.detach(),
        }
        return selected, binary_mask, info

    # ------------------------------------------------------------------
    def _merge_borderline_tokens(
        self,
        tokens: Tensor,
        scores: Tensor,
        preserved_tokens: Tensor,
        preserve_idx: Tensor,
        borderline_mask: Tensor,
    ) -> Tensor:
        """Weighted-merge each borderline token into cosine-nearest preserved token."""
        B, N, D = tokens.shape
        K = preserved_tokens.shape[1]

        num_borderline = borderline_mask.sum(-1)  # (B,)
        if num_borderline.sum() == 0:
            return preserved_tokens

        # Cosine similarity: borderline -> preserved
        preserved_norm = F.normalize(preserved_tokens, dim=-1)  # (B, K, D)
        tokens_norm = F.normalize(tokens, dim=-1)               # (B, N, D)

        # Similarity of all tokens to preserved tokens: (B, N, K)
        sim = torch.bmm(tokens_norm, preserved_norm.transpose(1, 2))

        # For each borderline token, find best preserved match
        best_match = sim.argmax(dim=-1)  # (B, N) — index into K

        # Importance-based merge weights
        preserve_scores = torch.gather(scores, 1, preserve_idx)  # (B, K)

        merged = preserved_tokens.clone()
        # TODO: vectorize this loop for better GPU efficiency
        for b in range(B):
            border_idx = borderline_mask[b].nonzero(as_tuple=True)[0]
            if border_idx.numel() == 0:
                continue
            for idx in border_idx:
                target = best_match[b, idx].item()
                w_border = torch.sigmoid(scores[b, idx] / (self.merge_weight_temp + 1e-8))
                w_orig = torch.sigmoid(preserve_scores[b, target] / (self.merge_weight_temp + 1e-8))
                total_w = w_orig + w_border + 1e-8
                merged[b, target] = (w_orig / total_w) * merged[b, target] + (w_border / total_w) * tokens[b, idx]

        return merged


if __name__ == "__main__":
    torch.manual_seed(42)
    B, N, D, k = 2, 32, 64, 8
    scores = torch.randn(B, N, requires_grad=True)
    tokens = torch.randn(B, N, D)

    selector = MarginAwareTokenSelector(temperature=0.5)

    # Training mode
    sel_train, mask_train, info_train = selector(scores, tokens, k, training=True)
    sel_train.sum().backward()
    print(f"[train] shape={sel_train.shape}, mask_sum={info_train['mask_sum']}, "
          f"grad OK={scores.grad is not None}")
    scores.grad = None

    # Inference mode
    with torch.no_grad():
        sel_inf, mask_inf, info_inf = selector(scores, tokens, k, training=False)
    print(f"[infer] shape={sel_inf.shape}, preserved={info_inf['num_preserved']}, "
          f"pruned={info_inf['num_pruned']}, merged={info_inf['num_merged']}")
