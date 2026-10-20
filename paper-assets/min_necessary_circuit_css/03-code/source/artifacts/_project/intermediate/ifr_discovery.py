"""IFR (Information Flow Routes) circuit discovery.

Activation decomposition method based on ALTI (Ferrando & Voita, EMNLP 2024).
Scores edges by residual-stream proximity between source output and destination input:

    score(u->v) = max(||x_v||_1 - ||y_u - x_v||_1, 0)

where y_u is component u's output and x_v is the residual stream input to component v.

Properties:
- Single forward pass + activation cache (no backprop, no optimization loop)
- Complementary to gradient-based (EAP-IG) and mask optimization (Edge Pruning)
- Scales to 0.5B-8B models, replacing ACDC in the large-model K=3 ensemble
"""

import torch
from typing import Dict, List, Tuple, Optional


def _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:
    """max(||x_v||_1 - ||y_u - x_v||_1, 0), averaged over batch and sequence."""
    diff_norm = (y_u - x_v).abs().sum(dim=-1)
    base_norm = x_v.abs().sum(dim=-1)
    return (base_norm - diff_norm).clamp(min=0).mean().item()


def _src_layer(name: str) -> int:
    if name == "hook_embed":
        return -1
    return int(name.split(".")[1])


def _before_attn(src: str, dst_layer: int) -> bool:
    """Source must come from a strictly earlier layer to feed into attention."""
    return _src_layer(src) < dst_layer


def _before_mlp(src: str, dst_layer: int) -> bool:
    """Source can be from earlier layers, or same-layer attention heads (not MLP)."""
    sl = _src_layer(src)
    if sl < dst_layer:
        return True
    return sl == dst_layer and "hook_result" in src


def _extract_tokens(dataset):
    if isinstance(dataset, torch.Tensor):
        return dataset
    if hasattr(dataset, "toks"):
        return dataset.toks
    if isinstance(dataset, dict) and "input_ids" in dataset:
        return dataset["input_ids"]
    return dataset


def _enumerate_edges(n_layers: int, n_heads: int) -> List[Tuple[str, str]]:
    """List all (src_name, dst_name) edge pairs in TransformerLens format."""
    sources = ["hook_embed"]
    for L in range(n_layers):
        for H in range(n_heads):
            sources.append(f"blocks.{L}.attn.hook_result[{H}]")
        sources.append(f"blocks.{L}.hook_mlp_out")

    edges = []
    for L_dst in range(n_layers):
        for H_dst in range(n_heads):
            for hook in ("hook_q", "hook_k", "hook_v"):
                dst = f"blocks.{L_dst}.attn.{hook}[{H_dst}]"
                for src in sources:
                    if _before_attn(src, L_dst):
                        edges.append((src, dst))
        mlp_dst = f"blocks.{L_dst}.hook_mlp_in"
        for src in sources:
            if _before_mlp(src, L_dst):
                edges.append((src, mlp_dst))
    return edges


def run_ifr(
    model,
    dataset,
    metric=None,
) -> Dict[str, float]:
    """Run IFR (Information Flow Routes) and return edge scores.

    Args:
        model: HookedTransformer instance
        dataset: tokenized input (tensor, dict with 'input_ids', or object with .toks)
        metric: unused (IFR is non-causal), kept for interface compatibility

    Returns:
        Dict mapping edge names to IFR proximity scores (>=0).
        Edge names use TransformerLens format:
        "blocks.{L}.attn.hook_result[{H}] -> blocks.{L'}.attn.hook_q[{H'}]"
    """
    n_layers = model.cfg.n_layers
    n_heads = model.cfg.n_heads

    required = set()
    for L in range(n_layers):
        required.update([
            f"blocks.{L}.attn.hook_result",
            f"blocks.{L}.hook_mlp_out",
            f"blocks.{L}.hook_resid_pre",
            f"blocks.{L}.hook_resid_mid",
        ])

    tokens = _extract_tokens(dataset)

    with torch.no_grad():
        _, cache = model.run_with_cache(
            tokens, names_filter=lambda n: n in required
        )

    # Source activations: embed (= resid_pre[0]), per-head attn outputs, MLP outputs
    src_act = {}
    src_act["hook_embed"] = cache["blocks.0.hook_resid_pre"]
    for L in range(n_layers):
        result = cache[f"blocks.{L}.attn.hook_result"]  # [batch, seq, n_heads, d_model]
        for H in range(n_heads):
            src_act[f"blocks.{L}.attn.hook_result[{H}]"] = result[:, :, H, :]
        src_act[f"blocks.{L}.hook_mlp_out"] = cache[f"blocks.{L}.hook_mlp_out"]

    edge_scores: Dict[str, float] = {}

    for L_dst in range(n_layers):
        resid_pre = cache[f"blocks.{L_dst}.hook_resid_pre"]   # input to attention
        resid_mid = cache[f"blocks.{L_dst}.hook_resid_mid"]   # input to MLP

        # Compute proximity once per (source, destination_layer) pair;
        # all heads at the same layer share resid_pre, so their scores are identical
        attn_prox: Dict[str, float] = {}
        mlp_prox: Dict[str, float] = {}

        for src_name, y_u in src_act.items():
            if _before_attn(src_name, L_dst):
                attn_prox[src_name] = _proximity(y_u, resid_pre)
            if _before_mlp(src_name, L_dst):
                mlp_prox[src_name] = _proximity(y_u, resid_mid)

        # Expand to per-head Q/K/V edges
        for src_name, score in attn_prox.items():
            for H_dst in range(n_heads):
                for hook in ("hook_q", "hook_k", "hook_v"):
                    edge_scores[f"{src_name} -> blocks.{L_dst}.attn.{hook}[{H_dst}]"] = score

        # MLP edges
        for src_name, score in mlp_prox.items():
            edge_scores[f"{src_name} -> blocks.{L_dst}.hook_mlp_in"] = score

    return edge_scores
