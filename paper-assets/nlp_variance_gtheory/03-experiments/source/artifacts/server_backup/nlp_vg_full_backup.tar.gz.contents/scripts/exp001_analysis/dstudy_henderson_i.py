"""D-study projection using Henderson Method I on exp-001 balanced data (259,200 records).

Two analyses:
  1. Six-facet (precision x temperature x prompt_template x seed x ordering x item_id)
  2. BF16-only five-facet (drop precision, keep bf16 subset: 86,400 records)

Output: results/exp001_analysis/dstudy_henderson_i_259k.json
"""

import json
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd


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
    return vc, n_levels


def compute_g_and_delta(vc: dict, n_levels: dict, facets: list[str]):
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


def dstudy_projection(sigma_item: float, sigma_delta: float, n_actual: int, item_counts: list[int]):
    curve = {}
    for ni in item_counts:
        ratio = n_actual / ni
        sd_ni = sigma_delta * ratio
        g_ni = sigma_item / (sigma_item + sd_ni) if (sigma_item + sd_ni) > 0 else 0.0
        curve[str(ni)] = {"G_item": round(g_ni, 6)}
    return curve


def find_min_n(sigma_item: float, sigma_delta: float, n_actual: int, target_g: float, max_n: int = 5000):
    for ni in range(1, max_n + 1):
        sd_ni = sigma_delta * (n_actual / ni)
        g = sigma_item / (sigma_item + sd_ni) if (sigma_item + sd_ni) > 0 else 0.0
        if g >= target_g:
            return ni
    return None


def run_analysis(df: pd.DataFrame, facets: list[str], label: str):
    print(f"\n{'='*60}")
    print(f"{label}: {len(df)} records, {len(facets)} facets")

    for f in facets:
        df[f] = df[f].astype(str)

    t0 = time.time()
    vc, n_levels = compute_henderson_i(df, "correct", facets)
    g_item, sigma_item, sigma_delta = compute_g_and_delta(vc, n_levels, facets)
    print(f"  Henderson I: {time.time()-t0:.1f}s")
    print(f"  G_item = {g_item:.6f}")

    total_var = sum(vc.values())
    print(f"  item_id% = {vc.get('item_id', 0) / total_var * 100:.2f}%")

    item_counts = [25, 50, 72, 100, 116, 150, 200, 300, 500, 631, 800, 1000]
    n_actual = int(n_levels["item_id"])
    dstudy = dstudy_projection(sigma_item, sigma_delta, n_actual, item_counts)

    n_g80 = find_min_n(sigma_item, sigma_delta, n_actual, 0.80)
    n_g90 = find_min_n(sigma_item, sigma_delta, n_actual, 0.90)
    n_g95 = find_min_n(sigma_item, sigma_delta, n_actual, 0.95)

    g_200_check = dstudy.get("200", {}).get("G_item")
    print(f"  G_at_200 = {g_200_check}")
    print(f"  n_G80={n_g80}, n_G90={n_g90}, n_G95={n_g95}")

    vc_sorted = dict(sorted(vc.items(), key=lambda x: -x[1]))

    return {
        "variance_components": {k: round(v, 10) for k, v in vc_sorted.items()},
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "total_variance": round(total_var, 10),
        "sigma_tau": round(sigma_item, 10),
        "sigma_delta": round(sigma_delta, 10),
        "G_item": round(g_item, 6),
        "dstudy": dstudy,
        "n_G80": n_g80,
        "n_G90": n_g90,
        "n_G95": n_g95,
        "G_at_200": g_200_check,
    }


def main():
    data_path = Path("results/analysis/llama_full_259200.csv")
    print(f"Loading {data_path}...")
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} records")
    assert len(df) == 259200, f"Expected 259200, got {len(df)}"

    facets_6 = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
    result_6 = run_analysis(df.copy(), facets_6, "6-facet (full)")

    df_bf16 = df[df["precision"] == "bf16"].reset_index(drop=True)
    print(f"\nBF16 subset: {len(df_bf16)} records")
    assert len(df_bf16) == 86400, f"Expected 86400, got {len(df_bf16)}"

    facets_5 = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
    result_5 = run_analysis(df_bf16.copy(), facets_5, "BF16 5-facet")

    output = {
        "data_source": "llama_full_259200.csv",
        "n_records": 259200,
        "six_facet": result_6,
        "bf16_five_facet": result_5,
    }

    out_path = Path("results/exp001_analysis/dstudy_henderson_i_259k.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n-> {out_path}")


if __name__ == "__main__":
    main()
