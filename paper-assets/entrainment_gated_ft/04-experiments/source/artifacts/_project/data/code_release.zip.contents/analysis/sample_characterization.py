# Sample characterization analysis for LAMBADA per-example data
# Computes features for helped/hurt samples across GDN, HGRN2, RetNet architectures

import json
import os
import numpy as np
import pandas as pd
from collections import Counter
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from transformers import AutoTokenizer

OUT_DIR = '/root/entrainment_gated_ft/analysis'
DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'
TOKENIZER_PATH = '/root/autodl-tmp/models_1.3b/1.3B-100B-GatedDeltaNet-pure/'

# ── Data loading ─────────────────────────────────────────────────

def load_json_samples(path, task='lambada_openai'):
    with open(path) as f:
        d = json.load(f)
    return sorted(d['samples'][task], key=lambda x: x['doc_id'])

def load_jsonl_samples(path):
    samples = []
    with open(path) as f:
        for line in f:
            samples.append(json.loads(line))
    return sorted(samples, key=lambda x: x['doc_id'])

print("Loading model predictions...")
models = {
    'GDN-pure':   load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),
    'GDN-h31':    load_jsonl_samples(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),
    'HGRN2-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),
    'HGRN2-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),
    'RetNet-pure': load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-pure.json')),
    'RetNet-h31':  load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-hybrid-3-1.json')),
}

n_samples = len(models['GDN-pure'])
print(f"Loaded {n_samples} samples per model")

# ── Feature extraction ───────────────────────────────────────────

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)

texts = [s['doc']['text'] for s in models['GDN-pure']]
targets = [s['target'].strip() for s in models['GDN-pure']]

print("Tokenizing...")
target_freq = Counter(targets)

context_lengths = []
context_unique_tokens_list = []

for i, text in enumerate(texts):
    token_ids = tokenizer.encode(text, add_special_tokens=False)
    target_text = targets[i]
    target_ids = tokenizer.encode(' ' + target_text, add_special_tokens=False)
    n_target = len(target_ids)
    context_ids = token_ids[:-n_target] if n_target > 0 else token_ids
    context_lengths.append(len(context_ids))
    context_unique_tokens_list.append(len(set(context_ids)))

features = pd.DataFrame({
    'doc_id': [s['doc_id'] for s in models['GDN-pure']],
    'target_token': targets,
    'context_length': context_lengths,
    'target_token_frequency': [target_freq[t] for t in targets],
    'context_unique_tokens': context_unique_tokens_list,
})

print(f"Feature stats:\n{features[['context_length', 'target_token_frequency', 'context_unique_tokens']].describe()}")

# ── Helped/Hurt identification ───────────────────────────────────

ARCHS = ['GDN', 'HGRN2', 'RetNet']

acc_arrays = {}
for name, samples in models.items():
    acc_arrays[name] = np.array([s['acc'] for s in samples])

helped = {}  # hybrid=1, pure=0
hurt = {}    # hybrid=0, pure=1

for arch in ARCHS:
    pure_acc = acc_arrays[f'{arch}-pure']
    hybrid_acc = acc_arrays[f'{arch}-h31']
    helped[arch] = (hybrid_acc == 1) & (pure_acc == 0)
    hurt[arch] = (hybrid_acc == 0) & (pure_acc == 1)
    print(f"{arch}: helped={helped[arch].sum()}, hurt={hurt[arch].sum()}, "
          f"both_correct={(hybrid_acc & pure_acc).sum()}, both_wrong={((1-hybrid_acc) * (1-pure_acc)).astype(int).sum()}")

# ── Statistical tests ────────────────────────────────────────────

FEATURE_COLS = ['context_length', 'target_token_frequency', 'context_unique_tokens']

stat_rows = []

# Per-architecture: helped vs hurt
for arch in ARCHS:
    h_mask = helped[arch]
    r_mask = hurt[arch]
    if h_mask.sum() < 2 or r_mask.sum() < 2:
        print(f"WARNING: {arch} has too few helped/hurt samples for stats")
        continue
    for feat in FEATURE_COLS:
        vals_h = features.loc[h_mask, feat].values
        vals_r = features.loc[r_mask, feat].values
        u_stat, p_val = stats.mannwhitneyu(vals_h, vals_r, alternative='two-sided')
        n1, n2 = len(vals_h), len(vals_r)
        rank_biserial = 1 - (2 * u_stat) / (n1 * n2)
        stat_rows.append({
            'comparison': f'{arch}: helped vs hurt',
            'feature': feat,
            'helped_median': np.median(vals_h),
            'hurt_median': np.median(vals_r),
            'helped_mean': np.mean(vals_h),
            'hurt_mean': np.mean(vals_r),
            'helped_n': n1,
            'hurt_n': n2,
            'U_statistic': u_stat,
            'p_value': p_val,
            'rank_biserial_r': rank_biserial,
        })

# Cross-architecture: helped vs helped
for i, a1 in enumerate(ARCHS):
    for a2 in ARCHS[i+1:]:
        m1 = helped[a1]
        m2 = helped[a2]
        if m1.sum() < 2 or m2.sum() < 2:
            continue
        for feat in FEATURE_COLS:
            v1 = features.loc[m1, feat].values
            v2 = features.loc[m2, feat].values
            u_stat, p_val = stats.mannwhitneyu(v1, v2, alternative='two-sided')
            n1, n2 = len(v1), len(v2)
            rank_biserial = 1 - (2 * u_stat) / (n1 * n2)
            stat_rows.append({
                'comparison': f'helped: {a1} vs {a2}',
                'feature': feat,
                'helped_median': np.median(v1),
                'hurt_median': np.median(v2),
                'helped_mean': np.mean(v1),
                'hurt_mean': np.mean(v2),
                'helped_n': n1,
                'hurt_n': n2,
                'U_statistic': u_stat,
                'p_value': p_val,
                'rank_biserial_r': rank_biserial,
            })

stats_df = pd.DataFrame(stat_rows)
stats_path = os.path.join(OUT_DIR, 'sample_characterization_results.csv')
stats_df.to_csv(stats_path, index=False)
print(f"\nStatistical results saved to {stats_path}")
print(stats_df.to_string(index=False))

# ── Visualization ────────────────────────────────────────────────

fig = plt.figure(figsize=(18, 14))
gs = gridspec.GridSpec(2, 3, hspace=0.35, wspace=0.3)

feat_labels = {
    'context_length': 'Context Length\n(tokens)',
    'target_token_frequency': 'Target Token\nFrequency',
    'context_unique_tokens': 'Context Unique\nTokens',
}

arch_colors = {
    'GDN': ('#2196F3', '#90CAF9'),
    'HGRN2': ('#FF5722', '#FFAB91'),
    'RetNet': ('#4CAF50', '#A5D6A7'),
}

# Upper row: per-architecture helped vs hurt
for col, arch in enumerate(ARCHS):
    ax = fig.add_subplot(gs[0, col])
    h_mask = helped[arch]
    r_mask = hurt[arch]

    data_helped = []
    data_hurt = []
    positions = []
    for fi, feat in enumerate(FEATURE_COLS):
        data_helped.append(features.loc[h_mask, feat].values)
        data_hurt.append(features.loc[r_mask, feat].values)
        positions.append(fi)

    # Normalize each feature to [0,1] for comparable violin plots
    all_vals = [np.concatenate([data_helped[i], data_hurt[i]]) for i in range(len(FEATURE_COLS))]
    mins = [v.min() for v in all_vals]
    maxs = [v.max() for v in all_vals]

    bp_positions_h = [p - 0.18 for p in positions]
    bp_positions_r = [p + 0.18 for p in positions]

    norm_h = [(data_helped[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]
    norm_r = [(data_hurt[i] - mins[i]) / (maxs[i] - mins[i] + 1e-8) for i in range(len(FEATURE_COLS))]

    vp1 = ax.violinplot(norm_h, positions=bp_positions_h, widths=0.3, showextrema=False)
    for body in vp1['bodies']:
        body.set_facecolor(arch_colors[arch][0])
        body.set_alpha(0.7)

    vp2 = ax.violinplot(norm_r, positions=bp_positions_r, widths=0.3, showextrema=False)
    for body in vp2['bodies']:
        body.set_facecolor(arch_colors[arch][1])
        body.set_alpha(0.7)

    # Add median markers
    for i in range(len(FEATURE_COLS)):
        med_h = np.median(norm_h[i])
        med_r = np.median(norm_r[i])
        ax.plot(bp_positions_h[i], med_h, 'o', color='white', markeredgecolor=arch_colors[arch][0], markersize=6, zorder=5)
        ax.plot(bp_positions_r[i], med_r, 'o', color='white', markeredgecolor=arch_colors[arch][1], markersize=6, zorder=5)

    ax.set_xticks(positions)
    ax.set_xticklabels([feat_labels[f] for f in FEATURE_COLS], fontsize=8)
    ax.set_ylabel('Normalized value', fontsize=9)
    ax.set_title(f'{arch} (h={helped[arch].sum()}, r={hurt[arch].sum()})', fontsize=11, fontweight='bold')

    if col == 0:
        from matplotlib.patches import Patch
        ax.legend(handles=[
            Patch(facecolor=arch_colors[arch][0], alpha=0.7, label='Helped'),
            Patch(facecolor=arch_colors[arch][1], alpha=0.7, label='Hurt'),
        ], fontsize=8, loc='upper right')

    # Add p-value annotations
    for i, feat in enumerate(FEATURE_COLS):
        match = stats_df[(stats_df['comparison'] == f'{arch}: helped vs hurt') & (stats_df['feature'] == feat)]
        if len(match) > 0:
            p = match.iloc[0]['p_value']
            sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'
            ax.text(positions[i], 1.05, sig, ha='center', fontsize=8, color='black')

    ax.set_ylim(-0.1, 1.2)

# Lower row: cross-architecture helped comparison
for col, feat in enumerate(FEATURE_COLS):
    ax = fig.add_subplot(gs[1, col])

    data = []
    labels = []
    colors = []
    for arch in ARCHS:
        h_mask = helped[arch]
        if h_mask.sum() > 0:
            data.append(features.loc[h_mask, feat].values)
            labels.append(f'{arch}\n(n={h_mask.sum()})')
            colors.append(arch_colors[arch][0])

    vp = ax.violinplot(data, positions=range(len(data)), widths=0.6, showextrema=False)
    for i, body in enumerate(vp['bodies']):
        body.set_facecolor(colors[i])
        body.set_alpha(0.7)

    # Median + IQR
    for i, d in enumerate(data):
        med = np.median(d)
        q1, q3 = np.percentile(d, [25, 75])
        ax.vlines(i, q1, q3, color='black', linewidth=2)
        ax.scatter(i, med, color='white', edgecolor='black', s=40, zorder=5)

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel(feat.replace('_', ' ').title(), fontsize=9)
    ax.set_title(f'Helped samples: {feat_labels[feat].replace(chr(10), " ")}', fontsize=10, fontweight='bold')

    # Add cross-arch p-values
    y_max = max(d.max() for d in data)
    y_step = (y_max - min(d.min() for d in data)) * 0.08
    y_pos = y_max + y_step
    for i, a1 in enumerate(ARCHS):
        for j, a2 in enumerate(ARCHS):
            if j <= i:
                continue
            match = stats_df[(stats_df['comparison'] == f'helped: {a1} vs {a2}') & (stats_df['feature'] == feat)]
            if len(match) > 0:
                p = match.iloc[0]['p_value']
                sig = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'
                if sig != 'n.s.':
                    idx_a1 = ARCHS.index(a1)
                    idx_a2 = ARCHS.index(a2)
                    ax.plot([idx_a1, idx_a2], [y_pos, y_pos], 'k-', linewidth=0.8)
                    ax.text((idx_a1 + idx_a2) / 2, y_pos, sig, ha='center', va='bottom', fontsize=7)
                    y_pos += y_step * 1.5

fig.suptitle('LAMBADA Sample Characterization: Helped vs Hurt by Attention Hybridization',
             fontsize=14, fontweight='bold', y=0.98)

for fmt in ['pdf', 'png']:
    path = os.path.join(OUT_DIR, f'sample_characterization.{fmt}')
    fig.savefig(path, dpi=200, bbox_inches='tight')
    print(f"Figure saved: {path}")

plt.close()
print("\nDone.")
