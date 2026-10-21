"""Aggregate P0 3-seed Llama heuristic pruning results on GSM8K (N=300).

Input:  outputs/e2e_llama_n300_clean/seed{42,123,456}_heuristic.json
Output: outputs/e2e_llama_n300_clean/3seed_aggregate.json  (+ stdout table)

Statistical tests:
  - TOST equivalence at ±1pp and ±3pp margins
  - Non-inferiority with δ=-3pp
  - McNemar's test on per-task correctness flips (pooled across seeds)
"""
import json
import os
import sys

import numpy as np
from scipy import stats

BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "outputs", "e2e_llama_n300_clean",
)
SEEDS = [42, 123, 456]
SEED_FILES = {s: os.path.join(BASE, f"seed{s}_heuristic.json") for s in SEEDS}


def load_seed(seed: int) -> dict:
    path = SEED_FILES[seed]
    if not os.path.exists(path):
        print(f"MISSING: {path}")
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def tost_p(mean_d: float, se_d: float, n: int, margin: float) -> float:
    """Two one-sided t-tests for equivalence within ±margin pp."""
    if se_d == 0:
        return 0.0
    t_upper = (mean_d - margin) / se_d
    t_lower = (mean_d + margin) / se_d
    p_upper = stats.t.cdf(t_upper, df=n - 1)
    p_lower = 1 - stats.t.cdf(t_lower, df=n - 1)
    return float(max(p_upper, p_lower))


def non_inferiority_p(mean_d: float, se_d: float, n: int, delta: float) -> float:
    """One-sided test: H0: mean_d <= delta vs H1: mean_d > delta."""
    if se_d == 0:
        return 0.0
    t_ni = (mean_d - delta) / se_d
    return float(1 - stats.t.cdf(t_ni, df=n - 1))


def mcnemar_pooled(all_per_task: list[list[dict]]) -> dict:
    """McNemar's test on baseline_correct vs pruned_correct, pooled across seeds."""
    b = 0  # baseline correct, pruned wrong
    c = 0  # baseline wrong, pruned correct
    n_agree = 0
    for per_task in all_per_task:
        for t in per_task:
            bl = t["baseline_correct"]
            pr = t["pruned_correct"]
            if bl and not pr:
                b += 1
            elif not bl and pr:
                c += 1
            else:
                n_agree += 1
    n_total = b + c + n_agree
    if b + c == 0:
        return {"b": b, "c": c, "n": n_total, "chi2": 0.0, "p": 1.0}
    chi2 = (b - c) ** 2 / (b + c)
    p = float(1 - stats.chi2.cdf(chi2, df=1))
    return {"b": b, "c": c, "n": n_total, "chi2": round(chi2, 4), "p": round(p, 6)}


def main():
    deltas, baselines, pruned_accs, suppress_rates = [], [], [], []
    per_seed = []
    all_per_task = []

    for s in SEEDS:
        d = load_seed(s)
        bl = d["baseline"]["accuracy"] * 100
        pr = d["online_pruned"]["accuracy"] * 100
        delta = d["delta_pp"]
        sr = d["online_pruned"]["suppress_pct"]
        deltas.append(delta)
        baselines.append(bl)
        pruned_accs.append(pr)
        suppress_rates.append(sr)
        all_per_task.append(d.get("per_task", []))
        per_seed.append({
            "seed": s,
            "baseline_acc": round(bl, 2),
            "pruned_acc": round(pr, 2),
            "delta_pp": delta,
            "suppression_rate": round(sr, 2),
            "num_tasks": d["baseline"]["total"],
        })
        print(f"  seed {s:5d}: baseline={bl:.2f}%, pruned={pr:.2f}%, "
              f"Δ={delta:+.2f}pp, suppress={sr:.1f}%")

    deltas = np.array(deltas)
    n = len(deltas)
    mean_d = float(np.mean(deltas))
    sd_d = float(np.std(deltas, ddof=1))
    se_d = sd_d / np.sqrt(n)

    t_crit = stats.t.ppf(0.975, df=n - 1)
    ci_lo = mean_d - t_crit * se_d
    ci_hi = mean_d + t_crit * se_d

    # TOST
    tost_1pp = tost_p(mean_d, se_d, n, 1.0)
    tost_3pp = tost_p(mean_d, se_d, n, 3.0)

    # Non-inferiority
    ni_3pp = non_inferiority_p(mean_d, se_d, n, -3.0)

    # McNemar
    mcnemar = mcnemar_pooled(all_per_task)

    # Print
    print(f"\n{'='*60}")
    print(f"3-SEED LLAMA HEURISTIC AGGREGATE (GSM8K N=300)")
    print(f"{'='*60}")
    print(f"  N seeds        = {n}")
    print(f"  Mean baseline  = {np.mean(baselines):.2f}%")
    print(f"  Mean pruned    = {np.mean(pruned_accs):.2f}%")
    print(f"  Mean Δ         = {mean_d:+.2f} pp")
    print(f"  SD(Δ)          = {sd_d:.2f} pp")
    print(f"  SE(Δ)          = {se_d:.4f} pp")
    print(f"  95% CI         = [{ci_lo:+.2f}, {ci_hi:+.2f}]  (t-based, df={n-1})")
    print(f"  Mean suppress  = {np.mean(suppress_rates):.1f}%")

    print(f"\nTOST Equivalence Tests:")
    for margin, p in [(1.0, tost_1pp), (3.0, tost_3pp)]:
        sig = "✓ EQUIVALENT" if p < 0.05 else "✗ not sig."
        print(f"  ±{margin}pp: p = {p:.6f}  {sig}")

    sig_ni = "✓ NON-INFERIOR" if ni_3pp < 0.05 else "✗ not sig."
    print(f"\nNon-inferiority (δ=-3pp): p = {ni_3pp:.8f}  {sig_ni}")

    print(f"\nMcNemar (pooled per-task):")
    print(f"  b (bl✓→pr✗) = {mcnemar['b']}, c (bl✗→pr✓) = {mcnemar['c']}")
    print(f"  χ² = {mcnemar['chi2']}, p = {mcnemar['p']}")

    aggregate = {
        "model": "Llama-3.1-8B-Instruct",
        "dataset": "GSM8K",
        "detection": "heuristic",
        "pruning_mode": "skip",
        "n_seeds": n,
        "tasks_per_seed": 300,
        "mean_delta_pp": round(mean_d, 2),
        "sd_delta_pp": round(sd_d, 2),
        "se_delta_pp": round(se_d, 4),
        "ci_95": [round(ci_lo, 2), round(ci_hi, 2)],
        "mean_baseline_acc": round(float(np.mean(baselines)), 2),
        "mean_pruned_acc": round(float(np.mean(pruned_accs)), 2),
        "mean_suppression_rate": round(float(np.mean(suppress_rates)), 1),
        "tost_1pp": round(tost_1pp, 6),
        "tost_3pp": round(tost_3pp, 6),
        "non_inferiority_3pp_p": round(ni_3pp, 8),
        "mcnemar_pooled": mcnemar,
        "per_seed": per_seed,
    }

    out_path = os.path.join(BASE, "3seed_aggregate.json")
    with open(out_path, "w") as f:
        json.dump(aggregate, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
