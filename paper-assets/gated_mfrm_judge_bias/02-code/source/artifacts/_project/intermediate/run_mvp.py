"""Main driver for the G-MFRM synthetic recovery MVP experiment.

Sweeps over confounding levels (rho) and seeds, fits four methods,
evaluates theta recovery, and prints Pass/Fail diagnostics.

Usage:
    python run_mvp.py

Outputs:
    artifacts/mvp/results.csv  — per-seed metrics
    artifacts/mvp/results.png  — RMSE vs rho comparison plot

Dependencies: numpy, jax, numpyro, arviz, scipy, pandas, matplotlib
"""

import time
from pathlib import Path

import numpy as np

from data_gen import generate_gated_mfrm_data
from evaluate import compute_metrics, plot_results, run_significance_test, summarize_results
from models import fit_joint_gmfrm, fit_mfrm_only, fit_raw_average, fit_sequential

OUTPUT_DIR = Path(__file__).parent
RHOS = [0.0, 0.3, 0.6]
N_SEEDS = 10


def main() -> None:
    all_results: list[dict] = []
    convergence_ok = True

    t0 = time.time()
    total_runs = len(RHOS) * N_SEEDS
    run_idx = 0

    for rho in RHOS:
        for seed in range(N_SEEDS):
            run_idx += 1
            print(f"[{run_idx}/{total_runs}] rho={rho}, seed={seed}")

            data = generate_gated_mfrm_data(rho=rho, seed=seed)
            theta_true = data["true_params"]["theta"]
            e_values = data["true_params"]["e"]

            methods = {
                "raw_average": fit_raw_average(data),
                "mfrm_only": fit_mfrm_only(data),
                "sequential": fit_sequential(data, e_values),
                "joint_gmfrm": fit_joint_gmfrm(data, e_values),
            }

            for name, result in methods.items():
                metrics = compute_metrics(result["theta_hat"], theta_true)
                rhat = result.get("r_hat", float("nan"))

                if not np.isnan(rhat) and rhat >= 1.05:
                    print(f"  WARNING: {name} R-hat={rhat:.3f} >= 1.05")
                    convergence_ok = False

                all_results.append(
                    {
                        "rho": rho,
                        "seed": seed,
                        "method": name,
                        "rmse": metrics["rmse"],
                        "kendall_tau": metrics["kendall_tau"],
                        "r_hat": rhat,
                        "ess": result.get("ess", float("nan")),
                    }
                )

    elapsed = time.time() - t0
    print(f"\nAll runs completed in {elapsed:.0f}s")

    # Summarize and save
    summary_df = summarize_results(all_results)
    print("\n=== Summary ===")
    print(summary_df.to_string(index=False))

    import pandas as pd

    results_df = pd.DataFrame(all_results)
    csv_path = OUTPUT_DIR / "results.csv"
    results_df.to_csv(csv_path, index=False)
    print(f"\nResults saved to {csv_path}")

    png_path = OUTPUT_DIR / "results.png"
    plot_results(summary_df, png_path)
    print(f"Plot saved to {png_path}")

    # Pass/Fail checks
    print("\n=== Pass/Fail ===")
    passes = []

    # Condition 1: convergence
    c1 = convergence_ok
    passes.append(c1)
    print(f"[{'PASS' if c1 else 'FAIL'}] All MCMC R-hat < 1.05")

    # Condition 2: joint < sequential at rho=0.3 and rho=0.6
    for rho in [0.3, 0.6]:
        test = run_significance_test(all_results, rho)
        sig = test["p_value"] < 0.05 and test["t_stat"] < 0
        passes.append(sig)
        print(
            f"[{'PASS' if sig else 'FAIL'}] rho={rho}: "
            f"joint < sequential (t={test['t_stat']:.3f}, p={test['p_value']:.4f})"
        )

    # Condition 3: joint ≈ sequential at rho=0
    test0 = run_significance_test(all_results, 0.0)
    no_diff = test0["p_value"] > 0.05
    passes.append(no_diff)
    print(
        f"[{'PASS' if no_diff else 'FAIL'}] rho=0: "
        f"joint ≈ sequential (t={test0['t_stat']:.3f}, p={test0['p_value']:.4f})"
    )

    overall = all(passes)
    print(f"\n{'='*40}")
    print(f"OVERALL: {'PASS' if overall else 'FAIL'}")
    print(f"{'='*40}")


if __name__ == "__main__":
    main()
