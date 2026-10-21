#!/usr/bin/env python3
"""Aggregate scaling experiment results across model sizes into a unified table."""

import argparse
import csv
import json
import os
import sys
from pathlib import Path


# Known data points (fill in as experiments complete)
KNOWN_RESULTS = [
    {
        "model": "Qwen3-4B",
        "family": "Qwen3",
        "size_b": 4,
        "dataset": "SciERC",
        "regime": "fine-tuned",
        "n_seeds": 1,
        "greedy_f1": 0.6622,
        "oracle_f1": 0.7925,
        "headroom_pp": 13.03,
        "degen_pct": 10.4,
        "lp_rho": None,
        "lp_delta_pp": None,
        "constr_delta_pp": None,
    },
    {
        "model": "Qwen3-8B",
        "family": "Qwen3",
        "size_b": 8,
        "dataset": "FewNERD",
        "regime": "fine-tuned",
        "n_seeds": 4,
        "greedy_f1": 0.7481,
        "oracle_f1": 0.8739,
        "headroom_pp": 12.58,
        "degen_pct": 12.69,
        "lp_rho": None,
        "lp_delta_pp": 1.38,
        "constr_delta_pp": None,
    },
    {
        "model": "LLaMA-3.1-8B",
        "family": "LLaMA",
        "size_b": 8,
        "dataset": "FewNERD",
        "regime": "fine-tuned",
        "n_seeds": 3,
        "greedy_f1": 0.7842,
        "oracle_f1": 0.8843,
        "headroom_pp": 10.01,
        "degen_pct": 23.36,
        "lp_rho": None,
        "lp_delta_pp": 0.36,
        "constr_delta_pp": None,
    },
    {
        "model": "Qwen2.5-72B",
        "family": "Qwen2.5",
        "size_b": 72,
        "dataset": "SciERC",
        "regime": "zero-shot",
        "n_seeds": 1,
        "greedy_f1": 0.399,
        "oracle_f1": 0.549,
        "headroom_pp": 15.0,
        "degen_pct": None,
        "lp_rho": None,
        "lp_delta_pp": None,
        "constr_delta_pp": None,
    },
    # === PLACEHOLDER: fill as experiments complete ===
    # {
    #     "model": "Qwen2.5-7B",
    #     "family": "Qwen2.5",
    #     "size_b": 7,
    #     "dataset": "FewNERD",
    #     "regime": "fine-tuned",
    #     ...
    # },
    # {
    #     "model": "Qwen2.5-14B",
    #     "family": "Qwen2.5",
    #     "size_b": 14,
    #     "dataset": "FewNERD",
    #     "regime": "fine-tuned",
    #     ...
    # },
    # {
    #     "model": "Qwen2.5-32B",
    #     "family": "Qwen2.5",
    #     "size_b": 32,
    #     "dataset": "FewNERD",
    #     "regime": "fine-tuned",
    #     ...
    # },
]

METRIC_KEYS = [
    "model", "family", "size_b", "dataset", "regime", "n_seeds",
    "greedy_f1", "oracle_f1", "headroom_pp", "degen_pct",
    "lp_rho", "lp_delta_pp", "constr_delta_pp",
]


def load_from_unified_json(path: str) -> dict:
    """Extract scaling-relevant metrics from a unified result JSON file.

    Expected format: {per_seed: {seedN: {...}}, summary: {...}}
    or flat format: {greedy_macro_f1: ..., oracle_macro_f1: ..., ...}
    """
    with open(path) as f:
        data = json.load(f)

    if "summary" in data:
        s = data["summary"]
        greedy = s.get("greedy_macro_f1", {}).get("mean")
        oracle = s.get("oracle_macro_f1", {}).get("mean")
        degen = s.get("degeneracy_rate_pct", {}).get("mean")
        lp_rho = s.get("lp_spearman_global", {}).get("mean")
        lp_delta = s.get("lp_selection_delta_pp", {}).get("mean")
        n_seeds = len(data.get("per_seed", {}))
    else:
        greedy = data.get("greedy_macro_f1") or data.get("greedy_f1")
        oracle = data.get("oracle_macro_f1") or data.get("oracle_f1")
        degen = data.get("degeneracy_rate_pct") or data.get("degeneracy_rate")
        if degen and degen < 1:
            degen *= 100
        lp_rho = data.get("lp_spearman_global") or data.get("lp_rho")
        lp_delta = data.get("lp_selection_delta_pp") or data.get("lp_delta_pp")
        n_seeds = 1

    headroom = (oracle - greedy) * 100 if greedy and oracle else None

    return {
        "greedy_f1": greedy,
        "oracle_f1": oracle,
        "headroom_pp": round(headroom, 2) if headroom else None,
        "degen_pct": round(degen, 2) if degen else None,
        "lp_rho": round(lp_rho, 4) if lp_rho else None,
        "lp_delta_pp": round(lp_delta, 2) if lp_delta else None,
        "n_seeds": n_seeds,
    }


def aggregate(extra_json_paths: list[tuple[str, dict]] = None) -> list[dict]:
    """Merge KNOWN_RESULTS with any additional JSON result files.

    extra_json_paths: list of (path, metadata_dict) where metadata_dict has
        keys: model, family, size_b, dataset, regime
    """
    results = list(KNOWN_RESULTS)

    if extra_json_paths:
        for path, meta in extra_json_paths:
            if not os.path.exists(path):
                print(f"WARNING: {path} not found, skipping", file=sys.stderr)
                continue
            parsed = load_from_unified_json(path)
            row = {**meta, **parsed}
            row.setdefault("constr_delta_pp", None)
            results.append(row)

    results.sort(key=lambda r: (r["dataset"], r["regime"], r["size_b"], r["family"]))
    return results


def print_table(results: list[dict]):
    header = f"{'Model':<16} {'Size':>5} {'Dataset':<8} {'Regime':<10} " \
             f"{'Greedy':>7} {'Oracle':>7} {'Head':>6} {'Degen%':>7} " \
             f"{'LP rho':>7} {'LP D':>6} {'C D':>6}"
    print(header)
    print("-" * len(header))
    for r in results:
        def fmt(v, w=7, d=4):
            return f"{v:{w}.{d}f}" if v is not None else " " * (w - 1) + "-"
        def fmt2(v, w=6, d=2):
            return f"{v:{w}.{d}f}" if v is not None else " " * (w - 1) + "-"

        print(f"{r['model']:<16} {r['size_b']:>5} {r['dataset']:<8} {r['regime']:<10} "
              f"{fmt(r['greedy_f1'])} {fmt(r['oracle_f1'])} "
              f"{fmt2(r.get('headroom_pp'))} {fmt2(r.get('degen_pct'))} "
              f"{fmt(r.get('lp_rho'))} {fmt2(r.get('lp_delta_pp'))} "
              f"{fmt2(r.get('constr_delta_pp'))}")


def save_csv(results: list[dict], path: str):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=METRIC_KEYS, extrasaction="ignore")
        w.writeheader()
        w.writerows(results)
    print(f"Saved CSV: {path}")


def save_json(results: list[dict], path: str):
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved JSON: {path}")


def main():
    parser = argparse.ArgumentParser(description="Aggregate scaling results")
    parser.add_argument("--extra", nargs="*", help="extra_path:model:family:size:dataset:regime")
    parser.add_argument("--out-csv", default=None)
    parser.add_argument("--out-json", default=None)
    args = parser.parse_args()

    extra = []
    if args.extra:
        for spec in args.extra:
            parts = spec.split(":")
            if len(parts) != 6:
                print(f"ERROR: --extra format is path:model:family:size:dataset:regime, got {spec}",
                      file=sys.stderr)
                sys.exit(1)
            path, model, family, size, dataset, regime = parts
            extra.append((path, {
                "model": model, "family": family, "size_b": float(size),
                "dataset": dataset, "regime": regime,
            }))

    results = aggregate(extra if extra else None)
    print_table(results)

    if args.out_csv:
        save_csv(results, args.out_csv)
    if args.out_json:
        save_json(results, args.out_json)

    default_dir = os.path.dirname(os.path.abspath(__file__))
    if not args.out_csv and not args.out_json:
        csv_path = os.path.join(default_dir, "scaling_results.csv")
        json_path = os.path.join(default_dir, "scaling_results.json")
        save_csv(results, csv_path)
        save_json(results, json_path)


if __name__ == "__main__":
    main()
