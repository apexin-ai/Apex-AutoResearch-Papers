"""Generate LaTeX tables from MCMC results for paper inclusion.

Input:
  --mcmc-dir:   MCMC output directory with results.json
  --tau-csv:    Output of compute_tau_n17.py (results_tau.csv)
  --output-dir: Directory for .tex files (default: tables/ under mcmc-dir)

Output:
  table1_method_comparison.tex  - tau/rho comparison across methods and N
  table2_theta_estimates.tex    - per-model theta/c estimates
"""

import argparse
import csv
import json
import os
import sys

BASE_DIR = "/root/gated_mfrm_judge_bias"
sys.path.insert(0, os.path.join(BASE_DIR, "exp003"))
from evaluation import ARENA_ELO, ARENA_NAME_MAPPING, EXCLUDE_MODELS

METHODS = ["raw_average", "mfrm_only", "sequential", "joint_gmfrm"]
METHOD_DISPLAY = {
    "raw_average": "Raw Average",
    "mfrm_only": "MFRM",
    "sequential": "Sequential",
    "joint_gmfrm": "G-MFRM (Joint)",
}


def resolve_elo(model_name):
    arena_key = ARENA_NAME_MAPPING.get(model_name, model_name)
    return ARENA_ELO.get(arena_key)


def short_name(model_name):
    mapping = {
        "claude-3-5-sonnet-20241022": "Claude-3.5-Sonnet",
        "claude-3-haiku-20240307": "Claude-3-Haiku",
        "claude-3-opus-20240229": "Claude-3-Opus",
        "gemma-2-27b-it": "Gemma-2-27B",
        "gemma-2-9b-it": "Gemma-2-9B",
        "gpt-3.5-turbo-0613": "GPT-3.5-Turbo",
        "gpt-4-0613": "GPT-4",
        "gpt-4-turbo-2024-04-09": "GPT-4-Turbo",
        "gpt-4o-2024-05-13": "GPT-4o",
        "gpt-4o-mini-2024-07-18": "GPT-4o-mini",
        "llama-3-70b-instruct": "Llama-3-70B",
        "llama-3-8b-instruct": "Llama-3-8B",
        "llama-3.1-70b-instruct": "Llama-3.1-70B",
        "llama-3.3-70b-instruct": "Llama-3.3-70B",
        "mistral-large-2407": "Mistral-Large",
        "mixtral-8x22b-instruct-v0.1": "Mixtral-8x22B",
        "qwen2.5-72b-instruct": "Qwen2.5-72B",
        "qwen3-8b": "Qwen3-8B*",
    }
    return mapping.get(model_name, model_name)


def load_tau_csv(path):
    rows = {}
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row["method"], int(row["N"]))
            rows[key] = {
                "tau": float(row["tau"]),
                "rho": float(row["rho"]),
                "p_tau": float(row["p_tau"]),
                "p_rho": float(row["p_rho"]),
            }
    return rows


def gen_table1(tau_data, output_path):
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(
        r"\caption{Correlation with Chatbot Arena ELO across methods and model pool sizes.}"
    )
    lines.append(r"\label{tab:method_comparison}")
    lines.append(r"\begin{tabular}{l cc cc c}")
    lines.append(r"\toprule")
    lines.append(
        r"& \multicolumn{2}{c}{$N\!=\!8$} & \multicolumn{2}{c}{$N\!=\!17$} & \\"
    )
    lines.append(r"\cmidrule(lr){2-3} \cmidrule(lr){4-5}")
    lines.append(r"Method & $\tau$ & $\rho$ & $\tau$ & $\rho$ & $\Delta\tau$ \\")
    lines.append(r"\midrule")

    n8_key_n = None
    n17_key_n = None
    for (method, n), v in tau_data.items():
        if n <= 8:
            n8_key_n = n
        else:
            n17_key_n = n

    for method in METHODS:
        display = METHOD_DISPLAY[method]
        n8 = tau_data.get((method, n8_key_n))
        n17 = tau_data.get((method, n17_key_n))

        t8 = f"{n8['tau']:.3f}" if n8 else "---"
        r8 = f"{n8['rho']:.3f}" if n8 else "---"
        t17 = f"{n17['tau']:.3f}" if n17 else "---"
        r17 = f"{n17['rho']:.3f}" if n17 else "---"

        if n8 and n17:
            delta = n17["tau"] - n8["tau"]
            delta_str = f"{delta:+.3f}"
        else:
            delta_str = "---"

        if method == "joint_gmfrm":
            lines.append(
                rf"\textbf{{{display}}} & \textbf{{{t8}}} & \textbf{{{r8}}} "
                rf"& \textbf{{{t17}}} & \textbf{{{r17}}} & \textbf{{{delta_str}}} \\"
            )
        else:
            lines.append(
                rf"{display} & {t8} & {r8} & {t17} & {r17} & {delta_str} \\"
            )

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")

    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  Table 1 saved to {output_path}")


def gen_table2(results, output_path):
    params = results.get("parameters", {})
    model_names = results.get("data_summary", {}).get("model_names", [])

    gmfrm = params.get("joint_gmfrm", {})
    theta_gmfrm = gmfrm.get("theta_values", {})
    c_gmfrm = gmfrm.get("c_values", {})

    raw_theta = params.get("raw_average", {}).get("theta_values", {})
    mfrm_theta = params.get("mfrm_only", {}).get("theta_values", {})
    seq_theta = params.get("sequential", {}).get("theta_values", {})

    sorted_models = sorted(
        [m for m in model_names if m not in EXCLUDE_MODELS],
        key=lambda m: theta_gmfrm.get(m, 0),
        reverse=True,
    )

    lines = []
    lines.append(r"\begin{table*}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(
        r"\caption{Per-model parameter estimates across methods. "
        r"$\hat{\theta}$: ability estimate; $\hat{c}$: contamination sensitivity (G-MFRM).}"
    )
    lines.append(r"\label{tab:theta_estimates}")
    lines.append(r"\begin{tabular}{l rrrr r r}")
    lines.append(r"\toprule")
    lines.append(
        r"Model & $\hat{\theta}_{\text{raw}}$ & $\hat{\theta}_{\text{mfrm}}$ "
        r"& $\hat{\theta}_{\text{seq}}$ & $\hat{\theta}_{\text{gmfrm}}$ "
        r"& Arena ELO & $\hat{c}$ \\"
    )
    lines.append(r"\midrule")

    for m in sorted_models:
        sn = short_name(m)
        t_raw = f"{raw_theta[m]:.3f}" if m in raw_theta else "---"
        t_mfrm = f"{mfrm_theta[m]:.3f}" if m in mfrm_theta else "---"
        t_seq = f"{seq_theta[m]:.3f}" if m in seq_theta else "---"
        t_gm = f"{theta_gmfrm[m]:.3f}" if m in theta_gmfrm else "---"

        elo = resolve_elo(m)
        elo_str = str(elo) if elo else "---"

        c_val = c_gmfrm.get(m)
        c_str = f"{c_val:.3f}" if c_val is not None else "---"

        lines.append(
            rf"{sn} & {t_raw} & {t_mfrm} & {t_seq} & {t_gm} & {elo_str} & {c_str} \\"
        )

    # qwen3-8b as probe row
    if "qwen3-8b" in theta_gmfrm:
        m = "qwen3-8b"
        sn = short_name(m)
        t_raw = f"{raw_theta.get(m, 0):.3f}" if m in raw_theta else "---"
        t_mfrm = f"{mfrm_theta.get(m, 0):.3f}" if m in mfrm_theta else "---"
        t_seq = f"{seq_theta.get(m, 0):.3f}" if m in seq_theta else "---"
        t_gm = f"{theta_gmfrm[m]:.3f}"
        c_val = c_gmfrm.get(m)
        c_str = f"{c_val:.3f}" if c_val is not None else "---"
        lines.append(r"\midrule")
        lines.append(
            rf"\textit{{{sn}}} & {t_raw} & {t_mfrm} & {t_seq} & {t_gm} & --- & {c_str} \\"
        )

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table*}")

    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  Table 2 saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate LaTeX tables from MCMC results"
    )
    parser.add_argument(
        "--mcmc-dir", required=True, help="MCMC output directory with results.json"
    )
    parser.add_argument(
        "--tau-csv", required=True, help="CSV from compute_tau_n17.py"
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory for .tex files (default: tables/ under mcmc-dir)",
    )
    args = parser.parse_args()

    results_path = os.path.join(args.mcmc_dir, "results.json")
    if not os.path.exists(results_path):
        print(f"ERROR: {results_path} not found.")
        sys.exit(1)
    if not os.path.exists(args.tau_csv):
        print(f"ERROR: {args.tau_csv} not found. Run compute_tau_n17.py first.")
        sys.exit(1)

    with open(results_path) as f:
        results = json.load(f)

    tau_data = load_tau_csv(args.tau_csv)

    output_dir = args.output_dir or os.path.join(args.mcmc_dir, "tables")
    os.makedirs(output_dir, exist_ok=True)

    print("Generating Table 1 (method comparison)...")
    gen_table1(tau_data, os.path.join(output_dir, "table1_method_comparison.tex"))

    print("Generating Table 2 (per-model theta)...")
    gen_table2(results, os.path.join(output_dir, "table2_theta_estimates.tex"))

    print(f"\nDone. Tables in {output_dir}")


if __name__ == "__main__":
    main()
