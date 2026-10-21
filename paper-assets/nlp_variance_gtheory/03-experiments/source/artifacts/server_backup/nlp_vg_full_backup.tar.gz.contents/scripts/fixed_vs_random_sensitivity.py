import json
import numpy as np
import pandas as pd
from itertools import combinations
from pathlib import Path

df = pd.read_csv("results/analysis/llama_full.csv")
print(f"Loaded {len(df)} records", flush=True)

facets = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
n = {f: df[f].nunique() for f in facets}
N = len(df)
print(f"Facet levels: {n}", flush=True)

# Pre-compute all main-effect means
main_means = {}
for f in facets:
    main_means[f] = df.groupby(f).agg({"correct": "mean", "text_exact_match": "mean"})

def variance_decomposition(df, metric, fixed_facets=None):
    if fixed_facets is None:
        fixed_facets = set()
    
    grand_mean = df[metric].mean()
    SS_total = ((df[metric] - grand_mean) ** 2).sum()
    
    components = {}
    
    # Main effects (vectorized)
    for f in facets:
        means = main_means[f][metric]
        n_per = N // n[f]
        ss = n_per * ((means - grand_mean) ** 2).sum()
        components[f] = ss
    
    # 2-way interactions (vectorized)
    for f1, f2 in combinations(facets, 2):
        cell_means = df.groupby([f1, f2])[metric].mean().reset_index()
        cell_means.columns = [f1, f2, 'cell_mean']
        
        # Merge main effect means
        f1_means = main_means[f1][metric].reset_index()
        f1_means.columns = [f1, 'f1_mean']
        f2_means = main_means[f2][metric].reset_index()
        f2_means.columns = [f2, 'f2_mean']
        
        cell_means = cell_means.merge(f1_means, on=f1).merge(f2_means, on=f2)
        
        n_per = N // (n[f1] * n[f2])
        interaction = cell_means['cell_mean'] - cell_means['f1_mean'] - cell_means['f2_mean'] + grand_mean
        ss = n_per * (interaction ** 2).sum()
        components[f"{f1}:{f2}"] = ss
    
    ss_explained = sum(components.values())
    components["residual"] = SS_total - ss_explained
    
    total_var = sum(components.values())
    pct = {k: v/total_var * 100 for k, v in components.items()}
    
    tau = pct.get("item_id", 0)
    delta = 0
    for k, v in pct.items():
        if k == "item_id":
            continue
        parts = k.split(":")
        if any(p in fixed_facets for p in parts):
            continue
        delta += v
    
    G = tau / (tau + delta) if (tau + delta) > 0 else 0
    
    return {
        "components_pct": {k: round(v, 4) for k, v in sorted(pct.items(), key=lambda x: -x[1])},
        "G_coefficient": round(G, 4),
        "fixed_facets": list(fixed_facets),
        "tau_pct": round(tau, 4),
        "delta_pct": round(delta, 4),
    }

# binary_correct
results = {"metric": "binary_correct", "analyses": {}}
scenarios = [
    ("all_random", set()),
    ("temperature_fixed", {"temperature"}),
    ("ordering_fixed", {"ordering"}),
    ("precision_fixed", {"precision"}),
    ("three_fixed", {"temperature", "ordering", "precision"}),
    ("temp_prec_fixed", {"temperature", "precision"}),
]

print("\n=== binary_correct ===", flush=True)
for name, fixed in scenarios:
    r = variance_decomposition(df, "correct", fixed_facets=fixed)
    results["analyses"][name] = r
    print(f"{name:<40s} G={r['G_coefficient']:.4f}, delta={r['delta_pct']:.2f}%", flush=True)

# text_exact_match
results_text = {"metric": "text_exact_match", "analyses": {}}
text_scenarios = [
    ("all_random", set()),
    ("temperature_fixed", {"temperature"}),
    ("temp_prec_fixed", {"temperature", "precision"}),
    ("three_fixed", {"temperature", "ordering", "precision"}),
]

print("\n=== text_exact_match ===", flush=True)
for name, fixed in text_scenarios:
    r = variance_decomposition(df, "text_exact_match", fixed_facets=fixed)
    results_text["analyses"][name] = r
    print(f"{name:<40s} G={r['G_coefficient']:.4f}, delta={r['delta_pct']:.2f}%", flush=True)

# Save
output = {"binary_correct": results, "text_exact_match": results_text}
Path("results/analysis").mkdir(parents=True, exist_ok=True)
with open("results/analysis/fixed_vs_random_sensitivity.json", "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"\nSaved results/analysis/fixed_vs_random_sensitivity.json", flush=True)
print("DONE", flush=True)
