"""Main script for the G-MFRM MVP synthetic recovery experiment.

Runs all four fitting methods across multiple confounding levels (rho)
and random seeds, then evaluates recovery quality and prints verdict.

Usage: python run_mvp.py
Output: results.csv, results.png, console verdict

Dependencies: data_gen, models, evaluate (local modules), plus their deps
"""

import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

from data_gen import generate_gated_mfrm_data
from models import fit_raw_average, fit_mfrm_only, fit_sequential, fit_joint_gmfrm
from evaluate import compute_metrics, summarize_results, plot_results, run_significance_test, evaluate_pass_fail

RHOS = [0.0, 0.3, 0.6]
N_SEEDS = 20
OUTPUT_DIR = Path(__file__).parent
METHODS = ["raw_average", "mfrm_only", "sequential", "joint_gmfrm"]


def run_single(rho: float, seed: int) -> list[dict]:
    """Run all 4 methods on one (rho, seed) combination."""
    data = generate_gated_mfrm_data(rho=rho, seed=seed)
    theta_true = data["true_params"]["theta"]
    theta_true_centered = theta_true - theta_true.mean()
    e_values = data["true_params"]["e"]

    results = []

    raw = fit_raw_average(data)
    m = compute_metrics(raw["theta_hat"], theta_true_centered)
    results.append({"rho": rho, "seed": seed, "method": "raw_average",
                     "rmse": m["rmse"], "kendall_tau": m["kendall_tau"],
                     "r_hat": raw["r_hat"], "ess": raw["ess"]})

    mfrm = fit_mfrm_only(data)
    m = compute_metrics(mfrm["theta_hat"], theta_true_centered)
    results.append({"rho": rho, "seed": seed, "method": "mfrm_only",
                     "rmse": m["rmse"], "kendall_tau": m["kendall_tau"],
                     "r_hat": mfrm["r_hat"], "ess": mfrm["ess"]})

    seq = fit_sequential(data, e_values)
    m = compute_metrics(seq["theta_hat"], theta_true_centered)
    results.append({"rho": rho, "seed": seed, "method": "sequential",
                     "rmse": m["rmse"], "kendall_tau": m["kendall_tau"],
                     "r_hat": seq["r_hat"], "ess": seq["ess"]})

    joint = fit_joint_gmfrm(data, e_values)
    m = compute_metrics(joint["theta_hat"], theta_true_centered)
    results.append({"rho": rho, "seed": seed, "method": "joint_gmfrm",
                     "rmse": m["rmse"], "kendall_tau": m["kendall_tau"],
                     "r_hat": joint["r_hat"], "ess": joint["ess"]})

    return results


def print_results_table(summary_df: pd.DataFrame, all_results: list[dict]) -> None:
    """Print formatted results table."""
    print("\n" + "=" * 85)
    print(f"{'rho':>5} | {'method':<15} | {'RMSE mean±std':>18} | {'τ mean±std':>18} | {'p-value':>10}")
    print("-" * 85)

    for rho in RHOS:
        sub = summary_df[np.isclose(summary_df["rho"], rho)]
        for _, row in sub.iterrows():
            method = row["method"]
            rmse_str = f"{row['rmse_mean']:.4f}±{row['rmse_std']:.4f}"
            tau_str = f"{row['tau_mean']:.4f}±{row['tau_std']:.4f}"

            if method == "sequential":
                p_str = "ref"
            elif method in ("raw_average", "mfrm_only"):
                p_str = "—"
            else:
                test = run_significance_test(all_results, rho)
                p_str = f"{test['p_value']:.4f}"

            print(f"{rho:5.1f} | {method:<15} | {rmse_str:>18} | {tau_str:>18} | {p_str:>10}")
        print("-" * 85)
    print("=" * 85)


def main():
    print(f"G-MFRM MVP Experiment")
    print(f"Rhos: {RHOS}, Seeds: {N_SEEDS}")
    print(f"Methods: {METHODS}")

    all_results = []
    total = len(RHOS) * N_SEEDS
    done = 0

    t0 = time.time()
    for rho in RHOS:
        for seed in range(N_SEEDS):
            done += 1
            print(f"\r  [{done}/{total}] rho={rho}, seed={seed}", end="", flush=True)
            results = run_single(rho, seed)
            all_results.extend(results)

    elapsed = time.time() - t0
    print(f"\n  Completed in {elapsed:.1f}s")

    summary_df = summarize_results(all_results)

    csv_path = OUTPUT_DIR / "results.csv"
    pd.DataFrame(all_results).to_csv(csv_path, index=False)
    print(f"\nResults saved to {csv_path}")

    print_results_table(summary_df, all_results)

    plot_path = OUTPUT_DIR / "results.png"
    plot_results(summary_df, plot_path)
    print(f"Plot saved to {plot_path}")

    verdict = evaluate_pass_fail(all_results)
    print(f"\n{'='*40}")
    print(f"VERDICT: {verdict['verdict']}")
    print(f"{'='*40}")
    details = verdict["details"]
    print(f"  Convergence (R̂<1.05, ESS>100): {'PASS' if details['convergence'] else 'FAIL'}")
    if not details["convergence"]:
        print(f"    max R̂ = {details.get('max_rhat_observed', '?')}, min ESS = {details.get('min_ess_observed', '?')}")
    print(f"  ρ=0.3 improvement: p={details.get('p_03', 0):.4f} {'PASS' if details.get('pass_03') else 'FAIL'}")
    print(f"  ρ=0.6 improvement: p={details.get('p_06', 0):.4f} {'PASS' if details.get('pass_06') else 'FAIL'}")
    print(f"  ρ=0.0 no degradation: p={details.get('p_00', 0):.4f} {'PASS' if details.get('pass_00') else 'FAIL'}")

    # Kendall-τ summary
    print(f"\n  Kendall-τ (θ̂ vs θ_true):")
    for rho in RHOS:
        sub = summary_df[np.isclose(summary_df["rho"], rho)]
        for _, row in sub.iterrows():
            if row["method"] in ("sequential", "joint_gmfrm"):
                print(f"    ρ={rho} {row['method']:<15}: τ={row['tau_mean']:.4f}±{row['tau_std']:.4f}")

    if verdict["verdict"] == "FAIL":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
