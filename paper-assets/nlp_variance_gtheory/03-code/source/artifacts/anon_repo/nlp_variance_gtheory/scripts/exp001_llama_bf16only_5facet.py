import json
import numpy as np
import pandas as pd
from pathlib import Path
from itertools import combinations

FACETS = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
SHARD_PATHS = [
    "results/exp001_llama/llama_shard_0.jsonl",
    "results/exp001_llama/llama_shard_1.jsonl",
    "results/exp001_llama/llama_shard_2.jsonl",
    "results/exp001_llama/llama_shard_3.jsonl",
]
OUTPUT_PATH = "results/analysis/exp001_llama_bf16only_5facet.json"

# exp-001b resampling results for comparison
EXP001B_SAMPLES = {
    "sample1": {"item_id": 75.88, "prompt_template:item_id": 4.42, "seed:item_id": 5.41,
                "temperature:item_id": 1.64, "ordering:item_id": 0.54, "G_item": 0.759},
    "sample2": {"item_id": 75.38, "prompt_template:item_id": 4.35, "seed:item_id": 4.87,
                "temperature:item_id": 1.45, "ordering:item_id": 0.50, "G_item": 0.754},
    "sample3": {"item_id": 72.18, "prompt_template:item_id": 5.38, "seed:item_id": 5.32,
                "temperature:item_id": 2.17, "ordering:item_id": 0.63, "G_item": 0.722},
}


def run_gstudy(df, metric="correct"):
    facets = FACETS
    for f in facets:
        df[f] = df[f].astype(str)

    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    SS_total = ((y - grand_mean) ** 2).sum()
    N = len(df)
    n = {f: df[f].nunique() for f in facets}

    components = {}
    main_means = {}

    for f in facets:
        means = df.groupby(f)[metric].mean()
        main_means[f] = means
        n_per = N // n[f]
        ss = float(n_per * ((means.values - grand_mean) ** 2).sum())
        components[f] = ss

    for f1, f2 in combinations(facets, 2):
        cell_means = df.groupby([f1, f2])[metric].mean().reset_index()
        cell_means.columns = [f1, f2, "cell_mean"]
        cell_means["f1_mean"] = cell_means[f1].map(main_means[f1])
        cell_means["f2_mean"] = cell_means[f2].map(main_means[f2])
        n_per = N // (n[f1] * n[f2])
        deviations = cell_means["cell_mean"] - cell_means["f1_mean"] - cell_means["f2_mean"] + grand_mean
        ss = float(n_per * (deviations ** 2).sum())
        components[f"{f1}:{f2}"] = ss

    ss_explained = sum(components.values())
    components["residual"] = max(0.0, SS_total - ss_explained)

    total_var = sum(components.values())
    pct = {k: round(v / total_var * 100, 4) for k, v in components.items()}
    sorted_pct = dict(sorted(pct.items(), key=lambda x: -x[1]))

    G_item = pct.get("item_id", 0) / 100

    item_pct = pct.get("item_id", 0)
    n_items_actual = n["item_id"]
    non_item_pct = sum(v for k, v in pct.items() if k != "item_id")

    d_study = {}
    for ni in [25, 50, 75, 100, 150, 200, 300, 500]:
        G_n = item_pct / (item_pct + non_item_pct * (n_items_actual / ni))
        d_study[str(ni)] = round(G_n, 4)

    min_items_g80 = None
    for ni in range(1, 2001):
        G_n = item_pct / (item_pct + non_item_pct * (n_items_actual / ni))
        if G_n >= 0.80:
            min_items_g80 = ni
            break

    return {
        "grand_mean": round(float(grand_mean), 4),
        "components_pct": sorted_pct,
        "G_item": round(float(G_item), 4),
        "total_variance": round(float(total_var), 4),
        "n_records": int(N),
        "n_items": int(n["item_id"]),
        "n_conditions": int(N // n["item_id"]),
        "n_levels": {k: int(v) for k, v in n.items()},
        "d_study": d_study,
        "min_items_g80": min_items_g80,
    }


def main():
    # Load and filter bf16 data
    dfs = []
    for path in SHARD_PATHS:
        df = pd.read_json(path, lines=True)
        dfs.append(df)
    df_all = pd.concat(dfs, ignore_index=True)
    print(f"Total Llama records: {len(df_all)}")
    print(f"Precision distribution:\n{df_all['precision'].value_counts()}")

    df_bf16 = df_all[df_all["precision"] == "bfloat16"].copy()
    print(f"\nbf16 subset: {len(df_bf16)} records")
    print(f"Unique items: {df_bf16['item_id'].nunique()}")
    n_conds = len(df_bf16) // df_bf16['item_id'].nunique()
    print(f"Conditions: {n_conds}")

    # Verify facet levels
    for f in FACETS:
        print(f"  {f}: {df_bf16[f].nunique()} levels -> {sorted(df_bf16[f].unique())[:5]}...")

    # Run 5-facet G-study
    result = run_gstudy(df_bf16, metric="correct")
    print(f"\nG-study results:")
    print(f"  grand_mean = {result['grand_mean']}")
    print(f"  G_item = {result['G_item']}")
    print(f"  Top components:")
    for k, v in list(result["components_pct"].items())[:10]:
        print(f"    {k:30s}: {v:7.2f}%")

    # Save output
    output = {
        "description": "exp-001 Llama bf16-only 5-facet matched baseline",
        "facets": FACETS,
        "filter": "precision == bfloat16",
        "result": result,
    }
    Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {OUTPUT_PATH}")

    # Comparison table
    r = result
    s1 = EXP001B_SAMPLES["sample1"]
    s2 = EXP001B_SAMPLES["sample2"]
    s3 = EXP001B_SAMPLES["sample3"]

    print("\n" + "=" * 110)
    print("COMPARISON: exp-001 bf16 5-facet (matched baseline) vs exp-001b resampling samples")
    print("=" * 110)
    header = f"{'Metric':<25} {'bf16-5f baseline':>16} {'Sample1':>10} {'Sample2':>10} {'Sample3':>10} {'Mean±Std':>14} {'Delta':>8}"
    print(header)
    print("-" * len(header))

    rows = [
        ("item_id%", "item_id"),
        ("prompt×item%", "prompt_template:item_id"),
        ("seed×item%", "seed:item_id"),
        ("temp×item%", "temperature:item_id"),
        ("order×item%", "ordering:item_id"),
    ]
    for label, key in rows:
        bl_val = r["components_pct"].get(key, 0)
        v1 = s1.get(key, 0)
        v2 = s2.get(key, 0)
        v3 = s3.get(key, 0)
        mean_v = np.mean([v1, v2, v3])
        std_v = np.std([v1, v2, v3], ddof=1)
        delta = mean_v - bl_val
        print(f"{label:<25} {bl_val:>16.2f} {v1:>10.2f} {v2:>10.2f} {v3:>10.2f} {mean_v:>7.2f}±{std_v:<5.2f} {delta:>+8.2f}")

    # Residual
    bl_res = r["components_pct"].get("residual", 0)
    print(f"{'residual%':<25} {bl_res:>16.2f}")

    # G_item
    bl_g = r["G_item"]
    g1, g2, g3 = s1["G_item"], s2["G_item"], s3["G_item"]
    g_mean = np.mean([g1, g2, g3])
    g_std = np.std([g1, g2, g3], ddof=1)
    g_delta = g_mean - bl_g
    print(f"{'G_item':<25} {bl_g:>16.4f} {g1:>10.4f} {g2:>10.4f} {g3:>10.4f} {g_mean:>7.4f}±{g_std:<6.4f}{g_delta:>+8.4f}")

    # Also show 6-facet baseline for reference
    print("\n" + "-" * 110)
    print("Reference: exp-001 Llama 6-facet baseline (from llama_single_model_gstudy.json)")
    print(f"  item_id% = 61.08,  G_item = 0.6108")
    print(f"  precision:item_id% = 4.16,  precision% = 1.19")
    print(f"  Sum of precision-related = ~5.35%")
    bf16_item = r["components_pct"].get("item_id", 0)
    print(f"\nDelta decomposition:")
    print(f"  6-facet item_id%:                  61.08")
    print(f"  bf16-5f item_id%:                  {bf16_item:.2f}  (delta = {bf16_item - 61.08:+.2f})")
    print(f"  exp-001b mean item_id%:            74.48  (delta from bf16-5f = {74.48 - bf16_item:+.2f})")
    print(f"  -> Precision removal effect:       {bf16_item - 61.08:+.2f} pp")
    print(f"  -> Item selection effect:           {74.48 - bf16_item:+.2f} pp")

    print("\nDONE")


if __name__ == "__main__":
    main()
