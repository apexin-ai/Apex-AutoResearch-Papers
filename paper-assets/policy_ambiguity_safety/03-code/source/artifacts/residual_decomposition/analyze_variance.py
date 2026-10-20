#!/usr/bin/env python3
"""Analyze replicated episodes for residual variance decomposition.

Decomposes the 60.8% residual variance into:
  - Within-cell stochasticity (conversation trajectory randomness)
  - Systematic-but-unmeasured factors (cell identity effect)

Uses ICC(1) on binary violation outcomes grouped by cell
(clause_id × condition × model), with 5 reps per cell.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config

ARTIFACTS_DIR = Path(__file__).resolve().parent
VIOLATION_THRESHOLD = config.VIOLATION_BINARY_THRESHOLD  # "moderate"
VIOLATION_POSITIVE = {"moderate", "critical"}


def load_judgments(data_dir: Path) -> list[dict]:
    judgments = []
    for f in data_dir.glob("judgments*.jsonl"):
        with open(f) as fh:
            for line in fh:
                if line.strip():
                    judgments.append(json.loads(line))
    return judgments


def to_binary(judgment: dict) -> int:
    level = judgment["judgment"]["violation_level"]
    return 1 if level in VIOLATION_POSITIVE else 0


def build_cells(judgments: list[dict]) -> dict[str, list[int]]:
    """Group binary outcomes by cell key (clause_id|condition|model)."""
    cells: dict[str, list[int]] = defaultdict(list)
    for j in judgments:
        key = f"{j['clause_id']}|{j['condition']}|{j['model']}"
        cells[key].append(to_binary(j))
    return dict(cells)


def icc1(cells: dict[str, list[int]]) -> dict:
    """Compute ICC(1) for binary outcomes across cells.

    ICC(1) = (MS_between - MS_within) / (MS_between + (k-1)*MS_within)

    Returns dict with ICC, variance components, and interpretation.
    """
    cell_keys = sorted(cells.keys())
    n_cells = len(cell_keys)

    ks = [len(cells[k]) for k in cell_keys]
    if len(set(ks)) == 1:
        k = ks[0]
        balanced = True
    else:
        k = np.mean(ks)
        balanced = False

    cell_means = []
    ss_within = 0.0
    n_total = 0

    for key in cell_keys:
        outcomes = np.array(cells[key], dtype=float)
        cell_mean = outcomes.mean()
        cell_means.append(cell_mean)
        ss_within += np.sum((outcomes - cell_mean) ** 2)
        n_total += len(outcomes)

    cell_means = np.array(cell_means)
    grand_mean = np.mean(cell_means) if balanced else sum(
        cells[k][i] for k in cell_keys for i in range(len(cells[k]))
    ) / n_total

    df_between = n_cells - 1
    df_within = n_total - n_cells

    if balanced:
        ss_between = k * np.sum((cell_means - grand_mean) ** 2)
    else:
        ss_between = sum(
            len(cells[key]) * (cell_means[i] - grand_mean) ** 2
            for i, key in enumerate(cell_keys)
        )

    ms_between = ss_between / df_between if df_between > 0 else 0
    ms_within = ss_within / df_within if df_within > 0 else 0

    k_eff = k if balanced else np.mean(ks)
    icc_val = (ms_between - ms_within) / (ms_between + (k_eff - 1) * ms_within) \
        if (ms_between + (k_eff - 1) * ms_within) > 0 else 0.0

    sigma2_within = ms_within
    sigma2_between = max(0, (ms_between - ms_within) / k_eff)
    sigma2_total = sigma2_between + sigma2_within

    stochastic_share = sigma2_within / sigma2_total if sigma2_total > 0 else 0
    systematic_share = sigma2_between / sigma2_total if sigma2_total > 0 else 0

    return {
        "icc1": round(float(icc_val), 4),
        "n_cells": n_cells,
        "k_per_cell": round(float(k_eff), 1),
        "n_total": n_total,
        "grand_mean_violation_rate": round(float(grand_mean), 4),
        "ms_between": round(float(ms_between), 6),
        "ms_within": round(float(ms_within), 6),
        "sigma2_within": round(float(sigma2_within), 6),
        "sigma2_between": round(float(sigma2_between), 6),
        "sigma2_total": round(float(sigma2_total), 6),
        "stochastic_share": round(float(stochastic_share), 4),
        "systematic_share": round(float(systematic_share), 4),
        "balanced": balanced,
    }


def condition_breakdown(judgments: list[dict]) -> dict:
    """ICC separately for ambiguous and unambiguous conditions."""
    by_cond = defaultdict(list)
    for j in judgments:
        by_cond[j["condition"]].append(j)

    results = {}
    for cond, jdgs in by_cond.items():
        cells = build_cells(jdgs)
        results[cond] = icc1(cells)
    return results


def type_breakdown(judgments: list[dict]) -> dict:
    """ICC separately per ambiguity type."""
    by_type = defaultdict(list)
    for j in judgments:
        by_type[j["ambiguity_type"]].append(j)

    results = {}
    for atype, jdgs in sorted(by_type.items()):
        cells = build_cells(jdgs)
        if len(cells) >= 3:
            results[atype] = icc1(cells)
    return results


def cell_consistency_stats(cells: dict[str, list[int]]) -> dict:
    """Descriptive stats on within-cell consistency."""
    unanimous_same = 0
    all_zero = 0
    all_one = 0
    mixed = 0

    cell_variances = []
    for key, outcomes in cells.items():
        arr = np.array(outcomes, dtype=float)
        v = np.var(arr, ddof=1) if len(arr) > 1 else 0.0
        cell_variances.append(v)

        if v == 0:
            unanimous_same += 1
            if arr[0] == 0:
                all_zero += 1
            else:
                all_one += 1
        else:
            mixed += 1

    return {
        "n_cells": len(cells),
        "unanimous_cells": unanimous_same,
        "unanimous_no_violation": all_zero,
        "unanimous_violation": all_one,
        "mixed_cells": mixed,
        "pct_unanimous": round(unanimous_same / len(cells) * 100, 1) if cells else 0,
        "mean_within_cell_variance": round(float(np.mean(cell_variances)), 4),
        "median_within_cell_variance": round(float(np.median(cell_variances)), 4),
    }


def map_to_original_residual(icc_result: dict, original_residual_pct: float = 60.8) -> dict:
    """Map ICC decomposition back to the original variance decomposition."""
    stoch = icc_result["stochastic_share"]
    syst = icc_result["systematic_share"]
    return {
        "original_residual_pct": original_residual_pct,
        "stochastic_pct_of_total": round(original_residual_pct * stoch, 1),
        "systematic_unmeasured_pct_of_total": round(original_residual_pct * syst, 1),
        "interpretation": (
            f"Of the {original_residual_pct}% residual variance, "
            f"~{original_residual_pct * stoch:.1f}pp is run-to-run stochasticity "
            f"and ~{original_residual_pct * syst:.1f}pp is systematic-but-unmeasured factors."
        ),
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Residual variance decomposition analysis")
    parser.add_argument("--data-dir", default=str(ARTIFACTS_DIR))
    parser.add_argument("--output", default=str(ARTIFACTS_DIR / "results.json"))
    parser.add_argument("--original-residual", type=float, default=60.8)
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    judgments = load_judgments(data_dir)

    if not judgments:
        print(f"No judgments found in {data_dir}")
        sys.exit(1)

    print(f"Loaded {len(judgments)} judgments")

    cells = build_cells(judgments)
    print(f"Cells (clause×condition×model): {len(cells)}")

    # ── Overall ICC ──
    overall = icc1(cells)
    print(f"\nOverall ICC(1) = {overall['icc1']:.4f}")
    print(f"  σ²_within (stochastic) = {overall['sigma2_within']:.4f}")
    print(f"  σ²_between (systematic) = {overall['sigma2_between']:.4f}")
    print(f"  Stochastic share = {overall['stochastic_share']:.1%}")
    print(f"  Systematic share = {overall['systematic_share']:.1%}")

    # ── Cell consistency ──
    consistency = cell_consistency_stats(cells)
    print(f"\nCell consistency:")
    print(f"  Unanimous cells: {consistency['unanimous_cells']}/{consistency['n_cells']} "
          f"({consistency['pct_unanimous']}%)")
    print(f"    All no-violation: {consistency['unanimous_no_violation']}")
    print(f"    All violation: {consistency['unanimous_violation']}")
    print(f"  Mixed cells: {consistency['mixed_cells']}")

    # ── By condition ──
    by_condition = condition_breakdown(judgments)
    print(f"\nBy condition:")
    for cond, res in by_condition.items():
        print(f"  {cond}: ICC={res['icc1']:.4f}, "
              f"stochastic={res['stochastic_share']:.1%}, "
              f"violation_rate={res['grand_mean_violation_rate']:.1%}")

    # ── By ambiguity type ──
    by_type = type_breakdown(judgments)
    print(f"\nBy ambiguity type:")
    for atype, res in by_type.items():
        print(f"  {atype}: ICC={res['icc1']:.4f}, "
              f"stochastic={res['stochastic_share']:.1%}, "
              f"violation_rate={res['grand_mean_violation_rate']:.1%}")

    # ── Map to original residual ──
    mapping = map_to_original_residual(overall, args.original_residual)
    print(f"\n{mapping['interpretation']}")

    # ── Save results ──
    results = {
        "overall_icc": overall,
        "cell_consistency": consistency,
        "by_condition": by_condition,
        "by_ambiguity_type": by_type,
        "residual_mapping": mapping,
        "metadata": {
            "n_judgments": len(judgments),
            "n_cells": len(cells),
            "violation_threshold": VIOLATION_THRESHOLD,
            "original_residual_pct": args.original_residual,
        },
    }

    output_path = Path(args.output)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
