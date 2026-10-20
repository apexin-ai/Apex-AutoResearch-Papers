# Head importance evaluation and masking with GQA support.
#
# Computes per-Q-head importance via attention output L2 norms,
# selects heads to keep, and determines which KV heads can be
# skipped when all their associated Q heads are masked.
#
# GQA mapping for DeepSeek-R1-Distill-Qwen-7B:
#   28 Q heads → 4 KV heads, group size 7
#   KV 0 serves Q [0..6], KV 1 serves Q [7..13], etc.

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import torch


@dataclass
class HeadMask:
    active_q_heads: List[int]      # indices of Q heads to keep
    active_kv_heads: List[int]     # indices of KV heads still needed
    q_head_mask: torch.Tensor      # (num_q_heads,) bool
    kv_head_mask: torch.Tensor     # (num_kv_heads,) bool


def group_heads_by_kv(
    num_q_heads: int = 28, num_kv_heads: int = 4,
) -> Dict[int, List[int]]:
    """Map each KV head index to the Q head indices it serves under GQA."""
    group_size = num_q_heads // num_kv_heads
    return {
        kv_idx: list(range(kv_idx * group_size, (kv_idx + 1) * group_size))
        for kv_idx in range(num_kv_heads)
    }


class HeadSelector:
    def __init__(self, num_q_heads: int, num_kv_heads: int):
        self.num_q_heads = num_q_heads
        self.num_kv_heads = num_kv_heads
        self.kv_groups = group_heads_by_kv(num_q_heads, num_kv_heads)

    def compute_importance(
        self,
        model: torch.nn.Module,
        layer_idx: int,
        calibration_input_ids: torch.Tensor,
    ) -> torch.Tensor:
        """Run a calibration forward pass through *model* and return per-head
        importance scores of shape ``(num_q_heads,)``.

        Importance is the mean L2 norm of each head's contribution to the
        attention output (averaged over batch and sequence positions).
        """
        attn_module = self._get_attention_layer(model, layer_idx)
        captured: dict = {}

        def _capture(module, inp, output):
            hidden = output[0] if isinstance(output, tuple) else output
            captured["output"] = hidden.detach()

        handle = attn_module.register_forward_hook(_capture)
        try:
            with torch.no_grad():
                model(input_ids=calibration_input_ids)
        finally:
            handle.remove()

        hidden = captured["output"]  # (bsz, seq_len, hidden_dim)
        bsz, seq_len, hidden_dim = hidden.shape
        head_dim = hidden_dim // self.num_q_heads

        reshaped = hidden.view(bsz, seq_len, self.num_q_heads, head_dim)
        per_head_norm = reshaped.norm(dim=-1)  # (bsz, seq_len, num_q_heads)
        importance = per_head_norm.mean(dim=(0, 1))  # (num_q_heads,)
        return importance

    def select(self, importance: torch.Tensor, keep_ratio: float) -> HeadMask:
        """Select Q heads to keep based on importance scores.

        Returns a ``HeadMask`` that also records which KV heads can be
        completely skipped (all their Q heads are masked).
        """
        num_keep = max(1, int(self.num_q_heads * keep_ratio))
        _, top_indices = importance.topk(num_keep, largest=True)
        active_q_heads = sorted(top_indices.tolist())

        q_head_mask = torch.zeros(self.num_q_heads, dtype=torch.bool)
        q_head_mask[active_q_heads] = True

        # A KV head is needed iff at least one of its Q heads is active
        active_q_set = set(active_q_heads)
        active_kv_heads: List[int] = []
        kv_head_mask = torch.zeros(self.num_kv_heads, dtype=torch.bool)

        for kv_idx, q_indices in self.kv_groups.items():
            if any(q in active_q_set for q in q_indices):
                active_kv_heads.append(kv_idx)
                kv_head_mask[kv_idx] = True

        return HeadMask(
            active_q_heads=active_q_heads,
            active_kv_heads=sorted(active_kv_heads),
            q_head_mask=q_head_mask,
            kv_head_mask=kv_head_mask,
        )

    # ------------------------------------------------------------------

    @staticmethod
    def _get_attention_layer(
        model: torch.nn.Module, layer_idx: int,
    ) -> torch.nn.Module:
        """Locate the attention sub-module at *layer_idx* by common HF naming."""
        for attr in ("model.layers", "transformer.h", "layers"):
            obj = model
            try:
                for part in attr.split("."):
                    obj = getattr(obj, part)
                layer = obj[layer_idx]
                for name in ("self_attn", "attention", "attn"):
                    if hasattr(layer, name):
                        return getattr(layer, name)
            except (AttributeError, IndexError, TypeError):
                continue
        raise ValueError(f"Cannot find attention layer at index {layer_idx}")
