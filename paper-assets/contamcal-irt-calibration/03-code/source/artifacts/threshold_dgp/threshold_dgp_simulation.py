#!/usr/bin/env python3
"""Threshold DGP simulation: demonstrate attenuation when linear 2PL+γ
is fit to data generated from a step-function contamination mechanism.

R3-W10: reviewer-requested experiment for Round 6.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Data generation
# ---------------------------------------------------------------------------

def generate_data(N, J, gamma_true, dgp_type, seed):
    """Generate binary response matrix under linear or threshold DGP.

    Parameters
    ----------
    N : int – number of respondents (LLMs)
    J : int – number of items
    gamma_true : float – true contamination effect size
    dgp_type : str – "linear" or "threshold"
    seed : int – random seed

    Returns
    -------
    y : ndarray (N, J) – binary response matrix
    exposure_matrix : ndarray (N, J) – exposure values (broadcast)
    true_params : dict
    """
    rng = np.random.RandomState(seed)

    theta = rng.randn(N)
    a = np.exp(rng.randn(J) * 0.5)  # lognormal(0, 0.5) matching Stan prior
    b = rng.randn(J)
    exposure = rng.uniform(0, 1, size=N)

    # Broadcast exposure to (N, J) matrix
    exposure_matrix = np.tile(exposure[:, None], (1, J))

    # Compute contamination effect
    if dgp_type == "linear":
        gamma_effect = gamma_true * exposure_matrix
    elif dgp_type == "threshold":
        med = np.median(exposure)
        gamma_effect = np.where(exposure_matrix > med, gamma_true, 0.0)
    else:
        raise ValueError(f"Unknown dgp_type: {dgp_type}")

    # IRT logit
    eta = a[None, :] * (theta[:, None] - b[None, :]) + gamma_effect
    prob = 1.0 / (1.0 + np.exp(-eta))
    y = (rng.uniform(size=(N, J)) < prob).astype(int)

    true_params = dict(
        theta=theta, a=a, b=b, gamma_true=gamma_true,
        exposure=exposure, dgp_type=dgp_type,
    )
    return y, exposure_matrix, true_params


# ---------------------------------------------------------------------------
# Stan fitting
# ---------------------------------------------------------------------------

def fit_stan_model(y, exposure_matrix, stan_file, seed=1, chains=4,
                   iter_sampling=1000, iter_warmup=500):
    """Fit the linear 2PL+γ Stan model via CmdStanPy.

    Returns dict with gamma posterior summary and diagnostics.
    """
    import cmdstanpy

    N, J = y.shape
    stan_data = dict(
        N_models=N,
        N_items=J,
        y=y.tolist(),
        exposure=exposure_matrix.tolist(),
    )

    model = cmdstanpy.CmdStanModel(stan_file=str(stan_file))

    fit = model.sample(
        data=stan_data,
        seed=seed,
        chains=chains,
        iter_sampling=iter_sampling,
        iter_warmup=iter_warmup,
        show_progress=False,
        show_console=False,
    )

    # Extract gamma
    gamma_draws = fit.stan_variable("gamma")  # shape (chains*iter_sampling,)
    gamma_mean = float(np.mean(gamma_draws))
    gamma_sd = float(np.std(gamma_draws))
    gamma_q025 = float(np.percentile(gamma_draws, 2.5))
    gamma_q975 = float(np.percentile(gamma_draws, 97.5))

    # Diagnostics
    diag = fit.diagnose()
    n_divergent = diag.count("divergent transition") if isinstance(diag, str) else 0

    return dict(
        gamma_mean=gamma_mean,
        gamma_sd=gamma_sd,
        gamma_q025=gamma_q025,
        gamma_q975=gamma_q975,
        n_divergent=n_divergent,
    )


# ---------------------------------------------------------------------------
# Single run
# ---------------------------------------------------------------------------

def run_single(N, J, gamma_true, dgp_type, seed, stan_file, chains=4,
               iter_sampling=1000, iter_warmup=500):
    """Run one simulation: generate + fit + summarize."""
    y, exposure_matrix, true_params = generate_data(N, J, gamma_true, dgp_type, seed)

    result = fit_stan_model(
        y, exposure_matrix, stan_file, seed=seed,
        chains=chains, iter_sampling=iter_sampling, iter_warmup=iter_warmup,
    )

    gamma_hat = result["gamma_mean"]
    covers = (result["gamma_q025"] <= gamma_true <= result["gamma_q975"])
    attenuation = gamma_hat / gamma_true if gamma_true != 0 else np.nan

    return dict(
        dgp_type=dgp_type,
        N=N,
        J=J,
        gamma_true=gamma_true,
        seed=seed,
        gamma_hat=gamma_hat,
        gamma_hat_sd=result["gamma_sd"],
        gamma_q025=result["gamma_q025"],
        gamma_q975=result["gamma_q975"],
        covers_95ci=int(covers),
        attenuation_ratio=attenuation,
        n_divergent=result["n_divergent"],
    )


# ---------------------------------------------------------------------------
# Main sweep
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stan-file", type=str, default=None,
                        help="Path to contam_irt_2pl_gamma.stan")
    parser.add_argument("--output-dir", type=str,
                        default="/root/contamcal-irt-calibration/artifacts/threshold_dgp")
    parser.add_argument("--N", type=int, default=20,
                        help="Number of respondents")
    parser.add_argument("--n-seeds", type=int, default=10)
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--iter-sampling", type=int, default=1000)
    parser.add_argument("--iter-warmup", type=int, default=500)
    parser.add_argument("--dry-run", action="store_true",
                        help="Run 1 condition x 1 seed only")
    args = parser.parse_args()

    if args.stan_file is None:
        args.stan_file = "/root/contamcal-irt-calibration/stan_models/contam_irt_2pl_gamma.stan"

    stan_file = Path(args.stan_file)
    if not stan_file.exists():
        sys.exit(f"Stan file not found: {stan_file}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Parameter grid: 4 J levels x 5 gamma levels = 20 conditions
    J_values = [50, 100, 200, 500]
    gamma_values = [0.5, 1.0, 1.5, 2.0, 3.0]

    if args.dry_run:
        J_values = [100]
        gamma_values = [1.0]
        seeds = [0]
        print("=== DRY RUN: 1 condition (J=100, γ=1.0) × 1 seed ===")
    else:
        seeds = list(range(args.n_seeds))

    # We run BOTH dgp types for every condition to show the contrast
    dgp_types = ["linear", "threshold"]

    total = len(dgp_types) * len(J_values) * len(gamma_values) * len(seeds)
    print(f"Total runs: {total} ({len(dgp_types)} DGPs × {len(J_values)} J × "
          f"{len(gamma_values)} γ × {len(seeds)} seeds)")
    print(f"N_respondents = {args.N}, chains = {args.chains}, "
          f"iter = {args.iter_sampling}+{args.iter_warmup}")

    results = []
    done = 0
    t0 = time.time()

    for dgp_type in dgp_types:
        for J in J_values:
            for gamma_true in gamma_values:
                for seed in seeds:
                    done += 1
                    label = f"[{done}/{total}] dgp={dgp_type} J={J} γ={gamma_true} seed={seed}"
                    try:
                        row = run_single(
                            N=args.N, J=J, gamma_true=gamma_true,
                            dgp_type=dgp_type, seed=seed,
                            stan_file=stan_file,
                            chains=args.chains,
                            iter_sampling=args.iter_sampling,
                            iter_warmup=args.iter_warmup,
                        )
                        results.append(row)
                        elapsed = time.time() - t0
                        eta = elapsed / done * (total - done)
                        print(f"{label} → γ̂={row['gamma_hat']:.3f} "
                              f"atten={row['attenuation_ratio']:.3f} "
                              f"div={row['n_divergent']} "
                              f"[{elapsed:.0f}s elapsed, ETA {eta:.0f}s]",
                              flush=True)
                    except Exception as e:
                        print(f"{label} FAILED: {e}", flush=True)
                        results.append(dict(
                            dgp_type=dgp_type, N=args.N, J=J,
                            gamma_true=gamma_true, seed=seed,
                            gamma_hat=np.nan, gamma_hat_sd=np.nan,
                            gamma_q025=np.nan, gamma_q975=np.nan,
                            covers_95ci=np.nan, attenuation_ratio=np.nan,
                            n_divergent=np.nan, error=str(e),
                        ))

    # Save raw results
    df = pd.DataFrame(results)
    raw_path = output_dir / "threshold_dgp_raw.csv"
    df.to_csv(raw_path, index=False)
    print(f"\nRaw results saved: {raw_path}")

    # Summary table
    if len(df) > 0 and not df["attenuation_ratio"].isna().all():
        summary = (
            df.groupby(["dgp_type", "J", "gamma_true"])
            .agg(
                mean_attenuation=("attenuation_ratio", "mean"),
                sd_attenuation=("attenuation_ratio", "std"),
                coverage_95ci=("covers_95ci", "mean"),
                mean_gamma_hat=("gamma_hat", "mean"),
                mean_divergent=("n_divergent", "mean"),
                n_runs=("seed", "count"),
            )
            .reset_index()
        )
        summary_path = output_dir / "threshold_dgp_summary.csv"
        summary.to_csv(summary_path, index=False)
        print(f"Summary saved: {summary_path}")

        # Print summary
        print("\n" + "=" * 80)
        print("SUMMARY: Attenuation ratios (γ̂/γ_true)")
        print("=" * 80)
        for dgp in dgp_types:
            sub = summary[summary["dgp_type"] == dgp]
            print(f"\n--- DGP: {dgp} ---")
            pivot = sub.pivot_table(
                index="J", columns="gamma_true",
                values="mean_attenuation", aggfunc="first"
            )
            print(pivot.to_string(float_format="%.3f"))

        print("\n--- Coverage (95% CI) under threshold DGP ---")
        thr = summary[summary["dgp_type"] == "threshold"]
        pivot_cov = thr.pivot_table(
            index="J", columns="gamma_true",
            values="coverage_95ci", aggfunc="first"
        )
        print(pivot_cov.to_string(float_format="%.2f"))

    # Sentinel file
    with open(output_dir / "DONE", "w") as f:
        f.write(f"completed at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"total runs: {total}, elapsed: {time.time() - t0:.0f}s\n")

    print(f"\nTotal time: {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
