#!/usr/bin/env python3
"""Atlas paper figures: 4 publication-quality figures for recursive generation depth estimation."""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from pathlib import Path
from collections import defaultdict
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import confusion_matrix as cm_func

BASE = Path('/root/autodl-tmp/recursive_gen_depth_est')
OUT = BASE / 'artifacts' / 'figures'
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 13,
    'axes.titlesize': 14,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'font.family': 'DejaVu Sans',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

MODEL_COLORS = {
    'Pythia-1.4B': '#2166AC',
    'OLMo-1B': '#2CA02C',
    'GPT-2 XL': '#D62728',
}
STRATEGY_LS = {'nucleus': '-', 'temp': '--', 'topk': ':'}
STRATEGY_MK = {'nucleus': 'o', 'temp': 's', 'topk': '^'}

FEATURE_COLS = [
    'mean_ppl', 'var_ppl', 'skewness_ppl', 'kurtosis_ppl',
    'p10_ppl', 'p25_ppl', 'p50_ppl', 'p75_ppl', 'p90_ppl',
    'mean_surprisal', 'var_surprisal', 'entropy_of_surprisal',
    'type_token_ratio', 'hapax_ratio',
    'bigram_entropy', 'trigram_entropy',
    'rep_2gram', 'rep_3gram', 'rep_4gram',
]

# ============================================================
# Figure 1: AUC Decay Curve
# ============================================================
def fig1_auc_decay():
    auc = {
        ('Pythia-1.4B', 'nucleus'): [0.9975, 0.8607, 0.8005],
        ('Pythia-1.4B', 'temp'):    [0.9968, 0.8327, 0.7928],
        ('Pythia-1.4B', 'topk'):    [0.9927, 0.7518, 0.6918],
        ('OLMo-1B', 'nucleus'):     [0.9834, 0.8673, 0.8124],
        ('OLMo-1B', 'temp'):        [0.996,  0.901,  0.8214],
        ('OLMo-1B', 'topk'):        [0.993,  0.8305, 0.7357],
        ('GPT-2 XL', 'nucleus'):    [0.9941, 0.9131, 0.8829],
        ('GPT-2 XL', 'temp'):       [0.9963, 0.9367, 0.8815],
        ('GPT-2 XL', 'topk'):       [0.9884, 0.8259, 0.7708],
    }

    fig, ax = plt.subplots(figsize=(7, 4.2))
    x = np.arange(3)
    x_labels = [r'd$_0$–d$_1$', r'd$_1$–d$_2$', r'd$_2$–d$_3$']

    for (model, strat), vals in auc.items():
        ax.plot(x, vals,
                color=MODEL_COLORS[model],
                linestyle=STRATEGY_LS[strat],
                marker=STRATEGY_MK[strat],
                markersize=5, linewidth=1.6,
                label=f'{model} / {strat}')

    ax.axhline(0.75, color='#666666', ls='--', lw=1, alpha=0.6, zorder=0)
    ax.text(2.05, 0.755, r'$\tau=0.75$', fontsize=9, color='#666666', va='bottom')

    below = []
    for (model, strat), vals in auc.items():
        for i, v in enumerate(vals):
            if v < 0.75:
                below.append((model, strat, i, v))
                break

    offsets_used = {}
    for model, strat, idx, v in below:
        key = (idx, round(v, 2))
        dy = -18 if key not in offsets_used else -32
        offsets_used[key] = True
        edd_val = idx + 2
        ax.annotate(f'EDD={edd_val}',
                     xy=(idx, v), xytext=(8, dy),
                     textcoords='offset points', fontsize=8,
                     color=MODEL_COLORS[model], fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color=MODEL_COLORS[model], lw=0.8))

    edd_gt3_models = set()
    for (model, strat), vals in auc.items():
        if all(v >= 0.75 for v in vals):
            edd_gt3_models.add(model)
    if edd_gt3_models:
        ax.text(0.02, 0.02,
                'EDD > 3 for all other configurations',
                transform=ax.transAxes, fontsize=8, color='#444444', style='italic')

    ax.set_xlabel('Adjacent Depth Pair')
    ax.set_ylabel('Pairwise AUC (Random Forest)')
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    ax.set_ylim(0.64, 1.02)
    ax.set_xlim(-0.15, 2.15)

    handles, labels = ax.get_legend_handles_labels()
    leg = ax.legend(handles, labels, ncol=3, loc='lower left',
                    bbox_to_anchor=(0.0, 0.06), fontsize=7.5,
                    framealpha=0.9, edgecolor='#cccccc',
                    columnspacing=1.0, handlelength=2.5)

    ax.grid(axis='y', alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT / 'fig1_auc_decay.pdf')
    fig.savefig(OUT / 'fig1_auc_decay.png')
    plt.close(fig)
    print('Figure 1: AUC Decay Curve — done')


# ============================================================
# Figure 2: Feature Trajectory Panel (3 subplots)
# ============================================================
def load_features(path):
    rows = defaultdict(list)
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            d = rec['depth']
            feats = {k: rec[k] for k in FEATURE_COLS if k in rec}
            rows[d].append(feats)
    return rows

def fig2_feature_trajectory():
    panels = [
        ('Pythia-1.4B',  BASE / 'data' / 'pythia_temp09' / 'features.jsonl'),
        ('OLMo-1B',      BASE / 'data' / 'olmo' / 'features.jsonl'),
        ('GPT-2 XL',     BASE / 'data' / 'gpt2xl' / 'features.jsonl'),
    ]
    top5 = ['p90_ppl', 'var_surprisal', 'mean_ppl', 'mean_surprisal', 'p75_ppl']
    feat_labels = {
        'p90_ppl': 'P90 Perplexity',
        'var_surprisal': 'Var(Surprisal)',
        'mean_ppl': 'Mean Perplexity',
        'mean_surprisal': 'Mean Surprisal',
        'p75_ppl': 'P75 Perplexity',
    }
    feat_colors = ['#D62728', '#2CA02C', '#2166AC', '#FF7F0E', '#9467BD']
    feat_markers = ['o', 's', '^', 'D', 'v']

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.5), sharey=True)

    for ax, (model, fpath) in zip(axes, panels):
        rows = load_features(fpath)
        depths = sorted(rows.keys())

        for fi, feat in enumerate(top5):
            means = []
            for d in depths:
                vals = [r[feat] for r in rows[d] if feat in r]
                means.append(np.mean(vals))
            normed = np.array(means) / (means[0] + 1e-12)
            ax.plot(depths, normed,
                    color=feat_colors[fi], marker=feat_markers[fi],
                    markersize=4, linewidth=1.4,
                    label=feat_labels[feat])

        ax.set_title(model, fontsize=12, color=MODEL_COLORS[model], fontweight='bold')
        ax.set_xlabel('Depth')
        ax.set_xticks(depths)
        ax.grid(alpha=0.25)

    axes[0].set_ylabel('Normalized Feature Mean\n(relative to depth 0)')
    axes[2].legend(fontsize=7, loc='upper right', framealpha=0.9, edgecolor='#cccccc')
    fig.tight_layout()
    fig.savefig(OUT / 'fig2_feature_trajectory.pdf')
    fig.savefig(OUT / 'fig2_feature_trajectory.png')
    plt.close(fig)
    print('Figure 2: Feature Trajectory — done')


# ============================================================
# Figure 3: Confusion Matrix Heatmap (2 panels)
# ============================================================
def load_Xy(path):
    X, y = [], []
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            feats = [rec.get(c, 0.0) for c in FEATURE_COLS]
            X.append(feats)
            y.append(rec['depth'])
    return np.array(X), np.array(y)

def get_confusion_matrix_cv(X, y, n_splits=5, seed=42):
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    all_true, all_pred = [], []
    for train_idx, test_idx in skf.split(X, y):
        clf = RandomForestClassifier(n_estimators=200, max_depth=None,
                                      random_state=seed, n_jobs=-1)
        clf.fit(X[train_idx], y[train_idx])
        preds = clf.predict(X[test_idx])
        all_true.extend(y[test_idx])
        all_pred.extend(preds)
    return cm_func(all_true, all_pred, labels=sorted(set(y)))

def fig3_confusion_matrices():
    cells = [
        ('GPT-2 XL / temp (best, 85.4%)',
         BASE / 'results' / 'gpt2xl_temp09' / 'features.jsonl'),
        ('Pythia / top-k (worst, 69.6%)',
         BASE / 'results' / 'pythia_topk50' / 'features.jsonl'),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.8))
    depth_labels = ['d0', 'd1', 'd2', 'd3']

    for ax, (title, fpath) in zip(axes, cells):
        print(f'  Training RF for {title}...')
        X, y = load_Xy(fpath)
        cm = get_confusion_matrix_cv(X, y)
        cm_pct = cm.astype(float) / cm.sum(axis=1, keepdims=True) * 100

        mask_diag = np.eye(4, dtype=bool)
        sns.heatmap(cm_pct, annot=True, fmt='.1f', cmap='Blues',
                    xticklabels=depth_labels, yticklabels=depth_labels,
                    vmin=0, vmax=100, ax=ax, cbar=False,
                    linewidths=0.5, linecolor='white',
                    annot_kws={'fontsize': 11})
        for i in range(4):
            ax.add_patch(plt.Rectangle((i, i), 1, 1, fill=False,
                                        edgecolor='#333333', linewidth=2))

        ax.set_xlabel('Predicted')
        ax.set_ylabel('True')
        ax.set_title(title, fontsize=11)

    fig.tight_layout(w_pad=2.5)
    fig.savefig(OUT / 'fig3_confusion_matrix.pdf')
    fig.savefig(OUT / 'fig3_confusion_matrix.png')
    plt.close(fig)
    print('Figure 3: Confusion Matrices — done')


# ============================================================
# Figure 4: Atlas Heatmap Grid (3×3)
# ============================================================
def fig4_atlas_heatmap():
    acc = np.array([
        [78.2, 76.3, 69.6],
        [78.8, 82.0, 74.2],
        [83.3, 85.4, 76.6],
    ])
    models = ['Pythia-1.4B', 'OLMo-1B', 'GPT-2 XL']
    strategies = ['nucleus', 'temp=0.9', 'top-k=50']

    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(acc, annot=True, fmt='.1f', cmap='YlOrRd',
                xticklabels=strategies, yticklabels=models,
                vmin=65, vmax=90, ax=ax,
                linewidths=1.5, linecolor='white',
                annot_kws={'fontsize': 13, 'fontweight': 'bold'},
                cbar_kws={'label': '4-Class RF Accuracy (%)', 'shrink': 0.8})

    ax.set_xlabel('Decoding Strategy', fontsize=12)
    ax.set_ylabel('Model', fontsize=12)
    ax.tick_params(axis='x', rotation=0)
    ax.tick_params(axis='y', rotation=0)

    fig.tight_layout()
    fig.savefig(OUT / 'fig4_atlas_heatmap.pdf')
    fig.savefig(OUT / 'fig4_atlas_heatmap.png')
    plt.close(fig)
    print('Figure 4: Atlas Heatmap — done')


# ============================================================
if __name__ == '__main__':
    print(f'Output directory: {OUT}')
    fig1_auc_decay()
    fig2_feature_trajectory()
    fig3_confusion_matrices()
    fig4_atlas_heatmap()
    print(f'\nAll figures saved to {OUT}')
    import os
    for f in sorted(OUT.iterdir()):
        print(f'  {f.name}  ({os.path.getsize(f)//1024}KB)')
