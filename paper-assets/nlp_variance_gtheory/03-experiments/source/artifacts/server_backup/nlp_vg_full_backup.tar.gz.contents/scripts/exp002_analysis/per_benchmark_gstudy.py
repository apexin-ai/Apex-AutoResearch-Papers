"""Per-benchmark Henderson I variance decomposition for exp-002.

Input:  Merged exp-002 JSONL (4 models x 4 benchmarks x bf16 x 2 temps x 6 prompts x 6 seeds x 4 orderings).
Output: results/analysis/exp002_per_benchmark_gstudy.json
        — per-benchmark variance components, G_item, D-study projections.

Facets (7, within each benchmark):
  model, temperature, prompt_template, seed, ordering, item_id
  + all 2-way interactions. Residual absorbs >=3-way.

Usage:
  python scripts/exp002_analysis/per_benchmark_gstudy.py --data-dir results/exp002
"""

import argparse
import json
import sys
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
BENCHMARKS = ["mmlu", "gsm8k", "arc", "hellaswag"]


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


def compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]):
    """Henderson Method I: SS -> EMS -> variance components."""
    grand_mean = df[response].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in facets}

    effects = {}

    for f in facets:
        group_means = df.groupby(f, observed=True)[response].mean()
        n_per = N // n_levels[f]
        ss = float(n_per * ((group_means - grand_mean) ** 2).sum())
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for fi, fj in combinations(facets, 2):
        cell_means = df.groupby([fi, fj], observed=True)[response].mean()
        main_fi = df.groupby(fi, observed=True)[response].mean()
        main_fj = df.groupby(fj, observed=True)[response].mean()
        n_per = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), cm in cell_means.items():
            interaction = cm - main_fi[li] - main_fj[lj] + grand_mean
            ss += n_per * interaction ** 2
        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        effects[f"{fi}:{fj}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((df[response] - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
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
    return vc, n_levels, effects


def compute_g_item(vc: dict, n_levels: dict) -> tuple[float, float, float]:
    """G_item: object of measurement = item_id.

    sigma_tau = sigma^2(item_id)
    sigma_delta = sum of X:item_id / n_X terms + residual / prod(n_X for X != item_id)
    """
    sigma_item = vc.get("item_id", 0.0)
    non_item_facets = [f for f in FACETS if f != "item_id"]

    sigma_delta = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            divisor = prod(n_levels[f] for f in non_item_facets)
            sigma_delta += est / divisor
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = prod(n_levels[f] for f in other) if other else 1
        sigma_delta += est / divisor

    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return g, sigma_item, sigma_delta


def d_study_curve(vc: dict, n_levels: dict, item_counts: list[int]) -> dict:
    """D-study: vary n_items, hold other facets at actual levels."""
    non_item_facets = [f for f in FACETS if f != "item_id"]
    sigma_item = vc.get("item_id", 0.0)
    n_actual = n_levels["item_id"]

    non_item_error = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            divisor = prod(n_levels[f] for f in non_item_facets)
            non_item_error += est / divisor
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = prod(n_levels[f] for f in other) if other else 1
        non_item_error += est / divisor

    curve = {}
    for ni in item_counts:
        ratio = n_actual / ni
        sigma_delta_ni = non_item_error * ratio
        g_ni = sigma_item / (sigma_item + sigma_delta_ni) if (sigma_item + sigma_delta_ni) > 0 else 0.0
        curve[ni] = round(g_ni, 6)
    return curve


def find_min_items_for_g(vc: dict, n_levels: dict, target_g: float, max_items: int = 2000) -> int | None:
    non_item_facets = [f for f in FACETS if f != "item_id"]
    sigma_item = vc.get("item_id", 0.0)
    n_actual = n_levels["item_id"]

    non_item_error = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            divisor = prod(n_levels[f] for f in non_item_facets)
            non_item_error += est / divisor
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        divisor = prod(n_levels[f] for f in other) if other else 1
        non_item_error += est / divisor

    for ni in range(1, max_items + 1):
        ratio = n_actual / ni
        sigma_delta_ni = non_item_error * ratio
        g = sigma_item / (sigma_item + sigma_delta_ni) if (sigma_item + sigma_delta_ni) > 0 else 0.0
        if g >= target_g:
            return ni
    return None


def analyze_benchmark(df_bm: pd.DataFrame, benchmark: str) -> dict:
    print(f"\n{'='*60}", flush=True)
    print(f"Benchmark: {benchmark} ({len(df_bm)} obs)", flush=True)

    vc, n_levels, effects = compute_henderson_i(df_bm, "correct", FACETS)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)

    print(f"  G_item = {g_item:.6f}", flush=True)
    print(f"  item_id% = {vc.get('item_id', 0) / total_var * 100:.2f}%", flush=True)
    print(f"  model:item_id% = {vc.get('model:item_id', 0) / total_var * 100:.2f}%", flush=True)

    item_counts = [25, 50, 75, 100, 150, 200, 300, 500, 1000]
    d_curve = d_study_curve(vc, n_levels, item_counts)
    min_80 = find_min_items_for_g(vc, n_levels, 0.80)

    return {
        "benchmark": benchmark,
        "n_observations": len(df_bm),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean_accuracy": round(float(df_bm["correct"].mean()), 6),
        "variance_components": {
            k: {"estimate": round(v, 10), "pct": round(v / total_var * 100, 4) if total_var > 0 else 0.0}
            for k, v in sorted(vc.items(), key=lambda x: -x[1])
        },
        "total_variance": round(total_var, 10),
        "G_item": round(g_item, 6),
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
        "d_study_curve": d_curve,
        "min_items_G_0.80": min_80,
    }


def main():
    parser = argparse.ArgumentParser(description="Per-benchmark Henderson I G-study for exp-002")
    parser.add_argument("--data-dir", default="results/exp002", help="Directory containing exp-002 JSONL files")
    parser.add_argument("--output", default="results/analysis/exp002_per_benchmark_gstudy.json")
    args = parser.parse_args()

    t0 = time.time()
    df = load_exp002_data(args.data_dir)
    print(f"Loaded {len(df)} records ({time.time()-t0:.1f}s)", flush=True)
    print(f"Benchmarks: {sorted(df['benchmark'].unique())}", flush=True)
    print(f"Models: {sorted(df['model'].unique())}", flush=True)

    results = {}
    for bm in BENCHMARKS:
        df_bm = df[df["benchmark"] == bm].reset_index(drop=True)
        if len(df_bm) == 0:
            print(f"WARNING: no data for benchmark '{bm}', skipping", flush=True)
            continue
        results[bm] = analyze_benchmark(df_bm, bm)

    summary = {
        "gradient_check": {
            bm: results[bm]["variance_components"].get("item_id", {}).get("pct", 0)
            for bm in results
        },
        "g_item_by_benchmark": {bm: results[bm]["G_item"] for bm in results},
    }

    output = {
        "experiment": "exp-002",
        "analysis": "per_benchmark_henderson_i_gstudy",
        "facets": FACETS,
        "benchmarks": results,
        "summary": summary,
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n{'='*60}", flush=True)
    print("SUMMARY", flush=True)
    print(f"{'Benchmark':<12} {'item_id%':>10} {'model:item%':>12} {'G_item':>8} {'min_n(G>=.80)':>14}", flush=True)
    for bm in results:
        r = results[bm]
        item_pct = r["variance_components"].get("item_id", {}).get("pct", 0)
        mi_pct = r["variance_components"].get("model:item_id", {}).get("pct", 0)
        min_n = r["min_items_G_0.80"]
        print(f"{bm:<12} {item_pct:>9.2f}% {mi_pct:>11.2f}% {r['G_item']:>8.4f} {str(min_n):>14}", flush=True)

    print(f"\nTotal runtime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {args.output}", flush=True)


if __name__ == "__main__":
    main()
