#!/usr/bin/env python3
"""Fig 3: Layer-wise Probe Accuracy — restyled with unified color system."""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ── Color system ─────────────────────────────────────────────────────
NAVY      = '#1B2838'
SLATE     = '#3D5A80'
TEAL      = '#5BA4B5'
CORAL     = '#E07A5F'
EN_BLUE   = '#4A90D9'
ZH_RED    = '#E07A5F'
CROSS_TEAL= '#5BA4B5'

CROSS_TEAL_DARK = '#3D8A9A'
DIR_STYLE = {
    'en_en': dict(color=EN_BLUE, ls='-',  lw=1.8, label=r'EN$\rightarrow$EN'),
    'zh_zh': dict(color=ZH_RED,  ls='-',  lw=1.8, label=r'ZH$\rightarrow$ZH'),
    'en_zh': dict(color=CROSS_TEAL, ls=(0, (5, 3)), lw=1.3, label=r'EN$\rightarrow$ZH'),
    'zh_en': dict(color=CROSS_TEAL_DARK, ls=(0, (3, 1, 1, 1)), lw=1.3, label=r'ZH$\rightarrow$EN'),
}
PEAK_MARKERS = {'en_en': 'o', 'zh_zh': 's', 'en_zh': '^', 'zh_en': 'D'}
CURVE_MARKERS = {'en_en': 'o', 'zh_zh': 's', 'en_zh': '^', 'zh_en': 'D'}
CURVE_MARK_EVERY = 4
MLP_GRAY = '#C0C0C0'

# ── Paths ────────────────────────────────────────────────────────────
DATA_PATH = Path(__file__).resolve().parent.parent.parent / 'artifacts' / 'layerwise_probe_curves.json'
OUT_DIR   = Path(__file__).resolve().parent
OUT_DIR.mkdir(parents=True, exist_ok=True)

with open(DATA_PATH) as f:
    data = json.load(f)

# ── Helpers ──────────────────────────────────────────────────────────
def get_curve(section, direction):
    d = section['directions'][direction]
    layers = sorted(d.keys(), key=int)
    return np.array([int(l) for l in layers]), np.array([d[l] for l in layers])

def get_ci(ci_section, direction):
    d = ci_section['directions'][direction]
    layers = sorted(d.keys(), key=int)
    lo = np.array([d[l]['ci_lower'] for l in layers])
    hi = np.array([d[l]['ci_upper'] for l in layers])
    return np.array([int(l) for l in layers]), lo, hi

# ── Global style ─────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'axes.facecolor': '#FFFFFF',
    'figure.facecolor': '#FFFFFF',
    'axes.edgecolor': SLATE,
    'axes.linewidth': 0.8,
    'xtick.color': SLATE,
    'ytick.color': SLATE,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'axes.grid': False,
})

# ── Models to plot ───────────────────────────────────────────────────
models = []
if 'llama31' in data:
    models.append(('(a) Llama-3.1-8B', 'llama31', 'llama31_mlp', None, 32))
if 'qwen3' in data:
    models.append(('(b) Qwen3-8B', 'qwen3', 'qwen3_mlp', 'qwen3_bootstrap_ci', 36))
if 'gemma2' in data:
    models.append(('(c) Gemma-2-9B', 'gemma2', None, 'gemma2_bootstrap_ci', 42))

n_panels = len(models)
fig, axes = plt.subplots(1, n_panels, figsize=(5.5 * n_panels, 4.2), sharey=True)
if n_panels == 1:
    axes = [axes]

for ax, (title, res_key, mlp_key, ci_key, n_layers) in zip(axes, models):
    directions = ['en_en', 'zh_zh', 'en_zh', 'zh_en']

    # CI bands (if available)
    if ci_key and ci_key in data:
        for d in directions:
            s = DIR_STYLE[d]
            cx, clo, chi = get_ci(data[ci_key], d)
            ax.fill_between(cx, clo, chi, color=s['color'], alpha=0.10, zorder=0)

    # MLP output (de-emphasized, light gray dashed)
    if mlp_key and mlp_key in data:
        for d in directions:
            mx, my = get_curve(data[mlp_key], d)
            ax.plot(mx, my, color=MLP_GRAY, linewidth=0.8, linestyle='--',
                    alpha=0.5, zorder=1)

    # Main residual stream curves
    for d in directions:
        s = DIR_STYLE[d]
        lx, ly = get_curve(data[res_key], d)
        ax.plot(lx, ly, color=s['color'], linewidth=s['lw'], linestyle=s['ls'],
                marker=CURVE_MARKERS[d], markersize=3.5, markevery=CURVE_MARK_EVERY,
                markeredgecolor='white', markeredgewidth=0.4,
                zorder=3, alpha=0.9)

    # Peak markers + vertical lines
    for d in directions:
        s = DIR_STYLE[d]
        pk = data[res_key]['peaks'][d]
        pl, pa = pk['peak_layer'], pk['peak_acc']
        ax.plot(pl, pa, marker=PEAK_MARKERS[d], markersize=9,
                color=s['color'], zorder=6,
                markeredgecolor='white', markeredgewidth=1.0)
        ax.axvline(x=pl, ymin=0, ymax=0.03, color=s['color'],
                   linewidth=0.8, alpha=0.5, zorder=1,
                   clip_on=False)

    # Styling
    ax.set_title(title, fontsize=12, fontweight='bold', pad=8, color=NAVY)
    ax.set_xlabel('Layer Index', fontsize=10.5, color=SLATE)
    ax.set_xlim(-0.5, n_layers - 0.5)
    ax.set_ylim(0.44, 0.82)
    ax.tick_params(labelsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Chance-level reference
    ax.axhline(y=0.5, color='#CCCCCC', linewidth=0.7, linestyle=':', zorder=0)

axes[0].set_ylabel('Balanced Accuracy', fontsize=10.5, color=SLATE)

# ── Legend ────────────────────────────────────────────────────────────
from matplotlib.lines import Line2D
handles = []
for d in ['en_en', 'zh_zh', 'en_zh', 'zh_en']:
    s = DIR_STYLE[d]
    handles.append(Line2D([], [], color=s['color'], lw=s['lw'], ls=s['ls'],
                          marker=PEAK_MARKERS[d], markersize=6,
                          markeredgecolor='white', markeredgewidth=0.6,
                          label=s['label']))
handles.append(Line2D([], [], color=MLP_GRAY, lw=0.8, ls='--', alpha=0.5,
                       label='MLP output'))
handles.append(Line2D([], [], color='#CCCCCC', lw=0.7, ls=':',
                       label='Chance'))

fig.legend(handles=handles, loc='lower center', ncol=6, fontsize=8.5,
           frameon=False, bbox_to_anchor=(0.5, -0.06),
           columnspacing=1.8, handletextpad=0.5)

plt.tight_layout(rect=[0, 0.05, 1, 1])

# ── Save ─────────────────────────────────────────────────────────────
fig.savefig(OUT_DIR / 'fig3_layerwise.pdf', bbox_inches='tight', dpi=300)
fig.savefig(OUT_DIR / 'fig3_layerwise.png', bbox_inches='tight', dpi=300)
print(f'Saved: {OUT_DIR / "fig3_layerwise.png"}')
print(f'Saved: {OUT_DIR / "fig3_layerwise.pdf"}')
plt.close()
