"""Bootstrap confidence intervals for G-theory variance components.

Resamples items (the object of measurement) with replacement, preserving
all observations within each item. Each resample re-runs the full ANOVA
variance decomposition, producing an empirical distribution for every
variance component. Reports percentile-based 95% CIs.

Supports both the MVP 6-facet design and the exp-001 7-facet design
(with model as an additional crossed random facet).

Input:  JSONL data files (same format as model_facet_analysis.py).
Output: JSON with point estimates and bootstrap CIs for each component.
"""

import argparse
import glob
import json
from pathlib import Path

import numpy as np
import pandas as pd

from src.analysis.variance_decomposition import (
    compute_ss,
    compute_text_exact_match,
    estimate_variance_components,
)

FACETS_6 = [
    "precision", "temperature",
    "prompt_template", "seed", "ordering", "item_id",
]
FACETS_7 = [
    "model", "precision", "temperature",
    "prompt_template", "seed", "ordering", "item_id",
]


def load_jsonl_glob(patterns: list[str]) -> pd.DataFrame:
    """Load and concatenate JSONL files matching glob patterns.

    Args:
        patterns: File paths or glob patterns.

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


def detect_facets(df: pd.DataFrame) -> list[str]:
    """Auto-detect whether data has 6 or 7 facets based on column presence.

    Args:
        df: Input DataFrame.

    Returns:
        Facet list (FACETS_7 if 'model' column exists with >1 unique value,
        else FACETS_6).
    """
    if "model" in df.columns and df["model"].nunique() > 1:
        return FACETS_7
    return FACETS_6


def bootstrap_variance_components(
    df: pd.DataFrame,
    response: str,
    facets: list[str],
    n_bootstrap: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
) -> tuple[dict[str, float], dict[str, dict[str, float]]]:
    """Bootstrap CIs for variance components by resampling items.

    Each bootstrap iteration:
    1. Sample N items with replacement from the unique item_ids.
    2. Collect all observations for the sampled items, re-indexing item_id
       to maintain a balanced design.
    3. Run ANOVA and estimate variance components.

    Args:
        df: Full dataset with facet columns and response variable.
        response: Name of the response column.
        facets: List of facet names for the G-study.
        n_bootstrap: Number of bootstrap iterations.
        alpha: Significance level for CIs (default 0.05 -> 95% CI).
        seed: Random seed for reproducibility.

    Returns:
        (point_estimates, cis) where point_estimates maps component -> float,
        and cis maps component -> {"lower": float, "upper": float}.
    """
    # Point estimates from full data
    effects, n_levels = compute_ss(df, response, facets)
    point_est = estimate_variance_components(effects, facets, n_levels)

    rng = np.random.RandomState(seed)
    items = df["item_id"].unique()
    n_items = len(items)

    boot_vcs: list[dict[str, float]] = []
    n_failed = 0

    print(f"Bootstrap ({n_bootstrap} iterations, {n_items} items) ...")
    for i in range(n_bootstrap):
        sampled = rng.choice(items, size=n_items, replace=True)
        frames = []
        for new_idx, item in enumerate(sampled):
            sub = df[df["item_id"] == item].copy()
            sub["item_id"] = f"boot_{new_idx}"
            frames.append(sub)
        boot_df = pd.concat(frames, ignore_index=True)

        try:
            eff, nl = compute_ss(boot_df, response, facets)
            vc = estimate_variance_components(eff, facets, nl)
            boot_vcs.append(vc)
        except Exception:
            n_failed += 1
            continue

        if (i + 1) % 200 == 0:
            print(f"  ... {i + 1}/{n_bootstrap}")

    if n_failed > 0:
        print(f"  {n_failed}/{n_bootstrap} iterations failed (skipped)")

    lo_pct = 100 * alpha / 2
    hi_pct = 100 * (1 - alpha / 2)
    cis: dict[str, dict[str, float]] = {}
    for key in point_est:
        values = [bv.get(key, 0.0) for bv in boot_vcs]
        cis[key] = {
            "lower": float(np.percentile(values, lo_pct)),
            "upper": float(np.percentile(values, hi_pct)),
        }

    return point_est, cis


def run_bootstrap(
    data_patterns: list[str],
    output_path: str,
    response_var: str = "correct",
    n_bootstrap: int = 1000,
    seed: int = 42,
) -> dict:
    """Run bootstrap CI analysis and save results.

    Args:
        data_patterns: Glob patterns for input JSONL files.
        output_path: Destination JSON path.
        response_var: "correct" or "text_exact_match".
        n_bootstrap: Number of bootstrap iterations.
        seed: Random seed.

    Returns:
        Results dict (also written to output_path).
    """
    df = load_jsonl_glob(data_patterns)
    facets = detect_facets(df)

    for f in facets:
        df[f] = df[f].astype(str)

    if response_var == "text_exact_match":
        df = compute_text_exact_match(df)

    print(f"Facets: {facets} ({len(facets)}-facet design)")

    point_est, cis = bootstrap_variance_components(
        df, response_var, facets,
        n_bootstrap=n_bootstrap, seed=seed,
    )

    total_var = sum(point_est.values())
    results = {
        "variance_components": {
            k: {
                "estimate": v,
                "pct": v / total_var * 100 if total_var > 0 else 0.0,
                "ci_95": cis[k],
            }
            for k, v in point_est.items()
        },
        "total_variance": total_var,
        "n_observations": len(df),
        "facets": facets,
        "n_bootstrap": n_bootstrap,
        "response_var": response_var,
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as fout:
        json.dump(results, fout, indent=2)

    _print_summary(results)
    print(f"\n-> {output_path}")
    return results


def _print_summary(results: dict) -> None:
    """Print formatted table with point estimates and CIs."""
    vc = results["variance_components"]
    n_obs = results["n_observations"]
    n_boot = results["n_bootstrap"]
    n_facets = len(results["facets"])

    print(f"\nBootstrap Variance Components  ({n_obs} obs, {n_facets} facets, {n_boot} boots)")
    header = f"{'Component':<30} {'Estimate':>10} {'%':>8}  {'95% CI':>24}"
    print(header)
    print("-" * len(header))
    for name, info in sorted(vc.items(), key=lambda x: -x[1]["estimate"]):
        lo, hi = info["ci_95"]["lower"], info["ci_95"]["upper"]
        print(
            f"{name:<30} {info['estimate']:>10.6f} {info['pct']:>7.1f}%  "
            f"[{lo:.6f}, {hi:.6f}]"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Bootstrap CIs for G-theory variance components"
    )
    parser.add_argument(
        "--data", nargs="+", required=True,
        help="JSONL file(s) or glob pattern(s)",
    )
    parser.add_argument(
        "--response-var", default="correct",
        choices=["correct", "text_exact_match"],
        help="Response variable (default: correct)",
    )
    parser.add_argument(
        "--n-bootstrap", type=int, default=1000,
        help="Number of bootstrap iterations (default: 1000)",
    )
    parser.add_argument(
        "--seed", type=int, default=42,
        help="Random seed (default: 42)",
    )
    parser.add_argument(
        "--output", default="results/analysis/bootstrap_ci.json",
        help="Output JSON path",
    )
    args = parser.parse_args()
    run_bootstrap(args.data, args.output, args.response_var, args.n_bootstrap, args.seed)
