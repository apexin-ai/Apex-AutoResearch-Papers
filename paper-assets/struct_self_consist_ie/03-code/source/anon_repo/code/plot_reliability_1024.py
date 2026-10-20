#!/usr/bin/env python3
"""Fig: ECE reliability diagram from exp_012_rerun_1024 per-instance data."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
from pathlib import Path

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

COLORS = {'sj': '#56B4E9', 'voting': '#E69F00', 'logprob': '#0072B2'}
MARKERS = {'sj': 'o', 'voting': 's', 'logprob': '^'}

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/reliability_data_1024.json"
FIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/artifacts/figures')
FIG_DIR.mkdir(parents=True, exist_ok=True)

data = json.load(open(DATA_PATH))

def compute_bins(confidences, accuracies, n_bins=10):
    bin_edges = np.linspace(0, 1, n_bins + 1)
    bin_accs, bin_confs, bin_counts = [], [], []
    for i in range(n_bins):
        lo, hi = bin_edges[i], bin_edges[i + 1]
        if i == n_bins - 1:
            mask = (confidences >= lo) & (confidences <= hi)
        else:
            mask = (confidences >= lo) & (confidences < hi)
        if mask.sum() > 0:
            bin_accs.append(accuracies[mask].mean())
            bin_confs.append(confidences[mask].mean())
            bin_counts.append(mask.sum())
        else:
            bin_accs.append(np.nan)
            bin_confs.append((lo + hi) / 2)
            bin_counts.append(0)
    return np.array(bin_accs), np.array(bin_confs), np.array(bin_counts), bin_edges

def compute_ece(bin_accs, bin_confs, bin_counts):
    total = bin_counts.sum()
    if total == 0:
        return 0.0
    valid = ~np.isnan(bin_accs)
    return np.sum(bin_counts[valid] / total * np.abs(bin_accs[valid] - bin_confs[valid]))

# Prepare arrays
ner_mask = [d['has_gold_ents'] for d in data]
re_mask = [d['has_gold_rels'] for d in data]

sj_ner = np.array([d['sj_ner'] for d, m in zip(data, ner_mask) if m and d['sj_ner'] is not None])
vc_ner = np.array([d['vc_ner'] for d, m in zip(data, ner_mask) if m])
f1_ner = np.array([d['mean_sample_ner_f1'] for d, m in zip(data, ner_mask) if m and d['sj_ner'] is not None])
f1_ner_vc = np.array([d['mean_sample_ner_f1'] for d, m in zip(data, ner_mask) if m])
lp_raw_ner = np.array([d['mean_logprob'] for d, m in zip(data, ner_mask) if m and d['mean_logprob'] is not None])
f1_ner_lp = np.array([d['mean_sample_ner_f1'] for d, m in zip(data, ner_mask) if m and d['mean_logprob'] is not None])

sj_re = np.array([d['sj_re'] for d, m in zip(data, re_mask) if m and d['sj_re'] is not None])
vc_re = np.array([d['vc_re'] for d, m in zip(data, re_mask) if m])
f1_re = np.array([d['mean_sample_re_f1'] for d, m in zip(data, re_mask) if m and d['sj_re'] is not None])
f1_re_vc = np.array([d['mean_sample_re_f1'] for d, m in zip(data, re_mask) if m])
lp_raw_re = np.array([d['mean_logprob'] for d, m in zip(data, re_mask) if m and d['mean_logprob'] is not None])
f1_re_lp = np.array([d['mean_sample_re_f1'] for d, m in zip(data, re_mask) if m and d['mean_logprob'] is not None])

# Normalize logprob to [0,1]
all_lp = np.array([d['mean_logprob'] for d in data if d['mean_logprob'] is not None])
lp_min, lp_max = all_lp.min(), all_lp.max()
lp_ner_norm = (lp_raw_ner - lp_min) / (lp_max - lp_min)
lp_re_norm = (lp_raw_re - lp_min) / (lp_max - lp_min)

n_bins = 10

fig, axes = plt.subplots(2, 2, figsize=(10, 4.5),
                         gridspec_kw={'height_ratios': [3, 1], 'hspace': 0.08, 'wspace': 0.3},
                         sharex='col')

panels = [
    {
        'title': 'NER (N=1024)',
        'signals': [
            ('Soft Jaccard', 'sj', sj_ner, f1_ner),
            ('Voting Conf.', 'voting', vc_ner, f1_ner_vc),
            ('Logprob', 'logprob', lp_ner_norm, f1_ner_lp),
        ],
        'ax_main': axes[0, 0],
        'ax_hist': axes[1, 0],
    },
    {
        'title': 'RE (N=1024)',
        'signals': [
            ('Soft Jaccard', 'sj', sj_re, f1_re),
            ('Voting Conf.', 'voting', vc_re, f1_re_vc),
            ('Logprob', 'logprob', lp_re_norm, f1_re_lp),
        ],
        'ax_main': axes[0, 1],
        'ax_hist': axes[1, 1],
    },
]

for panel in panels:
    ax_main = panel['ax_main']
    ax_hist = panel['ax_hist']
    ax_main.plot([0, 1], [0, 1], 'k--', linewidth=1, alpha=0.5, zorder=1)

    for label, key, confs, accs in panel['signals']:
        bin_accs, bin_confs, bin_counts, bin_edges = compute_bins(confs, accs, n_bins)
        ece = compute_ece(bin_accs, bin_confs, bin_counts)
        valid = ~np.isnan(bin_accs)
        ax_main.plot(bin_confs[valid], bin_accs[valid],
                     marker=MARKERS[key], color=COLORS[key],
                     label=f'{label} (ECE={ece:.3f})',
                     markersize=5, zorder=2)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        ax_hist.bar(bin_centers, bin_counts, width=0.08, alpha=0.4,
                    color=COLORS[key], zorder=2)

    ax_main.set_xlim(0, 1)
    ax_main.set_ylim(0, 1)
    ax_main.set_ylabel('Mean F1')
    ax_main.set_title(panel['title'])
    ax_main.legend(loc='upper left', fontsize=8.5, framealpha=0.9)
    ax_main.grid(True, alpha=0.2, zorder=0)
    ax_main.tick_params(labelbottom=False)
    ax_hist.set_xlabel('Confidence')
    ax_hist.set_ylabel('Count', fontsize=9)
    ax_hist.set_xlim(0, 1)
    ax_hist.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax_hist.grid(True, alpha=0.2, zorder=0)

outpath = FIG_DIR / 'fig_reliability_1024.pdf'
plt.savefig(outpath)
plt.close()
print(f'Saved: {outpath}')

png_path = str(outpath).replace('.pdf', '.png')
fig2, axes2 = plt.subplots(2, 2, figsize=(10, 4.5),
                           gridspec_kw={'height_ratios': [3, 1], 'hspace': 0.08, 'wspace': 0.3},
                           sharex='col')
for pi, panel in enumerate(panels):
    ax_main = axes2[0, pi]
    ax_hist = axes2[1, pi]
    ax_main.plot([0, 1], [0, 1], 'k--', linewidth=1, alpha=0.5, zorder=1)
    for label, key, confs, accs in panel['signals']:
        bin_accs, bin_confs, bin_counts, bin_edges = compute_bins(confs, accs, n_bins)
        ece = compute_ece(bin_accs, bin_confs, bin_counts)
        valid = ~np.isnan(bin_accs)
        ax_main.plot(bin_confs[valid], bin_accs[valid],
                     marker=MARKERS[key], color=COLORS[key],
                     label=f'{label} (ECE={ece:.3f})',
                     markersize=5, zorder=2)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        ax_hist.bar(bin_centers, bin_counts, width=0.08, alpha=0.4,
                    color=COLORS[key], zorder=2)
    ax_main.set_xlim(0, 1)
    ax_main.set_ylim(0, 1)
    ax_main.set_ylabel('Mean F1')
    ax_main.set_title(panel['title'])
    ax_main.legend(loc='upper left', fontsize=8.5, framealpha=0.9)
    ax_main.grid(True, alpha=0.2, zorder=0)
    ax_main.tick_params(labelbottom=False)
    ax_hist.set_xlabel('Confidence')
    ax_hist.set_ylabel('Count', fontsize=9)
    ax_hist.set_xlim(0, 1)
    ax_hist.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax_hist.grid(True, alpha=0.2, zorder=0)
plt.savefig(png_path, dpi=150)
plt.close()
print(f'Saved: {png_path}')
