"""Cross-method Stability Scoring (CSS).
Computes per-edge consensus across K independent circuit discovery methods.
CSS(edge) = (number of methods selecting edge) / K, taking values in {0, 1/K, ..., 1}.
"""

from typing import Dict, Set


def compute_css(
    method_circuits: Dict[str, Set[str]],
    K: int,
) -> Dict[str, float]:
    """Compute CSS scores from K methods' binary edge sets.

    Args:
        method_circuits: method_name -> set of selected edge names
        K: total number of methods (used as denominator)

    Returns:
        edge_name -> CSS score in {0, 1/K, 2/K, ..., 1}
    """
    all_edges: Set[str] = set()
    for edges in method_circuits.values():
        all_edges |= edges

    css_scores = {}
    for edge in all_edges:
        count = sum(1 for edges in method_circuits.values() if edge in edges)
        css_scores[edge] = count / K

    return css_scores


def threshold_css(
    css_scores: Dict[str, float],
    threshold: float = 0.67,
) -> Set[str]:
    """Select edges meeting CSS threshold.

    Threshold is snapped to nearest n/K level to avoid floating point issues
    (e.g. threshold=0.67 matches CSS=2/3=0.6666...).

    Args:
        css_scores: edge_name -> CSS score
        threshold: minimum CSS to include (default 0.67 = 2/3 for K=3)

    Returns:
        Set of edge names with CSS >= threshold
    """
    eps = 0.01
    return {edge for edge, score in css_scores.items() if score >= threshold - eps}


def binarize_scores(
    edge_scores: Dict[str, float],
    method: str = "eap_ig",
    top_n: int = 100,
) -> Set[str]:
    """Convert edge scores to binary circuit using method-appropriate strategy.

    - EAP-IG: continuous attribution scores → top-N by absolute value
    - Edge Pruning: L0 mask values in [0,1] → threshold at 0.5
    - ACDC: binary inclusion (0 or 1) → select all non-zero edges

    Args:
        edge_scores: edge_name -> score (interpretation depends on method)
        method: "eap_ig" | "edge_pruning" | "acdc"
        top_n: number of top edges (only used for eap_ig)

    Returns:
        Set of selected edge names
    """
    if method == "acdc":
        return {edge for edge, score in edge_scores.items() if score > 0}
    elif method == "edge_pruning":
        return {edge for edge, score in edge_scores.items() if score > 0.5}
    elif method == "ifr":
        sorted_edges = sorted(edge_scores.items(), key=lambda x: abs(x[1]), reverse=True)
        return {edge for edge, _ in sorted_edges[:top_n]}
    else:
        sorted_edges = sorted(edge_scores.items(), key=lambda x: abs(x[1]), reverse=True)
        return {edge for edge, _ in sorted_edges[:top_n]}


def css_summary(css_scores: Dict[str, float], K: int) -> Dict[str, int]:
    """Count edges at each CSS level.

    Returns:
        Dict mapping CSS level string to count, e.g. {"0/3": 50, "1/3": 30, "2/3": 15, "3/3": 5}
    """
    from collections import Counter
    level_counts = Counter()
    for score in css_scores.values():
        n_methods = round(score * K)
        level_counts[f"{n_methods}/{K}"] += 1
    return dict(sorted(level_counts.items()))
