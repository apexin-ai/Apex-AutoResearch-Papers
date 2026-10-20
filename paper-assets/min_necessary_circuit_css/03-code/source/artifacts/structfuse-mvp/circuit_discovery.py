"""Unified circuit discovery interface for K=3 methods.
Each method returns Dict[str, float] mapping edge_name -> attribution_score.
Edge names are normalized to TransformerLens format: "blocks.{L}.attn.hook_result[{H}] -> blocks.{L'}.attn.hook_q[{H'}]"
"""

import re
from typing import Dict, Callable, Optional

from config import MVPConfig, MVP_CONFIG


# --- Edge name normalization ---

def _normalize_eap_edge(edge_str: str) -> str:
    """EAP uses Graph node naming close to TransformerLens. Minimal normalization needed."""
    # EAP format: "blocks.0.attn.hook_result[0] -> blocks.1.attn.hook_q[1]"
    # Already close to TL standard; strip whitespace and ensure consistent spacing
    return edge_str.strip()


def _normalize_edge_pruning_edge(edge_str: str) -> str:
    """Edge Pruning L0 outputs TransformerLens-format names directly."""
    return edge_str.strip()


def _normalize_acdc_edge(edge_str: str) -> str:
    """Auto-Circuit/ACDC edge naming normalization."""
    # Auto-Circuit typically uses TL-compatible naming already
    return edge_str.strip()


def _normalize_ifr_edge(edge_str: str) -> str:
    """IFR outputs TL-format edge names directly; no normalization needed."""
    return edge_str.strip()


_NORMALIZERS = {
    "eap_ig": _normalize_eap_edge,
    "edge_pruning": _normalize_edge_pruning_edge,
    "acdc": _normalize_acdc_edge,
    "ifr": _normalize_ifr_edge,
}


def normalize_edge_names(scores: Dict[str, float], method: str) -> Dict[str, float]:
    """Normalize edge names from method-specific format to TransformerLens standard."""
    normalizer = _NORMALIZERS.get(method, lambda x: x)
    return {normalizer(k): v for k, v in scores.items()}


# --- Method implementations ---

def run_eap_ig(
    model,
    dataset,
    metric: Callable,
    ig_steps: int = 5,
    config: MVPConfig = MVP_CONFIG,
) -> Dict[str, float]:
    """Run EAP-IG attribution and return edge scores.

    Args:
        model: HookedTransformer instance
        dataset: IOI dataset or EAPDataset-compatible
        metric: loss/logit-diff metric function
        ig_steps: integrated gradients interpolation steps

    Returns:
        Dict mapping normalized edge names to attribution scores
    """
    from eap import Graph, attribute

    graph = Graph.from_model(model)

    # TODO: wrap dataset into EAPDataset format if needed
    # dataloader = EAPDataset('ioi').to_dataloader()
    dataloader = dataset  # placeholder — adapt to EAPDataset API

    attribute(
        model, graph, dataloader, metric,
        method="EAP-IG-inputs",
        ig_steps=ig_steps,
    )

    raw_scores = {}
    for edge in graph.edges:
        raw_scores[str(edge)] = float(edge.score)

    return normalize_edge_names(raw_scores, "eap_ig")


def run_edge_pruning(
    model,
    dataset,
    metric: Callable,
    target_sparsity: float = 0.05,
    config: MVPConfig = MVP_CONFIG,
) -> Dict[str, float]:
    """Run Edge Pruning with L0 mask optimization.

    Uses Hard Concrete relaxation (Louizos et al. 2018) to optimize continuous
    edge masks. Finds the minimal circuit preserving task performance.

    Args:
        model: HookedTransformer instance
        dataset: IOI dataset
        metric: callable(logits) -> scalar, higher = better
        target_sparsity: fraction of edges to retain

    Returns:
        Dict mapping normalized edge names to mask scores (0-1)
    """
    from edge_pruning_l0 import run_edge_pruning_l0

    raw_scores = run_edge_pruning_l0(
        model, dataset, metric,
        target_sparsity=target_sparsity,
    )

    return normalize_edge_names(raw_scores, "edge_pruning")


def run_acdc(
    model,
    dataset,
    metric: Callable,
    threshold: float = 0.05,
    config: MVPConfig = MVP_CONFIG,
) -> Dict[str, float]:
    """Run ACDC via auto_circuit library.

    Args:
        model: HookedTransformer instance
        dataset: IOI dataset
        metric: loss/logit-diff metric function
        threshold: ACDC edge inclusion threshold

    Returns:
        Dict mapping normalized edge names to binary scores (0 or 1)
    """
    # TODO: auto_circuit API integration
    # from auto_circuit.experiment_utils import load_tl_model
    # from auto_circuit.prune_algos.ACDC import acdc_prune_scores
    # from auto_circuit.types import PruneScores
    #
    # prune_scores: PruneScores = acdc_prune_scores(
    #     model=model,
    #     dataloader=dataset,
    #     official_edges=None,
    #     tao_exps=[-2],  # threshold
    # )
    # Convert PruneScores (nested dict of tensors) to flat edge dict

    raw_scores: Dict[str, float] = {}

    return normalize_edge_names(raw_scores, "acdc")


def run_all_methods(
    model,
    dataset,
    metric: Callable,
    config: MVPConfig = MVP_CONFIG,
) -> Dict[str, Dict[str, float]]:
    """Run all K methods and return their edge scores.

    Returns:
        Dict mapping method_name -> {edge_name: score}
    """
    from ifr_discovery import run_ifr

    runners = {
        "eap_ig": lambda: run_eap_ig(model, dataset, metric, config.eap_ig_steps, config),
        "edge_pruning": lambda: run_edge_pruning(model, dataset, metric, config.edge_pruning_target_sparsity, config),
        "acdc": lambda: run_acdc(model, dataset, metric, config.acdc_threshold, config),
        "ifr": lambda: run_ifr(model, dataset, metric),
    }

    results = {}
    for method in config.methods:
        print(f"Running {method}...")
        results[method] = runners[method]()
        print(f"  {method}: {len(results[method])} edges scored")

    return results
