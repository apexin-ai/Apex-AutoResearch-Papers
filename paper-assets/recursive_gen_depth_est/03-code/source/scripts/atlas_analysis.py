"""
Depth Degradation Atlas v1 Analysis

Input:  Feature JSONL files from 4 completed chains (Pythia nucleus/temp09, OLMo nucleus, GPT-2 XL nucleus).
        Each JSONL: {depth, sample_id, <19 features>} with depths 0-3, ~5000 samples/depth.
Output: artifacts/atlas/{monotonicity_scores,edd_matrix,heatmap_data,feature_consistency}.json

Modules:
  1. Monotonicity: Spearman rho + Kendall tau per feature per chain
  2. EDD: Effective Degradation Distance (depth at which feature change saturates)
  3. Heatmap: z-scored feature x model x depth matrix
  4. Feature Consistency: Jaccard + rank correlation of importance across nucleus models
"""

import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path("/root/autodl-tmp/recursive_gen_depth_est")
OUT = ROOT / "artifacts" / "atlas"

CHAINS = {
    "pythia_nucleus": ROOT / "data" / "features_all.jsonl",
    "pythia_temp09":  ROOT / "data" / "pythia_temp09" / "features.jsonl",
    "olmo_nucleus":   ROOT / "data" / "olmo" / "features.jsonl",
    "gpt2xl_nucleus": ROOT / "data" / "gpt2xl" / "features.jsonl",
}

FEATURE_COLS = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

NUCLEUS_CHAINS = ["pythia_nucleus", "olmo_nucleus", "gpt2xl_nucleus"]

KNOWN_TOP5 = {
    "pythia_nucleus": ["var_surprisal", "p90_ppl", "mean_ppl", "mean_surprisal", "p75_ppl"],
    "olmo_nucleus":   ["p90_ppl", "var_surprisal", "p75_ppl", "mean_surprisal", "type_token_ratio"],
    "gpt2xl_nucleus": ["p90_ppl", "var_surprisal", "p75_ppl", "mean_surprisal", "mean_ppl"],
}

IMPORTANCE_FILES = {
    "pythia_nucleus": ROOT / "results" / "feature_importance.json",
    "pythia_temp09":  ROOT / "results" / "pythia_temp09" / "feature_importance.json",
    "olmo_nucleus":   ROOT / "results" / "olmo" / "feature_importance.json",
    "gpt2xl_nucleus": ROOT / "results" / "gpt2xl" / "feature_importance.json",
}


def load_chain(path: Path) -> pd.DataFrame:
    records = []
    with open(path) as f:
        for line in f:
            records.append(json.loads(line))
    return pd.DataFrame(records)


def compute_monotonicity(chains_data: dict[str, pd.DataFrame]) -> dict:
    results = {}
    for chain_name, df in chains_data.items():
        chain_res = {}
        for feat in FEATURE_COLS:
            rho, p_rho = stats.spearmanr(df["depth"], df[feat])
            tau, p_tau = stats.kendalltau(df["depth"], df[feat])
            chain_res[feat] = {
                "spearman_rho": round(float(rho), 6),
                "spearman_p": float(p_rho),
                "kendall_tau": round(float(tau), 6),
                "kendall_p": float(p_tau),
            }
        results[chain_name] = chain_res
    return results


def compute_edd(chains_data: dict[str, pd.DataFrame]) -> dict:
    results = {}
    for chain_name, df in chains_data.items():
        depths = sorted(df["depth"].unique())
        depth_means = {}
        for d in depths:
            depth_means[d] = df[df["depth"] == d][FEATURE_COLS].mean()

        chain_res = {}
        for feat in FEATURE_COLS:
            means = [depth_means[d][feat] for d in depths]
            deltas = [abs(means[i + 1] - means[i]) for i in range(len(means) - 1)]
            if len(deltas) == 0 or deltas[0] == 0:
                chain_res[feat] = {"edd": 1, "deltas": [round(float(d), 6) for d in deltas]}
                continue

            eps = 0.05 * deltas[0]
            edd = len(depths) - 1  # max depth transition
            for i, delta in enumerate(deltas):
                if delta < eps:
                    edd = i + 1  # depth transition index where saturation occurs
                    break

            chain_res[feat] = {
                "edd": edd,
                "epsilon": round(float(eps), 6),
                "deltas": [round(float(d), 6) for d in deltas],
                "depth_means": [round(float(m), 6) for m in means],
            }
        results[chain_name] = chain_res
    return results


def compute_heatmap(chains_data: dict[str, pd.DataFrame]) -> dict:
    all_means = {}
    for chain_name, df in chains_data.items():
        depths = sorted(df["depth"].unique())
        chain_means = {}
        for d in depths:
            subset = df[df["depth"] == d][FEATURE_COLS]
            chain_means[str(d)] = {f: float(subset[f].mean()) for f in FEATURE_COLS}
        all_means[chain_name] = chain_means

    depths = sorted(list(chains_data.values())[0]["depth"].unique())
    zscored = {}
    for feat in FEATURE_COLS:
        vals = []
        for chain_name in chains_data:
            for d in depths:
                vals.append(all_means[chain_name][str(d)][feat])
        vals = np.array(vals)
        mu, sigma = vals.mean(), vals.std()
        if sigma == 0:
            sigma = 1.0

        feat_data = {}
        for chain_name in chains_data:
            feat_data[chain_name] = {}
            for d in depths:
                raw = all_means[chain_name][str(d)][feat]
                feat_data[chain_name][str(d)] = {
                    "raw": round(raw, 6),
                    "zscore": round((raw - mu) / sigma, 6),
                }
        zscored[feat] = feat_data

    return {"features": zscored, "models": list(chains_data.keys()), "depths": [str(d) for d in depths]}


def compute_feature_consistency() -> dict:
    importance = {}
    for chain_name, path in IMPORTANCE_FILES.items():
        if chain_name in NUCLEUS_CHAINS and path.exists():
            with open(path) as f:
                importance[chain_name] = json.load(f)

    # Jaccard of top-5
    top5_sets = {k: set(v) for k, v in KNOWN_TOP5.items()}
    pairs = []
    for i, m1 in enumerate(NUCLEUS_CHAINS):
        for m2 in NUCLEUS_CHAINS[i + 1:]:
            inter = len(top5_sets[m1] & top5_sets[m2])
            union = len(top5_sets[m1] | top5_sets[m2])
            pairs.append({
                "pair": f"{m1}_vs_{m2}",
                "jaccard": round(inter / union, 4),
                "intersection": sorted(top5_sets[m1] & top5_sets[m2]),
                "union": sorted(top5_sets[m1] | top5_sets[m2]),
            })

    all_top5 = set()
    for v in top5_sets.values():
        all_top5 |= v
    three_way_jaccard = len(top5_sets["pythia_nucleus"] & top5_sets["olmo_nucleus"] & top5_sets["gpt2xl_nucleus"]) / len(all_top5)

    # Rank correlation of full importance vectors
    rank_corrs = []
    for i, m1 in enumerate(NUCLEUS_CHAINS):
        for m2 in NUCLEUS_CHAINS[i + 1:]:
            if m1 in importance and m2 in importance:
                ranks1 = [importance[m1].get(f, 0) for f in FEATURE_COLS]
                ranks2 = [importance[m2].get(f, 0) for f in FEATURE_COLS]
                rho, p_val = stats.spearmanr(ranks1, ranks2)
                rank_corrs.append({
                    "pair": f"{m1}_vs_{m2}",
                    "spearman_rho": round(float(rho), 6),
                    "p_value": float(p_val),
                })

    return {
        "top5_known": KNOWN_TOP5,
        "pairwise_jaccard": pairs,
        "three_way_jaccard": round(three_way_jaccard, 4),
        "three_way_intersection": sorted(top5_sets["pythia_nucleus"] & top5_sets["olmo_nucleus"] & top5_sets["gpt2xl_nucleus"]),
        "rank_correlations": rank_corrs,
    }


def save_json(data, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  -> {path}")


def main():
    print("=" * 60)
    print("Depth Degradation Atlas v1")
    print("=" * 60)

    # Load data
    print("\n[1/5] Loading chains...")
    chains_data = {}
    for name, path in CHAINS.items():
        if not path.exists():
            print(f"  SKIP {name}: {path} not found")
            continue
        df = load_chain(path)
        chains_data[name] = df
        depths = sorted(df["depth"].unique())
        print(f"  {name}: {len(df)} samples, depths={depths}")

    if not chains_data:
        print("ERROR: No data loaded")
        sys.exit(1)

    # 1. Monotonicity
    print("\n[2/5] Computing monotonicity scores...")
    mono = compute_monotonicity(chains_data)
    save_json(mono, OUT / "monotonicity_scores.json")

    # Print summary
    for chain_name in chains_data:
        top_feats = sorted(mono[chain_name].items(), key=lambda x: abs(x[1]["spearman_rho"]), reverse=True)[:5]
        top_str = ", ".join(f"{f}={v['spearman_rho']:.3f}" for f, v in top_feats)
        print(f"  {chain_name} top-5 |rho|: {top_str}")

    # 2. EDD
    print("\n[3/5] Computing EDD matrix...")
    edd = compute_edd(chains_data)
    save_json(edd, OUT / "edd_matrix.json")

    # Print summary
    for chain_name in chains_data:
        edd_vals = {f: v["edd"] for f, v in edd[chain_name].items()}
        early = [f for f, e in edd_vals.items() if e == 1]
        late = [f for f, e in edd_vals.items() if e == 3]
        print(f"  {chain_name}: early_saturate(edd=1)={len(early)}, late(edd=3)={len(late)}")

    # 3. Heatmap
    print("\n[4/5] Computing heatmap data...")
    heatmap = compute_heatmap(chains_data)
    save_json(heatmap, OUT / "heatmap_data.json")
    print(f"  {len(heatmap['features'])} features x {len(heatmap['models'])} models x {len(heatmap['depths'])} depths")

    # 4. Feature consistency
    print("\n[5/5] Computing feature importance consistency...")
    consistency = compute_feature_consistency()
    save_json(consistency, OUT / "feature_consistency.json")

    print(f"  3-way intersection: {consistency['three_way_intersection']}")
    print(f"  3-way Jaccard: {consistency['three_way_jaccard']}")
    for rc in consistency["rank_correlations"]:
        print(f"  {rc['pair']}: rho={rc['spearman_rho']:.4f} (p={rc['p_value']:.2e})")

    # Final summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Chains analyzed: {len(chains_data)}")
    print(f"Features: {len(FEATURE_COLS)}")
    print(f"Output dir: {OUT}")
    print("Files:")
    for fname in ["monotonicity_scores.json", "edd_matrix.json", "heatmap_data.json", "feature_consistency.json"]:
        fpath = OUT / fname
        size = fpath.stat().st_size if fpath.exists() else 0
        print(f"  {fname}: {size:,} bytes")


if __name__ == "__main__":
    main()
