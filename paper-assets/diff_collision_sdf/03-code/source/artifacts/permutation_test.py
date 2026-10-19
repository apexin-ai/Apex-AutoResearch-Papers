#!/usr/bin/env python3
"""Exact permutation test + Welch t-test: SDF λ=0.1 vs LoRA-only baseline."""

import argparse
import sys
from itertools import combinations
from math import comb, sqrt

from scipy import stats

NULL_VALUES = [57, 52.5, 55, 57, 54, 52.5]
TREATMENT_2SEED = [58, 58.5]

NULL_LABELS = [
    "LoRA-only s0=57", "LoRA-only s1=52.5", "LoRA-only s2=55",
    "λ=0.005 s0=57", "λ=0.005 s1=54", "λ=0.005 s2=52.5",
]
TREAT_LABELS_2 = ["λ=0.1 s0=58", "λ=0.1 s1=58.5"]


def mean(vals):
    return sum(vals) / len(vals)


def permutation_test(pool, k, obs_mean):
    """Exact permutation test. Returns (one_tail_p, two_tail_p, all_combos)."""
    overall_mean = mean(pool)
    n_total = comb(len(pool), k)
    obs_dev = abs(obs_mean - overall_mean)

    one_tail_count = 0
    two_tail_count = 0
    combos = []

    for combo in combinations(pool, k):
        m = mean(combo)
        combos.append((combo, m))
        if m >= obs_mean:
            one_tail_count += 1
        if abs(m - overall_mean) >= obs_dev - 1e-12:
            two_tail_count += 1

    return one_tail_count / n_total, two_tail_count / n_total, combos, n_total


def welch_ttest(null_vals, treat_vals):
    """Welch t-test (unequal variance). Returns (t_stat, two_tail_p, one_tail_p)."""
    t_stat, two_p = stats.ttest_ind(treat_vals, null_vals, equal_var=False)
    one_p = two_p / 2 if t_stat > 0 else 1 - two_p / 2
    return t_stat, two_p, one_p


def run(treatment, treat_labels, out=sys.stdout):
    k = len(treatment)
    pool = NULL_VALUES + treatment
    obs_mean = mean(treatment)
    overall_mean = mean(pool)

    p1, p2, combos, n_total = permutation_test(pool, k, obs_mean)
    t_stat, welch_two, welch_one = welch_ttest(NULL_VALUES, treatment)

    w = out.write
    w("=" * 70 + "\n")
    w(f"  EXACT PERMUTATION TEST — treatment size = {k}\n")
    w("=" * 70 + "\n\n")

    w("Null group (n=6):\n")
    for lbl, v in zip(NULL_LABELS, NULL_VALUES):
        w(f"  {lbl:25s} = {v}\n")
    w(f"  Mean = {mean(NULL_VALUES):.4f}\n\n")

    w(f"Treatment group (n={k}):\n")
    for lbl, v in zip(treat_labels, treatment):
        w(f"  {lbl:25s} = {v}\n")
    w(f"  Observed mean = {obs_mean:.4f}\n\n")

    w(f"Pool size = {len(pool)}, C({len(pool)},{k}) = {n_total}\n")
    w(f"Overall pool mean = {overall_mean:.4f}\n\n")

    w("-" * 70 + "\n")
    w("All combinations (treatment draws) and their means:\n")
    w("-" * 70 + "\n")
    for i, (combo, m) in enumerate(combos, 1):
        marker = " ***" if m >= obs_mean else ""
        vals_str = ", ".join(f"{v:g}" for v in combo)
        w(f"  {i:3d}. ({vals_str:30s})  mean={m:7.4f}{marker}\n")

    w(f"\n*** = mean >= observed {obs_mean:.4f}\n\n")

    w("=" * 70 + "\n")
    w("  RESULTS SUMMARY\n")
    w("=" * 70 + "\n\n")

    w(f"Permutation test (exact, {n_total} combos):\n")
    w(f"  One-tailed p (mean >= {obs_mean:.4f}):  {p1:.4f}  ({int(p1*n_total)}/{n_total})\n")
    w(f"  Two-tailed p (|dev| >= {abs(obs_mean - overall_mean):.4f}): {p2:.4f}  ({int(p2*n_total)}/{n_total})\n\n")

    w(f"Welch t-test (unequal variance):\n")
    w(f"  t-statistic:   {t_stat:.4f}\n")
    w(f"  Two-tailed p:  {welch_two:.4f}\n")
    w(f"  One-tailed p:  {welch_one:.4f}\n\n")

    sig_05 = "YES" if p1 < 0.05 else "NO"
    sig_10 = "YES" if p1 < 0.10 else "NO"
    w(f"Significant at α=0.05 (one-tailed perm)? {sig_05}\n")
    w(f"Significant at α=0.10 (one-tailed perm)? {sig_10}\n")
    w("\n")

    return {
        "perm_one": p1, "perm_two": p2,
        "welch_t": t_stat, "welch_two": welch_two, "welch_one": welch_one,
        "obs_mean": obs_mean, "n_combos": n_total,
    }


def main():
    parser = argparse.ArgumentParser(description="Exact permutation test for SDF λ=0.1")
    parser.add_argument("--s2", type=float, default=None,
                        help="Third seed value for λ=0.1 (enables 3-of-9 mode)")
    args = parser.parse_args()

    if args.s2 is not None:
        treatment = TREATMENT_2SEED + [args.s2]
        labels = TREAT_LABELS_2 + [f"λ=0.1 s2={args.s2}"]
    else:
        treatment = TREATMENT_2SEED
        labels = TREAT_LABELS_2

    run(treatment, labels)


if __name__ == "__main__":
    main()
