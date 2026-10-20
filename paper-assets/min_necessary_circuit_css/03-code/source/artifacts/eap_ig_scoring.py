"""EAP-IG (Edge Attribution Patching with Integrated Gradients) for HuggingFace models.

Implements edge-level causal attribution from:
  Syed et al., "Attribution Patching Outperforms Automated Circuit Discovery", 2023.

Algorithm:
  1. Capture clean/corrupt source activations (embedding, per-head attn, MLP outputs).
  2. For each IG step, interpolate embeddings, forward+backward to accumulate
     gradients at Q/K/V projection outputs and resid_mid.
  3. Edge score = |avg_grad_at_dst · projected_delta_src|, where the source delta
     is projected through Q/K/V weight matrices for per-head attribution.

Input:
  - model: HuggingFace CausalLM (Qwen2, Llama, Gemma2, Mistral, GPT-2)
  - clean_inputs / corrupt_inputs: token IDs (Tensor, list, or dict)
  - metric_fn: callable(logits, target_ids) -> scalar
  - target_ids: target token IDs for metric

Output:
  - Dict[str, float] mapping canonical edge names to |attribution scores|.
    Format: "{src}->{dst}"
    Nodes: input, a{L}.h{H}, m{L}
    Attention destinations carry .q/.k/.v suffix: a{L}.h{H}.q

Dependencies: torch, transformers
"""

from __future__ import annotations

import torch
import torch.nn as nn
from typing import Dict, Callable, Union, List


# ---------------------------------------------------------------------------
# Architecture detection (shared pattern with ifr_scoring.py)
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
        n_kv_heads = getattr(cfg, "num_key_value_heads", n_heads)
        d_model = cfg.hidden_size
        head_dim = getattr(cfg, "head_dim", d_model // n_heads)
        return dict(
            arch="llama_like", backbone=backbone, layers=layers,
            n_layers=len(layers), n_heads=n_heads, n_kv_heads=n_kv_heads,
            head_dim=head_dim, d_model=d_model, model_type=model_type,
        )

    if model_type == "gpt2":
        backbone = model.transformer
        layers = backbone.h
        n_heads = cfg.n_head
        d_model = cfg.n_embd
        return dict(
            arch="gpt2", backbone=backbone, layers=layers,
            n_layers=len(layers), n_heads=n_heads, n_kv_heads=n_heads,
            head_dim=d_model // n_heads, d_model=d_model, model_type=model_type,
        )

    raise ValueError(f"Unsupported model_type={model_type!r}")


# ---------------------------------------------------------------------------
# Input preparation
# ---------------------------------------------------------------------------

def _prepare_inputs(
    inputs: Union[torch.Tensor, List, dict],
    device: str,
) -> torch.Tensor:
    if isinstance(inputs, torch.Tensor):
        t = inputs
    elif isinstance(inputs, dict) and "input_ids" in inputs:
        ids = inputs["input_ids"]
        t = ids if isinstance(ids, torch.Tensor) else torch.tensor(ids)
    elif isinstance(inputs, list) and len(inputs) > 0:
        first = inputs[0]
        if isinstance(first, dict) and "input_ids" in first:
            tensors = [
                d["input_ids"] if isinstance(d["input_ids"], torch.Tensor)
                else torch.tensor(d["input_ids"])
                for d in inputs
            ]
            t = torch.stack(tensors)
        elif isinstance(first, torch.Tensor):
            t = torch.stack(inputs)
        elif isinstance(first, (list, int)):
            t = torch.tensor(inputs if isinstance(first, list) else [inputs])
        else:
            raise TypeError(f"Unsupported input element type: {type(first)}")
    else:
        raise TypeError(f"Unsupported input type: {type(inputs)}")
    t = t.to(device)
    return t.unsqueeze(0) if t.dim() == 1 else t


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


def _src_label(kind: str, layer: int, head: int) -> str:
    if kind == "input":
        return "input"
    if kind == "attn":
        return f"a{layer}.h{head}"
    return f"m{layer}"


# ---------------------------------------------------------------------------
# Per-head decomposition through output projection
# ---------------------------------------------------------------------------

def _decompose_per_head(
    concat_heads: torch.Tensor,
    proj: nn.Module,
    n_heads: int,
    head_dim: int,
) -> Dict[int, torch.Tensor]:
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
            W_h = W[h * head_dim:(h + 1) * head_dim, :]
            heads[h] = h_in @ W_h
        else:
            W_h = W[:, h * head_dim:(h + 1) * head_dim]
            heads[h] = h_in @ W_h.T
    return heads


# ---------------------------------------------------------------------------
# Source activation capture
# ---------------------------------------------------------------------------

def _capture_source_activations(model, tokens, info):
    """Single forward pass to capture all source node activations (detached)."""
    arch = info["arch"]
    n_layers = info["n_layers"]
    n_heads = info["n_heads"]
    head_dim = info["head_dim"]
    layers = info["layers"]

    cache: dict = {}
    hooks: list = []

    def pre_hook_l0(mod, inp):
        cache["embed"] = inp[0].detach()
    hooks.append(layers[0].register_forward_pre_hook(pre_hook_l0))

    for L in range(n_layers):
        layer = layers[L]
        o_proj = (
            layer.self_attn.o_proj if arch == "llama_like"
            else layer.attn.c_proj
        )

        def oproj_hook(mod, inp, out, _L=L):
            cache[("head", _L)] = _decompose_per_head(
                inp[0].detach(), mod, n_heads, head_dim,
            )
        hooks.append(o_proj.register_forward_hook(oproj_hook))

        def mlp_hook(mod, inp, out, _L=L):
            cache[("mlp", _L)] = (
                out.detach() if isinstance(out, torch.Tensor)
                else out[0].detach()
            )
        hooks.append(layer.mlp.register_forward_hook(mlp_hook))

    model.eval()
    with torch.no_grad():
        model(tokens)

    for h in hooks:
        h.remove()

    src: Dict[tuple, torch.Tensor] = {}
    src[("input", -1, -1)] = cache["embed"]
    for L in range(n_layers):
        for H in range(n_heads):
            src[("attn", L, H)] = cache[("head", L)][H]
        src[("mlp", L, -1)] = cache[("mlp", L)]
    return src


# ---------------------------------------------------------------------------
# Q/K/V projection weight extraction
# ---------------------------------------------------------------------------

def _get_proj_weights(layer, info):
    """Effective Q/K/V weights W such that proj = delta @ W.

    Returns (W_q, W_k, W_v) each [d_model, proj_dim] in float32.
    """
    arch = info["arch"]
    d_model = info["d_model"]

    if arch == "llama_like":
        W_q = layer.self_attn.q_proj.weight.detach().float().T
        W_k = layer.self_attn.k_proj.weight.detach().float().T
        W_v = layer.self_attn.v_proj.weight.detach().float().T
        return W_q, W_k, W_v

    c_attn = layer.attn.c_attn
    try:
        from transformers.pytorch_utils import Conv1D
        is_conv1d = isinstance(c_attn, Conv1D)
    except ImportError:
        is_conv1d = False

    W = c_attn.weight.detach().float()
    if is_conv1d:
        return W[:, :d_model], W[:, d_model:2 * d_model], W[:, 2 * d_model:]
    return W[:d_model, :].T, W[d_model:2 * d_model, :].T, W[2 * d_model:, :].T


# ---------------------------------------------------------------------------
# Pre-MLP layer norm finder
# ---------------------------------------------------------------------------

def _get_pre_mlp_ln(layer, arch):
    if arch == "gpt2":
        return layer.ln_2
    if hasattr(layer, "pre_feedforward_layernorm"):
        return layer.pre_feedforward_layernorm
    return layer.post_attention_layernorm


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def compute_eap_ig_edges(
    model,
    clean_inputs,
    corrupt_inputs,
    metric_fn: Callable,
    target_ids,
    ig_steps: int = 5,
    device: str = "cuda",
) -> Dict[str, float]:
    """Compute EAP-IG edge-level attribution scores.

    Returns dict of canonical_edge_name -> |score|.
    Edge format: "{src}->{dst}" with nodes named as:
      input, a{L}.h{H}, m{L}
    Attention destinations carry a .q/.k/.v suffix.

    Per-head attribution uses gradient at Q/K/V projection outputs
    with source deltas projected through QKV weight matrices (LayerNorm
    Jacobian approximated as identity).

    GQA is handled: K/V edges for query heads sharing a KV group use the
    shared KV head's gradient and weight slice.

    Model must reside on a single device.
    """
    info = _get_model_info(model)
    arch = info["arch"]
    n_layers = info["n_layers"]
    n_heads = info["n_heads"]
    n_kv_heads = info["n_kv_heads"]
    head_dim = info["head_dim"]
    d_model = info["d_model"]
    layers = info["layers"]
    heads_per_group = n_heads // n_kv_heads if n_kv_heads > 0 else 1

    clean_tokens = _prepare_inputs(clean_inputs, device)
    corrupt_tokens = _prepare_inputs(corrupt_inputs, device)
    model.eval()

    # --- Phase 1: source activations & deltas ---
    clean_src = _capture_source_activations(model, clean_tokens, info)
    corrupt_src = _capture_source_activations(model, corrupt_tokens, info)

    clean_embeds = clean_src[("input", -1, -1)].float()
    corrupt_embeds = corrupt_src[("input", -1, -1)].float()

    deltas = {k: (clean_src[k] - corrupt_src[k]).float() for k in clean_src}
    del clean_src, corrupt_src

    # --- Phase 2: IG gradient accumulation ---
    if ig_steps <= 1:
        alphas = [1.0]
    else:
        alphas = [step / (ig_steps - 1) for step in range(ig_steps)]

    acc_q: List = [None] * n_layers
    acc_k: List = [None] * n_layers
    acc_v: List = [None] * n_layers
    acc_mid: List = [None] * n_layers

    for alpha in alphas:
        interp = (
            corrupt_embeds + alpha * (clean_embeds - corrupt_embeds)
        ).detach().requires_grad_(True)

        hooks: list = []
        cached: dict = {}

        # Inject interpolated embedding at layer-0 input
        def _layer0_pre(mod, inp, _interp=interp):
            return (_interp,) + inp[1:]
        hooks.append(layers[0].register_forward_pre_hook(_layer0_pre))

        for L in range(n_layers):
            layer_mod = layers[L]

            if arch == "llama_like":
                for pname in ("q", "k", "v"):
                    proj_mod = getattr(layer_mod.self_attn, f"{pname}_proj")

                    def _qkv_hook(mod, inp, out, _key=(pname, L)):
                        out.retain_grad()
                        cached[_key] = out
                    hooks.append(proj_mod.register_forward_hook(_qkv_hook))
            else:
                def _cattn_hook(mod, inp, out, _L=L):
                    out.retain_grad()
                    cached[("qkv", _L)] = out
                hooks.append(layer_mod.attn.c_attn.register_forward_hook(_cattn_hook))

            ln2 = _get_pre_mlp_ln(layer_mod, arch)

            def _mid_hook(mod, inp, _L=L):
                x = inp[0]
                x.retain_grad()
                cached[("mid", _L)] = x
            hooks.append(ln2.register_forward_pre_hook(_mid_hook))

        # Forward + backward
        with torch.enable_grad():
            outputs = model(clean_tokens)
            loss = metric_fn(outputs.logits, target_ids)
            loss.backward()

        # Harvest gradients
        for L in range(n_layers):
            if arch == "llama_like":
                for pname, acc in [("q", acc_q), ("k", acc_k), ("v", acc_v)]:
                    t = cached.get((pname, L))
                    if t is not None and t.grad is not None:
                        g = t.grad.detach().float()
                        acc[L] = g if acc[L] is None else acc[L] + g
            else:
                t = cached.get(("qkv", L))
                if t is not None and t.grad is not None:
                    g = t.grad.detach().float()
                    acc_q[L] = (g[:, :, :d_model]
                                if acc_q[L] is None
                                else acc_q[L] + g[:, :, :d_model])
                    acc_k[L] = (g[:, :, d_model:2 * d_model]
                                if acc_k[L] is None
                                else acc_k[L] + g[:, :, d_model:2 * d_model])
                    acc_v[L] = (g[:, :, 2 * d_model:]
                                if acc_v[L] is None
                                else acc_v[L] + g[:, :, 2 * d_model:])

            t = cached.get(("mid", L))
            if t is not None and t.grad is not None:
                g = t.grad.detach().float()
                acc_mid[L] = g if acc_mid[L] is None else acc_mid[L] + g

        for h in hooks:
            h.remove()
        model.zero_grad()

    # Average over IG steps
    n_alpha = len(alphas)
    for L in range(n_layers):
        for acc in [acc_q, acc_k, acc_v, acc_mid]:
            if acc[L] is not None:
                acc[L] /= n_alpha

    # --- Phase 3: edge score computation ---
    edge_scores: Dict[str, float] = {}

    for L in range(n_layers):
        if acc_q[L] is None:
            continue

        W_q, W_k, W_v = _get_proj_weights(layers[L], info)
        grad_q = acc_q[L]
        grad_k = acc_k[L]
        grad_v = acc_v[L]
        grad_mid = acc_mid[L]

        for (kind, sl, sh), delta_u in deltas.items():
            src_name = _src_label(kind, sl, sh)

            if _before_attn(kind, sl, L):
                proj_q = delta_u @ W_q
                proj_k = delta_u @ W_k
                proj_v = delta_u @ W_v

                for H in range(n_heads):
                    kv = H // heads_per_group
                    hd = head_dim

                    gq = grad_q[:, :, H * hd:(H + 1) * hd]
                    pq = proj_q[:, :, H * hd:(H + 1) * hd]
                    edge_scores[f"{src_name}->a{L}.h{H}.q"] = (
                        (gq * pq).sum(-1).mean().abs().item()
                    )

                    gk = grad_k[:, :, kv * hd:(kv + 1) * hd]
                    pk = proj_k[:, :, kv * hd:(kv + 1) * hd]
                    edge_scores[f"{src_name}->a{L}.h{H}.k"] = (
                        (gk * pk).sum(-1).mean().abs().item()
                    )

                    gv = grad_v[:, :, kv * hd:(kv + 1) * hd]
                    pv = proj_v[:, :, kv * hd:(kv + 1) * hd]
                    edge_scores[f"{src_name}->a{L}.h{H}.v"] = (
                        (gv * pv).sum(-1).mean().abs().item()
                    )

            if _before_mlp(kind, sl, L) and grad_mid is not None:
                edge_scores[f"{src_name}->m{L}"] = (
                    (grad_mid * delta_u).sum(-1).mean().abs().item()
                )

        del W_q, W_k, W_v

    return edge_scores
