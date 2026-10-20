import json
import os
import glob
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

result_dir = '/root/entrainment_gated_ft/lm_eval_clean'
fig_dir = os.path.join(result_dir, 'figures')
os.makedirs(fig_dir, exist_ok=True)

# === 1. Build file-to-model mapping ===
# Priority: prefer full .json over _results.json; skip _lambada_only
model_meta = {
    'GDN-pure':    ('GDN', 'pure', 0),
    'GDN-h24-1':   ('GDN', 'h24-1', 1),
    'GDN-h12-1':   ('GDN', 'h12-1', 2),
    'GDN-h6-1':    ('GDN', 'h6-1', 4),
    'GDN-h3-1':    ('GDN', 'h3-1', 8),
    'RetNet-pure':  ('RetNet', 'pure', 0),
    'RetNet-h24-1': ('RetNet', 'h24-1', 1),
    'RetNet-h12-1': ('RetNet', 'h12-1', 2),
    'RetNet-h6-1':  ('RetNet', 'h6-1', 4),
    'RetNet-h3-1':  ('RetNet', 'h3-1', 8),
    'HGRN2-pure':   ('HGRN2', 'pure', 0),
    'HGRN2-h24-1':  ('HGRN2', 'h24-1', 1),
    'HGRN2-h12-1':  ('HGRN2', 'h12-1', 2),
    'HGRN2-h6-1':   ('HGRN2', 'h6-1', 4),
    'HGRN2-h3-1':   ('HGRN2', 'h3-1', 8),
    'Transformer':  ('Transformer', 'baseline', 24),
}

file_to_model = {
    '1.3B-100B-GatedDeltaNet-pure.json': 'GDN-pure',
    '1.3B-100B-GatedDeltaNet-hybrid-24-1_results.json': 'GDN-h24-1',
    '1.3B-100B-GatedDeltaNet-hybrid-12-1.json': 'GDN-h12-1',
    '1.3B-100B-GatedDeltaNet-hybrid-6-1_results.json': 'GDN-h6-1',
    '1.3B-100B-GatedDeltaNet-hybrid-3-1_results.json': 'GDN-h3-1',
    '1.3B-100B-RetNet-pure.json': 'RetNet-pure',
    '1.3B-100B-RetNet-hybrid-24-1.json': 'RetNet-h24-1',
    '1.3B-100B-RetNet-hybrid-12-1.json': 'RetNet-h12-1',
    '1.3B-100B-RetNet-hybrid-6-1.json': 'RetNet-h6-1',
    '1.3B-100B-RetNet-hybrid-3-1.json': 'RetNet-h3-1',
    '1.3B-100B-HGRN2-pure.json': 'HGRN2-pure',
    '1.3B-100B-HGRN2-hybrid-24-1.json': 'HGRN2-h24-1',
    '1.3B-100B-HGRN2-hybrid-12-1.json': 'HGRN2-h12-1',
    '1.3B-100B-HGRN2-hybrid-6-1.json': 'HGRN2-h6-1',
    '1.3B-100B-HGRN2-hybrid-3-1.json': 'HGRN2-h3-1',
    'transformer_1.3B_baseline.json': 'Transformer',
}

skip_files = {
    '1.3B-100B-GatedDeltaNet-pure_lambada_only.json',
    '1.3B-100B-GatedDeltaNet-pure_results.json',
    '1.3B-100B-RetNet-pure_results.json',
}

rows = []
for fname, model_key in file_to_model.items():
    fpath = os.path.join(result_dir, fname)
    if not os.path.exists(fpath):
        print(f"WARNING: missing file {fname}")
        continue

    family, variant, attn_layers = model_meta[model_key]

    with open(fpath) as f:
        data = json.load(f)

    has_results_key = 'results' in data
    results = data.get('results', data)

    def get_metric(task, metric):
        task_data = results.get(task, {})
        if isinstance(task_data, dict):
            return task_data.get(metric)
        return None

    # MMLU: use groups aggregate if available, else compute weighted average
    mmlu_acc = None
    if has_results_key and 'groups' in data and 'mmlu' in data['groups']:
        mmlu_acc = data['groups']['mmlu'].get('acc,none')
    else:
        mmlu_tasks = [k for k in results.keys() if k.startswith('mmlu_')]
        if mmlu_tasks:
            total_samples = 0
            weighted_sum = 0
            for t in mmlu_tasks:
                acc = results[t].get('acc,none')
                sl = results[t].get('sample_len', 1)
                if acc is not None:
                    weighted_sum += acc * sl
                    total_samples += sl
            if total_samples > 0:
                mmlu_acc = weighted_sum / total_samples

    row = {
        'model_name': model_key,
        'model_family': family,
        'variant': variant,
        'attn_layers': attn_layers,
        'lambada_acc': get_metric('lambada_openai', 'acc,none'),
        'lambada_ppl': get_metric('lambada_openai', 'perplexity,none'),
        'hellaswag_norm': get_metric('hellaswag', 'acc_norm,none'),
        'winogrande_acc': get_metric('winogrande', 'acc,none'),
        'arc_easy_norm': get_metric('arc_easy', 'acc_norm,none'),
        'arc_challenge_norm': get_metric('arc_challenge', 'acc_norm,none'),
        'mmlu_acc': mmlu_acc,
    }
    rows.append(row)

df = pd.DataFrame(rows)
df = df.sort_values(['model_family', 'attn_layers'])
csv_path = os.path.join(result_dir, 'summary_all_1.3b.csv')
df.to_csv(csv_path, index=False)
print(f"CSV saved: {csv_path}")
print(f"Total models: {len(df)}")
print()
print(df.to_string(index=False))

# === 2. Figures ===
family_styles = {
    'GDN':    {'color': '#e74c3c', 'marker': 'o', 'label': 'GatedDeltaNet'},
    'RetNet': {'color': '#3498db', 'marker': 's', 'label': 'RetNet'},
    'HGRN2':  {'color': '#2ecc71', 'marker': '^', 'label': 'HGRN2'},
}

plt.rcParams.update({'font.size': 12, 'figure.dpi': 150})

tf = df[df['model_family'] == 'Transformer']

# --- Fig 1: LAMBADA acc vs attention layers ---
fig, ax = plt.subplots(figsize=(8, 5))
for family, style in family_styles.items():
    sub = df[df['model_family'] == family].sort_values('attn_layers')
    if len(sub) == 0:
        continue
    ax.plot(sub['attn_layers'], sub['lambada_acc'],
            color=style['color'], marker=style['marker'],
            label=style['label'], linewidth=2, markersize=8)

if len(tf) > 0:
    tf_acc = tf['lambada_acc'].values[0]
    if tf_acc is not None and not pd.isna(tf_acc):
        ax.axhline(y=tf_acc, color='gray', linestyle='--', linewidth=1.5, label='Transformer baseline')

ax.set_xlabel('Number of Attention Layers (out of 24)', fontsize=12)
ax.set_ylabel('LAMBADA Accuracy', fontsize=12)
ax.set_title('LAMBADA Accuracy vs Attention Layer Count (1.3B models)', fontsize=13)
ax.legend(fontsize=10)
ax.set_xticks([0, 1, 2, 4, 8])
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(fig_dir, 'fig1_lambada_vs_attn.pdf'), bbox_inches='tight')
fig.savefig(os.path.join(fig_dir, 'fig1_lambada_vs_attn.png'), bbox_inches='tight')
plt.close(fig)
print("\nFig1 saved")

# --- Fig 2: 6-panel subplot ---
benchmarks = [
    ('lambada_acc', 'LAMBADA acc'),
    ('lambada_ppl', 'LAMBADA ppl'),
    ('hellaswag_norm', 'HellaSwag acc_norm'),
    ('winogrande_acc', 'Winogrande acc'),
    ('arc_easy_norm', 'ARC-Easy acc_norm'),
    ('arc_challenge_norm', 'ARC-Challenge acc_norm'),
]

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()

for idx, (col, title) in enumerate(benchmarks):
    ax = axes[idx]
    for family, style in family_styles.items():
        sub = df[df['model_family'] == family].sort_values('attn_layers')
        if len(sub) == 0 or col not in sub.columns:
            continue
        valid = sub.dropna(subset=[col])
        if len(valid) == 0:
            continue
        ax.plot(valid['attn_layers'], valid[col],
                color=style['color'], marker=style['marker'],
                label=style['label'], linewidth=2, markersize=6)

    if len(tf) > 0 and col in tf.columns:
        tf_val = tf[col].values[0]
        if tf_val is not None and not pd.isna(tf_val):
            ax.axhline(y=tf_val, color='gray', linestyle='--', linewidth=1, alpha=0.7,
                       label='Transformer' if idx == 0 else None)

    ax.set_title(title, fontsize=11)
    ax.set_xlabel('Attn Layers', fontsize=10)
    ax.set_xticks([0, 1, 2, 4, 8])
    ax.grid(True, alpha=0.3)
    if idx == 0:
        ax.legend(fontsize=8)
    if 'ppl' in col:
        ax.invert_yaxis()

fig.suptitle('Benchmark Performance vs Attention Layer Count (1.3B models)', fontsize=14, y=1.01)
fig.tight_layout()
fig.savefig(os.path.join(fig_dir, 'fig2_all_benchmarks.pdf'), bbox_inches='tight')
fig.savefig(os.path.join(fig_dir, 'fig2_all_benchmarks.png'), bbox_inches='tight')
plt.close(fig)
print("Fig2 saved")

# --- Fig 3: Heatmap (delta vs pure) ---
metrics = ['lambada_acc', 'hellaswag_norm', 'winogrande_acc', 'arc_easy_norm', 'arc_challenge_norm', 'mmlu_acc']
metric_labels = ['LAMBADA', 'HellaSwag', 'Winogrande', 'ARC-E', 'ARC-C', 'MMLU']

heatmap_rows = []
for family in ['GDN', 'RetNet', 'HGRN2']:
    sub = df[df['model_family'] == family]
    pure = sub[sub['variant'] == 'pure']
    if len(pure) == 0:
        continue
    for _, row in sub.iterrows():
        if row['variant'] == 'pure':
            continue
        deltas = {}
        for m, ml in zip(metrics, metric_labels):
            pure_val = pure[m].values[0]
            curr_val = row[m]
            if pure_val is not None and curr_val is not None and not pd.isna(pure_val) and not pd.isna(curr_val):
                deltas[ml] = curr_val - pure_val
            else:
                deltas[ml] = np.nan
        heatmap_rows.append({'model': f"{family} {row['variant']}", **deltas})

if heatmap_rows:
    hm_df = pd.DataFrame(heatmap_rows).set_index('model')
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(hm_df, annot=True, fmt='.3f', cmap='RdYlGn', center=0,
                linewidths=0.5, ax=ax, cbar_kws={'label': 'Delta acc vs pure'})
    ax.set_title('Performance Delta vs Pure Linear Baseline', fontsize=13)
    ax.set_ylabel('')
    fig.tight_layout()
    fig.savefig(os.path.join(fig_dir, 'fig3_delta_heatmap.pdf'), bbox_inches='tight')
    fig.savefig(os.path.join(fig_dir, 'fig3_delta_heatmap.png'), bbox_inches='tight')
    plt.close(fig)
    print("Fig3 saved")

print(f"\nAll figures saved to: {fig_dir}")
