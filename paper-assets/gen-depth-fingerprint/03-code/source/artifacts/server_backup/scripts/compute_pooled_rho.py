import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import json

features = ['hapax_ratio', 'ttr', 'entropy_mean', 'entropy_min', 'entropy_max', 'tail_decay', 'entropy_std']

# Step 1: Pooled Spearman rho
df = pd.read_csv('/root/gen-depth-fingerprint/data/features_all_models.csv')
generators = sorted(df['model_name'].unique().tolist())
n_samples = len(df)

print(f"Generators: {generators}")
print(f"Per-gen counts: {df['model_name'].value_counts().to_dict()}")
print(f"Total samples: {n_samples}")
print()

pooled_rho = {}
for feat in features:
    rho, pval = spearmanr(df[feat], df['depth'])
    pooled_rho[feat] = round(rho, 4)

# Step 2: Per-gen median rho
with open('/root/gen-depth-fingerprint/results/spearman_per_generator.json') as f:
    per_gen = json.load(f)

per_gen_median_rho = {}
for feat in features:
    vals = sorted([per_gen[g][feat] for g in per_gen])
    median_val = (vals[2] + vals[3]) / 2  # 6 values: median = avg of 3rd and 4th
    per_gen_median_rho[feat] = round(median_val, 4)

# Save results
result = {
    "pooled_rho": pooled_rho,
    "per_gen_median_rho": per_gen_median_rho,
    "n_samples_pooled": n_samples,
    "generators": generators,
    "computation_details": f"Pooled: Spearman rho on all {n_samples} samples from {len(generators)} generators. Median: median of 6 per-gen rho values from spearman_per_generator.json."
}
with open('/root/gen-depth-fingerprint/results/pooled_rho_fix.json', 'w') as f:
    json.dump(result, f, indent=2)

# Print results
print("=== POOLED RHO (all ~27500 samples) ===")
for feat in features:
    print(f"{feat}: {pooled_rho[feat]}")

print()
print("=== PER-GEN MEDIAN RHO ===")
for feat in features:
    print(f"{feat}: {per_gen_median_rho[feat]}")

print()
print("=== WRONG VALUES (currently in paper, Qwen3-8B only) ===")
wrong = {'hapax_ratio': -0.558, 'ttr': -0.542, 'entropy_mean': -0.475, 'entropy_min': -0.303, 'entropy_max': 0.095, 'tail_decay': -0.089, 'entropy_std': -0.076}
for feat in features:
    print(f"{feat}: wrong={wrong[feat]}, pooled={pooled_rho[feat]}, median={per_gen_median_rho[feat]}")
