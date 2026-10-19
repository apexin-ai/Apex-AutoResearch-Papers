#!/usr/bin/env python3
"""Pooled Fisher exact test for multi-seed comparisons.

Reads actual counts from magnitude_curve_data.json — never hardcodes n_rollouts.
Supports 2/3/4/5 seed pooled analysis via --seeds argument.

Usage:
    python pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin
    python pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin --seeds 42 43 44
"""

import argparse
import json
import sys
from scipy.stats import fisher_exact
import numpy as np


def load_data(json_path: str) -> dict:
    with open(json_path) as f:
        return json.load(f)


def get_method_data(data: dict, method_key: str) -> list[dict]:
    """Get seed-level data for a method from seed_comparison section."""
    seed_comp = data.get("seed_comparison", {})
    if method_key not in seed_comp:
        available = list(seed_comp.keys())
        print(f"Error: method '{method_key}' not found. Available: {available}", file=sys.stderr)
        sys.exit(1)
    return seed_comp[method_key]


def pool_counts(entries: list[dict], seeds: list[int] | None = None) -> tuple[int, int]:
    """Pool successes and totals across specified seeds."""
    filtered = entries
    if seeds is not None:
        filtered = [e for e in entries if e["seed"] in seeds]
        found_seeds = {e["seed"] for e in filtered}
        missing = set(seeds) - found_seeds
        if missing:
            print(f"Warning: seeds {missing} not found in data (available: {[e['seed'] for e in entries]})", file=sys.stderr)
    total_successes = sum(e["successes"] for e in filtered)
    total_trials = sum(e["total"] for e in filtered)
    return total_successes, total_trials


def fisher_test_pooled(s1: int, n1: int, s2: int, n2: int) -> dict:
    """Run Fisher exact test on pooled 2x2 contingency table.

    Table:
              success  failure
    method1:    s1     n1 - s1
    method2:    s2     n2 - s2
    """
    table = np.array([[s1, n1 - s1], [s2, n2 - s2]])
    or_two, p_two = fisher_exact(table, alternative='two-sided')
    or_greater, p_greater = fisher_exact(table, alternative='greater')
    or_less, p_less = fisher_exact(table, alternative='less')
    return {
        "contingency_table": table.tolist(),
        "method1_sr": s1 / n1 if n1 > 0 else 0,
        "method2_sr": s2 / n2 if n2 > 0 else 0,
        "delta_pp": (s1 / n1 - s2 / n2) * 100 if n1 > 0 and n2 > 0 else 0,
        "odds_ratio": or_two,
        "p_two_sided": p_two,
        "p_greater": p_greater,
        "p_less": p_less,
    }


def main():
    parser = argparse.ArgumentParser(description="Pooled Fisher exact test from JSON data")
    parser.add_argument("--data", required=True, help="Path to magnitude_curve_data.json")
    parser.add_argument("--method1", required=True, help="First method key in seed_comparison")
    parser.add_argument("--method2", required=True, help="Second method key in seed_comparison")
    parser.add_argument("--seeds", nargs="+", type=int, default=None,
                        help="Which seeds to include (default: all available)")
    args = parser.parse_args()

    data = load_data(args.data)
    entries1 = get_method_data(data, args.method1)
    entries2 = get_method_data(data, args.method2)

    s1, n1 = pool_counts(entries1, args.seeds)
    s2, n2 = pool_counts(entries2, args.seeds)

    seeds_used = args.seeds if args.seeds else sorted({e["seed"] for e in entries1})
    n_seeds = len(seeds_used)

    print(f"{'='*60}")
    print(f"Pooled Fisher Exact Test ({n_seeds}-seed)")
    print(f"{'='*60}")
    print(f"Method 1: {args.method1}")
    print(f"  Seeds: {seeds_used}")
    print(f"  Pooled: {s1}/{n1} = {s1/n1:.1%}")
    for e in entries1:
        if args.seeds is None or e["seed"] in args.seeds:
            print(f"    seed{e['seed']}: {e['successes']}/{e['total']} ({e['exp_id']})")
    print(f"Method 2: {args.method2}")
    print(f"  Seeds: {sorted({e['seed'] for e in entries2 if args.seeds is None or e['seed'] in args.seeds})}")
    print(f"  Pooled: {s2}/{n2} = {s2/n2:.1%}")
    for e in entries2:
        if args.seeds is None or e["seed"] in args.seeds:
            print(f"    seed{e['seed']}: {e['successes']}/{e['total']} ({e['exp_id']})")
    print()

    result = fisher_test_pooled(s1, n1, s2, n2)

    print(f"Contingency table:")
    print(f"              success  failure")
    print(f"  {args.method1:20s}  {s1:>5d}  {n1-s1:>5d}")
    print(f"  {args.method2:20s}  {s2:>5d}  {n2-s2:>5d}")
    print()
    print(f"Delta: {result['delta_pp']:+.1f} pp ({args.method1} - {args.method2})")
    print(f"Odds ratio: {result['odds_ratio']:.4f}")
    print(f"p (two-sided): {result['p_two_sided']:.4f}")
    print(f"p (method1 > method2): {result['p_greater']:.4f}")
    print(f"p (method1 < method2): {result['p_less']:.4f}")
    print()

    alpha = 0.05
    sig = "SIGNIFICANT" if result['p_two_sided'] < alpha else "NOT significant"
    print(f"At alpha={alpha}: {sig}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
