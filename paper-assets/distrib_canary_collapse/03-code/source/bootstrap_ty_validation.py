"""Monte Carlo validation of Toda-Yamamoto Granger causality test under short T.

Estimates Type I error rate (under H0: independent AR(1) processes) and
statistical power (under H1: VAR(2) with unidirectional causality) for
TY Granger tests at T ∈ {10, 15, 20, 30} and d_max ∈ {0, 1, adaptive}.

Motivated by reviewer concern that T=10 (11 observations) may be too short
for reliable TY inference in the distrib_canary_collapse project.
"""

import json
import os
import warnings
from itertools import product

import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller

warnings.filterwarnings("ignore")

ALPHA = 0.05
N_SIM = 1000
T_VALUES = [10, 15, 20, 30]
DMAX_OPTIONS = [0, 1, "adaptive"]
SEED_BASE = 20260514


def _adf_order(series, max_d=2):
    """Determine integration order via sequential ADF tests."""
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


def generate_h0(T, phi=0.8, sigma=0.1, rng=None):
    """H0 DGP: two independent AR(1) processes."""
    if rng is None:
        rng = np.random.default_rng()
    n = T + 1
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = rng.normal(0, sigma / np.sqrt(1 - phi**2))
    y[0] = rng.normal(0, sigma / np.sqrt(1 - phi**2))
    for t in range(1, n):
        x[t] = phi * x[t - 1] + rng.normal(0, sigma)
        y[t] = phi * y[t - 1] + rng.normal(0, sigma)
    return x, y


def generate_h1(T, phi=0.8, beta_cause=0.3, sigma=0.1, rng=None):
    """H1 DGP: VAR(2) with x -> y at lag 1, no reverse causality."""
    if rng is None:
        rng = np.random.default_rng()
    n = T + 1
    burn = 50
    total = n + burn
    x = np.zeros(total)
    y = np.zeros(total)
    x[0] = rng.normal(0, sigma)
    y[0] = rng.normal(0, sigma)
    if total > 1:
        x[1] = phi * x[0] + rng.normal(0, sigma)
        y[1] = phi * y[0] + rng.normal(0, sigma)
    for t in range(2, total):
        x[t] = phi * x[t - 1] + rng.normal(0, sigma)
        y[t] = phi * y[t - 1] + beta_cause * x[t - 1] + rng.normal(0, sigma)
    return x[burn:], y[burn:]


def ty_test(x, y, p=1, d_max_setting=1):
    """Run TY Granger causality test (x -> y direction).

    Returns p-value or None if test is infeasible.
    """
    n = len(x)

    if d_max_setting == "adaptive":
        dc = _adf_order(x)
        dd = _adf_order(y)
        d_max = max(dc, dd)
    else:
        d_max = int(d_max_setting)

    k = p + d_max
    T_eff = n - k
    n_params = 1 + 2 * k
    df_resid = T_eff - n_params

    if df_resid < 1:
        return None

    Y = y[k:]
    X_cols = [np.ones(T_eff)]
    for l in range(1, k + 1):
        X_cols.append(x[k - l : n - l])
        X_cols.append(y[k - l : n - l])
    X = np.column_stack(X_cols)

    try:
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        resid = Y - X @ beta
        sigma2 = np.sum(resid**2) / df_resid
        XtX_inv = np.linalg.inv(X.T @ X)
    except Exception:
        return None

    test_idx = [2 * (l - 1) + 1 for l in range(1, p + 1)]
    R = np.zeros((p, n_params))
    for i, idx in enumerate(test_idx):
        R[i, idx] = 1.0

    Rb = R @ beta
    try:
        cov_Rb = sigma2 * (R @ XtX_inv @ R.T)
        W = float(Rb @ np.linalg.inv(cov_Rb) @ Rb)
        F = W / p
        pval = float(1.0 - stats.f.cdf(F, p, df_resid))
    except Exception:
        return None

    return pval


def wilson_ci(k, n, z=1.96):
    """Wilson score 95% CI for a proportion."""
    p_hat = k / n
    denom = 1 + z**2 / n
    center = (p_hat + z**2 / (2 * n)) / denom
    margin = z * np.sqrt((p_hat * (1 - p_hat) + z**2 / (4 * n)) / n) / denom
    return [round(max(0, center - margin), 4), round(min(1, center + margin), 4)]


def run_simulation(n_sim=N_SIM):
    results = {}

    for T in T_VALUES:
        results[T] = {}
        for d_max_setting in DMAX_OPTIONS:
            d_key = str(d_max_setting)

            reject_h0 = 0
            reject_h1 = 0
            feasible_h0 = 0
            feasible_h1 = 0

            for i in range(n_sim):
                rng0 = np.random.default_rng(SEED_BASE + i)
                rng1 = np.random.default_rng(SEED_BASE + n_sim + i)

                x0, y0 = generate_h0(T, rng=rng0)
                pval0 = ty_test(x0, y0, p=1, d_max_setting=d_max_setting)
                if pval0 is not None:
                    feasible_h0 += 1
                    if pval0 < ALPHA:
                        reject_h0 += 1

                x1, y1 = generate_h1(T, rng=rng1)
                pval1 = ty_test(x1, y1, p=1, d_max_setting=d_max_setting)
                if pval1 is not None:
                    feasible_h1 += 1
                    if pval1 < ALPHA:
                        reject_h1 += 1

            type1 = reject_h0 / feasible_h0 if feasible_h0 > 0 else None
            power = reject_h1 / feasible_h1 if feasible_h1 > 0 else None

            results[T][d_key] = {
                "type1_error": round(type1, 4) if type1 is not None else None,
                "power": round(power, 4) if power is not None else None,
                "n_sim": n_sim,
                "feasible_h0": feasible_h0,
                "feasible_h1": feasible_h1,
                "infeasible_h0": n_sim - feasible_h0,
                "infeasible_h1": n_sim - feasible_h1,
                "ci_95_type1": wilson_ci(reject_h0, feasible_h0) if feasible_h0 > 0 else None,
                "ci_95_power": wilson_ci(reject_h1, feasible_h1) if feasible_h1 > 0 else None,
            }

            print(
                f"T={T:>2}, d_max={d_key:>8}: "
                f"Type I={type1:.4f} [{results[T][d_key]['ci_95_type1'][0]:.3f},{results[T][d_key]['ci_95_type1'][1]:.3f}], "
                f"Power={power:.4f} [{results[T][d_key]['ci_95_power'][0]:.3f},{results[T][d_key]['ci_95_power'][1]:.3f}], "
                f"infeasible=({n_sim - feasible_h0},{n_sim - feasible_h1})"
                if type1 is not None and power is not None
                else f"T={T:>2}, d_max={d_key:>8}: ALL INFEASIBLE"
            )

    return results


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n_sim", type=int, default=N_SIM)
    parser.add_argument(
        "--output",
        default="results/bootstrap_ty_results.json",
    )
    args = parser.parse_args()

    global N_SIM
    N_SIM = args.n_sim

    print(f"Running TY power analysis: N_sim={args.n_sim}, T={T_VALUES}, d_max={DMAX_OPTIONS}")
    print("=" * 80)

    results = run_simulation(args.n_sim)

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)

    print("=" * 80)
    print(f"Results saved to {args.output}")

    # Summary diagnostics
    print("\n=== DIAGNOSTIC SUMMARY ===")
    for T in T_VALUES:
        for d_key in [str(d) for d in DMAX_OPTIONS]:
            r = results[T][d_key]
            if r["type1_error"] is None:
                print(f"T={T}, d_max={d_key}: INFEASIBLE")
                continue
            flags = []
            if r["type1_error"] > 0.10:
                flags.append("TYPE_I_INFLATED")
            elif r["type1_error"] > 0.075:
                flags.append("TYPE_I_BORDERLINE")
            if r["power"] < 0.50:
                flags.append("LOW_POWER")
            elif r["power"] < 0.80:
                flags.append("MODERATE_POWER")
            status = ", ".join(flags) if flags else "OK"
            print(f"T={T}, d_max={d_key}: Type I={r['type1_error']:.3f}, Power={r['power']:.3f} -> {status}")

    # d_max sensitivity
    print("\n=== d_max SENSITIVITY ===")
    for T in T_VALUES:
        vals = {d: results[T][str(d)] for d in DMAX_OPTIONS}
        type1s = [v["type1_error"] for v in vals.values() if v["type1_error"] is not None]
        powers = [v["power"] for v in vals.values() if v["power"] is not None]
        if type1s:
            t1_range = max(type1s) - min(type1s)
            pw_range = max(powers) - min(powers) if powers else 0
            sensitive = "SENSITIVE" if t1_range > 0.15 or pw_range > 0.15 else "stable"
            print(f"T={T}: Type I range={t1_range:.3f}, Power range={pw_range:.3f} -> {sensitive}")


if __name__ == "__main__":
    main()
