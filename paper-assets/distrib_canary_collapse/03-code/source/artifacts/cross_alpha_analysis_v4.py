"""Cross-alpha analysis v4 with per-alpha consensus classification.

Extends v3 with:
  5. Per-alpha multi-method consensus classification (regime-dependent validity)
  6. Markdown report output

Handles mixed data paths:
  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)
  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)
  - alpha=1.0 consensus loads existing method_ablation.json
  - Single-seed alpha points: seed_threshold=1, method agreement only

Dependencies: numpy, scipy, statsmodels
"""

import argparse
import glob
import json
import os
import re
import sys
import warnings
from datetime import datetime

import numpy as np
from statsmodels.stats.multitest import multipletests

warnings.filterwarnings("ignore")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from method_ablation import (
    CANARY, DOWNSTREAM,
    extract as ma_extract,
    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,
)
from consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder

SWEEP_DIR = os.path.join(BASE_DIR, "results", "alpha_sweep")
MVP_DIR = os.path.join(BASE_DIR, "results", "mvp")
ANALYSIS_DIR = os.path.join(BASE_DIR, "results", "analysis")

METRICS = ["distinct_1", "distinct_2", "distinct_3", "token_entropy", "ece", "perplexity"]

GRANGER_PAIRS = [
    ("token_entropy", "distinct_1", "entropy->d1"),
    ("ece",           "distinct_1", "ECE->d1"),
    ("token_entropy", "distinct_2", "entropy->d2"),
    ("ece",           "distinct_2", "ECE->d2"),
    ("distinct_1", "token_entropy", "d1->entropy"),
    ("distinct_1", "ece",           "d1->ECE"),
    ("distinct_2", "token_entropy", "d2->entropy"),
    ("distinct_2", "ece",           "d2->ECE"),
]

XCORR_PAIRS = [
    ("token_entropy", "distinct_1", "entropy_vs_d1"),
    ("ece",           "distinct_1", "ece_vs_d1"),
]

MA_METHODS = ["naive_pearson", "differenced_xcorr", "threshold_onset",
              "toda_yamamoto", "permutation_granger"]
MA_METHOD_FN = {
    "naive_pearson": naive_pearson,
    "differenced_xcorr": diff_xcorr,
    "threshold_onset": threshold_lead,
    "toda_yamamoto": toda_yamamoto,
    "permutation_granger": perm_granger,
}


# ---------------------------------------------------------------------------
# Data loading (extended for MVP alpha=1.0)
# ---------------------------------------------------------------------------

def _find_mvp_seeds():
    seeds = []
    if not os.path.isdir(MVP_DIR):
        return seeds
    for d in sorted(os.listdir(MVP_DIR)):
        m = re.match(r"rep_(\d+)$", d)
        if m and os.path.isfile(os.path.join(MVP_DIR, d, "all_metrics.json")):
            seeds.append(int(m.group(1)))
    return sorted(seeds)


def discover_alpha_dirs(explicit=None, include_mvp=True):
    """Find alpha directories.

    Returns sorted list of (alpha_key, alpha_float, path, seeds).
    """
    dirs = []

    if explicit:
        for name in explicit:
            if name in ("mvp", "a100_mvp"):
                rep42 = os.path.join(MVP_DIR, "rep_42")
                if os.path.isdir(rep42):
                    dirs.append(("a100", 1.0, rep42, _find_mvp_seeds()))
                continue
            path = os.path.join(SWEEP_DIR, name)
            if not os.path.isdir(path):
                print(f"WARNING: {path} not found, skipping", file=sys.stderr)
                continue
            m = re.match(r"a(\d{3})_s(\d+)", name)
            if m:
                alpha_val = int(m.group(1)) / 100.0
                dirs.append((f"a{m.group(1)}", alpha_val, path, [int(m.group(2))]))
    else:
        pattern = os.path.join(SWEEP_DIR, "a*_s42")
        for path in sorted(glob.glob(pattern)):
            name = os.path.basename(path)
            m = re.match(r"a(\d{3})_s42", name)
            if m:
                alpha_val = int(m.group(1)) / 100.0
                dirs.append((f"a{m.group(1)}", alpha_val, path, [42]))

        if include_mvp and not any(d[1] == 1.0 for d in dirs):
            rep42 = os.path.join(MVP_DIR, "rep_42")
            if os.path.isdir(rep42):
                dirs.append(("a100", 1.0, rep42, _find_mvp_seeds()))

    return sorted(dirs, key=lambda x: x[1])


def load_metrics(alpha_dir):
    path = os.path.join(alpha_dir, "all_metrics.json")
    with open(path) as f:
        data = json.load(f)
    return sorted(data, key=lambda x: x["generation"])


def load_all_seeds_metrics(alpha_val, primary_dir, seeds):
    """Load metrics for all seeds. Returns list of (seed, metrics_list)."""
    results = []
    for seed in seeds:
        if alpha_val == 1.0:
            path = os.path.join(MVP_DIR, f"rep_{seed}")
        else:
            path = primary_dir
        mpath = os.path.join(path, "all_metrics.json")
        if os.path.isfile(mpath):
            results.append((seed, load_metrics(path)))
    return results


def extract_series(metrics_list, key):
    return np.array([m[key] for m in metrics_list], dtype=float)


# ---------------------------------------------------------------------------
# 1. Dose-response
# ---------------------------------------------------------------------------

def compute_dose_response(all_data):
    result = {}
    for alpha_key, alpha_val, metrics_list in all_data:
        entry = {"alpha": alpha_val}
        for metric in METRICS:
            vals = extract_series(metrics_list, metric)
            gen0, genN = vals[0], vals[-1]
            drift_pct = round((genN - gen0) / abs(gen0) * 100, 2) if abs(gen0) > 1e-12 else 0.0
            entry[metric] = {
                "gen0": round(float(gen0), 6),
                f"gen{len(vals)-1}": round(float(genN), 6),
                "drift_pct": drift_pct,
            }
        result[alpha_key] = entry
    return result


# ---------------------------------------------------------------------------
# 2. Permutation Granger causality
# ---------------------------------------------------------------------------

def _build_lag_matrix(y, x, max_lag):
    T = len(y)
    n = T - max_lag
    Y = y[max_lag:]
    cols_r = [np.ones(n)]
    for lag in range(1, max_lag + 1):
        cols_r.append(y[max_lag - lag: T - lag])
    cols_u = list(cols_r)
    for lag in range(1, max_lag + 1):
        cols_u.append(x[max_lag - lag: T - lag])
    return Y, np.column_stack(cols_r), np.column_stack(cols_u)


def _granger_f_stat(y, x, max_lag):
    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)
    n = len(Y)
    q = max_lag
    try:
        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]
        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]
    except np.linalg.LinAlgError:
        return np.nan
    rss_r = np.sum((Y - X_r @ beta_r) ** 2)
    rss_u = np.sum((Y - X_u @ beta_u) ** 2)
    k_u = X_u.shape[1]
    df_resid = n - k_u
    if df_resid <= 0 or rss_u < 1e-15:
        return np.nan
    return ((rss_r - rss_u) / q) / (rss_u / df_resid)


def permutation_granger_test(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if difference:
        x, y = np.diff(x), np.diff(y)
    T = len(x)
    if T <= max_lag + 2:
        return {"f_stat": None, "p_raw": None, "note": f"Series too short: T={T}"}

    f_obs = _granger_f_stat(y, x, max_lag)
    if np.isnan(f_obs):
        return {"f_stat": None, "p_raw": None, "note": "F-stat computation failed"}

    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)
    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)
    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)
    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None

    rng = np.random.default_rng(seed)
    null_f = np.empty(n_perm)
    for i in range(n_perm):
        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)
    valid = null_f[~np.isnan(null_f)]
    if len(valid) == 0:
        return {"f_stat": round(float(f_obs), 4), "p_raw": None, "note": "All permutations failed"}

    p_value = (np.sum(valid >= f_obs) + 1) / (len(valid) + 1)
    return {
        "f_stat": round(float(f_obs), 4),
        "p_raw": round(float(p_value), 6),
        "n_perm": n_perm,
        "effect_size_f2": round(float(f2), 4) if f2 is not None else None,
    }


def run_granger_all(all_data, max_lag=1, n_perms=5000):
    results = []
    for alpha_key, alpha_val, metrics_list in all_data:
        for cause_key, effect_key, label in GRANGER_PAIRS:
            x = extract_series(metrics_list, cause_key)
            y = extract_series(metrics_list, effect_key)
            res = permutation_granger_test(x, y, max_lag=max_lag, n_perm=n_perms)
            res.update({
                "alpha": alpha_val,
                "alpha_key": alpha_key,
                "direction": label,
                "cause": cause_key,
                "effect": effect_key,
            })
            results.append(res)
    return results


def apply_fdr(granger_results):
    valid_idx = [i for i, r in enumerate(granger_results) if r.get("p_raw") is not None]
    if not valid_idx:
        return granger_results

    raw_ps = [granger_results[i]["p_raw"] for i in valid_idx]
    _, fdr_ps, _, _ = multipletests(raw_ps, method="fdr_bh")

    for j, idx in enumerate(valid_idx):
        granger_results[idx]["p_fdr"] = round(float(fdr_ps[j]), 6)

    for r in granger_results:
        if r.get("alpha", -1) == 0.0 and r.get("p_raw") is not None and r["p_raw"] < 0.05:
            r["note"] = "consistent with FPR, likely false positive"

    return granger_results


# ---------------------------------------------------------------------------
# 3. Cross-correlation lead-lag
# ---------------------------------------------------------------------------

def cross_correlation(all_data, max_lag=3):
    result = {}
    for alpha_key, alpha_val, metrics_list in all_data:
        entry = {"alpha": alpha_val}
        for cause_key, effect_key, pair_label in XCORR_PAIRS:
            dx = np.diff(extract_series(metrics_list, cause_key))
            dy = np.diff(extract_series(metrics_list, effect_key))
            lags = {}
            best_lag, best_r = 0, 0.0
            for lag in range(-max_lag, max_lag + 1):
                if lag >= 0:
                    a, b = dx[:len(dx) - lag] if lag > 0 else dx, dy[lag:] if lag > 0 else dy
                else:
                    a, b = dx[-lag:], dy[:len(dy) + lag]
                n = min(len(a), len(b))
                if n < 3:
                    continue
                a, b = a[:n], b[:n]
                std_a, std_b = np.std(a, ddof=1), np.std(b, ddof=1)
                if std_a < 1e-15 or std_b < 1e-15:
                    r = 0.0
                else:
                    r = float(np.corrcoef(a, b)[0, 1])
                lags[str(lag)] = round(r, 4)
                if abs(r) > abs(best_r):
                    best_lag, best_r = lag, r
            entry[pair_label] = {
                "peak_lag": best_lag,
                "peak_r": round(best_r, 4),
                "lags": lags,
            }
        result[alpha_key] = entry
    return result


# ---------------------------------------------------------------------------
# 4. Per-gen velocity
# ---------------------------------------------------------------------------

def per_gen_velocity(all_data):
    result = {}
    for alpha_key, alpha_val, metrics_list in all_data:
        vals = extract_series(metrics_list, "distinct_1")
        deltas = np.diff(vals)
        n = len(deltas)
        mid = n // 2
        early_mean = float(np.mean(deltas[:mid])) if mid > 0 else None
        late_mean = float(np.mean(deltas[mid:])) if mid < n else None
        max_drop_idx = int(np.argmin(deltas))
        result[alpha_key] = {
            "alpha": alpha_val,
            "d1_values": [round(float(v), 6) for v in vals],
            "d1_deltas": [round(float(d), 6) for d in deltas],
            "cumulative_drift_pct": round((vals[-1] - vals[0]) / abs(vals[0]) * 100, 2),
            "mean_velocity": round(float(np.mean(deltas)), 6),
            "max_drop_gen": max_drop_idx,
            "max_drop_value": round(float(deltas[max_drop_idx]), 6),
            "early_mean_velocity": round(early_mean, 6) if early_mean is not None else None,
            "late_mean_velocity": round(late_mean, 6) if late_mean is not None else None,
            "deceleration_ratio": round(late_mean / early_mean, 4) if early_mean and abs(early_mean) > 1e-12 else None,
        }
    return result


# ---------------------------------------------------------------------------
# 5. Per-alpha consensus classification
# ---------------------------------------------------------------------------

def run_consensus_per_alpha(alpha_dirs, mvp_ablation_path=None, consensus_n_perm=1000):
    """Run 5-method consensus classification at each alpha point.

    alpha=1.0 with existing method_ablation.json: load directly (4 seeds).
    Other alpha points: run 5 methods on single-seed data, seed_threshold=1.
    """
    results = {}

    for alpha_key, alpha_val, primary_dir, seeds in alpha_dirs:
        # alpha=1.0: use existing method_ablation.json
        if alpha_val == 1.0 and mvp_ablation_path and os.path.isfile(mvp_ablation_path):
            sig, pair_names, method_names, ab_seeds = load_sig_matrix(mvp_ablation_path)
            n_m, n_p, n_s = sig.shape
            mt = n_m - 1  # 4/5
            st = 3        # 3/4 seeds
            consensus = classify_robust(sig, mt, st)

            for cl in consensus["classifications"]:
                pi = cl["pair_index"]
                cl["canary"] = pair_names[pi][0]
                cl["downstream"] = pair_names[pi][1]
                cl["pair_label"] = f"{pair_names[pi][0]}→{pair_names[pi][1]}"

            results[alpha_key] = {
                "alpha": alpha_val,
                "n_seeds": n_s,
                "seeds": ab_seeds,
                "mode": "full_consensus",
                "note": f"{n_s}-seed full consensus (≥{mt}/{n_m} methods, ≥{st}/{n_s} seeds)",
                "method_threshold": mt,
                "seed_threshold": st,
                "n_methods": n_m,
                "n_pairs": n_p,
                "consensus": consensus,
                "pair_names": [list(p) for p in pair_names],
            }
            continue

        # Other alpha points: run 5 methods from scratch
        seed_data = load_all_seeds_metrics(alpha_val, primary_dir, seeds)
        n_seeds = len(seed_data)
        n_pairs = len(CANARY) * len(DOWNSTREAM)
        n_methods = len(MA_METHODS)

        sig_matrix = np.zeros((n_methods, n_pairs, n_seeds), dtype=bool)
        pair_names = []

        for si, (seed, metrics_list) in enumerate(seed_data):
            pi = 0
            for cn in CANARY:
                c = ma_extract(metrics_list, cn)
                for dn in DOWNSTREAM:
                    if si == 0:
                        pair_names.append((cn, dn))
                    d = ma_extract(metrics_list, dn)
                    for mi, method_name in enumerate(MA_METHODS):
                        fn = MA_METHOD_FN[method_name]
                        try:
                            if method_name == "permutation_granger":
                                res = fn(c, d, cn, dn, n_perm=consensus_n_perm)
                            else:
                                res = fn(c, d, cn, dn)
                            sig_matrix[mi, pi, si] = res.get("significant", False)
                        except Exception:
                            sig_matrix[mi, pi, si] = False
                    pi += 1

        st = 1 if n_seeds == 1 else 3
        mt = n_methods - 1  # 4/5

        consensus = classify_robust(sig_matrix, mt, st)
        for cl in consensus["classifications"]:
            pi = cl["pair_index"]
            cl["canary"] = pair_names[pi][0]
            cl["downstream"] = pair_names[pi][1]
            cl["pair_label"] = f"{pair_names[pi][0]}→{pair_names[pi][1]}"

        mode = "method_agreement_only" if n_seeds == 1 else "full_consensus"
        note_prefix = "single-seed, method agreement only" if n_seeds == 1 else f"{n_seeds}-seed full consensus"

        results[alpha_key] = {
            "alpha": alpha_val,
            "n_seeds": n_seeds,
            "seeds": [s for s, _ in seed_data],
            "mode": mode,
            "note": f"{note_prefix} (≥{mt}/{n_methods} methods, ≥{st}/{n_seeds} seeds)",
            "method_threshold": mt,
            "seed_threshold": st,
            "n_methods": n_methods,
            "n_pairs": n_pairs,
            "consensus": consensus,
            "pair_names": [list(p) for p in pair_names],
        }

    return results


def consensus_regime_comparison(consensus_results):
    """Compare robust/non-robust classifications across alpha points."""
    alpha_keys = sorted(consensus_results.keys(),
                        key=lambda k: consensus_results[k]["alpha"])
    if not alpha_keys:
        return {}

    first = consensus_results[alpha_keys[0]]
    pair_labels = [cl["pair_label"] for cl in first["consensus"]["classifications"]]

    pairs_comp = {}
    for label in pair_labels:
        row = {"pair": label, "per_alpha": {}}
        for ak in alpha_keys:
            cr = consensus_results[ak]
            cls = [c for c in cr["consensus"]["classifications"] if c["pair_label"] == label]
            if cls:
                cl = cls[0]
                row["per_alpha"][ak] = {
                    "alpha": cr["alpha"],
                    "is_robust": cl["is_robust"],
                    "n_sig_methods": cl["n_sig_methods"],
                    "mode": cr["mode"],
                }
        verdicts = [v["is_robust"] for v in row["per_alpha"].values()]
        row["stable"] = len(set(verdicts)) <= 1
        row["all_robust"] = all(verdicts) if verdicts else False
        row["all_non_robust"] = not any(verdicts) if verdicts else True
        pairs_comp[label] = row

    n_stable = sum(1 for r in pairs_comp.values() if r["stable"])
    return {
        "alpha_keys": alpha_keys,
        "alpha_values": [consensus_results[ak]["alpha"] for ak in alpha_keys],
        "n_pairs": len(pair_labels),
        "n_stable": n_stable,
        "n_regime_dependent": len(pair_labels) - n_stable,
        "pairs": pairs_comp,
    }


# ---------------------------------------------------------------------------
# 6. Markdown report
# ---------------------------------------------------------------------------

def generate_markdown_report(output, out_path):
    lines = []
    lines.append(f"# Cross-Alpha Analysis Report ({output['version']})")
    lines.append("")
    lines.append(f"**Date:** {output['date']}")
    lines.append(f"**Alpha points:** {output['alpha_points']}")
    lines.append(f"**Generations:** {output['gen_range']}")
    lines.append("")

    # 1. Dose-response
    lines.append("## 1. Dose-Response (gen0 to genN drift %)")
    lines.append("")
    dr = output["dose_response"]
    alphas = sorted(dr.keys())
    header = "| Metric |"
    sep = "|--------|"
    for ak in alphas:
        header += f" α={dr[ak]['alpha']:.2f} |"
        sep += "--------:|"
    lines.append(header)
    lines.append(sep)
    for metric in METRICS:
        row = f"| {metric} |"
        for ak in alphas:
            d = dr[ak][metric]["drift_pct"]
            row += f" {d:+.1f}% |"
        lines.append(row)
    lines.append("")

    # 2. Granger
    lines.append("## 2. Granger Causality (bidirectional, permutation, FDR-corrected)")
    lines.append("")
    gc = output["granger_causality"]
    ak_list = sorted(set(r["alpha_key"] for r in gc))
    header = "| Direction |"
    sep = "|-----------|"
    for ak in ak_list:
        a = [r for r in gc if r["alpha_key"] == ak][0]["alpha"]
        header += f" α={a:.2f} p_raw | p_fdr |"
        sep += "--------:|--------:|"
    lines.append(header)
    lines.append(sep)
    directions = list(dict.fromkeys(r["direction"] for r in gc))
    for d in directions:
        row = f"| {d} |"
        for ak in ak_list:
            match = [r for r in gc if r["alpha_key"] == ak and r["direction"] == d]
            if match:
                r = match[0]
                pr = f"{r['p_raw']:.4f}" if r.get("p_raw") is not None else "N/A"
                pf = f"{r['p_fdr']:.4f}" if r.get("p_fdr") is not None else "N/A"
                sig = " *" if r.get("p_fdr") is not None and r["p_fdr"] < 0.05 else ""
                row += f" {pr} | {pf}{sig} |"
            else:
                row += " -- | -- |"
        lines.append(row)
    lines.append("")
    sc = output["statistical_config"]
    lines.append(f"FDR: {sc['n_independent_tests']} tests, BH correction. \\* = p_fdr < 0.05")
    lines.append("")

    # 3. Consensus per alpha
    if "consensus_per_alpha" in output:
        lines.append("## 3. Consensus Classification (regime-dependent validity)")
        lines.append("")
        cpa = output["consensus_per_alpha"]
        for ak in sorted(cpa.keys(), key=lambda k: cpa[k]["alpha"]):
            entry = cpa[ak]
            lines.append(f"### α={entry['alpha']:.2f} ({entry['note']})")
            lines.append("")
            lines.append(f"- Robust pairs: {entry['consensus']['n_robust']}/{entry['n_pairs']}")
            lines.append(f"- Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}")
            lines.append("")
            lines.append("| Pair | Robust | Methods |")
            lines.append("|------|--------|---------|")
            for cl in entry["consensus"]["classifications"]:
                tag = "**ROBUST**" if cl["is_robust"] else "non-robust"
                lines.append(f"| {cl['pair_label']} | {tag} | {cl['n_sig_methods']}/{entry['n_methods']} |")
            lines.append("")

        if "consensus_regime_comparison" in output:
            rc = output["consensus_regime_comparison"]
            lines.append("### Regime Comparison Summary")
            lines.append("")
            lines.append(f"- Stable pairs (same classification at all α): {rc['n_stable']}/{rc['n_pairs']}")
            lines.append(f"- Regime-dependent pairs: {rc['n_regime_dependent']}/{rc['n_pairs']}")
            lines.append("")
            header = "| Pair |"
            sep = "|------|"
            for av in rc["alpha_values"]:
                header += f" α={av:.2f} |"
                sep += "--------|"
            header += " Stable |"
            sep += "--------|"
            lines.append(header)
            lines.append(sep)
            for label, info in rc["pairs"].items():
                row = f"| {label} |"
                for ak in rc["alpha_keys"]:
                    if ak in info["per_alpha"]:
                        v = info["per_alpha"][ak]
                        tag = f"R({v['n_sig_methods']})" if v["is_robust"] else f".({v['n_sig_methods']})"
                        row += f" {tag} |"
                    else:
                        row += " - |"
                row += f" {'Y' if info['stable'] else 'N'} |"
                lines.append(row)
            lines.append("")

    # 4. Velocity
    lines.append("## 4. D1 Velocity")
    lines.append("")
    vel = output["per_gen_velocity"]
    lines.append("| α | mean_vel | early | late | decel_ratio |")
    lines.append("|---|----------|-------|------|-------------|")
    for ak in sorted(vel.keys()):
        v = vel[ak]
        decel = f"{v['deceleration_ratio']:.2f}" if v.get("deceleration_ratio") else "N/A"
        lines.append(f"| {v['alpha']:.2f} | {v['mean_velocity']:+.6f} | "
                     f"{v['early_mean_velocity']:+.6f} | {v['late_mean_velocity']:+.6f} | {decel} |")
    lines.append("")

    with open(out_path, "w") as f:
        f.write("\n".join(lines))
    return out_path


# ---------------------------------------------------------------------------
# Output / summary
# ---------------------------------------------------------------------------

def auto_version():
    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    existing = glob.glob(os.path.join(ANALYSIS_DIR, "cross_alpha_v*.json"))
    max_v = 0
    for f in existing:
        m = re.search(r"cross_alpha_v(\d+)", f)
        if m:
            max_v = max(max_v, int(m.group(1)))
    return max_v + 1


def print_summary(output):
    print("\n" + "=" * 80)
    print("CROSS-ALPHA ANALYSIS SUMMARY (v4)")
    print("=" * 80)

    # Dose-response table
    dr = output["dose_response"]
    alphas = sorted(dr.keys())
    print(f"\nDOSE-RESPONSE (drift %)")
    print("-" * 80)
    header = f"{'Metric':<16}"
    for ak in alphas:
        header += f" | a={dr[ak]['alpha']:<5}"
    print(header)
    print("-" * 80)
    for metric in METRICS:
        line = f"{metric:<16}"
        for ak in alphas:
            d = dr[ak][metric]["drift_pct"]
            line += f" | {d:>+7.1f}%"
        print(line)

    # Granger table
    gc = output["granger_causality"]
    print(f"\nGRANGER CAUSALITY (bidirectional, differenced, permutation)")
    print("-" * 80)
    header = f"{'Direction':<20}"
    alpha_keys = sorted(set(r["alpha_key"] for r in gc))
    for ak in alpha_keys:
        header += f" | a={[r for r in gc if r['alpha_key']==ak][0]['alpha']:<4} p_raw   p_fdr"
    print(header)
    print("-" * 80)

    directions = list(dict.fromkeys(r["direction"] for r in gc))
    for d in directions:
        line = f"{d:<20}"
        for ak in alpha_keys:
            match = [r for r in gc if r["alpha_key"] == ak and r["direction"] == d]
            if match:
                r = match[0]
                p_raw = f"{r['p_raw']:.4f}" if r.get("p_raw") is not None else "  N/A "
                p_fdr = f"{r.get('p_fdr', 'N/A')}" if r.get("p_fdr") is not None else "  N/A "
                if isinstance(p_fdr, float):
                    p_fdr = f"{p_fdr:.4f}"
                sig = "*" if r.get("p_fdr") is not None and r["p_fdr"] < 0.05 else " "
                fp = "FP?" if r.get("note", "").startswith("consistent") else "   "
                line += f" | {p_raw} {p_fdr:>7} {sig}{fp}"
            else:
                line += f" |    --       --     "
        print(line)

    valid = [r for r in gc if r.get("p_raw") is not None]
    n_total = len(valid)
    n_raw_sig = sum(1 for r in valid if r["p_raw"] < 0.05)
    n_fdr_sig = sum(1 for r in valid if r.get("p_fdr") is not None and r["p_fdr"] < 0.05)
    print(f"\nFDR: {n_raw_sig}/{n_total} raw-sig -> {n_fdr_sig}/{n_total} FDR-sig "
          f"(BH correction across all {n_total} tests)")

    # Consensus per alpha
    if "consensus_per_alpha" in output:
        cpa = output["consensus_per_alpha"]
        print(f"\nCONSENSUS CLASSIFICATION PER ALPHA")
        print("-" * 80)
        for ak in sorted(cpa.keys(), key=lambda k: cpa[k]["alpha"]):
            entry = cpa[ak]
            print(f"\n  a={entry['alpha']:.2f} [{entry['note']}]")
            print(f"    Robust: {entry['consensus']['n_robust']}/{entry['n_pairs']}, "
                  f"Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}")
            for cl in entry["consensus"]["classifications"]:
                if cl["is_robust"]:
                    print(f"      ROBUST  {cl['pair_label']:<35s} ({cl['n_sig_methods']}/{entry['n_methods']} methods)")

        if "consensus_regime_comparison" in output:
            rc = output["consensus_regime_comparison"]
            print(f"\n  REGIME COMPARISON: {rc['n_stable']}/{rc['n_pairs']} stable, "
                  f"{rc['n_regime_dependent']}/{rc['n_pairs']} regime-dependent")
            changed = [l for l, p in rc["pairs"].items() if not p["stable"]]
            if changed:
                print(f"    Regime-dependent pairs:")
                for label in changed:
                    info = rc["pairs"][label]
                    tags = []
                    for ak in rc["alpha_keys"]:
                        if ak in info["per_alpha"]:
                            v = info["per_alpha"][ak]
                            t = "R" if v["is_robust"] else "."
                            tags.append(f"a={v['alpha']:.2f}:{t}")
                    print(f"      {label:<35s} {' '.join(tags)}")

    # Cross-correlation
    xcorr = output["cross_correlation"]
    print(f"\nCROSS-CORRELATION (delta-metric, peak lag)")
    print("-" * 60)
    for pair_label in ["entropy_vs_d1", "ece_vs_d1"]:
        line = f"  {pair_label:<18}"
        for ak in sorted(xcorr.keys()):
            p = xcorr[ak].get(pair_label, {})
            line += f" | a={xcorr[ak]['alpha']}: lag={p.get('peak_lag','?'):>2} r={p.get('peak_r','?'):>7}"
        print(line)

    # Velocity
    vel = output["per_gen_velocity"]
    print(f"\nD1 VELOCITY")
    print("-" * 60)
    for ak in sorted(vel.keys()):
        v = vel[ak]
        decel = f"{v['deceleration_ratio']:.2f}" if v.get("deceleration_ratio") is not None else "N/A"
        print(f"  a={v['alpha']}: mean_vel={v['mean_velocity']:+.6f}  "
              f"early={v['early_mean_velocity']:+.6f}  late={v['late_mean_velocity']:+.6f}  "
              f"decel_ratio={decel}  max_drop=gen{v['max_drop_gen']}")

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Cross-alpha analysis v4 with per-alpha consensus classification."
    )
    parser.add_argument("--alpha-dirs", nargs="*", default=None,
                        help="Specific alpha dirs (e.g. a000_s42 a025_s42 mvp). Default: auto-discover all.")
    parser.add_argument("--n-perms", type=int, default=5000,
                        help="Permutations for Granger test (default: 5000)")
    parser.add_argument("--consensus-n-perms", type=int, default=1000,
                        help="Permutations for consensus perm_granger method (default: 1000)")
    parser.add_argument("--max-lag", type=int, default=1,
                        help="Max lag for Granger test (default: 1)")
    parser.add_argument("--no-mvp", action="store_true",
                        help="Exclude MVP (alpha=1.0) from auto-discovery")
    parser.add_argument("--no-consensus", action="store_true",
                        help="Skip consensus classification (faster)")
    parser.add_argument("--version", type=int, default=None,
                        help="Output version number (default: auto-increment)")
    parser.add_argument("--update-registry", action="store_true",
                        help="Print registry update commands after analysis")
    args = parser.parse_args()

    alpha_dirs = discover_alpha_dirs(args.alpha_dirs, include_mvp=not args.no_mvp)
    if not alpha_dirs:
        print("ERROR: No alpha directories found.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(alpha_dirs)} alpha points: "
          f"{[(a[0], f'seeds={a[3]}') for a in alpha_dirs]}")

    # Load primary seed data (seed=42) for v3 analyses
    all_data = []
    for alpha_key, alpha_val, path, seeds in alpha_dirs:
        metrics = load_metrics(path)
        print(f"  {alpha_key} (a={alpha_val}): {len(metrics)} generations, seeds={seeds}")
        all_data.append((alpha_key, alpha_val, metrics))

    # 1. Dose-response
    dose_resp = compute_dose_response(all_data)

    # 2. Granger
    print(f"\nRunning bidirectional Granger ({len(GRANGER_PAIRS)} pairs x {len(all_data)} alphas, "
          f"n_perms={args.n_perms})...")
    granger = run_granger_all(all_data, max_lag=args.max_lag, n_perms=args.n_perms)
    granger = apply_fdr(granger)

    # 3. Cross-correlation
    xcorr = cross_correlation(all_data)

    # 4. Velocity
    velocity = per_gen_velocity(all_data)

    # Assemble output
    version = args.version or auto_version()
    n_gens = len(all_data[0][2]) if all_data else 0
    output = {
        "version": f"v{version}",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "n_alphas": len(all_data),
        "alpha_points": [a[1] for a in all_data],
        "n_generations": n_gens,
        "gen_range": f"gen_0 to gen_{n_gens - 1}" if n_gens else "N/A",
        "statistical_config": {
            "granger_max_lag": args.max_lag,
            "granger_n_perm": args.n_perms,
            "granger_differenced": True,
            "fdr_method": "benjamini-hochberg",
            "fdr_scope": f"all {len(granger)} tests corrected together",
            "n_independent_tests": len([r for r in granger if r.get("p_raw") is not None]),
        },
        "dose_response": dose_resp,
        "granger_causality": granger,
        "cross_correlation": xcorr,
        "per_gen_velocity": velocity,
    }

    # 5. Consensus per alpha
    if not args.no_consensus:
        mvp_ablation = os.path.join(MVP_DIR, "analysis", "method_ablation.json")
        print(f"\nRunning per-alpha consensus classification "
              f"(5 methods x 16 pairs x {len(alpha_dirs)} alphas)...")
        consensus_results = run_consensus_per_alpha(
            alpha_dirs, mvp_ablation_path=mvp_ablation,
            consensus_n_perm=args.consensus_n_perms)
        output["consensus_per_alpha"] = consensus_results
        output["consensus_regime_comparison"] = consensus_regime_comparison(consensus_results)

    # Save JSON
    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    json_path = os.path.join(ANALYSIS_DIR, f"cross_alpha_v{version}.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False, cls=NumpyEncoder)

    # Save Markdown report
    md_path = os.path.join(ANALYSIS_DIR, f"cross_alpha_v{version}_report.md")
    generate_markdown_report(output, md_path)

    print_summary(output)
    print(f"\nSaved: {json_path}")
    print(f"Report: {md_path}")

    if args.update_registry:
        print("\n--- Registry update commands ---")
        for alpha_key, alpha_val, _ in all_data:
            dr = dose_resp[alpha_key]
            print(f"# {alpha_key}: d1_drift={dr['distinct_1']['drift_pct']}%, "
                  f"entropy_drift={dr['token_entropy']['drift_pct']}%, "
                  f"ece_drift={dr['ece']['drift_pct']}%")


if __name__ == "__main__":
    main()
