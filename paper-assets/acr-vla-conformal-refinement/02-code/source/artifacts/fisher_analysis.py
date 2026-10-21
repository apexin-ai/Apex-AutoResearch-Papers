"""Fisher exact test + bootstrap CI for obs_only CRM vs argmin baseline.

Compares success rates on LIBERO object benchmark across seeds.
Each seed: 10 tasks × 10 rollouts = 100 trials per condition.

Usage:
    python fisher_analysis.py \
        --obs_only_seed42_sr 0.19 --argmin_seed42_sr 0.12 \
        --obs_only_seed43_sr 0.20 --argmin_seed43_sr 0.17 \
        --n_trials 100

Output:
    Per-seed Fisher exact tests, pooled Fisher test, bootstrap 95% CI
    for effect size, and a decision label (CLAIM SUPPORTED / BORDERLINE / CLAIM WEAK).
"""

import argparse
import numpy as np
from scipy.stats import fisher_exact


def make_table(successes_a, successes_b, n):
    """2x2 contingency table: [[a_success, a_fail], [b_success, b_fail]]."""
    return np.array([
        [successes_a, n - successes_a],
        [successes_b, n - successes_b],
    ])


def run_fisher(successes_a, successes_b, n, label=""):
    table = make_table(successes_a, successes_b, n)
    odds_ratio, p = fisher_exact(table, alternative="two-sided")
    sr_a = successes_a / n
    sr_b = successes_b / n
    print(f"{label}obs_only {successes_a}/{n} ({sr_a:.0%}) vs argmin {successes_b}/{n} ({sr_b:.0%}), OR={odds_ratio:.4f}, p={p:.4f}")
    return odds_ratio, p


def bootstrap_effect_ci(successes_a, successes_b, n_total, n_boot=10000, ci=0.95, rng_seed=0):
    """Bootstrap CI for difference in success rates (obs_only - argmin)."""
    rng = np.random.default_rng(rng_seed)
    pool_a = np.concatenate([np.ones(successes_a), np.zeros(n_total - successes_a)])
    pool_b = np.concatenate([np.ones(successes_b), np.zeros(n_total - successes_b)])

    deltas = np.empty(n_boot)
    for i in range(n_boot):
        sa = rng.choice(pool_a, size=n_total, replace=True).mean()
        sb = rng.choice(pool_b, size=n_total, replace=True).mean()
        deltas[i] = sa - sb

    alpha = 1 - ci
    lo = np.percentile(deltas, 100 * alpha / 2)
    hi = np.percentile(deltas, 100 * (1 - alpha / 2))
    point = successes_a / n_total - successes_b / n_total
    return point, lo, hi


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--obs_only_seed42_sr", type=float, required=True)
    parser.add_argument("--argmin_seed42_sr", type=float, required=True)
    parser.add_argument("--obs_only_seed43_sr", type=float, required=True)
    parser.add_argument("--argmin_seed43_sr", type=float, required=True)
    parser.add_argument("--n_trials", type=int, default=100)
    parser.add_argument("--n_boot", type=int, default=10000)
    args = parser.parse_args()

    n = args.n_trials

    obs42 = round(args.obs_only_seed42_sr * n)
    arg42 = round(args.argmin_seed42_sr * n)
    obs43 = round(args.obs_only_seed43_sr * n)
    arg43 = round(args.argmin_seed43_sr * n)

    print("=" * 50)
    print("Per-seed Fisher Exact Test")
    print("=" * 50)
    run_fisher(obs42, arg42, n, label="seed=42: ")
    run_fisher(obs43, arg43, n, label="seed=43: ")

    obs_pooled = obs42 + obs43
    arg_pooled = arg42 + arg43
    n_pooled = n * 2

    print()
    print("=" * 50)
    print(f"Pooled Fisher Exact Test (N={n_pooled} per condition)")
    print("=" * 50)
    _, p_pooled = run_fisher(obs_pooled, arg_pooled, n_pooled, label="pooled: ")

    print()
    print("=" * 50)
    print("Bootstrap 95% CI for effect size")
    print("=" * 50)
    delta, lo, hi = bootstrap_effect_ci(obs_pooled, arg_pooled, n_pooled, n_boot=args.n_boot)
    print(f"Δ = {delta * 100:.1f} pp, 95% CI: [{lo * 100:.1f}, {hi * 100:.1f}] pp")

    print()
    print("=" * 50)
    print("DECISION")
    print("=" * 50)
    if p_pooled < 0.05:
        print("CLAIM SUPPORTED: statistically significant")
    elif p_pooled < 0.10:
        print("BORDERLINE: consider seed=44")
    else:
        print("CLAIM WEAK: adjust to suggestive evidence")

    print(f"\n(pooled p={p_pooled:.4f})")


if __name__ == "__main__":
    main()
