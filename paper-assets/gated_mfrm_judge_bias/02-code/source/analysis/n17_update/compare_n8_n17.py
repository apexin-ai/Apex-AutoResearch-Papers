"""Compare N=8 vs N=17 MCMC results on shared models.

Input:
  --n8-dir:  N=8 MCMC output directory (exp003/output_003b)
  --n17-dir: N=17 MCMC output directory (exp003/output_n17_phase1)
  --output:  Output CSV path (default: comparison_summary.csv in n17-dir)

Output:
  CSV summarizing theta rank changes, tau changes, c/d estimate shifts.
  Console table with key comparison metrics.

The N=8 and N=17 experiments use different model name formats:
  N=8: short names (gpt-4o, gemma-2-9b, ...)
  N=17: full names (gpt-4o-2024-05-13, gemma-2-9b-it, ...)
This script handles the mapping automatically.
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

N8_TO_N17_MODEL_MAP = {
    "gemma-2-9b": "gemma-2-9b-it",
    "gpt-3.5-turbo-0125": "gpt-3.5-turbo-0613",
    "gpt-4-0613": "gpt-4-0613",
    "gpt-4o": "gpt-4o-2024-05-13",
    "gpt-4o-mini": "gpt-4o-mini-2024-07-18",
    "llama-3.3-70b": "llama-3.3-70b-instruct",
    "qwen2.5-72b": "qwen2.5-72b-instruct",
    "qwen3-8b": "qwen3-8b",
}

METHODS = ["raw_average", "mfrm_only", "sequential", "joint_gmfrm"]


def load_results(path):
    results_path = os.path.join(path, "results.json")
    if not os.path.exists(results_path):
        print(f"ERROR: {results_path} not found.")
        sys.exit(1)
    with open(results_path) as f:
        return json.load(f)


def get_theta_dict(results, method):
    return results.get("parameters", {}).get(method, {}).get("theta_values", {})


def get_c_dict(results, method):
    return results.get("parameters", {}).get(method, {}).get("c_values", {})


def get_d_dict(results, method):
    return results.get("parameters", {}).get(method, {}).get("d_values", {})


def compare_theta_on_shared(n8_theta, n17_theta, exclude=None):
    if exclude is None:
        exclude = []
    shared = []
    for n8_name, n17_name in N8_TO_N17_MODEL_MAP.items():
        if n8_name in exclude or n17_name in exclude:
            continue
        if n8_name in n8_theta and n17_name in n17_theta:
            shared.append((n8_name, n8_theta[n8_name], n17_theta[n17_name]))

    if len(shared) < 3:
        return None

    names = [s[0] for s in shared]
    v8 = [s[1] for s in shared]
    v17 = [s[2] for s in shared]

    tau, p_tau = kendalltau(v8, v17)
    rho, p_rho = spearmanr(v8, v17)
    diffs = [v17[i] - v8[i] for i in range(len(shared))]

    return {
        "n_shared": len(shared),
        "models": names,
        "tau": tau,
        "rho": rho,
        "p_tau": p_tau,
        "p_rho": p_rho,
        "max_abs_diff": max(abs(d) for d in diffs),
        "mean_abs_diff": np.mean([abs(d) for d in diffs]),
        "per_model": {names[i]: {"n8": v8[i], "n17": v17[i], "diff": diffs[i]} for i in range(len(shared))},
    }


def compare_d_on_shared(n8_d, n17_d):
    shared_judges = set(n8_d.keys()) & set(n17_d.keys())
    if len(shared_judges) < 2:
        return None

    judges = sorted(shared_judges)
    v8 = [n8_d[j] for j in judges]
    v17 = [n17_d[j] for j in judges]
    diffs = [n17_d[j] - n8_d[j] for j in judges]

    tau, p_tau = kendalltau(v8, v17)
    rho, p_rho = spearmanr(v8, v17)

    return {
        "n_shared": len(judges),
        "judges": judges,
        "tau": tau,
        "rho": rho,
        "max_abs_diff": max(abs(d) for d in diffs),
        "per_judge": {judges[i]: {"n8": v8[i], "n17": v17[i], "diff": diffs[i]} for i in range(len(judges))},
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compare N=8 vs N=17 MCMC results"
    )
    parser.add_argument(
        "--n8-dir", required=True, help="N=8 output directory (exp003/output_003b)"
    )
    parser.add_argument(
        "--n17-dir", required=True, help="N=17 output directory"
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output CSV path (default: comparison_summary.csv in n17-dir)",
    )
    args = parser.parse_args()

    n8 = load_results(args.n8_dir)
    n17 = load_results(args.n17_dir)
    output_path = args.output or os.path.join(args.n17_dir, "comparison_summary.csv")

    print("=" * 70)
    print("N=8 vs N=17 Comparison (shared models, excluding qwen3-8b)")
    print("=" * 70)

    rows = []

    # N=8 only has joint_gmfrm in results.json
    n8_methods = [m for m in METHODS if get_theta_dict(n8, m)]
    n17_methods = [m for m in METHODS if get_theta_dict(n17, m)]

    for method in METHODS:
        n8_theta = get_theta_dict(n8, method)
        n17_theta = get_theta_dict(n17, method)
        if not n8_theta or not n17_theta:
            continue

        comp = compare_theta_on_shared(n8_theta, n17_theta, exclude=EXCLUDE_MODELS)
        if comp is None:
            continue

        print(f"\n--- {method} ---")
        print(f"  Shared models: {comp['n_shared']}")
        print(f"  Theta rank tau (N8 vs N17): {comp['tau']:.3f} (p={comp['p_tau']:.3f})")
        print(f"  Theta rank rho: {comp['rho']:.3f}")
        print(f"  Max |delta_theta|: {comp['max_abs_diff']:.3f}")
        print(f"  Mean |delta_theta|: {comp['mean_abs_diff']:.3f}")

        print(f"  Per-model theta changes:")
        for m, vals in sorted(comp["per_model"].items(), key=lambda x: abs(x[1]["diff"]), reverse=True):
            print(f"    {m:25s}  N8={vals['n8']:+.3f}  N17={vals['n17']:+.3f}  delta={vals['diff']:+.3f}")

        rows.append({
            "metric": f"{method}_theta_rank_tau",
            "value": f"{comp['tau']:.3f}",
            "p_value": f"{comp['p_tau']:.2e}",
            "n": comp["n_shared"],
        })
        rows.append({
            "metric": f"{method}_theta_rank_rho",
            "value": f"{comp['rho']:.3f}",
            "p_value": f"{comp['p_rho']:.2e}",
            "n": comp["n_shared"],
        })
        rows.append({
            "metric": f"{method}_theta_max_abs_diff",
            "value": f"{comp['max_abs_diff']:.3f}",
            "p_value": "",
            "n": comp["n_shared"],
        })

        # c comparison
        n8_c = get_c_dict(n8, method)
        n17_c = get_c_dict(n17, method)
        if n8_c and n17_c:
            c_comp = compare_theta_on_shared(n8_c, n17_c, exclude=EXCLUDE_MODELS)
            if c_comp:
                print(f"  c rank tau: {c_comp['tau']:.3f}, max |delta_c|: {c_comp['max_abs_diff']:.3f}")
                rows.append({
                    "metric": f"{method}_c_rank_tau",
                    "value": f"{c_comp['tau']:.3f}",
                    "p_value": f"{c_comp['p_tau']:.2e}",
                    "n": c_comp["n_shared"],
                })

    # d_j comparison (judge severity)
    for method in METHODS:
        n8_d = get_d_dict(n8, method)
        n17_d = get_d_dict(n17, method)
        if not n8_d or not n17_d:
            continue
        d_comp = compare_d_on_shared(n8_d, n17_d)
        if d_comp:
            print(f"\n--- {method} judge severity (d_j) ---")
            print(f"  Shared judges: {d_comp['n_shared']}")
            print(f"  d rank tau: {d_comp['tau']:.3f}")
            print(f"  Max |delta_d|: {d_comp['max_abs_diff']:.3f}")
            for j, vals in sorted(d_comp["per_judge"].items(), key=lambda x: abs(x[1]["diff"]), reverse=True):
                print(f"    {j:30s}  N8={vals['n8']:+.3f}  N17={vals['n17']:+.3f}  delta={vals['diff']:+.3f}")
            rows.append({
                "metric": f"{method}_d_rank_tau",
                "value": f"{d_comp['tau']:.3f}",
                "p_value": f"{d_comp['p_tau']:.2e}" if d_comp.get("p_tau") else "",
                "n": d_comp["n_shared"],
            })

    # Arena tau comparison
    print("\n--- Arena ELO correlation comparison ---")
    for method in METHODS:
        n8_corr = n8.get("arena_correlation", {}).get(method, {})
        n17_corr = n17.get("arena_correlation", {}).get(method, {})
        if "kendall_tau" in n8_corr and "kendall_tau" in n17_corr:
            delta = n17_corr["kendall_tau"] - n8_corr["kendall_tau"]
            print(
                f"  {method}: tau N8={n8_corr['kendall_tau']:.3f} -> "
                f"N17={n17_corr['kendall_tau']:.3f} (delta={delta:+.3f})"
            )
            rows.append({
                "metric": f"{method}_arena_tau_n8",
                "value": f"{n8_corr['kendall_tau']:.3f}",
                "p_value": f"{n8_corr['kendall_p']:.2e}",
                "n": n8_corr.get("n_matched", ""),
            })
            rows.append({
                "metric": f"{method}_arena_tau_n17",
                "value": f"{n17_corr['kendall_tau']:.3f}",
                "p_value": f"{n17_corr['kendall_p']:.2e}",
                "n": n17_corr.get("n_matched", ""),
            })
            rows.append({
                "metric": f"{method}_arena_tau_delta",
                "value": f"{delta:+.3f}",
                "p_value": "",
                "n": "",
            })

    fieldnames = ["metric", "value", "p_value", "n"]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSaved {len(rows)} metrics to {output_path}")


if __name__ == "__main__":
    main()
