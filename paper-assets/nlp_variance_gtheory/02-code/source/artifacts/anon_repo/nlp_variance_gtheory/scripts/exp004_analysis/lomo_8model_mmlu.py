"""LOMO (Leave-One-Model-Out) analysis on 8-model MMLU data.

For each of 8 models, drop it and compute Henderson I G_item on the
remaining 7-model subset.  Also compute the full 8-model baseline.

Facets: model, temperature, prompt_template, seed, ordering, item_id
Output: results/exp004_8model_analysis/lomo_8model_mmlu.json
"""

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
DATA_DIR = Path("results/exp002")
OUTPUT = Path("results/exp004_8model_analysis/lomo_8model_mmlu.json")


def load_mmlu_data(data_dir: Path) -> pd.DataFrame:
    frames = []
    for f in sorted(data_dir.glob("*_mmlu.jsonl")):
        df = pd.read_json(f, lines=True)
        frames.append(df)
    df = pd.concat(frames, ignore_index=True)
    if "top_logprobs" in df.columns:
        df.drop(columns=["top_logprobs"], inplace=True)
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    df["temperature"] = df["temperature"].round(1)
    df = df[df["temperature"].isin([0.0, 0.7])].reset_index(drop=True)
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]):
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


def compute_g_item(vc: dict, n_levels: dict, facets: list[str]) -> tuple[float, float, float]:
    sigma_item = vc.get("item_id", 0.0)
    non_item_facets = [f for f in facets if f != "item_id"]

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


def analyze_subset(df_sub: pd.DataFrame, label: str) -> dict:
    vc, n_levels, effects = compute_henderson_i(df_sub, "correct", FACETS)
    total_var = sum(vc.values())
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels, FACETS)

    item_pct = vc.get("item_id", 0.0) / total_var * 100 if total_var > 0 else 0.0
    mi_pct = vc.get("model:item_id", 0.0) / total_var * 100 if total_var > 0 else 0.0

    expected_n = prod(n_levels[f] for f in FACETS)
    actual_n = len(df_sub)
    assert actual_n == expected_n, f"{label}: expected {expected_n}, got {actual_n}"

    print(f"  {label}: N={actual_n}, item_id={item_pct:.2f}%, model:item={mi_pct:.2f}%, G_item={g_item:.4f}", flush=True)

    return {
        "label": label,
        "n_observations": actual_n,
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "grand_mean_accuracy": round(float(df_sub["correct"].mean()), 6),
        "variance_components": {
            k: {"estimate": round(v, 10), "pct": round(v / total_var * 100, 4) if total_var > 0 else 0.0}
            for k, v in sorted(vc.items(), key=lambda x: -x[1])
        },
        "total_variance": round(total_var, 10),
        "item_id_pct": round(item_pct, 4),
        "model_item_pct": round(mi_pct, 4),
        "G_item": round(g_item, 6),
        "sigma_tau": round(sigma_tau, 10),
        "sigma_delta": round(sigma_delta, 10),
    }


def main():
    t0 = time.time()
    df = load_mmlu_data(DATA_DIR)
    models = sorted(df["model"].unique())
    print(f"Loaded {len(df)} records, {len(models)} models: {models}", flush=True)
    print(f"Temps: {sorted(df['temperature'].unique())}", flush=True)

    for f in FACETS:
        print(f"  {f}: {df[f].nunique()} levels", flush=True)

    # Full 8-model baseline
    print("\n=== Full 8-model baseline ===", flush=True)
    full_result = analyze_subset(df, "Full 8-model")

    # LOMO: drop each model
    print("\n=== LOMO analysis ===", flush=True)
    lomo_results = {}
    for drop_model in models:
        df_sub = df[df["model"] != drop_model].reset_index(drop=True)
        result = analyze_subset(df_sub, f"Drop {drop_model}")
        lomo_results[drop_model] = result

    # Summary table
    g_values = [r["G_item"] for r in lomo_results.values()]
    item_values = [r["item_id_pct"] for r in lomo_results.values()]

    print(f"\n{'='*70}", flush=True)
    print(f"{'Dropped Model':<20} {'item_id%':>10} {'model*item%':>12} {'G_item':>8} {'N':>10}", flush=True)
    print(f"{'-'*70}", flush=True)
    for model_name in models:
        r = lomo_results[model_name]
        print(f"{model_name:<20} {r['item_id_pct']:>9.2f}% {r['model_item_pct']:>11.2f}% {r['G_item']:>8.4f} {r['n_observations']:>10}", flush=True)
    print(f"{'-'*70}", flush=True)
    print(f"Full 8-model: item_id={full_result['item_id_pct']:.2f}%, G_item={full_result['G_item']:.4f}", flush=True)
    print(f"LOMO range: G_item [{min(g_values):.4f}, {max(g_values):.4f}], item_id% [{min(item_values):.2f}%, {max(item_values):.2f}%]", flush=True)

    output = {
        "analysis": "lomo_8model_mmlu",
        "full_8model": full_result,
        "lomo": lomo_results,
        "summary": {
            "g_item_range": [round(min(g_values), 6), round(max(g_values), 6)],
            "item_id_pct_range": [round(min(item_values), 4), round(max(item_values), 4)],
            "full_g_item": full_result["G_item"],
            "full_item_id_pct": full_result["item_id_pct"],
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nRuntime: {time.time()-t0:.1f}s", flush=True)
    print(f"-> {OUTPUT}", flush=True)


if __name__ == "__main__":
    main()
