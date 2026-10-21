#!/usr/bin/env python3
"""Analyze SOPBench expansion results: merge original + new data, compute Fisher p-values."""

import json
import os
import sys
from collections import defaultdict
from scipy.stats import fisher_exact
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../sopbench/output_ambiguity")

MODELS = ["deepseek-v3", "gpt-5.4", "gpt-4.1", "claude-sonnet-4-6", "qwen3-235b"]


def load_model_results(model_dir):
    results = {"ambiguous": [], "unambiguous": []}
    errors = 0
    for fn in sorted(os.listdir(model_dir)):
        if not fn.endswith(".json"):
            continue
        with open(os.path.join(model_dir, fn)) as f:
            data = json.load(f)
        if "error" in data and "evaluation" not in data:
            errors += 1
            continue
        condition = data.get("condition")
        if condition in results:
            results[condition].append(data)
    return results, errors


def compute_stats(results):
    stats = {}
    for condition in ["ambiguous", "unambiguous"]:
        entries = results[condition]
        n = len(entries)
        violations = sum(1 for e in entries if not e["evaluation"]["constraint_not_violated"])
        stats[condition] = {"n": n, "violations": violations, "rate": violations / n if n else 0}
    return stats


def main():
    print("=" * 80)
    print("SOPBench Cross-Benchmark Replication — Expansion Analysis")
    print("=" * 80)

    all_stats = {}
    for model in MODELS:
        model_dir = os.path.join(OUTPUT_DIR, model)
        if not os.path.isdir(model_dir):
            print(f"\n{model}: directory not found, skipping")
            continue

        results, errors = load_model_results(model_dir)
        stats = compute_stats(results)

        amb = stats["ambiguous"]
        unamb = stats["unambiguous"]

        table = [
            [amb["violations"], amb["n"] - amb["violations"]],
            [unamb["violations"], unamb["n"] - unamb["violations"]],
        ]
        _, p_two = fisher_exact(table, alternative="two-sided")
        _, p_one = fisher_exact(table, alternative="greater")
        delta = amb["rate"] - unamb["rate"]

        all_stats[model] = {
            "n": amb["n"],
            "amb_rate": amb["rate"],
            "unamb_rate": unamb["rate"],
            "delta": delta,
            "p_two": p_two,
            "p_one": p_one,
            "errors": errors,
        }

        sig2 = "***" if p_two < 0.001 else "**" if p_two < 0.01 else "*" if p_two < 0.05 else "ns"
        sig1 = "***" if p_one < 0.001 else "**" if p_one < 0.01 else "*" if p_one < 0.05 else "ns"
        print(f"\n{model}:")
        print(f"  n = {amb['n']} episodes")
        print(f"  Ambiguous:   {amb['violations']}/{amb['n']} ({100*amb['rate']:.1f}%)")
        print(f"  Unambiguous: {unamb['violations']}/{unamb['n']} ({100*unamb['rate']:.1f}%)")
        print(f"  Δ = {100*delta:+.1f}pp")
        print(f"  Fisher two-sided p = {p_two:.4f} {sig2}")
        print(f"  Fisher one-sided p = {p_one:.4f} {sig1}")
        if errors:
            print(f"  Errors: {errors}")

    print(f"\n{'=' * 80}")
    print("Summary Table")
    print(f"{'=' * 80}")
    print(f"{'Model':<20} {'n':>5} {'Amb%':>7} {'Unamb%':>8} {'Δ(pp)':>8} {'p(2s)':>8} {'p(1s)':>8} {'Sig(1s)':>8}")
    print("-" * 78)
    for model in MODELS:
        if model not in all_stats:
            continue
        s = all_stats[model]
        sig = "***" if s["p_one"] < 0.001 else "**" if s["p_one"] < 0.01 else "*" if s["p_one"] < 0.05 else "ns"
        print(f"{model:<20} {s['n']:>5} {100*s['amb_rate']:>6.1f}% {100*s['unamb_rate']:>7.1f}% {100*s['delta']:>+7.1f} {s['p_two']:>8.4f} {s['p_one']:>8.4f} {sig:>8}")

    summary = {model: all_stats[model] for model in MODELS if model in all_stats}
    out_path = os.path.join(os.path.dirname(__file__), "expansion_summary.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary saved to: {out_path}")


if __name__ == "__main__":
    main()
