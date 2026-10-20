"""G-theory variance decomposition for LLM evaluation.

Estimates variance components for all 6 facets (main effects) and all
15 two-way interactions using ANOVA-based estimation (Henderson Method I)
for balanced fully-crossed designs.  Higher-order interactions (≥3-way) are
absorbed into the residual.

Estimation treats all facets as random (standard G-study practice).  The
fixed/random distinction is used downstream in the D-study to partition
universe-score variance from error variance.

Bootstrap 95 %% CIs are computed by resampling items with replacement.

Facets
------
precision, temperature                    — fixed  (in D-study)
prompt_template, seed, ordering, item_id  — random (in D-study)

Input:  JSONL from ``run_experiment.py`` (one row per item × condition).
Output: JSON with ANOVA table, variance components, and bootstrap CIs.
"""

import argparse
import json
from itertools import combinations
from math import prod
from pathlib import Path
from collections import Counter
from typing import Optional

import numpy as np
import pandas as pd

ALL_FACETS = [
    "precision", "temperature",
    "prompt_template", "seed", "ordering", "item_id",
]
FIXED_FACETS = ["precision", "temperature"]
RANDOM_FACETS = ["prompt_template", "seed", "ordering", "item_id"]


# ---------------------------------------------------------------------------
# ANOVA helpers
# ---------------------------------------------------------------------------

def compute_ss(
    df: pd.DataFrame,
    response: str,
    facets: list[str],
) -> tuple[dict, dict[str, int]]:
    """Compute Type-I sums of squares for main effects and 2-way interactions.

    For a balanced design, Type I = Type III, so the order of terms does not
    matter.

    Returns:
        (effects_dict, n_levels_dict) where each effect entry has keys
        ``ss``, ``df``, ``ms``.
    """
    grand_mean = df[response].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in facets}

    effects: dict = {}

    # --- main effects ---
    for f in facets:
        group_means = df.groupby(f, observed=True)[response].mean()
        n_per_group = N // n_levels[f]
        ss = float(n_per_group * ((group_means - grand_mean) ** 2).sum())
        df_eff = n_levels[f] - 1
        effects[f] = {
            "ss": ss,
            "df": df_eff,
            "ms": ss / df_eff if df_eff > 0 else 0.0,
        }

    # --- 2-way interactions ---
    for fi, fj in combinations(facets, 2):
        cell_means = df.groupby([fi, fj], observed=True)[response].mean()
        main_fi = df.groupby(fi, observed=True)[response].mean()
        main_fj = df.groupby(fj, observed=True)[response].mean()
        n_per_cell = N // (n_levels[fi] * n_levels[fj])

        ss = 0.0
        for (li, lj), cell_mean in cell_means.items():
            interaction = cell_mean - main_fi[li] - main_fj[lj] + grand_mean
            ss += n_per_cell * interaction ** 2

        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        key = f"{fi}:{fj}"
        effects[key] = {
            "ss": ss,
            "df": df_eff,
            "ms": ss / df_eff if df_eff > 0 else 0.0,
        }

    # --- residual (confounds ≥3-way interactions) ---
    ss_total = float(((df[response] - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {
        "ss": ss_res,
        "df": df_res,
        "ms": ss_res / df_res if df_res > 0 else 0.0,
    }

    return effects, n_levels


def estimate_variance_components(
    effects: dict,
    facets: list[str],
    n_levels: dict[str, int],
) -> dict[str, float]:
    """Solve EMS equations for variance components.

    For a balanced crossed design with all-random facets and effects up to
    2-way interactions:

    * 2-way σ²_{ij} = (MS_{ij} − MS_res) / ∏_{k∉{i,j}} n_k
    * main  σ²_i    = (MS_i − ∑_j c_{ij} σ²_{ij} − MS_res) / ∏_{k≠i} n_k

    Negative estimates are truncated to zero.
    """
    ms_res = effects["residual"]["ms"]
    vc: dict[str, float] = {}

    # --- 2-way interactions first ---
    for fi, fj in combinations(facets, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in facets if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    # --- main effects (require 2-way estimates) ---
    for fi in facets:
        coeff_main = prod(n_levels[f] for f in facets if f != fi)
        interaction_contrib = 0.0
        for fj in facets:
            if fj == fi:
                continue
            int_key = (
                f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            )
            coeff_ij = prod(
                n_levels[f] for f in facets if f not in (fi, fj)
            )
            interaction_contrib += coeff_ij * vc[int_key]

        raw = (
            (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main
            if coeff_main > 0
            else 0.0
        )
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc


# ---------------------------------------------------------------------------
# Bootstrap
# ---------------------------------------------------------------------------

def bootstrap_ci(
    df: pd.DataFrame,
    response: str,
    facets: list[str],
    n_bootstrap: int = 1000,
    alpha: float = 0.05,
    seed: int = 42,
) -> dict[str, dict[str, float]]:
    """Bootstrap 95 % CIs for variance components by resampling items.

    Each bootstrap sample draws 50 items with replacement, assigns unique
    item IDs, re-runs the full ANOVA, and records variance components.
    """
    rng = np.random.RandomState(seed)
    items = df["item_id"].unique()
    n_items = len(items)

    boot_vcs: list[dict[str, float]] = []
    for _ in range(n_bootstrap):
        sampled = rng.choice(items, size=n_items, replace=True)
        frames = []
        for new_idx, item in enumerate(sampled):
            sub = df[df["item_id"] == item].copy()
            sub["item_id"] = f"boot_{new_idx}"
            frames.append(sub)
        boot_df = pd.concat(frames, ignore_index=True)

        eff, nl = compute_ss(boot_df, response, facets)
        vc = estimate_variance_components(eff, facets, nl)
        boot_vcs.append(vc)

    ci: dict[str, dict[str, float]] = {}
    for key in boot_vcs[0]:
        values = [bv[key] for bv in boot_vcs]
        ci[key] = {
            "lower": float(np.percentile(values, 100 * alpha / 2)),
            "upper": float(np.percentile(values, 100 * (1 - alpha / 2))),
        }
    return ci


# ---------------------------------------------------------------------------
# Text exact match
# ---------------------------------------------------------------------------

def compute_text_exact_match(df: pd.DataFrame) -> pd.DataFrame:
    """Add ``text_exact_match`` column (0/1) to *df*.

    For each item_id the canonical text is the most frequent generated_text
    across all conditions.  A record scores 1 iff its generated_text equals
    the canonical text for that item.
    """
    canonical = (
        df.groupby("item_id")["generated_text"]
        .agg(lambda texts: Counter(texts).most_common(1)[0][0])
    )
    df = df.copy()
    df["text_exact_match"] = (
        df.apply(lambda r: int(r["generated_text"] == canonical[r["item_id"]]), axis=1)
    )
    return df


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def run_analysis(
    input_path: str,
    output_path: str,
    n_bootstrap: int = 1000,
    response_var: str = "correct",
) -> dict:
    """Full G-theory analysis: ANOVA → variance components → bootstrap CIs.

    Args:
        input_path: JSONL from ``run_experiment.py``.
        output_path: Destination JSON.
        n_bootstrap: Number of bootstrap iterations (default 1000).
        response_var: Response variable — ``"correct"`` or ``"text_exact_match"``.

    Returns:
        Results dict (also written to ``output_path``).
    """
    df = pd.read_json(input_path, lines=True)

    for f in ALL_FACETS:
        df[f] = df[f].astype(str)

    if response_var == "text_exact_match":
        df = compute_text_exact_match(df)

    print(f"Running G-study on {len(df)} observations (response={response_var}) …")

    effects, n_levels = compute_ss(df, response_var, ALL_FACETS)
    vc = estimate_variance_components(effects, ALL_FACETS, n_levels)

    print(f"Bootstrapping ({n_bootstrap} iterations) …")
    ci = bootstrap_ci(df, response_var, ALL_FACETS, n_bootstrap=n_bootstrap)

    total_var = sum(vc.values())
    results = {
        "variance_components": {
            k: {
                "estimate": v,
                "pct": v / total_var * 100 if total_var > 0 else 0.0,
                "ci_95": ci[k],
            }
            for k, v in vc.items()
        },
        "total_variance": total_var,
        "n_observations": len(df),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "fixed_facets": FIXED_FACETS,
        "random_facets": RANDOM_FACETS,
        "anova_table": {
            k: {"ss": v["ss"], "df": v["df"], "ms": v["ms"]}
            for k, v in effects.items()
        },
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    # --- print summary ---
    print(
        f"\nG-theory Variance Decomposition  "
        f"({len(df)} obs, {len(ALL_FACETS)} facets)"
    )
    header = f"{'Component':<30} {'Estimate':>10} {'%':>8}  {'95% CI':>24}"
    print(header)
    print("-" * len(header))
    for name, info in sorted(
        results["variance_components"].items(),
        key=lambda x: -x[1]["estimate"],
    ):
        lo, hi = info["ci_95"]["lower"], info["ci_95"]["upper"]
        print(
            f"{name:<30} {info['estimate']:>10.6f} {info['pct']:>7.1f}%  "
            f"[{lo:.6f}, {hi:.6f}]"
        )

    print(f"\n→ {output_path}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="G-theory variance decomposition"
    )
    parser.add_argument(
        "--input", required=True, help="Path to experiment results JSONL"
    )
    parser.add_argument("--output", default=None)
    parser.add_argument("--n-bootstrap", type=int, default=1000)
    parser.add_argument(
        "--response-var",
        default="correct",
        choices=["correct", "text_exact_match"],
        help="Response variable: 'correct' (binary accuracy) or 'text_exact_match' (text-level determinism)",
    )
    args = parser.parse_args()

    if args.output is None:
        if args.response_var == "text_exact_match":
            args.output = "results/variance_components_text.json"
        else:
            args.output = "results/variance_components.json"

    run_analysis(args.input, args.output, args.n_bootstrap, args.response_var)
