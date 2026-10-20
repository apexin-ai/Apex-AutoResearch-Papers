"""
Subset distribution analysis for reviewer W5.
Compares 300-item random subset vs full MMLU (14042 items)
on difficulty, domain, and discrimination distributions.
"""
import csv
import json
import os
import sys
import numpy as np
from scipy import stats
from collections import Counter

# === Load item metadata (subject, domain, difficulty for all 14042 MMLU items) ===
META_FILE = "/root/contamcal-irt-calibration/analysis/irt_data/mmlu/item_metadata.csv"
AGG_FILE = "/root/autodl-tmp/exp002/signals/rrf/exposure_aggregated.json"

items = []
with open(META_FILE) as f:
    reader = csv.DictReader(f)
    for row in reader:
        items.append({
            "item_id": int(row["item_id"]),
            "subject": row["subject"],
            "domain": row["domain"],
            "difficulty": float(row["difficulty_baseline"]),
        })

N_total = len(items)
print(f"Total MMLU items: {N_total}")

# Load aggregated RRF exposure scores
with open(AGG_FILE) as f:
    agg_data = json.load(f)

mmlu_rrf = np.array(agg_data["mmlu"])
print(f"Aggregated RRF scores: {len(mmlu_rrf)} items")

# === Determine the 300-item subset (random subsample, seed=42) ===
np.random.seed(42)
subset_idx_random = np.sort(np.random.choice(N_total, 300, replace=False))
print(f"\nRandom 300-item subset (seed=42): indices {subset_idx_random[:5]}...{subset_idx_random[-5:]}")

# Also compute top-300 by aggregated RRF score (for comparison)
top300_rrf_idx = np.argsort(-mmlu_rrf)[:300]
top300_rrf_idx_sorted = np.sort(top300_rrf_idx)
print(f"Top-300 by RRF score: indices {top300_rrf_idx_sorted[:5]}...{top300_rrf_idx_sorted[-5:]}")

# === Helper functions ===
def get_subset(items, indices):
    return [items[i] for i in indices]

def domain_counts(item_list):
    return Counter(it["domain"] for it in item_list)

def difficulty_stats(item_list):
    diffs = [it["difficulty"] for it in item_list]
    return {
        "mean": np.mean(diffs),
        "std": np.std(diffs),
        "median": np.median(diffs),
        "q25": np.percentile(diffs, 25),
        "q75": np.percentile(diffs, 75),
        "min": np.min(diffs),
        "max": np.max(diffs),
    }

# === Analysis for both subsets ===
results = {}

for label, idx in [("random_300", subset_idx_random), ("rrf_top300", top300_rrf_idx_sorted)]:
    subset = get_subset(items, idx)
    
    # --- Difficulty distribution ---
    full_diff = [it["difficulty"] for it in items]
    sub_diff = [it["difficulty"] for it in subset]
    
    full_stats = difficulty_stats(items)
    sub_stats = difficulty_stats(subset)
    
    ks_stat, ks_p = stats.ks_2samp(full_diff, sub_diff)
    
    # Cohen's d (effect size)
    pooled_std = np.sqrt((np.std(full_diff)**2 + np.std(sub_diff)**2) / 2)
    cohens_d = (np.mean(sub_diff) - np.mean(full_diff)) / pooled_std if pooled_std > 0 else 0
    
    # --- Domain distribution ---
    full_domains = domain_counts(items)
    sub_domains = domain_counts(subset)
    
    domain_order = sorted(full_domains.keys())
    
    # Chi-square test
    observed = np.array([sub_domains.get(d, 0) for d in domain_order])
    expected_prop = np.array([full_domains[d] / N_total for d in domain_order])
    expected = expected_prop * len(subset)
    chi2, chi2_p = stats.chisquare(observed, f_exp=expected)
    
    # Cramer's V (effect size for chi-square)
    k = len(domain_order)
    n = len(subset)
    cramers_v = np.sqrt(chi2 / (n * (k - 1))) if n * (k - 1) > 0 else 0
    
    # --- Subject distribution ---
    full_subjects = Counter(it["subject"] for it in items)
    sub_subjects = Counter(it["subject"] for it in subset)
    
    # Number of subjects represented
    n_subjects_full = len(full_subjects)
    n_subjects_sub = len(sub_subjects)
    
    # --- RRF score distribution for subset vs rest ---
    sub_rrf = mmlu_rrf[idx]
    rest_idx = np.setdiff1d(np.arange(N_total), idx)
    rest_rrf = mmlu_rrf[rest_idx]
    rrf_ks, rrf_ks_p = stats.ks_2samp(sub_rrf, rest_rrf)
    
    # --- Difficulty histogram bins ---
    bins = [0.0, 0.2, 0.4, 0.6, 0.8, 1.01]
    bin_labels = ["[0, 0.2)", "[0.2, 0.4)", "[0.4, 0.6)", "[0.6, 0.8)", "[0.8, 1.0]"]
    full_hist, _ = np.histogram(full_diff, bins=bins)
    sub_hist, _ = np.histogram(sub_diff, bins=bins)
    
    result = {
        "label": label,
        "n_subset": len(subset),
        "difficulty": {
            "full": full_stats,
            "subset": sub_stats,
            "ks_stat": ks_stat,
            "ks_p": ks_p,
            "cohens_d": cohens_d,
            "full_hist": full_hist.tolist(),
            "sub_hist": sub_hist.tolist(),
            "bin_labels": bin_labels,
        },
        "domain": {
            "full_counts": {d: full_domains[d] for d in domain_order},
            "sub_counts": {d: sub_domains.get(d, 0) for d in domain_order},
            "full_pct": {d: 100 * full_domains[d] / N_total for d in domain_order},
            "sub_pct": {d: 100 * sub_domains.get(d, 0) / len(subset) for d in domain_order},
            "chi2": chi2,
            "chi2_p": chi2_p,
            "cramers_v": cramers_v,
        },
        "subject": {
            "n_full": n_subjects_full,
            "n_subset": n_subjects_sub,
            "coverage": n_subjects_sub / n_subjects_full,
        },
        "rrf_score": {
            "sub_mean": float(np.mean(sub_rrf)),
            "sub_std": float(np.std(sub_rrf)),
            "rest_mean": float(np.mean(rest_rrf)),
            "rest_std": float(np.std(rest_rrf)),
            "ks_stat": rrf_ks,
            "ks_p": rrf_ks_p,
        },
    }
    results[label] = result

# === Print report ===
print("\n" + "=" * 80)
print("SUBSET DISTRIBUTION ANALYSIS — MMLU 300-item subset vs Full 14042")
print("=" * 80)

for label in ["random_300", "rrf_top300"]:
    r = results[label]
    print(f"\n{'─' * 80}")
    print(f"  Subset: {label} (n={r['n_subset']})")
    print(f"{'─' * 80}")
    
    # Difficulty
    d = r["difficulty"]
    print(f"\n  DIFFICULTY (d000 baseline accuracy):")
    print(f"  {'':20s} {'Full (14042)':>15s} {'Subset (300)':>15s}")
    print(f"  {'Mean':20s} {d['full']['mean']:>15.4f} {d['subset']['mean']:>15.4f}")
    print(f"  {'Std':20s} {d['full']['std']:>15.4f} {d['subset']['std']:>15.4f}")
    print(f"  {'Median':20s} {d['full']['median']:>15.4f} {d['subset']['median']:>15.4f}")
    print(f"  {'Q25':20s} {d['full']['q25']:>15.4f} {d['subset']['q25']:>15.4f}")
    print(f"  {'Q75':20s} {d['full']['q75']:>15.4f} {d['subset']['q75']:>15.4f}")
    print(f"\n  KS test: D={d['ks_stat']:.4f}, p={d['ks_p']:.4f}")
    print(f"  Cohen's d: {d['cohens_d']:.4f}")
    
    print(f"\n  Difficulty histogram:")
    print(f"  {'Bin':15s} {'Full %':>10s} {'Sub %':>10s} {'Δ':>8s}")
    for i, bl in enumerate(d["bin_labels"]):
        fp = 100 * d["full_hist"][i] / sum(d["full_hist"])
        sp = 100 * d["sub_hist"][i] / sum(d["sub_hist"])
        print(f"  {bl:15s} {fp:>10.1f} {sp:>10.1f} {sp - fp:>+8.1f}")
    
    # Domain
    dm = r["domain"]
    print(f"\n  DOMAIN DISTRIBUTION:")
    print(f"  {'Domain':20s} {'Full %':>10s} {'Sub %':>10s} {'Δ':>8s} {'Full N':>8s} {'Sub N':>8s}")
    for d_name in sorted(dm["full_pct"].keys()):
        fp = dm["full_pct"][d_name]
        sp = dm["sub_pct"][d_name]
        fc = dm["full_counts"][d_name]
        sc = dm["sub_counts"][d_name]
        print(f"  {d_name:20s} {fp:>10.1f} {sp:>10.1f} {sp - fp:>+8.1f} {fc:>8d} {sc:>8d}")
    
    print(f"\n  Chi-square: χ²={dm['chi2']:.4f}, p={dm['chi2_p']:.4f}")
    print(f"  Cramér's V: {dm['cramers_v']:.4f}")
    
    # Subject coverage
    s = r["subject"]
    print(f"\n  SUBJECT COVERAGE: {s['n_subset']}/{s['n_full']} subjects ({100*s['coverage']:.1f}%)")
    
    # RRF scores
    rrf = r["rrf_score"]
    print(f"\n  RRF SCORE DISTRIBUTION:")
    print(f"  Subset mean: {rrf['sub_mean']:.4f} ± {rrf['sub_std']:.4f}")
    print(f"  Rest mean:   {rrf['rest_mean']:.4f} ± {rrf['rest_std']:.4f}")
    print(f"  KS test: D={rrf['ks_stat']:.4f}, p={rrf['ks_p']:.6f}")

# === Save JSON results ===
output_file = "/root/contamcal-irt-calibration/analysis/subset_distribution_results.json"
# Convert numpy types for JSON
def convert(obj):
    if isinstance(obj, (np.int64, np.int32)):
        return int(obj)
    if isinstance(obj, (np.float64, np.float32)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj

import json as json_mod
class NpEncoder(json_mod.JSONEncoder):
    def default(self, obj):
        return convert(obj)

with open(output_file, "w") as f:
    json.dump(results, f, indent=2, cls=NpEncoder)
print(f"\nResults saved to {output_file}")

# === Generate visualization ===
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("300-item Subset Distribution Analysis (MMLU)", fontsize=14, fontweight='bold')
    
    # --- Panel A: Difficulty histogram (random_300) ---
    ax = axes[0, 0]
    r = results["random_300"]
    d = r["difficulty"]
    x = np.arange(len(d["bin_labels"]))
    w = 0.35
    full_pct = 100 * np.array(d["full_hist"]) / sum(d["full_hist"])
    sub_pct = 100 * np.array(d["sub_hist"]) / sum(d["sub_hist"])
    ax.bar(x - w/2, full_pct, w, label=f"Full (N={N_total})", color="#4878CF", alpha=0.8)
    ax.bar(x + w/2, sub_pct, w, label=f"Subset (n=300)", color="#D65F5F", alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(d["bin_labels"], fontsize=8)
    ax.set_ylabel("Percentage (%)")
    ax.set_title(f"A. Difficulty Distribution\n(KS D={d['ks_stat']:.3f}, p={d['ks_p']:.3f})")
    ax.legend(fontsize=8)
    
    # --- Panel B: Domain proportions (random_300) ---
    ax = axes[0, 1]
    dm = r["domain"]
    domains = sorted(dm["full_pct"].keys())
    x = np.arange(len(domains))
    full_pct_d = [dm["full_pct"][d] for d in domains]
    sub_pct_d = [dm["sub_pct"][d] for d in domains]
    ax.bar(x - w/2, full_pct_d, w, label=f"Full", color="#4878CF", alpha=0.8)
    ax.bar(x + w/2, sub_pct_d, w, label=f"Subset", color="#D65F5F", alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(domains, fontsize=8, rotation=15)
    ax.set_ylabel("Percentage (%)")
    ax.set_title(f"B. Domain Distribution\n(χ²={dm['chi2']:.2f}, p={dm['chi2_p']:.3f})")
    ax.legend(fontsize=8)
    
    # --- Panel C: Difficulty histogram (rrf_top300) ---
    ax = axes[1, 0]
    r2 = results["rrf_top300"]
    d2 = r2["difficulty"]
    full_pct2 = 100 * np.array(d2["full_hist"]) / sum(d2["full_hist"])
    sub_pct2 = 100 * np.array(d2["sub_hist"]) / sum(d2["sub_hist"])
    ax.bar(x[:len(d2["bin_labels"])] - w/2, full_pct2, w, label="Full", color="#4878CF", alpha=0.8)
    ax.bar(x[:len(d2["bin_labels"])] + w/2, sub_pct2, w, label="RRF Top-300", color="#6ACC65", alpha=0.8)
    ax.set_xticks(x[:len(d2["bin_labels"])])
    ax.set_xticklabels(d2["bin_labels"], fontsize=8)
    ax.set_ylabel("Percentage (%)")
    ax.set_title(f"C. Difficulty (RRF Top-300)\n(KS D={d2['ks_stat']:.3f}, p={d2['ks_p']:.4f})")
    ax.legend(fontsize=8)
    
    # --- Panel D: Domain proportions (rrf_top300) ---
    ax = axes[1, 1]
    dm2 = r2["domain"]
    domains2 = sorted(dm2["full_pct"].keys())
    full_pct_d2 = [dm2["full_pct"][d] for d in domains2]
    sub_pct_d2 = [dm2["sub_pct"][d] for d in domains2]
    ax.bar(x[:len(domains2)] - w/2, full_pct_d2, w, label="Full", color="#4878CF", alpha=0.8)
    ax.bar(x[:len(domains2)] + w/2, sub_pct_d2, w, label="RRF Top-300", color="#6ACC65", alpha=0.8)
    ax.set_xticks(x[:len(domains2)])
    ax.set_xticklabels(domains2, fontsize=8, rotation=15)
    ax.set_ylabel("Percentage (%)")
    ax.set_title(f"D. Domain (RRF Top-300)\n(χ²={dm2['chi2']:.2f}, p={dm2['chi2_p']:.3f})")
    ax.legend(fontsize=8)
    
    plt.tight_layout()
    fig_path = "/root/contamcal-irt-calibration/analysis/subset_distribution_analysis.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.savefig(fig_path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Figure saved to {fig_path}")
except Exception as e:
    print(f"Visualization failed: {e}")

print("\nDone.")
