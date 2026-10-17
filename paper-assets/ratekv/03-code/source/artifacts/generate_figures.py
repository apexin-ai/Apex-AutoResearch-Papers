"""Generate paper figures for RateKV head sensitivity analysis."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm, Normalize
from matplotlib.ticker import MaxNLocator
import numpy as np
import json
import os

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

COLORS_MODEL = {
    'qwen': '#D55E00',
    'llama': '#0072B2',
    'mistral': '#CC79A7',
}
COLORS_BIT = {
    2: '#E69F00',
    4: '#56B4E9',
    8: '#009E73',
    16: '#F0E442',
}

OUT_DIR = '/root/ratekv/figures'


def load_profiles(path):
    with open(path) as f:
        data = json.load(f)
    profiles = data['profiles']
    n_layers = len(profiles)
    n_heads = len(profiles['0'])
    delta_2bit = np.zeros((n_layers, n_heads))
    for li in range(n_layers):
        for hi in range(n_heads):
            delta_2bit[li, hi] = profiles[str(li)][str(hi)]['quantization']['2']
    return delta_2bit, n_layers, n_heads


def fig1_heatmap():
    models = [
        ('Qwen2.5-7B', '/root/ratekv/ppl_profiles_hires.json', 'GQA 7:1'),
        ('Llama-3.1-8B', '/root/ratekv/llama_ppl_profiles_hires.json', 'GQA 4:1'),
        ('Mistral-7B-v0.3', '/root/ratekv/mistral_ppl_profiles_hires.json', 'GQA 4:1'),
    ]

    deltas = []
    infos = []
    for name, path, gqa in models:
        d, nl, nh = load_profiles(path)
        deltas.append(d)
        infos.append((name, nl, nh, gqa))

    vmin = 0
    vmax = max(d.max() for d in deltas)
    vmax = min(vmax, 10.0)

    fig, axes = plt.subplots(1, 3, figsize=(14, 5.5),
                              gridspec_kw={'width_ratios': [4, 8, 8], 'wspace': 0.15})

    for idx, (ax, delta, (name, nl, nh, gqa)) in enumerate(zip(axes, deltas, infos)):
        im = ax.imshow(delta, aspect='auto', origin='lower',
                       cmap='YlOrRd', vmin=vmin, vmax=vmax,
                       interpolation='nearest')
        ax.set_title(f'{name}\n({gqa}, {nl}L×{nh}H)', fontsize=11, pad=8)
        ax.set_xlabel('KV Head Index')
        if idx == 0:
            ax.set_ylabel('Layer Index')
        ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=8))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        layer0_max = delta[0].max()
        if layer0_max > 1.0:
            max_h = int(np.argmax(delta[0]))
            ax.annotate(f'L0: Δ={layer0_max:.1f}',
                        xy=(max_h, 0), xytext=(max_h + 0.5, nl * 0.15),
                        fontsize=8, color='#333333',
                        arrowprops=dict(arrowstyle='->', color='#333333', lw=1.0),
                        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#999999', alpha=0.9))

    cbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])
    cbar = fig.colorbar(im, cax=cbar_ax)
    cbar.set_label('2-bit Δ PPL', fontsize=11)

    fig.suptitle('Per-Head Quantization Sensitivity (2-bit Delta)', fontsize=14, y=1.02)

    for fmt in ['pdf', 'png']:
        fig.savefig(os.path.join(OUT_DIR, f'fig1_head_delta_heatmap.{fmt}'),
                    bbox_inches='tight', dpi=300)
    plt.close(fig)
    print('fig1 done')


def fig2_compounding():
    with open('/root/ratekv/compounding_sweep_results.json') as f:
        sweep = json.load(f)
    with open('/root/ratekv/compounding_k10_12_results.json') as f:
        k10_12 = json.load(f)

    all_points = {}
    for entry in sweep + k10_12:
        k = entry['max_2bit']
        all_points[k] = entry['ppl']

    ks = sorted(all_points.keys())
    ppls = [all_points[k] for k in ks]

    fig, ax = plt.subplots(figsize=(7, 4.5))

    ax.plot(ks, ppls, 'o-', color=COLORS_MODEL['qwen'], markersize=6, zorder=3)

    best_k = 8
    best_ppl = all_points[best_k]
    ax.annotate(f'k={best_k}, PPL={best_ppl:.2f}',
                xy=(best_k, best_ppl),
                xytext=(best_k + 12, best_ppl - 1.5),
                fontsize=10,
                arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2),
                bbox=dict(boxstyle='round,pad=0.3', fc='#FFF5E6', ec=COLORS_MODEL['qwen'], alpha=0.95))

    uniform_ppl = all_points[0]
    ax.axhline(y=uniform_ppl, color='#999999', linestyle='--', linewidth=1.2, zorder=1)
    ax.text(max(ks) * 0.6, uniform_ppl + 0.5,
            f'Uniform 4-bit (PPL={uniform_ppl:.2f})',
            fontsize=9, color='#666666', ha='center')

    ax.set_xlabel('Max 2-bit Heads (k)')
    ax.set_ylabel('Perplexity')
    ax.set_title('Compounding Effect of 2-bit Quantization\n(Qwen2.5-7B, Budget=0.25)', fontsize=13)

    ax.set_ylim(bottom=max(0, min(ppls) - 2), top=min(40, max(ppls) + 3))

    for fmt in ['pdf', 'png']:
        fig.savefig(os.path.join(OUT_DIR, f'fig2_compounding_curve.{fmt}'),
                    bbox_inches='tight', dpi=300)
    plt.close(fig)
    print('fig2 done')


def fig3_allocation():
    with open('/root/ratekv/compounding_sweep_results.json') as f:
        sweep = json.load(f)

    mckp_alloc = None
    for entry in sweep:
        if entry['max_2bit'] == 8:
            mckp_alloc = entry['allocation']
            break

    n_layers = 28
    n_heads = 4
    bit_levels = [2, 4, 8, 16]

    uniform_counts = np.zeros((n_layers, len(bit_levels)))
    mckp_counts = np.zeros((n_layers, len(bit_levels)))

    for li in range(n_layers):
        uniform_counts[li, bit_levels.index(4)] = n_heads

    for key, val in mckp_alloc.items():
        li = int(key.split(',')[0])
        bit = val[1]
        bi = bit_levels.index(bit)
        mckp_counts[li, bi] += 1

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
    x = np.arange(n_layers)
    bar_width = 0.8

    for ax, counts, title in zip(axes,
                                  [uniform_counts, mckp_counts],
                                  ['Uniform 4-bit', 'MCKP Allocation']):
        bottom = np.zeros(n_layers)
        for bi, bit in enumerate(bit_levels):
            vals = counts[:, bi]
            if vals.sum() > 0:
                ax.bar(x, vals, bar_width, bottom=bottom,
                       color=COLORS_BIT[bit], label=f'{bit}-bit',
                       edgecolor='white', linewidth=0.3)
            bottom += vals
        ax.set_xlabel('Layer Index')
        ax.set_title(title, fontsize=12)
        ax.set_xlim(-0.5, n_layers - 0.5)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=10))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    axes[0].set_ylabel('Number of KV Heads')

    handles, labels = [], []
    for bit in bit_levels:
        handles.append(plt.Rectangle((0, 0), 1, 1, fc=COLORS_BIT[bit]))
        labels.append(f'{bit}-bit')
    fig.legend(handles, labels, loc='upper center', ncol=4,
               bbox_to_anchor=(0.5, 1.02), frameon=False, fontsize=10)

    fig.suptitle('Bit-Width Allocation per Layer (Qwen2.5-7B, Budget=0.25)',
                 fontsize=13, y=1.08)

    for fmt in ['pdf', 'png']:
        fig.savefig(os.path.join(OUT_DIR, f'fig3_allocation_comparison.{fmt}'),
                    bbox_inches='tight', dpi=300)
    plt.close(fig)
    print('fig3 done')


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    fig1_heatmap()
    fig2_compounding()
    fig3_allocation()
    print(f'All figures saved to {OUT_DIR}')
