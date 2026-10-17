"""Graph construction and greedy coloring for type decomposition.

Input: Similarity matrix, threshold tau, type names
Output: Type batches via graph coloring (NetworkX)
Dependencies: torch, networkx
"""
import logging
from typing import Dict, List

import networkx as nx
import torch

logger = logging.getLogger(__name__)


def build_threshold_graph(
    sim_matrix: torch.Tensor,
    tau: float,
    type_names: List[str],
) -> nx.Graph:
    """Build undirected graph where edges connect types with similarity > tau.

    Args:
        sim_matrix: [N, N] pairwise similarity matrix
        tau: threshold — pairs with sim > tau get an edge
        type_names: list of type names (length N)

    Returns:
        NetworkX Graph with type names as nodes
    """
    n = len(type_names)
    G = nx.Graph()
    G.add_nodes_from(type_names)

    n_edges = 0
    for i in range(n):
        for j in range(i + 1, n):
            if sim_matrix[i, j].item() > tau:
                G.add_edge(type_names[i], type_names[j], weight=sim_matrix[i, j].item())
                n_edges += 1

    logger.info("Threshold graph: %d nodes, %d edges (tau=%.4f)", n, n_edges, tau)
    return G


def color_graph(G: nx.Graph, strategy: str = "largest_first") -> Dict[str, int]:
    """Greedy graph coloring — confusable types get different colors (batches).

    Args:
        G: NetworkX graph
        strategy: coloring strategy (default largest_first)

    Returns:
        Dict mapping type_name -> color_id
    """
    coloring = nx.coloring.greedy_color(G, strategy=strategy)
    n_colors = max(coloring.values()) + 1 if coloring else 0
    logger.info("Graph coloring: %d colors using strategy '%s'", n_colors, strategy)
    return coloring


def group_by_color(coloring: Dict[str, int]) -> Dict[int, List[str]]:
    """Group type names by their assigned color (batch).

    Returns:
        Dict mapping color_id -> list of type names
    """
    groups: Dict[int, List[str]] = {}
    for type_name, color_id in coloring.items():
        groups.setdefault(color_id, []).append(type_name)
    for color_id in groups:
        groups[color_id].sort()
    return groups


def get_graph_stats(G: nx.Graph, batches: Dict[int, List[str]]) -> Dict:
    """Compute summary statistics for the decomposition."""
    sizes = [len(b) for b in batches.values()]
    return {
        "n_nodes": G.number_of_nodes(),
        "n_edges": G.number_of_edges(),
        "n_colors": len(batches),
        "max_batch_size": max(sizes) if sizes else 0,
        "min_batch_size": min(sizes) if sizes else 0,
        "mean_batch_size": sum(sizes) / len(sizes) if sizes else 0,
        "batch_sizes": sorted(sizes, reverse=True),
    }


def enforce_min_batch_size(
    batches: Dict[int, List[str]],
    min_size: int,
    sim_matrix: torch.Tensor = None,
    type_names: List[str] = None,
) -> Dict[int, List[str]]:
    """Merge batches smaller than min_size into the least-confusable larger batch.

    When sim_matrix is available, picks the target batch with the lowest
    max cross-similarity to the small batch (preserves coloring intent).
    Otherwise merges into the smallest existing batch for balance.
    """
    batch_list = [list(b) for b in batches.values()]

    type_to_idx = {}
    if sim_matrix is not None and type_names is not None:
        type_to_idx = {name: i for i, name in enumerate(type_names)}

    merged_count = 0
    while len(batch_list) > 1:
        sizes = [len(b) for b in batch_list]
        if min(sizes) >= min_size:
            break

        min_idx = sizes.index(min(sizes))
        small_batch = batch_list.pop(min_idx)

        if type_to_idx:
            best_target = 0
            best_score = float('inf')
            for ti, target in enumerate(batch_list):
                max_sim = 0.0
                for s_type in small_batch:
                    si = type_to_idx.get(s_type)
                    if si is None:
                        continue
                    for t_type in target:
                        tj = type_to_idx.get(t_type)
                        if tj is None:
                            continue
                        val = sim_matrix[si, tj].item()
                        if val > max_sim:
                            max_sim = val
                if max_sim < best_score:
                    best_score = max_sim
                    best_target = ti
        else:
            target_sizes = [len(b) for b in batch_list]
            best_target = target_sizes.index(min(target_sizes))

        batch_list[best_target].extend(small_batch)
        merged_count += 1

    logger.info("enforce_min_batch_size: merged %d small batches (min_size=%d), "
                "%d batches remaining", merged_count, min_size, len(batch_list))

    return {i: sorted(types) for i, types in enumerate(batch_list)}
