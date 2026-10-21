"""Compute Kendall-tau and Spearman-rho from MCMC theta estimates vs Chatbot Arena ELO.

Input:
  --mcmc-dir: MCMC output directory containing results.json and run_metadata.json
  --output:   Output CSV path (default: results_tau.csv in mcmc-dir)

Output:
  CSV with columns: method, N, tau, rho, p_tau, p_rho

Excludes qwen3-8b from tau computation (方案B). Also computes N=8 subset
tau by filtering to the 8 models used in the original experiment.
"""

import argparse
import csv
import json
import os
import sys

import numpy as np
from scipy.stats import kendalltau, spearmanr

BASE_DIR = "/root/gated_mfrm_judge_bias"
sys.path.insert(0, os.path.join(BASE_DIR, "exp003"))
from evaluation import ARENA_ELO, ARENA_NAME_MAPPING, EXCLUDE_MODELS

N8_MODELS_DATA = [
    "gemma-2-9b-it",
    "gpt-3.5-turbo-0613",
    "gpt-4-0613",
    "gpt-4o-2024-05-13",
    "gpt-4o-mini-2024-07-18",
    "llama-3.3-70b-instruct",
    "qwen2.5-72b-instruct",
    "qwen3-8b",
]

METHODS = ["raw_average", "mfrm_only", "sequential", "joint_gmfrm"]


def resolve_elo(model_name):
    arena_key = ARENA_NAME_MAPPING.get(model_name, model_name)
    return ARENA_ELO.get(arena_key)


def compute_correlation(theta_dict, model_subset=None, exclude=None):
    if exclude is None:
        exclude = []
    models = list(theta_dict.keys())
    if model_subset is not None:
        models = [m for m in models if m in model_subset]

    paired = []
    for m in models:
        if m in exclude:
            continue
        elo = resolve_elo(m)
        if elo is None:
            continue
        paired.append((m, theta_dict[m], elo))

    if len(paired) < 3:
        return None

    thetas = [p[1] for p in paired]
    elos = [p[2] for p in paired]
    tau, p_tau = kendalltau(thetas, elos)
    rho, p_rho = spearmanr(thetas, elos)
    return {
        "n": len(paired),
        "tau": tau,
        "rho": rho,
        "p_tau": p_tau,
        "p_rho": p_rho,
        "models": [p[0] for p in paired],
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compute tau/rho of MCMC theta vs Arena ELO"
    )
    parser.add_argument(
        "--mcmc-dir",
        required=True,
        help="MCMC output directory with results.json",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output CSV path (default: results_tau.csv in mcmc-dir)",
    )
    args = parser.parse_args()

    results_path = os.path.join(args.mcmc_dir, "results.json")
    if not os.path.exists(results_path):
        print(f"ERROR: {results_path} not found. MCMC not finished?")
        sys.exit(1)

    with open(results_path) as f:
        results = json.load(f)

    params = results.get("parameters", {})
    model_names = results.get("data_summary", {}).get("model_names", [])

    output_path = args.output or os.path.join(args.mcmc_dir, "results_tau.csv")

    rows = []
    for method in METHODS:
        method_params = params.get(method, {})
        theta_dict = method_params.get("theta_values")
        if theta_dict is None:
            print(f"  {method}: no theta_values, skipping")
            continue

        # N=17 (all models minus qwen3-8b)
        corr_17 = compute_correlation(theta_dict, exclude=EXCLUDE_MODELS)
        if corr_17:
            rows.append({
                "method": method,
                "N": corr_17["n"],
                "tau": corr_17["tau"],
                "rho": corr_17["rho"],
                "p_tau": corr_17["p_tau"],
                "p_rho": corr_17["p_rho"],
            })
            print(
                f"  {method} N={corr_17['n']}: "
                f"tau={corr_17['tau']:.3f} (p={corr_17['p_tau']:.2e}), "
                f"rho={corr_17['rho']:.3f} (p={corr_17['p_rho']:.2e})"
            )

        # N=8 subset (from N=17 theta, using only the 8 original models)
        n8_set = set(N8_MODELS_DATA)
        corr_8 = compute_correlation(
            theta_dict, model_subset=n8_set, exclude=EXCLUDE_MODELS
        )
        if corr_8:
            rows.append({
                "method": method,
                "N": corr_8["n"],
                "tau": corr_8["tau"],
                "rho": corr_8["rho"],
                "p_tau": corr_8["p_tau"],
                "p_rho": corr_8["p_rho"],
            })
            print(
                f"  {method} N={corr_8['n']} (N8 subset): "
                f"tau={corr_8['tau']:.3f} (p={corr_8['p_tau']:.2e}), "
                f"rho={corr_8['rho']:.3f} (p={corr_8['p_rho']:.2e})"
            )

    fieldnames = ["method", "N", "tau", "rho", "p_tau", "p_rho"]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSaved {len(rows)} rows to {output_path}")


if __name__ == "__main__":
    main()
