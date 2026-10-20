"""Gradient permutation test across benchmarks.

Tests whether item_id% monotonically decreases (and model:item_id% monotonically
increases) across benchmarks ordered by cognitive complexity, using Spearman rho
as the test statistic with an exact permutation test.

Input:  Per-benchmark G-study results (exp-002) + optionally exp-001 MMLU results.
Output: results/analysis/gradient_permutation_test.json

Usage:
  python scripts/exp002_analysis/gradient_permutation_test.py --data-dir results/exp002
  python scripts/exp002_analysis/gradient_permutation_test.py --data-dir results/exp002 --exp001-gstudy results/analysis/exp001_gstudy.json
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
from scipy.stats import spearmanr, kendalltau

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]

BENCHMARK_ORDER = ["mmlu", "arc", "hellaswag", "gsm8k", "math"]


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


def compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]) -> dict:
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
    pct = {k: v / total_var * 100 if total_var > 0 else 0.0 for k, v in vc.items()}
    return {"vc": vc, "pct": pct, "n_levels": n_levels, "total_var": total_var}


def spearman_permutation_test(values_by_benchmark: dict[str, float],
                              benchmark_order: list[str],
                              direction: str) -> dict:
    """Exact permutation test using Spearman rho as the test statistic.

    direction: "decreasing" (expect negative rho) or "increasing" (expect positive rho)
    """
    ordered_values = [values_by_benchmark[bm] for bm in benchmark_order]
    positions = list(range(len(ordered_values)))

    rho_obs, _ = spearmanr(positions, ordered_values)
    tau_obs, tau_p_asymptotic = kendalltau(positions, ordered_values)

    all_perms = list(permutations(ordered_values))
    n_total = len(all_perms)

    if direction == "decreasing":
        # H1: rho < 0, count permutations with rho <= observed
        n_extreme = sum(1 for perm in all_perms if spearmanr(positions, perm)[0] <= rho_obs)
    else:
        # H1: rho > 0, count permutations with rho >= observed
        n_extreme = sum(1 for perm in all_perms if spearmanr(positions, perm)[0] >= rho_obs)

    p_value = n_extreme / n_total

    return {
        "observed_order": benchmark_order,
        "observed_values": [round(v, 4) for v in ordered_values],
        "observed_rho": round(float(rho_obs), 6),
        "direction": direction,
        "n_permutations": n_total,
        "n_extreme": n_extreme,
        "p_value": round(p_value, 6),
        "significant_at_0.05": p_value <= 0.05,
        "kendall_tau": round(float(tau_obs), 6),
        "kendall_p": round(float(tau_p_asymptotic), 6),
    }


def load_exp001_gstudy(path: str) -> dict | None:
    p = Path(path)
    if not p.exists():
        return None
    with open(p) as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Gradient permutation test across benchmarks")
    parser.add_argument("--data-dir", default="results/exp002", help="Directory with exp-002 JSONL files")
    parser.add_argument("--exp001-gstudy", default=None, help="Path to exp-001 G-study JSON (optional, for 5th benchmark)")
    parser.add_argument("--use-exp001-mmlu", action="store_true", help="Use exp-001 MMLU instead of exp-002 MMLU")
    parser.add_argument("--output", default="results/analysis/gradient_permutation_test.json")
    args = parser.parse_args()

    t0 = time.time()
    df = load_exp002_data(args.data_dir)
    print(f"Loaded {len(df)} records ({time.time()-t0:.1f}s)", flush=True)

    benchmark_stats = {}
    for bm in df["benchmark"].unique():
        df_bm = df[df["benchmark"] == bm].reset_index(drop=True)
        result = compute_henderson_i(df_bm, "correct", FACETS)
        benchmark_stats[bm] = {
            "item_id_pct": result["pct"].get("item_id", 0.0),
            "model_item_pct": result["pct"].get("model:item_id", 0.0),
            "n_obs": len(df_bm),
            "accuracy": float(df_bm["correct"].mean()),
        }
        print(f"  {bm}: item_id={benchmark_stats[bm]['item_id_pct']:.2f}%, "
              f"model:item={benchmark_stats[bm]['model_item_pct']:.2f}%", flush=True)

    if args.exp001_gstudy and args.use_exp001_mmlu:
        exp001 = load_exp001_gstudy(args.exp001_gstudy)
        if exp001 and "variance_components" in exp001:
            vc = exp001["variance_components"]
            item_pct = vc.get("item_id", {}).get("pct", 0.0)
            mi_pct = vc.get("model:item_id", {}).get("pct", 0.0)
            benchmark_stats["mmlu_exp001"] = {
                "item_id_pct": item_pct,
                "model_item_pct": mi_pct,
                "n_obs": exp001.get("n_observations", 0),
                "source": "exp-001",
            }
            print(f"  mmlu_exp001: item_id={item_pct:.2f}%, model:item={mi_pct:.2f}%", flush=True)

    available_benchmarks = [bm for bm in BENCHMARK_ORDER if bm in benchmark_stats]
    print(f"\nBenchmarks for gradient test: {available_benchmarks}", flush=True)

    item_pcts = {bm: benchmark_stats[bm]["item_id_pct"] for bm in available_benchmarks}
    model_item_pcts = {bm: benchmark_stats[bm]["model_item_pct"] for bm in available_benchmarks}

    test_item = spearman_permutation_test(item_pcts, available_benchmarks, "decreasing")
    test_model_item = spearman_permutation_test(model_item_pcts, available_benchmarks, "increasing")

    results = {
        "experiment": "exp-002 (+ optional exp-001)",
        "test_statistic": "spearman_rho",
        "n_benchmarks": len(available_benchmarks),
        "n_permutations": test_item["n_permutations"],
        "benchmark_order_hypothesis": BENCHMARK_ORDER,
        "benchmarks_used": available_benchmarks,
        "benchmark_stats": benchmark_stats,
        "item_id_gradient": {
            "observed_values": test_item["observed_values"],
            "observed_rho": test_item["observed_rho"],
            "p_value": test_item["p_value"],
            "n_extreme": test_item["n_extreme"],
            "significant_at_0.05": test_item["significant_at_0.05"],
            "kendall_tau": test_item["kendall_tau"],
            "kendall_p": test_item["kendall_p"],
            "direction": "decreasing",
        },
        "model_item_gradient": {
            "observed_values": test_model_item["observed_values"],
            "observed_rho": test_model_item["observed_rho"],
            "p_value": test_model_item["p_value"],
            "n_extreme": test_model_item["n_extreme"],
            "significant_at_0.05": test_model_item["significant_at_0.05"],
            "kendall_tau": test_model_item["kendall_tau"],
            "kendall_p": test_model_item["kendall_p"],
            "direction": "increasing",
        },
        "interpretation": (
            "Spearman rho measures rank correlation between benchmark position "
            "(knowledge-retrieval -> reasoning) and variance component percentage. "
            "P-value from exact permutation test over all k! orderings. "
            f"For {len(available_benchmarks)} benchmarks, k! = {test_item['n_permutations']}."
        ),
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nRESULTS:", flush=True)
    print(f"  item_id gradient:     rho={test_item['observed_rho']:.4f}, "
          f"p={test_item['p_value']:.4f}, "
          f"tau={test_item['kendall_tau']:.4f}", flush=True)
    print(f"  model:item gradient:  rho={test_model_item['observed_rho']:.4f}, "
          f"p={test_model_item['p_value']:.4f}, "
          f"tau={test_model_item['kendall_tau']:.4f}", flush=True)
    print(f"\nRuntime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {args.output}", flush=True)


if __name__ == "__main__":
    main()
