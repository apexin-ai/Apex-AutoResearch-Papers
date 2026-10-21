#!/usr/bin/env python3
"""Cinelli & Hazlett (2020) OVB Sensitivity Analysis for K_eff coefficient.

Extracts OLS statistics from existing regression results and computes:
  - Robustness Value (RV_q=1) for K_eff coefficient
  - Benchmark eta_max partial R² with treatment and outcome
  - Contour plots of adjusted K_eff coefficient

Output:
  - artifacts/results/plan001/sensitivity_analysis.json
  - artifacts/figures/sensitivity_contour_K{k}.png
"""

import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
FIG_DIR = Path("/root/cert_manip_resist_eval/artifacts/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)

DATASETS = ["mmlu", "arc_challenge"]
ATTACKS = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]
ATTACK_SHORT = {
    "prompt_injection": "PromptInj",
    "sycophancy": "Sycoph",
    "score_manipulation": "ScoreManip",
    "verbosity_bias": "Verbose",
    "position_bias": "Position",
    "authority_bias": "Authority",
}
DS_SHORT = {"mmlu": "MMLU", "arc_challenge": "ARC"}


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


# ── Cinelli & Hazlett (2020) Formulas ────────────────────────────────

def partial_r2_from_t(t_stat, dof):
    return t_stat**2 / (t_stat**2 + dof)


def robustness_value(t_stat, dof, q=1.0):
    """RV_q: minimum confounder strength (equal partial R² with D and Y)
    needed to reduce |beta| by factor q. q=1 means zeroing out."""
    f2 = (q * t_stat)**2 / dof
    rv = 0.5 * (np.sqrt(f2**2 + 4 * f2) - f2)
    return rv


def adjusted_estimate(estimate, se, dof, r2dz_x, r2yz_dx):
    """Bias-adjusted estimate (Cinelli & Hazlett 2020, Eq. 9).
    Assumes confounding direction reduces |estimate| (reduce=True)."""
    bf = np.sqrt(r2yz_dx * r2dz_x / np.maximum(1 - r2dz_x, 1e-10))
    return np.sign(estimate) * (np.abs(estimate) - bf * se * np.sqrt(dof))


def adjusted_t_stat(t_stat, dof, r2dz_x, r2yz_dx):
    """Bias-adjusted t-statistic."""
    f2 = r2yz_dx * r2dz_x / np.maximum(1 - r2dz_x, 1e-10)
    num = np.abs(t_stat) / np.sqrt(dof) - np.sqrt(f2)
    den = np.sqrt((1 - r2yz_dx) / np.maximum(1 - r2dz_x, 1e-10))
    return np.sign(t_stat) * num / np.maximum(den, 1e-10) * np.sqrt(dof)


# ── Load Existing Results ────────────────────────────────────────────

def load_k3_results():
    path = RESULTS_DIR / "panel_regression" / "step4_regression_results.json"
    with open(path) as f:
        data = json.load(f)
    results = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            cd = data["conditions"].get(cond)
            if cd is None or cd.get("skipped"):
                continue
            n = cd["n_panels"]
            dof = n - 3
            t_keff = cd["ols"]["keff_t"]
            beta_keff = cd["ols"]["keff_beta"]
            se_keff = beta_keff / t_keff if abs(t_keff) > 1e-10 else 0.0
            t_eta = cd["ols"]["eta_max_t"]
            vif = cd.get("vif_keff", 1.0)
            r2dz_eta = max(0.0, 1 - 1 / vif) if vif > 1 else 0.0
            results[cond] = dict(
                K=3, n_panels=n, dof=dof,
                beta_keff=beta_keff, se_keff=se_keff, t_keff=t_keff,
                beta_eta=cd["ols"]["eta_max_beta"], t_eta=t_eta,
                R2=cd["ols"]["R2"], r2dz_eta=r2dz_eta,
            )
    return results


def load_k5k7_results():
    path = RESULTS_DIR / "k5_k7_panel_analysis.json"
    with open(path) as f:
        data = json.load(f)
    results = {}
    for kkey in ["K5", "K7"]:
        entry = data["results"][kkey]
        K = entry["K"]
        for cond_key, cd in entry["conditions"].items():
            n = cd["n_panels"]
            dof = n - 3
            ols = cd["ols"]
            beta_keff = ols["beta_keff"]
            se_keff = ols["se_keff"]
            t_keff = beta_keff / se_keff if abs(se_keff) > 1e-10 else 0.0
            beta_eta = ols["beta_eta"]
            se_eta = ols["se_eta"]
            t_eta = beta_eta / se_eta if abs(se_eta) > 1e-10 else 0.0

            keff_std = ols.get("keff_std_beta", 0)
            eta_std = ols.get("eta_std_beta", 0)
            R2 = ols["R2"]
            denom = 2 * keff_std * eta_std
            if abs(denom) > 1e-10:
                c = (R2 - keff_std**2 - eta_std**2) / denom
                c = np.clip(c, -1, 1)
                r2dz_eta = c**2
            else:
                r2dz_eta = 0.0

            results[(K, cond_key)] = dict(
                K=K, n_panels=n, dof=dof,
                beta_keff=beta_keff, se_keff=se_keff, t_keff=t_keff,
                beta_eta=beta_eta, t_eta=t_eta,
                R2=R2, r2dz_eta=r2dz_eta,
            )
    return results


# ── Sensitivity Analysis ─────────────────────────────────────────────

def analyze_condition(stats):
    t = stats["t_keff"]
    dof = stats["dof"]
    se = stats["se_keff"]
    beta = stats["beta_keff"]
    t_eta = stats["t_eta"]

    pr2_keff = partial_r2_from_t(t, dof)
    pr2_eta = partial_r2_from_t(t_eta, dof)
    rv = robustness_value(t, dof, q=1.0)

    r2dz_eta = stats["r2dz_eta"]
    r2ydz_eta = pr2_eta

    rv_exceeds = rv > max(r2dz_eta, r2ydz_eta)

    return dict(
        K=stats["K"],
        n_panels=stats["n_panels"],
        dof=dof,
        beta_keff=beta,
        se_keff=se,
        t_keff=t,
        partial_r2_keff=pr2_keff,
        keff_rv=rv,
        eta_partial_r2_treatment=r2dz_eta,
        eta_partial_r2_outcome=r2ydz_eta,
        rv_exceeds_eta=rv_exceeds,
        R2=stats["R2"],
    )


# ── Contour Plot ─────────────────────────────────────────────────────

def plot_contour_grid(results_by_cond, K, out_path):
    """4×3 contour plot grid for 12 conditions at a given K."""
    fig, axes = plt.subplots(4, 3, figsize=(14, 16))
    fig.suptitle(
        f"Cinelli–Hazlett Sensitivity Analysis: K={K}",
        fontsize=14, fontweight="bold", y=0.98,
    )

    grid_n = 200
    conditions = []
    for ds in DATASETS:
        for atk in ATTACKS:
            conditions.append(f"{ds}x{atk}")

    for idx, cond in enumerate(conditions):
        row, col = divmod(idx, 3)
        ax = axes[row, col]
        r = results_by_cond.get(cond)
        if r is None:
            ax.set_visible(False)
            continue

        rv = r["keff_rv"]
        bm_x = r["eta_partial_r2_treatment"]
        bm_y = r["eta_partial_r2_outcome"]
        beta = r["beta_keff"]
        se = r["se_keff"]
        dof = r["dof"]

        x_max = min(0.99, max(0.7, 1.5 * max(rv, bm_x, 0.1)))
        y_max = min(0.99, max(0.7, 1.5 * max(rv, bm_y, 0.1)))

        rx = np.linspace(0.001, x_max, grid_n)
        ry = np.linspace(0.001, y_max, grid_n)
        RX, RY = np.meshgrid(rx, ry)

        ADJ = adjusted_estimate(beta, se, dof, RX, RY)

        n_levels = 12
        vmin = np.nanmin(ADJ)
        vmax = np.nanmax(ADJ)
        if vmin < 0 < vmax:
            neg_levels = np.linspace(vmin, 0, max(2, n_levels // 3 + 1))
            pos_levels = np.linspace(0, vmax, max(2, n_levels * 2 // 3 + 1))
            levels = np.unique(np.concatenate([neg_levels, pos_levels]))
        else:
            levels = np.linspace(vmin, vmax, n_levels)

        cs = ax.contourf(RX, RY, ADJ, levels=levels, cmap="RdBu_r", alpha=0.85)
        ax.contour(RX, RY, ADJ, levels=[0.0], colors="black", linewidths=2)

        ax.plot(bm_x, bm_y, "D", color="limegreen", markersize=7,
                markeredgecolor="black", markeredgewidth=0.8, zorder=5)
        ax.annotate(r"$\eta_{\max}$", (bm_x, bm_y),
                    textcoords="offset points", xytext=(6, 6),
                    fontsize=8, fontweight="bold", color="black")

        rv_theta = np.linspace(0, np.pi / 2, 100)
        rv_x = rv * np.cos(rv_theta)
        rv_y = rv * np.sin(rv_theta)
        mask = (rv_x <= x_max) & (rv_y <= y_max)
        if mask.any():
            ax.plot(rv_x[mask], rv_y[mask], "--", color="darkorange",
                    linewidth=1.5, label=f"RV={rv:.3f}")

        ds_name, atk_name = cond.split("x")
        title = f"{DS_SHORT[ds_name]} × {ATTACK_SHORT[atk_name]}"
        ax.set_title(title, fontsize=9, fontweight="bold")
        ax.set_xlabel(r"$R^2_{D \sim Z | X}$", fontsize=8)
        ax.set_ylabel(r"$R^2_{Y \sim Z | D,X}$", fontsize=8)
        ax.tick_params(labelsize=7)
        ax.set_xlim(0, x_max)
        ax.set_ylim(0, y_max)

        info = f"RV={rv:.3f}\n" + r"$\beta$" + f"={beta:.2f}"
        ax.text(0.97, 0.97, info, transform=ax.transAxes,
                fontsize=7, va="top", ha="right",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8))

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out_path}")


# ── Main ─────────────────────────────────────────────────────────────

def main():
    print("Loading K=3 results...")
    k3 = load_k3_results()
    print(f"  K=3: {len(k3)} conditions")

    print("Loading K=5,7 results...")
    k5k7 = load_k5k7_results()
    k5 = {k: v for (K, k), v in k5k7.items() if K == 5}
    k7 = {k: v for (K, k), v in k5k7.items() if K == 7}
    print(f"  K=5: {len(k5)} conditions, K=7: {len(k7)} conditions")

    all_results = []
    results_by_K = {3: {}, 5: {}, 7: {}}

    for K, source in [(3, k3), (5, k5), (7, k7)]:
        for cond_key, stats in source.items():
            r = analyze_condition(stats)
            ds, atk = cond_key.split("x")
            entry = dict(K=K, benchmark=ds, attack=atk, **r)
            all_results.append(entry)
            results_by_K[K][cond_key] = r

    # Verification: print first condition
    first = all_results[0]
    print(f"\nVerification (K={first['K']}, {first['benchmark']}x{first['attack']}):")
    print(f"  beta_keff = {first['beta_keff']:.4f}")
    print(f"  t_keff    = {first['t_keff']:.4f}")
    print(f"  dof       = {first['dof']}")
    print(f"  partial_r2_keff = {first['partial_r2_keff']:.4f}")
    print(f"  RV(q=1)   = {first['keff_rv']:.4f}")
    # Manual check: f2 = t^2/dof, RV = 0.5*(sqrt(f4+4f2) - f2)
    t = first["t_keff"]
    dof = first["dof"]
    f2 = t**2 / dof
    rv_check = 0.5 * (np.sqrt(f2**2 + 4*f2) - f2)
    print(f"  RV manual = {rv_check:.4f} (should match)")
    print(f"  eta_partial_r2_treatment = {first['eta_partial_r2_treatment']:.4f}")
    print(f"  eta_partial_r2_outcome   = {first['eta_partial_r2_outcome']:.4f}")
    print(f"  rv_exceeds_eta = {first['rv_exceeds_eta']}")

    # Summary
    rv_exceeds_count = sum(1 for r in all_results if r["rv_exceeds_eta"])
    by_K = {}
    for K in [3, 5, 7]:
        k_results = [r for r in all_results if r["K"] == K]
        by_K[f"K{K}"] = f"{sum(1 for r in k_results if r['rv_exceeds_eta'])}/{len(k_results)}"

    summary = {
        "rv_exceeds_eta_count": f"{rv_exceeds_count}/{len(all_results)}",
        "by_K": by_K,
    }

    print(f"\nSummary: {summary['rv_exceeds_eta_count']} conditions RV > eta benchmarks")
    for k, v in by_K.items():
        print(f"  {k}: {v}")

    # Save JSON
    output = {
        "method": "Cinelli & Hazlett (2020)",
        "description": "OVB Sensitivity Analysis for K_eff coefficient",
        "formulas": {
            "partial_r2": "t^2 / (t^2 + dof)",
            "RV_q1": "0.5 * (sqrt(f^4 + 4*f^2) - f^2), f^2 = t^2/dof",
            "adjusted_estimate": "sign(b)*(|b| - sqrt(r2yz*r2dz/(1-r2dz))*se*sqrt(dof))",
        },
        "results_by_condition": all_results,
        "summary": summary,
    }

    out_path = RESULTS_DIR / "sensitivity_analysis.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default)
    print(f"\nSaved: {out_path}")

    # Contour plots
    for K in [3, 5, 7]:
        fig_path = FIG_DIR / f"sensitivity_contour_K{K}.png"
        plot_contour_grid(results_by_K[K], K, fig_path)

    print("\nDone.")


if __name__ == "__main__":
    main()
