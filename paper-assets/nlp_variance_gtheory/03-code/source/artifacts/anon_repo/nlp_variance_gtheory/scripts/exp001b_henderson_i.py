"""Recompute exp-001b resampling variance decomposition using Henderson Method I.

5 facets: temperature(3) × prompt_template(6) × seed(6) × ordering(4) × item_id(200)
"""
import json
import numpy as np
import pandas as pd
from pathlib import Path
from itertools import combinations
from math import prod

DIM_ORDER = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
SAMPLES = {
    "sample1": "results/exp001b/sample1/all_results.jsonl",
    "sample2": "results/exp001b/sample2/all_results.jsonl",
    "sample3": "results/exp001b/sample3/all_results.jsonl",
}

def henderson_i_from_tensor(Y, dim_sizes, dim_names=None):
    grand_mean = Y.mean()
    N = Y.size
    n_dims = len(dim_sizes)
    if dim_names is None:
        dim_names = DIM_ORDER[:n_dims]

    effects = {}
    for d, name in enumerate(dim_names):
        ax = tuple(i for i in range(n_dims) if i != d)
        gm = Y.mean(axis=ax)
        n_per = N // dim_sizes[d]
        ss = float(n_per * ((gm - grand_mean) ** 2).sum())
        df_eff = dim_sizes[d] - 1
        effects[name] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for (d1, n1), (d2, n2) in combinations(enumerate(zip(dim_names, dim_sizes)), 2):
        di, ni = d1, n1[1]
        dj, nj = d2, n2[1]
        name_i, name_j = n1[0], n2[0]
        ax = tuple(k for k in range(n_dims) if k != di and k != dj)
        cell_mean = Y.mean(axis=ax)
        main_i = Y.mean(axis=tuple(k for k in range(n_dims) if k != di))
        main_j = Y.mean(axis=tuple(k for k in range(n_dims) if k != dj))
        n_per = N // (ni * nj)
        interaction = cell_mean - main_i.reshape([-1 if k == 0 else 1 for k in range(cell_mean.ndim)]) \
                      - main_j.reshape([1 if k == 0 else -1 for k in range(cell_mean.ndim)])  + grand_mean
        ss = float(n_per * (interaction ** 2).sum())
        df_eff = (ni - 1) * (nj - 1)
        key = f"{name_i}:{name_j}"
        effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((Y - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    n_levels = dict(zip(dim_names, dim_sizes))
    vc = {}

    for fi, fj in combinations(dim_names, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in dim_names if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in dim_names:
        coeff_main = prod(n_levels[f] for f in dim_names if f != fi)
        ic = 0.0
        for fj in dim_names:
            if fj == fi:
                continue
            ik = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            cij = prod(n_levels[f] for f in dim_names if f not in (fi, fj))
            ic += cij * vc[ik]
        raw = (effects[fi]["ms"] - ic - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, n_levels


def main():
    proj = Path(".")
    results = {}

    for name, path in SAMPLES.items():
        print(f"\n--- {name} ---")
        df = pd.read_json(proj / path, lines=True)
        print(f"  Loaded {len(df)} records")

        temps = sorted(df["temperature"].unique())
        prompts = sorted(df["prompt_template"].unique())
        seeds = sorted(df["seed"].unique())
        orderings = sorted(df["ordering"].unique())
        items = sorted(df["item_id"].unique())

        dim_sizes = [len(temps), len(prompts), len(seeds), len(orderings), len(items)]
        print(f"  dims: temp={len(temps)}, prompt={len(prompts)}, seed={len(seeds)}, ordering={len(orderings)}, items={len(items)}")
        print(f"  Expected size: {prod(dim_sizes)}, actual: {len(df)}")

        # Build tensor
        df["t_idx"] = df["temperature"].map({v: i for i, v in enumerate(temps)})
        df["p_idx"] = df["prompt_template"].map({v: i for i, v in enumerate(prompts)})
        df["s_idx"] = df["seed"].map({v: i for i, v in enumerate(seeds)})
        df["o_idx"] = df["ordering"].map({v: i for i, v in enumerate(orderings)})
        df["i_idx"] = df["item_id"].map({v: i for i, v in enumerate(items)})

        Y = np.zeros(dim_sizes, dtype=np.float64)
        Y[df["t_idx"].values, df["p_idx"].values, df["s_idx"].values, df["o_idx"].values, df["i_idx"].values] = df["correct"].values

        vc, n_levels = henderson_i_from_tensor(Y, dim_sizes, DIM_ORDER)
        total_var = sum(vc.values())
        item_id_pct = vc["item_id"] / total_var * 100

        print(f"  total_var = {total_var:.8f}")
        print(f"  item_id% = {item_id_pct:.4f}")
        for k in sorted(vc.keys(), key=lambda x: -vc[x]):
            pct = vc[k] / total_var * 100
            if pct >= 0.1:
                print(f"    {k:<30} {pct:>7.2f}%")

        results[name] = {
            "item_id_pct": round(item_id_pct, 4),
            "total_variance": round(total_var, 8),
            "n_items": len(items),
            "vc": {k: round(v / total_var * 100, 4) for k, v in sorted(vc.items(), key=lambda x: -x[1])},
        }

    # Compute CV
    values = [results[s]["item_id_pct"] for s in ["sample1", "sample2", "sample3"]]
    mean_v = np.mean(values)
    cv = np.std(values, ddof=1) / mean_v * 100

    print(f"\n\n=== SUMMARY ===")
    print(f"Sample 1: item_id = {values[0]:.2f}%")
    print(f"Sample 2: item_id = {values[1]:.2f}%")
    print(f"Sample 3: item_id = {values[2]:.2f}%")
    print(f"Mean: {mean_v:.2f}%")
    print(f"CV: {cv:.2f}%")
    print(f"Reference (6-facet exp-001): 58.39%")

    output = {
        "method": "Henderson Method I",
        "facets": 5,
        "facet_levels": {"temperature": 3, "prompt_template": 6, "seed": 6, "ordering": 4, "item_id": 200},
        "model": "Llama-3.1-8B-Instruct",
        "note": "exp-001b has single precision (bfloat16); 5-facet Henderson I applied",
        "samples": [
            {"name": "sample1", "item_id_pct": results["sample1"]["item_id_pct"],
             "total_variance": results["sample1"]["total_variance"], "n_items": 200,
             "all_components_pct": results["sample1"]["vc"]},
            {"name": "sample2", "item_id_pct": results["sample2"]["item_id_pct"],
             "total_variance": results["sample2"]["total_variance"], "n_items": 200,
             "all_components_pct": results["sample2"]["vc"]},
            {"name": "sample3", "item_id_pct": results["sample3"]["item_id_pct"],
             "total_variance": results["sample3"]["total_variance"], "n_items": 200,
             "all_components_pct": results["sample3"]["vc"]},
        ],
        "mean_item_id_pct": round(float(mean_v), 4),
        "cv_pct": round(float(cv), 4),
        "reference_full_mmlu_item_id_pct": 58.39,
    }

    print(f"\nJSON output:")
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
