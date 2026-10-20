"""Leave-one-benchmark-out gradient robustness test.

For each of the 4 (or 5) benchmarks, remove it and check whether the
gradient pattern (item_id% decreasing, model:item_id% increasing) is
preserved on the remaining benchmarks.

Input:  exp-002 JSONL data
Output: results/analysis/leave_one_benchmark_out.json

Usage:
  python scripts/exp002_analysis/leave_one_benchmark_out.py --data-dir results/exp002
"""

import argparse
import json
import sys
import time
from itertools import combinations, permutations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
BENCHMARK_ORDER = ["mmlu", "arc", "hellaswag", "gsm8k"]


def load_exp002_data(data_dir: str) -> pd.DataFrame:
    data_path = Path(data_dir)
    jsonl_files = sorted(data_path.glob("*.jsonl"))
    if not jsonl_files:
        raise FileNotFoundError(f"No JSONL files in {data_dir}")
    frames = [pd.read_json(f, lines=True) for f in jsonl_files]
    df = pd.concat(frames, ignore_index=True)
    if "top_logprobs" in df.columns:
        df.drop(columns=["top_logprobs"], inplace=True)
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def compute_variance_pcts(df: pd.DataFrame, facets: list[str]) -> dict[str, float]:
    """Compute Henderson I variance component percentages."""
    grand_mean = df["correct"].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in facets}

    effects = {}
    for f in facets:
        group_means = df.groupby(f, observed=True)["correct"].mean()
        n_per = N // n_levels[f]
        ss = float(n_per * ((group_means - grand_mean) ** 2).sum())
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for fi, fj in combinations(facets, 2):
        cell_means = df.groupby([fi, fj], observed=True)["correct"].mean()
        main_fi = df.groupby(fi, observed=True)["correct"].mean()
        main_fj = df.groupby(fj, observed=True)["correct"].mean()
        n_per = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), cm in cell_means.items():
            interaction = cm - main_fi[li] - main_fj[lj] + grand_mean
            ss += n_per * interaction ** 2
        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        effects[f"{fi}:{fj}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((df["correct"] - grand_mean) ** 2).sum())
    ss_model_sum = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model_sum)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    vc = {}
    for fi, fj in combinations(facets, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in facets if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in facets:
        coeff_main = prod(n_levels[f] for f in facets if f != fi)
        interaction_contrib = 0.0
        for fj in facets:
            if fj == fi:
                continue
            int_key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(n_levels[f] for f in facets if f not in (fi, fj))
            interaction_contrib += coeff_ij * vc[int_key]
        raw = (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    total_var = sum(vc.values())
    return {k: v / total_var * 100 if total_var > 0 else 0.0 for k, v in vc.items()}


def is_monotonic_decreasing(vals: list[float]) -> bool:
    return all(a >= b for a, b in zip(vals, vals[1:]))


def is_monotonic_increasing(vals: list[float]) -> bool:
    return all(a <= b for a, b in zip(vals, vals[1:]))


def permutation_p_value(values: list[float], direction: str) -> float:
    check = is_monotonic_decreasing if direction == "decreasing" else is_monotonic_increasing
    all_perms = list(permutations(range(len(values))))
    n_match = sum(1 for p in all_perms if check([values[i] for i in p]))
    return n_match / len(all_perms)


def main():
    parser = argparse.ArgumentParser(description="Leave-one-benchmark-out gradient robustness")
    parser.add_argument("--data-dir", default="results/exp002")
    parser.add_argument("--output", default="results/analysis/leave_one_benchmark_out.json")
    args = parser.parse_args()

    t0 = time.time()
    df = load_exp002_data(args.data_dir)
    print(f"Loaded {len(df)} records ({time.time()-t0:.1f}s)", flush=True)

    available = [bm for bm in BENCHMARK_ORDER if bm in df["benchmark"].unique()]
    print(f"Benchmarks: {available}", flush=True)

    full_stats = {}
    for bm in available:
        df_bm = df[df["benchmark"] == bm].reset_index(drop=True)
        pcts = compute_variance_pcts(df_bm, FACETS)
        full_stats[bm] = {
            "item_id_pct": pcts.get("item_id", 0.0),
            "model_item_pct": pcts.get("model:item_id", 0.0),
        }

    full_item_vals = [full_stats[bm]["item_id_pct"] for bm in available]
    full_mi_vals = [full_stats[bm]["model_item_pct"] for bm in available]
    full_item_dec = is_monotonic_decreasing(full_item_vals)
    full_mi_inc = is_monotonic_increasing(full_mi_vals)

    print(f"\nFull set gradient:", flush=True)
    print(f"  item_id decreasing: {full_item_dec} {[f'{v:.2f}' for v in full_item_vals]}", flush=True)
    print(f"  model:item increasing: {full_mi_inc} {[f'{v:.2f}' for v in full_mi_vals]}", flush=True)

    lobo_results = {}
    for drop_bm in available:
        remaining = [bm for bm in available if bm != drop_bm]
        item_vals = [full_stats[bm]["item_id_pct"] for bm in remaining]
        mi_vals = [full_stats[bm]["model_item_pct"] for bm in remaining]

        item_dec = is_monotonic_decreasing(item_vals)
        mi_inc = is_monotonic_increasing(mi_vals)

        p_item = permutation_p_value(item_vals, "decreasing")
        p_mi = permutation_p_value(mi_vals, "increasing")

        lobo_results[drop_bm] = {
            "dropped": drop_bm,
            "remaining": remaining,
            "item_id_pct_values": {bm: round(full_stats[bm]["item_id_pct"], 4) for bm in remaining},
            "model_item_pct_values": {bm: round(full_stats[bm]["model_item_pct"], 4) for bm in remaining},
            "item_id_monotonic_decreasing": item_dec,
            "model_item_monotonic_increasing": mi_inc,
            "both_preserved": item_dec and mi_inc,
            "p_item_decreasing": round(p_item, 6),
            "p_model_item_increasing": round(p_mi, 6),
        }

        status = "PRESERVED" if (item_dec and mi_inc) else "BROKEN"
        print(f"\n  Drop {drop_bm}: {status}", flush=True)
        print(f"    item_id dec: {item_dec} (p={p_item:.4f}), model:item inc: {mi_inc} (p={p_mi:.4f})", flush=True)

    n_preserved = sum(1 for r in lobo_results.values() if r["both_preserved"])

    output = {
        "experiment": "exp-002",
        "analysis": "leave_one_benchmark_out",
        "benchmark_order": available,
        "full_set": {
            "item_id_monotonic_decreasing": full_item_dec,
            "model_item_monotonic_increasing": full_mi_inc,
            "benchmark_stats": {
                bm: {k: round(v, 4) for k, v in full_stats[bm].items()}
                for bm in available
            },
        },
        "lobo_results": lobo_results,
        "summary": {
            "n_benchmarks": len(available),
            "n_drops": len(lobo_results),
            "n_gradient_preserved": n_preserved,
            "gradient_robust": n_preserved == len(lobo_results),
        },
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nSummary: gradient preserved in {n_preserved}/{len(lobo_results)} drops", flush=True)
    print(f"Runtime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {args.output}", flush=True)


if __name__ == "__main__":
    main()
