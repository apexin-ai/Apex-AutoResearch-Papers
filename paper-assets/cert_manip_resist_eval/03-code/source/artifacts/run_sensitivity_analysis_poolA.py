#!/usr/bin/env python3
"""Cinelli & Hazlett (2020) OVB Sensitivity Analysis for Pool A (9 capability-matched models).

Reads pre-computed regression results from capability_matched_subsample.json (strategy_a),
computes RV, benchmark partial R^2, and rv_exceeds_eta for K=3 (84 panels) and K=5 (126 panels).

Output: artifacts/results/plan001/sensitivity_analysis_poolA.json
"""

import json
import numpy as np
from pathlib import Path

RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")

DATASETS = ["mmlu", "arc_challenge"]
ATTACKS = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]


def _json_default(obj):
    if isinstance(obj, np.floating):
        v = float(obj)
        return None if (np.isnan(v) or np.isinf(v)) else v
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.bool_):
        return bool(obj)
    raise TypeError(f"Not JSON serializable: {type(obj)}")


def partial_r2_from_t(t_stat, dof):
    return t_stat**2 / (t_stat**2 + dof)


def robustness_value(t_stat, dof, q=1.0):
    f2 = (q * t_stat)**2 / dof
    rv = 0.5 * (np.sqrt(f2**2 + 4 * f2) - f2)
    return rv


def compute_interpredictor_r2(R2_full, partial_r2_keff, partial_r2_eta):
    """Recover r^2(K_eff, eta_max) from regression statistics.

    Uses: R^2_{eta only} = 1 - (1-R^2_full)/(1-partial_r2_keff)
          R^2_{keff only} = 1 - (1-R^2_full)/(1-partial_r2_eta)
    Then solves quadratic: R^2_full*(1-c^2) = a + b - 2*c*sqrt(a*b)
    where a = R^2_{keff only}, b = R^2_{eta only}, c = r_12.
    Returns the smaller root c^2 (= r2dz_eta = VIF-based benchmark).
    """
    denom_k = 1 - partial_r2_keff
    denom_e = 1 - partial_r2_eta
    if denom_k < 1e-10 or denom_e < 1e-10:
        return 0.0

    r2_eta_only = 1 - (1 - R2_full) / denom_k
    r2_keff_only = 1 - (1 - R2_full) / denom_e

    r2_eta_only = np.clip(r2_eta_only, 0, 1)
    r2_keff_only = np.clip(r2_keff_only, 0, 1)

    a, b, F = r2_keff_only, r2_eta_only, R2_full
    sqab = np.sqrt(a * b)

    # F*c^2 - 2*sqab*c + (a+b-F) = 0
    A_coef = F
    B_coef = -2 * sqab
    C_coef = a + b - F

    if abs(A_coef) < 1e-10:
        if abs(B_coef) > 1e-10:
            c = -C_coef / B_coef
            return np.clip(c**2, 0, 1)
        return 0.0

    disc = B_coef**2 - 4 * A_coef * C_coef
    if disc < 0:
        return 0.0

    sqrt_disc = np.sqrt(disc)
    c1 = (-B_coef + sqrt_disc) / (2 * A_coef)
    c2 = (-B_coef - sqrt_disc) / (2 * A_coef)

    # Pick the smaller valid root (less extreme collinearity)
    candidates = []
    for c in [c1, c2]:
        if -1 <= c <= 1:
            candidates.append(c**2)
    if not candidates:
        return 0.0
    return min(candidates)


def analyze_condition(beta_keff, se_keff, beta_eta, se_eta, R2, n_panels, K):
    dof = n_panels - 3
    t_keff = beta_keff / se_keff if abs(se_keff) > 1e-10 else 0.0
    t_eta = beta_eta / se_eta if abs(se_eta) > 1e-10 else 0.0

    pr2_keff = partial_r2_from_t(t_keff, dof)
    pr2_eta = partial_r2_from_t(t_eta, dof)
    rv = robustness_value(t_keff, dof, q=1.0)

    r2dz_eta = compute_interpredictor_r2(R2, pr2_keff, pr2_eta)

    rv_exceeds = rv > max(r2dz_eta, pr2_eta)

    return dict(
        K=K,
        n_panels=n_panels,
        dof=dof,
        beta_keff=beta_keff,
        se_keff=se_keff,
        t_keff=t_keff,
        partial_r2_keff=pr2_keff,
        keff_rv=rv,
        eta_partial_r2_treatment=r2dz_eta,
        eta_partial_r2_outcome=pr2_eta,
        rv_exceeds_eta=rv_exceeds,
        R2=R2,
    )


def load_pool_a_data():
    path = RESULTS_DIR / "capability_matched_subsample.json"
    with open(path) as f:
        data = json.load(f)
    sa = data["strategy_a"]
    results = {}

    for K_key, K_val in [("K3", 3), ("K5", 5)]:
        k_data = sa[K_key]
        for ds in DATASETS:
            for atk in ATTACKS:
                cond = f"{ds}x{atk}"
                cd = k_data["conditions"].get(cond)
                if cd is None:
                    continue
                ols = cd["ols"]
                cl = cd["clustered"]
                beta_keff = ols["beta_keff"]
                beta_eta = ols["beta_eta"]
                se_keff = cl["ols_se"][1]
                se_eta = cl["ols_se"][2]
                R2 = ols["R2"]
                n_panels = ols["n_panels"]
                results[(K_val, cond)] = dict(
                    beta_keff=beta_keff, se_keff=se_keff,
                    beta_eta=beta_eta, se_eta=se_eta,
                    R2=R2, n_panels=n_panels, K=K_val,
                )
    return results


def main():
    print("Loading Pool A regression data...")
    raw = load_pool_a_data()
    k3_count = sum(1 for (K, _) in raw if K == 3)
    k5_count = sum(1 for (K, _) in raw if K == 5)
    print(f"  K=3: {k3_count} conditions, K=5: {k5_count} conditions")

    all_results = []
    for (K, cond_key), stats in sorted(raw.items()):
        r = analyze_condition(
            stats["beta_keff"], stats["se_keff"],
            stats["beta_eta"], stats["se_eta"],
            stats["R2"], stats["n_panels"], K,
        )
        ds, atk = cond_key.split("x")
        entry = dict(**r, benchmark=ds, attack=atk)
        all_results.append(entry)

    # Verification
    first = all_results[0]
    print(f"\nVerification (K={first['K']}, {first['benchmark']}x{first['attack']}):")
    print(f"  beta_keff = {first['beta_keff']:.4f}")
    print(f"  t_keff    = {first['t_keff']:.4f}")
    print(f"  dof       = {first['dof']}")
    print(f"  partial_r2_keff = {first['partial_r2_keff']:.4f}")
    print(f"  RV(q=1)   = {first['keff_rv']:.4f}")
    print(f"  eta_partial_r2_treatment = {first['eta_partial_r2_treatment']:.4f}")
    print(f"  eta_partial_r2_outcome   = {first['eta_partial_r2_outcome']:.4f}")
    print(f"  rv_exceeds_eta = {first['rv_exceeds_eta']}")

    # Summary
    rv_exceeds_count = sum(1 for r in all_results if r["rv_exceeds_eta"])
    by_K = {}
    for K in [3, 5]:
        k_results = [r for r in all_results if r["K"] == K]
        by_K[f"K{K}"] = f"{sum(1 for r in k_results if r['rv_exceeds_eta'])}/{len(k_results)}"

    summary = {
        "rv_exceeds_eta_count": f"{rv_exceeds_count}/{len(all_results)}",
        "by_K": by_K,
    }

    print(f"\nPool A Summary: {summary['rv_exceeds_eta_count']} conditions RV > eta benchmarks")
    for k, v in by_K.items():
        print(f"  {k}: {v}")

    # Per-condition details
    print("\n--- Per-condition RV ---")
    print(f"{'K':>2} {'Condition':<30} {'RV':>8} {'eta_r2_treat':>12} {'eta_r2_out':>10} {'exceeds':>8}")
    for r in all_results:
        cond = f"{r['benchmark']}x{r['attack']}"
        print(f"{r['K']:>2} {cond:<30} {r['keff_rv']:>8.4f} {r['eta_partial_r2_treatment']:>12.4f} {r['eta_partial_r2_outcome']:>10.4f} {str(r['rv_exceeds_eta']):>8}")

    # Save
    output = {
        "method": "Cinelli & Hazlett (2020)",
        "description": "OVB Sensitivity Analysis for K_eff coefficient - Pool A (9 capability-matched models)",
        "pool": "strategy_a",
        "n_models": 9,
        "models": [
            "gpt-4.1", "claude-sonnet-4-6", "gpt-4.1-mini",
            "gemini-3.5-flash", "gpt-4.1-nano", "llama3.1-70b",
            "mistral-large", "qwen2.5-32b", "qwen2.5-72b",
        ],
        "formulas": {
            "partial_r2": "t^2 / (t^2 + dof)",
            "RV_q1": "0.5 * (sqrt(f^4 + 4*f^2) - f^2), f^2 = t^2/dof",
            "r2dz_eta": "recovered from regression R^2 + partial R^2s via quadratic",
        },
        "results_by_condition": all_results,
        "summary": summary,
    }

    out_path = RESULTS_DIR / "sensitivity_analysis_poolA.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
