"""TOST equivalence testing for Claude Sonnet 4 BT results."""

import json
import numpy as np
from scipy.stats import norm

DELTA = 0.10  # equivalence margin
ALPHA = 0.05
NULL_P = 0.50

DATA = {
    "formality": {"p_hat": 0.562, "n": 88, "ci_low": 0.489, "ci_high": 0.636},
    "verbosity": {"p_hat": 0.541, "n": 86, "ci_low": 0.459, "ci_high": 0.616},
}


def tost_proportion(p_hat, n, se, delta=DELTA):
    upper_bound = NULL_P + delta  # 0.60
    lower_bound = NULL_P - delta  # 0.40

    # Upper test: H0: P >= 0.60, reject if p_hat sufficiently below 0.60
    z_upper = (p_hat - upper_bound) / se
    p_upper = norm.cdf(z_upper)

    # Lower test: H0: P <= 0.40, reject if p_hat sufficiently above 0.40
    z_lower = (p_hat - lower_bound) / se
    p_lower = 1 - norm.cdf(z_lower)

    tost_p = max(p_upper, p_lower)

    # 90% CI (1 - 2*alpha) for equivalence
    ci_90_low = p_hat - norm.ppf(1 - ALPHA) * se
    ci_90_high = p_hat + norm.ppf(1 - ALPHA) * se

    equivalence_by_tost = bool(tost_p < ALPHA)
    equivalence_by_ci = bool(ci_90_low >= lower_bound and ci_90_high <= upper_bound)

    return {
        "upper_test": {"z": float(round(z_upper, 4)), "p": float(round(p_upper, 6))},
        "lower_test": {"z": float(round(z_lower, 4)), "p": float(round(p_lower, 6))},
        "tost_p": float(round(tost_p, 6)),
        "ci_90": [float(round(ci_90_low, 4)), float(round(ci_90_high, 4))],
        "equivalence_by_tost": equivalence_by_tost,
        "equivalence_by_ci": equivalence_by_ci,
        "equivalence_confirmed": equivalence_by_tost and equivalence_by_ci,
    }


def main():
    results = {"equivalence_margin": DELTA, "null_proportion": NULL_P, "alpha": ALPHA}

    for axis, d in DATA.items():
        # SE from bootstrap CI: SE ≈ (CI_upper - CI_lower) / (2 * 1.96)
        se_bootstrap = float((d["ci_high"] - d["ci_low"]) / (2 * norm.ppf(0.975)))
        se_binomial = float(np.sqrt(d["p_hat"] * (1 - d["p_hat"]) / d["n"]))

        tost = tost_proportion(d["p_hat"], d["n"], se_bootstrap)

        conclusion_parts = []
        if tost["equivalence_confirmed"]:
            conclusion_parts.append(
                f"Equivalence confirmed (TOST p={tost['tost_p']:.4f} < 0.05, "
                f"90% CI [{tost['ci_90'][0]:.3f}, {tost['ci_90'][1]:.3f}] ⊂ [0.40, 0.60])"
            )
        else:
            if not tost["equivalence_by_tost"]:
                conclusion_parts.append(f"TOST not significant (p={tost['tost_p']:.4f} >= 0.05)")
            if not tost["equivalence_by_ci"]:
                conclusion_parts.append(
                    f"90% CI [{tost['ci_90'][0]:.3f}, {tost['ci_90'][1]:.3f}] not fully within [0.40, 0.60]"
                )

        results[axis] = {
            "p_hat": d["p_hat"],
            "n_pairs": d["n"],
            "bootstrap_ci_95": [d["ci_low"], d["ci_high"]],
            "se_bootstrap": round(se_bootstrap, 5),
            "se_binomial": round(se_binomial, 5),
            **tost,
            "conclusion": "; ".join(conclusion_parts),
        }

    results["method"] = "TOST for proportions (Lakens 2017), SE from pair-level bootstrap CI"

    out_path = "data/claude_tost_equivalence.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Print summary
    for axis in DATA:
        r = results[axis]
        print(f"\n{'='*60}")
        print(f"{axis.upper()}: P(style) = {r['p_hat']}, n = {r['n_pairs']}")
        print(f"  SE (bootstrap): {r['se_bootstrap']:.5f}")
        print(f"  Upper test: z={r['upper_test']['z']:.4f}, p={r['upper_test']['p']:.6f}")
        print(f"  Lower test: z={r['lower_test']['z']:.4f}, p={r['lower_test']['p']:.6f}")
        print(f"  TOST p-value: {r['tost_p']:.6f}")
        print(f"  90% CI: [{r['ci_90'][0]:.4f}, {r['ci_90'][1]:.4f}]")
        print(f"  Equivalence margin: [{NULL_P-DELTA:.2f}, {NULL_P+DELTA:.2f}]")
        print(f"  Equivalence confirmed: {r['equivalence_confirmed']}")
        print(f"  Conclusion: {r['conclusion']}")

    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
