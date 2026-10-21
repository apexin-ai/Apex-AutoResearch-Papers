"""Evaluation utilities for the G-MFRM synthetic recovery experiment.

Computes RMSE and Kendall-tau between estimated and true theta,
aggregates multi-seed results, plots, and runs significance tests.

Dependencies: numpy, scipy, pandas, matplotlib
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


def compute_metrics(theta_hat: np.ndarray, theta_true: np.ndarray) -> dict:
    """Compute recovery metrics between estimated and true ability parameters.

    Args:
        theta_hat: Estimated theta, shape (N,).
        theta_true: Ground-truth theta, shape (N,).

    Returns:
        Dict with 'rmse' (float) and 'kendall_tau' (float).
    """
    rmse = float(np.sqrt(np.mean((theta_hat - theta_true) ** 2)))
    tau, _ = stats.kendalltau(theta_hat, theta_true)
    return {"rmse": rmse, "kendall_tau": float(tau)}


def summarize_results(all_results: list[dict]) -> pd.DataFrame:
    """Aggregate multi-seed results into mean +/- std per method and rho.

    Args:
        all_results: List of dicts, each with keys:
            rho (float), seed (int), method (str),
            rmse (float), kendall_tau (float).

    Returns:
        DataFrame indexed by (rho, method) with columns
        rmse_mean, rmse_std, tau_mean, tau_std.
    """
    df = pd.DataFrame(all_results)
    grouped = df.groupby(["rho", "method"]).agg(
        rmse_mean=("rmse", "mean"),
        rmse_std=("rmse", "std"),
        tau_mean=("kendall_tau", "mean"),
        tau_std=("kendall_tau", "std"),
    )
    return grouped.reset_index()


def plot_results(summary_df: pd.DataFrame, output_path: str | Path) -> None:
    """Line plot of RMSE vs rho for each method, with +/-1 std error bars.

    Args:
        summary_df: Output of summarize_results().
        output_path: File path to save the figure (e.g. .png).
    """
    fig, ax = plt.subplots(figsize=(7, 4.5))
    methods = summary_df["method"].unique()
    markers = ["o", "s", "^", "D"]

    for i, method in enumerate(methods):
        sub = summary_df[summary_df["method"] == method].sort_values("rho")
        ax.errorbar(
            sub["rho"],
            sub["rmse_mean"],
            yerr=sub["rmse_std"],
            label=method,
            marker=markers[i % len(markers)],
            capsize=3,
        )

    ax.set_xlabel(r"Confounding strength ($\rho$)")
    ax.set_ylabel("RMSE (theta recovery)")
    ax.set_title("G-MFRM: Theta Recovery vs Confounding")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def run_significance_test(
    results: list[dict], rho: float, alternative: str = "less"
) -> dict:
    """Paired Wilcoxon signed-rank test: joint G-MFRM RMSE vs sequential RMSE.

    Args:
        results: Full list of per-seed result dicts.
        rho: The confounding level to test.
        alternative: 'less' (joint < seq), 'two-sided', or 'greater'.

    Returns:
        Dict with 'statistic' and 'p_value'.
    """
    df = pd.DataFrame(results)
    df_rho = df[np.isclose(df["rho"], rho)]

    joint = df_rho[df_rho["method"] == "joint_gmfrm"].sort_values("seed")["rmse"].values
    seq = df_rho[df_rho["method"] == "sequential"].sort_values("seed")["rmse"].values

    diff = joint - seq
    if np.all(diff == 0):
        return {"statistic": 0.0, "p_value": 1.0}
    stat, p_value = stats.wilcoxon(diff, alternative=alternative)
    return {"statistic": float(stat), "p_value": float(p_value)}


def evaluate_pass_fail(all_results: list[dict]) -> dict:
    """Apply quantified pass/fail criteria.

    Criteria:
      1. Convergence: all MCMC fits have max R-hat < 1.05 AND min ESS > 100
      2. Improvement: at rho=0.3 AND rho=0.6, joint theta-RMSE < sequential
         (Wilcoxon signed-rank p<0.05)
      3. No degradation: at rho=0, joint not significantly worse than sequential
         (Wilcoxon p>0.05, two-sided)

    Returns dict with:
      verdict: "PASS" / "CONDITIONAL PASS" / "FAIL"
      details: dict with per-criterion results
    """
    df = pd.DataFrame(all_results)

    # Criterion 1: convergence
    mcmc_rows = df[df["method"] != "raw_average"]
    max_rhat_obs = mcmc_rows["r_hat"].max()
    min_ess_obs = mcmc_rows["ess"].min()
    convergence = (max_rhat_obs < 1.05) and (min_ess_obs > 100)

    # Criterion 2: improvement at rho=0.3 and rho=0.6
    test_03 = run_significance_test(all_results, 0.3, alternative="less")
    test_06 = run_significance_test(all_results, 0.6, alternative="less")
    pass_03 = test_03["p_value"] < 0.05
    pass_06 = test_06["p_value"] < 0.05

    # Criterion 3: no degradation at rho=0
    test_00 = run_significance_test(all_results, 0.0, alternative="two-sided")
    pass_00 = test_00["p_value"] > 0.05

    # Verdict
    if convergence and pass_03 and pass_06 and pass_00:
        verdict = "PASS"
    elif convergence and pass_06 and not pass_03 and pass_00:
        verdict = "CONDITIONAL PASS"
    else:
        verdict = "FAIL"

    return {
        "verdict": verdict,
        "details": {
            "convergence": convergence,
            "max_rhat_observed": float(max_rhat_obs),
            "min_ess_observed": float(min_ess_obs),
            "p_03": test_03["p_value"],
            "pass_03": pass_03,
            "p_06": test_06["p_value"],
            "pass_06": pass_06,
            "p_00": test_00["p_value"],
            "pass_00": pass_00,
        },
    }
