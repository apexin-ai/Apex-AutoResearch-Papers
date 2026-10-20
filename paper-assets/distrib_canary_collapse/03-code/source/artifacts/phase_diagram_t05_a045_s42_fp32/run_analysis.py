"""5-method lead-lag analysis for phase_diagram_t05_a045_s42_fp32.
T=5 generations, alpha=0.45, seed=42, fp32, Pythia-410m.
Adapted from canonical run_analysis.py methodology.
"""
import json
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.vector_ar.var_model import VAR

N_PERM = 5000
ALPHA_SIG = 0.05

CANARIES = ["token_entropy", "ece"]
DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3", "mauve"]

HIGHER_IS_WORSE = {"ece"}
LOWER_IS_WORSE = {"token_entropy", "distinct_1", "distinct_2", "distinct_3", "mauve"}

ALL_METRICS = [
  {"token_entropy": 3.23419483150593, "self_bleu": 0.011078699301381554, "ece": 0.010804557477709054, "effective_rank": 46.612774691899155, "perplexity": 26.948958972544652, "distinct_1": 0.0979600146585773, "distinct_2": 0.5141374985748489, "distinct_3": 0.8127010497341054, "mauve": 0.031110582626136873, "generation": 0, "effective_alpha": 0.45},
  {"token_entropy": 2.494058441616721, "self_bleu": 0.01181542928801186, "ece": 0.06666987054815446, "effective_rank": 58.30666526113631, "perplexity": 22.538010937788044, "distinct_1": 0.09759209446336131, "distinct_2": 0.5124500211292787, "distinct_3": 0.8121673127402459, "mauve": 0.0314065242440103, "generation": 1, "effective_alpha": 0.45},
  {"token_entropy": 2.534136101724104, "self_bleu": 0.012035022098091467, "ece": 0.0776851344230731, "effective_rank": 62.23149385795327, "perplexity": 25.144345507719237, "distinct_1": 0.0839296875, "distinct_2": 0.4432612754787147, "distinct_3": 0.7360505632900514, "mauve": 0.03256302608932375, "generation": 2, "effective_alpha": 0.45},
  {"token_entropy": 2.5901672458724554, "self_bleu": 0.01229421686114261, "ece": 0.07674335772304731, "effective_rank": 63.461815189636326, "perplexity": 26.117359098847647, "distinct_1": 0.0783828125, "distinct_2": 0.40030781490480394, "distinct_3": 0.671760496257754, "mauve": 0.03222753095848002, "generation": 3, "effective_alpha": 0.45},
  {"token_entropy": 2.5706613419304554, "self_bleu": 0.012043209085476533, "ece": 0.08360082054034103, "effective_rank": 63.453629462752325, "perplexity": 27.209104983248583, "distinct_1": 0.0730703125, "distinct_2": 0.36358096547629276, "distinct_3": 0.6132283316926826, "mauve": 0.0317127295809647, "generation": 4, "effective_alpha": 0.45},
  {"token_entropy": 2.5727669083072353, "self_bleu": 0.014117583793544781, "ece": 0.08865605692062944, "effective_rank": 62.76527409416098, "perplexity": 28.01640758040761, "distinct_1": 0.0698125, "distinct_2": 0.33251041023758, "distinct_3": 0.554649291395178, "mauve": 0.030588378386534935, "generation": 5, "effective_alpha": 0.45},
]


def orient(series, name):
    return -series.copy() if name in LOWER_IS_WORSE else series.copy()


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


def permutation_granger_test(x, y, max_lag=1, n_perm=1000, seed=42, difference=True):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if difference:
        x = np.diff(x)
        y = np.diff(y)
    f_obs = _granger_f_stat(y, x, max_lag)
    if np.isnan(f_obs):
        return {"f_stat": None, "p_value": None, "significant": False}
    rng = np.random.default_rng(seed)
    null_f = np.empty(n_perm)
    for i in range(n_perm):
        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)
    valid_null = null_f[~np.isnan(null_f)]
    if len(valid_null) == 0:
        return {"f_stat": round(float(f_obs), 4), "p_value": None, "significant": False}
    p_value = (np.sum(valid_null >= f_obs) + 1) / (len(valid_null) + 1)
    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)
    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)
    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)
    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None
    return {
        "f_stat": round(float(f_obs), 4),
        "p_value": round(float(p_value), 6),
        "null_mean": round(float(np.mean(valid_null)), 4),
        "null_std": round(float(np.std(valid_null)), 4),
        "effect_size_f2": round(float(f2), 4) if f2 is not None else None,
        "significant": bool(p_value < 0.05),
    }


def bh_fdr(p_values, alpha=0.05):
    pv = np.array(p_values, dtype=float)
    n = len(pv)
    valid = ~np.isnan(pv)
    adjusted = np.full(n, np.nan)
    if valid.sum() == 0:
        return adjusted.tolist(), [False] * n
    idx = np.where(valid)[0]
    p_valid = pv[idx]
    sorted_idx = np.argsort(p_valid)
    ranks = np.empty_like(sorted_idx)
    ranks[sorted_idx] = np.arange(1, len(p_valid) + 1)
    m = len(p_valid)
    adj = p_valid * m / ranks
    adj_sorted = adj[sorted_idx].copy()
    for i in range(m - 2, -1, -1):
        adj_sorted[i] = min(adj_sorted[i], adj_sorted[i + 1])
    adj_sorted = np.minimum(adj_sorted, 1.0)
    adj_final = np.empty(m)
    adj_final[sorted_idx] = adj_sorted
    for i, ix in enumerate(idx):
        adjusted[ix] = adj_final[i]
    significant = [(adjusted[i] < alpha if not np.isnan(adjusted[i]) else False) for i in range(n)]
    return adjusted.tolist(), significant


def naive_xcorr(c, d, cn, dn, max_lag=5):
    x, y = orient(c, cn), orient(d, dn)
    n = len(x)
    best_lag, best_r, best_p = 0, 0.0, 1.0
    all_lags = []
    for lag in range(-max_lag, max_lag + 1):
        if lag >= 0:
            a, b = x[lag:], y[:n - lag]
        else:
            a, b = x[:n + lag], y[-lag:]
        if len(a) < 4:
            continue
        r, p = stats.pearsonr(a, b)
        all_lags.append({"lag": int(lag), "r": round(float(r), 4), "p": round(float(p), 6)})
        if abs(r) > abs(best_r):
            best_lag, best_r, best_p = lag, r, p
    return {
        "method": "naive_xcorr",
        "peak_lag": int(best_lag),
        "r": round(float(best_r), 4),
        "p_value": round(float(best_p), 6),
        "significant": bool(best_p < ALPHA_SIG),
        "all_lags": all_lags,
    }


def diff_xcorr(c, d, cn, dn, max_lag=5):
    dx, dy = np.diff(orient(c, cn)), np.diff(orient(d, dn))
    n = len(dx)
    best_lag, best_r, best_p = 0, 0.0, 1.0
    all_lags = []
    for lag in range(-max_lag, max_lag + 1):
        if lag >= 0:
            a, b = dx[lag:], dy[:n - lag]
        else:
            a, b = dx[:n + lag], dy[-lag:]
        if len(a) < 4:
            continue
        if np.std(a) < 1e-12 or np.std(b) < 1e-12:
            continue
        r, p = stats.pearsonr(a, b)
        all_lags.append({"lag": int(lag), "r": round(float(r), 4), "p": round(float(p), 6)})
        if abs(r) > abs(best_r):
            best_lag, best_r, best_p = lag, r, p
    return {
        "method": "diff_xcorr",
        "peak_lag": int(best_lag),
        "r": round(float(best_r), 4),
        "p_value": round(float(best_p), 6),
        "significant": bool(best_p < ALPHA_SIG),
        "all_lags": all_lags,
    }


def _onset_gen(series, name):
    s = orient(series, name)
    base, sigma = s[0], np.std(s)
    if sigma < 1e-12:
        return None
    thresh = base + 3.0 * sigma
    for i in range(1, len(s)):
        if s[i] > thresh:
            return i
    return None


def threshold_onset(c, d, cn, dn):
    c_onset = _onset_gen(c, cn)
    d_onset = _onset_gen(d, dn)
    if c_onset is not None and d_onset is not None:
        lead_time = d_onset - c_onset
        significant = lead_time > 0
    else:
        lead_time = None
        significant = False
    return {
        "method": "threshold_onset",
        "canary_onset": c_onset,
        "downstream_onset": d_onset,
        "lead_time": lead_time,
        "significant": significant,
        "threshold": "true_3sigma_d105",
    }


def perm_granger(c, d, cn, dn, seed):
    x = orient(c, cn)
    y = orient(d, dn)
    result = permutation_granger_test(x, y, max_lag=1, n_perm=N_PERM, seed=seed, difference=True)
    return {
        "method": "perm_granger",
        "f_stat": result["f_stat"],
        "p_value": result["p_value"],
        "null_mean": result.get("null_mean"),
        "null_std": result.get("null_std"),
        "effect_size_f2": result.get("effect_size_f2"),
        "significant": bool(result["p_value"] < ALPHA_SIG) if result["p_value"] is not None else False,
    }


def ty_granger(c, d, cn, dn, max_order=2):
    x = orient(c, cn)
    y = orient(d, dn)
    n = len(x)
    d_max = 0
    for series in [x, y]:
        try:
            result = adfuller(series, maxlag=min(3, n // 3 - 1))
            if result[1] > 0.05:
                d_max = max(d_max, 1)
        except:
            d_max = max(d_max, 1)
    best_k, best_aic = 1, np.inf
    data = np.column_stack([x, y])
    for k in range(1, max_order + 1):
        try:
            model = VAR(data)
            result = model.fit(k)
            if result.aic < best_aic:
                best_k, best_aic = k, result.aic
        except:
            continue
    total_order = best_k + d_max
    if total_order >= n // 2:
        total_order = max(1, n // 2 - 1)
    try:
        model = VAR(data)
        result = model.fit(total_order)
        test_result = result.test_causality(causing=1, caused=0, kind="f")
        f_stat = float(test_result.test_statistic)
        p_value = float(test_result.pvalue)
        return {
            "method": "ty_granger",
            "f_stat": round(f_stat, 4),
            "p_value": round(p_value, 4),
            "significant": bool(p_value < ALPHA_SIG),
            "order": total_order,
            "k_opt": best_k,
            "d_max": d_max,
        }
    except Exception as e:
        return {
            "method": "ty_granger",
            "f_stat": None,
            "p_value": None,
            "significant": False,
            "error": str(e),
            "order": total_order,
            "k_opt": best_k,
            "d_max": d_max,
        }


def main():
    data = sorted(ALL_METRICS, key=lambda x: x["generation"])
    series = {}
    for k in CANARIES + DOWNSTREAMS:
        series[k] = np.array([d[k] for d in data])

    n_gens = len(data)
    seed = 42

    pairs = [{"canary": c, "downstream": d} for c in CANARIES for d in DOWNSTREAMS]

    pair_results = []
    perm_pval_fwd, perm_pval_rev = [], []
    diff_pval_fwd, diff_pval_rev = [], []

    for pair in pairs:
        cn, dn = pair["canary"], pair["downstream"]
        c, d = series[cn], series[dn]

        fwd_naive = naive_xcorr(c, d, cn, dn)
        fwd_diff = diff_xcorr(c, d, cn, dn)
        fwd_onset = threshold_onset(c, d, cn, dn)
        fwd_perm = perm_granger(c, d, cn, dn, seed)
        fwd_ty = ty_granger(c, d, cn, dn)

        rev_naive = naive_xcorr(d, c, dn, cn)
        rev_diff = diff_xcorr(d, c, dn, cn)
        rev_onset = threshold_onset(d, c, dn, cn)
        rev_perm = perm_granger(d, c, dn, cn, seed)
        rev_ty = ty_granger(d, c, dn, cn)

        result = {
            "canary": cn, "downstream": dn,
            "forward": {
                "naive_xcorr": fwd_naive, "diff_xcorr": fwd_diff,
                "threshold_onset": fwd_onset, "perm_granger": fwd_perm,
                "ty_granger": fwd_ty,
            },
            "reverse": {
                "naive_xcorr": rev_naive, "diff_xcorr": rev_diff,
                "threshold_onset": rev_onset, "perm_granger": rev_perm,
                "ty_granger": rev_ty,
            },
        }

        perm_pval_fwd.append(fwd_perm["p_value"] if fwd_perm["p_value"] is not None else np.nan)
        perm_pval_rev.append(rev_perm["p_value"] if rev_perm["p_value"] is not None else np.nan)
        diff_pval_fwd.append(fwd_diff["p_value"] if fwd_diff["p_value"] is not None else np.nan)
        diff_pval_rev.append(rev_diff["p_value"] if rev_diff["p_value"] is not None else np.nan)
        pair_results.append(result)

    perm_adj_fwd, perm_sig_fwd = bh_fdr(perm_pval_fwd)
    perm_adj_rev, perm_sig_rev = bh_fdr(perm_pval_rev)
    diff_adj_fwd, diff_sig_fwd = bh_fdr(diff_pval_fwd)
    diff_adj_rev, diff_sig_rev = bh_fdr(diff_pval_rev)

    for i, r in enumerate(pair_results):
        r["forward"]["perm_granger"]["p_fdr"] = round(perm_adj_fwd[i], 6) if not np.isnan(perm_adj_fwd[i]) else None
        r["forward"]["perm_granger"]["significant_fdr"] = perm_sig_fwd[i]
        r["reverse"]["perm_granger"]["p_fdr"] = round(perm_adj_rev[i], 6) if not np.isnan(perm_adj_rev[i]) else None
        r["reverse"]["perm_granger"]["significant_fdr"] = perm_sig_rev[i]
        r["forward"]["diff_xcorr"]["p_fdr"] = round(diff_adj_fwd[i], 6) if not np.isnan(diff_adj_fwd[i]) else None
        r["forward"]["diff_xcorr"]["significant_fdr"] = diff_sig_fwd[i]
        r["reverse"]["diff_xcorr"]["p_fdr"] = round(diff_adj_rev[i], 6) if not np.isnan(diff_adj_rev[i]) else None
        r["reverse"]["diff_xcorr"]["significant_fdr"] = diff_sig_rev[i]

    print("=" * 100)
    print("5-METHOD LEAD-LAG ANALYSIS | T=5 | alpha=0.45 | seed=42 | phase_diagram_t05_a045_s42_fp32")
    print("=" * 100)
    print(f"Loaded {n_gens} generations (NOTE: T=5, only 6 data points)\n")

    for direction in ["forward", "reverse"]:
        dir_label = "FORWARD (canary -> downstream)" if direction == "forward" else "REVERSE (downstream -> canary)"
        print(f"\n{'=' * 100}")
        print(f"  {dir_label}")
        print(f"{'=' * 100}")
        print(f"  {'Pair':<30} {'Naive XCorr':<20} {'Diff XCorr(FDR)':<20} {'Threshold':<18} {'PermG(FDR)':<20} {'TY Granger':<15}")
        print("-" * 130)
        for r in pair_results:
            label = f"{r['canary']}<{r['downstream']}"
            d = r[direction]

            naive_str = f"lag={d['naive_xcorr']['peak_lag']} r={d['naive_xcorr']['r']:.3f} {'*' if d['naive_xcorr']['significant'] else ''}"
            diff_p = d['diff_xcorr'].get('p_value')
            diff_str = f"lag={d['diff_xcorr']['peak_lag']} r={d['diff_xcorr']['r']:.3f} {'*' if d['diff_xcorr'].get('significant_fdr', False) else ''}" if diff_p is not None else "N/A (too few pts)"
            onset_str = f"c={d['threshold_onset']['canary_onset']} d={d['threshold_onset']['downstream_onset']} {'*' if d['threshold_onset']['significant'] else ''}"
            perm_str = f"F={d['perm_granger']['f_stat']:.2f} p={d['perm_granger']['p_value']:.4f} {'*' if d['perm_granger'].get('significant_fdr', False) else ''}" if d['perm_granger']['f_stat'] else "N/A"
            ty_str = f"F={d['ty_granger']['f_stat']:.2f} p={d['ty_granger']['p_value']:.4f} {'*' if d['ty_granger']['significant'] else ''}" if d['ty_granger']['f_stat'] else "N/A"
            print(f"  {label:<30} {naive_str:<20} {diff_str:<20} {onset_str:<18} {perm_str:<20} {ty_str:<15}")

    print(f"\n{'=' * 100}")
    print("  CONSENSUS (forward, D111 direction filter: peak_lag < 0 for xcorr)")
    print(f"{'=' * 100}")
    consensus = []
    for r in pair_results:
        f = r["forward"]
        votes = 0
        methods_sig = []
        if f["naive_xcorr"]["significant"] and f["naive_xcorr"]["peak_lag"] < 0:
            votes += 1; methods_sig.append("naive")
        if f["diff_xcorr"].get("significant_fdr", False) and f["diff_xcorr"]["peak_lag"] < 0:
            votes += 1; methods_sig.append("diff")
        if f["threshold_onset"]["significant"]:
            votes += 1; methods_sig.append("threshold")
        if f["perm_granger"].get("significant_fdr", False):
            votes += 1; methods_sig.append("perm")
        if f["ty_granger"]["significant"]:
            votes += 1; methods_sig.append("ty")
        label = f"{r['canary']}<{r['downstream']}"
        consensus.append({"pair": label, "votes": votes, "methods": methods_sig})
        print(f"  {label:<30} {votes}/5  [{', '.join(methods_sig) if methods_sig else 'none'}]")

    summary = {
        "PermG_fwd": f"{sum(perm_sig_fwd)}/8",
        "PermG_rev": f"{sum(perm_sig_rev)}/8",
        "diff_xcorr_fdr_fwd": f"{sum(diff_sig_fwd)}/8",
        "diff_xcorr_fdr_rev": f"{sum(diff_sig_rev)}/8",
        "naive_xcorr_fwd_D111": f"{sum(1 for r in pair_results if r['forward']['naive_xcorr']['significant'] and r['forward']['naive_xcorr']['peak_lag'] < 0)}/8",
        "threshold_onset_3sigma": f"{sum(1 for r in pair_results if r['forward']['threshold_onset']['significant'])}/8",
        "TY_granger": f"{sum(1 for r in pair_results if r['forward']['ty_granger']['significant'])}/8",
        "K_ge_3": f"{sum(1 for c in consensus if c['votes'] >= 3)}/8",
        "K_ge_4": f"{sum(1 for c in consensus if c['votes'] >= 4)}/8",
        "robust_pairs": f"{sum(1 for c in consensus if c['votes'] >= 3)}/8",
    }

    print(f"\n{'=' * 100}")
    print("  SUMMARY")
    print(f"{'=' * 100}")
    for k, v in summary.items():
        print(f"  {k:<30} {v}")

    print(f"\n{'=' * 100}")
    print("  DRIFT STATISTICS (gen0 -> gen5)")
    print(f"{'=' * 100}")
    g0, gN = data[0], data[-1]
    for metric in ["token_entropy", "ece", "perplexity", "distinct_1", "distinct_2", "distinct_3", "mauve", "effective_rank"]:
        v0, vN = g0[metric], gN[metric]
        drift = (vN - v0) / abs(v0) * 100 if abs(v0) > 1e-12 else float('inf')
        print(f"  {metric:<20} {v0:.4f} -> {vN:.4f}  ({drift:+.2f}%)")

    full_results = {
        "meta": {
            "exp_id": "phase_diagram_t05_a045_s42_fp32",
            "alpha": 0.45,
            "seed": 42,
            "T": 5,
            "n_gens": n_gens,
            "n_perm": N_PERM,
            "canaries": CANARIES,
            "downstreams": DOWNSTREAMS,
            "threshold_criterion": "true_3sigma_d105",
            "D111_direction": "peak_lag < 0 (C009 corrected)",
            "D105_3sigma": "true 3sigma (std of full series)",
            "note": "T=5 only has 6 data points (gen 0-5). Statistical power is reduced compared to T=10 (11 points).",
        },
        "summary": summary,
        "consensus": consensus,
        "pairs": [],
    }

    def clean(obj):
        if isinstance(obj, (np.floating, np.float64)):
            return float(obj)
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, dict):
            return {k: clean(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [clean(v) for v in obj]
        return obj

    for r in pair_results:
        pr = clean(r)
        for d in ["forward", "reverse"]:
            for m in ["naive_xcorr", "diff_xcorr"]:
                if "all_lags" in pr[d][m]:
                    del pr[d][m]["all_lags"]
        full_results["pairs"].append(pr)

    out_path = "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a045_s42_fp32/5method_leadlag.json"
    with open(out_path, "w") as f:
        json.dump(full_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
