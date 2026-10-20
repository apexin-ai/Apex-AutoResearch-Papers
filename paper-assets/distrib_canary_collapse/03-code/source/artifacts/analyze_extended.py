# analyze_extended.py — Plan-006 extended 20-gen analysis
# Input:  results/extended_20gen/s{seed}/all_metrics.json
# Output: results/extended_20gen/analysis/{extended_analysis.json, summary.txt, mvp_comparison.json}

import argparse
import json
import os
import sys
import warnings
from datetime import datetime

import numpy as np
from scipy import stats
from statsmodels.stats.multitest import multipletests
from statsmodels.tsa.stattools import adfuller

from permutation_granger import permutation_granger_test
from detrending_utils import detrend, cross_correlate, detrend_and_crosscorr

warnings.filterwarnings("ignore")

CANARY_METRICS = ["token_entropy", "ece"]
DOWNSTREAM_METRICS = ["distinct_1", "distinct_2", "distinct_3", "perplexity"]
HIGHER_IS_WORSE = {"self_bleu", "ece", "perplexity"}
LOWER_IS_WORSE = {"token_entropy", "effective_rank", "distinct_1", "distinct_2",
                   "distinct_3", "mauve"}
ALPHA_SIG = 0.05
N_PERM = 5000


# ── helpers ──────────────────────────────────────────────────────────────

def load_metrics(path):
    """Load all_metrics.json, return sorted list of dicts."""
    with open(path) as f:
        data = json.load(f)
    return sorted(data, key=lambda m: m["generation"])


def extract(metrics_list, name):
    return np.array([m[name] for m in metrics_list])


def orient(series, name):
    return -series.copy() if name in LOWER_IS_WORSE else series.copy()


def cohen_r_label(r):
    r = abs(r)
    if r >= 0.5:   return "large"
    if r >= 0.3:   return "medium"
    if r >= 0.1:   return "small"
    return "negligible"


def cohen_f2_label(f2):
    if f2 is None: return "N/A"
    if f2 >= 0.35: return "large"
    if f2 >= 0.15: return "medium"
    if f2 >= 0.02: return "small"
    return "negligible"


def adf_order(series, max_d=2):
    for d in range(max_d + 1):
        s = series.copy()
        for _ in range(d):
            s = np.diff(s)
        if len(s) < 5:
            return d
        try:
            if adfuller(s, maxlag=1, autolag=None)[1] < 0.05:
                return d
        except Exception:
            pass
    return max_d


# ── 1. Cross-correlation (raw + detrended) ──────────────────────────────

def full_crosscorr(canary, downstream, cn, dn, max_lag=10):
    """Raw and first-differenced cross-correlation with permutation p-value."""
    c, d = orient(extract(canary, cn), cn), orient(extract(downstream, dn), dn)

    # raw
    raw_corrs = cross_correlate(c, d, max_lag=max_lag)
    raw_peak_lag = max(raw_corrs, key=lambda k: abs(raw_corrs[k]))
    raw_peak_r = raw_corrs[raw_peak_lag]

    # first-differenced
    dt = detrend_and_crosscorr(c, d, method="first_diff", max_lag=max_lag)
    diff_peak_lag = dt["peak_lag"]
    diff_peak_r = dt["peak_corr"]

    # permutation p-value for raw peak
    n = len(c)
    obs_abs_r = abs(raw_peak_r)
    rng = np.random.RandomState(42)
    count_ge = 0
    for _ in range(N_PERM):
        d_shuf = rng.permutation(d)
        shuf_corrs = cross_correlate(c, d_shuf, max_lag=max_lag)
        max_perm_r = max(abs(v) for v in shuf_corrs.values())
        if max_perm_r >= obs_abs_r:
            count_ge += 1
    p_raw = (count_ge + 1) / (N_PERM + 1)

    # permutation p-value for diff peak
    dc, dd = np.diff(c), np.diff(d)
    obs_abs_r_diff = abs(diff_peak_r)
    rng2 = np.random.RandomState(43)
    count_ge2 = 0
    for _ in range(N_PERM):
        dd_shuf = rng2.permutation(dd)
        shuf_corrs2 = cross_correlate(dc, dd_shuf, max_lag=max_lag)
        max_perm_r2 = max(abs(v) for v in shuf_corrs2.values())
        if max_perm_r2 >= obs_abs_r_diff:
            count_ge2 += 1
    p_diff = (count_ge2 + 1) / (N_PERM + 1)

    return {
        "canary": cn, "downstream": dn,
        "raw_peak_lag": int(raw_peak_lag),
        "raw_peak_r": round(float(raw_peak_r), 4),
        "raw_abs_r": round(float(obs_abs_r), 4),
        "raw_p": round(float(p_raw), 6),
        "raw_effect_label": cohen_r_label(obs_abs_r),
        "diff_peak_lag": int(diff_peak_lag),
        "diff_peak_r": round(float(diff_peak_r), 4),
        "diff_abs_r": round(float(obs_abs_r_diff), 4),
        "diff_p": round(float(p_diff), 6),
        "diff_effect_label": cohen_r_label(obs_abs_r_diff),
        "all_raw_corrs": {str(k): round(float(v), 4) for k, v in raw_corrs.items()},
    }


# ── 2. Permutation Granger ──────────────────────────────────────────────

def run_permutation_granger(metrics_list, cn, dn, max_lag=1, n_perm=N_PERM):
    """Permutation Granger test for a single pair."""
    c = extract(metrics_list, cn)
    d = extract(metrics_list, dn)
    res = permutation_granger_test(c, d, max_lag=max_lag, n_perm=n_perm, seed=42)
    res["canary"] = cn
    res["downstream"] = dn
    return res


# ── 3. Toda-Yamamoto Granger ────────────────────────────────────────────

def toda_yamamoto(metrics_list, cn, dn, d_max_mode="adaptive"):
    """TY Granger causality. d_max_mode: 'adaptive', or int (0,1,2)."""
    c = orient(extract(metrics_list, cn), cn)
    d = orient(extract(metrics_list, dn), dn)
    n = len(c)

    if d_max_mode == "adaptive":
        dc, dd = adf_order(c), adf_order(d)
        d_max = max(dc, dd)
    else:
        d_max = int(d_max_mode)
        dc = dd = d_max

    p_order = 1
    k = p_order + d_max
    T_eff = n - k
    n_params = 1 + 2 * k
    df_resid = T_eff - n_params

    base = {"canary": cn, "downstream": dn, "method": "toda_yamamoto",
            "p_order": int(p_order), "d_max": int(d_max), "d_max_mode": str(d_max_mode),
            "k": int(k), "d_canary": int(dc), "d_downstream": int(dd),
            "T": int(n), "T_eff": int(T_eff)}

    if df_resid < 1:
        return {**base, "wald_F": None, "p_value": 1.0, "significant": False,
                "effect_size_f2": None, "effect_size_label": "N/A",
                "note": f"no residual df (T_eff={T_eff}, params={n_params})"}

    Y = d[k:]
    X_cols = [np.ones(T_eff)]
    for lag in range(1, k + 1):
        X_cols.append(c[k - lag: n - lag])
        X_cols.append(d[k - lag: n - lag])
    X = np.column_stack(X_cols)

    try:
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        resid = Y - X @ beta
        sigma2 = np.sum(resid ** 2) / df_resid
        XtX_inv = np.linalg.inv(X.T @ X)
    except Exception:
        return {**base, "wald_F": None, "p_value": 1.0, "significant": False,
                "effect_size_f2": None, "effect_size_label": "N/A", "note": "OLS failed"}

    test_idx = [2 * (lag - 1) + 1 for lag in range(1, p_order + 1)]
    R = np.zeros((p_order, n_params))
    for i, idx in enumerate(test_idx):
        R[i, idx] = 1.0

    Rb = R @ beta
    try:
        cov_Rb = sigma2 * (R @ XtX_inv @ R.T)
        W = float(Rb @ np.linalg.inv(cov_Rb) @ Rb)
        F = W / p_order
        pval = float(1.0 - stats.f.cdf(F, p_order, df_resid))
    except Exception:
        return {**base, "wald_F": None, "p_value": 1.0, "significant": False,
                "effect_size_f2": None, "effect_size_label": "N/A", "note": "Wald failed"}

    f2 = F * p_order / df_resid if df_resid > 0 else None
    return {**base, "wald_F": round(float(F), 4),
            "p_value": round(float(pval), 6),
            "significant": bool(pval < ALPHA_SIG),
            "effect_size_f2": round(float(f2), 4) if f2 is not None else None,
            "effect_size_label": cohen_f2_label(f2)}


# ── 4. BH FDR correction ────────────────────────────────────────────────

def apply_bh_fdr(results_list, p_key="p_value"):
    """Apply BH FDR correction. Adds p_fdr and significant_fdr."""
    p_values, valid_idx = [], []
    for i, r in enumerate(results_list):
        p = r.get(p_key)
        if p is not None and np.isfinite(p):
            p_values.append(p)
            valid_idx.append(i)
        else:
            r["p_fdr"] = None
            r["significant_fdr"] = False

    if not p_values:
        return results_list

    reject, q_values, _, _ = multipletests(p_values, alpha=ALPHA_SIG, method='fdr_bh')
    for j, idx in enumerate(valid_idx):
        results_list[idx]["p_fdr"] = round(float(q_values[j]), 6)
        results_list[idx]["significant_fdr"] = bool(reject[j])
    return results_list


# ── 5. Window analysis ──────────────────────────────────────────────────

def window_analysis(metrics_list, start_gen, end_gen, label, max_lag=10):
    """Run cross-corr + permutation Granger on a sub-window."""
    sub = [m for m in metrics_list if start_gen <= m["generation"] <= end_gen]
    if len(sub) < 5:
        return {"label": label, "error": f"too few points: {len(sub)}"}

    xcorr_results = []
    granger_results = []
    for cn in CANARY_METRICS:
        for dn in DOWNSTREAM_METRICS:
            xcorr_results.append(full_crosscorr(sub, sub, cn, dn, max_lag=max_lag))
            granger_results.append(run_permutation_granger(sub, cn, dn, max_lag=1))

    granger_results = apply_bh_fdr(granger_results)

    return {
        "label": label,
        "gen_range": [start_gen, end_gen],
        "n_points": len(sub),
        "cross_correlations": xcorr_results,
        "permutation_granger": granger_results,
    }


# ── 6. MVP comparison ───────────────────────────────────────────────────

def compare_with_mvp(extended_results, mvp_dir, seeds):
    """Compare extended 20-gen results with MVP 10-gen."""
    comparison = {}
    for seed in seeds:
        mvp_path = os.path.join(mvp_dir, f"rep_{seed}", "all_metrics.json")
        if not os.path.isfile(mvp_path):
            comparison[f"seed_{seed}"] = {"error": f"MVP data not found: {mvp_path}"}
            continue

        mvp_metrics = load_metrics(mvp_path)
        mvp_xcorr = []
        mvp_granger = []
        for cn in CANARY_METRICS:
            for dn in DOWNSTREAM_METRICS:
                mvp_xcorr.append(full_crosscorr(mvp_metrics, mvp_metrics, cn, dn, max_lag=5))
                mvp_granger.append(run_permutation_granger(mvp_metrics, cn, dn))
        mvp_granger = apply_bh_fdr(mvp_granger)

        ext_key = f"seed_{seed}"
        ext_data = extended_results.get(ext_key)
        if ext_data is None:
            comparison[ext_key] = {
                "mvp_xcorr": mvp_xcorr, "mvp_granger": mvp_granger,
                "note": "extended data not available yet"
            }
            continue

        pair_comparisons = []
        for cn in CANARY_METRICS:
            for dn in DOWNSTREAM_METRICS:
                mvp_xc = next((x for x in mvp_xcorr
                               if x["canary"] == cn and x["downstream"] == dn), None)
                ext_xc = next((x for x in ext_data["full_series"]["cross_correlations"]
                               if x["canary"] == cn and x["downstream"] == dn), None)
                mvp_gr = next((g for g in mvp_granger
                               if g["canary"] == cn and g["downstream"] == dn), None)
                ext_gr = next((g for g in ext_data["full_series"]["permutation_granger"]
                               if g["canary"] == cn and g["downstream"] == dn), None)
                pair_comparisons.append({
                    "canary": cn, "downstream": dn,
                    "mvp_lag": mvp_xc["raw_peak_lag"] if mvp_xc else None,
                    "ext_lag": ext_xc["raw_peak_lag"] if ext_xc else None,
                    "lag_stable": (mvp_xc["raw_peak_lag"] == ext_xc["raw_peak_lag"]
                                   if mvp_xc and ext_xc else None),
                    "mvp_p": mvp_gr.get("p_value") if mvp_gr else None,
                    "ext_p": ext_gr.get("p_value") if ext_gr else None,
                    "mvp_sig": mvp_gr.get("significant") if mvp_gr else None,
                    "ext_sig": ext_gr.get("significant") if ext_gr else None,
                    "power_gain": (mvp_gr.get("p_value", 1) > ALPHA_SIG and
                                   ext_gr.get("p_value", 1) < ALPHA_SIG
                                   if mvp_gr and ext_gr else None),
                })
        comparison[ext_key] = {
            "mvp_n": len(mvp_metrics),
            "ext_n": ext_data["full_series"]["n_points"],
            "pairs": pair_comparisons,
        }
    return comparison


# ── main ─────────────────────────────────────────────────────────────────

def analyze_seed(metrics_path, max_lag=10):
    """Full analysis pipeline for a single seed."""
    metrics = load_metrics(metrics_path)
    n = len(metrics)
    gens = [m["generation"] for m in metrics]

    # 1. Full series cross-corr + permutation Granger
    xcorr_full = []
    granger_full = []
    for cn in CANARY_METRICS:
        for dn in DOWNSTREAM_METRICS:
            xcorr_full.append(full_crosscorr(metrics, metrics, cn, dn, max_lag=max_lag))
            granger_full.append(run_permutation_granger(metrics, cn, dn, max_lag=1))
    granger_full = apply_bh_fdr(granger_full)

    full_series = {
        "gen_range": [min(gens), max(gens)],
        "n_points": n,
        "max_lag": max_lag,
        "cross_correlations": xcorr_full,
        "permutation_granger": granger_full,
    }

    # 2. Rolling window (exclude gen 0→1 artifact): gen 5-end
    last_gen = max(gens)
    rolling = window_analysis(metrics, 5, last_gen, f"gen_5_to_{last_gen}", max_lag=max_lag)

    # 3. TY supplementary (d_max = 0, 1, adaptive)
    ty_results = []
    for d_mode in [0, 1, "adaptive"]:
        for cn in CANARY_METRICS:
            for dn in DOWNSTREAM_METRICS:
                ty_results.append(toda_yamamoto(metrics, cn, dn, d_max_mode=d_mode))
    ty_results = apply_bh_fdr(ty_results)

    # 4. Effect size summary for key pair
    key_pair_xcorr = next((x for x in xcorr_full
                           if x["canary"] == "token_entropy" and x["downstream"] == "perplexity"), None)
    key_pair_granger = next((g for g in granger_full
                             if g["canary"] == "token_entropy" and g["downstream"] == "perplexity"), None)

    return {
        "metrics_path": metrics_path,
        "full_series": full_series,
        "rolling_window": rolling,
        "ty_supplementary": ty_results,
        "key_pair_token_entropy_perplexity": {
            "xcorr": key_pair_xcorr,
            "granger": key_pair_granger,
        },
    }


def write_summary(path, results, comparison):
    """Write human-readable summary."""
    lines = []
    w = lines.append

    w("=" * 72)
    w("PLAN-006 EXTENDED 20-GEN ANALYSIS")
    w(f"Generated: {datetime.now().isoformat()}")
    w("=" * 72)

    for seed_key, data in sorted(results.items()):
        w(f"\n{'─' * 72}")
        w(f"  {seed_key}")
        w(f"{'─' * 72}")

        fs = data["full_series"]
        w(f"\n  FULL SERIES (gen {fs['gen_range'][0]}-{fs['gen_range'][1]}, "
          f"N={fs['n_points']}, max_lag={fs['max_lag']})")
        w(f"  {'Canary':<16} {'Downstream':<12} {'RawLag':>7} {'|r|':>6} "
          f"{'p_raw':>8} {'DiffLag':>8} {'|r|_d':>6} {'p_diff':>8} {'Grng_p':>8} {'FDR_q':>8} {'Sig':>4}")
        w("  " + "-" * 100)

        for xc in fs["cross_correlations"]:
            cn, dn = xc["canary"], xc["downstream"]
            gr = next((g for g in fs["permutation_granger"]
                       if g["canary"] == cn and g["downstream"] == dn), {})
            sig = "***" if gr.get("significant_fdr") else ("*" if gr.get("significant") else "")
            gr_p = f"{gr.get('p_value', 'N/A'):>8}" if isinstance(gr.get('p_value'), float) else "     N/A"
            fdr_q = f"{gr.get('p_fdr', 'N/A'):>8}" if isinstance(gr.get('p_fdr'), float) else "     N/A"
            w(f"  {cn:<16} {dn:<12} {xc['raw_peak_lag']:>7} {xc['raw_abs_r']:>6.3f} "
              f"{xc['raw_p']:>8.4f} {xc['diff_peak_lag']:>8} {xc['diff_abs_r']:>6.3f} "
              f"{xc['diff_p']:>8.4f} {gr_p} {fdr_q} {sig:>4}")

        # Key pair highlight
        kp = data.get("key_pair_token_entropy_perplexity", {})
        kpx = kp.get("xcorr")
        kpg = kp.get("granger")
        if kpx:
            w(f"\n  KEY PAIR: token_entropy → perplexity")
            w(f"    Raw:  lag={kpx['raw_peak_lag']}, |r|={kpx['raw_abs_r']:.3f} ({kpx['raw_effect_label']}), p={kpx['raw_p']:.4f}")
            w(f"    Diff: lag={kpx['diff_peak_lag']}, |r|={kpx['diff_abs_r']:.3f} ({kpx['diff_effect_label']}), p={kpx['diff_p']:.4f}")
        if kpg:
            w(f"    Granger: F={kpg.get('f_stat')}, p={kpg.get('p_value')}, "
              f"f²={kpg.get('effect_size_f2')}, sig={kpg.get('significant')}")

        # Rolling window
        rw = data["rolling_window"]
        if "error" not in rw:
            w(f"\n  ROLLING WINDOW ({rw['label']}, N={rw['n_points']})")
            w(f"  {'Canary':<16} {'Downstream':<12} {'RawLag':>7} {'|r|':>6} "
              f"{'DiffLag':>8} {'Grng_p':>8} {'Sig':>4}")
            w("  " + "-" * 70)
            for xc in rw["cross_correlations"]:
                cn, dn = xc["canary"], xc["downstream"]
                gr = next((g for g in rw["permutation_granger"]
                           if g["canary"] == cn and g["downstream"] == dn), {})
                sig = "***" if gr.get("significant_fdr") else ("*" if gr.get("significant") else "")
                gr_p = f"{gr.get('p_value', 'N/A'):>8}" if isinstance(gr.get('p_value'), float) else "     N/A"
                w(f"  {cn:<16} {dn:<12} {xc['raw_peak_lag']:>7} {xc['raw_abs_r']:>6.3f} "
                  f"{xc['diff_peak_lag']:>8} {gr_p} {sig:>4}")
        else:
            w(f"\n  ROLLING WINDOW: {rw['error']}")

        # TY supplementary
        w(f"\n  TY SUPPLEMENTARY")
        w(f"  {'d_max':>5} {'Canary':<16} {'Downstream':<12} {'F':>8} {'p':>8} {'f²':>8} {'Sig':>4}")
        w("  " + "-" * 70)
        for ty in data["ty_supplementary"]:
            sig = "*" if ty.get("significant") else ""
            F_str = f"{ty['wald_F']:.3f}" if ty.get("wald_F") is not None else "N/A"
            p_str = f"{ty['p_value']:.4f}" if isinstance(ty.get("p_value"), float) else "N/A"
            f2_str = f"{ty['effect_size_f2']:.3f}" if ty.get("effect_size_f2") is not None else "N/A"
            w(f"  {ty['d_max']:>5} {ty['canary']:<16} {ty['downstream']:<12} "
              f"{F_str:>8} {p_str:>8} {f2_str:>8} {sig:>4}")

    # MVP comparison
    if comparison:
        w(f"\n{'=' * 72}")
        w("MVP (10-gen) vs EXTENDED (20-gen) COMPARISON")
        w("=" * 72)
        for sk, comp in sorted(comparison.items()):
            w(f"\n  {sk}:")
            if "error" in comp:
                w(f"    {comp['error']}")
                continue
            if "note" in comp:
                w(f"    {comp['note']}")
                continue
            w(f"    MVP N={comp['mvp_n']}, Extended N={comp['ext_n']}")
            w(f"    {'Canary':<16} {'Downstream':<12} {'MVPlag':>7} {'EXTlag':>7} "
              f"{'Stable':>7} {'MVP_p':>8} {'EXT_p':>8} {'PowerGain':>10}")
            w("    " + "-" * 80)
            for p in comp["pairs"]:
                mvp_l = str(p["mvp_lag"]) if p["mvp_lag"] is not None else "N/A"
                ext_l = str(p["ext_lag"]) if p["ext_lag"] is not None else "N/A"
                stable = "YES" if p["lag_stable"] else ("NO" if p["lag_stable"] is not None else "N/A")
                mvp_p = f"{p['mvp_p']:.4f}" if isinstance(p["mvp_p"], float) else "N/A"
                ext_p = f"{p['ext_p']:.4f}" if isinstance(p["ext_p"], float) else "N/A"
                pg = "YES" if p["power_gain"] else ("" if p["power_gain"] is not None else "N/A")
                w(f"    {p['canary']:<16} {p['downstream']:<12} {mvp_l:>7} {ext_l:>7} "
                  f"{stable:>7} {mvp_p:>8} {ext_p:>8} {pg:>10}")

    w("\n" + "=" * 72)
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", default="results/extended_20gen",
                        help="Directory containing s42/, s43/ subdirs")
    parser.add_argument("--mvp_dir", default="results/mvp",
                        help="MVP results directory")
    parser.add_argument("--seeds", nargs="+", type=int, default=[42, 43])
    parser.add_argument("--max_lag", type=int, default=10)
    parser.add_argument("--dry_run", action="store_true",
                        help="Use MVP data for structural validation")
    args = parser.parse_args()

    results = {}

    if args.dry_run:
        print("=== DRY RUN MODE: using MVP data for validation ===")
        for seed in args.seeds:
            mvp_path = os.path.join(args.mvp_dir, f"rep_{seed}", "all_metrics.json")
            if not os.path.isfile(mvp_path):
                print(f"  SKIP seed {seed}: {mvp_path} not found")
                continue
            print(f"  Analyzing MVP seed {seed} ({mvp_path}) ...")
            results[f"seed_{seed}"] = analyze_seed(mvp_path, max_lag=min(args.max_lag, 5))
            print(f"  Done.")
    else:
        for seed in args.seeds:
            path = os.path.join(args.results_dir, f"s{seed}", "all_metrics.json")
            if not os.path.isfile(path):
                print(f"  SKIP seed {seed}: {path} not found")
                continue
            print(f"  Analyzing seed {seed} ({path}) ...")
            results[f"seed_{seed}"] = analyze_seed(path, max_lag=args.max_lag)
            print(f"  Done.")

    if not results:
        print("ERROR: no data found to analyze", file=sys.stderr)
        sys.exit(1)

    # MVP comparison
    comparison = compare_with_mvp(results, args.mvp_dir, args.seeds)

    # Output
    out_dir = os.path.join(args.results_dir, "analysis")
    if args.dry_run:
        out_dir = os.path.join(args.mvp_dir, "analysis_dryrun")
    os.makedirs(out_dir, exist_ok=True)

    analysis_path = os.path.join(out_dir, "extended_analysis.json")
    with open(analysis_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Analysis JSON: {analysis_path}")

    summary_path = os.path.join(out_dir, "summary.txt")
    write_summary(summary_path, results, comparison)
    print(f"Summary: {summary_path}")

    comp_path = os.path.join(out_dir, "mvp_comparison.json")
    with open(comp_path, "w") as f:
        json.dump(comparison, f, indent=2, default=str)
    print(f"MVP comparison: {comp_path}")

    # Print key result to stdout
    for sk, data in results.items():
        kp = data.get("key_pair_token_entropy_perplexity", {})
        kpx = kp.get("xcorr")
        kpg = kp.get("granger")
        if kpx and kpg:
            print(f"\n  {sk} KEY: token_entropy→perplexity "
                  f"lag={kpx['raw_peak_lag']}, |r|={kpx['raw_abs_r']:.3f}, "
                  f"granger_p={kpg.get('p_value')}")


if __name__ == "__main__":
    main()
