#!/usr/bin/env python3
"""Compute contrastive direction vectors (d_syc, d_gen) from paired activations.

Input:  .pt file from extract_activations.py — list[dict] with keys:
        {pair_id, condition, domain, evidence_strength, correction_turn,
         activations: Tensor(num_layers, 2, hidden_dim)}
        Each pair_id has two entries: condition="valid_correction" and
        condition="invalid_pressure".

Output: directions.pt — dict with keys:
        d_syc              (num_layers, 2, hidden_dim) — L2-normalized
        d_gen              (num_layers, 2, hidden_dim) — L2-normalized
        train_pair_ids     list[str]
        test_pair_ids      list[str]
        metadata           dict

Deps:   torch, numpy, sklearn (for StratifiedShuffleSplit)
"""

import argparse
import logging
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
from sklearn.model_selection import StratifiedShuffleSplit

logger = logging.getLogger(__name__)


def load_and_group(path: str) -> dict[str, dict[str, dict]]:
    """Load activation records and group by pair_id.

    Returns {pair_id: {"valid_correction": record, "invalid_pressure": record}}.
    """
    records = torch.load(path, map_location="cpu", weights_only=False)
    logger.info("Loaded %d records from %s", len(records), path)

    grouped: dict[str, dict[str, dict]] = defaultdict(dict)
    for rec in records:
        pid = rec["pair_id"]
        cond = rec["condition"]
        if cond in grouped[pid]:
            logger.warning("Duplicate condition '%s' for pair_id '%s'; overwriting", cond, pid)
        grouped[pid][cond] = rec

    complete = {}
    for pid, conds in grouped.items():
        if "valid_correction" in conds and "invalid_pressure" in conds:
            complete[pid] = conds
        else:
            logger.warning(
                "Pair '%s' incomplete (conditions: %s); skipping", pid, list(conds.keys())
            )

    logger.info("Complete pairs: %d", len(complete))
    return complete


def stratified_split(
    pairs: dict[str, dict[str, dict]], test_ratio: float, seed: int
) -> tuple[list[str], list[str]]:
    """Split pair_ids into train/test with stratification by domain.

    Uses StratifiedShuffleSplit so each domain's proportion is preserved
    across the split. The split unit is the pair (both conditions stay together).
    """
    pair_ids = sorted(pairs.keys())
    domains = [pairs[pid]["valid_correction"]["domain"] for pid in pair_ids]

    # Check if stratification is feasible (need >= 2 samples per domain for split)
    domain_counts = defaultdict(int)
    for d in domains:
        domain_counts[d] += 1

    min_count = min(domain_counts.values())
    if min_count < 2:
        logger.warning(
            "Some domains have < 2 pairs (min=%d); falling back to unstratified shuffle",
            min_count,
        )
        rng = np.random.RandomState(seed)
        idx = rng.permutation(len(pair_ids))
        n_test = max(1, int(len(pair_ids) * test_ratio))
        test_idx = set(idx[:n_test])
        train_ids = [pair_ids[i] for i in range(len(pair_ids)) if i not in test_idx]
        test_ids = [pair_ids[i] for i in range(len(pair_ids)) if i in test_idx]
        return train_ids, test_ids

    splitter = StratifiedShuffleSplit(n_splits=1, test_size=test_ratio, random_state=seed)
    pair_ids_arr = np.array(pair_ids)
    domains_arr = np.array(domains)

    train_idx, test_idx = next(splitter.split(pair_ids_arr, domains_arr))
    train_ids = pair_ids_arr[train_idx].tolist()
    test_ids = pair_ids_arr[test_idx].tolist()

    logger.info("Split: %d train, %d test", len(train_ids), len(test_ids))
    return train_ids, test_ids


def compute_direction(
    pairs: dict[str, dict[str, dict]],
    pair_ids: list[str],
    positive_condition: str,
    negative_condition: str,
) -> torch.Tensor:
    """Compute difference-in-means direction: mean(positive) - mean(negative).

    Returns L2-normalized direction of shape (num_layers, 2, hidden_dim).
    """
    pos_acts = []
    neg_acts = []
    for pid in pair_ids:
        pos_acts.append(pairs[pid][positive_condition]["activations"])
        neg_acts.append(pairs[pid][negative_condition]["activations"])

    # Stack: (N, num_layers, 2, hidden_dim)
    pos_mean = torch.stack(pos_acts).mean(dim=0)
    neg_mean = torch.stack(neg_acts).mean(dim=0)

    direction = pos_mean - neg_mean

    # L2 normalize per (layer, token_position) slice
    norms = direction.norm(dim=-1, keepdim=True).clamp(min=1e-8)
    direction = direction / norms

    return direction


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute contrastive direction vectors from paired activations."
    )
    parser.add_argument("input", help="Path to activations .pt file (Phase 2 output)")
    parser.add_argument("--output-dir", default=".", help="Output directory (default: .)")
    parser.add_argument(
        "--test-ratio", type=float, default=0.2, help="Test set ratio (default: 0.2)"
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    pairs = load_and_group(args.input)
    if not pairs:
        logger.error("No complete pairs found; exiting")
        sys.exit(1)

    train_ids, test_ids = stratified_split(pairs, args.test_ratio, args.seed)

    # d_syc: invalid_pressure - valid_correction (on train set)
    logger.info("Computing d_syc from %d train pairs", len(train_ids))
    d_syc = compute_direction(
        pairs, train_ids,
        positive_condition="invalid_pressure",
        negative_condition="valid_correction",
    )

    # d_gen: valid_correction - invalid_pressure (on train set)
    # Currently d_gen = -d_syc, but stored separately for future extensibility.
    logger.info("Computing d_gen from %d train pairs", len(train_ids))
    d_gen = compute_direction(
        pairs, train_ids,
        positive_condition="valid_correction",
        negative_condition="invalid_pressure",
    )

    num_layers, _, hidden_dim = d_syc.shape
    metadata = {
        "num_layers": num_layers,
        "hidden_dim": hidden_dim,
        "test_ratio": args.test_ratio,
        "seed": args.seed,
        "num_train_pairs": len(train_ids),
        "num_test_pairs": len(test_ids),
        "num_total_pairs": len(pairs),
    }

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "directions.pt"

    payload = {
        "d_syc": d_syc,
        "d_gen": d_gen,
        "train_pair_ids": train_ids,
        "test_pair_ids": test_ids,
        "metadata": metadata,
    }
    torch.save(payload, out_path)
    logger.info("Saved directions to %s", out_path)
    logger.info("Metadata: %s", metadata)


if __name__ == "__main__":
    main()
