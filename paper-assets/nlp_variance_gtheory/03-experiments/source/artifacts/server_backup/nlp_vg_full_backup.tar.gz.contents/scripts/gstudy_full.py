import json
import numpy as np
import pandas as pd
from pathlib import Path
from itertools import combinations

df = pd.read_csv("results/analysis/llama_full.csv")
print("Loaded %d records" % len(df), flush=True)

facets = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
levels = {f: sorted(df[f].unique()) for f in facets}
n = {f: len(v) for f, v in levels.items()}
N = len(df)
print("Facet levels:", n, flush=True)

results = {}
for metric in ["correct", "text_exact_match"]:
    print("\n" + "=" * 60, flush=True)
    print("METRIC: " + metric, flush=True)

    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    SS_total = ((y - grand_mean) ** 2).sum()
    print("Grand mean: %.4f, SS_total: %.4f" % (grand_mean, SS_total), flush=True)

    components = {}
    main_means = {}
    for f in facets:
        means = df.groupby(f)[metric].mean()
        main_means[f] = means
        n_per = N // n[f]
        ss = n_per * ((means.values - grand_mean) ** 2).sum()
        components[f] = ss
        print("  main %s: %.2f%%" % (f, ss / SS_total * 100), flush=True)

    for f1, f2 in combinations(facets, 2):
        cell_means = df.groupby([f1, f2])[metric].mean().reset_index()
        cell_means.columns = [f1, f2, "cell_mean"]
        cell_means["f1_mean"] = cell_means[f1].map(main_means[f1])
        cell_means["f2_mean"] = cell_means[f2].map(main_means[f2])
        n_per = N // (n[f1] * n[f2])
        deviations = cell_means["cell_mean"] - cell_means["f1_mean"] - cell_means["f2_mean"] + grand_mean
        ss = n_per * (deviations ** 2).sum()
        key = "%s:%s" % (f1, f2)
        components[key] = ss

    ss_explained = sum(components.values())
    components["residual"] = SS_total - ss_explained
    total_var = sum(components.values())
    pct = {k: v / total_var * 100 for k, v in components.items()}
    sorted_pct = sorted(pct.items(), key=lambda x: -x[1])

    print("\nVariance Decomposition:", flush=True)
    for comp, p in sorted_pct:
        if p >= 0.01:
            print("  %-30s: %7.2f%%" % (comp, p), flush=True)

    tau = components.get("item_id", 0) / total_var
    G = tau
    print("\nG coefficient: %.4f" % G, flush=True)

    results[metric] = {
        "grand_mean": round(grand_mean, 4),
        "components_pct": {k: round(v, 4) for k, v in sorted_pct},
        "G_coefficient": round(G, 4),
        "total_variance": round(total_var, 4),
        "n_records": len(df),
        "n_items": n["item_id"],
        "n_conditions": int(df["condition_id"].nunique()),
    }

print("\n" + "=" * 60, flush=True)
print("D-STUDY (binary_correct)", flush=True)
d_study = {}
item_pct = results["correct"]["components_pct"].get("item_id", 0)
n_items_actual = results["correct"]["n_items"]
non_item_pct = sum(v for k, v in results["correct"]["components_pct"].items() if k != "item_id")
for ni in [25, 50, 75, 100, 150, 200, 300, 500]:
    G_n = item_pct / (item_pct + non_item_pct * (n_items_actual / ni))
    d_study[ni] = round(G_n, 4)
    print("  n_items=%4d: G = %.4f" % (ni, G_n), flush=True)
g_values = list(d_study.values())
assert all(g_values[i] <= g_values[i+1] for i in range(len(g_values)-1)),     f"D-study G must be monotonically increasing with n_items, got: {g_values}"
results["d_study_correct"] = d_study

with open("results/analysis/llama_single_model_gstudy.json", "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print("\nSaved results/analysis/llama_single_model_gstudy.json", flush=True)
print("DONE", flush=True)
