"""TOST equivalence test: Conflict delta_asym vs XNLI delta_asym."""

import argparse
import json
import math
from pathlib import Path
from scipy.stats import norm


MARGIN = 0.02


def se_from_ci(ci_lo, ci_hi, z=1.96):
    return (ci_hi - ci_lo) / (2 * z)


def tost(diff, se_diff, margin):
    t1 = (diff + margin) / se_diff
    t2 = (diff - margin) / se_diff
    p1 = 1 - norm.cdf(t1)
    p2 = norm.cdf(t2)
    return max(p1, p2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", type=str, required=True,
                        help='JSON: [{"name": "...", "key": "...", "conflict_bootstrap": "path", "xnli_bootstrap": "path"}]')
    parser.add_argument("--output", type=str, default="results/tost_equivalence_results.json")
    parser.add_argument("--margin", type=float, default=0.02)
    args = parser.parse_args()

    margin = args.margin
    models = json.loads(args.models)

    print(f"TOST Equivalence Test (margin = +/-{margin*100:.0f}pp)")
    print("=" * 72)

    rows = []
    for entry in models:
        name = entry["name"]

        with open(entry["conflict_bootstrap"]) as f:
            cd = json.load(f)
        c_mean = cd["asymmetry_peak"]["mean_diff"]
        c_lo = cd["asymmetry_peak"]["ci_lower"]
        c_hi = cd["asymmetry_peak"]["ci_upper"]

        with open(entry["xnli_bootstrap"]) as f:
            xd = json.load(f)
        if "asymmetry" in xd:
            x_mean = xd["asymmetry"]["mean_diff_pp"] / 100
            x_lo = xd["asymmetry"]["ci_lo_pp"] / 100
            x_hi = xd["asymmetry"]["ci_hi_pp"] / 100
        else:
            x_mean = xd["bootstrap_mean_diff"]
            x_lo = xd["ci_95_low"]
            x_hi = xd["ci_95_high"]

        se_c = se_from_ci(c_lo, c_hi)
        se_x = se_from_ci(x_lo, x_hi)
        se_diff = math.sqrt(se_c**2 + se_x**2)
        diff = c_mean - x_mean
        p = tost(diff, se_diff, margin)
        equiv = p < 0.05

        rows.append({
            "model": name,
            "conflict_delta_pp": round(c_mean * 100, 2),
            "xnli_delta_pp": round(x_mean * 100, 2),
            "diff_pp": round(diff * 100, 2),
            "p_tost": round(p, 6),
            "equivalent": equiv,
        })

        print(f"\n{name}")
        print(f"  Conflict delta = {c_mean*100:.2f}pp")
        print(f"  XNLI delta     = {x_mean*100:.2f}pp")
        print(f"  TOST p-value   = {p:.4f}")
        print(f"  Equivalent?    {'YES' if equiv else 'NO'}")

    results = {"test": "TOST_equivalence", "margin_pp": margin * 100, "models": {r["model"]: r for r in rows}}
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
