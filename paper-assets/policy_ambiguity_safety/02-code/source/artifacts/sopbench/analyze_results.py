#!/usr/bin/env python3
"""Analyze SOPBench Phase 2C ambiguity experiment results.

Reads per-episode JSON files from the output directory, computes violation rates,
Newcombe 95% CIs for the ambiguous-minus-unambiguous difference, and compares
with the τ²-bench reference effect (+34pp).

Usage:
    python analyze_results.py --input-dir output_ambiguity/gpt-4.1
    python analyze_results.py --input-dir output_ambiguity/gpt-4.1 --output results_summary.md
"""

import os
import json
import math
import argparse
from collections import defaultdict
from datetime import datetime


def newcombe_ci(p1, n1, p2, n2):
    """Newcombe's method for 95% CI of p1 - p2."""
    z = 1.96

    def wilson(p, n):
        if n == 0:
            return 0.0, 0.0
        denom = 1 + z ** 2 / n
        center = (p + z ** 2 / (2 * n)) / denom
        half = z * math.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / denom
        return max(0.0, center - half), min(1.0, center + half)

    l1, u1 = wilson(p1, n1)
    l2, u2 = wilson(p2, n2)
    delta = p1 - p2
    lower = delta - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    upper = delta + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return delta, lower, upper


def load_results(input_dir):
    results = []
    for fname in sorted(os.listdir(input_dir)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(input_dir, fname)) as f:
            r = json.load(f)
        if "error" not in r and "evaluation" in r:
            results.append(r)
    return results


def violation_stats(episodes):
    n = len(episodes)
    v = sum(1 for r in episodes if not r["evaluation"]["constraint_not_violated"])
    p = v / n if n else 0.0
    return v, n, p


def format_row(label, amb_eps, unamb_eps):
    av, an, ap = violation_stats(amb_eps)
    uv, un, up = violation_stats(unamb_eps)
    d, lo, hi = newcombe_ci(ap, an, up, un)
    return (
        f"| {label} | {av}/{an} ({100 * ap:.0f}%) | {uv}/{un} ({100 * up:.0f}%) "
        f"| {100 * d:+.1f} | [{100 * lo:+.1f}, {100 * hi:+.1f}] |"
    )


def generate_report(results):
    amb = [r for r in results if r["condition"] == "ambiguous"]
    unamb = [r for r in results if r["condition"] == "unambiguous"]
    av, an, ap = violation_stats(amb)
    uv, un, up = violation_stats(unamb)
    d, lo, hi = newcombe_ci(ap, an, up, un)

    lines = [
        "# SOPBench Phase 2C: Ambiguity Experiment Results",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Overall",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Total valid episodes | {len(results)} |",
        f"| Ambiguous episodes | {an} |",
        f"| Unambiguous episodes | {un} |",
        f"| Ambiguous violation rate | {av}/{an} ({100 * ap:.1f}%) |",
        f"| Unambiguous violation rate | {uv}/{un} ({100 * up:.1f}%) |",
        f"| **Δpp** | **{100 * d:+.1f}pp** |",
        f"| 95% Newcombe CI | [{100 * lo:+.1f}, {100 * hi:+.1f}]pp |",
        f"| τ²-bench reference | +34pp |",
        "",
        "## Per Ambiguity Type",
        "",
        "| Type | Amb Viol | Unamb Viol | Δpp | 95% CI |",
        "|------|----------|------------|-----|--------|",
    ]

    for atype in sorted(set(r["ambiguity_type"] for r in results)):
        a = [r for r in amb if r["ambiguity_type"] == atype]
        u = [r for r in unamb if r["ambiguity_type"] == atype]
        lines.append(format_row(atype, a, u))

    lines += [
        "",
        "## Per Domain",
        "",
        "| Domain | Amb Viol | Unamb Viol | Δpp | 95% CI |",
        "|--------|----------|------------|-----|--------|",
    ]

    for domain in sorted(set(r["domain"] for r in results)):
        a = [r for r in amb if r["domain"] == domain]
        u = [r for r in unamb if r["domain"] == domain]
        lines.append(format_row(domain, a, u))

    lines += [
        "",
        "## Per Pair",
        "",
        "| Pair ID | Domain | Type | Amb CNV=F | Unamb CNV=F | Δpp |",
        "|---------|--------|------|-----------|-------------|-----|",
    ]

    for pid in sorted(set(r["pair_id"] for r in results)):
        a = [r for r in amb if r["pair_id"] == pid]
        u = [r for r in unamb if r["pair_id"] == pid]
        av2, an2, ap2 = violation_stats(a)
        uv2, un2, up2 = violation_stats(u)
        domain = a[0]["domain"] if a else u[0]["domain"]
        atype = a[0]["ambiguity_type"] if a else u[0]["ambiguity_type"]
        lines.append(
            f"| {pid} | {domain} | {atype} "
            f"| {av2}/{an2} | {uv2}/{un2} | {100 * (ap2 - up2):+.0f}pp |"
        )

    lines += [
        "",
        "## Comparison with τ²-bench",
        "",
        f"- SOPBench overall Δ: {100 * d:+.1f}pp  (CI: [{100 * lo:+.1f}, {100 * hi:+.1f}])",
        f"- τ²-bench overall Δ: +34pp",
        "",
        "Effect replicates across benchmarks."
        if d > 0 and lo > 0
        else "Effect direction consistent but CI includes zero — needs more data."
        if d > 0
        else "No clear effect detected.",
    ]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Analyze SOPBench ambiguity results")
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    results = load_results(args.input_dir)
    if not results:
        print("No valid results found.")
        return

    print(f"Loaded {len(results)} valid episodes")
    report = generate_report(results)
    print(report)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report + "\n")
        print(f"\nSaved to: {args.output}")


if __name__ == "__main__":
    main()
