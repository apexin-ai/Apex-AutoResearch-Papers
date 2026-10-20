"""5-method lead-lag analysis for phase_diagram_t20_a075_s43_fp32.
T=20 generations, alpha=0.75, seed=43, fp32, Pythia-410m.
Cross-seed validation of t20_a075_s42_fp32.
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
  {"token_entropy": 3.23419483150593, "ece": 0.010804557477709054, "distinct_1": 0.09826975532304685, "distinct_2": 0.5146237399644992, "distinct_3": 0.8139529202934542, "mauve": 0.0314907126188509, "generation": 0, "effective_alpha": 0.75},
  {"token_entropy": 2.165255432472167, "ece": 0.13772681489225452, "distinct_1": 0.09663940689677597, "distinct_2": 0.5111736157967044, "distinct_3": 0.8110021786492375, "mauve": 0.03125231646418338, "generation": 1, "effective_alpha": 0.75},
  {"token_entropy": 2.1199712530123915, "ece": 0.17350539030187168, "distinct_1": 0.0839921875, "distinct_2": 0.4392221814232924, "distinct_3": 0.7262066594790544, "mauve": 0.030269643819352383, "generation": 2, "effective_alpha": 0.75},
  {"token_entropy": 2.0905788794508595, "ece": 0.18813730625897196, "distinct_1": 0.0777734375, "distinct_2": 0.3956202782834241, "distinct_3": 0.6638150596103064, "mauve": 0.029847105765446184, "generation": 3, "effective_alpha": 0.75},
  {"token_entropy": 2.1370965882762563, "ece": 0.19135050120984004, "distinct_1": 0.07478125, "distinct_2": 0.3693075727154118, "distinct_3": 0.6170643291301426, "mauve": 0.031292905516543165, "generation": 4, "effective_alpha": 0.75},
  {"token_entropy": 2.147404683718436, "ece": 0.19867218743440174, "distinct_1": 0.07375, "distinct_2": 0.3578934210423519, "distinct_3": 0.595829622337849, "mauve": 0.03259267733156405, "generation": 5, "effective_alpha": 0.75},
  {"token_entropy": 2.1484669928184306, "ece": 0.20798230462519454, "distinct_1": 0.0733203125, "distinct_2": 0.35401057820764226, "distinct_3": 0.5888451382052845, "mauve": 0.028503338843974338, "generation": 6, "effective_alpha": 0.75},
  {"token_entropy": 2.160765342380653, "ece": 0.2161769904378178, "distinct_1": 0.072984375, "distinct_2": 0.3505730513519637, "distinct_3": 0.5820637822465976, "mauve": 0.030462700755256283, "generation": 7, "effective_alpha": 0.75},
  {"token_entropy": 2.2231368606222865, "ece": 0.21321299583212813, "distinct_1": 0.07296875, "distinct_2": 0.3495574184173314, "distinct_3": 0.5797903092235817, "mauve": 0.031636537786991395, "generation": 8, "effective_alpha": 0.75},
  {"token_entropy": 2.248839528298156, "ece": 0.21481752034347956, "distinct_1": 0.072796875, "distinct_2": 0.3477917796232783, "distinct_3": 0.5762199409365771, "mauve": 0.03241155919353214, "generation": 9, "effective_alpha": 0.75},
  {"token_entropy": 2.286704584874, "ece": 0.2132208430544018, "distinct_1": 0.07259375, "distinct_2": 0.34652614473550575, "distinct_3": 0.5739230300473445, "mauve": 0.031888971779399714, "generation": 10, "effective_alpha": 0.75},
  {"token_entropy": 2.3087121197913807, "ece": 0.21368265621238822, "distinct_1": 0.072453125, "distinct_2": 0.34579957655919186, "distinct_3": 0.5723605056329005, "mauve": 0.03220931740809482, "generation": 11, "effective_alpha": 0.75},
  {"token_entropy": 2.3394903870708923, "ece": 0.2129255979266479, "distinct_1": 0.07234375, "distinct_2": 0.3450495706997711, "distinct_3": 0.5700792199878123, "mauve": 0.03225044927399488, "generation": 12, "effective_alpha": 0.75},
  {"token_entropy": 2.3331425466320583, "ece": 0.216888487729628, "distinct_1": 0.07234375, "distinct_2": 0.3445105039883124, "distinct_3": 0.5685557586837294, "mauve": 0.03239000432486919, "generation": 13, "effective_alpha": 0.75},
  {"token_entropy": 2.3896542109827235, "ece": 0.21299382661984395, "distinct_1": 0.072296875, "distinct_2": 0.3442058141079227, "distinct_3": 0.5677744964765075, "mauve": 0.03388049974153197, "generation": 14, "effective_alpha": 0.75},
  {"token_entropy": 2.40308750786051, "ece": 0.21516025604172298, "distinct_1": 0.072171875, "distinct_2": 0.3436745599574997, "distinct_3": 0.5672666760418131, "mauve": 0.033807538990171734, "generation": 15, "effective_alpha": 0.75},
  {"token_entropy": 2.4295791618022955, "ece": 0.2146086324214194, "distinct_1": 0.072125, "distinct_2": 0.3432292439784686, "distinct_3": 0.56637603712558, "mauve": 0.032381311568781504, "generation": 16, "effective_alpha": 0.75},
  {"token_entropy": 2.440831776747916, "ece": 0.21580805934466668, "distinct_1": 0.0720546875, "distinct_2": 0.342432362752834, "distinct_3": 0.5650244535070861, "mauve": 0.03223503225223609, "generation": 17, "effective_alpha": 0.75},
  {"token_entropy": 2.4294725499562984, "ece": 0.21707609304930606, "distinct_1": 0.0720390625, "distinct_2": 0.3421511105555512, "distinct_3": 0.564344755386803, "mauve": 0.03313301287753493, "generation": 18, "effective_alpha": 0.75},
  {"token_entropy": 2.445365365544241, "ece": 0.2180182052221425, "distinct_1": 0.0719921875, "distinct_2": 0.3421745482386581, "distinct_3": 0.5642744417881529, "mauve": 0.03330702087627517, "generation": 19, "effective_alpha": 0.75},
  {"token_entropy": 2.4709035693358037, "ece": 0.2177405333793532, "distinct_1": 0.0720234375, "distinct_2": 0.34242455019179835, "distinct_3": 0.5647197612462694, "mauve": 0.033075960466098134, "generation": 20, "effective_alpha": 0.75},
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


def permutation_granger_test(x, y, max_lag=1, n_perm=1000, seed=43, difference=True):
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
    seed = 43

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
    print("5-METHOD LEAD-LAG ANALYSIS | T=20 | alpha=0.75 | seed=43 | phase_diagram_t20_a075_s43_fp32")
    print("=" * 100)
    print(f"Loaded {n_gens} generations (T=20, 21 data points)\n")

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
            diff_str = f"lag={d['diff_xcorr']['peak_lag']} r={d['diff_xcorr']['r']:.3f} {'*' if d['diff_xcorr'].get('significant_fdr', False) else ''}" if diff_p is not None else "N/A"
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
    print("  DRIFT STATISTICS (gen0 -> gen20)")
    print(f"{'=' * 100}")
    g0, gN = data[0], data[-1]
    for metric in ["token_entropy", "ece", "perplexity", "distinct_1", "distinct_2", "distinct_3", "mauve", "effective_rank"]:
        if metric in g0 and metric in gN:
            v0, vN = g0[metric], gN[metric]
            drift = (vN - v0) / abs(v0) * 100 if abs(v0) > 1e-12 else float('inf')
            print(f"  {metric:<20} {v0:.4f} -> {vN:.4f}  ({drift:+.2f}%)")

    full_results = {
        "meta": {
            "exp_id": "phase_diagram_t20_a075_s43_fp32",
            "alpha": 0.75,
            "seed": 43,
            "T": 20,
            "n_gens": n_gens,
            "n_perm": N_PERM,
            "canaries": CANARIES,
            "downstreams": DOWNSTREAMS,
            "threshold_criterion": "true_3sigma_d105",
            "D111_direction": "peak_lag < 0 (C009 corrected)",
            "D105_3sigma": "true 3sigma (std of full series)",
            "cross_seed_parent": "t20_a075_s42_fp32",
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

    out_path = "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t20_a075_s43_fp32/data/5method_leadlag.json"
    with open(out_path, "w") as f:
        json.dump(full_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
