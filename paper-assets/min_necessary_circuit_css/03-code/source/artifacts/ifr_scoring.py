"""IFR (Information Flow Routes) edge-level scoring for HuggingFace models.

Implements ALTI-based proximity attribution from:
  Ferrando & Voita, "Information Flow Routes: Automatically Interpreting
  Language Models at Scale", EMNLP 2024.

Scores each edge (u->v) by how much source u's output is "present" in the
residual stream that destination v reads from:

    score(u->v) = max(||x_v||_1 - ||y_u - x_v||_1, 0)

where y_u = component u's output, x_v = residual stream input to component v.

Input:
  - model: HuggingFace CausalLM (Llama, Qwen2, Gemma2, Mistral, GPT2)
  - dataset: tokenized examples (list[dict], dict with input_ids, or Tensor)
  - metric_fn: unused — kept for interface parity with EAP-IG / Edge Pruning

Output:
  - Dict[str, float] mapping canonical edge names to proximity scores (>=0).
    Format: "{src}->{dst}"
    Nodes: input, a{L}.h{H}, m{L}
    Attention destinations carry .q/.k/.v suffix: a{L}.h{H}.q

Dependencies: torch, transformers
"""

from __future__ import annotations

import torch
import torch.nn as nn
from typing import Dict, Callable, Union


# ---------------------------------------------------------------------------
# Core proximity metric (ALTI)
# ---------------------------------------------------------------------------

def _proximity(y_u: torch.Tensor, x_v: torch.Tensor) -> float:
    """max(||x_v||_1 - ||y_u - x_v||_1, 0), averaged over batch & sequence."""
    diff_norm = (y_u - x_v).abs().sum(dim=-1)
    base_norm = x_v.abs().sum(dim=-1)
    return (base_norm - diff_norm).clamp(min=0).mean().item()


# ---------------------------------------------------------------------------
# Architecture detection
# ---------------------------------------------------------------------------

_LLAMA_LIKE = frozenset({
    "llama", "qwen2", "gemma", "gemma2", "mistral", "phi3", "phi",
})


def _get_model_info(model) -> dict:
    cfg = model.config
    model_type = getattr(cfg, "model_type", "")

    if model_type in _LLAMA_LIKE:
        backbone = model.model
        layers = backbone.layers
        n_heads = cfg.num_attention_heads
        d_model = cfg.hidden_size
        return dict(
            arch="llama_like", backbone=backbone, layers=layers,
            n_layers=len(layers), n_heads=n_heads,
            head_dim=d_model // n_heads, d_model=d_model,
        )

    if model_type == "gpt2":
        backbone = model.transformer
        layers = backbone.h
        n_heads = cfg.n_head
        d_model = cfg.n_embd
        return dict(
            arch="gpt2", backbone=backbone, layers=layers,
            n_layers=len(layers), n_heads=n_heads,
            head_dim=d_model // n_heads, d_model=d_model,
        )

    raise ValueError(f"Unsupported model_type={model_type!r}")


# ---------------------------------------------------------------------------
# Edge topology helpers
# ---------------------------------------------------------------------------

def _before_attn(kind: str, src_layer: int, dst_layer: int) -> bool:
    if kind == "input":
        return True
    return src_layer < dst_layer


def _before_mlp(kind: str, src_layer: int, dst_layer: int) -> bool:
    if kind == "input":
        return True
    if src_layer < dst_layer:
        return True
    return src_layer == dst_layer and kind == "attn"


# ---------------------------------------------------------------------------
# Dataset preparation
# ---------------------------------------------------------------------------

def _prepare_tokens(
    dataset: Union[torch.Tensor, dict, list],
    device: str,
) -> torch.Tensor:
    if isinstance(dataset, torch.Tensor):
        t = dataset
    elif isinstance(dataset, dict) and "input_ids" in dataset:
        ids = dataset["input_ids"]
        t = ids if isinstance(ids, torch.Tensor) else torch.tensor(ids)
    elif isinstance(dataset, list) and len(dataset) > 0:
        first = dataset[0]
        if isinstance(first, dict) and "input_ids" in first:
            tensors = [
                d["input_ids"] if isinstance(d["input_ids"], torch.Tensor)
                else torch.tensor(d["input_ids"])
                for d in dataset
            ]
            t = torch.stack(tensors)
        elif isinstance(first, torch.Tensor):
            t = torch.stack(dataset)
        else:
            t = torch.tensor(dataset)
    else:
        raise TypeError(f"Unsupported dataset type: {type(dataset)}")
    t = t.to(device)
    return t.unsqueeze(0) if t.dim() == 1 else t


# ---------------------------------------------------------------------------
# Per-head decomposition through the output projection
# ---------------------------------------------------------------------------

def _decompose_per_head(
    concat_heads: torch.Tensor,
    proj: nn.Module,
    n_heads: int,
    head_dim: int,
) -> Dict[int, torch.Tensor]:
    """Split concatenated head activations and project each through o_proj."""
    try:
        from transformers.pytorch_utils import Conv1D
        is_conv1d = isinstance(proj, Conv1D)
    except ImportError:
        is_conv1d = False

    W = proj.weight
    heads: Dict[int, torch.Tensor] = {}
    for h in range(n_heads):
        h_in = concat_heads[:, :, h * head_dim:(h + 1) * head_dim]
        if is_conv1d:
            # Conv1D: weight [in, out], forward = input @ weight
            W_h = W[h * head_dim:(h + 1) * head_dim, :]
            heads[h] = h_in @ W_h
        else:
            # nn.Linear: weight [out, in], forward = input @ weight.T
            W_h = W[:, h * head_dim:(h + 1) * head_dim]
            heads[h] = h_in @ W_h.T
    return heads


# ---------------------------------------------------------------------------
# Canonical edge name helpers
# ---------------------------------------------------------------------------

def _src_label(kind: str, layer: int, head: int) -> str:
    if kind == "input":
        return "input"
    if kind == "attn":
        return f"a{layer}.h{head}"
    return f"m{layer}"


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def compute_ifr_edges(
    model,
    dataset,
    metric_fn: Callable,
    threshold: float = 0.1,
    device: str = "cuda",
) -> Dict[str, float]:
    """Compute IFR edge-level scores.

    Returns dict of canonical_edge_name -> score.
    Edge format: "{src}->{dst}" with nodes named as:
      input, a{L}.h{H}, m{L}
    Attention destinations carry a .q/.k/.v suffix.

    metric_fn is accepted for interface compatibility but unused;
    IFR is a non-causal, activation-decomposition method.
    """
    info = _get_model_info(model)
    arch = info["arch"]
    n_layers = info["n_layers"]
    n_heads = info["n_heads"]
    head_dim = info["head_dim"]
    layers = info["layers"]

    tokens = _prepare_tokens(dataset, device)

    # ---- register hooks to capture activations in a single forward pass ----
    cache: dict = dict(resid_pre={}, attn_out={}, head_out={}, mlp_out={})
    hooks: list = []

    for l_idx in range(n_layers):
        layer = layers[l_idx]

        # 1) resid_pre: residual stream entering this layer
        def _pre(mod, inp, *, _l=l_idx):
            x = inp[0]
            if isinstance(x, torch.Tensor):
                cache["resid_pre"][_l] = x.detach()
        hooks.append(layer.register_forward_pre_hook(_pre))

        # 2) Per-head + full attention output via the output projection
        o_proj = (
            layer.self_attn.o_proj if arch == "llama_like"
            else layer.attn.c_proj
        )

        def _oproj(mod, inp, out, *, _l=l_idx):
            cache["attn_out"][_l] = out.detach()
            cache["head_out"][_l] = _decompose_per_head(
                inp[0].detach(), mod, n_heads, head_dim,
            )
        hooks.append(o_proj.register_forward_hook(_oproj))

        # 3) MLP output
        def _mlp(mod, inp, out, *, _l=l_idx):
            cache["mlp_out"][_l] = (
                out.detach() if isinstance(out, torch.Tensor)
                else out[0].detach()
            )
        hooks.append(layer.mlp.register_forward_hook(_mlp))

    # ---- single forward pass ----
    model.eval()
    try:
        with torch.no_grad():
            model(tokens)
    finally:
        for h in hooks:
            h.remove()

    # ---- build source activation table: (kind, layer, head) -> [B, S, D] ----
    src_act: Dict[tuple, torch.Tensor] = {}
    src_act[("input", -1, -1)] = cache["resid_pre"][0]

    for l in range(n_layers):
        if l in cache["head_out"]:
            for h in range(n_heads):
                src_act[("attn", l, h)] = cache["head_out"][l][h]
        if l in cache["mlp_out"]:
            src_act[("mlp", l, -1)] = cache["mlp_out"][l]

    # resid_mid[L] = resid_pre[L] + attn_out[L]
    # (exact for Llama/Qwen2/Mistral; slight approximation for Gemma2
    #  which applies an extra LN on attn output before residual addition)
    resid_mid: Dict[int, torch.Tensor] = {}
    for l in range(n_layers):
        if l in cache["resid_pre"] and l in cache["attn_out"]:
            resid_mid[l] = cache["resid_pre"][l] + cache["attn_out"][l]

    # ---- proximity scoring ----
    edge_scores: Dict[str, float] = {}

    for L in range(n_layers):
        rp = cache["resid_pre"].get(L)
        rm = resid_mid.get(L)

        # Edges into attention at layer L
        if rp is not None:
            for (kind, sl, sh), y_u in src_act.items():
                if not _before_attn(kind, sl, L):
                    continue
                score = _proximity(y_u, rp)
                if score < threshold:
                    continue
                src = _src_label(kind, sl, sh)
                for H in range(n_heads):
                    for qkv in ("q", "k", "v"):
                        edge_scores[f"{src}->a{L}.h{H}.{qkv}"] = score

        # Edges into MLP at layer L
        if rm is not None:
            for (kind, sl, sh), y_u in src_act.items():
                if not _before_mlp(kind, sl, L):
                    continue
                score = _proximity(y_u, rm)
                if score < threshold:
                    continue
                src = _src_label(kind, sl, sh)
                edge_scores[f"{src}->m{L}"] = score

    return edge_scores
