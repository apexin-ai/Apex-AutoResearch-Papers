# KV cache eviction based on aggregated attention scores.
#
# Computes per-position importance by summing the attention weight
# each KV position receives across all query positions and heads.
# Protected positions (BOS by default) are never evicted.

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import torch


@dataclass
class KVMask:
    active_positions: torch.Tensor   # (num_keep,) indices of kept KV positions
    position_mask: torch.Tensor      # (seq_len,) bool mask
    keep_ratio_actual: float         # actual keep ratio after protecting BOS etc.


class KVEvictor:
    def __init__(self, protect_positions: Optional[List[int]] = None):
        """``protect_positions``: indices that are never evicted (default ``[0]`` for BOS)."""
        self.protect_positions = protect_positions if protect_positions is not None else [0]

    def compute_kv_importance(self, attn_weights: torch.Tensor) -> torch.Tensor:
        """Aggregate attention received by each KV position.

        Args:
            attn_weights: ``(batch, num_heads, q_len, kv_len)`` attention
                probability matrix.

        Returns:
            ``(kv_len,)`` importance — total attention mass each KV position
            receives from all queries, heads, and batch elements.
        """
        return attn_weights.sum(dim=(0, 1, 2))  # (kv_len,)

    def select(self, kv_importance: torch.Tensor, keep_ratio: float) -> KVMask:
        """Return a ``KVMask`` keeping the most important positions.

        Protected positions are kept regardless of their importance score.
        """
        seq_len = kv_importance.size(0)
        num_keep = max(1, int(seq_len * keep_ratio))

        protect_set = {p for p in self.protect_positions if 0 <= p < seq_len}
        num_keep = max(num_keep, len(protect_set))
        num_keep = min(num_keep, seq_len)

        # Give protected positions infinite importance so they survive topk
        adjusted = kv_importance.clone()
        for pos in protect_set:
            adjusted[pos] = float("inf")

        _, top_indices = adjusted.topk(num_keep, largest=True)
        active_positions = top_indices.sort().values

        position_mask = torch.zeros(seq_len, dtype=torch.bool, device=kv_importance.device)
        position_mask[active_positions] = True

        return KVMask(
            active_positions=active_positions,
            position_mask=position_mask,
            keep_ratio_actual=active_positions.numel() / seq_len,
        )
