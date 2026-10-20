"""Recomputation budget manager: total -> boundary (fixed) -> CEGR/ProphetKV (variable)."""

from typing import List, Dict


class RecomputationBudgetManager:
    """Manages recomputation budget allocation.

    Total budget -> boundary deduction (fixed) -> remaining for CEGR/ProphetKV (variable).
    """

    def __init__(self, total_budget: float = 0.2, block_size: int = 32):
        self.total_budget = total_budget
        self.block_size = block_size

    def allocate(self, num_tokens: int, chunk_boundaries: List[int]) -> Dict:
        """Allocate recomputation budget.

        Args:
            num_tokens: total token count in the KV cache
            chunk_boundaries: positions where chunk boundaries occur

        Returns:
            dict with boundary_indices, boundary_budget, cegr_budget,
            cegr_num_tokens, non_boundary_indices
        """
        boundary_indices = []
        for b in chunk_boundaries:
            boundary_indices.extend(range(b, min(b + self.block_size, num_tokens)))
        boundary_indices = sorted(set(boundary_indices))

        boundary_budget = len(boundary_indices) / num_tokens if num_tokens > 0 else 0.0
        cegr_budget = max(0.0, self.total_budget - boundary_budget)
        cegr_num = int(cegr_budget * num_tokens)

        all_indices = set(range(num_tokens))
        non_boundary = sorted(all_indices - set(boundary_indices))

        return {
            "boundary_indices": boundary_indices,
            "boundary_budget": boundary_budget,
            "cegr_budget": cegr_budget,
            "cegr_num_tokens": cegr_num,
            "non_boundary_indices": non_boundary,
        }
