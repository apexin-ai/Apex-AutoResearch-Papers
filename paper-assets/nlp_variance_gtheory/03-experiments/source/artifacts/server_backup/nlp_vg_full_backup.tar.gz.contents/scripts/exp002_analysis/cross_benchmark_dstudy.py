"""Cross-benchmark D-study comparison.

For each benchmark, computes:
  - D-study curves (item count vs G coefficient)
  - Minimum items needed for G >= 0.80 / 0.90 / 0.95

Input:  exp-002 JSONL data
Output: results/analysis/cross_benchmark_dstudy.json

Usage:
  python scripts/exp002_analysis/cross_benchmark_dstudy.py --data-dir results/exp002
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
BENCHMARKS = ["mmlu", "arc", "hellaswag", "gsm8k"]
ITEM_COUNTS = [10, 25, 50, 75, 100, 150, 200, 300, 500, 750, 1000]
G_TARGETS = [0.80, 0.90, 0.95]


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


def compute_henderson_i(df: pd.DataFrame, facets: list[str]) -> tuple[dict, dict]:
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
    return vc, {k: int(v) for k, v in n_levels.items()}


def compute_g_for_n_items(vc: dict, n_levels: dict, n_items: int) -> float:
    """Compute G_item for a given number of items (D-study projection).

    Uses the correct formula: scale error by n_actual/n_items.
    """
    sigma_item = vc.get("item_id", 0.0)
    n_actual = n_levels["item_id"]
    non_item = [f for f in FACETS if f != "item_id"]

    sigma_delta_actual = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            sigma_delta_actual += est / prod(n_levels[f] for f in non_item)
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        sigma_delta_actual += est / (prod(n_levels[f] for f in other) if other else 1)

    sigma_delta_n = sigma_delta_actual * (n_actual / n_items)
    total = sigma_item + sigma_delta_n
    return sigma_item / total if total > 0 else 0.0


def find_min_items(vc: dict, n_levels: dict, target_g: float, max_items: int = 5000) -> int | None:
    for ni in range(1, max_items + 1):
        g = compute_g_for_n_items(vc, n_levels, ni)
        if g >= target_g:
            return ni
    return None


def main():
    parser = argparse.ArgumentParser(description="Cross-benchmark D-study comparison")
    parser.add_argument("--data-dir", default="results/exp002")
    parser.add_argument("--output", default="results/analysis/cross_benchmark_dstudy.json")
    args = parser.parse_args()

    t0 = time.time()
    df = load_exp002_data(args.data_dir)
    print(f"Loaded {len(df)} records ({time.time()-t0:.1f}s)", flush=True)

    results = {}
    for bm in BENCHMARKS:
        df_bm = df[df["benchmark"] == bm].reset_index(drop=True)
        if len(df_bm) == 0:
            print(f"WARNING: no data for '{bm}', skipping", flush=True)
            continue

        vc, n_levels = compute_henderson_i(df_bm, FACETS)
        total_var = sum(vc.values())

        curve = {}
        for ni in ITEM_COUNTS:
            g = compute_g_for_n_items(vc, n_levels, ni)
            curve[ni] = round(g, 6)

        min_items = {}
        for target in G_TARGETS:
            n = find_min_items(vc, n_levels, target)
            min_items[str(target)] = n

        g_current = compute_g_for_n_items(vc, n_levels, n_levels["item_id"])

        results[bm] = {
            "n_items_actual": n_levels["item_id"],
            "G_current": round(g_current, 6),
            "item_id_pct": round(vc.get("item_id", 0) / total_var * 100 if total_var > 0 else 0, 4),
            "d_study_curve": curve,
            "min_items_for_G": min_items,
            "accuracy": round(float(df_bm["correct"].mean()), 6),
        }

        print(f"\n{bm}: G_current={g_current:.4f}, acc={df_bm['correct'].mean():.4f}", flush=True)
        print(f"  min items: G>=0.80={min_items.get('0.8')}, G>=0.90={min_items.get('0.9')}, G>=0.95={min_items.get('0.95')}", flush=True)

    output = {
        "experiment": "exp-002",
        "analysis": "cross_benchmark_dstudy",
        "facets": FACETS,
        "item_counts_evaluated": ITEM_COUNTS,
        "g_targets": G_TARGETS,
        "benchmarks": results,
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*70}", flush=True)
    print(f"{'Benchmark':<12} {'n_items':>8} {'G_curr':>8} {'min(.80)':>9} {'min(.90)':>9} {'min(.95)':>9}", flush=True)
    print("-" * 58, flush=True)
    for bm in results:
        r = results[bm]
        m80 = str(r["min_items_for_G"].get("0.8", ">5000"))
        m90 = str(r["min_items_for_G"].get("0.9", ">5000"))
        m95 = str(r["min_items_for_G"].get("0.95", ">5000"))
        print(f"{bm:<12} {r['n_items_actual']:>8} {r['G_current']:>8.4f} {m80:>9} {m90:>9} {m95:>9}", flush=True)

    print(f"\nRuntime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {args.output}", flush=True)


if __name__ == "__main__":
    main()
