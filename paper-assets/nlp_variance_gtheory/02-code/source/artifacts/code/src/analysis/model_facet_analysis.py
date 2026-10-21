"""Multi-model G-theory variance decomposition (exp-001).

Extends the MVP single-model analysis to a fully-crossed design with 7 facets:
model, precision, temperature, prompt_template, seed, ordering, item_id.

Estimates all 7 main effects + 21 two-way interactions + residual using
Henderson Method I (ANOVA-based), identical to the MVP approach but with
model added as a crossed random facet.

Input:  One or more JSONL files from multi-model experiments. Each row has
        model, precision, temperature, prompt_template, seed, ordering,
        item_id, correct, generated_text.
Output: JSON with variance components, G coefficient, and D-study projections.
"""

import argparse
import glob
import json
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

from src.analysis.variance_decomposition import (
    compute_ss,
    compute_text_exact_match,
    estimate_variance_components,
)

ALL_FACETS = [
    "model", "precision", "temperature",
    "prompt_template", "seed", "ordering", "item_id",
]
FIXED_FACETS = ["precision", "temperature"]
RANDOM_FACETS = ["model", "prompt_template", "seed", "ordering", "item_id"]


def load_jsonl_glob(patterns: list[str]) -> pd.DataFrame:
    """Load and concatenate JSONL files matching one or more glob patterns.

    Args:
        patterns: List of file paths or glob patterns (e.g. ["results/*.jsonl"]).

    Returns:
        Combined DataFrame.
    """
    paths = []
    for pat in patterns:
        expanded = sorted(glob.glob(pat))
        if not expanded:
            raise FileNotFoundError(f"No files matched pattern: {pat}")
        paths.extend(expanded)

    frames = [pd.read_json(p, lines=True) for p in paths]
    df = pd.concat(frames, ignore_index=True)

    for col in ["answer_logprob"]:
        if col in df.columns:
            df[col] = df[col].replace(-np.inf, np.nan)
    if "top_logprobs" in df.columns:
        df["top_logprobs"] = df["top_logprobs"].apply(
            lambda x: {k: (v if v != float('-inf') else None) for k, v in x.items()} if isinstance(x, dict) else x
        )

    print(f"Loaded {len(df)} observations from {len(paths)} file(s)")
    return df


def compute_g_coefficient(
    variance_components: dict[str, float],
    random_n: dict[str, int],
) -> tuple[float, float, float]:
    """Compute generalizability coefficient for a D-study design.

    Universe-score variance (sigma_tau): components involving only fixed facets.
    Relative error variance (sigma_delta): components with >= 1 random facet,
    each divided by the product of sample sizes of the random facets it contains.

    Args:
        variance_components: {component_name: estimate} from G-study.
        random_n: Number of levels for each random facet in the D-study design.

    Returns:
        (G, sigma_tau, sigma_delta).
    """
    fixed_set = set(FIXED_FACETS)
    sigma_tau = 0.0
    sigma_delta = 0.0

    for component, est in variance_components.items():
        if component == "residual":
            divisor = prod(random_n.get(f, 1) for f in RANDOM_FACETS)
            sigma_delta += est / divisor
            continue

        facets_in = component.split(":")
        random_in = [f for f in facets_in if f not in fixed_set]

        if len(random_in) == 0:
            sigma_tau += est
        else:
            divisor = prod(random_n.get(f, 1) for f in random_in)
            sigma_delta += est / divisor

    total = sigma_tau + sigma_delta
    g = sigma_tau / total if total > 0 else 0.0
    return g, sigma_tau, sigma_delta


def d_study_model_sweep(
    variance_components: dict[str, float],
    base_levels: dict[str, int],
    max_models: int = 10,
) -> list[dict]:
    """Sweep model count from 1 to max_models, holding other facets fixed.

    Args:
        variance_components: G-study variance component estimates.
        base_levels: Baseline replication counts for all random facets.
        max_models: Maximum number of models to project.

    Returns:
        List of {n_models, g, sigma_tau, sigma_delta} dicts.
    """
    results = []
    for n in range(1, max_models + 1):
        levels = base_levels.copy()
        levels["model"] = n
        g, tau, delta = compute_g_coefficient(variance_components, levels)
        results.append({
            "n_models": n,
            "g": round(g, 6),
            "sigma_tau": round(tau, 8),
            "sigma_delta": round(delta, 8),
        })
    return results


def run_analysis(
    data_patterns: list[str] | None = None,
    output_path: str = "results/analysis/model_variance_components.json",
    response_var: str = "correct",
    input_csv: str | None = None,
    precisions: list[str] | None = None,
) -> dict:
    """Full multi-model G-theory analysis.

    Args:
        data_patterns: Glob patterns for input JSONL files.
        output_path: Destination JSON path.
        response_var: "correct" or "text_exact_match".
        input_csv: CSV path (alternative to data_patterns).
        precisions: If set, keep only these precision levels.

    Returns:
        Results dict (also written to output_path).
    """
    if input_csv:
        df = pd.read_csv(input_csv)
        print(f"Loaded {len(df)} observations from {input_csv}")
    elif data_patterns:
        df = load_jsonl_glob(data_patterns)
    else:
        raise ValueError("Either data_patterns or input_csv must be provided")

    if precisions:
        before = len(df)
        df = df[df["precision"].astype(str).isin(precisions)].reset_index(drop=True)
        print(f"Precision filter: kept {len(df)}/{before} rows")

    for f in ALL_FACETS:
        df[f] = df[f].astype(str)

    if response_var == "text_exact_match":
        df = compute_text_exact_match(df)

    print(f"Running 7-facet G-study on {len(df)} observations (response={response_var})")

    effects, n_levels = compute_ss(df, response_var, ALL_FACETS)
    vc = estimate_variance_components(effects, ALL_FACETS, n_levels)
    total_var = sum(vc.values())

    # G coefficient at observed design
    observed_random_n = {f: n_levels[f] for f in RANDOM_FACETS}
    g_current, tau, delta = compute_g_coefficient(vc, observed_random_n)

    # D-study: sweep model count
    model_sweep = d_study_model_sweep(vc, observed_random_n, max_models=10)

    results = {
        "variance_components": {
            k: {
                "estimate": v,
                "pct": v / total_var * 100 if total_var > 0 else 0.0,
            }
            for k, v in vc.items()
        },
        "total_variance": total_var,
        "n_observations": len(df),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "fixed_facets": FIXED_FACETS,
        "random_facets": RANDOM_FACETS,
        "all_facets": ALL_FACETS,
        "anova_table": {
            k: {"ss": v["ss"], "df": v["df"], "ms": v["ms"]}
            for k, v in effects.items()
        },
        "g_coefficient": {
            "g": round(g_current, 6),
            "sigma_tau": round(tau, 8),
            "sigma_delta": round(delta, 8),
        },
        "d_study_model_sweep": model_sweep,
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as fout:
        json.dump(results, fout, indent=2)

    _print_summary(results)
    print(f"\n-> {output_path}")
    return results


def _print_summary(results: dict) -> None:
    """Print formatted variance decomposition table."""
    vc = results["variance_components"]
    n_obs = results["n_observations"]
    g = results["g_coefficient"]["g"]

    print(f"\nMulti-model G-theory Variance Decomposition  ({n_obs} obs, 7 facets)")
    print(f"G coefficient = {g:.4f}\n")

    header = f"{'Component':<30} {'Estimate':>10} {'%':>8}"
    print(header)
    print("-" * len(header))
    for name, info in sorted(vc.items(), key=lambda x: -x[1]["estimate"]):
        print(f"{name:<30} {info['estimate']:>10.6f} {info['pct']:>7.1f}%")

    print(f"\nD-study: model count sweep")
    print(f"{'n_models':>10} {'G':>10}")
    print("-" * 22)
    for row in results["d_study_model_sweep"]:
        print(f"{row['n_models']:>10} {row['g']:>10.4f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Multi-model G-theory variance decomposition (exp-001)"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--data", nargs="+",
        help="JSONL file(s) or glob pattern(s) (e.g. results/exp001/*.jsonl)",
    )
    group.add_argument(
        "--input", dest="input_csv",
        help="Input CSV path (pre-merged, alternative to --data)",
    )
    parser.add_argument(
        "--response-var", default="correct",
        choices=["correct", "text_exact_match"],
        help="Response variable (default: correct)",
    )
    parser.add_argument(
        "--precisions",
        help="Comma-separated precision levels to keep (e.g. bfloat16,float32)",
    )
    parser.add_argument(
        "--output", default="results/analysis/model_variance_components.json",
        help="Output JSON path",
    )
    args = parser.parse_args()
    prec_list = [p.strip() for p in args.precisions.split(",")] if args.precisions else None
    run_analysis(
        data_patterns=args.data,
        output_path=args.output,
        response_var=args.response_var,
        input_csv=args.input_csv,
        precisions=prec_list,
    )
