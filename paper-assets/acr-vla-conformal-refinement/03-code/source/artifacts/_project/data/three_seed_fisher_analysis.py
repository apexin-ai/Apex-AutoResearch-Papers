#!/usr/bin/env python3
"""3-seed pooled Fisher exact test for ACR-VLA conformal refinement."""

import argparse
import numpy as np
from scipy import stats


def cohens_h(p1, p2):
    return 2 * (np.arcsin(np.sqrt(p1)) - np.arcsin(np.sqrt(p2)))


def bootstrap_ci(obs_successes, obs_totals, arg_successes, arg_totals, n_boot=10000, alpha=0.05):
    rng = np.random.default_rng(42)
    diffs = []
    for _ in range(n_boot):
        obs_boot = sum(rng.binomial(t, s / t) for s, t in zip(obs_successes, obs_totals))
        arg_boot = sum(rng.binomial(t, s / t) for s, t in zip(arg_successes, arg_totals))
        total_obs = sum(obs_totals)
        total_arg = sum(arg_totals)
        diffs.append(obs_boot / total_obs - arg_boot / total_arg)
    lower = np.percentile(diffs, 100 * alpha / 2)
    upper = np.percentile(diffs, 100 * (1 - alpha / 2))
    return lower, upper


def main():
    parser = argparse.ArgumentParser(description="3-seed pooled Fisher exact test")
    parser.add_argument("--obs42", type=int, required=True, help="obs_only seed42 successes")
    parser.add_argument("--obs43", type=int, required=True, help="obs_only seed43 successes")
    parser.add_argument("--obs44", type=int, required=True, help="obs_only seed44 successes")
    parser.add_argument("--arg42", type=int, required=True, help="argmin seed42 successes")
    parser.add_argument("--arg43", type=int, required=True, help="argmin seed43 successes")
    parser.add_argument("--arg44", type=int, required=True, help="argmin seed44 successes")
    parser.add_argument("--total", type=int, default=100, help="trials per seed (default: 100)")
    args = parser.parse_args()

    obs = [args.obs42, args.obs43, args.obs44]
    arg = [args.arg42, args.arg43, args.arg44]
    totals = [args.total] * 3

    obs_pooled = sum(obs)
    arg_pooled = sum(arg)
    n_obs = sum(totals)
    n_arg = sum(totals)

    table = np.array([
        [obs_pooled, n_obs - obs_pooled],
        [arg_pooled, n_arg - arg_pooled]
    ])
    _, p_value = stats.fisher_exact(table, alternative='two-sided')

    obs_rate = obs_pooled / n_obs
    arg_rate = arg_pooled / n_arg
    diff = obs_rate - arg_rate
    h = cohens_h(obs_rate, arg_rate)

    ci_low, ci_high = bootstrap_ci(obs, totals, arg, totals)

    print("=" * 60)
    print("3-SEED POOLED FISHER EXACT TEST")
    print("=" * 60)

    print("\n--- Per-seed breakdown ---")
    print(f"{'Seed':<8} {'obs_only':<12} {'argmin':<12} {'diff':<10}")
    print("-" * 42)
    for i, seed in enumerate([42, 43, 44]):
        o_rate = obs[i] / totals[i]
        a_rate = arg[i] / totals[i]
        print(f"{seed:<8} {obs[i]}/{totals[i]} ({o_rate:.0%})  {arg[i]}/{totals[i]} ({a_rate:.0%})  {o_rate - a_rate:+.0%}")

    print("\n--- Pooled statistics ---")
    print(f"obs_only: {obs_pooled}/{n_obs} ({obs_rate:.1%})")
    print(f"argmin:   {arg_pooled}/{n_arg} ({arg_rate:.1%})")
    print(f"diff:     {diff:+.1%}")

    print("\n--- Inference ---")
    print(f"Fisher exact p-value:  {p_value:.4f}")
    print(f"Bootstrap 95% CI:      [{ci_low:+.3f}, {ci_high:+.3f}]")
    print(f"Cohen's h:             {h:.3f}")

    print("\n--- Conclusion ---")
    if p_value < 0.05:
        print(f"SIGNIFICANT (p={p_value:.4f} < 0.05): obs_only > argmin claim supported.")
    elif p_value < 0.10:
        print(f"DIRECTIONAL (p={p_value:.4f} < 0.10): trend favoring obs_only, not significant at α=0.05.")
    else:
        print(f"INSUFFICIENT (p={p_value:.4f} ≥ 0.10): no evidence for obs_only > argmin.")

    abs_h = abs(h)
    if abs_h < 0.2:
        h_label = "negligible"
    elif abs_h < 0.5:
        h_label = "small"
    elif abs_h < 0.8:
        h_label = "medium"
    else:
        h_label = "large"
    print(f"Effect size: {h_label} (|h|={abs_h:.3f})")
    print("=" * 60)


if __name__ == "__main__":
    main()
