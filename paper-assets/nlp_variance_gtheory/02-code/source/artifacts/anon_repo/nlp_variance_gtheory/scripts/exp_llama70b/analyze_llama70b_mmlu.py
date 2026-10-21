"""Henderson Method I variance decomposition for Llama-3.1-70B MMLU.

5-facet fully-crossed balanced design:
  T (temperature) x Q (prompt_template) x S (seed) x O (ordering) x I (item_id)
  2 x 6 x 6 x 4 x 200 = 57,600 observations
"""

import json
import numpy as np
import pandas as pd
from itertools import combinations
from math import prod

INPUT = "./data/exp_llama70b/llama70b_mmlu.jsonl"
OUTPUT = "./data/exp_llama70b/llama70b_mmlu_gstudy.json"
FACETS = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
METRIC = "correct"


def verify_balance(df, facets):
    n = {f: df[f].nunique() for f in facets}
    expected = prod(n.values())
    actual = len(df)
    print(f"Facet levels: {n}")
    print(f"Expected N = {expected}, Actual N = {actual}")
    assert actual == expected, f"Unbalanced: {actual} != {expected}"
    print("Design is fully balanced.")
    return n


def compute_henderson_i(df, facets, metric, n_levels):
    N = len(df)
    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    SS_total = ((y - grand_mean) ** 2).sum()

    effects = {}

    # Main effects
    for f in facets:
        means = df.groupby(f)[metric].mean()
        n_per = N // n_levels[f]
        ss = n_per * ((means.values - grand_mean) ** 2).sum()
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": float(ss), "df": int(df_eff), "ms": float(ss / df_eff)}

    # 2-way interactions
    main_means = {f: df.groupby(f)[metric].mean() for f in facets}
    for fi, fj in combinations(facets, 2):
        cell_means = df.groupby([fi, fj])[metric].mean()
        n_per_cell = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), cm in cell_means.items():
            interaction = cm - main_means[fi][li] - main_means[fj][lj] + grand_mean
            ss += n_per_cell * interaction ** 2
        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        key = f"{fi}:{fj}"
        effects[key] = {"ss": float(ss), "df": int(df_eff), "ms": float(ss / df_eff)}

    # Residual
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, SS_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": float(ss_res), "df": int(df_res),
                            "ms": float(ss_res / df_res) if df_res > 0 else 0.0}

    # EMS-based variance components (Henderson Method I)
    vc_raw = {}
    ms_res = effects["residual"]["ms"]

    # 2-way: σ²_{ij} = (MS_{ij} - MS_res) / prod(n_k for k not in {i,j})
    for fi, fj in combinations(facets, 2):
        key = f"{fi}:{fj}"
        others = [f for f in facets if f not in (fi, fj)]
        denom = prod(n_levels[f] for f in others)
        vc_raw[key] = max(0.0, (effects[key]["ms"] - ms_res) / denom)

    # Main: σ²_i = (MS_i - Σ interaction contributions - MS_res) / prod(n_k, k≠i)
    for fi in facets:
        interaction_sum = 0.0
        for fj in facets:
            if fj == fi:
                continue
            key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc_raw else f"{fj}:{fi}"
            others_of_int = [f for f in facets if f not in (fi, fj)]
            coeff = prod(n_levels[f] for f in others_of_int)
            interaction_sum += coeff * vc_raw[key]
        denom = prod(n_levels[f] for f in facets if f != fi)
        vc_raw[fi] = max(0.0, (effects[fi]["ms"] - interaction_sum - ms_res) / denom)

    vc_raw["residual"] = ms_res

    return effects, vc_raw, grand_mean, SS_total


def compute_g_and_dstudy(vc_raw, facets, n_levels, n_items_list=[25, 50, 100, 200, 500]):
    sigma_tau = vc_raw["item_id"]
    n_conditions = prod(n_levels[f] for f in facets if f != "item_id")
    n_original = n_levels["item_id"]

    # σ²(δ) = Σ_j [σ²(item×j) / n_j] + σ²(res) / n_conditions
    delta_breakdown = {}
    for key, val in vc_raw.items():
        if key == "item_id" or key == "residual":
            continue
        if "item_id" in key:
            parts = key.split(":")
            other = [p for p in parts if p != "item_id"][0]
            delta_breakdown[key] = val / n_levels[other]

    delta_breakdown["residual"] = vc_raw["residual"] / n_conditions
    sigma_delta = sum(delta_breakdown.values())

    G_item = sigma_tau / (sigma_tau + sigma_delta) if (sigma_tau + sigma_delta) > 0 else 0.0

    # D-study: G(n_i) = σ²(τ) / [σ²(τ) + σ²(δ) × n_original / n_i]
    d_study = {}
    for ni in n_items_list:
        sigma_delta_ni = sigma_delta * n_original / ni
        G = sigma_tau / (sigma_tau + sigma_delta_ni) if (sigma_tau + sigma_delta_ni) > 0 else 0.0
        d_study[str(ni)] = round(G, 6)

    return G_item, sigma_tau, sigma_delta, delta_breakdown, d_study


def main():
    df = pd.read_json(INPUT, lines=True)
    for f in FACETS:
        df[f] = df[f].astype(str)

    print(f"Loaded {len(df)} rows from {INPUT}")
    n_levels = verify_balance(df, FACETS)

    effects, vc_raw, grand_mean, ss_total = compute_henderson_i(df, FACETS, METRIC, n_levels)

    total_var = sum(vc_raw.values())
    vc_pct = {k: round(v / total_var * 100, 4) for k, v in vc_raw.items()}

    G_item, sigma_tau, sigma_delta, delta_breakdown, d_study = compute_g_and_dstudy(
        vc_raw, FACETS, n_levels
    )

    # Print summary
    print(f"\nGrand mean: {grand_mean:.6f}")
    print(f"Total variance: {total_var:.10f}")
    print(f"\n{'Component':<30} {'sigma_sq':>12} {'%':>8}")
    print("-" * 52)
    for k, v in sorted(vc_pct.items(), key=lambda x: -x[1]):
        print(f"{k:<30} {vc_raw[k]:>12.10f} {v:>7.2f}%")

    print(f"\nG_item (200 items): {G_item:.6f}")
    print(f"sigma_tau = {sigma_tau:.10f}")
    print(f"sigma_delta = {sigma_delta:.10f}")

    print(f"\nDelta breakdown:")
    for k, v in sorted(delta_breakdown.items(), key=lambda x: -x[1]):
        print(f"  {k:<30} {v:.10f}")

    print("\nD-study (G by n_items):")
    for ni, g in d_study.items():
        print(f"  n={ni}: G={g:.6f}")

    # Cross-model comparison
    qwen = {"item_id_pct": 83.2482, "G_item": 0.978544, "grand_mean": 0.870347}
    print(f"\n{'='*60}")
    print("Cross-model comparison (MMLU, 200 items, 288 conditions)")
    print(f"{'Metric':<30} {'Llama-70B':>14} {'Qwen-72B':>14}")
    print(f"-" * 60)
    print(f"{'Grand mean':<30} {grand_mean:>14.4f} {qwen['grand_mean']:>14.4f}")
    print(f"{'item_id %':<30} {vc_pct['item_id']:>14.2f} {qwen['item_id_pct']:>14.2f}")
    print(f"{'G_item':<30} {G_item:>14.6f} {qwen['G_item']:>14.6f}")

    # Facet ranking comparison
    qwen_rank = ["item_id", "residual", "prompt_template:item_id", "ordering:item_id",
                  "seed:item_id", "temperature:item_id"]
    llama_rank = [k for k, _ in sorted(vc_pct.items(), key=lambda x: -x[1])
                  if vc_pct[k] > 0.01]
    print(f"\nFacet ranking (>0.01%):")
    print(f"  Llama-70B: {llama_rank}")
    print(f"  Qwen-72B:  {qwen_rank}")

    # Save
    result = {
        "model": "Llama-3.1-70B-Instruct",
        "benchmark": "mmlu",
        "n_items": n_levels["item_id"],
        "n_conditions": prod(n_levels[f] for f in FACETS if f != "item_id"),
        "total_records": len(df),
        "grand_mean": round(grand_mean, 6),
        "total_variance": round(total_var, 10),
        "components_pct": {k: v for k, v in sorted(vc_pct.items(), key=lambda x: -x[1])},
        "components_raw": {k: round(v, 10) for k, v in sorted(vc_raw.items(), key=lambda x: -x[1])},
        "G_item": round(G_item, 6),
        "sigma_tau": sigma_tau,
        "sigma_delta": sigma_delta,
        "delta_breakdown": delta_breakdown,
        "d_study": d_study,
        "comparison_qwen72b": {
            "qwen_item_id_pct": 83.2482,
            "qwen_G_item": 0.978544,
            "qwen_grand_mean": 0.870347,
            "llama_item_id_pct": vc_pct["item_id"],
            "llama_G_item": round(G_item, 6),
            "llama_grand_mean": round(grand_mean, 6),
        },
        "anova_table": {k: {"ss": v["ss"], "df": v["df"], "ms": v["ms"]}
                        for k, v in effects.items()},
    }

    with open(OUTPUT, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {OUTPUT}")


if __name__ == "__main__":
    main()
