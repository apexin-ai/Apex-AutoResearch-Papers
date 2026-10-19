#!/usr/bin/env python3
"""
Pooled Fisher Exact Test + Bootstrap CI for CRM ablation (obs_only vs argmin).
Two seeds × 100 trials each (10 tasks × 10 rollouts on LIBERO object benchmark).

Usage:
  # Run with pre-filled seed=42 data only:
  python seed43_fisher_analysis.py

  # With JSON result files:
  python seed43_fisher_analysis.py \
    --obs-only-s42 results/obs_only_seed42_results.json \
    --argmin-s42 results/argmin_seed42_results.json \
    --obs-only-s43 results/obs_only_seed43_results.json \
    --argmin-s43 results/argmin_seed43_results.json

  # With aggregate numbers (success/total):
  python seed43_fisher_analysis.py --agg \
    --obs-s42 19 100 --arg-s42 12 100 \
    --obs-s43 8 60 --arg-s43 6 60

  # Output saved to analysis/fisher_results.json
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats


# === Pre-filled seed=42 data ===
SEED42_OBS_ONLY = {
    "alphabet_soup": {"success": 0, "total": 10},
    "cream_cheese": {"success": 1, "total": 10},
    "salad_dressing": {"success": 1, "total": 10},
    "bbq_sauce": {"success": 3, "total": 10},
    "ketchup": {"success": 2, "total": 10},
    "tomato_sauce": {"success": 1, "total": 10},
    "butter": {"success": 1, "total": 10},
    "milk": {"success": 2, "total": 10},
    "chocolate_pudding": {"success": 6, "total": 10},
    "orange_juice": {"success": 3, "total": 10},
}  # total: 20/100 = 20% ... but user said 19%, using 19 below as aggregate

SEED42_ARGMIN_AGGREGATE = {"success": 12, "total": 100}
SEED42_OBS_ONLY_AGGREGATE = {"success": 19, "total": 100}


def load_results_json(path):
    """Load per-task results JSON: {"task": {"success": N, "total": M}, ...}"""
    with open(path) as f:
        data = json.load(f)
    return data


def aggregate_from_pertask(pertask):
    """Sum per-task results into aggregate."""
    s = sum(v["success"] for v in pertask.values())
    t = sum(v["total"] for v in pertask.values())
    return {"success": s, "total": t}


def fisher_exact_2x2(obs_succ, obs_total, arg_succ, arg_total):
    """
    2×2 Fisher exact test.
    Table:
              success  failure
    obs_only  [a        b]
    argmin    [c        d]
    """
    a, b = obs_succ, obs_total - obs_succ
    c, d = arg_succ, arg_total - arg_succ
    table = np.array([[a, b], [c, d]])
    odds_ratio, p_value = stats.fisher_exact(table, alternative="two-sided")

    # 95% CI for odds ratio (Woolf logit method)
    if 0 in [a, b, c, d]:
        # Haldane correction
        a_, b_, c_, d_ = a + 0.5, b + 0.5, c + 0.5, d + 0.5
    else:
        a_, b_, c_, d_ = a, b, c, d

    log_or = np.log(a_ * d_ / (b_ * c_))
    se_log_or = np.sqrt(1/a_ + 1/b_ + 1/c_ + 1/d_)
    ci_low = np.exp(log_or - 1.96 * se_log_or)
    ci_high = np.exp(log_or + 1.96 * se_log_or)

    return {
        "obs_success": int(obs_succ),
        "obs_total": int(obs_total),
        "arg_success": int(arg_succ),
        "arg_total": int(arg_total),
        "obs_sr": obs_succ / obs_total,
        "arg_sr": arg_succ / arg_total,
        "diff_pp": (obs_succ / obs_total - arg_succ / arg_total) * 100,
        "odds_ratio": float(odds_ratio),
        "odds_ratio_ci95": [float(ci_low), float(ci_high)],
        "p_value": float(p_value),
    }


def bootstrap_sr_diff(obs_outcomes, arg_outcomes, n_boot=10000, seed=0):
    """
    Bootstrap CI for SR difference (obs_only - argmin).
    obs_outcomes / arg_outcomes: arrays of 0/1.
    """
    rng = np.random.default_rng(seed)
    n_obs = len(obs_outcomes)
    n_arg = len(arg_outcomes)
    diffs = np.empty(n_boot)

    for i in range(n_boot):
        obs_sample = rng.choice(obs_outcomes, size=n_obs, replace=True)
        arg_sample = rng.choice(arg_outcomes, size=n_arg, replace=True)
        diffs[i] = obs_sample.mean() - arg_sample.mean()

    ci_low, ci_high = np.percentile(diffs, [2.5, 97.5])
    return {
        "mean_diff": float(diffs.mean()),
        "ci95_low": float(ci_low),
        "ci95_high": float(ci_high),
        "p_boot": float(np.mean(diffs <= 0)),  # one-sided: P(obs <= argmin)
    }


def pertask_paired_bootstrap(obs_pertask, arg_pertask, n_boot=10000, seed=0):
    """
    Per-task paired bootstrap: resample tasks, compute mean SR diff.
    Both dicts must have the same task keys.
    """
    common_tasks = sorted(set(obs_pertask.keys()) & set(arg_pertask.keys()))
    if not common_tasks:
        return None

    obs_srs = np.array([obs_pertask[t]["success"] / obs_pertask[t]["total"] for t in common_tasks])
    arg_srs = np.array([arg_pertask[t]["success"] / arg_pertask[t]["total"] for t in common_tasks])
    task_diffs = obs_srs - arg_srs

    rng = np.random.default_rng(seed)
    n_tasks = len(common_tasks)
    boot_means = np.empty(n_boot)

    for i in range(n_boot):
        idx = rng.choice(n_tasks, size=n_tasks, replace=True)
        boot_means[i] = task_diffs[idx].mean()

    ci_low, ci_high = np.percentile(boot_means, [2.5, 97.5])
    return {
        "n_tasks": n_tasks,
        "mean_task_diff": float(task_diffs.mean()),
        "ci95_low": float(ci_low),
        "ci95_high": float(ci_high),
        "per_task": {t: {"obs_sr": float(obs_srs[i]), "arg_sr": float(arg_srs[i]),
                         "diff": float(task_diffs[i])}
                     for i, t in enumerate(common_tasks)},
    }


def outcomes_from_aggregate(success, total):
    """Create binary outcome array from aggregate counts."""
    return np.array([1]*success + [0]*(total - success))


def print_results(results):
    """Print structured table."""
    print("=" * 70)
    print("FISHER EXACT TEST: obs_only vs argmin (CRM ablation)")
    print("=" * 70)

    for label in ["seed42", "seed43", "pooled"]:
        if label not in results["fisher"]:
            continue
        r = results["fisher"][label]
        print(f"\n--- {label.upper()} ---")
        print(f"  obs_only: {r['obs_success']}/{r['obs_total']} = {r['obs_sr']*100:.1f}%")
        print(f"  argmin:   {r['arg_success']}/{r['arg_total']} = {r['arg_sr']*100:.1f}%")
        print(f"  Δ = {r['diff_pp']:+.1f} pp")
        print(f"  OR = {r['odds_ratio']:.3f}  95% CI [{r['odds_ratio_ci95'][0]:.3f}, {r['odds_ratio_ci95'][1]:.3f}]")
        print(f"  p = {r['p_value']:.4f} {'***' if r['p_value']<0.001 else '**' if r['p_value']<0.01 else '*' if r['p_value']<0.05 else 'ns'}")

    if "bootstrap" in results:
        print(f"\n--- BOOTSTRAP (10k resamples) ---")
        for label in ["seed42", "seed43", "pooled"]:
            if label not in results["bootstrap"]:
                continue
            b = results["bootstrap"][label]
            print(f"  {label}: mean Δ = {b['mean_diff']*100:.1f} pp, "
                  f"95% CI [{b['ci95_low']*100:.1f}, {b['ci95_high']*100:.1f}] pp, "
                  f"P(obs≤arg) = {b['p_boot']:.4f}")

    if "paired_bootstrap" in results and results["paired_bootstrap"]:
        print(f"\n--- PER-TASK PAIRED BOOTSTRAP ---")
        for label, pb in results["paired_bootstrap"].items():
            if pb is None:
                continue
            print(f"  {label}: {pb['n_tasks']} tasks, mean Δ = {pb['mean_task_diff']*100:.1f} pp, "
                  f"95% CI [{pb['ci95_low']*100:.1f}, {pb['ci95_high']*100:.1f}] pp")

    print("\n" + "=" * 70)
    sig = results["fisher"].get("pooled", results["fisher"].get("seed42", {}))
    p = sig.get("p_value", 1.0)
    print(f"VERDICT: p = {p:.4f} → {'SIGNIFICANT (p < 0.05)' if p < 0.05 else 'NOT SIGNIFICANT'}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Fisher exact test + bootstrap CI for CRM ablation (obs_only vs argmin)")
    parser.add_argument("--obs-only-s42", type=str, help="Path to obs_only seed42 per-task JSON")
    parser.add_argument("--argmin-s42", type=str, help="Path to argmin seed42 per-task JSON")
    parser.add_argument("--obs-only-s43", type=str, help="Path to obs_only seed43 per-task JSON")
    parser.add_argument("--argmin-s43", type=str, help="Path to argmin seed43 per-task JSON")
    parser.add_argument("--agg", action="store_true", help="Use aggregate mode (pass --obs-s42 S T etc.)")
    parser.add_argument("--obs-s42", nargs=2, type=int, metavar=("S", "T"), help="obs_only seed42: success total")
    parser.add_argument("--arg-s42", nargs=2, type=int, metavar=("S", "T"), help="argmin seed42: success total")
    parser.add_argument("--obs-s43", nargs=2, type=int, metavar=("S", "T"), help="obs_only seed43: success total")
    parser.add_argument("--arg-s43", nargs=2, type=int, metavar=("S", "T"), help="argmin seed43: success total")
    parser.add_argument("--output", type=str, default="analysis/fisher_results.json", help="Output JSON path")
    parser.add_argument("--n-boot", type=int, default=10000, help="Bootstrap resamples")
    args = parser.parse_args()

    # Collect data
    obs_s42_pertask = None
    arg_s42_pertask = None
    obs_s43_pertask = None
    arg_s43_pertask = None

    # Seed 42 data
    if args.obs_only_s42:
        obs_s42_pertask = load_results_json(args.obs_only_s42)
        obs_s42_agg = aggregate_from_pertask(obs_s42_pertask)
    elif args.agg and args.obs_s42:
        obs_s42_agg = {"success": args.obs_s42[0], "total": args.obs_s42[1]}
    else:
        # Use pre-filled data
        obs_s42_pertask = SEED42_OBS_ONLY
        obs_s42_agg = SEED42_OBS_ONLY_AGGREGATE

    if args.argmin_s42:
        arg_s42_pertask = load_results_json(args.argmin_s42)
        arg_s42_agg = aggregate_from_pertask(arg_s42_pertask)
    elif args.agg and args.arg_s42:
        arg_s42_agg = {"success": args.arg_s42[0], "total": args.arg_s42[1]}
    else:
        arg_s42_agg = SEED42_ARGMIN_AGGREGATE

    # Seed 43 data
    has_s43 = False
    if args.obs_only_s43:
        obs_s43_pertask = load_results_json(args.obs_only_s43)
        obs_s43_agg = aggregate_from_pertask(obs_s43_pertask)
        has_s43 = True
    elif args.agg and args.obs_s43:
        obs_s43_agg = {"success": args.obs_s43[0], "total": args.obs_s43[1]}
        has_s43 = True

    if args.argmin_s43:
        arg_s43_pertask = load_results_json(args.argmin_s43)
        arg_s43_agg = aggregate_from_pertask(arg_s43_pertask)
        has_s43 = True
    elif args.agg and args.arg_s43:
        arg_s43_agg = {"success": args.arg_s43[0], "total": args.arg_s43[1]}
        has_s43 = True

    # === Fisher Exact Tests ===
    results = {"fisher": {}, "bootstrap": {}, "paired_bootstrap": {}}

    # Seed 42
    results["fisher"]["seed42"] = fisher_exact_2x2(
        obs_s42_agg["success"], obs_s42_agg["total"],
        arg_s42_agg["success"], arg_s42_agg["total"])

    # Bootstrap seed 42
    obs_out_42 = outcomes_from_aggregate(obs_s42_agg["success"], obs_s42_agg["total"])
    arg_out_42 = outcomes_from_aggregate(arg_s42_agg["success"], arg_s42_agg["total"])
    results["bootstrap"]["seed42"] = bootstrap_sr_diff(obs_out_42, arg_out_42, n_boot=args.n_boot)

    # Paired bootstrap seed 42
    if obs_s42_pertask and arg_s42_pertask:
        results["paired_bootstrap"]["seed42"] = pertask_paired_bootstrap(
            obs_s42_pertask, arg_s42_pertask, n_boot=args.n_boot)

    if has_s43:
        # Seed 43
        results["fisher"]["seed43"] = fisher_exact_2x2(
            obs_s43_agg["success"], obs_s43_agg["total"],
            arg_s43_agg["success"], arg_s43_agg["total"])

        obs_out_43 = outcomes_from_aggregate(obs_s43_agg["success"], obs_s43_agg["total"])
        arg_out_43 = outcomes_from_aggregate(arg_s43_agg["success"], arg_s43_agg["total"])
        results["bootstrap"]["seed43"] = bootstrap_sr_diff(obs_out_43, arg_out_43, n_boot=args.n_boot)

        if obs_s43_pertask and arg_s43_pertask:
            results["paired_bootstrap"]["seed43"] = pertask_paired_bootstrap(
                obs_s43_pertask, arg_s43_pertask, n_boot=args.n_boot)

        # Pooled (both seeds combined)
        pooled_obs_s = obs_s42_agg["success"] + obs_s43_agg["success"]
        pooled_obs_t = obs_s42_agg["total"] + obs_s43_agg["total"]
        pooled_arg_s = arg_s42_agg["success"] + arg_s43_agg["success"]
        pooled_arg_t = arg_s42_agg["total"] + arg_s43_agg["total"]

        results["fisher"]["pooled"] = fisher_exact_2x2(
            pooled_obs_s, pooled_obs_t, pooled_arg_s, pooled_arg_t)

        obs_out_pooled = np.concatenate([obs_out_42, obs_out_43])
        arg_out_pooled = np.concatenate([arg_out_42, arg_out_43])
        results["bootstrap"]["pooled"] = bootstrap_sr_diff(
            obs_out_pooled, arg_out_pooled, n_boot=args.n_boot)

        # Pooled paired bootstrap (merge per-task across seeds)
        if obs_s42_pertask and arg_s42_pertask and obs_s43_pertask and arg_s43_pertask:
            common = set(obs_s42_pertask.keys()) & set(obs_s43_pertask.keys()) & \
                     set(arg_s42_pertask.keys()) & set(arg_s43_pertask.keys())
            if common:
                obs_pooled_pt = {t: {"success": obs_s42_pertask[t]["success"] + obs_s43_pertask[t]["success"],
                                     "total": obs_s42_pertask[t]["total"] + obs_s43_pertask[t]["total"]}
                                 for t in common}
                arg_pooled_pt = {t: {"success": arg_s42_pertask[t]["success"] + arg_s43_pertask[t]["success"],
                                     "total": arg_s42_pertask[t]["total"] + arg_s43_pertask[t]["total"]}
                                 for t in common}
                results["paired_bootstrap"]["pooled"] = pertask_paired_bootstrap(
                    obs_pooled_pt, arg_pooled_pt, n_boot=args.n_boot)

    # Print results
    print_results(results)

    # Save JSON
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {out_path}")


if __name__ == "__main__":
    main()
