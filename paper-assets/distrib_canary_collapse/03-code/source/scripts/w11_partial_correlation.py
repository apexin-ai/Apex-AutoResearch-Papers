#!/usr/bin/env python3
"""W11: Partial correlation analysis controlling for generation number."""

import json
import os
import math
import numpy as np
from scipy import stats
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

BASE = Path("/root/autodl-tmp/distrib_canary_collapse")
RESULTS = BASE / "results" / "alpha_sweep"
OUT_JSON = BASE / "results" / "w11_partial_correlation_results.json"
OUT_FIG_DIR = BASE / "results" / "w11_figures"

CONDITIONS = [
    {"alpha": 0.0, "seeds": [42, 43, 44], "prefix": "a000"},
    {"alpha": 0.50, "seeds": [42, 43, 44], "prefix": "a050"},
    {"alpha": 0.75, "seeds": [42, 43, 44], "prefix": "a075"},
]

CANARIES = ["token_entropy", "ece"]
DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3"]


def load_metrics(alpha_prefix, seed):
    path = RESULTS / f"{alpha_prefix}_s{seed}" / "all_metrics.json"
    with open(path) as f:
        data = json.load(f)
    data.sort(key=lambda x: x["generation"])
    return data


def extract_series(data, metric):
    return np.array([d[metric] for d in data])


def pearson_with_p(x, y):
    if len(x) < 3:
        return np.nan, np.nan
    r, p = stats.pearsonr(x, y)
    return r, p


def partial_corr(x, y, z):
    """Partial correlation r(x,y|z) using formula."""
    if len(x) < 4:
        return np.nan, np.nan
    r_xy, _ = stats.pearsonr(x, y)
    r_xz, _ = stats.pearsonr(x, z)
    r_yz, _ = stats.pearsonr(y, z)
    denom = math.sqrt((1 - r_xz**2) * (1 - r_yz**2))
    if denom < 1e-12:
        return np.nan, np.nan
    r_partial = (r_xy - r_xz * r_yz) / denom
    n = len(x)
    df = n - 3
    if df < 1 or abs(r_partial) >= 1.0:
        return r_partial, np.nan
    t_stat = r_partial * math.sqrt(df / (1 - r_partial**2))
    p_val = 2 * stats.t.sf(abs(t_stat), df)
    return r_partial, p_val


def analyze_condition(alpha, seed, prefix):
    data = load_metrics(prefix, seed)
    T = len(data)
    gen = np.arange(T, dtype=float)
    results = []

    for canary in CANARIES:
        c_series = extract_series(data, canary)
        for downstream in DOWNSTREAMS:
            d_series = extract_series(data, downstream)

            # Zero-order correlation
            r0, p0 = pearson_with_p(c_series, d_series)

            # Partial correlation controlling for generation
            r_part, p_part = partial_corr(c_series, d_series, gen)

            # Lagged: canary[t] vs downstream[t+1], controlling for t
            c_lag = c_series[:-1]
            d_lag = d_series[1:]
            gen_lag = gen[:-1]

            r_lag0, p_lag0 = pearson_with_p(c_lag, d_lag)
            r_lag_part, p_lag_part = partial_corr(c_lag, d_lag, gen_lag)

            r_reduction = (
                (1 - abs(r_part) / abs(r0)) * 100
                if (not np.isnan(r0) and abs(r0) > 1e-9)
                else np.nan
            )
            r_lag_reduction = (
                (1 - abs(r_lag_part) / abs(r_lag0)) * 100
                if (not np.isnan(r_lag0) and abs(r_lag0) > 1e-9)
                else np.nan
            )

            results.append({
                "canary": canary,
                "downstream": downstream,
                "alpha": alpha,
                "seed": seed,
                "T": T,
                "zero_order_r": round(r0, 4) if not np.isnan(r0) else None,
                "zero_order_p": round(p0, 6) if not np.isnan(p0) else None,
                "partial_r": round(r_part, 4) if not np.isnan(r_part) else None,
                "partial_p": round(p_part, 6) if not np.isnan(p_part) else None,
                "r_reduction_pct": round(r_reduction, 1) if not np.isnan(r_reduction) else None,
                "lagged_zero_order_r": round(r_lag0, 4) if not np.isnan(r_lag0) else None,
                "lagged_zero_order_p": round(p_lag0, 6) if not np.isnan(p_lag0) else None,
                "lagged_partial_r": round(r_lag_part, 4) if not np.isnan(r_lag_part) else None,
                "lagged_partial_p": round(p_lag_part, 6) if not np.isnan(p_lag_part) else None,
                "lagged_r_reduction_pct": round(r_lag_reduction, 1) if not np.isnan(r_lag_reduction) else None,
            })
    return results


def compute_summary(all_results):
    detection = [r for r in all_results if r["alpha"] >= 0.50]
    null = [r for r in all_results if r["alpha"] == 0.0]

    def _stats(subset, key_r, key_p, key_red):
        rs = [abs(r[key_r]) for r in subset if r[key_r] is not None]
        ps = [r[key_p] for r in subset if r[key_p] is not None]
        reds = [r[key_red] for r in subset if r[key_red] is not None]
        sig = sum(1 for p in ps if p < 0.05)
        return {
            "n": len(rs),
            "mean_abs_r": round(np.mean(rs), 4) if rs else None,
            "sig_count": sig,
            "sig_fraction": round(sig / len(ps), 3) if ps else None,
            "mean_r_reduction_pct": round(np.mean(reds), 1) if reds else None,
            "median_r_reduction_pct": round(np.median(reds), 1) if reds else None,
        }

    summary = {
        "detection_conditions": {
            "zero_order": _stats(detection, "zero_order_r", "zero_order_p", "r_reduction_pct"),
            "partial": _stats(detection, "partial_r", "partial_p", "r_reduction_pct"),
            "lagged_zero_order": _stats(detection, "lagged_zero_order_r", "lagged_zero_order_p", "lagged_r_reduction_pct"),
            "lagged_partial": _stats(detection, "lagged_partial_r", "lagged_partial_p", "lagged_r_reduction_pct"),
        },
        "null_conditions": {
            "zero_order": _stats(null, "zero_order_r", "zero_order_p", "r_reduction_pct"),
            "partial": _stats(null, "partial_r", "partial_p", "r_reduction_pct"),
        },
    }

    det_zo = summary["detection_conditions"]["zero_order"]
    det_pa = summary["detection_conditions"]["partial"]
    det_lp = summary["detection_conditions"]["lagged_partial"]

    summary["key_message"] = (
        f"After partialing out generation trend, {det_pa['mean_r_reduction_pct']}% of zero-order correlation "
        f"is attributable to shared trend on average, but {round(100 - det_pa['mean_r_reduction_pct'], 1)}% persists "
        f"as genuine canary-downstream relationship. "
        f"{det_pa['sig_count']}/{det_pa['n']} pairs retain significance (p<0.05) after controlling for generation. "
        f"For lagged partial correlations, {det_lp['sig_count']}/{det_lp['n']} pairs remain significant."
    )
    return summary


def make_figure(all_results):
    os.makedirs(OUT_FIG_DIR, exist_ok=True)

    detection = [r for r in all_results if r["alpha"] >= 0.50]

    # Group by (alpha, canary, downstream) -> list across seeds
    from collections import defaultdict
    grouped = defaultdict(list)
    for r in detection:
        key = (r["alpha"], r["canary"], r["downstream"])
        grouped[key].append(r)

    # For the figure: group by alpha, show mean±SE of |zero_order_r| vs |partial_r|
    alphas = sorted(set(r["alpha"] for r in detection))
    pairs = []
    for c in CANARIES:
        for d in DOWNSTREAMS:
            pairs.append((c, d))

    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2), sharey=False)

    # Panel A: Contemporaneous correlations
    ax = axes[0]
    x_labels = []
    zero_means, zero_ses = [], []
    part_means, part_ses = [], []

    for alpha in alphas:
        for c, d in pairs:
            key = (alpha, c, d)
            recs = grouped.get(key, [])
            if not recs:
                continue
            zo_vals = [abs(r["zero_order_r"]) for r in recs if r["zero_order_r"] is not None]
            pa_vals = [abs(r["partial_r"]) for r in recs if r["partial_r"] is not None]
            if not zo_vals:
                continue
            zero_means.append(np.mean(zo_vals))
            zero_ses.append(np.std(zo_vals, ddof=1) / np.sqrt(len(zo_vals)) if len(zo_vals) > 1 else 0)
            part_means.append(np.mean(pa_vals))
            part_ses.append(np.std(pa_vals, ddof=1) / np.sqrt(len(pa_vals)) if len(pa_vals) > 1 else 0)
            c_short = "TE" if c == "token_entropy" else "ECE"
            d_short = d.replace("distinct_", "D")
            x_labels.append(f"{c_short}→{d_short}\nα={alpha}")

    x = np.arange(len(x_labels))
    w = 0.35
    bars1 = ax.bar(x - w/2, zero_means, w, yerr=zero_ses, label="Zero-order |r|",
                   color="#2166AC", capsize=2, linewidth=0.5, edgecolor="white", zorder=3)
    bars2 = ax.bar(x + w/2, part_means, w, yerr=part_ses, label="Partial |r| (gen.)",
                   color="#B2182B", capsize=2, linewidth=0.5, edgecolor="white", zorder=3)
    ax.set_ylabel("|Pearson r|", fontsize=8)
    ax.set_title("(a) Contemporaneous", fontsize=9, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=5.5, rotation=45, ha="right")
    ax.legend(fontsize=6, frameon=False)
    ax.set_ylim(0, 1.05)
    ax.axhline(0, color="black", linewidth=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Panel B: Lagged correlations
    ax = axes[1]
    x_labels2 = []
    lag_zo_means, lag_zo_ses = [], []
    lag_pa_means, lag_pa_ses = [], []

    for alpha in alphas:
        for c, d in pairs:
            key = (alpha, c, d)
            recs = grouped.get(key, [])
            if not recs:
                continue
            zo_vals = [abs(r["lagged_zero_order_r"]) for r in recs if r["lagged_zero_order_r"] is not None]
            pa_vals = [abs(r["lagged_partial_r"]) for r in recs if r["lagged_partial_r"] is not None]
            if not zo_vals:
                continue
            lag_zo_means.append(np.mean(zo_vals))
            lag_zo_ses.append(np.std(zo_vals, ddof=1) / np.sqrt(len(zo_vals)) if len(zo_vals) > 1 else 0)
            lag_pa_means.append(np.mean(pa_vals))
            lag_pa_ses.append(np.std(pa_vals, ddof=1) / np.sqrt(len(pa_vals)) if len(pa_vals) > 1 else 0)
            c_short = "TE" if c == "token_entropy" else "ECE"
            d_short = d.replace("distinct_", "D")
            x_labels2.append(f"{c_short}→{d_short}\nα={alpha}")

    x2 = np.arange(len(x_labels2))
    ax.bar(x2 - w/2, lag_zo_means, w, yerr=lag_zo_ses, label="Zero-order |r|",
           color="#2166AC", capsize=2, linewidth=0.5, edgecolor="white", zorder=3)
    ax.bar(x2 + w/2, lag_pa_means, w, yerr=lag_pa_ses, label="Partial |r| (gen.)",
           color="#B2182B", capsize=2, linewidth=0.5, edgecolor="white", zorder=3)
    ax.set_ylabel("|Pearson r|", fontsize=8)
    ax.set_title("(b) Lagged (canary[t] → downstream[t+1])", fontsize=9, fontweight="bold")
    ax.set_xticks(x2)
    ax.set_xticklabels(x_labels2, fontsize=5.5, rotation=45, ha="right")
    ax.legend(fontsize=6, frameon=False)
    ax.set_ylim(0, 1.05)
    ax.axhline(0, color="black", linewidth=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    fig.savefig(OUT_FIG_DIR / "fig_partial_correlation.pdf", bbox_inches="tight", dpi=300)
    fig.savefig(OUT_FIG_DIR / "fig_partial_correlation.png", bbox_inches="tight", dpi=300)
    plt.close(fig)

    # --- Panel figure 2: aggregated by alpha (cleaner for paper) ---
    fig2, axes2 = plt.subplots(1, 2, figsize=(5.5, 2.8))

    for panel_idx, (title, r_key, p_key, lag_prefix) in enumerate([
        ("(a) Contemporaneous", "zero_order_r", "partial_r", ""),
        ("(b) Lagged (t → t+1)", "lagged_zero_order_r", "lagged_partial_r", "lagged_"),
    ]):
        ax = axes2[panel_idx]
        zo_key = f"{lag_prefix}zero_order_r" if lag_prefix else "zero_order_r"
        pa_key = f"{lag_prefix}partial_r" if lag_prefix else "partial_r"

        alpha_zo_means, alpha_pa_means = [], []
        alpha_zo_ses, alpha_pa_ses = [], []
        alpha_labels = []

        for alpha in alphas:
            recs = [r for r in detection if r["alpha"] == alpha]
            zo = [abs(r[zo_key]) for r in recs if r[zo_key] is not None]
            pa = [abs(r[pa_key]) for r in recs if r[pa_key] is not None]
            if not zo:
                continue
            alpha_zo_means.append(np.mean(zo))
            alpha_zo_ses.append(np.std(zo, ddof=1) / np.sqrt(len(zo)) if len(zo) > 1 else 0)
            alpha_pa_means.append(np.mean(pa))
            alpha_pa_ses.append(np.std(pa, ddof=1) / np.sqrt(len(pa)) if len(pa) > 1 else 0)
            alpha_labels.append(f"α={alpha}")

        x = np.arange(len(alpha_labels))
        w = 0.3
        ax.bar(x - w/2, alpha_zo_means, w, yerr=alpha_zo_ses,
               label="Zero-order", color="#2166AC", capsize=3, edgecolor="white", zorder=3)
        ax.bar(x + w/2, alpha_pa_means, w, yerr=alpha_pa_ses,
               label="Partial (|gen)", color="#B2182B", capsize=3, edgecolor="white", zorder=3)
        ax.set_xticks(x)
        ax.set_xticklabels(alpha_labels, fontsize=8)
        ax.set_ylabel("Mean |r| across pairs", fontsize=8)
        ax.set_title(title, fontsize=9, fontweight="bold")
        ax.legend(fontsize=7, frameon=False)
        ax.set_ylim(0, 1.05)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    plt.tight_layout()
    fig2.savefig(OUT_FIG_DIR / "fig_partial_correlation_agg.pdf", bbox_inches="tight", dpi=300)
    fig2.savefig(OUT_FIG_DIR / "fig_partial_correlation_agg.png", bbox_inches="tight", dpi=300)
    plt.close(fig2)

    print(f"Figures saved to {OUT_FIG_DIR}/")


def main():
    all_results = []
    for cond in CONDITIONS:
        for seed in cond["seeds"]:
            try:
                res = analyze_condition(cond["alpha"], seed, cond["prefix"])
                all_results.extend(res)
                print(f"  ✓ α={cond['alpha']} s{seed}: {len(res)} pairs")
            except Exception as e:
                print(f"  ✗ α={cond['alpha']} s{seed}: {e}")

    summary = compute_summary(all_results)

    output = {
        "meta": {
            "analysis": "W11_partial_correlation",
            "description": "Partial correlations controlling for generation number",
            "conditions": [
                {"alpha": c["alpha"], "seeds": c["seeds"]} for c in CONDITIONS
            ],
            "canaries": CANARIES,
            "downstreams": DOWNSTREAMS,
        },
        "results": all_results,
        "summary": summary,
    }

    os.makedirs(OUT_JSON.parent, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved to {OUT_JSON}")

    print(f"\n=== SUMMARY (detection conditions, α≥0.50) ===")
    det = summary["detection_conditions"]
    print(f"Zero-order:  mean|r|={det['zero_order']['mean_abs_r']}, "
          f"sig={det['zero_order']['sig_count']}/{det['zero_order']['n']}")
    print(f"Partial:     mean|r|={det['partial']['mean_abs_r']}, "
          f"sig={det['partial']['sig_count']}/{det['partial']['n']}, "
          f"mean reduction={det['partial']['mean_r_reduction_pct']}%")
    print(f"Lagged ZO:   mean|r|={det['lagged_zero_order']['mean_abs_r']}, "
          f"sig={det['lagged_zero_order']['sig_count']}/{det['lagged_zero_order']['n']}")
    print(f"Lagged Part: mean|r|={det['lagged_partial']['mean_abs_r']}, "
          f"sig={det['lagged_partial']['sig_count']}/{det['lagged_partial']['n']}, "
          f"mean reduction={det['lagged_partial']['mean_r_reduction_pct']}%")
    print(f"\n{summary['key_message']}")

    make_figure(all_results)


if __name__ == "__main__":
    main()
