#!/usr/bin/env python3
"""PermG Power Analysis: Monte Carlo simulation for permutation Granger causality.

Generates power curves across signal strength (beta) and series length (T).
Matches the project's PermG implementation: first-difference, random shuffle,
F-stat, BH FDR correction.

Two power metrics:
  - raw:  P(p < 0.05) per replication (single-pair, no multiplicity)
  - fdr8: P(detected after BH FDR across 8 pairs: 1 signal + 7 null)
          Matches the project pipeline (8 bidirectional metric pairs).
"""

import json
import sys
import time
import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed


# ---------------------------------------------------------------------------
# Core PermG (matches project implementation)
# ---------------------------------------------------------------------------

def _granger_f_stat(y, x, max_lag=1):
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

    try:
        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]
        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]
    except np.linalg.LinAlgError:
        return np.nan

    rss_r = np.sum((Y - X_r @ beta_r) ** 2)
    rss_u = np.sum((Y - X_u @ beta_u) ** 2)

    q = max_lag
    df_resid = n - X_u.shape[1]

    if df_resid <= 0 or rss_u < 1e-15:
        return np.nan

    return ((rss_r - rss_u) / q) / (rss_u / df_resid)


def permutation_granger_pvalue(x, y, max_lag=1, n_perm=5000, rng=None):
    """Empirical p-value from permutation Granger test (with first-differencing)."""
    x = np.diff(np.asarray(x, dtype=np.float64))
    y = np.diff(np.asarray(y, dtype=np.float64))

    if len(x) <= max_lag + 2:
        return np.nan

    f_obs = _granger_f_stat(y, x, max_lag)
    if np.isnan(f_obs):
        return np.nan

    if rng is None:
        rng = np.random.default_rng()

    count_ge = 0
    n_valid = 0
    for _ in range(n_perm):
        x_perm = rng.permutation(x)
        f_null = _granger_f_stat(y, x_perm, max_lag)
        if not np.isnan(f_null):
            n_valid += 1
            if f_null >= f_obs:
                count_ge += 1

    if n_valid == 0:
        return np.nan

    return (count_ge + 1) / (n_valid + 1)


# ---------------------------------------------------------------------------
# BH FDR correction
# ---------------------------------------------------------------------------

def bh_fdr(pvalues, q=0.05):
    """Benjamini-Hochberg FDR correction. Returns boolean array (rejected)."""
    pv = np.asarray(pvalues, dtype=np.float64)
    n = len(pv)
    if n == 0:
        return np.array([], dtype=bool)

    order = np.argsort(pv)
    sorted_p = pv[order]
    thresholds = q * np.arange(1, n + 1) / n

    below = np.where(sorted_p <= thresholds)[0]
    if len(below) == 0:
        return np.zeros(n, dtype=bool)

    max_k = below[-1]
    rejected = np.zeros(n, dtype=bool)
    rejected[order[:max_k + 1]] = True
    return rejected


# ---------------------------------------------------------------------------
# Single (beta, T) cell simulation
# ---------------------------------------------------------------------------

def simulate_cell(beta, T, n_rep, n_perm, sigma, fdr_q, base_seed):
    """Run n_rep replications for one (beta, T) combination.

    Each replication:
      1) Generate x, y with y_t = beta * x_{t-1} + noise
      2) Run PermG to get p-value for the signal pair
      3) Also run 7 null pairs (independent noise series) to simulate
         the project's 8-pair FDR setup

    Returns: (raw_power, fdr8_power)
      - raw_power:  fraction with raw p < 0.05
      - fdr8_power: fraction where signal pair survives BH FDR across 8 pairs
    """
    rng_master = np.random.default_rng(base_seed)
    raw_rejections = 0
    fdr8_rejections = 0

    for r in range(n_rep):
        rep_seed = int(rng_master.integers(0, 2**31))
        rng_rep = np.random.default_rng(rep_seed)

        # Signal pair: x -> y with lag-1 coupling
        x = rng_rep.normal(0, 1, size=T)
        noise = rng_rep.normal(0, sigma, size=T)
        y = np.zeros(T)
        y[0] = noise[0]
        for t in range(1, T):
            y[t] = beta * x[t - 1] + noise[t]

        pv_signal = permutation_granger_pvalue(
            x, y, max_lag=1, n_perm=n_perm,
            rng=np.random.default_rng(rep_seed + 1))
        if np.isnan(pv_signal):
            pv_signal = 1.0

        # Raw power: simple p < 0.05
        if pv_signal < 0.05:
            raw_rejections += 1

        # FDR8: 7 additional null pairs (independent noise series)
        all_pv = [pv_signal]
        for j in range(7):
            nx = rng_rep.normal(0, 1, size=T)
            ny = rng_rep.normal(0, 1, size=T)
            pv_null = permutation_granger_pvalue(
                nx, ny, max_lag=1, n_perm=n_perm,
                rng=np.random.default_rng(rep_seed + 100 + j))
            all_pv.append(pv_null if not np.isnan(pv_null) else 1.0)

        rejected = bh_fdr(np.array(all_pv), q=fdr_q)
        if rejected[0]:  # signal pair is index 0
            fdr8_rejections += 1

    return (float(raw_rejections / n_rep), float(fdr8_rejections / n_rep))


# ---------------------------------------------------------------------------
# Worker function for parallel dispatch
# ---------------------------------------------------------------------------

def _worker(args):
    beta, T, n_rep, n_perm, sigma, fdr_q, base_seed = args
    raw_power, fdr8_power = simulate_cell(beta, T, n_rep, n_perm, sigma, fdr_q, base_seed)
    return (beta, T, raw_power, fdr8_power)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    betas = [round(b * 0.1, 2) for b in range(21)]  # 0.0 .. 2.0
    T_values = [6, 8, 10, 15, 20]
    n_rep = 100
    sigma = 1.0
    fdr_q = 0.05
    master_seed = 2026

    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        n_perm = 1000
        print("QUICK MODE: n_perm=1000")
    else:
        n_perm = 5000
        print(f"FULL MODE: n_perm={n_perm}")

    print(f"Config: {len(betas)} betas x {len(T_values)} T values x {n_rep} reps")
    print(f"Total simulations: {len(betas) * len(T_values) * n_rep}")
    print(f"Each rep: 8 pairs (1 signal + 7 null) x {n_perm} perms")

    # Build task list with deterministic seeds
    tasks = []
    seed_rng = np.random.default_rng(master_seed)
    for T in T_values:
        for beta in betas:
            base_seed = int(seed_rng.integers(0, 2**31))
            tasks.append((beta, T, n_rep, n_perm, sigma, fdr_q, base_seed))

    import multiprocessing
    n_workers = min(multiprocessing.cpu_count(), 16)
    print(f"Using {n_workers} workers")

    power_raw = {f"T={T}": {} for T in T_values}
    power_fdr8 = {f"T={T}": {} for T in T_values}
    start = time.time()
    done = 0
    total = len(tasks)

    with ProcessPoolExecutor(max_workers=n_workers) as pool:
        futures = {pool.submit(_worker, t): t for t in tasks}
        for future in as_completed(futures):
            beta, T, raw_pw, fdr8_pw = future.result()
            power_raw[f"T={T}"][f"beta={beta:.2f}"] = round(raw_pw, 4)
            power_fdr8[f"T={T}"][f"beta={beta:.2f}"] = round(fdr8_pw, 4)
            done += 1
            if done % 10 == 0 or done == total:
                elapsed = time.time() - start
                eta = elapsed / done * (total - done)
                print(f"  [{done}/{total}] elapsed={elapsed:.0f}s ETA={eta:.0f}s")

    elapsed_total = time.time() - start
    print(f"\nDone in {elapsed_total:.1f}s")

    # --- Derived metrics (from fdr8, the pipeline-matched metric) ---

    fpr = {}
    for T in T_values:
        fpr[f"T={T}"] = {
            "raw": power_raw[f"T={T}"]["beta=0.00"],
            "fdr8": power_fdr8[f"T={T}"]["beta=0.00"],
        }

    beta_50 = {}
    for T in T_values:
        key = f"T={T}"
        b50_raw, b50_fdr8 = None, None
        for beta in betas:
            bk = f"beta={beta:.2f}"
            if b50_raw is None and power_raw[key][bk] >= 0.50:
                b50_raw = beta
            if b50_fdr8 is None and power_fdr8[key][bk] >= 0.50:
                b50_fdr8 = beta
        beta_50[key] = {"raw": b50_raw, "fdr8": b50_fdr8}

    # sqrt(T) scaling check on raw power
    scaling_lines = []
    for T in T_values:
        b50_val = beta_50[f"T={T}"]["raw"]
        if b50_val is not None and b50_val > 0:
            scaling_lines.append(f"  T={T}: beta_50={b50_val:.2f}, "
                                 f"beta_50*sqrt(T)={b50_val * np.sqrt(T):.3f}")
        else:
            scaling_lines.append(f"  T={T}: beta_50={b50_val}")
    scaling_msg = ("If beta_50 * sqrt(T) ≈ constant, power scales as 1/√T.\n"
                   + "\n".join(scaling_lines))

    # Print summary
    print("\n=== RAW POWER (p<0.05, no FDR) ===")
    header = f"{'beta':>6}" + "".join(f"{'T='+str(T):>8}" for T in T_values)
    print(header)
    for beta in betas:
        row = f"{beta:6.2f}"
        for T in T_values:
            row += f"{power_raw[f'T={T}'][f'beta={beta:.2f}']:8.3f}"
        print(row)

    print("\n=== FDR8 POWER (BH FDR q=0.05 across 8 pairs) ===")
    print(header)
    for beta in betas:
        row = f"{beta:6.2f}"
        for T in T_values:
            row += f"{power_fdr8[f'T={T}'][f'beta={beta:.2f}']:8.3f}"
        print(row)

    print(f"\nFPR (beta=0): {json.dumps(fpr, indent=2)}")
    print(f"beta_50: {json.dumps(beta_50, indent=2)}")
    print(f"\nsqrt(T) scaling (raw):\n{scaling_msg}")

    # --- Save results ---
    results = {
        "config": {
            "betas": betas,
            "T_values": T_values,
            "n_rep": n_rep,
            "n_perm": n_perm,
            "sigma": sigma,
            "fdr_q": fdr_q,
            "master_seed": master_seed,
        },
        "power_matrix": power_fdr8,
        "power_matrix_raw": power_raw,
        "fpr": fpr,
        "beta_50": beta_50,
        "sqrt_T_scaling_check": scaling_msg,
        "elapsed_seconds": round(elapsed_total, 1),
    }

    out_path = "/root/autodl-tmp/distrib_canary_collapse/artifacts/permg_power_analysis.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # --- Plot ---
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

        colors = {6: "#e74c3c", 8: "#e67e22", 10: "#2ecc71", 15: "#3498db", 20: "#9b59b6"}

        # Panel 1: Raw power curves
        ax = axes[0]
        for T in T_values:
            powers = [power_raw[f"T={T}"][f"beta={b:.2f}"] for b in betas]
            ax.plot(betas, powers, "o-", color=colors[T], label=f"T={T}",
                    markersize=3, linewidth=1.8)
        ax.axhline(0.05, color="gray", ls="--", lw=0.8, label="α=0.05")
        ax.axhline(0.80, color="gray", ls=":", lw=0.8, label="80% power")
        ax.set_xlabel("Signal strength (β)", fontsize=12)
        ax.set_ylabel("Detection rate", fontsize=12)
        ax.set_title("Raw Power (p < 0.05)", fontsize=13, fontweight="bold")
        ax.legend(fontsize=9, loc="upper left")
        ax.set_xlim(-0.05, 2.05)
        ax.set_ylim(-0.02, 1.02)
        ax.grid(True, alpha=0.3)

        # Panel 2: FDR8 power curves
        ax = axes[1]
        for T in T_values:
            powers = [power_fdr8[f"T={T}"][f"beta={b:.2f}"] for b in betas]
            ax.plot(betas, powers, "o-", color=colors[T], label=f"T={T}",
                    markersize=3, linewidth=1.8)
        ax.axhline(0.05, color="gray", ls="--", lw=0.8, label="α=0.05")
        ax.axhline(0.80, color="gray", ls=":", lw=0.8, label="80% power")
        ax.set_xlabel("Signal strength (β)", fontsize=12)
        ax.set_ylabel("Detection rate", fontsize=12)
        ax.set_title("FDR-adjusted Power (BH q=0.05, 8 pairs)", fontsize=13, fontweight="bold")
        ax.legend(fontsize=9, loc="upper left")
        ax.set_xlim(-0.05, 2.05)
        ax.set_ylim(-0.02, 1.02)
        ax.grid(True, alpha=0.3)

        # Panel 3: beta_50 vs 1/sqrt(T)
        ax2 = axes[2]
        for label, b50_key, marker, color in [
                ("raw", "raw", "o", "#2c3e50"),
                ("FDR8", "fdr8", "s", "#c0392b")]:
            valid_T = [T for T in T_values
                       if beta_50[f"T={T}"][b50_key] is not None
                       and beta_50[f"T={T}"][b50_key] > 0]
            if len(valid_T) >= 2:
                inv_sqrt_T = [1.0 / np.sqrt(T) for T in valid_T]
                b50_vals = [beta_50[f"T={T}"][b50_key] for T in valid_T]
                ax2.plot(inv_sqrt_T, b50_vals, f"{marker}-", color=color,
                         markersize=8, linewidth=1.5, label=label)
                for T, isT, b50 in zip(valid_T, inv_sqrt_T, b50_vals):
                    ax2.annotate(f"T={T}", (isT, b50), textcoords="offset points",
                                 xytext=(8, 5), fontsize=8)
                coeffs = np.polyfit(inv_sqrt_T, b50_vals, 1)
                x_fit = np.linspace(min(inv_sqrt_T) * 0.8, max(inv_sqrt_T) * 1.2, 50)
                ax2.plot(x_fit, np.polyval(coeffs, x_fit), "--", color=color,
                         alpha=0.4, linewidth=1)

        ax2.set_xlabel("1 / √T", fontsize=12)
        ax2.set_ylabel("β₅₀ (50% power threshold)", fontsize=12)
        ax2.set_title("Power Theory: β₅₀ ∝ 1/√T", fontsize=13, fontweight="bold")
        ax2.legend(fontsize=10)
        ax2.grid(True, alpha=0.3)

        fig.tight_layout()
        fig_path = "/root/autodl-tmp/distrib_canary_collapse/artifacts/permg_power_curve.png"
        fig.savefig(fig_path, dpi=150, bbox_inches="tight")
        print(f"Figure saved to {fig_path}")
        plt.close(fig)
    except Exception as e:
        print(f"Plotting failed: {e}")


if __name__ == "__main__":
    main()
