#!/usr/bin/env python3
"""Per-generator TOST equivalence test for rebuttal."""
import argparse
import json, numpy as np, pandas as pd
from scipy import stats


def parse_args():
    parser = argparse.ArgumentParser(description="Per-generator TOST equivalence test.")
    parser.add_argument("--data-path", default="/root/gen-depth-fingerprint/data/features_8gen.csv")
    parser.add_argument("--margin", type=float, default=0.20, help="Cohen's d equivalence bound")
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--output", default="/root/gen-depth-fingerprint/results/tost_per_generator.json")
    return parser.parse_args()

args = parse_args()
df = pd.read_csv(args.data_path)

features_near_stat = ['entropy_max', 'tail_decay', 'entropy_min']
features_drifting = ['entropy_mean', 'ttr', 'hapax_ratio', 'entropy_std']
all_features = features_near_stat + features_drifting

d_bound = args.margin
results = {"equivalence_bound_d": d_bound, "per_generator": {}}

for gen in sorted(df['model_name'].unique()):
    gen_df = df[df['model_name'] == gen]
    gen1 = gen_df[gen_df['depth'] == 1]
    gen2p = gen_df[gen_df['depth'] >= 2]

    if len(gen1) < 10 or len(gen2p) < 10:
        continue

    gen_results = {"n_gen1": int(len(gen1)), "n_gen2p": int(len(gen2p)), "features": {}}

    for feat in all_features:
        if feat not in gen_df.columns:
            continue
        x1 = gen1[feat].dropna().values
        x2 = gen2p[feat].dropna().values
        n1, n2 = len(x1), len(x2)

        pooled_sd = np.sqrt(((n1-1)*x1.std(ddof=1)**2 + (n2-1)*x2.std(ddof=1)**2) / (n1+n2-2))
        delta = d_bound * pooled_sd
        diff = x1.mean() - x2.mean()
        se = pooled_sd * np.sqrt(1/n1 + 1/n2)
        dof = n1 + n2 - 2
        cohens_d = diff / pooled_sd if pooled_sd > 0 else 0

        t_lower = (diff + delta) / se
        p_lower = 1 - stats.t.cdf(t_lower, dof)
        t_upper = (diff - delta) / se
        p_upper = stats.t.cdf(t_upper, dof)
        p_tost = max(p_lower, p_upper)

        gen_results["features"][feat] = {
            "observed_d": round(float(cohens_d), 4),
            "p_tost": float(p_tost),
            "equivalent": bool(p_tost < args.alpha)
        }

    results["per_generator"][gen] = gen_results

out_path = args.output
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)

print(f"Per-generator TOST (d < {d_bound}):")
print(f"{'Generator':25s} | {'Feature':15s} | {'d_obs':>8s} | {'p_TOST':>10s} | {'Equiv?':>6s}")
print("-" * 75)
for gen, gdata in sorted(results["per_generator"].items()):
    for feat, fdata in sorted(gdata["features"].items()):
        eq = "YES" if fdata["equivalent"] else "NO"
        print(f"{gen:25s} | {feat:15s} | {fdata['observed_d']:+8.4f} | {fdata['p_tost']:10.2e} | {eq:>6s}")
    print("-" * 75)

# Summary stats
total_tests = sum(len(g["features"]) for g in results["per_generator"].values())
equiv_tests = sum(1 for g in results["per_generator"].values() for f in g["features"].values() if f["equivalent"])
print(f"\nSummary: {equiv_tests}/{total_tests} tests passed equivalence (p<0.05)")

# Per-feature summary
for feat in all_features:
    passed = sum(1 for g in results["per_generator"].values() if feat in g["features"] and g["features"][feat]["equivalent"])
    total = sum(1 for g in results["per_generator"].values() if feat in g["features"])
    if total > 0:
        print(f"  {feat:15s}: {passed}/{total} generators equivalent")

print(f"\nSaved to {out_path}")
