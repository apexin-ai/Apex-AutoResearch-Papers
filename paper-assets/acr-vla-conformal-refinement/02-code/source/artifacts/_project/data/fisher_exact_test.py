#!/usr/bin/env python3
"""Fisher exact test + bootstrap CI for ACR-VLA two-seed pooled comparison.

Dependencies: numpy, scipy
Usage: python fisher_exact_test.py [--json INPUT.json]
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats

# ── 10 canonical spatial tasks ────────────────────────────────────────
SPATIAL_TASKS = [
    "between_plate_and_ramekin",
    "next_to_ramekin",
    "from_table_center",
    "on_cookie_box",
    "in_top_drawer",
    "on_ramekin",
    "next_to_cookie_box",
    "on_stove",
    "next_to_plate",
    "on_wooden_cabinet",
]

TRIALS_PER_TASK = 10

# ── placeholder data (replace with actual results) ────────────────────
# Format: {method: {task: success_rate_0_to_1}}
SEED42_DATA = {
    "obs_only": {t: None for t in SPATIAL_TASKS},
    "argmin":   {t: None for t in SPATIAL_TASKS},
}
SEED43_DATA = {
    "obs_only": {t: None for t in SPATIAL_TASKS},
    "argmin":   {t: None for t in SPATIAL_TASKS},
}


def load_data(json_path=None):
    if json_path:
        with open(json_path) as f:
            raw = json.load(f)
        return raw["seed42"], raw["seed43"]
    return SEED42_DATA, SEED43_DATA


def sr_to_counts(sr, n=TRIALS_PER_TASK):
    """Convert SR (0-1 float) to (successes, failures)."""
    if sr is None:
        return None, None
    successes = round(sr * n)
    return successes, n - successes


def pool_counts(seed42, seed43, method):
    """Pool success/failure counts across two seeds for a method."""
    total_success = 0
    total_fail = 0
    for task in SPATIAL_TASKS:
        for seed_data in [seed42, seed43]:
            sr = seed_data[method].get(task)
            if sr is None:
                continue
            s, f = sr_to_counts(sr)
            total_success += s
            total_fail += f
    return total_success, total_fail


def fisher_exact(s42, s43, method_a="obs_only", method_b="argmin"):
    """Two-sided Fisher exact test on pooled 2x2 table."""
    a_succ, a_fail = pool_counts(s42, s43, method_a)
    b_succ, b_fail = pool_counts(s42, s43, method_b)
    table = np.array([[a_succ, a_fail], [b_succ, b_fail]])
    odds_ratio, p_value = stats.fisher_exact(table, alternative="two-sided")
    return {
        "table": table.tolist(),
        f"{method_a}_success": a_succ,
        f"{method_a}_total": a_succ + a_fail,
        f"{method_b}_success": b_succ,
        f"{method_b}_total": b_succ + b_fail,
        "odds_ratio": odds_ratio,
        "p_value": p_value,
    }


def bootstrap_sr_difference(s42, s43, method_a="obs_only", method_b="argmin",
                            n_resamples=10000, ci=0.95, rng_seed=2026):
    """Bootstrap CI for difference in overall SR (method_a - method_b).

    Resamples at the task level: for each bootstrap iteration, sample tasks
    with replacement, then compute pooled SR difference.
    """
    rng = np.random.default_rng(rng_seed)

    task_diffs = []
    for task in SPATIAL_TASKS:
        a_succ, a_total, b_succ, b_total = 0, 0, 0, 0
        for seed_data in [s42, s43]:
            sr_a = seed_data[method_a].get(task)
            sr_b = seed_data[method_b].get(task)
            if sr_a is not None:
                s, f = sr_to_counts(sr_a)
                a_succ += s
                a_total += s + f
            if sr_b is not None:
                s, f = sr_to_counts(sr_b)
                b_succ += s
                b_total += s + f
        if a_total > 0 and b_total > 0:
            task_diffs.append((a_succ / a_total) - (b_succ / b_total))

    task_diffs = np.array(task_diffs)
    if len(task_diffs) == 0:
        return {"error": "no valid task data"}

    observed_diff = np.mean(task_diffs)

    boot_diffs = np.empty(n_resamples)
    n_tasks = len(task_diffs)
    for i in range(n_resamples):
        idx = rng.integers(0, n_tasks, size=n_tasks)
        boot_diffs[i] = np.mean(task_diffs[idx])

    alpha = (1 - ci) / 2
    ci_low = np.percentile(boot_diffs, alpha * 100)
    ci_high = np.percentile(boot_diffs, (1 - alpha) * 100)

    return {
        "observed_diff": observed_diff,
        "ci_level": ci,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "n_resamples": n_resamples,
        "n_tasks": int(n_tasks),
        "boot_std": float(np.std(boot_diffs)),
    }


def per_task_table(s42, s43, method_a="obs_only", method_b="argmin"):
    """Per-task comparison across two seeds."""
    rows = []
    for task in SPATIAL_TASKS:
        row = {"task": task}
        for method, label in [(method_a, "A"), (method_b, "B")]:
            sr42 = s42[method].get(task)
            sr43 = s43[method].get(task)
            pooled_s, pooled_t = 0, 0
            for sr in [sr42, sr43]:
                if sr is not None:
                    s, f = sr_to_counts(sr)
                    pooled_s += s
                    pooled_t += s + f
            row[f"{label}_seed42"] = f"{sr42*100:.0f}%" if sr42 is not None else "—"
            row[f"{label}_seed43"] = f"{sr43*100:.0f}%" if sr43 is not None else "—"
            row[f"{label}_pooled"] = f"{pooled_s}/{pooled_t}" if pooled_t > 0 else "—"
        rows.append(row)
    return rows


def interpret_pvalue(p):
    if p < 0.01:
        return "highly significant (p < 0.01)"
    elif p < 0.05:
        return "significant (p < 0.05)"
    elif p < 0.10:
        return "marginal (0.05 ≤ p < 0.10)"
    else:
        return "not significant (p ≥ 0.10)"


def main():
    parser = argparse.ArgumentParser(description="Fisher exact test + bootstrap CI")
    parser.add_argument("--json", type=str, default=None,
                        help="JSON file with seed42/seed43 data")
    parser.add_argument("--method-a", default="obs_only", help="Treatment method")
    parser.add_argument("--method-b", default="argmin", help="Control method")
    parser.add_argument("--n-resamples", type=int, default=10000)
    parser.add_argument("--dry-run", action="store_true", help="Validate script runs")
    args = parser.parse_args()

    if args.dry_run:
        print("dry-run OK: all imports successful, argparse works")
        return

    s42, s43 = load_data(args.json)

    has_data = any(
        s42[args.method_a].get(t) is not None
        for t in SPATIAL_TASKS
    )
    if not has_data:
        print("ERROR: no data loaded. Provide --json or fill in placeholder data.", file=sys.stderr)
        sys.exit(1)

    print("=" * 70)
    print(f"Fisher Exact Test: {args.method_a} vs {args.method_b}")
    print(f"Pooled across seed=42 + seed=43 ({TRIALS_PER_TASK} trials/task/seed)")
    print("=" * 70)

    # Fisher exact test
    fisher = fisher_exact(s42, s43, args.method_a, args.method_b)
    a_sr = fisher[f"{args.method_a}_success"] / fisher[f"{args.method_a}_total"] * 100
    b_sr = fisher[f"{args.method_b}_success"] / fisher[f"{args.method_b}_total"] * 100
    print(f"\n{args.method_a}: {fisher[f'{args.method_a}_success']}/{fisher[f'{args.method_a}_total']} = {a_sr:.1f}%")
    print(f"{args.method_b}: {fisher[f'{args.method_b}_success']}/{fisher[f'{args.method_b}_total']} = {b_sr:.1f}%")
    print(f"\n2x2 table: {fisher['table']}")
    print(f"Odds ratio: {fisher['odds_ratio']:.3f}")
    print(f"p-value: {fisher['p_value']:.4f}")
    print(f"Conclusion: {interpret_pvalue(fisher['p_value'])}")

    # Bootstrap CI
    print(f"\n{'─' * 70}")
    print(f"Bootstrap CI ({args.n_resamples} resamples, task-level)")
    print(f"{'─' * 70}")
    boot = bootstrap_sr_difference(s42, s43, args.method_a, args.method_b,
                                   n_resamples=args.n_resamples)
    if "error" in boot:
        print(f"ERROR: {boot['error']}")
    else:
        print(f"Observed SR diff ({args.method_a} - {args.method_b}): {boot['observed_diff']*100:+.1f}pp")
        print(f"95% CI: [{boot['ci_low']*100:+.1f}pp, {boot['ci_high']*100:+.1f}pp]")
        print(f"Bootstrap SE: {boot['boot_std']*100:.1f}pp")
        ci_contains_zero = boot["ci_low"] <= 0 <= boot["ci_high"]
        print(f"CI contains zero: {'yes → not significant' if ci_contains_zero else 'no → significant'}")

    # Per-task table
    print(f"\n{'─' * 70}")
    print("Per-task comparison")
    print(f"{'─' * 70}")
    rows = per_task_table(s42, s43, args.method_a, args.method_b)
    header = f"{'Task':<28} {'A s42':>6} {'A s43':>6} {'A pool':>8} {'B s42':>6} {'B s43':>6} {'B pool':>8}"
    print(header)
    print("─" * len(header))
    for r in rows:
        print(f"{r['task']:<28} {r['A_seed42']:>6} {r['A_seed43']:>6} {r['A_pooled']:>8} "
              f"{r['B_seed42']:>6} {r['B_seed43']:>6} {r['B_pooled']:>8}")


if __name__ == "__main__":
    main()
