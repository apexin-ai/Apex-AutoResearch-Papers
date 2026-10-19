#!/usr/bin/env python3
"""Evaluate contrastive direction vectors on held-out test pairs.

Input:
  --directions  directions.pt from compute_directions.py
  --activations activations.pt from extract_activations.py
  --output-dir  directory for JSON report

Output:
  evaluation_report.json — per-layer AUROC, cosine similarity, stratified
                           breakdown, Go/No-Go verdict
  Human-readable summary printed to stdout

Deps: torch, numpy, sklearn
"""

import argparse
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import roc_auc_score

logger = logging.getLogger(__name__)


def load_test_samples(
    activations_path: str, test_pair_ids: list[str]
) -> list[dict]:
    """Load activation records and keep only those in the test set."""
    records = torch.load(activations_path, map_location="cpu", weights_only=False)
    test_set = set(test_pair_ids)
    filtered = [r for r in records if r["pair_id"] in test_set]
    logger.info(
        "Loaded %d total records; %d belong to test set (%d test pair_ids)",
        len(records), len(filtered), len(test_set),
    )
    return filtered


def compute_auroc_per_layer(
    samples: list[dict], d_syc: torch.Tensor
) -> dict[int, dict[int, float]]:
    """Compute AUROC per layer and token position.

    For each sample, project its activation onto d_syc (dot product) to get a
    scalar score. Label: 1=invalid_pressure, 0=valid_correction.

    Returns {layer_idx: {token_pos: auroc}}.
    """
    num_layers = d_syc.shape[0]
    num_positions = d_syc.shape[1]

    labels = []
    # scores[layer][pos] -> list of floats
    scores: dict[int, dict[int, list]] = {
        l: {p: [] for p in range(num_positions)} for l in range(num_layers)
    }

    for sample in samples:
        label = 1 if sample["condition"] == "invalid_pressure" else 0
        labels.append(label)
        acts = sample["activations"]  # (num_layers, 2, hidden_dim)

        for layer in range(num_layers):
            for pos in range(num_positions):
                score = torch.dot(acts[layer, pos], d_syc[layer, pos]).item()
                scores[layer][pos].append(score)

    labels_arr = np.array(labels)
    results = {}
    for layer in range(num_layers):
        results[layer] = {}
        for pos in range(num_positions):
            scores_arr = np.array(scores[layer][pos])
            if len(np.unique(labels_arr)) < 2:
                results[layer][pos] = float("nan")
            else:
                results[layer][pos] = roc_auc_score(labels_arr, scores_arr)

    return results


def compute_cosine_per_layer(
    d_syc: torch.Tensor, d_gen: torch.Tensor
) -> dict[int, dict[int, float]]:
    """Compute cosine similarity between d_syc and d_gen per layer and token position."""
    num_layers = d_syc.shape[0]
    num_positions = d_syc.shape[1]

    results = {}
    for layer in range(num_layers):
        results[layer] = {}
        for pos in range(num_positions):
            cos = torch.nn.functional.cosine_similarity(
                d_syc[layer, pos].unsqueeze(0),
                d_gen[layer, pos].unsqueeze(0),
            ).item()
            results[layer][pos] = cos

    return results


def compute_stratified_auroc(
    samples: list[dict], d_syc: torch.Tensor, group_key: str, best_layer: int
) -> dict[str, dict[int, float]]:
    """Compute AUROC broken down by a metadata field (domain, evidence_strength, etc.).

    Uses the best layer only, across all token positions.
    """
    num_positions = d_syc.shape[1]

    groups: dict[str, list[dict]] = defaultdict(list)
    for s in samples:
        groups[str(s[group_key])].append(s)

    results = {}
    for group_val, group_samples in sorted(groups.items()):
        labels = []
        scores_by_pos: dict[int, list] = {p: [] for p in range(num_positions)}

        for sample in group_samples:
            label = 1 if sample["condition"] == "invalid_pressure" else 0
            labels.append(label)
            for pos in range(num_positions):
                score = torch.dot(
                    sample["activations"][best_layer, pos], d_syc[best_layer, pos]
                ).item()
                scores_by_pos[pos].append(score)

        labels_arr = np.array(labels)
        if len(np.unique(labels_arr)) < 2:
            results[group_val] = {p: float("nan") for p in range(num_positions)}
        else:
            results[group_val] = {
                p: roc_auc_score(labels_arr, np.array(scores_by_pos[p]))
                for p in range(num_positions)
            }

    return results


def go_nogo_verdict(
    best_auroc: float, best_cosine: float,
    layer0_auroc: float = 0.5, layer0_delta: float = 1.0,
) -> dict:
    """Determine Go/No-Go based on v2 thresholds.

    Criteria (all must hold for PASS):
      1. Best-layer AUROC >= 0.85
      2. Δ(best_layer - layer0) >= 0.15 (signal in model computation, not embedding)
      3. cosine(d_syc, d_gen) < 0.3

    GRAY: AUROC in [0.80, 0.85) or Δ in [0.10, 0.15)
    FAIL: AUROC < 0.80 or Δ < 0.10
    """
    cosine_ok = best_cosine < 0.3
    delta_ok = layer0_delta >= 0.15
    delta_gray = layer0_delta >= 0.10

    reasons = []
    if best_auroc >= 0.85 and delta_ok and cosine_ok:
        verdict = "PASS"
        reasons.append(f"AUROC={best_auroc:.4f} >= 0.85")
        reasons.append(f"Δ(best-layer0)={layer0_delta:.4f} >= 0.15")
        reasons.append(f"cosine={best_cosine:.4f} < 0.3")
    elif best_auroc < 0.80 or layer0_delta < 0.10:
        verdict = "FAIL"
        if best_auroc < 0.80:
            reasons.append(f"AUROC={best_auroc:.4f} < 0.80")
        if layer0_delta < 0.10:
            reasons.append(f"Δ(best-layer0)={layer0_delta:.4f} < 0.10 (confound risk)")
    else:
        verdict = "GRAY"
        if best_auroc < 0.85:
            reasons.append(f"AUROC={best_auroc:.4f} in [0.80, 0.85)")
        if not delta_ok:
            reasons.append(f"Δ(best-layer0)={layer0_delta:.4f} in [0.10, 0.15)")
        if not cosine_ok:
            reasons.append(f"cosine={best_cosine:.4f} >= 0.3")

    return {
        "verdict": verdict,
        "reason": "; ".join(reasons),
        "auroc": best_auroc,
        "cosine": best_cosine,
        "layer0_auroc": layer0_auroc,
        "layer0_delta": layer0_delta,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate contrastive direction vectors on test set."
    )
    parser.add_argument(
        "--directions", required=True, help="Path to directions.pt from compute_directions.py"
    )
    parser.add_argument(
        "--activations", required=True, help="Path to activations.pt from extract_activations.py"
    )
    parser.add_argument("--output-dir", default=".", help="Output directory (default: .)")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    logger.info("Loading directions from %s", args.directions)
    directions = torch.load(args.directions, map_location="cpu", weights_only=False)
    d_syc = directions["d_syc"]
    d_gen = directions["d_gen"]
    test_pair_ids = directions["test_pair_ids"]
    metadata = directions["metadata"]

    if not test_pair_ids:
        logger.error("No test pair IDs in directions file; exiting")
        sys.exit(1)

    test_samples = load_test_samples(args.activations, test_pair_ids)
    if not test_samples:
        logger.error("No test samples found; exiting")
        sys.exit(1)

    # Per-layer AUROC
    logger.info("Computing per-layer AUROC")
    auroc_per_layer = compute_auroc_per_layer(test_samples, d_syc)

    # Find best layer (max AUROC across token positions)
    best_layer = -1
    best_auroc = -1.0
    best_pos = -1
    for layer, pos_dict in auroc_per_layer.items():
        for pos, auc in pos_dict.items():
            if not np.isnan(auc) and auc > best_auroc:
                best_auroc = auc
                best_layer = layer
                best_pos = pos

    logger.info("Best layer=%d, pos=%d, AUROC=%.4f", best_layer, best_pos, best_auroc)

    # Cosine similarity
    logger.info("Computing per-layer cosine similarity")
    cosine_per_layer = compute_cosine_per_layer(d_syc, d_gen)
    best_cosine = cosine_per_layer[best_layer][best_pos]

    # Stratified analysis at best layer
    logger.info("Computing stratified AUROC breakdown")
    breakdown_domain = compute_stratified_auroc(test_samples, d_syc, "domain", best_layer)
    breakdown_evidence = compute_stratified_auroc(
        test_samples, d_syc, "evidence_strength", best_layer
    )
    # Layer 0 confound baseline: if signal is already strong at layer 0,
    # it may be a surface-level token artifact rather than a learned representation.
    layer0_auroc = max(auroc_per_layer[0].values()) if 0 in auroc_per_layer else 0.5
    layer0_delta = best_auroc - layer0_auroc

    # Go/No-Go
    verdict = go_nogo_verdict(best_auroc, best_cosine, layer0_auroc, layer0_delta)

    # Build report
    report = {
        "metadata": metadata,
        "num_test_samples": len(test_samples),
        "num_test_pairs": len(test_pair_ids),
        "best_layer": best_layer,
        "best_token_position": best_pos,
        "best_auroc": best_auroc,
        "best_cosine": best_cosine,
        "layer0_auroc": layer0_auroc,
        "layer0_delta": layer0_delta,
        "per_layer_auroc": {
            str(l): {str(p): v for p, v in pos_dict.items()}
            for l, pos_dict in auroc_per_layer.items()
        },
        "per_layer_cosine": {
            str(l): {str(p): v for p, v in pos_dict.items()}
            for l, pos_dict in cosine_per_layer.items()
        },
        "stratified_auroc": {
            "by_domain": {
                k: {str(p): v for p, v in pos_dict.items()}
                for k, pos_dict in breakdown_domain.items()
            },
            "by_evidence_strength": {
                k: {str(p): v for p, v in pos_dict.items()}
                for k, pos_dict in breakdown_evidence.items()
            },
        },
        "go_nogo": verdict,
        "note": (
            "In the current binary setup d_gen = -d_syc, so cosine(d_syc, d_gen) = -1.0. "
            "The cosine threshold check (< 0.3) becomes meaningful only when d_gen is "
            "independently defined."
        ),
    }

    # Save JSON report
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    report_path = out_dir / "evaluation_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    logger.info("Saved report to %s", report_path)

    # Print human-readable summary
    token_pos_names = {0: "user_last", 1: "asst_first"}
    print("\n" + "=" * 60)
    print("DIRECTION EVALUATION SUMMARY")
    print("=" * 60)
    print(f"Test pairs: {len(test_pair_ids)}  |  Test samples: {len(test_samples)}")
    print(f"Layers: {metadata['num_layers']}  |  Hidden dim: {metadata['hidden_dim']}")
    print()

    print(f"Best layer: {best_layer}  |  Token position: {best_pos} ({token_pos_names.get(best_pos, '?')})")
    print(f"Best AUROC: {best_auroc:.4f}")
    print(f"Layer 0 AUROC: {layer0_auroc:.4f}  |  Delta(best - layer0): {layer0_delta:.4f}")
    print(f"Cosine(d_syc, d_gen) at best: {best_cosine:.4f}  (expected: -1.0 in binary setup)")
    print()

    # Top 5 layers
    all_layer_auc = []
    for layer, pos_dict in auroc_per_layer.items():
        for pos, auc in pos_dict.items():
            if not np.isnan(auc):
                all_layer_auc.append((layer, pos, auc))
    all_layer_auc.sort(key=lambda x: x[2], reverse=True)

    print("Top 5 (layer, position, AUROC):")
    for layer, pos, auc in all_layer_auc[:5]:
        print(f"  Layer {layer:2d}, {token_pos_names.get(pos, f'pos{pos}'):10s}: {auc:.4f}")
    print()

    # Stratified breakdown
    print("AUROC by domain (best layer, all positions):")
    for domain, pos_dict in sorted(breakdown_domain.items()):
        vals = [f"{token_pos_names.get(p, f'pos{p}')}={v:.4f}" for p, v in sorted(pos_dict.items())]
        print(f"  {domain:25s}  {', '.join(vals)}")
    print()

    print("AUROC by evidence_strength (best layer, all positions):")
    for es, pos_dict in sorted(breakdown_evidence.items()):
        vals = [f"{token_pos_names.get(p, f'pos{p}')}={v:.4f}" for p, v in sorted(pos_dict.items())]
        print(f"  {es:25s}  {', '.join(vals)}")
    print()

    # Go/No-Go
    print("-" * 60)
    print(f"GO/NO-GO VERDICT: {verdict['verdict']}")
    print(f"  {verdict['reason']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
