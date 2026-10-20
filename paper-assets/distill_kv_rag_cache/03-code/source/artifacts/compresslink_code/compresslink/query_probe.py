"""ProphetKV-style query relevance probe.

Computes per-token relevance as:
    p_r(t) = (1/L) * sum_l column_sum(softmax(Q_s @ K_l^T / sqrt(d)))
where the column sum is averaged over query tokens and heads.
"""

import torch
from torch import Tensor
from typing import List, Optional, Tuple


class QueryRelevanceProbe:
    """Computes query relevance from attention weights.

    Two usage modes:
    1. compute_relevance(): from pre-computed attention weights (output_attentions=True)
    2. probe(): run query through model and extract relevance in one call
    """

    @staticmethod
    def compute_relevance(attn_weights_per_layer: Tuple[Tensor, ...]) -> Tensor:
        """Compute per-token relevance from attention weight tensors.

        Args:
            attn_weights_per_layer: tuple of [batch, heads, q_len, kv_len] per layer

        Returns:
            [kv_len] relevance scores averaged over layers, heads, queries
        """
        relevance_per_layer = []
        for attn in attn_weights_per_layer:
            q_len = attn.shape[2]
            kv_len = attn.shape[3]
            # Column sum: sum over query dim, normalize
            col_sum = attn.sum(dim=2) / q_len  # [B, H, kv_len]
            col_sum = col_sum.mean(dim=(0, 1))  # [kv_len]
            relevance_per_layer.append(col_sum)

        return torch.stack(relevance_per_layer).mean(dim=0)  # [kv_len]

    @staticmethod
    def probe(
        model,
        query_input_ids: Tensor,
        past_key_value,
        position_ids: Optional[Tensor] = None,
    ) -> Tensor:
        """Run query through model with KV cache and return relevance scores.

        The model should already be NoPE-patched so that cached keys get
        dynamic RoPE during attention computation.

        Args:
            model: NoPE-patched causal LM
            query_input_ids: [batch, q_len]
            past_key_value: DynamicCache with NoPE keys
            position_ids: [batch, q_len] query position ids

        Returns:
            [kv_len] relevance scores (kv_len = cache length before query)
        """
        with torch.no_grad():
            outputs = model(
                input_ids=query_input_ids,
                past_key_values=past_key_value,
                position_ids=position_ids,
                output_attentions=True,
                use_cache=False,
            )

        # attentions: tuple of [B, H, q_len, kv_len+q_len] per layer
        # We only want relevance for the cache tokens (first kv_len positions)
        attn_tuple = outputs.attentions
        kv_len = past_key_value.layers[0].keys.shape[2]
        cache_attns = tuple(a[:, :, :, :kv_len] for a in attn_tuple)

        return QueryRelevanceProbe.compute_relevance(cache_attns)
