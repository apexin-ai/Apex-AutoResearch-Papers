"""
CSS (Cross-method Stability Scoring) binarization and consensus module.

Provides multiple binarization strategies for converting continuous edge scores
to binary circuit membership, then computes cross-method consensus.

D010: IFR proximity scores are identical for all heads in the same (src, dst_layer).
Top-N binarization causes block-voting. Use percentile_threshold or unique_score_rank
to handle tied scores fairly.
"""

from typing import Dict, List, Literal, Tuple
import numpy as np

BinarizeStrategy = Literal["topn", "threshold", "percentile_threshold", "unique_score_rank"]


def generate_nonnested_configs(
    node_thresholds: List[float],
    edge_thresholds: List[float],
    B: int = 9,
    seed: int = 42,
) -> List[Tuple[float, float]]:
    """Generate B non-nested (anti-chain) configurations from 2D threshold space.

    Anti-chain constraint: for any (n_i, e_i), (n_j, e_j),
    NOT (n_i <= n_j AND e_i <= e_j) — no dominance relation.

    Method: interpolate B values per axis within the provided ranges,
    then select the anti-diagonal (node ascending, edge descending).
    This guarantees pairwise incomparability.
    """
    n_lo, n_hi = min(node_thresholds), max(node_thresholds)
    e_lo, e_hi = min(edge_thresholds), max(edge_thresholds)

    n_vals = np.linspace(n_lo, n_hi, B)
    e_vals = np.linspace(e_lo, e_hi, B)

    return [(float(n_vals[i]), float(e_vals[B - 1 - i])) for i in range(B)]


def binarize_scores(
    scores: Dict[str, float],
    strategy: BinarizeStrategy,
    *,
    n: int = 200,
    threshold: float = 0.01,
    percentile: float = 95.0,
) -> set[str]:
    """Convert continuous edge scores to binary set of 'active' edges.

    Strategies:
    - topn: select top-N edges by score. Simple but biased when scores are tied (IFR problem).
    - threshold: select edges above absolute threshold. Method-dependent.
    - percentile_threshold: select edges above P-th percentile of unique score values.
      Handles IFR ties: 36 heads with same score count as 1 unique value for percentile calc,
      then all 36 are included if above threshold. Avoids block-vote quota stealing.
    - unique_score_rank: rank by unique score values, select top-N unique scores,
      then include ALL edges with those scores. Ensures tied edges are treated as one unit.
    """
    if not scores:
        return set()

    if strategy == "topn":
        sorted_edges = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return {edge for edge, _ in sorted_edges[:n]}

    elif strategy == "threshold":
        return {edge for edge, score in scores.items() if score >= threshold}

    elif strategy == "percentile_threshold":
        unique_scores = sorted(set(scores.values()))
        cutoff_idx = int(len(unique_scores) * percentile / 100)
        cutoff_value = unique_scores[cutoff_idx] if cutoff_idx < len(unique_scores) else unique_scores[-1]
        return {edge for edge, score in scores.items() if score >= cutoff_value}

    elif strategy == "unique_score_rank":
        unique_scores = sorted(set(scores.values()), reverse=True)
        top_n_scores = set(unique_scores[:n])
        return {edge for edge, score in scores.items() if score in top_n_scores}

    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def compute_css_matrix(
    method_circuits: Dict[str, set[str]],
    all_edges: set[str],
) -> Dict:
    """Compute cross-method stability matrix (cross-tabulation).

    For K methods, each edge falls into one of 2^K cells:
    - (1,1,1): all methods agree edge is in circuit (CSS-core)
    - (1,0,0): only method 1 includes it (method-specific)
    - (0,0,0): no method includes it
    - etc.

    Returns dict with:
    - 'cell_counts': {cell_label: count}
    - 'css_core': set of edges in all-1 cell
    - 'off_diagonal': set of edges where methods disagree (not all-0 or all-1)
    - 'off_diagonal_pct': off_diagonal count / total edges with at least one 1
    - 'per_method_counts': {method: n_edges}
    """
    methods = sorted(method_circuits.keys())
    k = len(methods)

    cell_counts: Dict[str, int] = {}
    css_core: set[str] = set()
    off_diagonal: set[str] = set()

    all_zeros = tuple(0 for _ in range(k))
    all_ones = tuple(1 for _ in range(k))

    for edge in all_edges:
        cell = tuple(1 if edge in method_circuits[m] else 0 for m in methods)
        label = str(cell)
        cell_counts[label] = cell_counts.get(label, 0) + 1

        if cell == all_ones:
            css_core.add(edge)
        elif cell != all_zeros:
            off_diagonal.add(edge)

    at_least_one = len(css_core) + len(off_diagonal)
    off_diagonal_pct = len(off_diagonal) / at_least_one if at_least_one > 0 else 0.0

    per_method_counts = {m: len(method_circuits[m]) for m in methods}

    return {
        "cell_counts": cell_counts,
        "css_core": css_core,
        "off_diagonal": off_diagonal,
        "off_diagonal_pct": off_diagonal_pct,
        "per_method_counts": per_method_counts,
    }


def circus_score(
    method_circuits: Dict[str, set[str]],
    edge: str,
) -> float:
    """CIRCUS score for a single edge: fraction of methods that include it.

    score = |{m : edge in C_m}| / K
    """
    k = len(method_circuits)
    if k == 0:
        return 0.0
    count = sum(1 for c in method_circuits.values() if edge in c)
    return count / k
