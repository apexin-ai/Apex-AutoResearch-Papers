#!/usr/bin/env python3
"""Likelihood Ratio Test: Step vs Smooth (sigmoid) model for detection probability."""

import json
import numpy as np
from scipy.optimize import minimize
from pathlib import Path

EPS = 1e-10

# === Phase diagram data (k/n per cell) ===
PHASE_DIAGRAM = {
    5:  {0.45: (0,8), 0.50: (0,8), 0.60: (0,8), 0.75: (0,8)},
    10: {0.45: (0,8), 0.50: (6,8), 0.60: (0,8), 0.75: (6,8)},
    15: {0.45: (6,8), 0.50: (6,8), 0.60: (0,8), 0.75: (6,8)},
    20: {0.45: (5,8), 0.50: (6,8), 0.60: (0,8), 0.75: (6,8)},
    25: {0.45: (6,8), 0.50: (6,8), 0.60: (5,8), 0.75: (6,8)},
}

# Sync-dip cells: α=0.60, T≤20
SYNC_DIP = {(T, 0.60) for T in [5, 10, 15, 20]}
SYNC_DIP_DENSE_ALPHAS = {0.55, 0.60, 0.65}


def load_dense_t10():
    """Load dense T=10 data from detection_bound_results.json."""
    path = Path(__file__).parent.parent / "detection_bound" / "detection_bound_results.json"
    with open(path) as f:
        data = json.load(f)

    t10_fracs = data["signal_strength"]["t10"]
    t10_detail = data["empirical_t10_detail"]

    result = {}
    for alpha_str, frac in t10_fracs.items():
        alpha = float(alpha_str)
        n_seeds = t10_detail[alpha_str]["n_seeds"]
        n = n_seeds * 8
        k = round(frac * n)
        # Verify
        assert abs(k/n - frac) < 0.01, f"k/n mismatch at α={alpha}: {k}/{n} vs {frac}"
        result[alpha] = (k, n)

    return result


def binom_ll(k, n, p):
    """Binomial log-likelihood for single observation."""
    p = np.clip(p, EPS, 1 - EPS)
    return k * np.log(p) + (n - k) * np.log(1 - p)


def total_ll(data, pred_func):
    """Total log-likelihood over data dict {α: (k, n)}."""
    ll = 0.0
    for alpha, (k, n) in data.items():
        p = pred_func(alpha)
        ll += binom_ll(k, n, p)
    return ll


# === Step Model ===
def fit_step(data, p_max=0.75):
    """Fit step model: P = 0 if α < α_c, else p_max. Grid search over α_c."""
    alphas = sorted(data.keys())

    # Grid search: α_c can be anywhere from below min(α) to above max(α)
    candidates = np.arange(-0.05, max(alphas) + 0.1, 0.001)

    best_ll = -np.inf
    best_ac = None

    for ac in candidates:
        def pred(a, ac=ac):
            return p_max if a >= ac else EPS
        ll = total_ll(data, pred)
        if ll > best_ll:
            best_ll = ll
            best_ac = ac

    return {"alpha_c": round(best_ac, 4), "p_max": p_max, "LL": best_ll, "n_params": 1}


# === Smooth (Sigmoid) Model ===
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -500, 500)))


def fit_smooth(data, fix_pmax=None):
    """Fit smooth sigmoid model. If fix_pmax is given, fix P_max to that value."""
    alphas_arr = np.array(sorted(data.keys()))
    ks = np.array([data[a][0] for a in alphas_arr])
    ns = np.array([data[a][1] for a in alphas_arr])

    def neg_ll(params):
        if fix_pmax is not None:
            k_steep, alpha_0 = params
            pmax = fix_pmax
            n_p = 2
        else:
            k_steep, alpha_0, pmax = params
            if pmax <= 0 or pmax > 1:
                return 1e10
            n_p = 3

        ll = 0.0
        for i, a in enumerate(alphas_arr):
            p = pmax * sigmoid(k_steep * (a - alpha_0))
            p = np.clip(p, EPS, 1 - EPS)
            ll += ks[i] * np.log(p) + (ns[i] - ks[i]) * np.log(1 - p)
        return -ll

    best_result = None
    best_ll = -np.inf

    # Multi-start optimization
    for k0 in [5, 10, 20, 50, 100]:
        for a0 in np.arange(0.1, 0.9, 0.1):
            if fix_pmax is not None:
                x0 = [k0, a0]
                bounds = [(0.1, 500), (-0.5, 1.5)]
            else:
                for pm0 in [0.5, 0.75, 0.9]:
                    x0 = [k0, a0, pm0]
                    bounds = [(0.1, 500), (-0.5, 1.5), (0.01, 0.999)]
                    try:
                        res = minimize(neg_ll, x0, method='L-BFGS-B', bounds=bounds)
                        if -res.fun > best_ll:
                            best_ll = -res.fun
                            best_result = res
                    except:
                        pass
                continue

            try:
                res = minimize(neg_ll, x0, method='L-BFGS-B', bounds=bounds)
                if -res.fun > best_ll:
                    best_ll = -res.fun
                    best_result = res
            except:
                pass

    if best_result is None:
        return None

    if fix_pmax is not None:
        k_fit, a0_fit = best_result.x
        pmax_fit = fix_pmax
        n_params = 2
    else:
        k_fit, a0_fit, pmax_fit = best_result.x
        n_params = 3

    return {
        "k": round(float(k_fit), 4),
        "alpha_0": round(float(a0_fit), 4),
        "p_max": round(float(pmax_fit), 4),
        "LL": float(best_ll),
        "n_params": n_params,
    }


def compute_ic(ll, n_params, n_data):
    """Compute AIC and BIC."""
    aic = -2 * ll + 2 * n_params
    bic = -2 * ll + n_params * np.log(n_data)
    return aic, bic


def analyze_row(label, data, exclude_sync_dip=False, sync_dip_keys=None):
    """Run step vs smooth comparison for one data row."""
    if exclude_sync_dip and sync_dip_keys:
        data = {a: v for a, v in data.items() if a not in sync_dip_keys}

    n_data = len(data)

    if n_data == 0:
        return None

    # Check if all zeros
    all_zero = all(k == 0 for k, n in data.values())

    # Fit step model
    step = fit_step(data, p_max=0.75)
    step_aic, step_bic = compute_ic(step["LL"], step["n_params"], n_data)

    # Fit smooth model (P_max fixed at 0.75)
    smooth_fixed = fit_smooth(data, fix_pmax=0.75)
    if smooth_fixed:
        sf_aic, sf_bic = compute_ic(smooth_fixed["LL"], smooth_fixed["n_params"], n_data)

    # Fit smooth model (P_max free)
    smooth_free = fit_smooth(data, fix_pmax=None)
    if smooth_free:
        sfree_aic, sfree_bic = compute_ic(smooth_free["LL"], smooth_free["n_params"], n_data)

    result = {
        "label": label,
        "n_data_points": n_data,
        "n_total_trials": sum(n for k, n in data.values()),
        "all_zero": all_zero,
        "data": {str(a): {"k": int(k), "n": int(n)} for a, (k, n) in sorted(data.items())},
        "step_model": {
            "alpha_c": step["alpha_c"],
            "p_max": step["p_max"],
            "LL": round(step["LL"], 4),
            "n_params": step["n_params"],
            "AIC": round(step_aic, 4),
            "BIC": round(step_bic, 4),
        },
    }

    if smooth_fixed:
        result["smooth_pmax_fixed"] = {
            "k": smooth_fixed["k"],
            "alpha_0": smooth_fixed["alpha_0"],
            "p_max": smooth_fixed["p_max"],
            "LL": round(smooth_fixed["LL"], 4),
            "n_params": smooth_fixed["n_params"],
            "AIC": round(sf_aic, 4),
            "BIC": round(sf_bic, 4),
            "delta_AIC_vs_step": round(sf_aic - step_aic, 4),
            "delta_BIC_vs_step": round(sf_bic - step_bic, 4),
        }

    if smooth_free:
        result["smooth_pmax_free"] = {
            "k": smooth_free["k"],
            "alpha_0": smooth_free["alpha_0"],
            "p_max": smooth_free["p_max"],
            "LL": round(smooth_free["LL"], 4),
            "n_params": smooth_free["n_params"],
            "AIC": round(sfree_aic, 4),
            "BIC": round(sfree_bic, 4),
            "delta_AIC_vs_step": round(sfree_aic - step_aic, 4),
            "delta_BIC_vs_step": round(sfree_bic - step_bic, 4),
        }

    # LRT: step (nested in smooth if we view step as k→∞ sigmoid)
    # Actually step is NOT nested in smooth — they're non-nested models.
    # Use AIC/BIC for comparison. But we can still report the LL difference.
    if smooth_fixed:
        result["LR_stat_vs_fixed"] = round(2 * (smooth_fixed["LL"] - step["LL"]), 4)
    if smooth_free:
        result["LR_stat_vs_free"] = round(2 * (smooth_free["LL"] - step["LL"]), 4)

    # Preferred model
    if smooth_fixed:
        if sf_aic < step_aic:
            result["preferred_AIC"] = "smooth_fixed"
        elif sf_aic > step_aic:
            result["preferred_AIC"] = "step"
        else:
            result["preferred_AIC"] = "tie"

        if sf_bic < step_bic:
            result["preferred_BIC"] = "smooth_fixed"
        elif sf_bic > step_bic:
            result["preferred_BIC"] = "step"
        else:
            result["preferred_BIC"] = "tie"

    return result


def main():
    dense_t10 = load_dense_t10()

    results = {"version_A_excl_sync_dip": {}, "version_B_all_cells": {}}

    for version_key, exclude in [("version_B_all_cells", False), ("version_A_excl_sync_dip", True)]:
        # Phase diagram rows
        for T in [5, 10, 15, 20, 25]:
            row_data = PHASE_DIAGRAM[T]
            sync_keys = {0.60} if exclude else None
            # Only exclude sync-dip for T≤20
            if exclude and T > 20:
                sync_keys = None

            label = f"T={T}_phase"
            r = analyze_row(label, row_data, exclude_sync_dip=exclude and T <= 20, sync_dip_keys=sync_keys)
            if r:
                results[version_key][label] = r

        # Dense T=10
        sync_keys_dense = SYNC_DIP_DENSE_ALPHAS if exclude else None
        label = "T=10_dense"
        r = analyze_row(label, dense_t10, exclude_sync_dip=exclude, sync_dip_keys=sync_keys_dense)
        if r:
            results[version_key][label] = r

    # Add metadata
    results["metadata"] = {
        "description": "Shape test: Step vs Smooth (sigmoid) likelihood ratio test",
        "step_model": "P(detect|α) = 0 if α < α_c else P_max (P_max=0.75 fixed, α_c fitted)",
        "smooth_fixed": "P(detect|α) = 0.75 × sigmoid(k×(α-α_0)), 2 params (k, α_0)",
        "smooth_free": "P(detect|α) = P_max × sigmoid(k×(α-α_0)), 3 params (k, α_0, P_max)",
        "comparison": "ΔAIC/ΔBIC < 0 favors smooth; > 0 favors step",
        "version_A": "Excludes sync-dip cells (α=0.60 for T≤20; α∈{0.55,0.60,0.65} for dense)",
        "version_B": "All cells included",
        "dense_t10_n_assumption": "n = n_seeds × 8 (verified from empirical_t10_detail)",
    }

    # Save JSON
    out_dir = Path(__file__).parent
    with open(out_dir / "shape_test_results.json", "w") as f:
        json.dump(results, f, indent=2)

    # Generate analysis markdown
    md = generate_markdown(results)
    with open(out_dir / "shape_test_analysis.md", "w") as f:
        f.write(md)

    print("Done. Outputs:")
    print(f"  {out_dir / 'shape_test_results.json'}")
    print(f"  {out_dir / 'shape_test_analysis.md'}")


def generate_markdown(results):
    lines = ["# Shape Test: Step vs Smooth Likelihood Ratio Test", ""]

    for version_key, version_label in [
        ("version_B_all_cells", "Version B: All Cells"),
        ("version_A_excl_sync_dip", "Version A: Excluding Sync-Dip Cells"),
    ]:
        lines.append(f"## {version_label}")
        lines.append("")

        vdata = results[version_key]

        # Summary table
        lines.append("| Row | N | Step α_c | Step LL | Smooth(fixed) LL | Smooth(free) LL | ΔAIC(fixed) | ΔBIC(fixed) | Preferred |")
        lines.append("|-----|---|----------|---------|-----------------|-----------------|-------------|-------------|-----------|")

        for key in ["T=5_phase", "T=10_phase", "T=10_dense", "T=15_phase", "T=20_phase", "T=25_phase"]:
            if key not in vdata:
                continue
            r = vdata[key]
            n = r["n_data_points"]
            step_ll = r["step_model"]["LL"]
            step_ac = r["step_model"]["alpha_c"]

            sf_ll = r.get("smooth_pmax_fixed", {}).get("LL", "—")
            sfree_ll = r.get("smooth_pmax_free", {}).get("LL", "—")
            daic = r.get("smooth_pmax_fixed", {}).get("delta_AIC_vs_step", "—")
            dbic = r.get("smooth_pmax_fixed", {}).get("delta_BIC_vs_step", "—")
            pref = r.get("preferred_AIC", "—")

            if r.get("all_zero"):
                pref = "trivial (all 0)"

            lines.append(f"| {key} | {n} | {step_ac} | {step_ll} | {sf_ll} | {sfree_ll} | {daic} | {dbic} | {pref} |")

        lines.append("")

        # Detailed per-row
        lines.append("### Detail")
        lines.append("")

        for key in ["T=5_phase", "T=10_phase", "T=10_dense", "T=15_phase", "T=20_phase", "T=25_phase"]:
            if key not in vdata:
                continue
            r = vdata[key]
            lines.append(f"**{key}** (N={r['n_data_points']}, total trials={r['n_total_trials']})")

            if r.get("all_zero"):
                lines.append("- All cells = 0/n → both models trivially fit (LL identical). No shape information.")
                lines.append("")
                continue

            lines.append(f"- Step: α_c={r['step_model']['alpha_c']}, LL={r['step_model']['LL']}, AIC={r['step_model']['AIC']}, BIC={r['step_model']['BIC']}")

            if "smooth_pmax_fixed" in r:
                sf = r["smooth_pmax_fixed"]
                lines.append(f"- Smooth(P_max=0.75): k={sf['k']}, α_0={sf['alpha_0']}, LL={sf['LL']}, AIC={sf['AIC']}, BIC={sf['BIC']}")
                lines.append(f"  - ΔAIC={sf['delta_AIC_vs_step']} (negative favors smooth)")
                lines.append(f"  - ΔBIC={sf['delta_BIC_vs_step']}")

            if "smooth_pmax_free" in r:
                sfree = r["smooth_pmax_free"]
                lines.append(f"- Smooth(P_max free): k={sfree['k']}, α_0={sfree['alpha_0']}, P_max={sfree['p_max']}, LL={sfree['LL']}, AIC={sfree['AIC']}, BIC={sfree['BIC']}")
                lines.append(f"  - ΔAIC={sfree['delta_AIC_vs_step']}")
                lines.append(f"  - ΔBIC={sfree['delta_BIC_vs_step']}")

            lines.append("")

    # Interpretation
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- **T=5**: All cells are 0/8 — no detectable signal at any α. Both models fit trivially. No shape discrimination possible.")
    lines.append("- **ΔAIC/ΔBIC > 0**: Step model preferred (smooth's extra parameter not justified by improved fit)")
    lines.append("- **ΔAIC/ΔBIC < 0**: Smooth model preferred (gradual transition fits data better)")
    lines.append("- **Step model** has 1 free parameter (α_c), **smooth(fixed)** has 2 (k, α_0), **smooth(free)** has 3 (k, α_0, P_max)")
    lines.append("- The step model's sharp threshold is an idealization; data with n=8 per cell has limited power to distinguish sharp vs gradual transitions")
    lines.append("- Sync-dip (α=0.60) is a known structural non-monotonicity that penalizes smooth models; Version A removes it for a cleaner comparison")
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    main()
