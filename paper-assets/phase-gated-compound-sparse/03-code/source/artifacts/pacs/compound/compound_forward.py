# Compound sparse forward: head masking + KV eviction in a single pass.
#
# Head masking: forward hooks on attention output, zero out masked heads
# by reshaping to (bsz, seq, num_q_heads, head_dim) and scaling.
#
# KV eviction: fold the KV position mask into the attention_mask so
# evicted positions are invisible to all queries.
#
# Designed for attn_implementation="eager" — needs access to attention
# weights for importance computation. Triton version will come later.
#
# Key deps: torch, pacs.compound.{head_selector, kv_evictor}, pacs.utils.metrics

from __future__ import annotations

from typing import List, Optional

import torch

from .head_selector import HeadMask
from .kv_evictor import KVMask
from ..utils.metrics import compute_perplexity


class CompoundSparseForward:
    """Execute a forward pass with simultaneous head masking and KV eviction."""

    def __init__(self, model: torch.nn.Module, device: str = "cuda"):
        self.model = model
        self.device = device

    @torch.no_grad()
    def forward(
        self,
        input_ids: torch.Tensor,
        head_mask: Optional[HeadMask] = None,
        kv_mask: Optional[KVMask] = None,
        attention_mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """Run forward with compound sparsity applied.

        Returns:
            logits ``(batch, seq_len, vocab_size)``.  Evicted KV positions
            still produce logits (attention just cannot attend to them);
            downstream PPL computation should filter by ``token_indices``.
        """
        input_ids = input_ids.to(self.device)
        if attention_mask is None:
            attention_mask = torch.ones_like(input_ids)
        attention_mask = attention_mask.to(self.device)

        # --- KV eviction: fold position mask into attention_mask ---
        if kv_mask is not None:
            kv_float = kv_mask.position_mask.to(self.device).float()
            attention_mask = attention_mask * kv_float.unsqueeze(0)

        # --- Head masking: register output hooks on every attention layer ---
        handles: list = []
        if head_mask is not None:
            float_mask = head_mask.q_head_mask.float().to(self.device)
            for attn_module in self._find_attention_layers():
                handle = attn_module.register_forward_hook(
                    self._make_head_mask_hook(float_mask)
                )
                handles.append(handle)

        try:
            outputs = self.model(
                input_ids=input_ids,
                attention_mask=attention_mask,
            )
        finally:
            for h in handles:
                h.remove()

        return outputs.logits

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _find_attention_layers(self) -> list:
        """Locate all leaf attention modules in the model."""
        layers = []
        for name, module in self.model.named_modules():
            if type(module).__name__.endswith("Attention"):
                children_attn = [
                    m for m in module.children()
                    if type(m).__name__.endswith("Attention")
                ]
                if not children_attn:
                    layers.append(module)
        if not layers:
            for name, module in self.model.named_modules():
                if name.endswith(".self_attn") or name.endswith(".attention"):
                    layers.append(module)
        return layers

    @staticmethod
    def _make_head_mask_hook(mask: torch.Tensor):
        """Hook that scales attention output by a per-Q-head binary mask.

        Reshapes the hidden-state output from ``(bsz, seq, hidden)`` to
        ``(bsz, seq, num_q_heads, head_dim)``, multiplies element-wise,
        then collapses back.  Works with GQA because the output projection
        has already merged KV-group information into per-Q-head slots.
        """
        def hook_fn(module, inp, output):
            if isinstance(output, tuple):
                hidden = output[0]
            else:
                hidden = output

            num_heads = mask.size(0)
            bsz, seq_len, hidden_dim = hidden.shape
            head_dim = hidden_dim // num_heads

            reshaped = hidden.view(bsz, seq_len, num_heads, head_dim)
            mask_expanded = mask.to(hidden.device, hidden.dtype).view(1, 1, num_heads, 1)
            masked_hidden = (reshaped * mask_expanded).view(bsz, seq_len, hidden_dim)

            if isinstance(output, tuple):
                return (masked_hidden,) + output[1:]
            return masked_hidden

        return hook_fn


def compute_compound_ppl(
    model: torch.nn.Module,
    tokenizer,
    input_ids: torch.Tensor,
    head_mask: Optional[HeadMask] = None,
    kv_mask: Optional[KVMask] = None,
    token_indices: Optional[List[int]] = None,
    device: str = "cuda",
) -> float:
    """Execute compound forward and compute perplexity on specified tokens.

    Args:
        model: HF causal LM.
        tokenizer: not used directly but kept for API consistency.
        input_ids: ``(1, seq_len)`` token ids.
        head_mask: which Q/KV heads to keep.
        kv_mask: which KV positions to keep.
        token_indices: label positions to evaluate; ``None`` = all.
        device: target device.

    Returns:
        Scalar perplexity.
    """
    csf = CompoundSparseForward(model, device=device)
    logits = csf.forward(input_ids, head_mask=head_mask, kv_mask=kv_mask)
    return compute_perplexity(logits[0], input_ids[0], token_indices=token_indices)
