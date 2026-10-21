#!/usr/bin/env python3
"""
D-study Calculator — Henderson Method I G Coefficient

Computes generalizability coefficients for benchmark evaluation designs
using variance components from a G-study.

Input:
  --components: JSON dict of variance components. Must include "item_id"
      (or "item") for the object of measurement, "residual" for the
      residual/error term, and any number of "facet:item" interaction
      terms (e.g., "temp:item", "prompt:item").
  --n_levels: JSON dict mapping each facet name to its number of levels
      in the D-study design.
  --n_items: Number of items in the benchmark (for display context).
  --sweep: Optional facet name. Prints G as that facet's levels vary
      from 1 to its current n_levels value.

Output:
  - Breakdown of σ²(δ) by source
  - G_item coefficient
  - Minimum n_conditions (product of facet levels) for G ≥ 0.80
  - G at various design scales

Formula:
  G_item = σ²(item) / [σ²(item) + σ²(δ)]
  σ²(δ) = Σ_k σ²(k:item)/n_k + σ²(residual)/Π(n_k)
  k iterates over all non-item facets.
"""

import argparse
import json
import math
import sys


def parse_components(components_dict):
    item_var = None
    residual_var = None
    interactions = {}

    for key, val in components_dict.items():
        if key in ("item_id", "item"):
            item_var = val
        elif key == "residual":
            residual_var = val
        elif ":item" in key or ":item_id" in key:
            facet = key.split(":")[0]
            interactions[facet] = val
        else:
            print(f"Warning: ignoring unknown component '{key}'", file=sys.stderr)

    if item_var is None:
        sys.exit("Error: missing 'item_id' or 'item' in --components")
    if residual_var is None:
        sys.exit("Error: missing 'residual' in --components")

    return item_var, interactions, residual_var


def compute_delta_variance(interactions, residual_var, n_levels):
    breakdown = {}

    for facet, var in interactions.items():
        n_k = n_levels.get(facet)
        if n_k is None:
            sys.exit(f"Error: facet '{facet}' in components but missing from --n_levels")
        breakdown[f"{facet}:item"] = var / n_k

    n_product = 1
    for facet in interactions:
        n_product *= n_levels[facet]
    breakdown["residual"] = residual_var / n_product

    return sum(breakdown.values()), breakdown


def compute_g(item_var, delta_var):
    return item_var / (item_var + delta_var)


def find_min_items_for_g(item_var, interactions, residual_var, n_levels, target=0.80):
    """Find minimum uniform scaling of all facet levels to achieve G >= target.

    Tries multiplying all n_levels by a uniform factor k = 1, 2, ...
    Returns (k, G) or None if not achievable within reasonable range.
    """
    for k in range(1, 10001):
        scaled = {f: n * k for f, n in n_levels.items()}
        delta, _ = compute_delta_variance(interactions, residual_var, scaled)
        g = compute_g(item_var, delta)
        if g >= target:
            return k, g
    return None


def print_results(item_var, interactions, residual_var, n_levels, n_items):
    delta_var, breakdown = compute_delta_variance(interactions, residual_var, n_levels)
    g = compute_g(item_var, delta_var)

    print("=" * 60)
    print("D-study Results (Henderson Method I)")
    print("=" * 60)

    print(f"\nBenchmark size: {n_items} items")
    print(f"Design: {' × '.join(f'{f}={n}' for f, n in n_levels.items())}")
    n_product = 1
    for f in interactions:
        n_product *= n_levels[f]
    print(f"Conditions per item: {n_product}")

    print(f"\nσ²(item) = {item_var:.6f}")
    print(f"\nσ²(δ) breakdown:")
    for source, val in breakdown.items():
        pct = val / delta_var * 100 if delta_var > 0 else 0
        print(f"  {source:20s}  {val:.6f}  ({pct:5.1f}%)")
    print(f"  {'TOTAL σ²(δ)':20s}  {delta_var:.6f}")

    print(f"\nG_item = {g:.4f}")

    if g >= 0.80:
        print(f"G ≥ 0.80: YES (already achieved with current design)")
    else:
        needed = math.ceil(delta_var * 0.80 / (item_var * (1 - 0.80)))
        single_delta = sum(interactions.values()) + residual_var
        single_g = compute_g(item_var, single_delta)
        print(f"G ≥ 0.80: NO with current design (G = {g:.4f})")
        print(f"  → Single-condition G = {single_g:.4f}")
        print(f"  → Increase facet levels to reduce σ²(δ). Use --sweep to explore.")

    print(f"\n{'n_items':>8s}  {'G_item':>8s}")
    print("-" * 20)
    for n in [50, 100, 200, 500, 1000]:
        print(f"{n:8d}  {g:8.4f}")

    print(f"\nNote: G_item depends on the evaluation design (n_levels),")
    print(f"not on the number of benchmark items.")


def sweep_facet(item_var, interactions, residual_var, n_levels, n_items, facet):
    if facet not in n_levels:
        sys.exit(f"Error: sweep facet '{facet}' not in --n_levels")

    max_level = n_levels[facet]
    print(f"\nSweep: {facet} levels 1..{max_level} (n_items={n_items})")
    print(f"{'n_' + facet:>12s}  {'σ²(δ)':>10s}  {'G_item':>8s}")
    print("-" * 34)

    for level in range(1, max_level + 1):
        swept = dict(n_levels)
        swept[facet] = level
        delta_var, _ = compute_delta_variance(interactions, residual_var, swept)
        g = compute_g(item_var, delta_var)
        print(f"{level:12d}  {delta_var:10.6f}  {g:8.4f}")


def main():
    parser = argparse.ArgumentParser(
        description="D-study Calculator: compute G coefficients for benchmark designs"
    )
    parser.add_argument(
        "--components", required=True,
        help='JSON dict of variance components, e.g. \'{"item_id": 0.12, "temp:item": 0.01, "residual": 0.05}\''
    )
    parser.add_argument(
        "--n_levels", required=True,
        help='JSON dict of facet levels, e.g. \'{"temp": 3, "prompt": 6}\''
    )
    parser.add_argument(
        "--n_items", type=int, default=200,
        help="Number of items in the benchmark (default: 200)"
    )
    parser.add_argument(
        "--sweep",
        help="Facet name to sweep from 1 to its n_levels value"
    )

    args = parser.parse_args()

    components = json.loads(args.components)
    n_levels = json.loads(args.n_levels)

    item_var, interactions, residual_var = parse_components(components)

    print_results(item_var, interactions, residual_var, n_levels, args.n_items)

    if args.sweep:
        sweep_facet(item_var, interactions, residual_var, n_levels, args.n_items, args.sweep)


if __name__ == "__main__":
    main()
