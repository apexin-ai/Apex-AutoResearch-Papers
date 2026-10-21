import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# 读取数据
csv_path = '/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv'
df = pd.read_csv(csv_path)

# 只保留三个 linear attention 家族（排除 Transformer baseline 和 new-h24-1）
df = df[df['model_family'].isin(['GDN', 'RetNet', 'HGRN2'])]
df = df[df['variant'] != 'new-h24-1']

print("Data loaded:")
print(df[['model_family', 'variant', 'attn_layers']].to_string(index=False))
print()

benchmarks = {
    'lambada_acc': 'LAMBADA acc',
    'hellaswag_norm': 'HellaSwag acc_norm',
    'winogrande_acc': 'Winogrande acc',
    'arc_easy_norm': 'ARC-Easy acc_norm',
    'arc_challenge_norm': 'ARC-Challenge acc_norm',
    'mmlu_acc': 'MMLU acc',
}

# 对每个 attention level，计算跨架构 std 和 range
attn_levels = sorted(df['attn_layers'].unique())
print(f"Attention levels: {attn_levels}")
print()

results = {}
for bench_col, bench_name in benchmarks.items():
    stds = []
    ranges = []
    means = []
    for attn in attn_levels:
        sub = df[df['attn_layers'] == attn]
        vals = sub[bench_col].dropna().values
        if len(vals) >= 2:
            stds.append(np.std(vals))
            ranges.append(np.max(vals) - np.min(vals))
            means.append(np.mean(vals))
        else:
            stds.append(np.nan)
            ranges.append(np.nan)
            means.append(np.nan)
    results[bench_name] = {
        'std': stds,
        'range': ranges,
        'mean': means,
    }
    print(f"\n{bench_name}:")
    print(f"  attn_layers: {attn_levels}")
    print(f"  cross-arch std: {[f'{s:.4f}' if not np.isnan(s) else 'N/A' for s in stds]}")
    print(f"  cross-arch range: {[f'{r:.4f}' if not np.isnan(r) else 'N/A' for r in ranges]}")
    
    # 详细：每个 attn level 各架构的值
    for attn in attn_levels:
        sub = df[df['attn_layers'] == attn][['model_family', bench_col]]
        vals = sub.dropna()
        if len(vals) > 0:
            detail = ', '.join([f"{row['model_family']}={row[bench_col]:.4f}" for _, row in vals.iterrows()])
            print(f"    attn={attn}: {detail}")

# Spearman correlation: attn_layers vs cross-arch std
from scipy import stats as sp_stats
from itertools import permutations
import math

def exact_spearman_p(x, y):
    x, y = np.array(x), np.array(y)
    rho_obs = sp_stats.spearmanr(x, y)[0]
    n = len(x)
    count = sum(1 for perm in permutations(range(n))
                if abs(sp_stats.spearmanr(x, y[list(perm)])[0]) >= abs(rho_obs))
    return rho_obs, count / math.factorial(n)
print("\n\n=== Convergence Test (Spearman: attn_layers vs cross-arch std) [exact permutation p-values] ===")
for bench_name, res in results.items():
    valid = [(a, s) for a, s in zip(attn_levels, res['std']) if not np.isnan(s)]
    if len(valid) >= 3:
        x, y = zip(*valid)
        rho, p = exact_spearman_p(x, y)
        trend = "CONVERGING (std decreases)" if rho < 0 else "DIVERGING (std increases)"
        sig = "significant" if p < 0.05 else "not significant"
        print(f"  {bench_name}: rho={rho:.3f}, p={p:.3f} -> {trend}, {sig}")

# 图表
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
plt.rcParams.update({'font.size': 12})

# 图 A: Cross-architecture std vs attention layers
ax = axes[0]
for bench_name, res in results.items():
    valid_idx = [i for i, s in enumerate(res['std']) if not np.isnan(s)]
    if valid_idx:
        ax.plot([attn_levels[i] for i in valid_idx], 
                [res['std'][i] for i in valid_idx],
                marker='o', label=bench_name, linewidth=1.5)
ax.set_xlabel('Number of Attention Layers', fontsize=12)
ax.set_ylabel('Cross-Architecture Std Dev', fontsize=12)
ax.set_title('Architecture Convergence vs Attention Ratio', fontsize=13)
ax.legend(fontsize=8, loc='best')
ax.set_xticks(attn_levels)
ax.grid(True, alpha=0.3)

# 图 B: Cross-architecture range vs attention layers
ax = axes[1]
for bench_name, res in results.items():
    valid_idx = [i for i, r in enumerate(res['range']) if not np.isnan(r)]
    if valid_idx:
        ax.plot([attn_levels[i] for i in valid_idx],
                [res['range'][i] for i in valid_idx],
                marker='s', label=bench_name, linewidth=1.5)
ax.set_xlabel('Number of Attention Layers', fontsize=12)
ax.set_ylabel('Cross-Architecture Range', fontsize=12)
ax.set_title('Architecture Spread vs Attention Ratio', fontsize=13)
ax.legend(fontsize=8, loc='best')
ax.set_xticks(attn_levels)
ax.grid(True, alpha=0.3)

fig.tight_layout()
out_dir = '/root/entrainment_gated_ft/analysis'
fig.savefig(os.path.join(out_dir, 'convergence_analysis.pdf'), bbox_inches='tight')
fig.savefig(os.path.join(out_dir, 'convergence_analysis.png'), bbox_inches='tight')
print(f"\nFigures saved to {out_dir}")
