#!/usr/bin/env python3
"""Holm-Bonferroni correction for 5 primary comparisons (matching paper Table I.1)."""

import json
import pathlib

OUTPUT_DIR = pathlib.Path(__file__).parent


def holm_bonferroni(comparisons, alpha=0.05):
    """Simple Holm-Bonferroni: adj_p = raw_p × (k - rank + 1).

    Uses step-down rejection (reject while p_(i) < α/(k-i+1)) for significance,
    and simple multiplication for adjusted p-values (matching paper Table I.1).
    With tied p-values, the strict monotonicity-enforced variant would give
    both ties the larger adj_p; we report simple multiplication per the paper.
    Significance conclusions are identical under either convention.
    """
    k = len(comparisons)
    sorted_comps = sorted(comparisons, key=lambda x: x["raw_p"])

    rejected_so_far = True
    for i, comp in enumerate(sorted_comps):
        rank = i + 1
        comp["adj_p"] = min(comp["raw_p"] * (k - rank + 1), 1.0)
        comp["rank"] = rank
        comp["multiplier"] = k - rank + 1
        threshold = alpha / (k - rank + 1)
        if rejected_so_far and comp["raw_p"] <= threshold:
            comp["significant"] = True
        else:
            comp["significant"] = False
            rejected_so_far = False

    return sorted_comps


comparisons = [
    {"name": "Repo: CLS vs CWM (Qwen3-8B)",     "raw_p": 0.003, "level": "repo",     "note": "paired bootstrap, diff=+29.17pp"},
    {"name": "Func: CLS vs CWM (TOST ±2pp)",    "raw_p": 0.007, "level": "function", "note": "seed-level paired t-test, 5 seeds (same as clustered bootstrap)"},
    {"name": "Func: CLS vs TRAJ (TOST ±2pp)",   "raw_p": 0.025, "level": "function", "note": "seed-level paired t-test, 5 seeds, df=4"},
    {"name": "Repo: CWM vs TRAJ (Qwen3-8B)",    "raw_p": 0.039, "level": "repo",     "note": "unpaired bootstrap, diff=-20.83pp"},
    {"name": "Repo: CLS vs TRAJ (Qwen3-8B)",    "raw_p": 0.385, "level": "repo",     "note": "unpaired bootstrap, diff=+8.33pp"},
]

results = holm_bonferroni(comparisons)

print(f"Holm-Bonferroni Correction (k={len(comparisons)}, α=0.05)")
print("=" * 100)
print(f"{'Rank':<5} {'Comparison':<38} {'Raw p':>8} {'×':>3} {'Adj p':>8} {'Sig?':>6}  {'Note'}")
print("-" * 100)
for r in results:
    sig_str = "YES" if r["significant"] else "no"
    print(f"{r['rank']:<5} {r['name']:<38} {r['raw_p']:>8.4f} {r['multiplier']:>3} {r['adj_p']:>8.4f} {sig_str:>6}  {r['note']}")
print("-" * 100)

n_sig = sum(1 for r in results if r["significant"])
print(f"\n{n_sig}/{len(results)} comparisons remain significant after correction.")

for r in results:
    assert r["adj_p"] >= r["raw_p"], f"adj_p < raw_p for {r['name']}"

output = {
    "method": "Holm-Bonferroni",
    "k": len(comparisons),
    "alpha": 0.05,
    "results": [
        {
            "rank": r["rank"],
            "comparison": r["name"],
            "level": r["level"],
            "raw_p": r["raw_p"],
            "multiplier": r["multiplier"],
            "adj_p": round(r["adj_p"], 4),
            "significant": r["significant"],
            "note": r["note"],
        }
        for r in results
    ],
}

out_path = OUTPUT_DIR / "holm_bonferroni_results.json"
out_path.write_text(json.dumps(output, indent=2) + "\n")
print(f"\nSaved to {out_path}")
