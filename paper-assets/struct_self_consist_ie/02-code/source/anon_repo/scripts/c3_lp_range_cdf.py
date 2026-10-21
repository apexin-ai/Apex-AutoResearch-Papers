import json
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict
import os

PROJ = "/root/autodl-tmp/struct_self_consist_ie"
SEED_FILES = {
    42: f"{PROJ}/output/exp_001_seed42_v2/samples.jsonl",
    123: f"{PROJ}/output/exp_001_seed123_v2/samples.jsonl",
    456: f"{PROJ}/output/exp_001_seed456_v2_ner/samples.jsonl",
}
N = 16

def entity_set(ents):
    return set((e["text"], e["type"], e["start"], e["end"]) for e in ents)

def compute_f1(pred_ents, gold_ents):
    pred = entity_set(pred_ents)
    gold = entity_set(gold_ents)
    if len(pred) == 0 and len(gold) == 0:
        return 1.0
    if len(pred) == 0 or len(gold) == 0:
        return 0.0
    tp = len(pred & gold)
    p = tp / len(pred)
    r = tp / len(gold)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

def load_seed(path):
    instances = []
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            lps = d["logprobs"]
            gold_ents = d["gold"]["entities"]
            f1s = [compute_f1(s["entities"], gold_ents) for s in d["samples"]]
            instances.append({
                "id": d["id"],
                "lps": np.array(lps),
                "f1s": np.array(f1s),
            })
    return instances

# Load data
print("Loading data...")
seed_data = {}
for seed, path in SEED_FILES.items():
    seed_data[seed] = load_seed(path)
    print(f"  Seed {seed}: {len(seed_data[seed])} instances")

results = {}

# === 1. LP range statistics ===
print("\n=== LP Range Statistics ===")
all_ranges = []
for seed, instances in seed_data.items():
    ranges = np.array([inst["lps"].max() - inst["lps"].min() for inst in instances])
    med = np.median(ranges)
    q1, q3 = np.percentile(ranges, [25, 75])
    iqr = q3 - q1
    results[f"seed{seed}_lp_range"] = {
        "median": float(med), "q1": float(q1), "q3": float(q3), "iqr": float(iqr),
        "mean": float(np.mean(ranges)), "std": float(np.std(ranges)),
        "min": float(np.min(ranges)), "max": float(np.max(ranges)),
    }
    all_ranges.extend(ranges.tolist())
    print(f"  Seed {seed}: median={med:.4f}, Q1={q1:.4f}, Q3={q3:.4f}, IQR={iqr:.4f}")

all_ranges = np.array(all_ranges)
med = np.median(all_ranges)
q1, q3 = np.percentile(all_ranges, [25, 75])
results["pooled_lp_range"] = {
    "median": float(med), "q1": float(q1), "q3": float(q3), "iqr": float(q3 - q1),
    "mean": float(np.mean(all_ranges)), "std": float(np.std(all_ranges)),
    "n_instances": len(all_ranges),
}
print(f"  Pooled: median={med:.4f}, Q1={q1:.4f}, Q3={q3:.4f}, IQR={q3-q1:.4f}")

# === 2. CDF Plot ===
print("\nGenerating CDF plot...")
fig_dir = f"{PROJ}/output/figures"
os.makedirs(fig_dir, exist_ok=True)

fig, ax = plt.subplots(1, 1, figsize=(7, 5))
colors = {42: '#1f77b4', 123: '#ff7f0e', 456: '#2ca02c'}
eps = 0.05

for seed, instances in seed_data.items():
    ranges = np.sort([inst["lps"].max() - inst["lps"].min() for inst in instances])
    cdf = np.arange(1, len(ranges)+1) / len(ranges)
    ax.plot(ranges, cdf, color=colors[seed], linewidth=1.5, label=f'Seed {seed}', alpha=0.7)

pooled_sorted = np.sort(all_ranges)
cdf_pooled = np.arange(1, len(pooled_sorted)+1) / len(pooled_sorted)
ax.plot(pooled_sorted, cdf_pooled, color='black', linewidth=2.0, label='Pooled (3 seeds)')

frac_below_eps = float(np.mean(all_ranges < eps))
ax.axvline(x=eps, color='red', linestyle='--', linewidth=1.2, alpha=0.8)
ax.text(eps + 0.002, 0.15, f'ε=0.05\n{frac_below_eps*100:.1f}% below',
        color='red', fontsize=9, va='bottom')
results["frac_below_eps005"] = frac_below_eps

for seed in seed_data:
    ranges_s = np.array([inst["lps"].max() - inst["lps"].min() for inst in seed_data[seed]])
    results[f"seed{seed}_frac_below_eps005"] = float(np.mean(ranges_s < eps))

ax.set_xlabel('Within-instance LP range (nats)', fontsize=12)
ax.set_ylabel('Cumulative fraction', fontsize=12)
ax.set_title('CDF of Within-Instance Mean Log-Prob Range\n(SciERC NER, Qwen3-8B, N=16)', fontsize=12)
ax.legend(fontsize=10, loc='lower right')
ax.set_xlim(left=0)
ax.set_ylim(0, 1.02)
ax.grid(True, alpha=0.3)
plt.tight_layout()
fig.savefig(f"{fig_dir}/lp_range_cdf_n16_3seed.pdf", dpi=300, bbox_inches='tight')
fig.savefig(f"{fig_dir}/lp_range_cdf_n16_3seed.png", dpi=300, bbox_inches='tight')
plt.close()
print(f"  Saved to {fig_dir}/lp_range_cdf_n16_3seed.{{pdf,png}}")

# === 3. Within-instance LP-F1 Spearman ρ ===
print("\n=== Spearman Correlations ===")

for seed, instances in seed_data.items():
    # 3a. Pooled: all (sample_lp, sample_f1) pairs
    all_lps_flat = np.concatenate([inst["lps"] for inst in instances])
    all_f1s_flat = np.concatenate([inst["f1s"] for inst in instances])
    rho_pooled, p_pooled = stats.spearmanr(all_lps_flat, all_f1s_flat)

    # 3b. Instance-level: ρ(LP_range, F1_range)
    lp_ranges = np.array([inst["lps"].max() - inst["lps"].min() for inst in instances])
    f1_ranges = np.array([inst["f1s"].max() - inst["f1s"].min() for inst in instances])
    rho_inst, p_inst = stats.spearmanr(lp_ranges, f1_ranges)

    # 3c. Per-instance: ρ(LP, F1) within each instance
    per_inst_rhos = []
    per_inst_pvals = []
    for inst in instances:
        if len(set(inst["lps"])) > 1 and len(set(inst["f1s"])) > 1:
            r, p = stats.spearmanr(inst["lps"], inst["f1s"])
            if not np.isnan(r):
                per_inst_rhos.append(r)
                per_inst_pvals.append(p)

    per_inst_rhos = np.array(per_inst_rhos)
    per_inst_pvals = np.array(per_inst_pvals)
    frac_sig = float(np.mean(per_inst_pvals < 0.05)) if len(per_inst_pvals) > 0 else 0.0

    results[f"seed{seed}_spearman"] = {
        "pooled_rho": float(rho_pooled),
        "pooled_p": float(p_pooled),
        "pooled_n_pairs": int(len(all_lps_flat)),
        "instance_level_rho_lprange_f1range": float(rho_inst),
        "instance_level_p": float(p_inst),
        "per_instance_mean_rho": float(np.mean(per_inst_rhos)),
        "per_instance_median_rho": float(np.median(per_inst_rhos)),
        "per_instance_std_rho": float(np.std(per_inst_rhos)),
        "per_instance_frac_significant_p005": frac_sig,
        "per_instance_n_computable": len(per_inst_rhos),
        "per_instance_n_total": len(instances),
    }

    print(f"\n  Seed {seed}:")
    print(f"    Pooled ρ={rho_pooled:.4f} (p={p_pooled:.2e}, n={len(all_lps_flat)})")
    print(f"    Instance-level ρ(LP_range, F1_range)={rho_inst:.4f} (p={p_inst:.2e})")
    print(f"    Per-instance: mean ρ={np.mean(per_inst_rhos):.4f}, median={np.median(per_inst_rhos):.4f}, "
          f"frac_sig={frac_sig:.3f} ({len(per_inst_rhos)}/{len(instances)} computable)")

# Pooled across all 3 seeds
all_lps_3seed = np.concatenate([np.concatenate([inst["lps"] for inst in instances]) for instances in seed_data.values()])
all_f1s_3seed = np.concatenate([np.concatenate([inst["f1s"] for inst in instances]) for instances in seed_data.values()])
rho_3seed, p_3seed = stats.spearmanr(all_lps_3seed, all_f1s_3seed)

all_lp_ranges_3seed = np.concatenate([np.array([inst["lps"].max() - inst["lps"].min() for inst in instances]) for instances in seed_data.values()])
all_f1_ranges_3seed = np.concatenate([np.array([inst["f1s"].max() - inst["f1s"].min() for inst in instances]) for instances in seed_data.values()])
rho_range_3seed, p_range_3seed = stats.spearmanr(all_lp_ranges_3seed, all_f1_ranges_3seed)

results["pooled_3seed_spearman"] = {
    "pooled_rho": float(rho_3seed),
    "pooled_p": float(p_3seed),
    "pooled_n_pairs": int(len(all_lps_3seed)),
    "instance_level_rho_lprange_f1range": float(rho_range_3seed),
    "instance_level_p": float(p_range_3seed),
}

print(f"\n  Pooled 3-seed: ρ={rho_3seed:.4f} (p={p_3seed:.2e}, n={len(all_lps_3seed)})")
print(f"  Pooled 3-seed instance-level ρ(LP_range, F1_range)={rho_range_3seed:.4f} (p={p_range_3seed:.2e})")

# Save JSON
out_path = f"{PROJ}/output/analysis_lp_range_cdf_n16_3seed.json"
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved results to {out_path}")
