#!/usr/bin/env python3
"""Pareto dominance analysis for cross-lingual probe transfer tradeoff.

Quantifies the depth-transferability tradeoff: deeper-layer EN probes achieve
higher in-language accuracy but may transfer worse cross-lingually. Identifies
Pareto-optimal layers, computes hypervolume indicators, and tests tradeoff
significance via Spearman correlation.

Input modes:
  (A) Pre-merged CSV with --en_metric and --transfer_metric columns per row.
  (B) Separate files: --results_csv (transfer eval) + --probe_csv (EN quality).
      In mode B, --method selects which transfer method to analyze.

Output (to --output_dir):
  pareto_detail.csv   per (layer, language) with Pareto flags and ranks
  pareto_summary.csv  per language: hypervolume, Spearman rho, p-value
  pareto_results.json combined results (with --json flag)

Algorithms:
  Pareto dominance: pairwise comparison, O(n^2), n = number of layers (< 50).
  Hypervolume: 2D sweep-line (Zitzler & Thiele, IEEE TEC 1999).
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict

import numpy as np
from scipy import stats


def find_pareto_optimal(points):
    """Identify non-dominated points (maximize both objectives). O(n^2)."""
    n = len(points)
    is_optimal = np.ones(n, dtype=bool)
    for i in range(n):
        if not is_optimal[i]:
            continue
        for j in range(n):
            if i == j or not is_optimal[j]:
                continue
            if (points[j, 0] >= points[i, 0] and points[j, 1] >= points[i, 1]
                    and (points[j, 0] > points[i, 0] or points[j, 1] > points[i, 1])):
                is_optimal[i] = False
                break
    return is_optimal


def compute_pareto_ranks(points):
    """Assign Pareto rank (1 = frontier) by iterative peeling."""
    n = len(points)
    ranks = np.zeros(n, dtype=int)
    remaining = np.ones(n, dtype=bool)
    rank = 1
    while remaining.any():
        idx = np.where(remaining)[0]
        is_opt = find_pareto_optimal(points[idx])
        for k, i in enumerate(idx):
            if is_opt[k]:
                ranks[i] = rank
                remaining[i] = False
        rank += 1
    return ranks


def compute_hypervolume_2d(pareto_points, ref_point):
    """2D hypervolume: area dominated by Pareto front above reference point.

    Sweep-line: sort Pareto points by x ascending (y non-increasing on front).
    HV = sum_i (x_i - x_{i-1}) * (y_i - ref_y), with x_{-1} = ref_x.
    """
    if len(pareto_points) == 0:
        return 0.0
    mask = (pareto_points[:, 0] > ref_point[0]) & (pareto_points[:, 1] > ref_point[1])
    pts = pareto_points[mask]
    if len(pts) == 0:
        return 0.0
    pts = pts[np.argsort(pts[:, 0])]
    hv = 0.0
    prev_x = ref_point[0]
    for i in range(len(pts)):
        hv += (pts[i, 0] - prev_x) * (pts[i, 1] - ref_point[1])
        prev_x = pts[i, 0]
    return hv


def load_data(args):
    """Load and merge EN probe quality + transfer results into per-language data."""
    with open(args.results_csv) as f:
        reader = csv.DictReader(f)
        transfer_rows = list(reader)

    if not transfer_rows:
        print("ERROR: results_csv is empty", file=sys.stderr)
        sys.exit(1)

    has_merged = (args.en_metric in transfer_rows[0] and
                  args.transfer_metric in transfer_rows[0])

    if has_merged:
        data = defaultdict(list)
        for row in transfer_rows:
            lang = row.get("language", "all")
            if args.languages and lang not in args.languages:
                continue
            data[lang].append((
                int(row["layer"]),
                float(row[args.en_metric]),
                float(row[args.transfer_metric]),
            ))
        return data

    if args.probe_csv is None:
        print(f"ERROR: results_csv lacks '{args.en_metric}' column. "
              f"Provide --probe_csv for EN probe quality.", file=sys.stderr)
        sys.exit(1)

    transfer_data = defaultdict(dict)
    for row in transfer_rows:
        if row["method"] != args.method:
            continue
        lang = row["language"]
        if args.languages and lang not in args.languages:
            continue
        transfer_data[lang][int(row["layer"])] = float(row["auroc"])

    en_data = {}
    with open(args.probe_csv) as f:
        reader = csv.DictReader(f)
        for row in reader:
            en_data[int(row["layer"])] = float(row["real_auroc"])

    data = defaultdict(list)
    for lang, layer_map in transfer_data.items():
        for layer in sorted(layer_map):
            if layer not in en_data:
                print(f"WARNING: layer {layer} in transfer results but not in probe_csv, skipping",
                      file=sys.stderr)
                continue
            data[lang].append((layer, en_data[layer], layer_map[layer]))
    return data


def analyze(data, ref_point):
    """Run Pareto analysis on per-language data. Returns (detail_rows, summary_rows, json_dict)."""
    detail_rows = []
    summary_rows = []
    json_results = {"ref_point": ref_point.tolist(), "languages": {}}

    for lang in sorted(data):
        entries = sorted(data[lang], key=lambda x: x[0])
        layers = np.array([e[0] for e in entries])
        en_vals = np.array([e[1] for e in entries])
        zs_vals = np.array([e[2] for e in entries])
        points = np.column_stack([en_vals, zs_vals])

        is_pareto = find_pareto_optimal(points)
        ranks = compute_pareto_ranks(points)
        hv = compute_hypervolume_2d(points[is_pareto], ref_point)
        rho, p_val = stats.spearmanr(en_vals, zs_vals)

        for i in range(len(layers)):
            detail_rows.append({
                "layer": int(layers[i]),
                "language": lang,
                "en_auroc": f"{en_vals[i]:.6f}",
                "zs_auroc": f"{zs_vals[i]:.6f}",
                "is_pareto_optimal": bool(is_pareto[i]),
                "pareto_rank": int(ranks[i]),
            })

        pareto_layers = sorted(layers[is_pareto].astype(int).tolist())
        summary_rows.append({
            "language": lang,
            "hypervolume": f"{hv:.6f}",
            "spearman_rho": f"{rho:.4f}",
            "spearman_p": f"{p_val:.6f}",
            "n_pareto_optimal": int(is_pareto.sum()),
            "pareto_layers": str(pareto_layers),
            "n_layers": len(layers),
            "tradeoff": "yes" if rho < 0 else "no",
        })

        json_results["languages"][lang] = {
            "hypervolume": round(hv, 6),
            "spearman_rho": round(float(rho), 4),
            "spearman_p": round(float(p_val), 6),
            "n_pareto_optimal": int(is_pareto.sum()),
            "pareto_layers": pareto_layers,
            "tradeoff": bool(rho < 0),
            "points": [
                {"layer": int(layers[i]), "en_auroc": round(float(en_vals[i]), 6),
                 "zs_auroc": round(float(zs_vals[i]), 6),
                 "is_pareto": True if is_pareto[i] else False,
                 "rank": int(ranks[i])}
                for i in range(len(layers))
            ],
        }

        print(f"[{lang}] HV={hv:.4f}  rho={rho:+.3f} (p={p_val:.4f})  "
              f"Pareto: {pareto_layers}  tradeoff={'YES' if rho < 0 else 'NO'}")

    return detail_rows, summary_rows, json_results


def write_outputs(detail_rows, summary_rows, json_results, output_dir, write_json):
    detail_path = os.path.join(output_dir, "pareto_detail.csv")
    with open(detail_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "layer", "language", "en_auroc", "zs_auroc",
            "is_pareto_optimal", "pareto_rank"])
        w.writeheader()
        w.writerows(detail_rows)
    print(f"\nWrote {detail_path}")

    summary_path = os.path.join(output_dir, "pareto_summary.csv")
    with open(summary_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "language", "hypervolume", "spearman_rho", "spearman_p",
            "n_pareto_optimal", "pareto_layers", "n_layers", "tradeoff"])
        w.writeheader()
        w.writerows(summary_rows)
    print(f"Wrote {summary_path}")

    if write_json:
        json_path = os.path.join(output_dir, "pareto_results.json")
        with open(json_path, "w") as f:
            json.dump(json_results, f, indent=2)
        print(f"Wrote {json_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Pareto dominance analysis for cross-lingual probe transfer")
    parser.add_argument("--results_csv", required=True,
                        help="Transfer results CSV (or pre-merged CSV with en/zs columns)")
    parser.add_argument("--probe_csv", default=None,
                        help="EN probe quality CSV (layer, real_auroc). "
                             "Required if results_csv lacks --en_metric column.")
    parser.add_argument("--output_dir", default="./results")
    parser.add_argument("--en_metric", default="en_auroc",
                        help="EN probe quality column name (default: en_auroc)")
    parser.add_argument("--transfer_metric", default="zs_auroc",
                        help="Transfer quality column name (default: zs_auroc)")
    parser.add_argument("--method", default="zero_shot",
                        help="Transfer method to analyze (default: zero_shot)")
    parser.add_argument("--languages", nargs="+", default=None,
                        help="Target languages (default: all in CSV)")
    parser.add_argument("--ref_point", nargs=2, type=float, default=[0.5, 0.5],
                        metavar=("X", "Y"),
                        help="Reference point for hypervolume (default: 0.5 0.5)")
    parser.add_argument("--json", action="store_true",
                        help="Also output JSON")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    data = load_data(args)
    if not data:
        print("ERROR: no data after filtering", file=sys.stderr)
        sys.exit(1)

    ref = np.array(args.ref_point)
    detail, summary, js = analyze(data, ref)
    write_outputs(detail, summary, js, args.output_dir, args.json)


if __name__ == "__main__":
    main()
