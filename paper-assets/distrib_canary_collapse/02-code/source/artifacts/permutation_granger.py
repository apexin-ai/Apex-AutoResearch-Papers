"""Permutation-based Granger causality test.

Uses permutation to build a null distribution of the Granger F-statistic,
avoiding asymptotic assumptions that fail on short series (T<20).
First-differences the series to handle non-stationarity, then uses random
shuffle (not circular shift) since differencing removes autocorrelation.
"""

import numpy as np


def _build_lag_matrix(y, x, max_lag):
    """Build design matrices for restricted and unrestricted Granger models."""
    T = len(y)
    n = T - max_lag
    Y = y[max_lag:]

    cols_r = [np.ones(n)]
    for lag in range(1, max_lag + 1):
        cols_r.append(y[max_lag - lag: T - lag])

    cols_u = list(cols_r)
    for lag in range(1, max_lag + 1):
        cols_u.append(x[max_lag - lag: T - lag])

    X_r = np.column_stack(cols_r)
    X_u = np.column_stack(cols_u)
    return Y, X_r, X_u


def _granger_f_stat(y, x, max_lag):
    """Compute Granger F-statistic: does x help predict y beyond y's own lags?"""
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

    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)
    return F


def permutation_granger_test(x, y, max_lag=1, n_perm=1000, seed=42,
                              difference=True):
    """Permutation-based Granger causality test.

    Tests whether x Granger-causes y using permutation null distribution.
    First-differences series by default to handle non-stationarity, then
    uses random shuffle of x to build the null (differencing removes
    autocorrelation, making shuffle appropriate).

    Args:
        x: 1D array, potential cause
        y: 1D array, potential effect
        max_lag: number of lags in the model
        n_perm: number of permutations for null distribution
        seed: random seed for reproducibility
        difference: if True, first-difference both series before testing

    Returns:
        dict with keys: f_stat, p_value, n_perm, null_mean, null_std,
                        effect_size_f2, significant (p<0.05)
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    assert len(x) == len(y), "x and y must have the same length"

    if difference:
        x = np.diff(x)
        y = np.diff(y)

    T = len(x)
    assert T > max_lag + 2, f"Series too short: T={T}, need > {max_lag + 2}"

    f_obs = _granger_f_stat(y, x, max_lag)

    if np.isnan(f_obs):
        return {
            "f_stat": None, "p_value": None, "n_perm": n_perm,
            "null_mean": None, "null_std": None,
            "effect_size_f2": None, "significant": False,
            "differenced": difference,
            "note": "F-stat computation failed",
        }

    rng = np.random.default_rng(seed)
    null_f = np.empty(n_perm)

    for i in range(n_perm):
        x_perm = rng.permutation(x)
        null_f[i] = _granger_f_stat(y, x_perm, max_lag)

    valid_null = null_f[~np.isnan(null_f)]
    n_valid = len(valid_null)

    if n_valid == 0:
        return {
            "f_stat": round(float(f_obs), 4), "p_value": None,
            "n_perm": n_perm, "null_mean": None, "null_std": None,
            "effect_size_f2": None, "significant": False,
            "differenced": difference,
            "note": "All permutations failed",
        }

    p_value = (np.sum(valid_null >= f_obs) + 1) / (n_valid + 1)

    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)
    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)
    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)
    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None

    return {
        "f_stat": round(float(f_obs), 4),
        "p_value": round(float(p_value), 6),
        "n_perm": n_perm,
        "null_mean": round(float(np.mean(valid_null)), 4),
        "null_std": round(float(np.std(valid_null)), 4),
        "effect_size_f2": round(float(f2), 4) if f2 is not None else None,
        "significant": bool(p_value < 0.05),
        "differenced": difference,
    }


if __name__ == "__main__":
    import json
    import os
    import sys

    data_dir = sys.argv[1] if len(sys.argv) > 1 else "results/mvp"
    seeds = [42, 43, 44, 45]

    POSITIVE = ("token_entropy", "distinct_1")
    NEGATIVE = ("effective_rank", "distinct_1")

    print("=" * 70)
    print("PERMUTATION GRANGER VALIDATION (shuffle + 1st-diff, n_perm=1000)")
    print("=" * 70)

    results = []
    for seed_val in seeds:
        path = os.path.join(data_dir, f"rep_{seed_val}", "all_metrics.json")
        with open(path) as f:
            metrics = json.load(f)
        metrics_sorted = sorted(metrics, key=lambda m: m["generation"])

        for label, (cause_name, effect_name) in [("POSITIVE", POSITIVE),
                                                   ("NEGATIVE", NEGATIVE)]:
            cause = np.array([m[cause_name] for m in metrics_sorted])
            effect = np.array([m[effect_name] for m in metrics_sorted])

            res = permutation_granger_test(cause, effect, max_lag=1,
                                           n_perm=1000, seed=seed_val)
            res["seed"] = seed_val
            res["pair"] = f"{cause_name} -> {effect_name}"
            res["label"] = label
            results.append(res)

            sig = "SIG" if res["significant"] else "n.s."
            f_str = f"F={res['f_stat']:.2f}" if res["f_stat"] else "F=N/A"
            p_str = f"p={res['p_value']:.4f}" if res["p_value"] else "p=N/A"
            f2_str = f"f2={res['effect_size_f2']:.4f}" if res["effect_size_f2"] is not None else "f2=N/A"
            null_str = f"null={res['null_mean']:.2f}±{res['null_std']:.2f}" if res["null_mean"] is not None else ""
            print(f"  seed {seed_val} | {label:>8} | {cause_name:>16} -> {effect_name:<12} "
                  f"| {f_str:>12} | {p_str:>10} | {f2_str:>12} | {null_str:>16} | {sig}")

    print()
    print("CONSISTENCY CHECK")
    print("-" * 70)
    pos_results = [r for r in results if r["label"] == "POSITIVE"]
    neg_results = [r for r in results if r["label"] == "NEGATIVE"]
    pos_all_sig = all(r["significant"] for r in pos_results)
    neg_all_ns = all(not r["significant"] for r in neg_results)
    print(f"  Positive (token_entropy -> distinct_1): "
          f"{'ALL SIG' if pos_all_sig else 'MIXED'} "
          f"({sum(r['significant'] for r in pos_results)}/4)")
    print(f"  Negative (effective_rank -> distinct_1): "
          f"{'ALL n.s.' if neg_all_ns else 'MIXED'} "
          f"({sum(not r['significant'] for r in neg_results)}/4)")
    print(f"\n  VALIDATION: {'PASSED' if pos_all_sig and neg_all_ns else 'FAILED'}")
