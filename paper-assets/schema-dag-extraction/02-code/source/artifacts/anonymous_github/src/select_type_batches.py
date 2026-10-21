"""Type batch selection strategies based on BCS.

Input: Similarity matrix .pt
Output: JSON with low/high/random type batches and their BCS scores
Dependencies: torch
"""
import argparse
import json
import logging
import random
from pathlib import Path

import torch

from compute_bcs import compute_bcs

logger = logging.getLogger(__name__)


def select_low_bcs(n: int, sim_matrix: torch.Tensor, type_names: list, type_to_idx: dict) -> list:
    """Greedily select n types to minimize batch BCS.

    Start from the pair with lowest similarity, then add the type whose
    max similarity to any already-selected type is lowest (consistent with BCS = max).
    """
    if n > len(type_names):
        return list(type_names)

    num_types = len(type_names)

    # Find the pair with minimum similarity
    min_val = float("inf")
    min_i, min_j = 0, 1
    for i in range(num_types):
        for j in range(i + 1, num_types):
            val = sim_matrix[i, j].item()
            if val < min_val:
                min_val = val
                min_i, min_j = i, j

    selected_indices = [min_i, min_j]

    while len(selected_indices) < n:
        best_idx = -1
        best_max_sim = float("inf")
        for cand in range(num_types):
            if cand in selected_indices:
                continue
            max_sim = max(sim_matrix[cand, s].item() for s in selected_indices)
            if max_sim < best_max_sim:
                best_max_sim = max_sim
                best_idx = cand
        selected_indices.append(best_idx)

    return [type_names[i] for i in selected_indices]


def select_high_bcs(n: int, sim_matrix: torch.Tensor, type_names: list, type_to_idx: dict) -> list:
    """Greedily select n types to maximize batch BCS.

    Start from the pair with highest similarity (excluding self-pairs),
    then add the type whose max similarity to any already-selected type is highest (consistent with BCS = max).
    """
    if n > len(type_names):
        return list(type_names)

    num_types = len(type_names)

    max_val = float("-inf")
    max_i, max_j = 0, 1
    for i in range(num_types):
        for j in range(i + 1, num_types):
            val = sim_matrix[i, j].item()
            if val > max_val:
                max_val = val
                max_i, max_j = i, j

    selected_indices = [max_i, max_j]

    while len(selected_indices) < n:
        best_idx = -1
        best_max_sim = float("-inf")
        for cand in range(num_types):
            if cand in selected_indices:
                continue
            max_sim = max(sim_matrix[cand, s].item() for s in selected_indices)
            if max_sim > best_max_sim:
                best_max_sim = max_sim
                best_idx = cand
        selected_indices.append(best_idx)

    return [type_names[i] for i in selected_indices]


def select_random_batches(
    n: int,
    num_samples: int,
    type_names: list,
    sim_matrix: torch.Tensor,
    type_to_idx: dict,
    seed: int = 42,
) -> list:
    """Randomly sample batches of n types and compute their BCS.

    Returns:
        List of {"types": [...], "bcs": float}.
    """
    rng = random.Random(seed)
    results = []
    for _ in range(num_samples):
        chosen = rng.sample(type_names, n)
        bcs = compute_bcs(chosen, sim_matrix, type_to_idx)
        results.append({"types": chosen, "bcs": bcs})
    return results


def main():
    parser = argparse.ArgumentParser(description="Select type batches by BCS strategy")
    parser.add_argument("--sim_matrix_path", required=True, help="sim_matrix.pt path")
    parser.add_argument("--output_path", required=True, help="Output JSON path")
    parser.add_argument("--counts", default="6,12", help="Comma-separated type counts")
    parser.add_argument("--num_random", type=int, default=10, help="Number of random batches per count")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    data = torch.load(args.sim_matrix_path, map_location="cpu", weights_only=True)
    sim_matrix = data["sim_matrix"]
    type_names = data["type_names"]
    type_to_idx = data["type_to_idx"]

    counts = [int(c.strip()) for c in args.counts.split(",")]
    result = {}

    for count in counts:
        logger.info("Processing count=%d", count)

        low_types = select_low_bcs(count, sim_matrix, type_names, type_to_idx)
        low_bcs = compute_bcs(low_types, sim_matrix, type_to_idx)

        high_types = select_high_bcs(count, sim_matrix, type_names, type_to_idx)
        high_bcs = compute_bcs(high_types, sim_matrix, type_to_idx)

        random_batches = select_random_batches(count, args.num_random, type_names, sim_matrix, type_to_idx, args.seed)

        result[f"count_{count}"] = {
            "low_bcs": {"types": low_types, "bcs": low_bcs},
            "high_bcs": {"types": high_types, "bcs": high_bcs},
            "random": random_batches,
        }

        logger.info("  low BCS=%.4f, high BCS=%.4f, random BCS range=[%.4f, %.4f]",
                     low_bcs, high_bcs,
                     min(b["bcs"] for b in random_batches),
                     max(b["bcs"] for b in random_batches))

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(result, f, indent=2)
    logger.info("Saved batch config to %s", args.output_path)


if __name__ == "__main__":
    main()
