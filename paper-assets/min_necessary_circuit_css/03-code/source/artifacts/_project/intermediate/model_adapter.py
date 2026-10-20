"""Model adapter: unified interface for GPT-2 (TransformerLens) and Qwen-2.5 (HuggingFace).

Bridges different model backends to a single canonical node/edge naming scheme
for StructFuse circuit discovery methods (EAP-IG, Edge Pruning, IFR).

Canonical node format:
  input           — embedding output
  a{L}.h{H}       — attention head H output at layer L
  a{L}.h{H}.q/k/v — attention head H destination at layer L
  m{L}            — MLP at layer L
  logits          — final output

Canonical edge format: "{src}->{dst}" (no spaces around arrow)

CANONICAL_VERSION must be embedded in all cached edge scores to prevent stale reads.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Optional

import torch
import torch.nn as nn


CANONICAL_VERSION = "v2"


@dataclass
class ModelInfo:
    arch: str                   # "gpt2" | "qwen2" | "llama" | ...
    n_layers: int
    n_heads: int
    n_kv_heads: int             # GQA: fewer KV heads than query heads
    d_model: int
    head_dim: int
    backend: str                # "transformerlens" | "huggingface"
    model_name: str


# ---------------------------------------------------------------------------
# TransformerLens node name → canonical conversion patterns
# ---------------------------------------------------------------------------

_TL_NODE_PATTERNS = [
    (re.compile(r"^hook_embed$"),
     lambda m: "input"),
    (re.compile(r"^blocks\.(\d+)\.attn\.hook_result\[(\d+)\]$"),
     lambda m: f"a{m.group(1)}.h{m.group(2)}"),
    (re.compile(r"^blocks\.(\d+)\.attn\.hook_(q|k|v)\[(\d+)\]$"),
     lambda m: f"a{m.group(1)}.h{m.group(3)}.{m.group(2)}"),
    (re.compile(r"^blocks\.(\d+)\.hook_mlp_out$"),
     lambda m: f"m{m.group(1)}"),
    (re.compile(r"^blocks\.(\d+)\.hook_mlp_in$"),
     lambda m: f"m{m.group(1)}"),
]


def _tl_to_canonical(name: str) -> str:
    for pattern, formatter in _TL_NODE_PATTERNS:
        m = pattern.match(name)
        if m:
            return formatter(m)
    return name


def _hf_to_canonical(name: str) -> str:
    if name == "model.embed_tokens":
        return "input"
    if name == "lm_head":
        return "logits"
    m = re.match(r"model\.layers\.(\d+)\.self_attn\.o_proj", name)
    if m:
        return f"a{m.group(1)}"
    m = re.match(r"model\.layers\.(\d+)\.mlp", name)
    if m:
        return f"m{m.group(1)}"
    return name


def _tl_edges_to_canonical(edge_scores: Dict[str, float]) -> Dict[str, float]:
    result = {}
    for edge, score in edge_scores.items():
        if " -> " in edge:
            src, dst = edge.split(" -> ", 1)
        elif "->" in edge:
            src, dst = edge.split("->", 1)
        else:
            result[edge] = score
            continue
        canon_src = _tl_to_canonical(src.strip())
        canon_dst = _tl_to_canonical(dst.strip())
        result[f"{canon_src}->{canon_dst}"] = score
    return result


def _is_gpt2(name: str) -> bool:
    return name.startswith("gpt2") or name in (
        "gpt2-small", "gpt2-medium", "gpt2-large", "gpt2-xl",
    )


# ---------------------------------------------------------------------------
# ModelAdapter
# ---------------------------------------------------------------------------

class ModelAdapter:
    """Unified model interface for circuit discovery methods."""

    def __init__(self, model: nn.Module, info: ModelInfo, tokenizer=None):
        self.model = model
        self.info = info
        self.tokenizer = tokenizer

    # ---- Factory ----

    @classmethod
    def from_pretrained(
        cls, model_name: str, device: str = "cuda", **kwargs,
    ) -> ModelAdapter:
        if _is_gpt2(model_name):
            return cls._load_tl(model_name, device)
        return cls._load_hf(model_name, device, **kwargs)

    @classmethod
    def _load_tl(cls, model_name: str, device: str) -> ModelAdapter:
        from transformer_lens import HookedTransformer

        model = HookedTransformer.from_pretrained(model_name, device=device)
        info = ModelInfo(
            arch="gpt2",
            n_layers=model.cfg.n_layers,
            n_heads=model.cfg.n_heads,
            n_kv_heads=model.cfg.n_heads,
            d_model=model.cfg.d_model,
            head_dim=model.cfg.d_head,
            backend="transformerlens",
            model_name=model_name,
        )
        return cls(model, info, tokenizer=model.tokenizer)

    @classmethod
    def _load_hf(cls, model_name: str, device: str, **kwargs) -> ModelAdapter:
        from transformers import AutoModelForCausalLM, AutoTokenizer

        dtype = kwargs.pop("torch_dtype", torch.float16)
        tokenizer = AutoTokenizer.from_pretrained(
            model_name, trust_remote_code=True,
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=dtype,
            device_map=device,
            trust_remote_code=True,
            **kwargs,
        )
        cfg = model.config
        n_heads = cfg.num_attention_heads
        info = ModelInfo(
            arch=getattr(cfg, "model_type", "unknown"),
            n_layers=cfg.num_hidden_layers,
            n_heads=n_heads,
            n_kv_heads=getattr(cfg, "num_key_value_heads", n_heads),
            d_model=cfg.hidden_size,
            head_dim=cfg.hidden_size // n_heads,
            backend="huggingface",
            model_name=model_name,
        )
        return cls(model, info, tokenizer=tokenizer)

    # ---- Hook point mapping ----

    def get_hook_points(self) -> Dict[str, str]:
        """Return {canonical_name: actual_module_path} for all hookable nodes.

        For HF models with GQA (n_kv_heads < n_heads), k_proj/v_proj are shared
        across query heads in the same KV group.  The canonical name still uses
        per-query-head indexing; the module path is the same for all heads in a group.
        """
        if self.info.backend == "transformerlens":
            return self._tl_hooks()
        return self._hf_hooks()

    def _tl_hooks(self) -> Dict[str, str]:
        hp: Dict[str, str] = {"input": "hook_embed", "logits": "ln_final"}
        for L in range(self.info.n_layers):
            for H in range(self.info.n_heads):
                hp[f"a{L}.h{H}"] = f"blocks.{L}.attn.hook_result"
                for qkv in "qkv":
                    hp[f"a{L}.h{H}.{qkv}"] = f"blocks.{L}.attn.hook_{qkv}"
            hp[f"m{L}"] = f"blocks.{L}.hook_mlp_out"
        return hp

    def _hf_hooks(self) -> Dict[str, str]:
        """Hook points for Llama-like HF models (Qwen2, Llama, Mistral, ...).

        EAP-IG needs forward + backward hooks at these points.
        Edge Pruning needs to insert masks between these modules.
        IFR uses forward-only hooks (already handled by ifr_scoring.py).

        Qwen-2.5 0.5B specifics (24L, 14H, 2KV):
          - model.layers.{i}.self_attn uses SDPA with RoPE
          - GQA: 14 query heads, 2 KV heads → 7 queries per KV group
          - q_proj: [896, 896]  (14 heads × 64 dim)
          - k_proj: [896, 128]  (2 KV heads × 64 dim)
          - v_proj: [896, 128]  (2 KV heads × 64 dim)
          - o_proj: [896, 896]
          - mlp: gate_proj [896, 4864], up_proj [896, 4864], down_proj [4864, 896]
        """
        hp: Dict[str, str] = {
            "input": "model.embed_tokens",
            "logits": "lm_head",
        }
        for L in range(self.info.n_layers):
            hp[f"resid_pre.{L}"] = f"model.layers.{L}"
            for H in range(self.info.n_heads):
                hp[f"a{L}.h{H}"] = f"model.layers.{L}.self_attn.o_proj"
                hp[f"a{L}.h{H}.q"] = f"model.layers.{L}.self_attn.q_proj"
                hp[f"a{L}.h{H}.k"] = f"model.layers.{L}.self_attn.k_proj"
                hp[f"a{L}.h{H}.v"] = f"model.layers.{L}.self_attn.v_proj"
            hp[f"m{L}"] = f"model.layers.{L}.mlp"
        return hp

    # ---- Canonical name conversion ----

    def canonical_node_name(self, module_path: str) -> str:
        if self.info.backend == "transformerlens":
            return _tl_to_canonical(module_path)
        return _hf_to_canonical(module_path)

    def to_canonical_edges(
        self, edge_scores: Dict[str, float], method: str,
    ) -> Dict[str, float]:
        """Convert method-specific edge names to canonical format.

        IFR from ifr_scoring.py already outputs canonical format.
        TL-based methods use "blocks.{L}..." format and need conversion.
        """
        if method == "ifr" and self.info.backend == "huggingface":
            return edge_scores
        if self.info.backend == "transformerlens":
            return _tl_edges_to_canonical(edge_scores)
        return edge_scores

    # ---- Edge topology ----

    def n_possible_edges(self) -> int:
        """Total edges in the full computational graph (attention + MLP)."""
        L, H = self.info.n_layers, self.info.n_heads
        comps_per_layer = H + 1  # H attn heads + 1 MLP
        attn_edges = sum((1 + l * comps_per_layer) * H * 3 for l in range(L))
        mlp_edges = sum(1 + l * comps_per_layer + H for l in range(L))
        return attn_edges + mlp_edges

    def gqa_kv_group(self, query_head: int) -> int:
        """Map query head index to its KV group index (for GQA models)."""
        if self.info.n_kv_heads == self.info.n_heads:
            return query_head
        heads_per_group = self.info.n_heads // self.info.n_kv_heads
        return query_head // heads_per_group


# ---------------------------------------------------------------------------
# Qwen-2.5 0.5B architecture reference
# ---------------------------------------------------------------------------
#
# | Property             | Value                              |
# |----------------------|------------------------------------|
# | model_type           | qwen2                              |
# | num_hidden_layers    | 24                                 |
# | num_attention_heads  | 14                                 |
# | num_key_value_heads  | 2  (GQA: 7 queries per KV group)  |
# | hidden_size          | 896                                |
# | head_dim             | 64                                 |
# | intermediate_size    | 4864                               |
# | vocab_size           | 151936                             |
# | max_position_embeddings | 32768 (RoPE)                   |
#
# Canonical node mapping for Qwen-2.5 0.5B:
#
# | Canonical        | HuggingFace module path                       | Note             |
# |------------------|-----------------------------------------------|------------------|
# | input            | model.embed_tokens                            |                  |
# | a{L}.h{H}       | model.layers.{L}.self_attn.o_proj (head H)    | per-head via decomposition |
# | a{L}.h{H}.q     | model.layers.{L}.self_attn.q_proj (head H)    | slice [H*64:(H+1)*64] |
# | a{L}.h{H}.k     | model.layers.{L}.self_attn.k_proj (KV group)  | GQA: H//7 maps to KV head |
# | a{L}.h{H}.v     | model.layers.{L}.self_attn.v_proj (KV group)  | GQA: H//7 maps to KV head |
# | m{L}            | model.layers.{L}.mlp                          |                  |
# | logits           | lm_head                                       |                  |
#
# EAP-IG hook registration for Qwen-2.5:
#   Forward hooks:  model.layers.{i} (pre-hook for resid_pre)
#                   model.layers.{i}.self_attn.o_proj (attn output, decompose per head)
#                   model.layers.{i}.mlp (MLP output)
#   Backward hooks: same modules, for gradient-based attribution
#
# Edge Pruning hook registration for Qwen-2.5:
#   Mask insertion points:
#     - Between embedding and first layer input
#     - Between each layer's output and next layer's input (residual connections)
#   Requires custom masked forward pass (analogous to edge_pruning_l0._masked_forward
#   but operating on HF module structure instead of TL blocks).
#   Key difference from GPT-2: GQA means K/V masks are shared across query groups.
