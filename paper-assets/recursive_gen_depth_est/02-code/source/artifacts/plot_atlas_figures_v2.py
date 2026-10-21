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

CELL_AUC_PATHS = {
    ('Pythia-1.4B', 'nucleus'): BASE / 'results' / 'pairwise_auc.json',
    ('Pythia-1.4B', 'temp'):    BASE / 'results' / 'pythia_temp09' / 'pairwise_auc.json',
    ('Pythia-1.4B', 'topk'):    BASE / 'results' / 'pythia_topk50' / 'pairwise_auc.json',
    ('OLMo-1B', 'nucleus'):     BASE / 'results' / 'olmo' / 'pairwise_auc.json',
    ('OLMo-1B', 'temp'):        BASE / 'results' / 'olmo_temp09' / 'pairwise_auc.json',
    ('OLMo-1B', 'topk'):        BASE / 'results' / 'olmo_topk50' / 'pairwise_auc.json',
    ('GPT-2 XL', 'nucleus'):    BASE / 'results' / 'gpt2xl' / 'pairwise_auc.json',
    ('GPT-2 XL', 'temp'):       BASE / 'results' / 'gpt2xl_temp09' / 'pairwise_auc.json',
    ('GPT-2 XL', 'topk'):       BASE / 'results' / 'gpt2xl_topk50' / 'pairwise_auc.json',
}

ATLAS_GRID = [
    ('Pythia-1.4B', [
        ('nucleus', 'pythia_nucleus095'),
        ('temp',    'pythia_temp09'),
        ('topk',    'pythia_topk50'),
    ]),
    ('OLMo-1B', [
        ('nucleus', 'olmo_nucleus095'),
        ('temp',    'olmo_temp09'),
        ('topk',    'olmo_topk50'),
    ]),
    ('GPT-2 XL', [
        ('nucleus', 'gpt2xl_nucleus095'),
        ('temp',    'gpt2xl_temp09'),
        ('topk',    'gpt2xl_topk50'),
    ]),
]

CELL_FEATURES_PATHS = {
    'pythia_nucleus095': BASE / 'data' / 'features_all.jsonl',
    'pythia_temp09':     BASE / 'data' / 'pythia_temp09' / 'features.jsonl',
    'pythia_topk50':     BASE / 'results' / 'pythia_topk50' / 'features.jsonl',
    'olmo_nucleus095':   BASE / 'data' / 'olmo' / 'features.jsonl',
    'olmo_temp09':       BASE / 'results' / 'olmo_temp09' / 'features.jsonl',
    'olmo_topk50':       BASE / 'results' / 'olmo_topk50' / 'features.jsonl',
    'gpt2xl_nucleus095': BASE / 'data' / 'gpt2xl' / 'features.jsonl',
    'gpt2xl_temp09':     BASE / 'results' / 'gpt2xl_temp09' / 'features.jsonl',
    'gpt2xl_topk50':     BASE / 'results' / 'gpt2xl_topk50' / 'features.jsonl',
}


def load_pipeline_auc():
    auc = {}
    for key, path in CELL_AUC_PATHS.items():
        if not path.exists():
            raise FileNotFoundError(f"Pipeline AUC file missing: {path}")
        with open(path) as f:
            data = json.load(f)
        rf = data['random_forest']
        auc[key] = [
            rf['depth0_vs_depth1'],
            rf['depth1_vs_depth2'],
            rf['depth2_vs_depth3'],
        ]
    return auc


# ============================================================
# Figure 1: AUC Decay Curve
# ============================================================
def fig1_auc_decay():
    auc = load_pipeline_auc()

    fig, ax = plt.subplots(figsize=(7, 4.2))
    x = np.arange(3)
    x_labels = [r'd$_0$-d$_1$', r'd$_1$-d$_2$', r'd$_2$-d$_3$']

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

    offsets_map = {}
    for model, strat, idx, v in below:
        key = idx
        cnt = offsets_map.get(key, 0)
        dy = -18 - cnt * 16
        offsets_map[key] = cnt + 1
        edd_val = idx + 1
        ax.annotate(f'EDD={edd_val}',
                     xy=(idx, v), xytext=(8, dy),
                     textcoords='offset points', fontsize=8,
                     color=MODEL_COLORS[model], fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color=MODEL_COLORS[model], lw=0.8))

    ax.text(0.02, 0.02,
            'EDD > 3 for 7/9 configurations (unsaturated)',
            transform=ax.transAxes, fontsize=8, color='#444444', style='italic')

    ax.set_xlabel('Adjacent Depth Pair')
    ax.set_ylabel('Pairwise AUC (Random Forest)')
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    ax.set_ylim(0.64, 1.02)
    ax.set_xlim(-0.15, 2.15)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, ncol=3, loc='lower left',
              bbox_to_anchor=(0.0, 0.06), fontsize=7.5,
              framealpha=0.9, edgecolor='#cccccc',
              columnspacing=1.0, handlelength=2.5)

    ax.grid(axis='y', alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT / 'fig1_auc_decay.pdf')
    fig.savefig(OUT / 'fig1_auc_decay.png')
    plt.close(fig)
    print('Figure 1: AUC Decay Curve -- done')


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
        ('Pythia-1.4B', 'Pythia-1.4B (temp τ=0.9)',  BASE / 'data' / 'pythia_temp09' / 'features.jsonl'),
        ('OLMo-1B', 'OLMo-1B (nucleus p=0.95)',      BASE / 'data' / 'olmo' / 'features.jsonl'),
        ('GPT-2 XL', 'GPT-2 XL (nucleus p=0.95)',     BASE / 'data' / 'gpt2xl' / 'features.jsonl'),
    ]
    top5 = ['p90_ppl', 'var_surprisal', 'mean_ppl', 'mean_surprisal', 'p75_ppl']
    feat_labels = {
        'p90_ppl': 'P90 PPL',
        'var_surprisal': 'Var(Surprisal)',
        'mean_ppl': 'Mean PPL',
        'mean_surprisal': 'Mean Surprisal',
        'p75_ppl': 'P75 PPL',
    }
    feat_colors = ['#D62728', '#2CA02C', '#2166AC', '#FF7F0E', '#9467BD']
    feat_markers = ['o', 's', '^', 'D', 'v']

    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.5), sharey=True)

    for ax, (model_key, model, fpath) in zip(axes, panels):
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

        ax.set_title(model, fontsize=11, color=MODEL_COLORS[model_key], fontweight='bold')
        ax.set_xlabel('Depth')
        ax.set_xticks(depths)
        ax.grid(alpha=0.25)

    axes[0].set_ylabel('Normalized Feature Mean\n(relative to depth 0)')
    axes[2].legend(fontsize=7, loc='upper right', framealpha=0.9, edgecolor='#cccccc')
    fig.tight_layout()
    fig.savefig(OUT / 'fig2_feature_trajectory.pdf')
    fig.savefig(OUT / 'fig2_feature_trajectory.png')
    plt.close(fig)
    print('Figure 2: Feature Trajectory -- done')


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
    X = np.array(X, dtype=np.float64)
    X = np.nan_to_num(X, nan=0.0, posinf=1e15, neginf=-1e15)
    X = np.clip(X, -1e15, 1e15)
    return X, np.array(y)

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
        ('GPT-2 XL / temp',
         BASE / 'results' / 'gpt2xl_temp09' / 'features.jsonl'),
        ('Pythia / top-k',
         BASE / 'results' / 'pythia_topk50' / 'features.jsonl'),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.8))
    depth_labels = ['d0', 'd1', 'd2', 'd3']

    for ax, (label, fpath) in zip(axes, cells):
        print(f'  Training RF for {label}...')
        X, y = load_Xy(fpath)
        cm = get_confusion_matrix_cv(X, y)
        cv_acc = np.trace(cm) / cm.sum() * 100
        title = f'{label} (5-fold CV acc: {cv_acc:.1f}%)'
        cm_pct = cm.astype(float) / cm.sum(axis=1, keepdims=True) * 100

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
    print('Figure 3: Confusion Matrices -- done')


# ============================================================
# Figure 4: Atlas Heatmap Grid (3x3)
# ============================================================
def fig4_atlas_heatmap():
    models = ['Pythia-1.4B', 'OLMo-1B', 'GPT-2 XL']
    strategies = ['nucleus', 'temp=0.9', 'top-k=50']

    acc = np.zeros((3, 3))
    for i, (model_name, cells) in enumerate(ATLAS_GRID):
        for j, (strat, cell_key) in enumerate(cells):
            fpath = CELL_FEATURES_PATHS[cell_key]
            if not fpath.exists():
                raise FileNotFoundError(f"Features file missing: {fpath}")
            print(f'  Computing RF accuracy for {cell_key}...')
            X, y = load_Xy(fpath)
            cm = get_confusion_matrix_cv(X, y)
            acc[i, j] = np.trace(cm) / cm.sum() * 100

    print(f'  Accuracy matrix:\n{acc}')

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
    print('Figure 4: Atlas Heatmap -- done')


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
