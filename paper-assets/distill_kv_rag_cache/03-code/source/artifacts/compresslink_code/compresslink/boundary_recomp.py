"""Boundary recomputation: fixed, query-independent restoration of chunk-boundary tokens.

Chunk-boundary tokens (first block of each chunk) lack cross-chunk attention context.
They are unconditionally recomputed regardless of query content.
"""

import torch
from torch import Tensor
from typing import List


class BoundaryRecomputer:
    def __init__(self, block_size: int = 32):
        self.block_size = block_size

    def get_boundary_indices(
        self, num_tokens: int, chunk_boundaries: List[int]
    ) -> List[int]:
        """Return all boundary token indices (first block of each chunk).

        These tokens are unconditionally recomputed, not scored.
        """
        indices = []
        for b in chunk_boundaries:
            indices.extend(range(b, min(b + self.block_size, num_tokens)))
        return sorted(set(indices))

    def restore_from_original(
        self, original_cache, decompressed_cache, boundary_indices: List[int]
    ):
        """Replace boundary tokens in decompressed cache with original values.

        MVP simulation of recomputation: the original cache (from full-context
        NoPE forward) provides the exact values that real recomputation would produce.

        Modifies decompressed_cache in-place.
        """
        if not boundary_indices:
            return

        idx = torch.tensor(boundary_indices)
        for layer_idx in range(len(decompressed_cache.layers)):
            decompressed_cache.layers[layer_idx].keys[:, :, idx] = (
                original_cache.layers[layer_idx].keys[:, :, idx]
            )
            decompressed_cache.layers[layer_idx].values[:, :, idx] = (
                original_cache.layers[layer_idx].values[:, :, idx]
            )

    def compute_boundary_budget(
        self, num_tokens: int, chunk_boundaries: List[int]
    ) -> float:
        n = len(self.get_boundary_indices(num_tokens, chunk_boundaries))
        return n / num_tokens if num_tokens > 0 else 0.0
