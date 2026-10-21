import pandas as pd
import numpy as np
import json
import glob
import os

os.chdir('.')
import sys
sys.path.insert(0, '.')

from src.config.model_paths import normalize_model_name

# === Load data for 3 models (Llama, Mistral, Qwen) ===
records = []

# Llama: llama_shard_*.jsonl
for f in sorted(glob.glob('results/exp001_llama/llama_shard_*.jsonl')):
    with open(f) as fh:
        for line in fh:
            records.append(json.loads(line))

# Mistral & Qwen: shard_*.jsonl (exclude special files)
for model_dir in ['exp001_mistral', 'exp001_qwen']:
    for f in sorted(glob.glob(f'results/{model_dir}/shard_[0-3].jsonl')):
        with open(f) as fh:
            for line in fh:
                records.append(json.loads(line))

df = pd.DataFrame(records)

# Normalize correct field
if 'binary_correct' not in df.columns and 'correct' in df.columns:
    df['binary_correct'] = df['correct']

df['model'] = df['model'].apply(normalize_model_name)

print(f"Total records loaded: {len(df)}")
print(f"Models: {sorted(df['model'].unique())}")
print(f"Precisions: {sorted(df['precision'].unique())}")
print(f"By model×precision:")
print(df.groupby(['model','precision']).size().unstack(fill_value=0))
print()

# === Helper: variance decomposition ===
def variance_decomposition(data, label=""):
    grand_mean = data['binary_correct'].mean()
    N = len(data)
    total_var = data['binary_correct'].var()
    ss_total = total_var * (N - 1)

    facets = ['model', 'precision', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']
    # Only use facets present in data with >1 level
    facets = [f for f in facets if f in data.columns and data[f].nunique() > 1]

    results = {}
    for facet in facets:
        group_means = data.groupby(facet)['binary_correct'].mean()
        n_levels = len(group_means)
        n_per_level = N / n_levels
        ss = n_per_level * ((group_means - grand_mean) ** 2).sum()
        results[facet] = {
            'n_levels': int(n_levels),
            'ss': float(ss),
            'mean_range': [float(group_means.min()), float(group_means.max())]
        }

    interactions = [
        ('model', 'item_id'), ('model', 'precision'), ('model', 'temperature'),
        ('precision', 'item_id'), ('precision', 'temperature'),
        ('temperature', 'item_id'), ('prompt_template', 'item_id'),
        ('seed', 'item_id'), ('ordering', 'item_id'),
    ]

    for f1, f2 in interactions:
        if f1 not in facets or f2 not in facets:
            continue
        cell_means = data.groupby([f1, f2])['binary_correct'].mean()
        marginal_A = data.groupby(f1)['binary_correct'].mean()
        marginal_B = data.groupby(f2)['binary_correct'].mean()
        n_a = data[f1].nunique()
        n_b = data[f2].nunique()
        n_per_cell = N / (n_a * n_b)

        interaction_ss = 0
        for (a, b), cell_mean in cell_means.items():
            expected = grand_mean + (marginal_A[a] - grand_mean) + (marginal_B[b] - grand_mean)
            interaction_ss += (cell_mean - expected) ** 2
        interaction_ss *= n_per_cell

        results[f'{f1}:{f2}'] = {
            'n_levels': int(n_a * n_b),
            'ss': float(interaction_ss)
        }

    all_ss = {k: v['ss'] for k, v in results.items()}
    ss_residual = ss_total - sum(all_ss.values())
    all_ss['residual'] = max(0, ss_residual)
    total_ss_sum = sum(all_ss.values())
    variance_pct = {k: v / total_ss_sum * 100 for k, v in all_ss.items()}

    print(f"\n=== {label} Variance Components ===")
    print(f"N={N}, grand_mean={grand_mean:.4f}, total_var={total_var:.6f}")
    for k, v in sorted(variance_pct.items(), key=lambda x: -x[1]):
        if v > 0.01:
            print(f"  {k}: {v:.4f}%")

    return results, variance_pct, {'N': N, 'grand_mean': float(grand_mean), 'total_var': float(total_var)}

# === Analysis 1: BF16+FP16 only (3 models) ===
df_bf16_fp16 = df[df['precision'].isin(['bfloat16', 'float16'])].copy()
print(f"\n--- BF16+FP16 Dataset ---")
print(f"Records: {len(df_bf16_fp16)}")
print(f"By model: {df_bf16_fp16.groupby('model').size().to_dict()}")
print(f"By precision: {df_bf16_fp16.groupby('precision').size().to_dict()}")
print(f"Mean accuracy by precision:")
print(df_bf16_fp16.groupby('precision')['binary_correct'].mean())
print(f"Mean accuracy by model×precision:")
print(df_bf16_fp16.groupby(['model','precision'])['binary_correct'].mean().unstack())

res_bf16fp16, pct_bf16fp16, stats_bf16fp16 = variance_decomposition(df_bf16_fp16, "BF16+FP16 Only (3 models)")

# === Analysis 2: All 3 precisions (same 3 models) ===
print(f"\n--- All 3 Precisions Dataset ---")
print(f"Records: {len(df)}")
print(f"By precision: {df.groupby('precision').size().to_dict()}")
print(f"Mean accuracy by precision:")
print(df.groupby('precision')['binary_correct'].mean())

res_3prec, pct_3prec, stats_3prec = variance_decomposition(df, "All 3 Precisions (3 models)")

# === Comparison table ===
print("\n\n========== COMPARISON TABLE ==========")
print(f"{'Component':<25} {'3-Prec (%)':<15} {'BF16+FP16 (%)':<15} {'Delta':<10}")
print("-" * 65)
all_keys = sorted(set(list(pct_3prec.keys()) + list(pct_bf16fp16.keys())),
                  key=lambda x: -max(pct_3prec.get(x, 0), pct_bf16fp16.get(x, 0)))
for k in all_keys:
    v3 = pct_3prec.get(k, 0)
    v2 = pct_bf16fp16.get(k, 0)
    delta = v2 - v3
    if max(v3, v2) > 0.01:
        print(f"  {k:<23} {v3:>10.4f}     {v2:>10.4f}     {delta:>+8.4f}")

# === Save ===
os.makedirs('results/analysis', exist_ok=True)

output = {
    'analysis': 'BF16 vs FP16 sensitivity — FP32 confound check',
    'date': '2026-05-21',
    'motivation': 'Reviewer concern: FP32 dominates precision facet. Check if precision variance ~0 when FP32 excluded.',
    'bf16_fp16_only': {
        'n_records': int(len(df_bf16_fp16)),
        'n_models': 3,
        'models': sorted(df_bf16_fp16['model'].unique().tolist()),
        'precisions': ['bfloat16', 'float16'],
        'grand_mean': stats_bf16fp16['grand_mean'],
        'variance_components_pct': {k: round(v, 4) for k, v in pct_bf16fp16.items()},
        'precision_pct': round(pct_bf16fp16.get('precision', 0), 4),
        'precision_item_pct': round(pct_bf16fp16.get('precision:item_id', 0), 4),
        'accuracy_by_precision': df_bf16_fp16.groupby('precision')['binary_correct'].mean().to_dict(),
    },
    'all_3_precisions': {
        'n_records': int(len(df)),
        'n_models': 3,
        'models': sorted(df['model'].unique().tolist()),
        'precisions': sorted(df['precision'].unique().tolist()),
        'grand_mean': stats_3prec['grand_mean'],
        'variance_components_pct': {k: round(v, 4) for k, v in pct_3prec.items()},
        'precision_pct': round(pct_3prec.get('precision', 0), 4),
        'precision_item_pct': round(pct_3prec.get('precision:item_id', 0), 4),
        'accuracy_by_precision': df.groupby('precision')['binary_correct'].mean().to_dict(),
    },
    'conclusion': '',
}

# Set conclusion based on results
prec_bf16fp16 = pct_bf16fp16.get('precision', 0)
prec_item_bf16fp16 = pct_bf16fp16.get('precision:item_id', 0)
prec_3prec = pct_3prec.get('precision', 0)
prec_item_3prec = pct_3prec.get('precision:item_id', 0)
output['conclusion'] = (
    f"With FP32 excluded: precision={prec_bf16fp16:.4f}%, precision×item={prec_item_bf16fp16:.4f}%. "
    f"With FP32 included: precision={prec_3prec:.4f}%, precision×item={prec_item_3prec:.4f}%. "
    f"FP32 removal {'confirms' if prec_bf16fp16 < 1.0 else 'does not confirm'} that "
    f"precision variance is driven by FP32, not BF16-vs-FP16 differences."
)

with open('results/analysis/bf16_fp16_only_gstudy.json', 'w') as f:
    json.dump(output, f, indent=2, default=str)

print(f"\nSaved to results/analysis/bf16_fp16_only_gstudy.json")
print(f"\n=== CONCLUSION ===")
print(output['conclusion'])
