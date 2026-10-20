"""SF5: Temperature-stratified seed variance analysis.

Separates T=0 (deterministic) vs T>0 (stochastic) seed effects using
Henderson Method I variance decomposition.
"""

import json
import sys
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd


def compute_ss(df, response, facets):
    grand_mean = df[response].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in facets}
    effects = {}

    for f in facets:
        group_means = df.groupby(f, observed=True)[response].mean()
        n_per_group = N // n_levels[f]
        ss = float(n_per_group * ((group_means - grand_mean) ** 2).sum())
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

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
        effects[f"{fi}:{fj}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((df[response] - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}
    return effects, n_levels


def estimate_variance_components(effects, facets, n_levels):
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
    return vc


def analyze_stratum(df, facets, label):
    """Run Henderson I on a temperature stratum."""
    for f in facets:
        df[f] = df[f].astype(str)

    effects, n_levels = compute_ss(df, "correct", facets)
    vc = estimate_variance_components(effects, facets, n_levels)
    total = sum(vc.values())

    pct = {k: v / total * 100 for k, v in vc.items()}
    sorted_pct = dict(sorted(pct.items(), key=lambda x: -x[1]))

    # Find seed-related components
    seed_pct = pct.get("seed", 0.0)
    seed_item_key = None
    for k in pct:
        parts = k.split(":")
        if "seed" in parts and "item_id" in parts:
            seed_item_key = k
            break
    seed_item_pct = pct.get(seed_item_key, 0.0) if seed_item_key else 0.0
    item_id_pct = pct.get("item_id", 0.0)
    G_item = item_id_pct / 100.0

    print(f"\n=== {label} (n={len(df)}) ===")
    print(f"  seed: {seed_pct:.4f}%")
    print(f"  seed:item_id: {seed_item_pct:.4f}%")
    print(f"  item_id: {item_id_pct:.4f}%")
    print(f"  G_item: {G_item:.4f}")

    return {
        "n_records": len(df),
        "seed_pct": round(seed_pct, 4),
        "seed_item_pct": round(seed_item_pct, 4),
        "item_id_pct": round(item_id_pct, 4),
        "G_item": round(G_item, 4),
        "all_components_pct": {k: round(v, 4) for k, v in sorted_pct.items()},
        "n_levels": {k: int(v) for k, v in n_levels.items()},
    }


def main():
    data_path = "./results/analysis/llama_full.csv"
    output_path = "./results/analysis/temp_stratified_seed.json"

    print("Loading data...")
    df = pd.read_csv(data_path)
    print(f"Total records: {len(df)}")
    print(f"Temperature values: {sorted(df['temperature'].unique())}")

    facets_5 = ["precision", "prompt_template", "seed", "ordering", "item_id"]
    facets_6 = ["precision", "prompt_template", "seed", "ordering", "temperature", "item_id"]

    # 1. T=0.0 subset (5 facets, no temperature)
    df_t0 = df[df["temperature"] == 0.0].copy()
    r_t0 = analyze_stratum(df_t0, facets_5, "T=0.0")

    # 2. T=0.3 subset (5 facets)
    df_t03 = df[df["temperature"] == 0.3].copy()
    r_t03 = analyze_stratum(df_t03, facets_5, "T=0.3")

    # 3. T=0.7 subset (5 facets)
    df_t07 = df[df["temperature"] == 0.7].copy()
    r_t07 = analyze_stratum(df_t07, facets_5, "T=0.7")

    # 4. T>0 combined (6 facets, temperature as facet)
    df_tgt0 = df[df["temperature"] > 0.0].copy()
    r_tgt0 = analyze_stratum(df_tgt0, facets_6, "T>0 (combined)")

    # 5. Gradient analysis
    seed_t0 = r_t0["seed_pct"]
    seed_t03 = r_t03["seed_pct"]
    seed_t07 = r_t07["seed_pct"]
    monotonic = bool(seed_t0 <= seed_t03 <= seed_t07)

    seed_item_t0 = r_t0["seed_item_pct"]
    seed_item_t03 = r_t03["seed_item_pct"]
    seed_item_t07 = r_t07["seed_item_pct"]
    monotonic_item = bool(seed_item_t0 <= seed_item_t03 <= seed_item_t07)

    # 6. FP non-associativity
    t0_seed_nonzero = bool(r_t0["seed_pct"] > 0.0 or r_t0["seed_item_pct"] > 0.0)
    fp_magnitude = r_t0["seed_pct"] + r_t0["seed_item_pct"]

    results = {
        "T0.0": r_t0,
        "T0.3": r_t03,
        "T0.7": r_t07,
        "T_gt0": r_tgt0,
        "gradient": {
            "seed_T0": seed_t0,
            "seed_T03": seed_t03,
            "seed_T07": seed_t07,
            "seed_item_T0": seed_item_t0,
            "seed_item_T03": seed_item_t03,
            "seed_item_T07": seed_item_t07,
            "monotonic_increase_seed": monotonic,
            "monotonic_increase_seed_item": monotonic_item,
        },
        "fp_non_associativity": {
            "T0_seed_nonzero": t0_seed_nonzero,
            "T0_seed_pct": seed_t0,
            "T0_seed_item_pct": seed_item_t0,
            "magnitude": round(fp_magnitude, 4),
            "interpretation": (
                "Non-zero seed variance at T=0 indicates floating-point non-associativity in vLLM. "
                f"Combined seed+seed:item = {fp_magnitude:.4f}% of total variance."
            ),
        },
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  T=0.0: seed={seed_t0:.4f}%, seed:item={seed_item_t0:.4f}%")
    print(f"  T=0.3: seed={seed_t03:.4f}%, seed:item={seed_item_t03:.4f}%")
    print(f"  T=0.7: seed={seed_t07:.4f}%, seed:item={seed_item_t07:.4f}%")
    print(f"  Monotonic seed increase: {monotonic}")
    print(f"  Monotonic seed:item increase: {monotonic_item}")
    print(f"  FP non-associativity (T=0 seed+seed:item): {fp_magnitude:.4f}%")
    print(f"\n-> {output_path}")


if __name__ == "__main__":
    main()
