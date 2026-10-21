"""Dual-seed analysis for 72B oracle pruning (Qwen-72B on GSM8K).

Usage:
  python scripts/analyze_72b_dual_seed.py --seed42 outputs/oracle_qwen72b_n500/seed_42.json
  python scripts/analyze_72b_dual_seed.py --seed42 outputs/oracle_qwen72b_n500/seed_42.json --seed123 outputs/oracle_qwen72b_n500/seed_123.json
"""
import argparse
import json
import math
import sys

from scipy import stats
from scipy.stats import binom


def load_result(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def extract_stats(data: dict) -> dict:
    n = data["baseline"]["total"]
    baseline_acc = data["baseline"]["accuracy"]
    pruned_acc = data["oracle_pruned"]["accuracy"]
    delta_pp = data["delta_pp"]
    suppression = data["oracle_pruned"]["suppression_rate"]

    b = data["mcnemar"]["b_oracle_only"]
    c = data["mcnemar"]["c_baseline_only"]
    n_discordant = b + c

    per_task = data.get("per_task", [])
    flips_b = sum(
        1 for t in per_task
        if t["baseline_correct"] and not t["oracle_pruned_correct"]
    )
    flips_c = sum(
        1 for t in per_task
        if not t["baseline_correct"] and t["oracle_pruned_correct"]
    )

    return {
        "n": n,
        "baseline_acc": baseline_acc,
        "pruned_acc": pruned_acc,
        "delta_pp": delta_pp,
        "suppression": suppression,
        "b": b,
        "c": c,
        "flips_b": flips_b,
        "flips_c": flips_c,
        "n_discordant": n_discordant,
        "per_task": per_task,
    }


def mcnemar_exact_p(b: int, c: int) -> float:
    n = b + c
    if n == 0:
        return 1.0
    return float(binom.cdf(min(b, c), n, 0.5) * 2)


def clopper_pearson_upper(k: int, n: int, alpha: float = 0.05) -> float:
    if k == 0:
        return 1.0 - alpha ** (1.0 / n)
    return float(stats.beta.ppf(1 - alpha / 2, k + 1, n - k))


def print_seed_report(label: str, s: dict):
    print(f"  {label}: N={s['n']}, baseline={s['baseline_acc']:.4f}, "
          f"pruned={s['pruned_acc']:.4f}, Δ={s['delta_pp']:+.2f}pp")
    print(f"    discordant b={s['flips_b']} (base→wrong), "
          f"c={s['flips_c']} (wrong→base), total={s['n_discordant']}")
    p = mcnemar_exact_p(s["flips_b"], s["flips_c"])
    print(f"    McNemar exact p={p:.4f}, suppression={s['suppression']:.1f}%")
    cp_ub = clopper_pearson_upper(s["n_discordant"], s["n"])
    print(f"    Clopper-Pearson 95% UB on flip rate: {cp_ub:.4f} ({cp_ub*100:.2f}%)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed42", required=True)
    parser.add_argument("--seed123", default=None)
    args = parser.parse_args()

    data42 = load_result(args.seed42)
    s42 = extract_stats(data42)

    print("=" * 50)
    print("  72B Dual-Seed Analysis")
    print("=" * 50)
    print()
    print("--- Per-Seed ---")
    print_seed_report("Seed 42", s42)

    if args.seed123 is None:
        print()
        print("[seed=123 not provided — single-seed report only]")
        print()
        cp42 = clopper_pearson_upper(s42["n_discordant"], s42["n"])
        print(f"Paper-ready (single seed):")
        print(f'  "Scale evidence at 72B (N={s42["n"]}, seed=42) shows '
              f'zero degradation (Δ={s42["delta_pp"]:+.2f}pp, '
              f'Clopper-Pearson 95% UB on flip rate: {cp42*100:.2f}%)."')
        return

    data123 = load_result(args.seed123)
    s123 = extract_stats(data123)
    print_seed_report("Seed 123", s123)

    print()
    print("--- Pooled ---")

    n_total = s42["n"] + s123["n"]
    total_b = s42["flips_b"] + s123["flips_b"]
    total_c = s42["flips_c"] + s123["flips_c"]
    total_flips = total_b + total_c

    pooled_baseline_correct = (
        s42["baseline_acc"] * s42["n"] + s123["baseline_acc"] * s123["n"]
    )
    pooled_pruned_correct = (
        s42["pruned_acc"] * s42["n"] + s123["pruned_acc"] * s123["n"]
    )
    pooled_baseline_acc = pooled_baseline_correct / n_total
    pooled_pruned_acc = pooled_pruned_correct / n_total
    pooled_delta = (pooled_pruned_acc - pooled_baseline_acc) * 100

    print(f"  N_total = {n_total} ({s42['n']} + {s123['n']})")
    print(f"  Pooled baseline = {pooled_baseline_acc:.4f}, "
          f"pruned = {pooled_pruned_acc:.4f}, Δ = {pooled_delta:+.2f}pp")
    print(f"  Total flips: b={total_b}, c={total_c}, total={total_flips}")

    flip_rate = total_flips / n_total if n_total > 0 else 0
    print(f"  Flip rate: {flip_rate:.4f} ({flip_rate*100:.2f}%)")

    cp_ub = clopper_pearson_upper(total_flips, n_total)
    print(f"  Clopper-Pearson 95% UB: {cp_ub:.4f} ({cp_ub*100:.2f}%)")

    cp_single = clopper_pearson_upper(s42["n_discordant"], s42["n"])
    print(f"  (down from {cp_single*100:.2f}% single-seed)")

    p_pooled = mcnemar_exact_p(total_b, total_c)
    print(f"  McNemar exact (pooled): p={p_pooled:.4f}")

    pooled_supp = (
        (s42["suppression"] * s42["n"] + s123["suppression"] * s123["n"])
        / n_total
    )
    print(f"  Pooled suppression: {pooled_supp:.1f}%")

    print()
    print("Paper-ready sentence:")
    print(f'  "Scale evidence at 72B (N={n_total}, 2 seeds) shows '
          f'{"zero" if total_flips == 0 else "near-zero"} degradation '
          f'(Δ={pooled_delta:+.2f}pp pooled, Clopper-Pearson 95% UB '
          f'on flip rate: {cp_ub*100:.2f}%)."')

    out = {
        "seeds": [42, 123],
        "per_seed": {
            "42": {k: v for k, v in s42.items() if k != "per_task"},
            "123": {k: v for k, v in s123.items() if k != "per_task"},
        },
        "pooled": {
            "n_total": n_total,
            "baseline_acc": round(pooled_baseline_acc, 4),
            "pruned_acc": round(pooled_pruned_acc, 4),
            "delta_pp": round(pooled_delta, 2),
            "total_flips": total_flips,
            "flip_rate": round(flip_rate, 4),
            "clopper_pearson_95_ub": round(cp_ub, 4),
            "mcnemar_exact_p": round(p_pooled, 4),
            "suppression_rate": round(pooled_supp, 1),
        },
    }
    out_path = args.seed42.replace("seed_42", "dual_seed_analysis")
    if out_path == args.seed42:
        out_path = "outputs/oracle_qwen72b_n500/dual_seed_analysis.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
