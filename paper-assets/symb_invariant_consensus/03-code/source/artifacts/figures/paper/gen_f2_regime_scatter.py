import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

COLORS = {
    'Mistral-7B': '#CC79A7',
    'Qwen2.5-14B': '#0072B2',
    'Qwen2.5-7B': '#56B4E9',
    'Qwen3-14B': '#D55E00',
    'LLaMA-8B': '#009E73',
    'DeepSeek-R1-7B': '#E69F00',
    'QwQ-32B': '#F0E442',
}

# (model, domain, n, sc%, delta_pp, significant)
data = [
    ('Mistral-7B',      'PW-D5',       600, 39.33, -2.83,  True),
    ('Mistral-7B',      'FOLIO-s42',   204, 54.41,  4.90,  True),
    ('Mistral-7B',      'FOLIO-s123',  204, 53.92,  3.43,  True),
    ('Mistral-7B',      'FOLIO-s456',  204, 56.37, -0.49, False),
    ('Qwen2.5-14B',     'StrategyQA',   60, 53.33,  3.33, False),
    ('Mistral-7B',      'LogiQA',      200, 51.00,  0.50, False),
    ('Mistral-7B',      'FOLIO-ICL',   199, 57.79, -3.52, False),
    ('LLaMA-8B',        'FOLIO',       204, 63.24, -2.45, False),
    ('DeepSeek-R1-7B',  'D012',         60, 71.67, -3.33, False),
    ('LLaMA-8B',        'StrategyQA',  200, 72.00,  2.00, False),
    ('Qwen2.5-14B',     'FOLIO-ICL',   199, 74.37,  0.50, False),
    ('Qwen2.5-14B',     'FOLIO+PW',    804, 76.24,  0.25, False),
    ('Qwen2.5-7B',      'FOLIO',       203, 77.34, -0.49, False),
    ('Qwen2.5-14B',     'LogiQA',      200, 78.50, -0.50, False),
    ('Qwen3-14B',       'FOLIO',       204, 83.82,  0.49, False),
    ('QwQ-32B',         'AIME',         22, 72.70,  0.00, False),
    ('Qwen2.5-14B',     'GSM8K',        30, 96.67,  0.00, False),
]

fig, ax = plt.subplots(figsize=(5.5, 4.125))

# --- shaded regime bands ---
ax.axvspan(50, 55, alpha=0.15, color='#4CAF50', zorder=0)
ax.axvspan(60, 100, alpha=0.08, color='#E53935', zorder=0)

# --- reference line at delta=0 ---
ax.axhline(y=0, color='#888', ls='--', lw=0.8, zorder=1)

# --- plot data points ---
for model, domain, n, sc, delta, sig in data:
    color = COLORS[model]
    marker = '*' if sig else 'o'
    size = 180 if sig else 55
    if n >= 100:
        ax.scatter(sc, delta, marker=marker, s=size, c=color,
                   edgecolors='#333', linewidths=0.5, zorder=3)
    else:
        ax.scatter(sc, delta, marker=marker, s=size, c='white',
                   edgecolors=color, linewidths=1.5, zorder=3)

# --- FOLIO seed labels ---
ax.text(55.4, 5.15, 's42', fontsize=7, color='#AA5A87')
ax.text(55.0, 3.65, 's123', fontsize=7, color='#AA5A87')
ax.text(57.3, -0.25, 's456', fontsize=7, color='#AA5A87')

# --- key annotations (positioned to avoid clipping) ---
ax.annotate('Mistral FOLIO +4.90 pp**',
            xy=(54.41, 4.90), xytext=(48, 6.2),
            fontsize=8, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),
            zorder=4)

ax.annotate('Mistral PW −2.83 pp**',
            xy=(39.33, -2.83), xytext=(47, -4.8),
            fontsize=8, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),
            zorder=4)

# --- zone labels (compact, at very top of each band) ---
ax.text(52.5, 7.05, 'Goldilocks', fontsize=7.5, color='#2E7D32',
        ha='center', va='top', fontstyle='italic', fontweight='bold')
ax.text(65, 7.05, 'Type A', fontsize=7.5, color='#C62828',
        ha='center', va='top', fontstyle='italic', fontweight='bold')

# --- degenerate label ---
ax.text(96.67, 0.7, 'degen.', fontsize=7, color='#999',
        fontstyle='italic', ha='center')

# --- axes ---
ax.set_xlabel('Self-Consistency Accuracy (%)')
ax.set_ylabel('SICA $\\Delta$ (pp)')
ax.set_xlim(33, 100)
ax.set_ylim(-5.8, 7.2)

# --- legend ---
model_order = ['Mistral-7B', 'LLaMA-8B', 'Qwen2.5-7B', 'Qwen2.5-14B',
               'Qwen3-14B', 'DeepSeek-R1-7B', 'QwQ-32B']
handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS[m],
                  markeredgecolor='#333', markersize=7, label=m, lw=0)
           for m in model_order]
handles.append(Line2D([0], [0], lw=0, label=''))
handles.extend([
    Line2D([0], [0], marker='*', color='w', markerfacecolor='#999',
           markeredgecolor='#333', markersize=12, label='$p < 0.05$', lw=0),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#999',
           markeredgecolor='#333', markersize=7, label='n.s.', lw=0),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='white',
           markeredgecolor='#999', markersize=7, markeredgewidth=1.5,
           label='$n < 100$', lw=0),
])
ax.legend(handles=handles, loc='upper right', framealpha=0.92, edgecolor='#ccc',
          fontsize=8, handletextpad=0.5, labelspacing=0.35)

plt.tight_layout()

out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper'
fig.savefig(f'{out}/f2_regime_scatter.pdf')
fig.savefig(f'{out}/f2_regime_scatter.png')
plt.close()
print(f'Done. {len(data)} points plotted.')
