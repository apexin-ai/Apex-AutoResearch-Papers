"""TOST equivalence test: Conflict Δ_asym vs XNLI Δ_asym."""

import json
import math
from scipy.stats import norm

MARGIN = 0.02  # ±2pp equivalence bound

def load_conflict(model):
    with open(f"data/{model}/probe_results_bootstrap_n2000.json") as f:
        d = json.load(f)
    ap = d["asymmetry_peak"]
    return ap["mean_diff"], ap["ci_lower"], ap["ci_upper"]

def load_xnli(model):
    if model == "gemma2":
        with open("data/xnli/gemma2/probe_results_bootstrap_n2000.json") as f:
            d = json.load(f)
        a = d["asymmetry"]
        return a["mean_diff_pp"] / 100, a["ci_lo_pp"] / 100, a["ci_hi_pp"] / 100
    else:
        with open(f"data/xnli/{model}/bootstrap_asymmetry.json") as f:
            d = json.load(f)
        return d["bootstrap_mean_diff"], d["ci_95_low"], d["ci_95_high"]

def se_from_ci(ci_lo, ci_hi, z=1.96):
    return (ci_hi - ci_lo) / (2 * z)

def tost(diff, se_diff, margin):
    t1 = (diff + margin) / se_diff
    t2 = (diff - margin) / se_diff
    p1 = 1 - norm.cdf(t1)  # H0: θ <= -margin
    p2 = norm.cdf(t2)       # H0: θ >= margin
    return max(p1, p2)

def main():
    models = [
        ("Llama-3.1-8B", "llama31"),
        ("Qwen-3-8B", "qwen3"),
        ("Gemma-2-9B", "gemma2"),
    ]

    print(f"TOST Equivalence Test (margin = ±{MARGIN*100:.0f}pp)")
    print(f"H0: |Δ_conflict - Δ_xnli| >= {MARGIN*100:.0f}pp (NOT equivalent)")
    print(f"H1: |Δ_conflict - Δ_xnli| < {MARGIN*100:.0f}pp (equivalent)")
    print("=" * 72)

    rows = []
    for name, key in models:
        c_mean, c_lo, c_hi = load_conflict(key)
        x_mean, x_lo, x_hi = load_xnli(key)

        se_c = se_from_ci(c_lo, c_hi)
        se_x = se_from_ci(x_lo, x_hi)
        se_diff = math.sqrt(se_c**2 + se_x**2)

        diff = c_mean - x_mean
        p = tost(diff, se_diff, MARGIN)
        equiv = p < 0.05

        rows.append({
            "model": name,
            "conflict_delta": c_mean,
            "conflict_ci": (c_lo, c_hi),
            "xnli_delta": x_mean,
            "xnli_ci": (x_lo, x_hi),
            "diff": diff,
            "se_diff": se_diff,
            "p_tost": p,
            "equivalent": equiv,
        })

        print(f"\n{name}")
        print(f"  Conflict Δ_asym = {c_mean*100:.2f}pp  95% CI [{c_lo*100:.2f}, {c_hi*100:.2f}]")
        print(f"  XNLI    Δ_asym = {x_mean*100:.2f}pp  95% CI [{x_lo*100:.2f}, {x_hi*100:.2f}]")
        print(f"  Diff (C - X)   = {diff*100:+.2f}pp   SE = {se_diff*100:.2f}pp")
        print(f"  TOST p-value   = {p:.4f}")
        print(f"  Equivalent?    {'YES' if equiv else 'NO'} (α=0.05)")

    print("\n" + "=" * 72)
    print(f"{'Model':<18} {'Δ_conflict':>10} {'Δ_xnli':>10} {'Diff':>10} {'p_TOST':>10} {'Equiv?':>8}")
    print("-" * 72)
    for r in rows:
        print(f"{r['model']:<18} {r['conflict_delta']*100:>9.2f}% {r['xnli_delta']*100:>9.2f}% {r['diff']*100:>+9.2f}% {r['p_tost']:>10.4f} {'YES' if r['equivalent'] else 'NO':>8}")

    results = {
        "test": "TOST_equivalence",
        "margin_pp": MARGIN * 100,
        "alpha": 0.05,
        "method": "CI-derived SE (Plan A)",
        "models": {r["model"]: {
            "conflict_delta_pp": round(r["conflict_delta"] * 100, 2),
            "xnli_delta_pp": round(r["xnli_delta"] * 100, 2),
            "diff_pp": round(r["diff"] * 100, 2),
            "se_diff_pp": round(r["se_diff"] * 100, 2),
            "p_tost": round(r["p_tost"], 6),
            "equivalent": r["equivalent"],
        } for r in rows}
    }
    with open("data/tost_equivalence_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to data/tost_equivalence_results.json")

if __name__ == "__main__":
    main()
