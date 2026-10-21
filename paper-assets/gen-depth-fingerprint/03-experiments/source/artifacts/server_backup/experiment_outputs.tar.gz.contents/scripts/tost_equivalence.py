#!/usr/bin/env python3
"""TOST equivalence test: gen-1 vs gen-2+ for all 7 features."""
import argparse
import json, numpy as np, pandas as pd
from scipy import stats


def parse_args():
    parser = argparse.ArgumentParser(description="TOST equivalence test: gen-1 vs gen-2+ for all 7 features.")
    parser.add_argument("--data-path", default="/root/gen-depth-fingerprint/data/features_8gen.csv")
    parser.add_argument("--margin", type=float, default=0.20, help="Cohen's d equivalence bound")
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--output", default="/root/gen-depth-fingerprint/results/tost_equivalence.json")
    return parser.parse_args()

args = parse_args()
df = pd.read_csv(args.data_path)

depth_col = 'depth' if 'depth' in df.columns else 'generation'
print(f"Depth column: {depth_col}")
print(f"Value counts:\n{df[depth_col].value_counts().sort_index()}")

gen1 = df[df[depth_col] == 1]
gen2p = df[df[depth_col] >= 2]
print(f"gen-1: {len(gen1)}, gen-2+: {len(gen2p)}")

features = {
    'entropy_mean': 'drifting',
    'entropy_std': 'intermediate',
    'entropy_max': 'near-stationary',
    'entropy_min': 'intermediate',
    'tail_decay': 'near-stationary',
    'ttr': 'drifting',
    'hapax_ratio': 'drifting',
}

d_bound = args.margin
results = {"equivalence_bound_d": d_bound, "alpha": args.alpha, "features": {}}

print(f"\n{'Feature':20s} | {'Group':16s} | {'d':>8s} | {'p_TOST':>12s} | Result")
print("-" * 80)

for feat, group in features.items():
    col = feat
    if col not in df.columns:
        for v in [feat, feat.replace('_', ''), feat.replace('_', '-')]:
            if v in df.columns:
                col = v
                break
        else:
            print(f"{feat:20s} | COLUMN NOT FOUND, skipping")
            continue

    x1 = gen1[col].dropna().values.astype(float)
    x2 = gen2p[col].dropna().values.astype(float)
    n1, n2 = len(x1), len(x2)

    s1, s2 = x1.std(ddof=1), x2.std(ddof=1)
    pooled_sd = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))

    delta = d_bound * pooled_sd
    diff = x1.mean() - x2.mean()
    se = pooled_sd * np.sqrt(1/n1 + 1/n2)
    dof = n1 + n2 - 2
    cohens_d = diff / pooled_sd

    t_lower = (diff + delta) / se
    p_lower = 1 - stats.t.cdf(t_lower, dof)

    t_upper = (diff - delta) / se
    p_upper = stats.t.cdf(t_upper, dof)

    p_tost = max(p_lower, p_upper)
    equivalent = bool(p_tost < args.alpha)

    results["features"][feat] = {
        "group": group,
        "n_gen1": int(n1), "n_gen2p": int(n2),
        "mean_gen1": round(float(x1.mean()), 6),
        "mean_gen2p": round(float(x2.mean()), 6),
        "mean_diff": round(float(diff), 6),
        "pooled_sd": round(float(pooled_sd), 6),
        "observed_d": round(float(cohens_d), 4),
        "delta_raw": round(float(delta), 6),
        "t_lower": round(float(t_lower), 4),
        "p_lower": float(p_lower),
        "t_upper": round(float(t_upper), 4),
        "p_upper": float(p_upper),
        "p_tost": float(p_tost),
        "equivalent_at_alpha_005": equivalent
    }

    tag = "EQUIV" if equivalent else "NOT"
    print(f"{feat:20s} | {group:16s} | {cohens_d:+8.4f} | {p_tost:12.2e} | {tag}")

out_path = args.output
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved: {out_path}")
