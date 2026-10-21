"""Within-format gradient analysis.

Groups benchmarks by item format:
  MC group:  MMLU + ARC + HellaSwag (multiple-choice)
  Free-form: GSM8K (generative numeric answer)

Checks:
  1. Whether the gradient (item_id% decreasing) holds within the MC group.
  2. Compares variance structure between MC and free-form groups.

Input:  exp-002 JSONL data
Output: results/analysis/within_format_gradient.json

Usage:
  python scripts/exp002_analysis/within_format_gradient.py --data-dir results/exp002
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

MC_BENCHMARKS = ["mmlu", "arc", "hellaswag"]
MC_ORDER = ["mmlu", "arc", "hellaswag"]
FREE_FORM_BENCHMARKS = ["gsm8k"]

FORMAT_GROUPS = {
    "multiple_choice": MC_BENCHMARKS,
    "free_form": FREE_FORM_BENCHMARKS,
}


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


def compute_henderson_i(df: pd.DataFrame, facets: list[str]) -> dict:
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
    pct = {k: v / total_var * 100 if total_var > 0 else 0.0 for k, v in vc.items()}
    return {
        "vc": vc,
        "pct": pct,
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "total_var": total_var,
        "grand_mean": float(grand_mean),
        "n_obs": len(df),
    }


def compute_g_item(vc: dict, n_levels: dict) -> float:
    sigma_item = vc.get("item_id", 0.0)
    non_item = [f for f in FACETS if f != "item_id"]
    sigma_delta = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            sigma_delta += est / prod(n_levels[f] for f in non_item)
            continue
        facets_in = set(comp.split(":"))
        if "item_id" not in facets_in:
            continue
        other = [f for f in facets_in if f != "item_id"]
        sigma_delta += est / (prod(n_levels[f] for f in other) if other else 1)
    return sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0


def main():
    parser = argparse.ArgumentParser(description="Within-format gradient analysis")
    parser.add_argument("--data-dir", default="results/exp002")
    parser.add_argument("--output", default="results/analysis/within_format_gradient.json")
    args = parser.parse_args()

    t0 = time.time()
    df = load_exp002_data(args.data_dir)
    print(f"Loaded {len(df)} records ({time.time()-t0:.1f}s)", flush=True)

    per_benchmark = {}
    for bm in df["benchmark"].unique():
        df_bm = df[df["benchmark"] == bm].reset_index(drop=True)
        result = compute_henderson_i(df_bm, FACETS)
        g_item = compute_g_item(result["vc"], result["n_levels"])
        per_benchmark[bm] = {
            "item_id_pct": result["pct"].get("item_id", 0.0),
            "model_item_pct": result["pct"].get("model:item_id", 0.0),
            "model_pct": result["pct"].get("model", 0.0),
            "temperature_pct": result["pct"].get("temperature", 0.0),
            "prompt_template_pct": result["pct"].get("prompt_template", 0.0),
            "seed_pct": result["pct"].get("seed", 0.0),
            "ordering_pct": result["pct"].get("ordering", 0.0),
            "residual_pct": result["pct"].get("residual", 0.0),
            "G_item": round(g_item, 6),
            "accuracy": result["grand_mean"],
            "n_obs": result["n_obs"],
        }

    # --- MC group internal gradient ---
    mc_available = [bm for bm in MC_ORDER if bm in per_benchmark]
    mc_item_vals = [per_benchmark[bm]["item_id_pct"] for bm in mc_available]
    mc_mi_vals = [per_benchmark[bm]["model_item_pct"] for bm in mc_available]

    mc_item_dec = all(a >= b for a, b in zip(mc_item_vals, mc_item_vals[1:]))
    mc_mi_inc = all(a <= b for a, b in zip(mc_mi_vals, mc_mi_vals[1:]))

    n_mc = len(mc_available)
    all_perms = list(permutations(range(n_mc)))
    n_item_dec = sum(1 for p in all_perms
                     if all(mc_item_vals[p[i]] >= mc_item_vals[p[i+1]] for i in range(n_mc-1)))
    n_mi_inc = sum(1 for p in all_perms
                   if all(mc_mi_vals[p[i]] <= mc_mi_vals[p[i+1]] for i in range(n_mc-1)))

    mc_gradient = {
        "benchmarks": mc_available,
        "item_id_pct": {bm: round(per_benchmark[bm]["item_id_pct"], 4) for bm in mc_available},
        "model_item_pct": {bm: round(per_benchmark[bm]["model_item_pct"], 4) for bm in mc_available},
        "item_id_monotonic_decreasing": mc_item_dec,
        "model_item_monotonic_increasing": mc_mi_inc,
        "p_item_decreasing": round(n_item_dec / len(all_perms), 6),
        "p_model_item_increasing": round(n_mi_inc / len(all_perms), 6),
    }

    print(f"\nMC group gradient ({mc_available}):", flush=True)
    print(f"  item_id dec: {mc_item_dec} {[f'{v:.2f}' for v in mc_item_vals]}", flush=True)
    print(f"  model:item inc: {mc_mi_inc} {[f'{v:.2f}' for v in mc_mi_vals]}", flush=True)

    # --- MC vs free-form structure comparison ---
    mc_avg = {}
    for key in ["item_id_pct", "model_item_pct", "model_pct", "temperature_pct",
                "prompt_template_pct", "seed_pct", "ordering_pct", "residual_pct", "G_item"]:
        vals = [per_benchmark[bm][key] for bm in mc_available]
        mc_avg[key] = round(float(np.mean(vals)), 4)

    ff_avg = {}
    ff_available = [bm for bm in FREE_FORM_BENCHMARKS if bm in per_benchmark]
    if ff_available:
        for key in ["item_id_pct", "model_item_pct", "model_pct", "temperature_pct",
                    "prompt_template_pct", "seed_pct", "ordering_pct", "residual_pct", "G_item"]:
            vals = [per_benchmark[bm][key] for bm in ff_available]
            ff_avg[key] = round(float(np.mean(vals)), 4)

    comparison_keys = ["item_id_pct", "model_item_pct", "model_pct", "residual_pct", "G_item"]
    format_comparison = {
        "mc_group": {"benchmarks": mc_available, "average": mc_avg},
        "free_form_group": {"benchmarks": ff_available, "average": ff_avg},
        "differences": {
            k: round(mc_avg.get(k, 0) - ff_avg.get(k, 0), 4)
            for k in comparison_keys
        } if ff_avg else {},
    }

    print(f"\nFormat comparison:", flush=True)
    print(f"  {'Metric':<20} {'MC avg':>10} {'Free-form':>10} {'Diff':>10}", flush=True)
    for k in comparison_keys:
        mc_v = mc_avg.get(k, 0)
        ff_v = ff_avg.get(k, 0)
        print(f"  {k:<20} {mc_v:>10.2f} {ff_v:>10.2f} {mc_v-ff_v:>+10.2f}", flush=True)

    output = {
        "experiment": "exp-002",
        "analysis": "within_format_gradient",
        "format_groups": {g: bms for g, bms in FORMAT_GROUPS.items()},
        "per_benchmark": {
            bm: {k: round(v, 4) if isinstance(v, float) else v for k, v in stats.items()}
            for bm, stats in per_benchmark.items()
        },
        "mc_group_gradient": mc_gradient,
        "format_comparison": format_comparison,
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nRuntime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {args.output}", flush=True)


if __name__ == "__main__":
    main()
