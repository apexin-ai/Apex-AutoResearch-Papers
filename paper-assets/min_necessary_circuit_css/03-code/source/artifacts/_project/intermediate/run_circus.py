"""StructFuse configurable pipeline: multi-method circuit discovery + CSS consensus.

Config-driven entry point that supports both GPT-2 (TransformerLens) and
Qwen-2.5 / Llama-like (HuggingFace) models.  Replaces the MVP's hardcoded
run_mvp.py with a general K-method pipeline.

Usage:
    python run_circus.py                       # default config (Qwen-2.5 0.5B / IOI / K=3)
    python run_circus.py config.json           # custom config
    python run_circus.py config.yaml           # YAML config
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Set

import torch

from model_adapter import CANONICAL_VERSION, ModelAdapter


# ---------------------------------------------------------------------------
# Default configuration
# ---------------------------------------------------------------------------

DEFAULT_CONFIG: Dict[str, Any] = {
    "model": "Qwen/Qwen2.5-0.5B",
    "task": "ioi",
    "methods": ["eap_ig", "edge_pruning", "ifr"],
    "K": 3,
    "num_samples": 50,
    "binarize": {
        "eap_ig":       {"strategy": "topn", "n": 200},
        "edge_pruning": {"strategy": "threshold", "value": 0.5},
        "ifr":          {"strategy": "topn", "n": 200},
    },
    "eap_ig_steps": 5,
    "edge_pruning_epochs": 100,
    "edge_pruning_lambda": 1e-2,
    "ifr_threshold": 0.1,
    "css_threshold": 0.67,
    "circus_B": 10,
    "circus_core_threshold": 1.0,
    "circus_contingent_threshold": 0.5,
    "device": "cuda",
    "seed": 42,
    "output_dir": "./results",
    "cache_dir": "./cache",
}


# ---------------------------------------------------------------------------
# Dataset loading
# ---------------------------------------------------------------------------

def load_dataset(
    task: str, tokenizer, num_samples: int, device: str,
) -> torch.Tensor:
    if task == "ioi":
        return _make_ioi_dataset(tokenizer, num_samples, device)
    if task == "greater_than":
        return _make_greater_than_dataset(tokenizer, num_samples, device)
    raise ValueError(f"Unknown task: {task}")


def _make_ioi_dataset(tokenizer, n: int, device: str) -> torch.Tensor:
    names = [
        "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank",
        "Grace", "Henry", "Iris", "Jack", "Kate", "Leo",
    ]
    import random
    rng = random.Random(42)
    sentences = []
    for _ in range(n):
        n1, n2 = rng.sample(names, 2)
        sentences.append(
            f"When {n1} and {n2} went to the store, {n1} gave a drink to"
        )
    enc = tokenizer(sentences, return_tensors="pt", padding=True)
    return enc["input_ids"].to(device)


def _make_greater_than_dataset(tokenizer, n: int, device: str) -> torch.Tensor:
    import random
    rng = random.Random(42)
    sentences = []
    for _ in range(n):
        year = rng.randint(1000, 1999)
        sentences.append(f"The war lasted from the year {year} to the year")
    enc = tokenizer(sentences, return_tensors="pt", padding=True)
    return enc["input_ids"].to(device)


# ---------------------------------------------------------------------------
# Method dispatch
# ---------------------------------------------------------------------------

def _mvp_sys_path():
    """Add structfuse-mvp/ to sys.path for TL-based method imports."""
    mvp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "structfuse-mvp")
    if mvp_dir not in sys.path:
        sys.path.insert(0, mvp_dir)


def _run_ifr_hf(
    adapter: ModelAdapter, dataset: torch.Tensor, cfg: dict,
) -> Dict[str, float]:
    from ifr_scoring import compute_ifr_edges
    return compute_ifr_edges(
        adapter.model,
        dataset,
        metric_fn=None,
        threshold=cfg.get("ifr_threshold", 0.1),
        device=cfg.get("device", "cuda"),
    )


def _run_ifr_tl(
    adapter: ModelAdapter, dataset: torch.Tensor, cfg: dict,
) -> Dict[str, float]:
    _mvp_sys_path()
    from ifr_discovery import run_ifr
    return run_ifr(adapter.model, dataset)


def _run_eap_ig_tl(
    adapter: ModelAdapter,
    dataset: torch.Tensor,
    metric: Callable,
    cfg: dict,
) -> Dict[str, float]:
    _mvp_sys_path()
    from circuit_discovery import run_eap_ig
    from config import MVPConfig
    mvp_cfg = MVPConfig(eap_ig_steps=cfg.get("eap_ig_steps", 5))
    return run_eap_ig(adapter.model, dataset, metric, config=mvp_cfg)


def _run_eap_ig_hf(
    adapter: ModelAdapter,
    dataset: torch.Tensor,
    metric: Callable,
    cfg: dict,
) -> Dict[str, float]:
    """EAP-IG on HuggingFace model (Qwen-2.5, Llama, ...).

    Hook registration points:
      Forward:  model.embed_tokens (embedding output)
                model.layers.{i} (pre-hook → resid_pre)
                model.layers.{i}.self_attn.o_proj (attn output, decompose per head)
                model.layers.{i}.mlp (MLP output)
      Backward: same modules, for integrated gradients

    IG procedure:
      1. Compute baseline embedding (zero or mean ablation)
      2. Interpolate alpha in [0,1] over ig_steps
      3. For each alpha: forward + backward, accumulate gradients × (input - baseline)
      4. Score each edge as |accumulated_gradient| averaged over dataset
    """
    raise NotImplementedError(
        "EAP-IG HF backend not yet implemented. "
        "See docstring for hook registration points."
    )


def _run_edge_pruning_tl(
    adapter: ModelAdapter,
    dataset: torch.Tensor,
    metric: Callable,
    cfg: dict,
) -> Dict[str, float]:
    _mvp_sys_path()
    from edge_pruning_l0 import run_edge_pruning_l0
    return run_edge_pruning_l0(
        adapter.model,
        dataset,
        metric,
        n_epochs=cfg.get("edge_pruning_epochs", 100),
        lambda_l0=cfg.get("edge_pruning_lambda", 1e-2),
    )


def _run_edge_pruning_hf(
    adapter: ModelAdapter,
    dataset: torch.Tensor,
    metric: Callable,
    cfg: dict,
) -> Dict[str, float]:
    """Edge Pruning L0 on HuggingFace model (Qwen-2.5, Llama, ...).

    Requires a custom masked forward pass operating on HF modules:
      - Reconstruct residual inputs as masked sums of upstream component outputs
      - Apply Hard Concrete masks per edge
      - Key modules to intercept:
          model.layers.{i}.input_layernorm  (pre-attn LN)
          model.layers.{i}.self_attn        (full attn block)
          model.layers.{i}.post_attention_layernorm (pre-MLP LN)
          model.layers.{i}.mlp              (full MLP block)

    GQA consideration: K/V edge masks are shared across the query heads
    within each KV group (7 query heads per KV group for Qwen-2.5 0.5B).
    """
    raise NotImplementedError(
        "Edge Pruning HF backend not yet implemented. "
        "See docstring for required adaptations."
    )


def run_method(
    adapter: ModelAdapter,
    method: str,
    dataset: torch.Tensor,
    metric: Optional[Callable],
    cfg: dict,
) -> Dict[str, float]:
    backend = adapter.info.backend
    dispatch = {
        ("ifr", "huggingface"):      lambda: _run_ifr_hf(adapter, dataset, cfg),
        ("ifr", "transformerlens"):   lambda: _run_ifr_tl(adapter, dataset, cfg),
        ("eap_ig", "huggingface"):    lambda: _run_eap_ig_hf(adapter, dataset, metric, cfg),
        ("eap_ig", "transformerlens"): lambda: _run_eap_ig_tl(adapter, dataset, metric, cfg),
        ("edge_pruning", "huggingface"):    lambda: _run_edge_pruning_hf(adapter, dataset, metric, cfg),
        ("edge_pruning", "transformerlens"): lambda: _run_edge_pruning_tl(adapter, dataset, metric, cfg),
    }
    key = (method, backend)
    if key not in dispatch:
        raise ValueError(f"No implementation for method={method}, backend={backend}")

    scores = dispatch[key]()
    return adapter.to_canonical_edges(scores, method)


# ---------------------------------------------------------------------------
# Caching (version-bound to prevent stale reads)
# ---------------------------------------------------------------------------

def _cache_key(cfg: dict, method: str) -> str:
    relevant: Dict[str, Any] = {
        "model": cfg["model"],
        "task": cfg["task"],
        "method": method,
        "canonical_version": CANONICAL_VERSION,
        "num_samples": cfg.get("num_samples", 50),
    }
    if method == "eap_ig":
        relevant["ig_steps"] = cfg.get("eap_ig_steps", 5)
    elif method == "edge_pruning":
        relevant["epochs"] = cfg.get("edge_pruning_epochs", 100)
        relevant["lambda"] = cfg.get("edge_pruning_lambda", 1e-2)
    elif method == "ifr":
        relevant["threshold"] = cfg.get("ifr_threshold", 0.1)
    return hashlib.sha256(json.dumps(relevant, sort_keys=True).encode()).hexdigest()[:16]


def _cache_path(cfg: dict, method: str) -> Path:
    cache_dir = Path(cfg.get("cache_dir", "./cache"))
    model_slug = cfg["model"].replace("/", "_")
    return (
        cache_dir / model_slug / cfg["task"]
        / f"{method}_{CANONICAL_VERSION}_{_cache_key(cfg, method)}.json"
    )


def load_cached(cfg: dict, method: str) -> Optional[Dict[str, float]]:
    path = _cache_path(cfg, method)
    if not path.exists():
        return None
    with open(path) as f:
        data = json.load(f)
    if data.get("canonical_version") != CANONICAL_VERSION:
        return None
    return data["scores"]


def save_cache(cfg: dict, method: str, scores: Dict[str, float]) -> None:
    path = _cache_path(cfg, method)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(
            {
                "canonical_version": CANONICAL_VERSION,
                "model": cfg["model"],
                "task": cfg["task"],
                "method": method,
                "n_edges": len(scores),
                "scores": scores,
            },
            f,
        )


# ---------------------------------------------------------------------------
# Binarization
# ---------------------------------------------------------------------------

def binarize(
    scores: Dict[str, float], method: str, cfg: dict,
) -> Set[str]:
    bconf = cfg.get("binarize", {}).get(method, {"strategy": "topn", "n": 200})
    strategy = bconf.get("strategy", "topn")

    if strategy == "topn":
        n = bconf.get("n", 200)
        ranked = sorted(scores.items(), key=lambda x: abs(x[1]), reverse=True)
        return {e for e, _ in ranked[:n]}
    if strategy == "threshold":
        val = bconf.get("value", 0.5)
        return {e for e, s in scores.items() if s > val}
    if strategy == "nonzero":
        return {e for e, s in scores.items() if s > 0}
    raise ValueError(f"Unknown binarize strategy: {strategy}")


# ---------------------------------------------------------------------------
# CSS (Cross-method Stability Scoring)
# ---------------------------------------------------------------------------

def compute_css(
    method_circuits: Dict[str, Set[str]], K: int,
) -> Dict[str, float]:
    all_edges: Set[str] = set()
    for edges in method_circuits.values():
        all_edges |= edges
    return {
        edge: sum(1 for edges in method_circuits.values() if edge in edges) / K
        for edge in all_edges
    }


def threshold_css(
    css_scores: Dict[str, float], threshold: float = 0.67,
) -> Set[str]:
    return {e for e, s in css_scores.items() if s >= threshold - 0.01}


def css_distribution(css_scores: Dict[str, float], K: int) -> Dict[str, int]:
    dist: Dict[str, int] = {}
    for s in css_scores.values():
        level = f"{round(s * K)}/{K}"
        dist[level] = dist.get(level, 0) + 1
    return dict(sorted(dist.items()))


# ---------------------------------------------------------------------------
# CIRCUS (config-bagging stability)
# ---------------------------------------------------------------------------

def config_bag(
    scores: Dict[str, float], B: int = 10,
) -> Dict[str, float]:
    if not scores:
        return {}
    import numpy as np
    vals = np.array(list(scores.values()))
    edges = list(scores.keys())
    percentiles = np.linspace(100 / (B + 1), 100 * B / (B + 1), B)
    thresholds = np.percentile(vals, percentiles)
    stability = sum((vals >= t).astype(float) for t in thresholds) / B
    return dict(zip(edges, stability.tolist()))


def classify_tiers(
    stability: Dict[str, float],
    core_thr: float = 1.0,
    contingent_thr: float = 0.5,
) -> Dict[str, str]:
    return {
        e: ("core" if s >= core_thr else "contingent" if s >= contingent_thr else "noise")
        for e, s in stability.items()
    }


# ---------------------------------------------------------------------------
# Cross-tabulation
# ---------------------------------------------------------------------------

def cross_tabulate(
    tiers: Dict[str, str],
    css_scores: Dict[str, float],
    css_thr: float,
) -> Dict[str, Any]:
    all_edges = set(tiers.keys()) | set(css_scores.keys())
    stable_core: Set[str] = set()
    method_specific: Set[str] = set()
    cross_unstable: Set[str] = set()
    noise: Set[str] = set()

    for e in all_edges:
        is_core = tiers.get(e) == "core"
        is_high = css_scores.get(e, 0.0) >= css_thr - 0.01
        if is_core and is_high:
            stable_core.add(e)
        elif is_core:
            method_specific.add(e)
        elif is_high:
            cross_unstable.add(e)
        else:
            noise.add(e)

    core_total = len(stable_core) + len(method_specific)
    off_diag = len(method_specific) / core_total if core_total > 0 else 0.0

    return {
        "stable_core": len(stable_core),
        "method_specific": len(method_specific),
        "cross_unstable": len(cross_unstable),
        "noise": len(noise),
        "core_total": core_total,
        "off_diagonal_pct": round(off_diag, 4),
        "stable_core_edges": stable_core,
        "method_specific_edges": method_specific,
    }


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run_pipeline(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    cfg = {**DEFAULT_CONFIG, **(config or {})}

    torch.manual_seed(cfg["seed"])

    print(f"StructFuse: model={cfg['model']}, task={cfg['task']}, K={cfg['K']}")
    print(f"Methods: {cfg['methods']}, canonical={CANONICAL_VERSION}")

    # 1. Load model
    adapter = ModelAdapter.from_pretrained(cfg["model"], device=cfg["device"])
    info = adapter.info
    n_edges = adapter.n_possible_edges()
    print(
        f"Model: {info.model_name} ({info.backend}) — "
        f"{info.n_layers}L × {info.n_heads}H"
        f" (KV={info.n_kv_heads})" * (info.n_kv_heads != info.n_heads)
        + f", d={info.d_model}, ~{n_edges:,} possible edges"
    )

    # 2. Load dataset
    dataset = load_dataset(
        cfg["task"], adapter.tokenizer,
        cfg.get("num_samples", 50), cfg["device"],
    )
    print(f"Dataset: {cfg['task']}, {dataset.shape[0]} samples, seq_len={dataset.shape[1]}")

    # 3. Run methods (with caching)
    all_scores: Dict[str, Dict[str, float]] = {}
    timings: Dict[str, float] = {}

    for method in cfg["methods"]:
        cached = load_cached(cfg, method)
        if cached is not None:
            print(f"  {method}: cache hit ({len(cached)} edges)")
            all_scores[method] = cached
            timings[method] = 0.0
            continue

        print(f"  {method}: running...")
        t0 = time.time()
        scores = run_method(adapter, method, dataset, None, cfg)
        elapsed = time.time() - t0
        print(f"  {method}: {len(scores)} edges ({elapsed:.1f}s)")

        save_cache(cfg, method, scores)
        all_scores[method] = scores
        timings[method] = elapsed

    # 4. Binarize
    circuits: Dict[str, Set[str]] = {}
    for method, scores in all_scores.items():
        circuits[method] = binarize(scores, method, cfg)
        print(f"  {method}: {len(circuits[method])} edges selected")

    # 5. CSS
    css = compute_css(circuits, cfg["K"])
    dist = css_distribution(css, cfg["K"])
    print(f"CSS distribution: {dist}")

    css_circuit = threshold_css(css, cfg["css_threshold"])
    print(f"CSS circuit (>= {cfg['css_threshold']}): {len(css_circuit)} edges")

    # 6. CIRCUS on primary method
    primary = cfg["methods"][0]
    stability = config_bag(all_scores[primary], cfg["circus_B"])
    tiers = classify_tiers(
        stability,
        cfg["circus_core_threshold"],
        cfg["circus_contingent_threshold"],
    )
    tier_counts = {
        t: sum(1 for v in tiers.values() if v == t)
        for t in ("core", "contingent", "noise")
    }
    print(f"CIRCUS tiers ({primary}): {tier_counts}")

    # 7. Cross-tabulation
    xtab = cross_tabulate(tiers, css, cfg["css_threshold"])
    print(
        f"Cross-table: stable_core={xtab['stable_core']}, "
        f"method_specific={xtab['method_specific']}, "
        f"cross_unstable={xtab['cross_unstable']}, noise={xtab['noise']}"
    )
    print(f"Off-diagonal %: {xtab['off_diagonal_pct'] * 100:.1f}%")

    # 8. Save results
    result = {
        "config": {
            "model": cfg["model"],
            "task": cfg["task"],
            "K": cfg["K"],
            "methods": cfg["methods"],
            "canonical_version": CANONICAL_VERSION,
            "num_samples": cfg.get("num_samples", 50),
        },
        "timings_sec": timings,
        "method_edge_counts": {m: len(s) for m, s in all_scores.items()},
        "binarized_counts": {m: len(c) for m, c in circuits.items()},
        "css_distribution": dist,
        "css_circuit_size": len(css_circuit),
        "circus_tiers": tier_counts,
        "cross_table": {
            k: v for k, v in xtab.items()
            if k not in ("stable_core_edges", "method_specific_edges")
        },
    }

    output_dir = Path(cfg["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    model_slug = cfg["model"].replace("/", "_")
    output_path = output_dir / f"{model_slug}_{cfg['task']}_K{cfg['K']}.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nResults → {output_path}")

    return result


# ---------------------------------------------------------------------------
# CLI entry
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    config_override = None
    if len(sys.argv) > 1:
        p = sys.argv[1]
        with open(p) as f:
            if p.endswith((".yaml", ".yml")):
                import yaml
                config_override = yaml.safe_load(f)
            else:
                config_override = json.load(f)
    run_pipeline(config_override)
