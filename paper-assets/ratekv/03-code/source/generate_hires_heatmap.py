"""Generate 5-model head delta heatmap using hires profiling data."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
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
})

OUT_DIR = '/root/ratekv/figures'

MODELS = [
    {
        'name': 'Gemma-2-9B',
        'path': '/root/ratekv/gemma2_hires_bf16_2bitonly_profiles.json',
        'gqa': 'GQA 2:1',
        'source': 'hires',
    },
    {
        'name': 'Llama-3.1-8B',
        'path': '/root/ratekv/llama_hires_bf16_2bitonly_profiles.json',
        'gqa': 'GQA 4:1',
        'source': 'hires',
    },
    {
        'name': 'Mistral-7B-v0.3',
        'path': '/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json',
        'gqa': 'GQA 4:1',
        'source': 'hires',
    },
    {
        'name': 'Qwen2.5-7B',
        'path': '/root/ratekv/hires_profiles.json',
        'gqa': 'GQA 7:1',
        'source': 'hires',
    },
    {
        'name': 'Yi-1.5-9B',
        'path': '/root/ratekv/yi15_hires_bf16_2bitonly_profiles.json',
        'gqa': 'GQA 8:1',
        'source': 'hires',
    },
]


def load_profiles(path):
    with open(path) as f:
        data = json.load(f)
    profiles = data.get('profiles', data)
    layer_keys = sorted([k for k in profiles if k.isdigit()], key=int)
    n_layers = len(layer_keys)
    n_heads = len(profiles[layer_keys[0]])
    delta_2bit = np.zeros((n_layers, n_heads))
    for li in range(n_layers):
        for hi in range(n_heads):
            delta_2bit[li, hi] = profiles[str(li)][str(hi)]['quantization']['2']
    return delta_2bit, n_layers, n_heads


def find_top_heads(delta, n=3):
    flat = delta.flatten()
    top_idx = np.argsort(flat)[-n:][::-1]
    results = []
    for idx in top_idx:
        li, hi = divmod(idx, delta.shape[1])
        results.append((li, hi, delta[li, hi]))
    return results


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    deltas = []
    infos = []
    for m in MODELS:
        d, nl, nh = load_profiles(m['path'])
        deltas.append(d)
        infos.append((m['name'], nl, nh, m['gqa'], m['source']))

    width_ratios = [info[2] for info in infos]
    vmin, vmax = 0.005, 16

    fig, axes = plt.subplots(1, 5, figsize=(18, 5.8),
                              gridspec_kw={'width_ratios': width_ratios, 'wspace': 0.12})

    norm = LogNorm(vmin=vmin, vmax=vmax)

    for idx, (ax, delta, (name, nl, nh, gqa, source)) in enumerate(zip(axes, deltas, infos)):
        plot_data = np.clip(delta, vmin, None)
        im = ax.imshow(plot_data, aspect='auto', origin='lower',
                       cmap='YlOrRd', norm=norm, interpolation='nearest')

        ax.set_title(f'{name}\n({gqa}, {nl}L×{nh}H)', fontsize=10.5, pad=8)
        ax.set_xlabel('KV Head')
        if idx == 0:
            ax.set_ylabel('Layer')
        else:
            ax.tick_params(axis='y', labelleft=False)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=8))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        tops = find_top_heads(delta, n=1)
        li, hi, val = tops[0]
        if val > 0.5:
            ax.plot(hi, li, 'x', color='black', markersize=6, markeredgewidth=1.5)
            y_offset = -6 if li > nl * 0.3 else 6
            va = 'top' if y_offset < 0 else 'bottom'
            ax.annotate(f'L{li}H{hi}: {val:.1f}',
                        xy=(hi, li), fontsize=7.5, fontweight='bold',
                        ha='center', va=va,
                        xytext=(0, y_offset), textcoords='offset points',
                        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.8))

    cbar_ax = fig.add_axes([0.92, 0.15, 0.012, 0.7])
    cbar = fig.colorbar(im, cax=cbar_ax)
    cbar.set_label('2-bit Quantization ΔPPL', fontsize=11)

    for fmt in ['pdf', 'png']:
        fig.savefig(os.path.join(OUT_DIR, f'fig1_head_delta_heatmap.{fmt}'),
                    bbox_inches='tight', dpi=300)
    plt.close(fig)

    print('Saved to', OUT_DIR)
    for m, d, (name, nl, nh, gqa, source) in zip(MODELS, deltas, infos):
        tops = find_top_heads(d, n=3)
        top_str = ', '.join([f'L{l}H{h}={v:.2f}' for l, h, v in tops])
        print(f'  {name} ({nl}x{nh}, {source}): {top_str}')


if __name__ == '__main__':
    main()
