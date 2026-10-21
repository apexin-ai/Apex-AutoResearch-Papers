"""Batch 6-pair D102 analysis for 1.4B s42 experiments.
Runs 5-method lead-lag on 6 pairs (2 canaries x 3 distinct, mauve excluded).
"""
import json, os, sys, argparse
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.vector_ar.var_model import VAR

N_PERM = 5000
ALPHA_SIG = 0.05
CANARIES = ["token_entropy", "ece"]
DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3"]
HIGHER_IS_WORSE = {"ece"}
LOWER_IS_WORSE = {"token_entropy", "distinct_1", "distinct_2", "distinct_3"}


def load_metrics(results_dir, end_gen):
    data = []
    for g in range(end_gen + 1):
        path = os.path.join(results_dir, f"gen_{g}", "metrics.json")
        if not os.path.exists(path):
            print(f"WARNING: {path} missing, stopping at gen_{g-1}")
            break
        with open(path) as f:
            m = json.load(f)
        data.append(m)
    return sorted(data, key=lambda x: x["generation"])


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
    final = np.empty(m)
    final[sorted_idx] = np.minimum(adj_sorted, 1.0)
    adjusted[idx] = final
    sig = [bool(adjusted[i] < alpha) if valid[i] else False for i in range(n)]
    return adjusted.tolist(), sig


def naive_xcorr(canary, downstream, max_lag=3):
    c = np.asarray(canary, dtype=float)
    d = np.asarray(downstream, dtype=float)
    c = (c - c.mean()) / (c.std() + 1e-12)
    d = (d - d.mean()) / (d.std() + 1e-12)
    n = len(c)
    best_lag, best_r = 0, 0.0
    for lag in range(-max_lag, max_lag + 1):
        if lag < 0:
            cc = c[-lag:]
            dd = d[:lag]
        elif lag > 0:
            cc = c[:-lag]
            dd = d[lag:]
        else:
            cc, dd = c, d
        if len(cc) < 4:
            continue
        r = np.corrcoef(cc, dd)[0, 1]
        if abs(r) > abs(best_r):
            best_r = r
            best_lag = lag
    return {
        "peak_lag": int(best_lag),
        "peak_r": round(float(best_r), 4),
        "significant": abs(best_r) > 0.5 and best_lag != 0,
    }


def diff_xcorr(canary, downstream, max_lag=3, n_perm=1000, seed=42):
    c = np.diff(np.asarray(canary, dtype=float))
    d = np.diff(np.asarray(downstream, dtype=float))
    c = (c - c.mean()) / (c.std() + 1e-12)
    d = (d - d.mean()) / (d.std() + 1e-12)
    n = len(c)
    best_lag, best_r = 0, 0.0
    for lag in range(-max_lag, max_lag + 1):
        if lag < 0:
            cc = c[-lag:]
            dd = d[:lag]
        elif lag > 0:
            cc = c[:-lag]
            dd = d[lag:]
        else:
            cc, dd = c, d
        if len(cc) < 4:
            continue
        r = np.corrcoef(cc, dd)[0, 1]
        if abs(r) > abs(best_r):
            best_r = r
            best_lag = lag
    rng = np.random.default_rng(seed)
    null_r = np.empty(n_perm)
    for i in range(n_perm):
        c_perm = rng.permutation(c)
        br = 0.0
        for lag in range(-max_lag, max_lag + 1):
            if lag < 0:
                cc = c_perm[-lag:]
                dd = d[:lag]
            elif lag > 0:
                cc = c_perm[:-lag]
                dd = d[lag:]
            else:
                cc, dd = c_perm, d
            if len(cc) < 4:
                continue
            r = np.corrcoef(cc, dd)[0, 1]
            if abs(r) > abs(br):
                br = r
        null_r[i] = br
    p_value = (np.sum(np.abs(null_r) >= abs(best_r)) + 1) / (n_perm + 1)
    return {
        "peak_lag": int(best_lag),
        "peak_r": round(float(best_r), 4),
        "p_value": round(float(p_value), 6),
        "significant": bool(p_value < 0.05),
    }


def threshold_onset(canary_series, downstream_series, canary_name, downstream_name,
                    all_data, threshold_criterion="true_3sigma_d105"):
    c = np.asarray(canary_series, dtype=float)
    d = np.asarray(downstream_series, dtype=float)
    n = len(c)

    def find_onset(series, name):
        baseline = series[0]
        std_0 = abs(baseline) * 0.01 if abs(baseline) > 1e-12 else 0.01
        if n >= 3:
            std_0 = np.std(series[:3]) if np.std(series[:3]) > 1e-12 else std_0
        threshold = 3 * std_0
        for i in range(1, n):
            if abs(series[i] - baseline) > threshold:
                return i
        return n

    c_onset = find_onset(orient(c, canary_name), canary_name)
    d_onset = find_onset(orient(d, downstream_name), downstream_name)

    return {
        "canary_onset": int(c_onset),
        "downstream_onset": int(d_onset),
        "lead": int(d_onset - c_onset),
        "significant": c_onset < d_onset,
    }


def ty_granger(canary, downstream, max_lag=1):
    import warnings
    warnings.filterwarnings("ignore")
    c = np.asarray(canary, dtype=float)
    d = np.asarray(downstream, dtype=float)

    def adf_order(series, max_d=2):
        for d_val in range(max_d + 1):
            s = series.copy()
            for _ in range(d_val):
                s = np.diff(s)
            if len(s) < 6:
                return d_val
            try:
                result = adfuller(s, maxlag=1, regression='c')
                if result[1] < 0.10:
                    return d_val
            except:
                pass
        return max_d

    d_c = adf_order(c)
    d_d = adf_order(d)
    d_max = max(d_c, d_d)

    p = max_lag
    k = p + d_max
    T = len(c)
    min_obs = k + 3

    if T < min_obs:
        return {
            "significant": False,
            "p_value": None,
            "f_stat": None,
            "d_max": int(d_max),
            "note": f"T={T} too small for TY (need {min_obs})"
        }

    try:
        import pandas as pd
        df = pd.DataFrame({"c": c, "d": d})
        model = VAR(df)
        fitted = model.fit(k)
        test = fitted.test_causality(caused="d", causing="c", kind='f')
        return {
            "significant": bool(test.pvalue < 0.05),
            "p_value": round(float(test.pvalue), 6),
            "f_stat": round(float(test.test_statistic), 4),
            "d_max": int(d_max),
            "df_resid": int(T - 2 * k - 1),
        }
    except Exception as e:
        return {
            "significant": False,
            "p_value": None,
            "f_stat": None,
            "d_max": int(d_max),
            "note": str(e)[:80]
        }


def analyze_experiment(exp_dir, alpha, seed, T, output_path):
    end_gen = T
    data = load_metrics(exp_dir, end_gen)
    n_gens = len(data)
    print(f"Loaded {n_gens} generations from {exp_dir}")

    pair_results = []
    perm_fwd_pvals = []
    perm_rev_pvals = []
    diff_fwd_pvals = []
    diff_rev_pvals = []

    for canary in CANARIES:
        c_series = [d[canary] for d in data]
        for ds in DOWNSTREAMS:
            d_series = [d[ds] for d in data]
            c_oriented = orient(np.array(c_series), canary)
            d_oriented = orient(np.array(d_series), ds)

            r_naive = naive_xcorr(c_oriented, d_oriented)
            r_diff = diff_xcorr(c_oriented, d_oriented, n_perm=N_PERM, seed=42)
            r_onset = threshold_onset(c_series, d_series, canary, ds, data)
            r_perm_fwd = permutation_granger_test(c_oriented, d_oriented,
                                                   max_lag=1, n_perm=N_PERM, seed=42)
            r_perm_rev = permutation_granger_test(d_oriented, c_oriented,
                                                   max_lag=1, n_perm=N_PERM, seed=42)
            r_ty = ty_granger(c_series, d_series)

            diff_rev = diff_xcorr(d_oriented, c_oriented, n_perm=N_PERM, seed=42)

            perm_fwd_pvals.append(r_perm_fwd.get("p_value"))
            perm_rev_pvals.append(r_perm_rev.get("p_value"))
            diff_fwd_pvals.append(r_diff.get("p_value"))
            diff_rev_pvals.append(diff_rev.get("p_value"))

            pair_results.append({
                "canary": canary,
                "downstream": ds,
                "forward": {
                    "naive_xcorr": r_naive,
                    "diff_xcorr": r_diff,
                    "threshold_onset": r_onset,
                    "perm_granger": r_perm_fwd,
                    "ty_granger": r_ty,
                },
                "reverse": {
                    "perm_granger": r_perm_rev,
                    "diff_xcorr": diff_rev,
                },
            })

    # BH FDR correction
    _, perm_fwd_sig = bh_fdr(perm_fwd_pvals)
    _, perm_rev_sig = bh_fdr(perm_rev_pvals)
    _, diff_fwd_sig = bh_fdr(diff_fwd_pvals)
    _, diff_rev_sig = bh_fdr(diff_rev_pvals)

    for i, r in enumerate(pair_results):
        r["forward"]["perm_granger"]["significant_fdr"] = perm_fwd_sig[i]
        r["reverse"]["perm_granger"]["significant_fdr"] = perm_rev_sig[i]
        r["forward"]["diff_xcorr"]["significant_fdr"] = diff_fwd_sig[i]
        r["reverse"]["diff_xcorr"]["significant_fdr"] = diff_rev_sig[i]

    # Consensus (D111: peak_lag < 0 for xcorr, C009)
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

    # Metrics trajectory
    metrics_trajectory = {}
    for d in data:
        g = d["generation"]
        metrics_trajectory[f"gen_{g}"] = {
            "token_entropy": round(d.get("token_entropy", 0), 4),
            "ece": round(d.get("ece", 0), 4),
            "distinct_1": round(d.get("distinct_1", 0), 4),
            "distinct_2": round(d.get("distinct_2", 0), 4),
            "distinct_3": round(d.get("distinct_3", 0), 4),
            "perplexity": round(d.get("perplexity", 0), 2),
            "mauve": None,
        }

    rel_dir = exp_dir.replace("/root/autodl-tmp/distrib_canary_collapse/", "")

    result = {
        "meta": {
            "alpha": alpha,
            "seed": seed,
            "T": T,
            "n_gens": n_gens,
            "data_dir": rel_dir,
            "methods": ["naive_xcorr", "diff_xcorr", "threshold_onset", "perm_granger", "ty_granger"],
            "n_perm": N_PERM,
            "canaries": CANARIES,
            "downstreams": DOWNSTREAMS,
            "threshold_criterion": "true_3sigma_d105",
            "note": "6-pair (distinct_1/2/3 only, mauve excluded)"
        },
        "summary": {
            "perm_granger_fdr_forward_sig": sum(perm_fwd_sig),
            "perm_granger_fdr_reverse_sig": sum(perm_rev_sig),
            "robust_pairs": sum(1 for c in consensus if c["votes"] >= 3),
            "total_pairs": 6
        },
        "consensus": consensus,
        "metrics_trajectory": metrics_trajectory,
    }

    def clean(obj):
        if isinstance(obj, (np.floating, np.float64)): return float(obj)
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, np.bool_): return bool(obj)
        if isinstance(obj, dict): return {k: clean(v) for k, v in obj.items()}
        if isinstance(obj, list): return [clean(v) for v in obj]
        return obj

    result = clean(result)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Saved: {output_path}")

    # Print summary
    print(f"\n=== {os.path.basename(exp_dir)} ===")
    print(f"  PermG fwd: {sum(perm_fwd_sig)}/6, rev: {sum(perm_rev_sig)}/6")
    print(f"  Robust >=3/5: {sum(1 for c in consensus if c['votes'] >= 3)}/6")
    for c in consensus:
        print(f"  {c['pair']:<30} {c['votes']}/5  [{', '.join(c['methods'])}]")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp-dir", required=True)
    parser.add_argument("--alpha", type=float, required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--T", type=int, required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    analyze_experiment(args.exp_dir, args.alpha, args.seed, args.T, args.output)
