"""
analyze_instruct_ref_ddr.py — Compare DDR signal: base-ref (Pythia-410M) vs instruct-ref (Qwen3-0.6B).

Metrics per feature per generator:
  - Spearman rho (feature vs depth)
  - Cohen's d (depth 0 vs depth 4 effect size)

Output: results/instruct_ref_ddr_comparison.json
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

FEATURES = ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "tail_decay", "ttr", "hapax_ratio"]

GENERATORS = {
    "qwen3-1.7b-instruct": "data/features_qwen3-1.7b-instruct.csv",
    "olmo-2-0425-1b-instruct": "data/features_olmo-2-0425-1b-instruct.csv",
}


def spearman_rho(df, feat):
    r, p = stats.spearmanr(df["depth"], df[feat])
    return float(r), float(p)


def cohens_d(df, feat, d0=0, d1=4):
    g0 = df.loc[df["depth"] == d0, feat].dropna()
    g1 = df.loc[df["depth"] == d1, feat].dropna()
    if len(g0) < 2 or len(g1) < 2:
        return 0.0
    pooled_std = np.sqrt(((len(g0)-1)*g0.std()**2 + (len(g1)-1)*g1.std()**2) / (len(g0)+len(g1)-2))
    if pooled_std == 0:
        return 0.0
    return float((g1.mean() - g0.mean()) / pooled_std)


def analyze_generator(gen_name, base_df, inst_df):
    result = {}
    for feat in FEATURES:
        base_rho, base_p = spearman_rho(base_df, feat)
        base_d = cohens_d(base_df, feat)
        inst_rho, inst_p = spearman_rho(inst_df, feat)
        inst_d = cohens_d(inst_df, feat)
        result[feat] = {
            "base_ref_rho": round(base_rho, 4),
            "base_ref_rho_p": round(base_p, 4),
            "base_ref_d": round(base_d, 4),
            "instruct_ref_rho": round(inst_rho, 4),
            "instruct_ref_rho_p": round(inst_p, 4),
            "instruct_ref_d": round(inst_d, 4),
            "rho_delta": round(inst_rho - base_rho, 4),
            "d_delta": round(abs(inst_d) - abs(base_d), 4),
        }
    return result


def main():
    root = Path(__file__).resolve().parent.parent
    inst_all = pd.read_csv(root / "data" / "features_instruct_ref_qwen06b.csv")

    results = {}
    for gen_name, base_path in GENERATORS.items():
        base_df = pd.read_csv(root / base_path)
        inst_df = inst_all[inst_all["generator"] == gen_name].copy()
        print(f"{gen_name}: base_ref={len(base_df)}, instruct_ref={len(inst_df)}")
        results[gen_name] = analyze_generator(gen_name, base_df, inst_df)

    # Summary table
    print("\n" + "="*100)
    print(f"{'Generator':<30} {'Feature':<16} {'Base ρ':>8} {'Inst ρ':>8} {'Δρ':>8} {'Base |d|':>10} {'Inst |d|':>10} {'Δ|d|':>8}")
    print("-"*100)
    for gen_name, feats in results.items():
        for feat, v in feats.items():
            print(f"{gen_name:<30} {feat:<16} {v['base_ref_rho']:>8.4f} {v['instruct_ref_rho']:>8.4f} "
                  f"{v['rho_delta']:>8.4f} {abs(v['base_ref_d']):>10.4f} {abs(v['instruct_ref_d']):>10.4f} "
                  f"{v['d_delta']:>8.4f}")
        print()

    out_path = root / "results" / "instruct_ref_ddr_comparison.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
