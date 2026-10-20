"""
CARC KV Cache Eviction — budget-triggered eviction with recurrence-aware protection.

When KV cache length exceeds a preset budget, evicts tokens with the highest
cumulative EMA similarity scores (most redundant), while protecting recent tokens
within a grace window and the attention sink (position 0).

Inputs:
  - Per-step EMA similarity scores from EMAAnchorManager (batch, num_layers) or scalar
  - KV cache (DynamicCache or legacy tuple format)

Outputs:
  - Boolean eviction masks
  - Pruned KV caches

Dependencies: torch, transformers (DynamicCache)
"""

from typing import Any, Dict, Optional, Tuple, Union

import torch
import torch.nn.functional as F


class CARCKVEviction:
    """
    Budget-triggered KV cache eviction using cumulative EMA similarity scores.

    When KV cache length exceeds budget, evicts the most redundant tokens
    (highest cumulative EMA score) while protecting recent tokens.
    """

    def __init__(self, budget: int, grace_window: int = 175,
                 evict_ratio: float = 0.1):
        """
        Args:
            budget: Max KV cache length before triggering eviction.
            grace_window: Recent tokens protected from eviction (W_grace).
            evict_ratio: Fraction of over-budget tokens to evict per trigger.
        """
        self.budget = budget
        self.grace_window = grace_window
        self.evict_ratio = evict_ratio

        self._cumulative_scores: Optional[torch.Tensor] = None
        self._length: int = 0

        self._total_evicted: int = 0
        self._eviction_triggers: int = 0
        self._sum_evicted_scores: float = 0.0
        self._current_cache_length: int = 0

    def update_scores(self, ema_scores: torch.Tensor) -> None:
        """
        Accumulate per-token EMA similarity scores.

        Args:
            ema_scores: Current step scores. Supported shapes:
                - (batch, num_layers, 1): per-layer scalar per token — averaged across layers
                - (batch, seq_len): per-token scores from a single layer
                - (seq_len,): unbatched single-layer scores
                - scalar: single score for the latest token
        """
        scores = ema_scores.float().detach()

        if scores.dim() == 0:
            scores = scores.unsqueeze(0)
        if scores.dim() == 3:
            # (batch, num_layers, 1) -> average across layers, squeeze last dim
            scores = scores.mean(dim=1).squeeze(-1)  # (batch,)
        if scores.dim() == 2:
            # (batch, seq_len) -> average across batch
            scores = scores.mean(dim=0)  # (seq_len,)
        # scores is now (seq_len,) or (1,)

        if self._cumulative_scores is None:
            self._cumulative_scores = scores.clone()
            self._length = scores.shape[0]
        else:
            new_len = scores.shape[0]
            if new_len == 1:
                # Appending a single new token score
                self._cumulative_scores = torch.cat([
                    self._cumulative_scores,
                    scores,
                ])
                self._length += 1
            elif new_len == self._length:
                # Full update for all existing positions
                self._cumulative_scores = self._cumulative_scores + scores
            elif new_len > self._length:
                # Scores include new positions beyond current length
                self._cumulative_scores[:self._length] += scores[:self._length]
                self._cumulative_scores = torch.cat([
                    self._cumulative_scores,
                    scores[self._length:],
                ])
                self._length = new_len
            else:
                # Partial update (fewer positions than current — update first new_len)
                self._cumulative_scores[:new_len] += scores

    def should_evict(self, cache_length: int) -> bool:
        """Returns True when cache_length exceeds the budget."""
        self._current_cache_length = cache_length
        return cache_length > self.budget

    def compute_eviction_mask(self, cache_length: int) -> torch.Tensor:
        """
        Compute a boolean keep/evict mask for the KV cache.

        Args:
            cache_length: Current sequence length in the KV cache.

        Returns:
            Boolean tensor of shape (cache_length,). True = keep, False = evict.
        """
        self._current_cache_length = cache_length
        n_evict = int((cache_length - self.budget) * (1.0 + self.evict_ratio))
        n_evict = max(n_evict, 1)

        # Build cumulative scores aligned to cache_length
        if self._cumulative_scores is None or self._cumulative_scores.shape[0] == 0:
            return torch.ones(cache_length, dtype=torch.bool)

        cum = self._cumulative_scores[:cache_length]
        if cum.shape[0] < cache_length:
            # Pad with zeros for positions we haven't scored yet
            cum = F.pad(cum, (0, cache_length - cum.shape[0]), value=0.0)

        # Protection mask: True = protected (cannot be evicted)
        protected = torch.zeros(cache_length, dtype=torch.bool, device=cum.device)
        protected[0] = True  # attention sink
        grace_start = max(cache_length - self.grace_window, 1)
        protected[grace_start:] = True

        # Set protected positions to -inf so they're never selected for eviction
        evictable_scores = cum.clone()
        evictable_scores[protected] = float("-inf")

        n_evictable = (~protected).sum().item()
        n_evict = min(n_evict, n_evictable)

        if n_evict <= 0:
            return torch.ones(cache_length, dtype=torch.bool, device=cum.device)

        # Select top-n_evict highest scores among evictable positions
        _, topk_indices = torch.topk(evictable_scores, n_evict)

        keep_mask = torch.ones(cache_length, dtype=torch.bool, device=cum.device)
        keep_mask[topk_indices] = False

        # Track stats
        evicted_scores = cum[topk_indices]
        self._total_evicted += n_evict
        self._eviction_triggers += 1
        self._sum_evicted_scores += evicted_scores.sum().item()

        # Compact cumulative scores to match new cache after eviction
        self._cumulative_scores = cum[keep_mask]
        self._length = self._cumulative_scores.shape[0]

        return keep_mask

    def apply_eviction(
        self,
        past_key_values: Any,
        eviction_mask: torch.Tensor,
    ) -> Any:
        """
        Apply eviction mask to HuggingFace KV cache.

        Supports:
          - DynamicCache (transformers >= 4.36): key_cache/value_cache lists
          - Legacy tuple format: tuple of (key, value) pairs per layer

        Args:
            past_key_values: The model's KV cache.
            eviction_mask: Boolean tensor (cache_length,). True = keep.

        Returns:
            Pruned past_key_values in the same format as input.
        """
        mask = eviction_mask.bool()

        # DynamicCache path
        if hasattr(past_key_values, "key_cache") and hasattr(past_key_values, "value_cache"):
            for layer_idx in range(len(past_key_values.key_cache)):
                # Shape: (batch, num_heads, seq_len, head_dim)
                k = past_key_values.key_cache[layer_idx]
                v = past_key_values.value_cache[layer_idx]
                seq_mask = mask.to(k.device)
                # Index along seq_len dimension (dim=2)
                past_key_values.key_cache[layer_idx] = k[:, :, seq_mask, :]
                past_key_values.value_cache[layer_idx] = v[:, :, seq_mask, :]
            return past_key_values

        # Legacy tuple format: tuple of (key, value) per layer
        pruned = []
        for layer_kv in past_key_values:
            k, v = layer_kv[0], layer_kv[1]
            seq_mask = mask.to(k.device)
            if k.dim() == 4:
                # (batch, num_heads, seq_len, head_dim)
                pruned.append((k[:, :, seq_mask, :], v[:, :, seq_mask, :]))
            else:
                # (batch, seq_len, dim)
                pruned.append((k[:, seq_mask, :], v[:, seq_mask, :]))
        return tuple(pruned)

    def reset(self) -> None:
        """Clear all accumulated scores and internal state."""
        self._cumulative_scores = None
        self._length = 0
        self._total_evicted = 0
        self._eviction_triggers = 0
        self._sum_evicted_scores = 0.0
        self._current_cache_length = 0

    def eviction_stats(self) -> Dict[str, Union[int, float]]:
        """
        Returns eviction statistics.

        Returns:
            Dict with total_evicted, eviction_triggers, avg_evicted_score,
            and cache_utilization.
        """
        avg_score = 0.0
        if self._total_evicted > 0:
            avg_score = self._sum_evicted_scores / self._total_evicted

        utilization = 0.0
        if self.budget > 0:
            utilization = self._current_cache_length / self.budget

        return {
            "total_evicted": self._total_evicted,
            "eviction_triggers": self._eviction_triggers,
            "avg_evicted_score": avg_score,
            "cache_utilization": utilization,
        }


def create_eviction_hook(eviction_manager: CARCKVEviction, ema_manager) -> callable:
    """
    Creates a generation hook that auto-evicts during model.generate().

    The returned callable has signature compatible with transformers
    GenerationMixin — it can be passed as a logits_processor or called
    manually after each generation step.

    Args:
        eviction_manager: CARCKVEviction instance with budget configured.
        ema_manager: EMAAnchorManager instance for computing per-step scores.

    Returns:
        A callable(step, input_ids, past_key_values, **kwargs) -> past_key_values
        that computes EMA scores, updates the eviction manager, and evicts
        if the cache exceeds budget.
    """

    def hook(
        step: int,
        input_ids: torch.Tensor,
        past_key_values: Any,
        layer_keys: Optional[torch.Tensor] = None,
        layer_values: Optional[torch.Tensor] = None,
        layer_idx: int = 0,
        **kwargs,
    ) -> Any:
        """
        Per-step eviction hook.

        Args:
            step: Current generation step index.
            input_ids: Current input token ids.
            past_key_values: Model's KV cache.
            layer_keys: Key tensor for the current layer (batch, seq_len, dim).
            layer_values: Value tensor for the current layer (batch, seq_len, dim).
            layer_idx: Which layer these K/V belong to.

        Returns:
            Potentially pruned past_key_values.
        """
        if layer_keys is not None and layer_values is not None:
            scores = ema_manager.compute_scores(layer_idx, layer_keys, layer_values)
            eviction_manager.update_scores(scores)

        # Determine cache length
        if hasattr(past_key_values, "key_cache") and len(past_key_values.key_cache) > 0:
            cache_length = past_key_values.key_cache[0].shape[2]
        elif isinstance(past_key_values, tuple) and len(past_key_values) > 0:
            cache_length = past_key_values[0][0].shape[-2]
        else:
            return past_key_values

        if eviction_manager.should_evict(cache_length):
            mask = eviction_manager.compute_eviction_mask(cache_length)
            past_key_values = eviction_manager.apply_eviction(past_key_values, mask)

        return past_key_values

    return hook
