"""
exp060_ddr_analysis.py — DDR metrics for Qwen3-14B-Base (14.7B params).
Reads features CSV, computes Spearman rho and Cohen's d for 7 features.
"""
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import json

FEATURES = ['entropy_mean', 'entropy_std', 'entropy_max', 'entropy_min', 'ttr', 'hapax_ratio', 'tail_decay']

def cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    pooled = np.sqrt(((n1-1)*g1.var() + (n2-1)*g2.var()) / (n1+n2-2))
    return (g1.mean() - g2.mean()) / pooled if pooled > 0 else 0

df = pd.read_csv('data/features_qwen3-14b-base.csv')
print(f"Loaded {len(df)} rows, columns: {list(df.columns)}")
print(f"Depth distribution: {df['depth'].value_counts().sort_index().to_dict()}")

gen0 = df[df['depth'] == 0]
gen2p = df[df['depth'] >= 2]

results = {
    "generator": "qwen3-14b-base",
    "params_b": 14.7,
    "n_seeds": int(df['seed_id'].nunique()),
    "n_samples": len(df),
    "features": {}
}

for feat in FEATURES:
    if feat not in df.columns:
        print(f"WARNING: {feat} not in columns, skipping")
        continue
    rho, p = spearmanr(df['depth'], df[feat])
    d = cohens_d(gen0[feat].dropna(), gen2p[feat].dropna())

    if abs(rho) > 0.3 and abs(d) > 0.5:
        group = "drifting"
    elif abs(d) < 0.2:
        group = "stationary"
    else:
        group = "intermediate"

    results["features"][feat] = {
        "rho": round(float(rho), 4),
        "rho_p": float(f"{p:.2e}"),
        "d_gen0_vs_gen2p": round(float(d), 4),
        "group": group
    }

drifting_expected = {'entropy_mean', 'ttr', 'hapax_ratio'}
stationary_expected = {'entropy_max', 'entropy_min', 'tail_decay'}
actual_drifting = {f for f, v in results["features"].items() if v["group"] == "drifting"}
actual_stationary = {f for f, v in results["features"].items() if v["group"] == "stationary"}
results["ddr_pattern_match"] = drifting_expected.issubset(actual_drifting) and stationary_expected.issubset(actual_stationary)
results["summary"] = f"DDR pattern {'CONFIRMED' if results['ddr_pattern_match'] else 'PARTIAL/ABSENT'} at 14.7B scale"

with open('results/exp_060_14b_ddr.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\n=== DDR Analysis: Qwen3-14B-Base ({results['n_samples']} samples) ===")
for feat, v in results["features"].items():
    print(f"  {feat:15s}: rho={v['rho']:+.4f}  d={v['d_gen0_vs_gen2p']:+.4f}  [{v['group']}]")
print(f"\nDDR pattern match: {results['ddr_pattern_match']}")
print(f"Summary: {results['summary']}")
