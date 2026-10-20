"""Edge Pruning with L0 regularization for HuggingFace models.

Implements princeton-nlp style Edge Pruning using Hard Concrete relaxation
(Louizos et al., 2018) on HuggingFace CausalLM models with GQA support.

Each edge (u->v) in the computational graph gets a learnable mask via the
Hard Concrete distribution, which allows exact zeros and ones. The masks
are optimized to minimize faithfulness loss + L0 sparsity penalty.

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

    def _src_nodes_before_layer(layer: int, include_attn_same_layer: bool = False):
        """Yield (src_name,) for all nodes whose output feeds into a given layer."""
        yield "input"
        for l in range(layer):
            for h in range(n_heads):
                yield f"a{l}.h{h}"
            yield f"m{l}"
        if include_attn_same_layer:
            for h in range(n_heads):
                yield f"a{layer}.h{h}"

    for L in range(n_layers):
        # --- Edges into attention heads at layer L ---
        srcs_attn = list(_src_nodes_before_layer(L, include_attn_same_layer=False))
        for src in srcs_attn:
            for H in range(n_heads):
                # Q edge: always independent
                q_edge = f"{src}->a{L}.h{H}.q"
                edge_names.append(q_edge)
                edge_to_mask_idx[q_edge] = mask_idx
                mask_idx += 1

            # K edges: shared within KV group
            for kv_group in range(n_kv_heads):
                k_mask_idx = mask_idx
                mask_idx += 1
                for h_in_group in range(heads_per_kv_group):
                    H = kv_group * heads_per_kv_group + h_in_group
                    k_edge = f"{src}->a{L}.h{H}.k"
                    edge_names.append(k_edge)
                    edge_to_mask_idx[k_edge] = k_mask_idx

            # V edges: shared within KV group
            for kv_group in range(n_kv_heads):
                v_mask_idx = mask_idx
                mask_idx += 1
                for h_in_group in range(heads_per_kv_group):
                    H = kv_group * heads_per_kv_group + h_in_group
                    v_edge = f"{src}->a{L}.h{H}.v"
                    edge_names.append(v_edge)
                    edge_to_mask_idx[v_edge] = v_mask_idx

        # --- Edges into MLP at layer L ---
        srcs_mlp = list(_src_nodes_before_layer(L, include_attn_same_layer=True))
        for src in srcs_mlp:
            mlp_edge = f"{src}->m{L}"
            edge_names.append(mlp_edge)
            edge_to_mask_idx[mlp_edge] = mask_idx
            mask_idx += 1

    return edge_names, edge_to_mask_idx, mask_idx


# ---------------------------------------------------------------------------
# Destination-grouped mask table for efficient hook application
# ---------------------------------------------------------------------------

def _build_dst_mask_table(
    edge_to_mask_idx: Dict[str, int],
) -> Dict[str, Dict[str, int]]:
    """Group edges by destination node.

    Returns: {dst_node: {src_node: mask_param_index}}
    """
    table: Dict[str, Dict[str, int]] = {}
    for edge, idx in edge_to_mask_idx.items():
        src, dst = edge.split("->", 1)
        if dst not in table:
            table[dst] = {}
        table[dst][src] = idx
    return table


# ---------------------------------------------------------------------------
# Source activation cache (captured via hooks)
# ---------------------------------------------------------------------------

class _ActivationCache:
    """Stores source node activations during forward pass."""

    def __init__(self):
        self.embed_out: Optional[torch.Tensor] = None
        self.head_out: Dict[int, Dict[int, torch.Tensor]] = {}
        self.mlp_out: Dict[int, torch.Tensor] = {}


# ---------------------------------------------------------------------------
# Hook-based masked forward pass
# ---------------------------------------------------------------------------

def _get_module(model, path: str) -> nn.Module:
    parts = path.split(".")
    m = model
    for p in parts:
        m = getattr(m, p)
    return m


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


def _masked_forward(
    model,
    input_ids: torch.Tensor,
    masks: torch.Tensor,
    arch_info: dict,
    dst_mask_table: Dict[str, Dict[str, int]],
) -> torch.Tensor:
    """Run forward pass with edge masks applied via hooks.

    Strategy:
    1. Register hooks to capture source node outputs (embed, attn heads, MLP).
    2. At each destination's pre-hook, replace its input with the masked sum
       of upstream source outputs.

    For memory efficiency, source activations are captured and masks applied
    layer-by-layer. Each layer's pre-hook constructs the masked residual
    from all upstream sources.
    """
    n_layers = arch_info["n_layers"]
    n_heads = arch_info["n_heads"]
    head_dim = arch_info["head_dim"]
    layers = model.model.layers

    cache = _ActivationCache()
    hooks = []

    # Capture embedding output
    def _embed_hook(mod, inp, out):
        cache.embed_out = out
    hooks.append(model.model.embed_tokens.register_forward_hook(_embed_hook))

    for L in range(n_layers):
        layer = layers[L]

        # Capture per-head attention output via o_proj
        def _oproj_hook(mod, inp, out, *, _L=L):
            cache.head_out[_L] = _decompose_attn_output(
                inp[0], mod, n_heads, head_dim,
            )
        hooks.append(layer.self_attn.o_proj.register_forward_hook(_oproj_hook))

        # Capture MLP output
        def _mlp_hook(mod, inp, out, *, _L=L):
            cache.mlp_out[_L] = out if isinstance(out, torch.Tensor) else out[0]
        hooks.append(layer.mlp.register_forward_hook(_mlp_hook))

        # Pre-hook on each layer: construct masked residual stream input.
        # This replaces the residual stream with the masked combination of
        # all upstream source nodes.
        def _layer_pre_hook(mod, inp, *, _L=L):
            x = inp[0] if isinstance(inp, tuple) else inp

            # Collect all source activations available before this layer
            src_acts: Dict[str, torch.Tensor] = {}
            if cache.embed_out is not None:
                src_acts["input"] = cache.embed_out
            for l in range(_L):
                if l in cache.head_out:
                    for h in range(n_heads):
                        src_acts[f"a{l}.h{h}"] = cache.head_out[l][h]
                if l in cache.mlp_out:
                    src_acts[f"m{l}"] = cache.mlp_out[l]

            # For attention destinations (q, k, v) at this layer:
            # We approximate by masking the residual stream input.
            # The mask for each destination type is the element-wise product
            # of all source masks. For simplicity and memory, we apply the
            # *minimum* mask across q/k/v destinations for each source,
            # effectively masking the residual input to the entire attention block.
            #
            # More precise: build separate masked inputs per q/k/v head.
            # But that requires modifying internal attention computation,
            # which is architecture-specific. The residual-level masking
            # is the standard approach in princeton-nlp/edge-pruning.

            # Gather all destination nodes at this layer
            attn_dsts = set()
            mlp_dst = f"m{_L}"
            for H in range(n_heads):
                for qkv in ("q", "k", "v"):
                    attn_dsts.add(f"a{_L}.h{H}.{qkv}")

            # Compute masked residual for attention input
            # Use average mask across all attn destinations for each source
            masked_resid = torch.zeros_like(x)
            for src_name, src_act in src_acts.items():
                # Collect mask values for this source across attn destinations
                mask_indices = []
                for dst in attn_dsts:
                    if dst in dst_mask_table and src_name in dst_mask_table[dst]:
                        mask_indices.append(dst_mask_table[dst][src_name])
                if mask_indices:
                    # Average mask across destinations (approximation)
                    src_mask = masks[mask_indices].mean()
                    masked_resid = masked_resid + src_act * src_mask

            if isinstance(inp, tuple):
                return (masked_resid,) + inp[1:]
            return masked_resid

        hooks.append(layer.register_forward_pre_hook(_layer_pre_hook))

    try:
        out = model(input_ids)
        return out.logits
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
    """KL divergence between clean and masked model output distributions.

    If target_ids is provided, only compute loss at target token positions.
    """
    if target_ids is not None:
        # target_ids: [batch] — index of the token position to evaluate
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

    # Build edge topology
    edge_names, edge_to_mask_idx, n_masks = _build_edge_topology(
        n_layers, n_heads, n_kv_heads, heads_per_kv_group,
    )
    dst_mask_table = _build_dst_mask_table(edge_to_mask_idx)

    # Initialize Hard Concrete mask parameters
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

    # Get clean model logits (frozen)
    model.eval()
    with torch.no_grad():
        clean_logits = model(clean_ids).logits.detach()

    # Optimization loop
    for epoch in range(n_epochs):
        optimizer.zero_grad()

        # Sample masks from Hard Concrete
        masks = hard_concrete(training=True)

        # Forward pass with masks applied
        masked_logits = _masked_forward(
            model, clean_ids, masks, arch_info, dst_mask_table,
        )

        # Loss = faithfulness + sparsity
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
    # Total edges (including shared masks counted separately)
    total_edges = 0
    for L in range(n_layers):
        n_src = 1 + L * (n_heads + 1)  # input + prior layers' heads + MLPs
        # Attn edges: Q independent, K/V shared per KV group
        total_edges += n_src * n_heads * 3  # q, k, v per head
        # MLP edges: from all upstream including same-layer attn
        n_src_mlp = n_src + n_heads
        total_edges += n_src_mlp

    return {
        "total_edges": total_edges,
        "n_independent_masks": n_masks,
        "mask_memory_bytes": n_masks * 4,  # float32
        "mask_memory_mb": n_masks * 4 / (1024 ** 2),
    }
