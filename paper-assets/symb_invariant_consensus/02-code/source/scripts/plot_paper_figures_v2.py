import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'axes.titlesize': 9,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.2,
})

OUTDIR = '/root/symb_invariant_consensus/artifacts/figures/paper'
os.makedirs(OUTDIR, exist_ok=True)

# Okabe-Ito colorblind-friendly palette
OI_BLUE    = '#0072B2'
OI_ORANGE  = '#E69F00'
OI_GREEN   = '#009E73'
OI_RED     = '#D55E00'
OI_PURPLE  = '#CC79A7'
OI_SKYBLUE = '#56B4E9'
OI_YELLOW  = '#F0E442'
OI_BLACK   = '#000000'

# ============================================================
# Figure 1: operating_regime (C0 vs SICA-SC gap scatter)
# ============================================================
def plot_operating_regime():
    data = [
        ('Qwen2.5-14B',    'FOLIO+PW',    804, 38.2,  +0.3),
        ('Qwen2.5-14B',    'StrategyQA',   60, 10.0,  +3.33),
        ('Qwen2.5-14B',    'ARC-Chall',    60,  5.0,  -1.67),
        ('Mistral-7B',     'FOLIO+PW',     60, 50.0,   0.0),
        ('LLaMA-3.1-8B',   'StrategyQA',  200, 41.0,  +2.0),
        ('LLaMA-3.1-8B',   'FOLIO',       204, 61.8,  -2.45),
        ('DeepSeek-R1-7B',  'FOLIO+PW',    60, 58.3,  -3.33),
        ('Qwen2.5-14B',    'GSM8K',        30, 13.3,   0.0),
    ]

    models = sorted(set(r[0] for r in data))
    model_colors = {
        'Qwen2.5-14B':    OI_BLUE,
        'Mistral-7B':     OI_PURPLE,
        'LLaMA-3.1-8B':   OI_ORANGE,
        'DeepSeek-R1-7B':  OI_RED,
    }
    model_markers = {
        'Qwen2.5-14B':    'o',
        'Mistral-7B':     's',
        'LLaMA-3.1-8B':   '^',
        'DeepSeek-R1-7B':  'D',
    }

    fig, ax = plt.subplots(figsize=(3.25, 2.6))

    ax.axhline(0, color='#888888', linewidth=0.8, linestyle='-', zorder=1)

    for model, domain, n, c0, delta in data:
        size = np.sqrt(n) * 1.8
        color = model_colors[model]
        marker = model_markers[model]
        ax.scatter(c0, delta, s=size, c=color, marker=marker,
                   edgecolors='white', linewidths=0.4, zorder=3, alpha=0.9)

        label_text = f'{domain}'
        offset_x, offset_y = 1.5, 0.3
        if domain == 'FOLIO+PW' and model == 'Qwen2.5-14B':
            offset_y = -0.6
        if domain == 'FOLIO' and model == 'LLaMA-3.1-8B':
            offset_x = -1.5
            offset_y = -0.6
        if domain == 'StrategyQA' and model == 'LLaMA-3.1-8B':
            offset_y = 0.5
        if domain == 'FOLIO+PW' and model == 'DeepSeek-R1-7B':
            offset_y = -0.6

        ax.annotate(label_text, (c0, delta),
                    xytext=(offset_x, offset_y), textcoords='offset points',
                    fontsize=5.5, color='#444444', ha='left', va='bottom')

    handles = []
    for model in models:
        h = ax.scatter([], [], s=30, c=model_colors[model],
                       marker=model_markers[model], edgecolors='white',
                       linewidths=0.4, label=model)
        handles.append(h)

    size_legend_ns = [30, 200, 800]
    for n_val in size_legend_ns:
        h = ax.scatter([], [], s=np.sqrt(n_val)*1.8, c='#CCCCCC',
                       edgecolors='#666666', linewidths=0.4,
                       label=f'n={n_val}')
        handles.append(h)

    ax.legend(handles=handles, loc='upper left', fontsize=5.5,
              framealpha=0.9, edgecolor='#CCCCCC', ncol=2,
              handletextpad=0.3, columnspacing=0.8, borderpad=0.4)

    ax.set_xlabel(r'Multi-candidate rate $C_0$ (%)')
    ax.set_ylabel(r'SICA$-$SC accuracy gap (pp)')
    ax.set_xlim(-2, 70)
    ax.set_ylim(-5, 5)
    ax.grid(True, alpha=0.2, linewidth=0.5)

    for fmt in ['pdf', 'png']:
        path = os.path.join(OUTDIR, f'operating_regime.{fmt}')
        fig.savefig(path)
        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')
    plt.close(fig)


# ============================================================
# Figure 2: capability_scatter (vote entropy vs exclusion rate)
# ============================================================
def plot_capability_scatter():
    csv_path = '/root/symb_invariant_consensus/analysis/f2_per_problem.csv'
    df = pd.read_csv(csv_path)

    fig, ax = plt.subplots(figsize=(3.25, 2.6))

    mask_correct = df['sica_correct'] == 1
    mask_wrong = df['sica_correct'] == 0
    mask_flipped = df['sica_flipped'] == 1

    ax.scatter(df.loc[mask_correct & ~mask_flipped, 'vote_entropy'],
               df.loc[mask_correct & ~mask_flipped, 'constraint_exclusion_rate'],
               s=8, c=OI_GREEN, alpha=0.5, edgecolors='none',
               label='SICA correct', zorder=2, rasterized=True)

    ax.scatter(df.loc[mask_wrong & ~mask_flipped, 'vote_entropy'],
               df.loc[mask_wrong & ~mask_flipped, 'constraint_exclusion_rate'],
               s=8, c=OI_RED, alpha=0.5, edgecolors='none',
               label='SICA wrong', zorder=2, rasterized=True)

    ax.scatter(df.loc[mask_flipped, 'vote_entropy'],
               df.loc[mask_flipped, 'constraint_exclusion_rate'],
               s=18, c=OI_SKYBLUE, alpha=0.85, edgecolors=OI_BLUE,
               linewidths=0.5, marker='D',
               label='SICA flipped', zorder=4)

    ax.set_xlabel('Vote entropy (K=12)')
    ax.set_ylabel('Constraint exclusion rate')
    ax.grid(True, alpha=0.2, linewidth=0.5)

    ax.legend(loc='upper right', fontsize=6, framealpha=0.9,
              edgecolor='#CCCCCC', handletextpad=0.3, borderpad=0.4,
              markerscale=1.2)

    for fmt in ['pdf', 'png']:
        path = os.path.join(OUTDIR, f'capability_scatter.{fmt}')
        fig.savefig(path)
        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')
    plt.close(fig)


if __name__ == '__main__':
    print('=== Figure 1: operating_regime ===')
    plot_operating_regime()
    print()
    print('=== Figure 2: capability_scatter ===')
    plot_capability_scatter()
    print()
    print('Done.')
