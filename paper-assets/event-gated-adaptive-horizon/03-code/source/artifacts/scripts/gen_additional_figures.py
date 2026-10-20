"""Generate Figures 3-5 for the Event-Gated Adaptive Horizon paper.

Usage (on server with matplotlib):
    python gen_additional_figures.py --datadir /path/to/analysis --outdir /path/to/figures
"""
import json
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

COLORS = {
    '008d': '#d62728',
    '008f': '#2ca02c',
    '018v2': '#1f77b4',
    '008e': '#9467bd',
    '015b': '#ff7f0e',
    '010b': '#8c564b',
    '008a': '#7f7f7f',
}

def get_color(label):
    for key, color in COLORS.items():
        if key in label:
            return color
    return '#333333'

def fig3_entropy_dynamics(datadir, outdir):
    with open(datadir / 'entropy_dynamics_data.json') as f:
        data = json.load(f)

    fig, ax = plt.subplots(figsize=(7, 4))

    for label, series in data.items():
        steps = [d['step'] / 1000 for d in series]
        entropy = [d['actor_entropy'] for d in series]
        color = get_color(label)
        ls = '--' if 'Pathway B' in label else '-'
        lw = 2.5 if 'CIVO' in label or 'Pathway B' in label else 1.8
        ax.plot(steps, entropy, color=color, ls=ls, lw=lw, marker='o', ms=4, label=label)

    ax.axhspan(-6, -5, alpha=0.08, color='green', label='Stable convergence zone')
    ax.annotate('Entropy rebound\n(Pathway B collapse)',
                xy=(95, -4.53), xytext=(75, -2.5),
                arrowprops=dict(arrowstyle='->', color='#9467bd', lw=1.5),
                fontsize=8, color='#9467bd', ha='center')
    ax.annotate('Training ends\n(CIVO crash)',
                xy=(55, -4.88), xytext=(45, -2.0),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.5),
                fontsize=8, color='#d62728', ha='center')

    ax.set_xlabel('Training Step (×1000)', fontsize=11)
    ax.set_ylabel('Actor Entropy (nats)', fontsize=11)
    ax.set_title('Figure 3: Actor Entropy Dynamics Across Collapse Pathways', fontsize=12, fontweight='bold')
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 115)

    fig.tight_layout()
    fig.savefig(outdir / 'fig3_entropy_dynamics.pdf', dpi=300, bbox_inches='tight')
    fig.savefig(outdir / 'fig3_entropy_dynamics.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved fig3_entropy_dynamics.pdf/png')


def fig4_civo_decomposition(datadir, outdir):
    with open(datadir / 'civo_decomposition_data.json') as f:
        data = json.load(f)

    labels_order = [
        '008a (unexposed)',
        '018v2 (Full-SGS)',
        '008f (no dt_emb)',
        '015b (frozen dt_emb)',
        '008d (trained dt_emb)',
        '010b (Cheetah)',
    ]

    fig, ax = plt.subplots(figsize=(8, 4.5))

    x_positions = np.arange(len(labels_order))
    bar_width = 0.35

    eval_finals = []
    value_finals = []
    short_labels = []

    for label in labels_order:
        series = data[label]
        last = series[-1]
        eval_finals.append(last.get('eval_return', 0))
        value_finals.append(last.get('value_mean', 0))
        short_labels.append(label.split('(')[1].rstrip(')'))

    bars_eval = ax.bar(x_positions - bar_width/2, eval_finals, bar_width,
                       label='Eval Return (actual)', color='#2ca02c', alpha=0.8)
    bars_value = ax.bar(x_positions + bar_width/2, value_finals, bar_width,
                        label='Value Mean (imagined)', color='#d62728', alpha=0.8)

    for i, (ev, vm) in enumerate(zip(eval_finals, value_finals)):
        nve = vm - ev
        if abs(nve) > 20:
            y_pos = max(ev, vm) + 15
            color = '#d62728' if nve > 0 else '#2ca02c'
            ax.text(i, y_pos, f'NVE={nve:+.0f}', ha='center', fontsize=7,
                    color=color, fontweight='bold')

    ax.set_xticks(x_positions)
    ax.set_xticklabels(short_labels, fontsize=9, rotation=15, ha='right')
    ax.set_ylabel('Return / Value', fontsize=11)
    ax.set_title('Figure 4: CIVO Decomposition — Final Value vs. Actual Return', fontsize=12, fontweight='bold')
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(True, axis='y', alpha=0.3)

    fig.tight_layout()
    fig.savefig(outdir / 'fig4_civo_decomposition.pdf', dpi=300, bbox_inches='tight')
    fig.savefig(outdir / 'fig4_civo_decomposition.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved fig4_civo_decomposition.pdf/png')


def fig5_value_vs_eval(datadir, outdir):
    with open(datadir / 'value_vs_eval_data.json') as f:
        data = json.load(f)

    fig, axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True)
    axes = axes.flatten()

    panel_order = [
        '008d (CIVO trigger)',
        '008f (no dt_emb, healthy)',
        '018v2 (Full-SGS)',
        '008e_v3_s2 (Pathway B)',
    ]
    panel_titles = [
        '(a) 008d — CIVO Trigger (Pathway A)',
        '(b) 008f — No dt_emb (Healthy)',
        '(c) 018v2 — Full-SGS (Healthy)',
        '(d) 008e_v3_s2 — Pathway B Collapse',
    ]

    for idx, (label, title) in enumerate(zip(panel_order, panel_titles)):
        ax = axes[idx]
        series = data[label]
        steps = [d['step'] / 1000 for d in series]
        value_mean = [d['value_mean'] for d in series]
        eval_return = [d['eval_return'] for d in series]

        ax.plot(steps, eval_return, 'o-', color='#2ca02c', lw=2, ms=5, label='Eval Return')
        ax.plot(steps, value_mean, 's--', color='#d62728', lw=2, ms=5, label='Value Mean')

        for i in range(len(steps)):
            vm, er = value_mean[i], eval_return[i]
            if vm > er * 1.2 and vm > 30:
                ax.fill_between([steps[i]-2, steps[i]+2],
                                [er, er], [vm, vm],
                                alpha=0.15, color='#d62728')

        ax.set_title(title, fontsize=10, fontweight='bold')
        ax.grid(True, alpha=0.3)
        if idx >= 2:
            ax.set_xlabel('Training Step (×1000)', fontsize=10)
        ax.set_ylabel('Value / Return', fontsize=10)
        if idx == 0:
            ax.legend(fontsize=8, loc='upper left')

    fig.suptitle('Figure 5: Value Mean vs. Eval Return — Divergence Indicates CIVO',
                 fontsize=12, fontweight='bold', y=1.02)
    fig.tight_layout()
    fig.savefig(outdir / 'fig5_value_vs_eval.pdf', dpi=300, bbox_inches='tight')
    fig.savefig(outdir / 'fig5_value_vs_eval.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved fig5_value_vs_eval.pdf/png')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--datadir', type=Path, default=Path('artifacts/analysis'))
    parser.add_argument('--outdir', type=Path, default=Path('artifacts/figures'))
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)

    fig3_entropy_dynamics(args.datadir, args.outdir)
    fig4_civo_decomposition(args.datadir, args.outdir)
    fig5_value_vs_eval(args.datadir, args.outdir)

    print(f'\nAll figures saved to {args.outdir}/')


if __name__ == '__main__':
    main()
