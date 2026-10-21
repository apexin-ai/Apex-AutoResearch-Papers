"""
ddr_temp_analysis.py — Temperature ablation analysis for differential depth response.

Computes Cohen's d (gen-1 vs gen-2+) for each feature across 4 generators
at 3 temperature settings (0.5, 0.7, 0.9) to verify that the drifting/stationary
partition is stable across sampling temperatures.
"""
import os
import pandas as pd
import numpy as np

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "..", "data")

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay", "ttr", "hapax_ratio"]

file_map = {
    ("qwen3-1.7b", 0.5): ("features_qwen3-1.7b-low-temp.csv", True),
    ("qwen3-1.7b", 0.7): ("features_qwen3-1.7b.csv", True),
    ("qwen3-1.7b", 0.9): ("features_qwen3-1.7b-t09.csv", False),
    ("qwen3-0.6b", 0.5): ("features_qwen3-0.6b-t05.csv", False),
    ("qwen3-0.6b", 0.7): ("features_qwen3-0.6b.csv", True),
    ("qwen3-0.6b", 0.9): ("features_qwen3-0.6b-t09.csv", False),
    ("pythia-2.8b", 0.5): ("features_pythia-2.8b-t05.csv", False),
    ("pythia-2.8b", 0.7): ("features_pythia-2.8b.csv", True),
    ("pythia-2.8b", 0.9): ("features_pythia-2.8b-t09.csv", False),
    ("olmo-2-1b", 0.5): ("features_olmo-2-1b-t05.csv", False),
    ("olmo-2-1b", 0.7): ("features_olmo-2-1b.csv", True),
    ("olmo-2-1b", 0.9): ("features_olmo-2-1b-t09.csv", False),
}


def cohens_d_pooled(g1, g2):
    n1, n2 = len(g1), len(g2)
    if n1 < 2 or n2 < 2:
        return np.nan
    m1, m2 = g1.mean(), g2.mean()
    s1, s2 = g1.std(ddof=1), g2.std(ddof=1)
    pooled = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    if pooled == 0:
        return 0.0
    return (m2 - m1) / pooled


def main():
    results = []

    for (gen, temp), (fname, has_model) in file_map.items():
        path = os.path.join(DATA_DIR, fname)
        df = pd.read_csv(path)

        if not has_model:
            if 'model_name' not in df.columns:
                df = df.rename(columns={'id': 'row_id'})

        df = df[df["depth"] >= 1].copy()

        gen1 = df[df["depth"] == 1]
        gen2plus = df[df["depth"] >= 2]

        for feat in FEATURES:
            d = cohens_d_pooled(gen1[feat].dropna(), gen2plus[feat].dropna())
            abs_d = abs(d)
            if abs_d > 0.5:
                label = "drifting"
            elif abs_d > 0.1:
                label = "intermediate"
            else:
                label = "near-stationary"
            results.append({
                "generator": gen,
                "temperature": temp,
                "feature": feat,
                "cohens_d": round(d, 4),
                "abs_cohens_d": round(abs_d, 4),
                "partition_label": label
            })

    rdf = pd.DataFrame(results)
    out_csv = os.path.join(DATA_DIR, "ddr_temperature_stability.csv")
    rdf.to_csv(out_csv, index=False)

    print("=== FULL RESULTS ===")
    print(rdf.to_string(index=False))

    print("\n=== PARTITION SUMMARY ===")
    for temp in [0.5, 0.7, 0.9]:
        print(f"\n--- Temperature {temp} ---")
        for gen in ["pythia-2.8b", "qwen3-0.6b", "qwen3-1.7b", "olmo-2-1b"]:
            sub = rdf[(rdf["generator"] == gen) & (rdf["temperature"] == temp)]
            d_feats = sub[sub["partition_label"] == "drifting"]["feature"].tolist()
            i_feats = sub[sub["partition_label"] == "intermediate"]["feature"].tolist()
            s_feats = sub[sub["partition_label"] == "near-stationary"]["feature"].tolist()
            print(f"  {gen}: D={len(d_feats)} I={len(i_feats)} S={len(s_feats)}  |  D={d_feats}  I={i_feats}  S={s_feats}")

    print("\n=== 3/1/3 STABILITY CHECK ===")
    for (gen, temp), grp in rdf.groupby(["generator", "temperature"]):
        counts = grp["partition_label"].value_counts()
        d = counts.get("drifting", 0)
        i = counts.get("intermediate", 0)
        s = counts.get("near-stationary", 0)
        is_313 = (d == 3 and i == 1 and s == 3)
        status = "3/1/3" if is_313 else "NOT 3/1/3"
        print(f"  {gen} t={temp}: {d}/{i}/{s} {status}")

    print("\n=== D-VALUE RANGES BY PARTITION ===")
    for temp in [0.5, 0.7, 0.9]:
        sub = rdf[rdf["temperature"] == temp]
        for label in ["drifting", "intermediate", "near-stationary"]:
            part = sub[sub["partition_label"] == label]
            if len(part) > 0:
                print(f"  t={temp} {label}: |d| in [{part['abs_cohens_d'].min():.3f}, {part['abs_cohens_d'].max():.3f}], mean={part['abs_cohens_d'].mean():.3f}")

    print(f"\nResults saved to {out_csv}")


if __name__ == "__main__":
    main()
