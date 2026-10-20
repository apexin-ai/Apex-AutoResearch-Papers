"""CEGR-MSE: Compression-Error-Guided Restoration.

Selects tokens for restoration based on joint score:
    score = r_q * epsilon^beta
where r_q is query relevance and epsilon is per-token compression error.
Only non-boundary tokens are candidates.
"""

import torch
from torch import Tensor
from typing import List


class CEGRSelector:
    def __init__(self, beta: float = 1.0):
        self.beta = beta

    def compute_compression_error(
        self, original_kv: Tensor, decompressed_kv: Tensor
    ) -> Tensor:
        """Per-token MSE between original and decompressed KV.

        Handles arbitrary tensor shapes by averaging all dims except the token dim.

        Args:
            original_kv: [L, B, H, T, D] or [T, D]
            decompressed_kv: same shape

        Returns:
            [T] MSE per token
        """
        diff_sq = (original_kv - decompressed_kv) ** 2
        if original_kv.dim() == 2:
            return diff_sq.mean(dim=-1)
        elif original_kv.dim() == 5:
            # [L, B, H, T, D] -> average over L, B, H, D
            return diff_sq.mean(dim=(0, 1, 2, 4))
        else:
            # [L, B, H, T, D] is canonical; for 4D assume [B, H, T, D]
            token_dim = -2
            dims = [d for d in range(diff_sq.dim()) if d != diff_sq.dim() + token_dim]
            return diff_sq.mean(dim=dims)

    def select_restoration_tokens(
        self,
        query_relevance: Tensor,
        compression_error: Tensor,
        non_boundary_indices: List[int],
        num_to_select: int,
    ) -> List[int]:
        """Select top-scoring non-boundary tokens for restoration.

        score = r_q * epsilon^beta  (multiplicative)

        Args:
            query_relevance: [num_tokens] relevance scores from query probe
            compression_error: [num_tokens] per-token MSE
            non_boundary_indices: only these tokens are scored
            num_to_select: how many tokens to select (from budget manager)

        Returns:
            sorted list of selected token indices
        """
        if num_to_select <= 0 or len(non_boundary_indices) == 0:
            return []

        nb_idx = torch.tensor(
            non_boundary_indices, device=query_relevance.device, dtype=torch.long
        )
        nb_relevance = query_relevance[nb_idx]
        nb_error = compression_error[nb_idx]

        scores = nb_relevance * (nb_error**self.beta)

        k = min(num_to_select, len(nb_idx))
        _, topk_local = scores.topk(k)
        selected = nb_idx[topk_local].tolist()
        return sorted(selected)
