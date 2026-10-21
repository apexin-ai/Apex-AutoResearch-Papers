#!/usr/bin/env python3
"""D127 Track A: Critical Slowing Down (CSD) Indicators Analysis.

Tests whether AR(1) autocorrelation and variance increase as α approaches
the onset boundary (~0.476), as predicted by CSD theory for second-order
phase transitions. Null result (no CSD) supports Class 1 first-order
transition hypothesis (Truong & Truong 2025).
"""

import json
import os
import sys
from pathlib import Path
from collections import defaultdict

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats

BASE = Path("/root/autodl-tmp/distrib_canary_collapse")
RESULTS = BASE / "results" / "alpha_sweep"
OUT_DIR = BASE / "artifacts" / "d127_csd"
OUT_DIR.mkdir(parents=True, exist_ok=True)

EXPERIMENTS = {
    0.00: ["a000_s42_fp32"],
    0.05: ["a005_s42_fp32_v3_d080"],
    0.10: ["a010_s42_fp32", "a010_s43_fp32"],
    0.25: ["a025_s42_fp32", "a025_s43_fp32", "a025_s44_fp32"],
    0.30: ["a030_s42_fp32"],
    0.35: ["a035_s42_fp32"],
    0.40: ["a040_s42_fp32"],
    0.45: ["a045_s42_fp32", "a045_s43_fp32"],
    0.50: ["a050_s42_fp32", "a050_s43_fp32", "a050_s44_fp32"],
    0.60: ["a060_s42_fp32_v3_d080", "a060_s43_fp32"],
    0.75: ["a075_s42_fp32"],
    1.00: ["a100_s42_fp32"],
}

METRICS = ["token_entropy", "ece", "distinct_1", "distinct_2", "distinct_3"]


def load_series(exp_dir):
    """Load all_metrics.json and return dict of metric -> np.array over generations."""
    path = RESULTS / exp_dir / "all_metrics.json"
    if not path.exists():
        return None
    with open(path) as f:
        data = json.load(f)
    data = sorted(data, key=lambda x: x["generation"])
    result = {}
    for m in METRICS:
        vals = [d[m] for d in data if m in d]
        if vals:
            result[m] = np.array(vals)
    return result


def ar1_coefficient(x):
    """Lag-1 autocorrelation coefficient."""
    if len(x) < 3:
        return np.nan
    x = np.asarray(x, dtype=float)
    x_centered = x - x.mean()
    var = np.sum(x_centered**2)
    if var == 0:
        return np.nan
    return np.sum(x_centered[:-1] * x_centered[1:]) / var


def detrended_ar1(x):
    """AR(1) after removing linear trend."""
    if len(x) < 4:
        return np.nan
    t = np.arange(len(x))
    slope, intercept, _, _, _ = stats.linregress(t, x)
    residuals = x - (slope * t + intercept)
    return ar1_coefficient(residuals)


def detrended_variance(x):
    """Variance of residuals after removing linear trend."""
    if len(x) < 4:
        return np.nan
    t = np.arange(len(x))
    slope, intercept, _, _, _ = stats.linregress(t, x)
    residuals = x - (slope * t + intercept)
    return np.var(residuals, ddof=1)


def rolling_ar1(x, window=5):
    """Rolling AR(1) in sliding windows. Returns array of AR(1) values."""
    if len(x) < window:
        return np.array([])
    vals = []
    for i in range(len(x) - window + 1):
        vals.append(ar1_coefficient(x[i:i+window]))
    return np.array(vals)


def rolling_variance(x, window=5):
    """Rolling variance in sliding windows."""
    if len(x) < window:
        return np.array([])
    vals = []
    for i in range(len(x) - window + 1):
        vals.append(np.var(x[i:i+window], ddof=1))
    return np.array(vals)


def kendall_trend_test(alphas, values):
    """Kendall τ test for monotonic trend of values vs alphas."""
    mask = ~np.isnan(values)
    if mask.sum() < 4:
        return np.nan, np.nan
    tau, pval = stats.kendalltau(alphas[mask], values[mask])
    return tau, pval


def bootstrap_kendall(alphas, values, n_boot=10000, seed=42):
    """Permutation test: shuffle α labels, recompute Kendall τ."""
    mask = ~np.isnan(values)
    a = alphas[mask]
    v = values[mask]
    if len(a) < 4:
        return np.nan, np.nan
    observed_tau, _ = stats.kendalltau(a, v)
    rng = np.random.RandomState(seed)
    count = 0
    for _ in range(n_boot):
        perm = rng.permutation(a)
        tau_perm, _ = stats.kendalltau(perm, v)
        if abs(tau_perm) >= abs(observed_tau):
            count += 1
    pval = (count + 1) / (n_boot + 1)
    return observed_tau, pval


def main():
    # --- Load all data ---
    all_data = {}
    for alpha, exp_dirs in sorted(EXPERIMENTS.items()):
        for exp_dir in exp_dirs:
            series = load_series(exp_dir)
            if series is None:
                print(f"WARNING: {exp_dir} not found, skipping")
                continue
            all_data[(alpha, exp_dir)] = series

    print(f"Loaded {len(all_data)} experiments across {len(EXPERIMENTS)} α values")

    # --- Compute CSD indicators per experiment ---
    records = []
    for (alpha, exp_dir), series in sorted(all_data.items()):
        rec = {"alpha": alpha, "exp": exp_dir}
        for m in METRICS:
            if m not in series:
                continue
            x = series[m]
            rec[f"{m}_ar1"] = ar1_coefficient(x)
            rec[f"{m}_ar1_detrend"] = detrended_ar1(x)
            rec[f"{m}_var"] = np.var(x, ddof=1)
            rec[f"{m}_var_detrend"] = detrended_variance(x)
            rec[f"{m}_sd"] = np.std(x, ddof=1)
            r_ar1 = rolling_ar1(x, window=5)
            r_var = rolling_variance(x, window=5)
            if len(r_ar1) > 0:
                rec[f"{m}_rolling_ar1_mean"] = float(np.nanmean(r_ar1))
                rec[f"{m}_rolling_ar1_last"] = float(r_ar1[-1])
                rec[f"{m}_rolling_var_mean"] = float(np.nanmean(r_var))
                rec[f"{m}_rolling_var_last"] = float(r_var[-1])
        records.append(rec)

    # --- Aggregate by α (mean across seeds) ---
    alpha_agg = defaultdict(lambda: defaultdict(list))
    for rec in records:
        a = rec["alpha"]
        for k, v in rec.items():
            if k in ("alpha", "exp"):
                continue
            if not np.isnan(v):
                alpha_agg[a][k].append(v)

    agg_records = []
    for a in sorted(alpha_agg.keys()):
        arec = {"alpha": a}
        for k, vals in alpha_agg[a].items():
            arec[f"{k}_mean"] = float(np.mean(vals))
            arec[f"{k}_std"] = float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.0
            arec[f"{k}_n"] = len(vals)
        agg_records.append(arec)

    # --- Kendall τ trend tests ---
    alphas_arr = np.array([r["alpha"] for r in agg_records])
    trend_results = {}
    for m in METRICS:
        for indicator in ["ar1", "ar1_detrend", "var", "var_detrend", "sd"]:
            key = f"{m}_{indicator}_mean"
            vals = np.array([r.get(key, np.nan) for r in agg_records])
            tau, pval = kendall_trend_test(alphas_arr, vals)
            boot_tau, boot_pval = bootstrap_kendall(alphas_arr, vals)
            trend_results[f"{m}_{indicator}"] = {
                "kendall_tau": round(float(tau), 4) if not np.isnan(tau) else None,
                "kendall_pval": round(float(pval), 4) if not np.isnan(pval) else None,
                "bootstrap_tau": round(float(boot_tau), 4) if not np.isnan(boot_tau) else None,
                "bootstrap_pval": round(float(boot_pval), 4) if not np.isnan(boot_pval) else None,
            }

    # --- Blind zone analysis (α ≤ 0.45) ---
    blind_mask = alphas_arr <= 0.45
    blind_alphas = alphas_arr[blind_mask]
    blind_trends = {}
    for m in METRICS:
        for indicator in ["ar1_detrend", "var_detrend"]:
            key = f"{m}_{indicator}_mean"
            vals = np.array([r.get(key, np.nan) for r in agg_records])[blind_mask]
            tau, pval = kendall_trend_test(blind_alphas, vals)
            blind_trends[f"{m}_{indicator}"] = {
                "kendall_tau": round(float(tau), 4) if not np.isnan(tau) else None,
                "kendall_pval": round(float(pval), 4) if not np.isnan(pval) else None,
            }

    # --- Onset jump analysis (α=0.45 → 0.50) ---
    onset_jump = {}
    for m in METRICS:
        for indicator in ["ar1_detrend", "var_detrend"]:
            key = f"{m}_{indicator}_mean"
            v045 = None
            v050 = None
            for r in agg_records:
                if r["alpha"] == 0.45:
                    v045 = r.get(key)
                if r["alpha"] == 0.50:
                    v050 = r.get(key)
            if v045 is not None and v050 is not None:
                onset_jump[f"{m}_{indicator}"] = {
                    "alpha_045": round(v045, 6),
                    "alpha_050": round(v050, 6),
                    "jump": round(v050 - v045, 6),
                    "ratio": round(v050 / v045, 4) if v045 != 0 else None,
                }

    # --- Summary verdict ---
    sig_count = 0
    total_tests = 0
    for k, v in trend_results.items():
        if "ar1" in k or "var" in k:
            total_tests += 1
            if v["bootstrap_pval"] is not None and v["bootstrap_pval"] < 0.05:
                sig_count += 1

    blind_sig = 0
    blind_total = 0
    for k, v in blind_trends.items():
        blind_total += 1
        if v["kendall_pval"] is not None and v["kendall_pval"] < 0.05:
            blind_sig += 1

    if sig_count <= total_tests * 0.2 and blind_sig <= blind_total * 0.2:
        verdict = "CSD indicators absent. Consistent with Class 1 first-order transition (Truong & Truong 2025): no gradual early-warning signal precedes the onset discontinuity at α_c ≈ 0.476."
    elif blind_sig > blind_total * 0.5:
        verdict = "CSD indicators present in blind zone. Suggests second-order or weakly first-order transition with detectable early-warning signals."
    else:
        verdict = "Mixed CSD evidence. Some indicators show trends but pattern is inconsistent across metrics."

    # --- Assemble output JSON ---
    output = {
        "task": "D127_Track_A_CSD_Indicators",
        "description": "Critical Slowing Down analysis for distributional canary collapse onset",
        "n_experiments": len(all_data),
        "n_alpha_values": len(EXPERIMENTS),
        "T_generations": 11,
        "metrics_analyzed": METRICS,
        "csd_indicators": ["AR(1) autocorrelation", "Variance (detrended)"],
        "per_experiment": records,
        "aggregated_by_alpha": agg_records,
        "trend_tests_full_range": trend_results,
        "trend_tests_blind_zone": blind_trends,
        "onset_jump_045_050": onset_jump,
        "summary": {
            "verdict": verdict,
            "significant_full_range": f"{sig_count}/{total_tests}",
            "significant_blind_zone": f"{blind_sig}/{blind_total}",
            "note": "T=11 severely limits CSD detection power. Absence of CSD should be interpreted cautiously given the short time series."
        }
    }

    json_path = OUT_DIR / "d127_csd_indicators.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"JSON saved: {json_path}")

    # --- Plotting ---
    fig, axes = plt.subplots(3, 2, figsize=(14, 15))
    fig.suptitle("D127: Critical Slowing Down Indicators vs α", fontsize=14, fontweight='bold')

    cmap = plt.cm.viridis
    alpha_vals = sorted(EXPERIMENTS.keys())

    # Panel (0,0): AR(1) detrended - canary metrics
    ax = axes[0, 0]
    for m in ["token_entropy", "ece"]:
        key = f"{m}_ar1_detrend_mean"
        vals = [next((r.get(key, np.nan) for r in agg_records if r["alpha"] == a), np.nan) for a in alpha_vals]
        errs = [next((r.get(f"{m}_ar1_detrend_std", 0) for r in agg_records if r["alpha"] == a), 0) for a in alpha_vals]
        ax.errorbar(alpha_vals, vals, yerr=errs, marker='o', label=m, capsize=3, markersize=5)
    ax.axvline(0.476, color='red', ls='--', alpha=0.5, label='α_c=0.476')
    ax.axvspan(0, 0.45, alpha=0.08, color='blue', label='blind zone')
    ax.set_xlabel('α')
    ax.set_ylabel('AR(1) (detrended)')
    ax.set_title('Canary Metrics: AR(1)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (0,1): AR(1) detrended - downstream metrics
    ax = axes[0, 1]
    for m in ["distinct_1", "distinct_2", "distinct_3"]:
        key = f"{m}_ar1_detrend_mean"
        vals = [next((r.get(key, np.nan) for r in agg_records if r["alpha"] == a), np.nan) for a in alpha_vals]
        errs = [next((r.get(f"{m}_ar1_detrend_std", 0) for r in agg_records if r["alpha"] == a), 0) for a in alpha_vals]
        ax.errorbar(alpha_vals, vals, yerr=errs, marker='s', label=m, capsize=3, markersize=5)
    ax.axvline(0.476, color='red', ls='--', alpha=0.5, label='α_c=0.476')
    ax.axvspan(0, 0.45, alpha=0.08, color='blue', label='blind zone')
    ax.set_xlabel('α')
    ax.set_ylabel('AR(1) (detrended)')
    ax.set_title('Downstream Metrics: AR(1)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (1,0): Variance detrended - canary metrics
    ax = axes[1, 0]
    for m in ["token_entropy", "ece"]:
        key = f"{m}_var_detrend_mean"
        vals = [next((r.get(key, np.nan) for r in agg_records if r["alpha"] == a), np.nan) for a in alpha_vals]
        errs = [next((r.get(f"{m}_var_detrend_std", 0) for r in agg_records if r["alpha"] == a), 0) for a in alpha_vals]
        ax.errorbar(alpha_vals, vals, yerr=errs, marker='o', label=m, capsize=3, markersize=5)
    ax.axvline(0.476, color='red', ls='--', alpha=0.5, label='α_c=0.476')
    ax.axvspan(0, 0.45, alpha=0.08, color='blue', label='blind zone')
    ax.set_xlabel('α')
    ax.set_ylabel('Variance (detrended)')
    ax.set_title('Canary Metrics: Variance')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (1,1): Variance detrended - downstream metrics
    ax = axes[1, 1]
    for m in ["distinct_1", "distinct_2", "distinct_3"]:
        key = f"{m}_var_detrend_mean"
        vals = [next((r.get(key, np.nan) for r in agg_records if r["alpha"] == a), np.nan) for a in alpha_vals]
        errs = [next((r.get(f"{m}_var_detrend_std", 0) for r in agg_records if r["alpha"] == a), 0) for a in alpha_vals]
        ax.errorbar(alpha_vals, vals, yerr=errs, marker='s', label=m, capsize=3, markersize=5)
    ax.axvline(0.476, color='red', ls='--', alpha=0.5, label='α_c=0.476')
    ax.axvspan(0, 0.45, alpha=0.08, color='blue', label='blind zone')
    ax.set_xlabel('α')
    ax.set_ylabel('Variance (detrended)')
    ax.set_title('Downstream Metrics: Variance')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (2,0): Onset jump comparison - AR(1)
    ax = axes[2, 0]
    jump_data = []
    for m in METRICS:
        key = f"{m}_ar1_detrend"
        if key in onset_jump:
            j = onset_jump[key]
            jump_data.append((m, j["alpha_045"], j["alpha_050"], j["jump"]))
    if jump_data:
        names = [d[0] for d in jump_data]
        v045 = [d[1] for d in jump_data]
        v050 = [d[2] for d in jump_data]
        x_pos = np.arange(len(names))
        width = 0.35
        ax.bar(x_pos - width/2, v045, width, label='α=0.45', color='steelblue', alpha=0.8)
        ax.bar(x_pos + width/2, v050, width, label='α=0.50', color='firebrick', alpha=0.8)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(names, rotation=30, ha='right', fontsize=8)
        ax.set_ylabel('AR(1) (detrended)')
        ax.set_title('Onset Jump: AR(1) at α=0.45 vs 0.50')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3, axis='y')

    # Panel (2,1): Summary statistics table
    ax = axes[2, 1]
    ax.axis('off')
    table_data = []
    table_data.append(["Metric", "Indicator", "τ (full)", "p (full)", "τ (blind)", "p (blind)"])
    for m in METRICS:
        for indicator in ["ar1_detrend", "var_detrend"]:
            key = f"{m}_{indicator}"
            tr = trend_results.get(key, {})
            bt = blind_trends.get(key, {})
            ind_label = "AR(1)" if "ar1" in indicator else "Var"
            tau_f = f"{tr.get('bootstrap_tau', 'N/A')}"
            p_f = f"{tr.get('bootstrap_pval', 'N/A')}"
            tau_b = f"{bt.get('kendall_tau', 'N/A')}"
            p_b = f"{bt.get('kendall_pval', 'N/A')}"
            table_data.append([m[:12], ind_label, tau_f, p_f, tau_b, p_b])

    table = ax.table(cellText=table_data[1:], colLabels=table_data[0],
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(1.0, 1.3)
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor('#d4e6f1')
            cell.set_fontsize(8)
        else:
            p_val_str = table_data[row][5] if col == 5 else (table_data[row][3] if col == 3 else None)
            try:
                if p_val_str and float(p_val_str) < 0.05:
                    cell.set_facecolor('#fadbd8')
            except (ValueError, TypeError):
                pass

    ax.set_title(f'Trend Tests Summary\n{verdict[:80]}...', fontsize=9, pad=20)

    plt.tight_layout()
    png_path = OUT_DIR / "csd_indicators.png"
    plt.savefig(png_path, dpi=150, bbox_inches='tight')
    print(f"PNG saved: {png_path}")

    # --- Print summary ---
    print("\n" + "="*70)
    print("D127 CSD ANALYSIS SUMMARY")
    print("="*70)
    print(f"\nVerdict: {verdict}")
    print(f"\nSignificant trends (full range): {sig_count}/{total_tests}")
    print(f"Significant trends (blind zone): {blind_sig}/{blind_total}")
    print(f"\nOnset jumps (α=0.45 → 0.50):")
    for k, v in onset_jump.items():
        print(f"  {k}: {v['alpha_045']:.6f} → {v['alpha_050']:.6f} (Δ={v['jump']:+.6f})")

    print(f"\nKey trend tests (full range):")
    for m in METRICS:
        for ind in ["ar1_detrend", "var_detrend"]:
            key = f"{m}_{ind}"
            tr = trend_results.get(key, {})
            star = " *" if tr.get("bootstrap_pval") is not None and tr["bootstrap_pval"] < 0.05 else ""
            print(f"  {m:15s} {ind:15s}: τ={tr.get('bootstrap_tau', 'N/A'):>7s}, p={tr.get('bootstrap_pval', 'N/A'):>7s}{star}")


if __name__ == "__main__":
    main()
