# Interaction Index (II) calculator for measuring super/sub-additivity
# of compound sparsity (attention head pruning + KV cache eviction).
#
# II = quality(both_sparse) - quality(attn_only) - quality(kv_only) + quality(dense)
# where quality = -perplexity.  II > 0 means super-additive.

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import torch
import torch.nn.functional as F

from ..utils.metrics import compute_perplexity

try:
    from .phase_segmentation import Phase
except ImportError:
    Phase = None  # will be resolved when phase_segmentation is created


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class InteractionResult:
    ii_value: float
    ppl_dense: float
    ppl_attn_sparse: float
    ppl_kv_sparse: float
    ppl_both_sparse: float
    is_super_additive: bool
    phase_name: Optional[str] = None
    num_tokens: int = 0

    def summary(self) -> str:
        tag = "super-additive" if self.is_super_additive else "sub-additive"
        return (
            f"II={self.ii_value:+.4f} ({tag})  "
            f"dense={self.ppl_dense:.2f}  attn={self.ppl_attn_sparse:.2f}  "
            f"kv={self.ppl_kv_sparse:.2f}  both={self.ppl_both_sparse:.2f}"
        )


# ---------------------------------------------------------------------------
# Hook-based head masking (works with GQA / MHA / MQA)
# ---------------------------------------------------------------------------

class _HeadMaskHook:
    """Registers forward hooks that zero out masked attention heads."""

    def __init__(self, model: torch.nn.Module, head_mask: torch.Tensor):
        """
        head_mask: (num_layers, num_heads) float tensor, 1 = active, 0 = masked.
        """
        self.handles: list = []
        attn_layers = self._find_attention_layers(model)
        for layer_idx, attn_module in enumerate(attn_layers):
            if layer_idx >= head_mask.size(0):
                break
            mask = head_mask[layer_idx]  # (num_heads,)
            handle = attn_module.register_forward_hook(
                self._make_hook(mask)
            )
            self.handles.append(handle)

    @staticmethod
    def _find_attention_layers(model: torch.nn.Module) -> list:
        """Heuristic: find all self-attention sub-modules by common naming."""
        layers = []
        for name, module in model.named_modules():
            # Covers LlamaAttention, Qwen2Attention, MistralAttention, etc.
            if type(module).__name__.endswith("Attention") and "self" not in name.split(".")[-1].lower():
                # Avoid double-counting – only pick the leaf Attention modules
                children_attn = [
                    m for m in module.children()
                    if type(m).__name__.endswith("Attention")
                ]
                if not children_attn:
                    layers.append(module)
        # Fallback: search by attribute path (model.layers[i].self_attn)
        if not layers:
            for name, module in model.named_modules():
                if name.endswith(".self_attn") or name.endswith(".attention"):
                    layers.append(module)
        return layers

    @staticmethod
    def _make_hook(mask: torch.Tensor):
        """Return a hook that scales the attention output by head mask.

        For GQA, mask length == num_query_heads.  The hook reshapes the output
        projection's input by head dim, applies the mask, then collapses back.
        """
        def hook_fn(module, input, output):
            # output is typically a tuple; first element is hidden_states
            if isinstance(output, tuple):
                hidden = output[0]
            else:
                hidden = output

            num_heads = mask.size(0)
            bsz, seq_len, hidden_dim = hidden.shape
            head_dim = hidden_dim // num_heads

            reshaped = hidden.view(bsz, seq_len, num_heads, head_dim)
            head_mask_expanded = mask.to(hidden.device, hidden.dtype).view(1, 1, num_heads, 1)
            reshaped = reshaped * head_mask_expanded
            masked_hidden = reshaped.view(bsz, seq_len, hidden_dim)

            if isinstance(output, tuple):
                return (masked_hidden,) + output[1:]
            return masked_hidden

        return hook_fn

    def remove(self):
        for h in self.handles:
            h.remove()
        self.handles.clear()


# ---------------------------------------------------------------------------
# KV eviction via attention-mask manipulation
# ---------------------------------------------------------------------------

def _build_kv_attention_mask(
    attention_mask: torch.Tensor,
    kv_mask: torch.Tensor,
) -> torch.Tensor:
    """Merge the standard attention mask with per-layer KV eviction mask.

    Args:
        attention_mask: (batch, seq_len) – 1 = attend, 0 = ignore.
        kv_mask: (num_layers, seq_len) – 1 = keep, 0 = evict.

    Returns:
        (num_layers, batch, seq_len) mask suitable for broadcasting into
        the (batch, num_heads, q_len, kv_len) attention score tensor.
    """
    # Expand attention_mask: (1, batch, seq_len)
    base = attention_mask.unsqueeze(0).float()  # (1, B, S)
    kv = kv_mask.unsqueeze(1).float()            # (L, 1, S)
    combined = base * kv                          # (L, B, S)
    return combined


# ---------------------------------------------------------------------------
# Main calculator
# ---------------------------------------------------------------------------

class InteractionIndexCalculator:
    def __init__(
        self,
        model: torch.nn.Module,
        tokenizer,
        device: str = "cuda",
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.device = device
        self.model.eval()

    # ------------------------------------------------------------------
    # Forward with a specific sparsity configuration
    # ------------------------------------------------------------------

    @torch.no_grad()
    def forward_with_sparse_config(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        attn_head_mask: Optional[torch.Tensor] = None,
        kv_mask: Optional[torch.Tensor] = None,
        phase_token_indices: Optional[List[int]] = None,
    ) -> float:
        """Run a forward pass under a given sparsity config, return mean perplexity.

        Args:
            input_ids: (batch, seq_len).
            attention_mask: (batch, seq_len), 1=attend. Defaults to all-ones.
            attn_head_mask: (num_layers, num_heads), 1=active 0=masked.
            kv_mask: (num_layers, seq_len), 1=keep 0=evict.
            phase_token_indices: Positions at which to evaluate perplexity.
        """
        input_ids = input_ids.to(self.device)
        if attention_mask is None:
            attention_mask = torch.ones_like(input_ids)
        attention_mask = attention_mask.to(self.device)

        # --- KV eviction: fold into attention_mask ---
        model_attention_mask = attention_mask
        if kv_mask is not None:
            kv_mask = kv_mask.to(self.device)
            # For simplicity, apply the *union* (min across layers) to the flat
            # attention mask. Per-layer masking would need custom model code.
            flat_kv_mask = kv_mask.min(dim=0).values  # (seq_len,)
            model_attention_mask = attention_mask * flat_kv_mask.unsqueeze(0)

        # --- Head masking: install hooks ---
        hook_ctx: Optional[_HeadMaskHook] = None
        if attn_head_mask is not None:
            hook_ctx = _HeadMaskHook(self.model, attn_head_mask)

        try:
            outputs = self.model(
                input_ids=input_ids,
                attention_mask=model_attention_mask,
            )
        finally:
            if hook_ctx is not None:
                hook_ctx.remove()

        logits = outputs.logits[0]   # (seq_len, vocab)
        labels = input_ids[0]        # (seq_len,)

        return compute_perplexity(logits, labels, token_indices=phase_token_indices)

    # ------------------------------------------------------------------
    # Mask construction helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _select_heads_to_mask(
        num_layers: int,
        num_heads: int,
        ratio: float,
        importance: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """Build a (num_layers, num_heads) binary mask, masking `ratio` of heads.

        If importance is given (num_layers, num_heads), mask the least important.
        Otherwise, mask randomly.
        """
        mask = torch.ones(num_layers, num_heads)
        num_to_mask = max(1, int(num_heads * ratio))

        for layer in range(num_layers):
            if importance is not None:
                _, indices = importance[layer].topk(num_to_mask, largest=False)
            else:
                indices = torch.randperm(num_heads)[:num_to_mask]
            mask[layer, indices] = 0.0

        return mask

    @staticmethod
    def _select_kv_to_evict(
        num_layers: int,
        seq_len: int,
        ratio: float,
        importance: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """Build a (num_layers, seq_len) binary mask, evicting `ratio` of KV positions.

        If importance is given (num_layers, seq_len), evict the least important.
        Otherwise, evict randomly (never evict first token / BOS).
        """
        mask = torch.ones(num_layers, seq_len)
        num_to_evict = max(1, int(seq_len * ratio))
        # Never evict position 0 (BOS)
        num_to_evict = min(num_to_evict, seq_len - 1)

        for layer in range(num_layers):
            if importance is not None:
                candidates = importance[layer, 1:]  # skip BOS
                _, indices = candidates.topk(num_to_evict, largest=False)
                indices = indices + 1  # shift back
            else:
                indices = torch.randperm(seq_len - 1)[:num_to_evict] + 1
            mask[layer, indices] = 0.0

        return mask

    # ------------------------------------------------------------------
    # Model config introspection
    # ------------------------------------------------------------------

    def _get_model_dims(self) -> Tuple[int, int]:
        """Return (num_layers, num_attention_heads) from model config."""
        config = self.model.config
        num_layers = getattr(config, "num_hidden_layers", None)
        num_heads = getattr(config, "num_attention_heads", None)
        if num_layers is None or num_heads is None:
            raise ValueError(
                "Cannot infer num_hidden_layers / num_attention_heads from model config"
            )
        return num_layers, num_heads

    # ------------------------------------------------------------------
    # Core: compute Interaction Index
    # ------------------------------------------------------------------

    def compute_interaction_index(
        self,
        input_ids: torch.Tensor,
        attn_sparsity_ratio: float = 0.3,
        kv_eviction_ratio: float = 0.3,
        phase_token_indices: Optional[List[int]] = None,
        head_importance: Optional[torch.Tensor] = None,
        kv_importance: Optional[torch.Tensor] = None,
    ) -> InteractionResult:
        """Compute the Interaction Index for a single input.

        II = -ppl(both) + ppl(attn_only) + ppl(kv_only) - ppl(dense)

        II > 0 means super-additive: combining both sparsity axes hurts
        less than the sum of individual degradations.
        """
        num_layers, num_heads = self._get_model_dims()
        seq_len = input_ids.size(-1)

        attn_head_mask = self._select_heads_to_mask(
            num_layers, num_heads, attn_sparsity_ratio, head_importance
        )
        kv_mask = self._select_kv_to_evict(
            num_layers, seq_len, kv_eviction_ratio, kv_importance
        )

        # 1. Dense
        ppl_dense = self.forward_with_sparse_config(
            input_ids, phase_token_indices=phase_token_indices,
        )
        # 2. Attention-only sparse
        ppl_attn = self.forward_with_sparse_config(
            input_ids, attn_head_mask=attn_head_mask,
            phase_token_indices=phase_token_indices,
        )
        # 3. KV-only sparse
        ppl_kv = self.forward_with_sparse_config(
            input_ids, kv_mask=kv_mask,
            phase_token_indices=phase_token_indices,
        )
        # 4. Both sparse
        ppl_both = self.forward_with_sparse_config(
            input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,
            phase_token_indices=phase_token_indices,
        )

        # II = quality(both) - quality(attn) - quality(kv) + quality(dense)
        # quality = -ppl, so:
        ii = -ppl_both + ppl_attn + ppl_kv - ppl_dense

        num_tokens = len(phase_token_indices) if phase_token_indices else seq_len

        return InteractionResult(
            ii_value=ii,
            ppl_dense=ppl_dense,
            ppl_attn_sparse=ppl_attn,
            ppl_kv_sparse=ppl_kv,
            ppl_both_sparse=ppl_both,
            is_super_additive=ii > 0,
            num_tokens=num_tokens,
        )

    # ------------------------------------------------------------------
    # Per-phase Interaction Index
    # ------------------------------------------------------------------

    def compute_per_phase_ii(
        self,
        input_ids: torch.Tensor,
        phases: List,
        attn_sparsity_ratio: float = 0.3,
        kv_eviction_ratio: float = 0.3,
    ) -> Dict[str, InteractionResult]:
        """Compute II separately for each phase (reasoning / execution / transition).

        Args:
            phases: List of Phase objects from phase_segmentation.  Each Phase must
                    have .name (str) and .token_indices (List[int]) attributes.

        Returns:
            Dict mapping phase name to its InteractionResult.
        """
        results: Dict[str, InteractionResult] = {}

        for phase in phases:
            result = self.compute_interaction_index(
                input_ids,
                attn_sparsity_ratio=attn_sparsity_ratio,
                kv_eviction_ratio=kv_eviction_ratio,
                phase_token_indices=phase.token_indices,
            )
            result.phase_name = phase.name
            results[phase.name] = result

        return results
