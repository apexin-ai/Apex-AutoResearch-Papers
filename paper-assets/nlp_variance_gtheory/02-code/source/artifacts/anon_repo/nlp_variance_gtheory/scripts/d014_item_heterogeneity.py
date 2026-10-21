import json
import os
import numpy as np
from collections import defaultdict
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

DATA_DIR = "./results/exp002"
OUT_DIR = "./results/exp004_8model_analysis"

MODELS_ALL = ['qwen', 'llama', 'gemma', 'mistral', 'internlm', 'deepseek', 'olmo', 'yi']
MODELS_HELLASWAG = ['qwen', 'llama', 'gemma', 'mistral', 'internlm', 'deepseek']
MODELS_MATH = ['qwen', 'llama', 'gemma', 'mistral', 'internlm', 'olmo', 'yi']

BENCHMARKS = ['mmlu', 'arc', 'hellaswag', 'gsm8k', 'math']

ITEM_ID_PCT = {
    'mmlu': 40.48,
    'arc': 42.46,
    'hellaswag': 32.20,
    'gsm8k': 16.86,
    'math': 26.48,
}

def get_models(bm):
    if bm == 'hellaswag':
        return MODELS_HELLASWAG
    elif bm == 'math':
        return MODELS_MATH
    return MODELS_ALL

def load_jsonl(path):
    data = []
    with open(path) as f:
        for line in f:
            row = json.loads(line.strip())
            if '_placeholder' in row:
                return None
            data.append(row)
    return data

def analyze_benchmark(bm):
    models = get_models(bm)
    item_model_scores = defaultdict(lambda: defaultdict(list))
    actual_models = []

    for model in models:
        path = os.path.join(DATA_DIR, f"{model}_{bm}.jsonl")
        if not os.path.exists(path):
            print(f"  SKIP: {path}")
            continue
        data = load_jsonl(path)
        if data is None:
            print(f"  SKIP: {path} (placeholder)")
            continue
        actual_models.append(model)
        for row in data:
            item_model_scores[row['item_id']][model].append(row['correct'])

    item_ids = sorted(item_model_scores.keys())
    n_items = len(item_ids)

    p_values = []
    model_variances = []

    for iid in item_ids:
        model_means = []
        for m in actual_models:
            if m in item_model_scores[iid]:
                model_means.append(np.mean(item_model_scores[iid][m]))
        if model_means:
            p_values.append(np.mean(model_means))
            model_variances.append(np.var(model_means, ddof=1) if len(model_means) > 1 else 0)

    p_values = np.array(p_values)
    model_variances = np.array(model_variances)

    return {
        'benchmark': bm,
        'n_models': len(actual_models),
        'models_used': actual_models,
        'n_items': n_items,
        'item_difficulty_stats': {
            'mean_p': float(np.mean(p_values)),
            'std_p': float(np.std(p_values, ddof=1)),
            'var_p': float(np.var(p_values, ddof=1)),
            'range_p': float(np.ptp(p_values)),
            'iqr_p': float(np.percentile(p_values, 75) - np.percentile(p_values, 25)),
            'min_p': float(np.min(p_values)),
            'max_p': float(np.max(p_values)),
        },
        'mean_model_item_var': float(np.mean(model_variances)),
        'item_id_pct': ITEM_ID_PCT[bm],
    }

results = {}
for bm in BENCHMARKS:
    print(f"Analyzing {bm}...")
    results[bm] = analyze_benchmark(bm)

std_p = [results[bm]['item_difficulty_stats']['std_p'] for bm in BENCHMARKS]
item_pct = [results[bm]['item_id_pct'] for bm in BENCHMARKS]
mmi_var = [results[bm]['mean_model_item_var'] for bm in BENCHMARKS]

rho_std, p_std = stats.spearmanr(std_p, item_pct)
rho_var, p_var = stats.spearmanr(mmi_var, item_pct)

print(f"\n{'Benchmark':<12} {'std(p)':<10} {'var(p)':<10} {'item_id%':<10} {'mean_m×i_var':<14} {'n_models'}")
print("-" * 68)
for bm in BENCHMARKS:
    r = results[bm]
    s = r['item_difficulty_stats']
    print(f"{bm:<12} {s['std_p']:<10.4f} {s['var_p']:<10.4f} {r['item_id_pct']:<10.2f} {r['mean_model_item_var']:<14.6f} {r['n_models']}")

print(f"\nSpearman: std(p) vs item_id%: rho={rho_std:.4f}, p={p_std:.4f}")
print(f"Spearman: mean_m×i_var vs item_id%: rho={rho_var:.4f}, p={p_var:.4f}")
print(f"Hypothesis (rho>0.8): {'SUPPORTED' if rho_std > 0.8 else 'NOT SUPPORTED'}")

# Scatter plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ax1 = axes[0]
ax1.scatter(std_p, item_pct, s=100, c='steelblue', zorder=5)
for i, bm in enumerate(BENCHMARKS):
    ax1.annotate(bm.upper(), (std_p[i], item_pct[i]),
                 textcoords="offset points", xytext=(8, 5), fontsize=10)
z1 = np.polyfit(std_p, item_pct, 1)
xl1 = np.linspace(min(std_p)*0.95, max(std_p)*1.05, 100)
ax1.plot(xl1, np.polyval(z1, xl1), '--', color='gray', alpha=0.7)
ax1.set_xlabel('Item Difficulty Heterogeneity (std of p_i)', fontsize=11)
ax1.set_ylabel('item_id Variance Component (%)', fontsize=11)
ax1.set_title(f'Spearman ρ = {rho_std:.3f} (p = {p_std:.3f})', fontsize=12)

ax2 = axes[1]
ax2.scatter(mmi_var, item_pct, s=100, c='coral', zorder=5)
for i, bm in enumerate(BENCHMARKS):
    ax2.annotate(bm.upper(), (mmi_var[i], item_pct[i]),
                 textcoords="offset points", xytext=(8, 5), fontsize=10)
z2 = np.polyfit(mmi_var, item_pct, 1)
xl2 = np.linspace(min(mmi_var)*0.95, max(mmi_var)*1.05, 100)
ax2.plot(xl2, np.polyval(z2, xl2), '--', color='gray', alpha=0.7)
ax2.set_xlabel('Mean Model×Item Variance', fontsize=11)
ax2.set_ylabel('item_id Variance Component (%)', fontsize=11)
ax2.set_title(f'Spearman ρ = {rho_var:.3f} (p = {p_var:.3f})', fontsize=12)

plt.suptitle('D014: Item Heterogeneity vs. item_id% Variance Component', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'item_heterogeneity_scatter.png'), dpi=150, bbox_inches='tight')
print(f"\nPlot saved: {OUT_DIR}/item_heterogeneity_scatter.png")

# Save JSON
output = {
    'analysis': 'D014_item_heterogeneity_verification',
    'date': '2026-05-21',
    'hypothesis': 'item difficulty heterogeneity drives item_id variance component',
    'per_benchmark': results,
    'correlation': {
        'std_p_vs_item_id_pct': {
            'spearman_rho': float(rho_std),
            'p_value': float(p_std),
            'supports_hypothesis': bool(rho_std > 0.8),
        },
        'mean_model_item_var_vs_item_id_pct': {
            'spearman_rho': float(rho_var),
            'p_value': float(p_var),
        },
    },
    'notes': {
        'hellaswag': '6 models only (OLMo/Yi hellaswag not on this server)',
        'math': '7 models (DeepSeek excluded, incomplete data)',
        'mc_item_id_pct': '6-model G-study values for MMLU/ARC/HellaSwag',
        'ff_item_id_pct': '8-model G-study for GSM8K, 7-model for MATH',
    },
}

if rho_std > 0.8:
    output['conclusion'] = f'SUPPORTED: rho={rho_std:.3f}>0.8. Item difficulty heterogeneity strongly correlates with item_id variance component.'
else:
    output['conclusion'] = f'NOT FULLY SUPPORTED: rho={rho_std:.3f}<0.8. Item difficulty heterogeneity alone does not fully explain item_id variance component.'

with open(os.path.join(OUT_DIR, 'item_heterogeneity_verification.json'), 'w') as f:
    json.dump(output, f, indent=2)

print(f"JSON saved: {OUT_DIR}/item_heterogeneity_verification.json")
print(f"\nConclusion: {output['conclusion']}")
