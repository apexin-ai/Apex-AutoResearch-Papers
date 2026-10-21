"""
Compute item difficulty heterogeneity std(p_i) for 5 benchmarks,
scatter-plot against Henderson item_id% variance components.
"""
import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
from collections import defaultdict

DATA_DIR = "./results/exp002"
OUT_DIR = "./results/exp004_8model_analysis"

BENCHMARKS = {
    "mmlu": {
        "models": ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek", "olmo", "yi"],
        "item_id_pct": 37.88,
    },
    "arc": {
        "models": ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek", "olmo", "yi"],
        "item_id_pct": 37.88,
    },
    "hellaswag": {
        "models": ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek"],
        "item_id_pct": 34.27,
    },
    "gsm8k": {
        "models": ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek", "olmo", "yi"],
        "item_id_pct": 16.86,
    },
    "math": {
        "models": ["llama", "mistral", "qwen", "internlm", "deepseek", "olmo", "yi"],
        "item_id_pct": 24.03,
    },
}

def load_benchmark(benchmark, models):
    """Load all jsonl files for a benchmark, return dict: item_id -> list of correct values."""
    item_correct = defaultdict(list)
    for model in models:
        fpath = os.path.join(DATA_DIR, f"{model}_{benchmark}.jsonl")
        if not os.path.exists(fpath):
            print(f"  WARNING: {fpath} not found, skipping")
            continue
        with open(fpath) as f:
            for line in f:
                rec = json.loads(line)
                item_id = rec["item_id"]
                item_correct[item_id].append(rec["correct"])
    return item_correct

def compute_std_pi(item_correct):
    """Compute p_i for each item, return std(p_i) and the array of p_i values."""
    p_values = []
    for item_id, corrects in item_correct.items():
        p_i = np.mean(corrects)
        p_values.append(p_i)
    p_values = np.array(p_values)
    return float(np.std(p_values)), p_values

results = {}
for bm, cfg in BENCHMARKS.items():
    print(f"Processing {bm} ({len(cfg['models'])} models)...")
    item_correct = load_benchmark(bm, cfg["models"])
    std_pi, p_values = compute_std_pi(item_correct)
    n_items = len(p_values)
    mean_pi = float(np.mean(p_values))
    results[bm] = {
        "std_pi": round(std_pi, 4),
        "mean_pi": round(mean_pi, 4),
        "n_items": n_items,
        "n_models": len(cfg["models"]),
        "item_id_pct": cfg["item_id_pct"],
    }
    print(f"  n_items={n_items}, mean(p_i)={mean_pi:.4f}, std(p_i)={std_pi:.4f}")

# Spearman correlation
x = [results[bm]["std_pi"] for bm in BENCHMARKS]
y = [results[bm]["item_id_pct"] for bm in BENCHMARKS]
rho, pval = stats.spearmanr(x, y)
print(f"\nSpearman rho={rho:.4f}, p={pval:.4f}")

results["_spearman"] = {"rho": round(rho, 4), "p_value": round(pval, 4)}

# Within-format analysis
mc_bms = ["mmlu", "arc", "hellaswag"]
ff_bms = ["gsm8k", "math"]

mc_std = [(bm, results[bm]["std_pi"]) for bm in mc_bms]
mc_item = [(bm, results[bm]["item_id_pct"]) for bm in mc_bms]
ff_std = [(bm, results[bm]["std_pi"]) for bm in ff_bms]
ff_item = [(bm, results[bm]["item_id_pct"]) for bm in ff_bms]

mc_std_rank = sorted(mc_std, key=lambda x: -x[1])
mc_item_rank = sorted(mc_item, key=lambda x: -x[1])
ff_std_rank = sorted(ff_std, key=lambda x: -x[1])
ff_item_rank = sorted(ff_item, key=lambda x: -x[1])

within_mc_rho, _ = stats.spearmanr(
    [results[bm]["std_pi"] for bm in mc_bms],
    [results[bm]["item_id_pct"] for bm in mc_bms]
)
within_ff_rho, _ = stats.spearmanr(
    [results[bm]["std_pi"] for bm in ff_bms],
    [results[bm]["item_id_pct"] for bm in ff_bms]
)

results["_within_format"] = {
    "mc_std_rank": [t[0] for t in mc_std_rank],
    "mc_item_rank": [t[0] for t in mc_item_rank],
    "mc_consistent": [t[0] for t in mc_std_rank] == [t[0] for t in mc_item_rank],
    "mc_spearman_rho": round(within_mc_rho, 4),
    "ff_std_rank": [t[0] for t in ff_std_rank],
    "ff_item_rank": [t[0] for t in ff_item_rank],
    "ff_consistent": [t[0] for t in ff_std_rank] == [t[0] for t in ff_item_rank],
    "ff_spearman_rho": round(within_ff_rho, 4),
}

print(f"\nWithin-MC std(p_i) rank: {[t[0] for t in mc_std_rank]}")
print(f"Within-MC item_id% rank: {[t[0] for t in mc_item_rank]}")
print(f"Within-MC consistent: {results['_within_format']['mc_consistent']}")
print(f"Within-FF std(p_i) rank: {[t[0] for t in ff_std_rank]}")
print(f"Within-FF item_id% rank: {[t[0] for t in ff_item_rank]}")
print(f"Within-FF consistent: {results['_within_format']['ff_consistent']}")

# Save JSON
json_path = os.path.join(OUT_DIR, "cross_benchmark_difficulty_heterogeneity.json")
with open(json_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nJSON saved to {json_path}")

# --- Scatter plot ---
fig, ax = plt.subplots(figsize=(5.5, 4.5))

mc_color = "#2166AC"
ff_color = "#B2182B"

bm_labels = list(BENCHMARKS.keys())
xs = [results[bm]["std_pi"] for bm in bm_labels]
ys = [results[bm]["item_id_pct"] for bm in bm_labels]

# Plot MC benchmarks
for bm in mc_bms:
    ax.scatter(results[bm]["std_pi"], results[bm]["item_id_pct"],
               c=mc_color, marker='o', s=100, zorder=5, edgecolors='white', linewidths=0.8)
    offset_x = 0.003
    offset_y = 0.8
    if bm == "hellaswag":
        offset_y = -1.5
    ax.annotate(bm.upper(), (results[bm]["std_pi"], results[bm]["item_id_pct"]),
                xytext=(offset_x, offset_y), textcoords='offset points',
                fontsize=10, ha='left', va='bottom')

# Plot FF benchmarks
for bm in ff_bms:
    ax.scatter(results[bm]["std_pi"], results[bm]["item_id_pct"],
               c=ff_color, marker='s', s=100, zorder=5, edgecolors='white', linewidths=0.8)
    offset_x = 0.003
    offset_y = 0.8
    ax.annotate(bm.upper(), (results[bm]["std_pi"], results[bm]["item_id_pct"]),
                xytext=(offset_x, offset_y), textcoords='offset points',
                fontsize=10, ha='left', va='bottom')

# Connect within-format points with dashed lines
mc_pts = sorted([(results[bm]["std_pi"], results[bm]["item_id_pct"]) for bm in mc_bms])
ax.plot([p[0] for p in mc_pts], [p[1] for p in mc_pts],
        '--', color=mc_color, alpha=0.4, linewidth=1.2, zorder=3)

ff_pts = sorted([(results[bm]["std_pi"], results[bm]["item_id_pct"]) for bm in ff_bms])
ax.plot([p[0] for p in ff_pts], [p[1] for p in ff_pts],
        '--', color=ff_color, alpha=0.4, linewidth=1.2, zorder=3)

# Annotation for Spearman
ax.annotate(f"Spearman $\\rho$ = {rho:.2f}\n$p$ = {pval:.3f}",
            xy=(0.05, 0.95), xycoords='axes fraction',
            fontsize=10, va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='wheat', alpha=0.5))

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=mc_color,
           markersize=10, label='Multiple-choice (MC)'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor=ff_color,
           markersize=10, label='Free-form (FF)'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9, framealpha=0.7)

ax.set_xlabel("Item Difficulty Heterogeneity  std($p_i$)", fontsize=12)
ax.set_ylabel("Item Variance Component (%)", fontsize=12)
ax.tick_params(labelsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.tight_layout()

pdf_path = os.path.join(OUT_DIR, "difficulty_vs_item_variance.pdf")
png_path = pdf_path.replace('.pdf', '.png')
fig.savefig(pdf_path, dpi=300, bbox_inches='tight')
fig.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"Figure saved to {pdf_path}")
