"""
J2 Fix: First-differencing power loss simulation.
Compare raw-levels Granger, first-differenced Granger, and permutation Granger
at T=11 (matching our experimental generation count).
"""
import json
import time
import numpy as np
from statsmodels.tsa.api import VAR

# ── Empirical data from a050_s42_fp32 ──
EMPIRICAL_ENTROPY = [3.234195, 2.513126, 2.510962, 2.581628, 2.588291,
                     2.585607, 2.607992, 2.656354, 2.660300, 2.672412, 2.707494]
EMPIRICAL_PPL = [26.948959, 23.363054, 26.685837, 27.597102, 28.710176,
                 29.732531, 29.886785, 30.060055, 31.024042, 31.447773, 31.461816]


def estimate_empirical_dgp():
    X = np.array(EMPIRICAL_ENTROPY)
    Y = np.array(EMPIRICAL_PPL)
    X_z = (X - X.mean()) / X.std()
    Y_z = (Y - Y.mean()) / Y.std()

    xcorr_lag1 = np.corrcoef(X_z[:-1], Y_z[1:])[0, 1]

    from numpy.linalg import lstsq
    # Y_t = a*Y_{t-1} + beta*X_{t-1} + eps
    dep = Y_z[1:]
    reg_full = np.column_stack([Y_z[:-1], X_z[:-1]])
    reg_restricted = Y_z[:-1].reshape(-1, 1)

    coefs_full, res_full, _, _ = lstsq(reg_full, dep, rcond=None)
    coefs_rest, res_rest, _, _ = lstsq(reg_restricted, dep, rcond=None)

    beta_hat = coefs_full[1]

    ss_full = np.sum((dep - reg_full @ coefs_full) ** 2)
    ss_rest = np.sum((dep - reg_restricted @ coefs_rest) ** 2)

    n = len(dep)
    df_num = 1
    df_den = n - reg_full.shape[1]
    f_stat = ((ss_rest - ss_full) / df_num) / (ss_full / df_den) if df_den > 0 else 0
    f2 = (ss_rest - ss_full) / ss_full if ss_full > 0 else 0

    return {
        "xcorr_lag1": round(float(xcorr_lag1), 4),
        "beta_hat_standardized": round(float(beta_hat), 4),
        "f_statistic": round(float(f_stat), 4),
        "cohens_f2": round(float(f2), 4),
    }


def run_granger_var(data, maxlags=1):
    try:
        model = VAR(data)
        fitted = model.fit(maxlags=maxlags, trend='c')
        result = fitted.test_causality(causing=1, caused=0, kind='f')
        return result.pvalue, result.test_statistic
    except Exception:
        return None, None


def simulation(T, beta, n_reps, n_perms, seed=42):
    rng = np.random.default_rng(seed)
    counts = {"raw": 0, "diff": 0, "perm": 0}
    burn = 50

    for rep in range(n_reps):
        e1 = rng.normal(0, 1, T + burn)
        e2 = rng.normal(0, 1, T + burn)
        X = np.zeros(T + burn)
        Y = np.zeros(T + burn)
        for t in range(1, T + burn):
            X[t] = 0.5 * X[t - 1] + e1[t]
            Y[t] = 0.5 * Y[t - 1] + beta * X[t - 1] + e2[t]
        X = X[burn:]
        Y = Y[burn:]

        # Raw levels
        p_raw, _ = run_granger_var(np.column_stack([Y, X]))
        if p_raw is not None and p_raw < 0.05:
            counts["raw"] += 1

        # First-differenced
        dX = np.diff(X)
        dY = np.diff(Y)
        p_diff, _ = run_granger_var(np.column_stack([dY, dX]))
        if p_diff is not None and p_diff < 0.05:
            counts["diff"] += 1

        # Permutation Granger
        p_raw_stat_val, stat_val = run_granger_var(np.column_stack([Y, X]))
        if stat_val is not None:
            perm_exceed = 0
            for _ in range(n_perms):
                X_perm = rng.permutation(X)
                _, perm_stat = run_granger_var(np.column_stack([Y, X_perm]))
                if perm_stat is not None and perm_stat >= stat_val:
                    perm_exceed += 1
            perm_p = perm_exceed / n_perms
            if perm_p < 0.05:
                counts["perm"] += 1

    return {k: v / n_reps for k, v in counts.items()}


def main():
    T = 11
    n_reps = 1000
    n_perms = 200

    effects = {
        "small":  {"beta": 0.1, "f2_approx": 0.02},
        "medium": {"beta": 0.3, "f2_approx": 0.15},
        "large":  {"beta": 0.6, "f2_approx": 0.35},
    }

    print(f"=== J2 First-Differencing Simulation ===")
    print(f"T={T}, n_reps={n_reps}, n_perms={n_perms}")
    print()

    empirical = estimate_empirical_dgp()
    print(f"Empirical DGP (a050_s42_fp32): {json.dumps(empirical, indent=2)}")
    print()

    results = {}
    total_start = time.time()

    for name, cfg in effects.items():
        beta = cfg["beta"]
        print(f"Running {name} (beta={beta})...", flush=True)
        t0 = time.time()
        power = simulation(T, beta, n_reps, n_perms, seed=42)
        elapsed = time.time() - t0

        diff_loss = ((power["raw"] - power["diff"]) / power["raw"] * 100) if power["raw"] > 0 else float("nan")
        perm_vs_raw = (power["perm"] / power["raw"] * 100) if power["raw"] > 0 else float("nan")

        results[name] = {
            "beta": beta,
            "raw_power": round(power["raw"], 4),
            "diff_power": round(power["diff"], 4),
            "perm_power": round(power["perm"], 4),
            "diff_loss_pct": f"{diff_loss:.1f}%",
            "perm_retention_pct": f"{perm_vs_raw:.1f}%",
        }
        print(f"  raw={power['raw']:.3f}  diff={power['diff']:.3f}  perm={power['perm']:.3f}  "
              f"diff_loss={diff_loss:.1f}%  [{elapsed:.1f}s]")

    total_elapsed = time.time() - total_start
    print(f"\nTotal time: {total_elapsed:.0f}s")

    # Conclusion
    diff_losses = [
        float(results[k]["diff_loss_pct"].rstrip("%"))
        for k in results if not np.isnan(float(results[k]["diff_loss_pct"].rstrip("%")))
    ]
    avg_diff_loss = np.mean(diff_losses) if diff_losses else 0

    perm_rets = [
        float(results[k]["perm_retention_pct"].rstrip("%"))
        for k in results if not np.isnan(float(results[k]["perm_retention_pct"].rstrip("%")))
    ]
    avg_perm_ret = np.mean(perm_rets) if perm_rets else 0

    conclusion = (
        f"First-differencing loses {avg_diff_loss:.0f}% power on average relative to raw levels at T={T}. "
        f"Permutation Granger retains {avg_perm_ret:.0f}% of raw-levels power without differencing requirement."
    )

    output = {
        "dgp": {
            "T": T,
            "ar_coef": 0.5,
            "n_reps": n_reps,
            "n_perms_for_perm_test": n_perms,
            "burn_in": 50,
        },
        "results": results,
        "empirical_effect_size": {
            "source": "a050_s42_fp32 token_entropy→perplexity",
            **empirical,
        },
        "conclusion": conclusion,
        "elapsed_seconds": round(total_elapsed, 1),
    }

    out_path = "/root/autodl-tmp/distrib_canary_collapse/artifacts/j2_first_diff_power_simulation.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {out_path}")
    print(f"\nConclusion: {conclusion}")


if __name__ == "__main__":
    main()
