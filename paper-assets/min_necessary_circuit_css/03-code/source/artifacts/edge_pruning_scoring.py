"""Edge Pruning v2 with L0 regularization for HuggingFace models.

v2 fixes two critical bugs from v1:
  1. MLP edge masks are now applied in forward via mlp pre-hook
     (v1 had mask params but no forward-pass hook for MLP).
  2. Q/K/V edge masks are kept independent per-head/KV-group
     (v1 averaged across all Q/K/V destinations into a single scalar).

Hook strategy (v2): 4 submodule pre-hooks per layer
  - self_attn.q_proj: per-head Q edge masks
  - self_attn.k_proj: per-KV-group K edge masks (GQA shared)
  - self_attn.v_proj: per-KV-group V edge masks (GQA shared)
  - mlp: per-source MLP edge masks
Plus capture hooks: embed_tokens, self_attn.o_proj (per-head), mlp (output).

Canonical node format:
  input, logits, a{L}.h{H}[.q|.k|.v], m{L}

Canonical edge format: "{src}->{dst}" (no spaces)

References:
  - Louizos et al. "Learning Sparse Neural Networks through L0 Regularization" (2018)
  - Bayazit et al. "Discovering Knowledge-Critical Subnetworks" (2023)
"""

from __future__ import annotations

import math
from typing import Dict, List, Tuple, Callable, Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


# ---------------------------------------------------------------------------
# Hard Concrete Distribution
# ---------------------------------------------------------------------------

class HardConcrete(nn.Module):
    """Hard Concrete distribution for L0 mask parameterization.

    Parameterized by log_alpha (location). During training, samples from a
    stretched Binary Concrete and clamps to [0, 1], yielding exact zeros/ones.
    """

    BETA = 2.0 / 3.0
    GAMMA = -0.1
    ZETA = 1.1
    EPS = 1e-8

    def __init__(self, n_masks: int, init_mean: float = 0.5):
        super().__init__()
        init_val = math.log(init_mean / (1.0 - init_mean + self.EPS))
        self.log_alpha = nn.Parameter(torch.full((n_masks,), init_val))

    def forward(self, training: bool = True) -> torch.Tensor:
        if training:
            u = torch.zeros_like(self.log_alpha).uniform_(self.EPS, 1.0 - self.EPS)
            s = torch.sigmoid((torch.log(u / (1.0 - u)) + self.log_alpha) / self.BETA)
        else:
            s = torch.sigmoid(self.log_alpha)
        s_bar = s * (self.ZETA - self.GAMMA) + self.GAMMA
        return s_bar.clamp(0.0, 1.0)

    def l0_penalty(self) -> torch.Tensor:
        """Expected L0 norm: sum of P(z != 0) for each mask."""
        return torch.sigmoid(
            self.log_alpha - self.BETA * math.log(-self.GAMMA / self.ZETA)
        ).sum()

    def expected_masks(self) -> torch.Tensor:
        """Deterministic mask expectations (for final scoring)."""
        return self.forward(training=False)


# ---------------------------------------------------------------------------
# Architecture detection (Llama-like HF models)
# ---------------------------------------------------------------------------

_LLAMA_LIKE = frozenset({
    "llama", "qwen2", "gemma", "gemma2", "mistral", "phi3", "phi",
})


def _get_arch_info(model) -> dict:
    cfg = model.config
    model_type = getattr(cfg, "model_type", "")
    if model_type not in _LLAMA_LIKE:
        raise ValueError(
            f"Edge Pruning L0 currently supports Llama-like architectures, "
            f"got model_type={model_type!r}"
        )
    n_heads = cfg.num_attention_heads
    n_kv_heads = getattr(cfg, "num_key_value_heads", n_heads)
    d_model = cfg.hidden_size
    return dict(
        n_layers=cfg.num_hidden_layers,
        n_heads=n_heads,
        n_kv_heads=n_kv_heads,
        heads_per_kv_group=n_heads // n_kv_heads,
        d_model=d_model,
        head_dim=d_model // n_heads,
    )


# ---------------------------------------------------------------------------
# Edge Topology: enumerate all edges and build mask index mapping
# ---------------------------------------------------------------------------

def _src_nodes_before_layer(
    layer: int, n_heads: int, include_attn_same_layer: bool = False,
):
    """Yield source node names whose output feeds into a given layer."""
    yield "input"
    for l in range(layer):
        for h in range(n_heads):
            yield f"a{l}.h{h}"
        yield f"m{l}"
    if include_attn_same_layer:
        for h in range(n_heads):
            yield f"a{layer}.h{h}"


def _build_edge_topology(
    n_layers: int, n_heads: int, n_kv_heads: int, heads_per_kv_group: int,
) -> Tuple[List[str], Dict[str, int], int]:
    """Build the full edge set and map each edge to its mask parameter index.

    For GQA models, K/V edges targeting the same KV group share a mask.
    Q edges always have independent masks.

    Returns:
        edge_names: list of canonical edge names
        edge_to_mask_idx: edge_name -> index into mask parameter vector
        n_masks: total number of independent mask parameters
    """
    edge_names: List[str] = []
    edge_to_mask_idx: Dict[str, int] = {}
    mask_idx = 0

    for L in range(n_layers):
        srcs_attn = list(_src_nodes_before_layer(L, n_heads, False))
        for src in srcs_attn:
            for H in range(n_heads):
                q_edge = f"{src}->a{L}.h{H}.q"
                edge_names.append(q_edge)
                edge_to_mask_idx[q_edge] = mask_idx
                mask_idx += 1

            for kv_group in range(n_kv_heads):
                k_mask_idx = mask_idx
                mask_idx += 1
                for h_in_group in range(heads_per_kv_group):
                    H = kv_group * heads_per_kv_group + h_in_group
                    k_edge = f"{src}->a{L}.h{H}.k"
                    edge_names.append(k_edge)
                    edge_to_mask_idx[k_edge] = k_mask_idx

            for kv_group in range(n_kv_heads):
                v_mask_idx = mask_idx
                mask_idx += 1
                for h_in_group in range(heads_per_kv_group):
                    H = kv_group * heads_per_kv_group + h_in_group
                    v_edge = f"{src}->a{L}.h{H}.v"
                    edge_names.append(v_edge)
                    edge_to_mask_idx[v_edge] = v_mask_idx

        srcs_mlp = list(_src_nodes_before_layer(L, n_heads, True))
        for src in srcs_mlp:
            mlp_edge = f"{src}->m{L}"
            edge_names.append(mlp_edge)
            edge_to_mask_idx[mlp_edge] = mask_idx
            mask_idx += 1

    return edge_names, edge_to_mask_idx, mask_idx


# ---------------------------------------------------------------------------
# Precomputed hook mask indices for vectorized application
# ---------------------------------------------------------------------------

def _build_hook_mask_indices(
    n_layers: int,
    n_heads: int,
    edge_to_mask_idx: Dict[str, int],
    device: torch.device,
) -> Tuple[
    List[Dict[str, torch.Tensor]],
    List[Dict[str, torch.Tensor]],
    List[Dict[str, torch.Tensor]],
    List[Dict[str, int]],
]:
    """Precompute per-hook mask index tensors.

    Returns (q_indices, k_indices, v_indices, mlp_indices) where:
      q/k/v_indices[L] = {src_name: LongTensor[n_heads]}
        GQA sharing is implicit: heads in the same KV group get identical index values.
      mlp_indices[L] = {src_name: int}
    """
    q_all: List[Dict[str, torch.Tensor]] = []
    k_all: List[Dict[str, torch.Tensor]] = []
    v_all: List[Dict[str, torch.Tensor]] = []
    mlp_all: List[Dict[str, int]] = []

    for L in range(n_layers):
        srcs_attn = list(_src_nodes_before_layer(L, n_heads, False))
        srcs_mlp = list(_src_nodes_before_layer(L, n_heads, True))

        qi: Dict[str, torch.Tensor] = {}
        ki: Dict[str, torch.Tensor] = {}
        vi: Dict[str, torch.Tensor] = {}
        for src in srcs_attn:
            qi[src] = torch.tensor(
                [edge_to_mask_idx[f"{src}->a{L}.h{h}.q"] for h in range(n_heads)],
                dtype=torch.long, device=device,
            )
            ki[src] = torch.tensor(
                [edge_to_mask_idx[f"{src}->a{L}.h{h}.k"] for h in range(n_heads)],
                dtype=torch.long, device=device,
            )
            vi[src] = torch.tensor(
                [edge_to_mask_idx[f"{src}->a{L}.h{h}.v"] for h in range(n_heads)],
                dtype=torch.long, device=device,
            )

        mi: Dict[str, int] = {}
        for src in srcs_mlp:
            mi[src] = edge_to_mask_idx[f"{src}->m{L}"]

        q_all.append(qi)
        k_all.append(ki)
        v_all.append(vi)
        mlp_all.append(mi)

    return q_all, k_all, v_all, mlp_all


# ---------------------------------------------------------------------------
# Per-head decomposition through the output projection
# ---------------------------------------------------------------------------

def _decompose_attn_output(
    concat_heads: torch.Tensor,
    o_proj: nn.Linear,
    n_heads: int,
    head_dim: int,
) -> Dict[int, torch.Tensor]:
    """Split concatenated head output and project each head through o_proj."""
    W = o_proj.weight  # [d_model, d_model]
    heads = {}
    for h in range(n_heads):
        h_slice = concat_heads[:, :, h * head_dim:(h + 1) * head_dim]
        W_h = W[:, h * head_dim:(h + 1) * head_dim]
        heads[h] = h_slice @ W_h.T
    return heads


# ---------------------------------------------------------------------------
# Masked input construction for submodule hooks
# ---------------------------------------------------------------------------

def _build_masked_input_qkv(
    src_cache: Dict[str, torch.Tensor],
    masks: torch.Tensor,
    idx_dict: Dict[str, torch.Tensor],
    n_heads: int,
    head_dim: int,
    layernorm: nn.Module,
    ref: torch.Tensor,
) -> torch.Tensor:
    """Construct masked + layernormed input for a Q/K/V projection.

    Applies per-head mask values to head_dim-sized slices of each source
    activation. GQA sharing is transparent: idx_dict encodes shared
    indices for heads within the same KV group.
    """
    B, S, D = ref.shape
    x = torch.zeros(B, S, D, device=ref.device, dtype=ref.dtype)
    for src_name, mask_idx_t in idx_dict.items():
        src = src_cache.get(src_name)
        if src is None:
            continue
        z = masks[mask_idx_t].view(1, 1, n_heads, 1)
        x = x + (src.view(B, S, n_heads, head_dim) * z).view(B, S, D)
    return layernorm(x)


def _build_masked_input_mlp(
    src_cache: Dict[str, torch.Tensor],
    masks: torch.Tensor,
    idx_dict: Dict[str, int],
    post_ln: nn.Module,
    ref: torch.Tensor,
) -> torch.Tensor:
    """Construct masked + post-layernormed input for an MLP module."""
    x = torch.zeros_like(ref)
    for src_name, mask_idx in idx_dict.items():
        src = src_cache.get(src_name)
        if src is None:
            continue
        x = x + src * masks[mask_idx]
    return post_ln(x)


# ---------------------------------------------------------------------------
# Hook-based masked forward pass (v2: submodule-level hooks)
# ---------------------------------------------------------------------------

def _masked_forward(
    model,
    input_ids: torch.Tensor,
    masks: torch.Tensor,
    arch_info: dict,
    hook_indices: Tuple,
) -> torch.Tensor:
    """Forward pass with per-destination edge masks via submodule hooks.

    Registers 7 hooks per layer:
      Pre-hooks (masking): q_proj, k_proj, v_proj, mlp
      Capture hooks: o_proj (per-head attn output), mlp (output)
    Plus 1 embed capture hook.
    """
    n_heads = arch_info["n_heads"]
    head_dim = arch_info["head_dim"]
    n_layers = arch_info["n_layers"]
    layers = model.model.layers

    q_idx, k_idx, v_idx, mlp_idx = hook_indices
    src_cache: Dict[str, torch.Tensor] = {}
    hooks: list = []

    def _embed_hook(mod, inp, out):
        src_cache["input"] = out
    hooks.append(model.model.embed_tokens.register_forward_hook(_embed_hook))

    for L in range(n_layers):
        layer = layers[L]
        ln1 = layer.input_layernorm
        ln2 = layer.post_attention_layernorm

        # --- Q/K/V projection pre-hooks: replace input with masked residual ---

        def _q_hook(mod, args, *, _qi=q_idx[L], _ln=ln1):
            return (_build_masked_input_qkv(
                src_cache, masks, _qi, n_heads, head_dim, _ln, args[0],
            ),) + args[1:]

        def _k_hook(mod, args, *, _ki=k_idx[L], _ln=ln1):
            return (_build_masked_input_qkv(
                src_cache, masks, _ki, n_heads, head_dim, _ln, args[0],
            ),) + args[1:]

        def _v_hook(mod, args, *, _vi=v_idx[L], _ln=ln1):
            return (_build_masked_input_qkv(
                src_cache, masks, _vi, n_heads, head_dim, _ln, args[0],
            ),) + args[1:]

        hooks.append(layer.self_attn.q_proj.register_forward_pre_hook(_q_hook))
        hooks.append(layer.self_attn.k_proj.register_forward_pre_hook(_k_hook))
        hooks.append(layer.self_attn.v_proj.register_forward_pre_hook(_v_hook))

        # --- Attention output capture: per-head decomposition through o_proj ---

        def _oproj_hook(mod, inp, out, *, _L=L):
            per_head = _decompose_attn_output(inp[0], mod, n_heads, head_dim)
            for h, h_out in per_head.items():
                src_cache[f"a{_L}.h{h}"] = h_out
        hooks.append(layer.self_attn.o_proj.register_forward_hook(_oproj_hook))

        # --- MLP pre-hook: replace input with masked residual ---

        def _mlp_pre_hook(mod, args, *, _mi=mlp_idx[L], _ln=ln2):
            return (_build_masked_input_mlp(
                src_cache, masks, _mi, _ln, args[0],
            ),) + args[1:]
        hooks.append(layer.mlp.register_forward_pre_hook(_mlp_pre_hook))

        # --- MLP output capture ---

        def _mlp_out_hook(mod, inp, out, *, _L=L):
            src_cache[f"m{_L}"] = out if isinstance(out, torch.Tensor) else out[0]
        hooks.append(layer.mlp.register_forward_hook(_mlp_out_hook))

    try:
        return model(input_ids).logits
    finally:
        for h in hooks:
            h.remove()


# ---------------------------------------------------------------------------
# Faithfulness loss
# ---------------------------------------------------------------------------

def _faithfulness_loss(
    masked_logits: torch.Tensor,
    clean_logits: torch.Tensor,
    target_ids: Optional[torch.Tensor],
) -> torch.Tensor:
    """KL divergence between clean and masked model output distributions."""
    if target_ids is not None:
        batch_size = masked_logits.size(0)
        idx = target_ids.view(batch_size)
        masked_logits = masked_logits[torch.arange(batch_size), idx]
        clean_logits = clean_logits[torch.arange(batch_size), idx]

    log_p = F.log_softmax(masked_logits, dim=-1)
    q = F.softmax(clean_logits, dim=-1)
    return F.kl_div(log_p, q, reduction="batchmean")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def compute_edge_pruning_scores(
    model,
    clean_inputs,
    corrupt_inputs,
    metric_fn: Callable,
    target_ids=None,
    n_epochs: int = 100,
    lambda_l0: float = 1e-3,
    lr: float = 0.1,
    device: str = "cuda",
) -> Dict[str, float]:
    """Compute Edge Pruning L0 edge scores.

    Returns dict of canonical_edge_name -> score (mask expectation).

    Args:
        model: HuggingFace CausalLM (Llama-like: Qwen2, Llama, Mistral, etc.)
        clean_inputs: dict with 'input_ids' [batch, seq_len]
        corrupt_inputs: dict with 'input_ids' [batch, seq_len]
        metric_fn: faithfulness metric (kept for interface parity; KL used internally)
        target_ids: [batch] token positions for evaluation (None = all positions)
        n_epochs: optimization epochs
        lambda_l0: L0 sparsity penalty weight
        lr: learning rate for mask parameters
        device: target device
    """
    arch_info = _get_arch_info(model)
    n_layers = arch_info["n_layers"]
    n_heads = arch_info["n_heads"]
    n_kv_heads = arch_info["n_kv_heads"]
    heads_per_kv_group = arch_info["heads_per_kv_group"]

    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology(
        n_layers, n_heads, n_kv_heads, heads_per_kv_group,
    )
    hook_indices = _build_hook_mask_indices(
        n_layers, n_heads, edge_to_mask_idx, device,
    )

    hard_concrete = HardConcrete(n_masks, init_mean=0.5).to(device)
    optimizer = torch.optim.Adam(hard_concrete.parameters(), lr=lr)

    # Prepare inputs
    if isinstance(clean_inputs, dict):
        clean_ids = clean_inputs["input_ids"]
        if not isinstance(clean_ids, torch.Tensor):
            clean_ids = torch.tensor(clean_ids)
    else:
        clean_ids = clean_inputs
    clean_ids = clean_ids.to(device)

    if isinstance(corrupt_inputs, dict):
        corrupt_ids = corrupt_inputs["input_ids"]
        if not isinstance(corrupt_ids, torch.Tensor):
            corrupt_ids = torch.tensor(corrupt_ids)
    else:
        corrupt_ids = corrupt_inputs
    corrupt_ids = corrupt_ids.to(device)

    if target_ids is not None:
        if not isinstance(target_ids, torch.Tensor):
            target_ids = torch.tensor(target_ids)
        target_ids = target_ids.to(device)

    # Freeze model — only mask params are optimized
    model.eval()
    model.requires_grad_(False)

    with torch.no_grad():
        clean_logits = model(clean_ids).logits.detach()

    # Optimization loop
    for epoch in range(n_epochs):
        optimizer.zero_grad()
        masks = hard_concrete(training=True)
        masked_logits = _masked_forward(
            model, clean_ids, masks, arch_info, hook_indices,
        )
        faith_loss = _faithfulness_loss(masked_logits, clean_logits, target_ids)
        l0_loss = hard_concrete.l0_penalty()
        loss = faith_loss + lambda_l0 * l0_loss
        loss.backward()
        optimizer.step()

    # Extract final scores
    with torch.no_grad():
        final_masks = hard_concrete.expected_masks()

    scores: Dict[str, float] = {}
    for edge_name, mask_idx in edge_to_mask_idx.items():
        scores[edge_name] = final_masks[mask_idx].item()

    return scores


# ---------------------------------------------------------------------------
# Utility: edge count estimation
# ---------------------------------------------------------------------------

def estimate_edge_counts(
    n_layers: int, n_heads: int, n_kv_heads: int,
) -> Dict[str, int]:
    """Estimate edge and mask parameter counts for a given architecture."""
    heads_per_kv = n_heads // n_kv_heads
    _, _, n_masks = _build_edge_topology(
        n_layers, n_heads, n_kv_heads, heads_per_kv,
    )
    total_edges = 0
    for L in range(n_layers):
        n_src = 1 + L * (n_heads + 1)  # input + prior layers' heads + MLPs
        total_edges += n_src * n_heads * 3  # q, k, v per head
        n_src_mlp = n_src + n_heads
        total_edges += n_src_mlp

    return {
        "total_edges": total_edges,
        "n_independent_masks": n_masks,
        "mask_memory_bytes": n_masks * 4,  # float32
        "mask_memory_mb": n_masks * 4 / (1024 ** 2),
    }
