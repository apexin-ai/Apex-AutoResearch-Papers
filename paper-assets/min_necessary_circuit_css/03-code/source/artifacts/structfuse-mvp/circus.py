"""CIRCUS config-bagging: stability analysis via multi-threshold binarization.
Applied to a single method's continuous edge scores (EAP-IG in MVP).
Produces core/contingent/noise tier classification.
"""

from typing import Dict, List, Set, Tuple
import numpy as np

from config import MVPConfig, MVP_CONFIG


def config_bag(
    edge_scores: Dict[str, float],
    B: int = 10,
) -> Dict[str, float]:
    """Multi-threshold config-bagging for stability scoring.

    Binarize edge scores at B evenly-spaced thresholds, then compute
    the fraction of thresholds at which each edge is included.

    Args:
        edge_scores: edge_name -> continuous attribution score
        B: number of threshold bins

    Returns:
        edge_name -> stability score in [0, 1]
        (1.0 = included at all thresholds, 0.0 = never included)
    """
    if not edge_scores:
        return {}

    scores = np.array(list(edge_scores.values()))
    edges = list(edge_scores.keys())

    # B evenly-spaced thresholds from min to max (exclusive of 0-percentile to avoid all-in)
    percentiles = np.linspace(100 / (B + 1), 100 * B / (B + 1), B)
    thresholds = np.percentile(scores, percentiles)

    stability = np.zeros(len(edges))
    for thresh in thresholds:
        stability += (scores >= thresh).astype(float)
    stability /= B

    return {edge: float(stab) for edge, stab in zip(edges, stability)}


def get_circus_tiers(
    stability_scores: Dict[str, float],
    core_threshold: float = 1.0,
    contingent_threshold: float = 0.5,
) -> Dict[str, str]:
    """Classify edges into core/contingent/noise tiers.

    Args:
        stability_scores: edge_name -> stability score from config_bag
        core_threshold: minimum stability for core tier (default: 1.0 = all thresholds)
        contingent_threshold: minimum stability for contingent tier

    Returns:
        edge_name -> tier label ("core" | "contingent" | "noise")
    """
    tiers = {}
    for edge, score in stability_scores.items():
        if score >= core_threshold:
            tiers[edge] = "core"
        elif score >= contingent_threshold:
            tiers[edge] = "contingent"
        else:
            tiers[edge] = "noise"
    return tiers


def get_tier_sets(tiers: Dict[str, str]) -> Dict[str, Set[str]]:
    """Group edges by tier into sets.

    Returns:
        Dict with keys "core", "contingent", "noise" -> Set of edge names
    """
    result: Dict[str, Set[str]] = {"core": set(), "contingent": set(), "noise": set()}
    for edge, tier in tiers.items():
        result[tier].add(edge)
    return result


def run_circus(
    edge_scores: Dict[str, float],
    config: MVPConfig = MVP_CONFIG,
) -> Tuple[Dict[str, float], Dict[str, str]]:
    """Full CIRCUS pipeline: config-bagging -> tier classification.

    Args:
        edge_scores: continuous edge scores from one method (EAP-IG)
        config: experiment config

    Returns:
        (stability_scores, tiers) tuple
    """
    stability = config_bag(edge_scores, B=config.circus_B)
    tiers = get_circus_tiers(
        stability,
        core_threshold=config.circus_core_threshold,
        contingent_threshold=config.circus_contingent_threshold,
    )

    tier_counts = {}
    for t in ["core", "contingent", "noise"]:
        tier_counts[t] = sum(1 for v in tiers.values() if v == t)
    print(f"CIRCUS tiers: {tier_counts}")

    return stability, tiers
