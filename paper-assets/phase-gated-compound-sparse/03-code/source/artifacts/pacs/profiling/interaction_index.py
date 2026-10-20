# Interaction Index (II) calculator for measuring super/sub-additivity
# of compound sparsity (attention head pruning + KV cache eviction).
#
# II = R_both - R_attn - R_kv + 1
# where R_x = ppl_x / ppl_dense (relative degradation ratio).
# II > 0 → super-additive degradation (compound sparsity hurts more than sum of parts)
# II < 0 → sub-additive degradation
# II = 0 → independent

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import numpy as np

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
    r_attn: float          # ppl_attn / ppl_dense
    r_kv: float            # ppl_kv / ppl_dense
    r_both: float          # ppl_both / ppl_dense
    is_super_additive: bool  # II > 0 → compound sparsity degrades more than sum of parts
    sparsity_level: float = 0.0
    phase_name: Optional[str] = None
    num_tokens: int = 0

    def summary(self) -> str:
        tag = "super-additive" if self.is_super_additive else "sub-additive"
        return (
            f"II={self.ii_value:+.4f} ({tag})  "
            f"R_attn={self.r_attn:.4f}  R_kv={self.r_kv:.4f}  R_both={self.r_both:.4f}  "
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
            head_mask_expanded = mask.to(hidden.device).view(1, 1, num_heads, 1)
            # torch.where avoids inf*0=NaN (IEEE 754) when KV eviction causes extreme outputs
            reshaped = torch.where(
                head_mask_expanded.bool(),
                reshaped,
                torch.zeros_like(reshaped),
            )
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
    """Merge the standard attention mask with KV eviction mask.

    Args:
        attention_mask: (batch, seq_len) – 1 = attend, 0 = ignore.
        kv_mask: (seq_len,) or (num_layers, seq_len) – 1 = keep, 0 = evict.

    Returns:
        (batch, seq_len) merged mask.
    """
    if kv_mask.dim() == 2:
        kv_mask = kv_mask.min(dim=0).values
    return attention_mask * kv_mask.unsqueeze(0).float()


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
            if kv_mask.dim() == 2:
                flat_kv_mask = kv_mask.min(dim=0).values
            else:
                flat_kv_mask = kv_mask
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
        seq_len: int,
        ratio: float,
        importance: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """Build a (seq_len,) binary mask shared across all layers, evicting `ratio` of KV positions.

        If importance is given ((seq_len,) or (num_layers, seq_len)), evict the least important.
        Otherwise, evict randomly. Position 0 (BOS) is never evicted.
        """
        mask = torch.ones(seq_len)
        num_to_evict = max(1, int(seq_len * ratio))
        num_to_evict = min(num_to_evict, seq_len - 1)

        if importance is not None:
            if importance.dim() == 2:
                importance = importance.mean(dim=0)
            candidates = importance[1:]
            _, indices = candidates.topk(num_to_evict, largest=False)
            indices = indices + 1
        else:
            indices = torch.randperm(seq_len - 1)[:num_to_evict] + 1
        mask[indices] = 0.0

        return mask

    # ------------------------------------------------------------------
    # Model config introspection
    # ------------------------------------------------------------------

    @torch.no_grad()
    def compute_dense_ce_losses(self, input_ids: torch.Tensor) -> torch.Tensor:
        """Dense forward pass returning per-token CE losses (shifted by 1)."""
        input_ids = input_ids.to(self.device)
        attention_mask = torch.ones_like(input_ids).to(self.device)
        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits[0]
        labels = input_ids[0]
        shift_logits = logits[:-1]
        shift_labels = labels[1:]
        return F.cross_entropy(shift_logits, shift_labels, reduction="none")

    @torch.no_grad()
    def compute_dense_forward_with_importance(
        self, input_ids: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """Dense forward returning (ce_losses, head_importance, kv_importance).

        head_importance: (num_layers, num_heads) — attention weight Frobenius norm.
        kv_importance: (seq_len,) — cumulative attention received per position.
        """
        input_ids = input_ids.to(self.device)
        attention_mask = torch.ones_like(input_ids).to(self.device)
        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_attentions=True,
        )
        logits = outputs.logits[0]
        labels = input_ids[0]
        ce_losses = F.cross_entropy(logits[:-1], labels[1:], reduction="none")

        attentions = outputs.attentions
        num_layers = len(attentions)
        num_heads = attentions[0].shape[1]
        seq_len = input_ids.shape[1]

        head_importance = torch.zeros(num_layers, num_heads)
        kv_importance = torch.zeros(seq_len)
        for l in range(num_layers):
            attn_f = attentions[l][0].float()
            head_importance[l] = attn_f.norm(dim=(-2, -1)).cpu()
            kv_importance += attn_f.sum(dim=(0, 1)).cpu()
            del attn_f

        return ce_losses, head_importance, kv_importance

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
        sparsity_level: float = 0.3,
        phase_token_indices: Optional[List[int]] = None,
        head_importance: Optional[torch.Tensor] = None,
        kv_importance: Optional[torch.Tensor] = None,
    ) -> InteractionResult:
        """Compute the Interaction Index for a single input.

        II = R_both - R_attn - R_kv + 1, where R_x = ppl_x / ppl_dense.
        II > 0 → super-additive degradation (compound sparsity is worse than
        the sum of individual degradations).
        """
        num_layers, num_heads = self._get_model_dims()
        seq_len = input_ids.size(-1)

        attn_head_mask = self._select_heads_to_mask(
            num_layers, num_heads, sparsity_level, head_importance
        )
        kv_mask = self._select_kv_to_evict(
            seq_len, sparsity_level, kv_importance
        )

        ppl_dense = self.forward_with_sparse_config(
            input_ids, phase_token_indices=phase_token_indices,
        )
        ppl_attn = self.forward_with_sparse_config(
            input_ids, attn_head_mask=attn_head_mask,
            phase_token_indices=phase_token_indices,
        )
        ppl_kv = self.forward_with_sparse_config(
            input_ids, kv_mask=kv_mask,
            phase_token_indices=phase_token_indices,
        )
        ppl_both = self.forward_with_sparse_config(
            input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,
            phase_token_indices=phase_token_indices,
        )

        r_attn = ppl_attn / ppl_dense if ppl_dense > 0 else float("nan")
        r_kv = ppl_kv / ppl_dense if ppl_dense > 0 else float("nan")
        r_both = ppl_both / ppl_dense if ppl_dense > 0 else float("nan")
        ii = r_both - r_attn - r_kv + 1

        num_tokens = len(phase_token_indices) if phase_token_indices else seq_len

        return InteractionResult(
            ii_value=ii,
            ppl_dense=ppl_dense,
            ppl_attn_sparse=ppl_attn,
            ppl_kv_sparse=ppl_kv,
            ppl_both_sparse=ppl_both,
            r_attn=r_attn,
            r_kv=r_kv,
            r_both=r_both,
            is_super_additive=ii > 0,
            sparsity_level=sparsity_level,
            num_tokens=num_tokens,
        )

    # ------------------------------------------------------------------
    # Per-phase Interaction Index
    # ------------------------------------------------------------------

    def compute_per_phase_ii(
        self,
        input_ids: torch.Tensor,
        phases: List,
        sparsity_level: float = 0.3,
    ) -> Dict[str, InteractionResult]:
        """Compute II separately for each phase (reasoning / execution / transition).

        Args:
            phases: List of Phase objects with .name and .token_indices attributes.
            sparsity_level: Fraction of heads to mask / KV positions to evict.

        Returns:
            Dict mapping phase name to its InteractionResult.
        """
        results: Dict[str, InteractionResult] = {}

        for phase in phases:
            result = self.compute_interaction_index(
                input_ids,
                sparsity_level=sparsity_level,
                phase_token_indices=phase.token_indices,
            )
            result.phase_name = phase.name
            results[phase.name] = result

        return results


# ---------------------------------------------------------------------------
# Bootstrap CI for Interaction Index
# ---------------------------------------------------------------------------

def bootstrap_interaction_index(
    ii_samples: List[float],
    n_resamples: int = 1000,
    ci_level: float = 0.95,
    seed: int = 42,
) -> Tuple[float, float, float]:
    """Bootstrap confidence interval for the mean II.

    Args:
        ii_samples: Per-problem II values for a given (phase, level).
        n_resamples: Number of bootstrap resamples.
        ci_level: Confidence level (default 0.95 → 95% CI).
        seed: Random seed for reproducibility.

    Returns:
        (mean, ci_low, ci_high) using percentile method.
    """
    rng = np.random.RandomState(seed)
    samples = np.array(ii_samples)
    n = len(samples)
    boot_means = np.empty(n_resamples)
    for i in range(n_resamples):
        idx = rng.randint(0, n, size=n)
        boot_means[i] = samples[idx].mean()
    alpha = 1.0 - ci_level
    ci_low = float(np.percentile(boot_means, 100 * alpha / 2))
    ci_high = float(np.percentile(boot_means, 100 * (1 - alpha / 2)))
    return float(samples.mean()), ci_low, ci_high
