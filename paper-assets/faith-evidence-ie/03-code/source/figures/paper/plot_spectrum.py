import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 10,
    'axes.labelsize': 11,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

COLORS = {
    'baseline':  '#5B9BD5',
    'treatment': '#009E73',
    'collapse':  '#D55E00',
    'safe':      '#E8A838',
    'neutral':   '#B0B0B0',
    'dpo':       '#CC79A7',
}

fig, ax = plt.subplots(figsize=(5.5, 3.8), dpi=300)

pts = {
    'SFT':        (0.4439, 0.7961, 'o', COLORS['neutral'],  90),
    'RSFT':       (0.4580, 0.8096, '*', COLORS['safe'],     200),
    'GRPO_bf16':  (0.4549, 0.8086, '^', COLORS['treatment'], 90),
    'DPO_1ep':    (0.3337, 0.8090, 's', COLORS['dpo'],      80),
    'DPO_3ep':    (0.3145, 0.8484, 's', COLORS['dpo'],      80),
    'GRPO_qlora': (0.0138, 0.8504, 'X', COLORS['collapse'], 120),
}

ax.axhspan(0.785, 0.800, color='#f0f0f0', alpha=0.5, zorder=0)
ax.text(0.54, 0.7912, 'SFT baseline', fontsize=7, color='#aaaaaa',
        ha='right', va='center', fontstyle='italic')

ax.axvspan(-0.02, 0.15, color='#FFF5F5', alpha=0.4, zorder=0)
ax.axvspan(0.40, 0.55, color='#F5FFF5', alpha=0.4, zorder=0)

for k, (x, y, m, c, s) in pts.items():
    ax.scatter(x, y, marker=m, c=c, s=s, edgecolors=c, linewidths=0.8,
              zorder=5, alpha=0.92)

ax.annotate('', xy=(0.3145, 0.8484), xytext=(0.3337, 0.8090),
            arrowprops=dict(arrowstyle='->', color=COLORS['dpo'], lw=1.3,
                            linestyle='--', mutation_scale=10))

txt = ax.text(0.258, 0.830, 'gradual\ndecay', fontsize=7.5, color=COLORS['dpo'],
              ha='center', va='center', fontstyle='italic', linespacing=0.85)
txt.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

offsets = {
    'SFT':       (-6, -11, 'right'),
    'RSFT':      (7, 6, 'left'),
    'GRPO_bf16': (-6, 7, 'right'),
    'DPO_1ep':   (7, -9, 'left'),
    'DPO_3ep':   (7, 4, 'left'),
}
labels = {
    'SFT': ('SFT', COLORS['neutral']),
    'RSFT': ('RSFT CED', COLORS['safe']),
    'GRPO_bf16': ('GRPO bf16', COLORS['treatment']),
    'DPO_1ep': ('DPO 1ep', COLORS['dpo']),
    'DPO_3ep': ('DPO 3ep', COLORS['dpo']),
}
for k, (label, color) in labels.items():
    x, y = pts[k][0], pts[k][1]
    ox, oy, ha = offsets[k]
    t = ax.annotate(label, (x, y), xytext=(ox, oy),
                    textcoords='offset points', fontsize=7.5, ha=ha,
                    color=color, fontweight='bold')
    t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

t = ax.annotate('catastrophic\ncollapse', xy=(0.0138, 0.8504),
                xytext=(0.09, 0.836), fontsize=8, color=COLORS['collapse'],
                fontweight='bold', ha='center', va='top', linespacing=0.85,
                arrowprops=dict(arrowstyle='->', color=COLORS['collapse'],
                                lw=1.0, mutation_scale=9))
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax.axhline(y=0.7961, color=COLORS['neutral'], linestyle=':', linewidth=0.5,
           alpha=0.25, zorder=1)

handles = [
    plt.Line2D([0], [0], marker='o', color='w', mfc=COLORS['neutral'],
               mec=COLORS['neutral'], ms=6.5, lw=0, label='SFT'),
    plt.Line2D([0], [0], marker='*', color='w', mfc=COLORS['safe'],
               mec=COLORS['safe'], ms=9, lw=0, label='RSFT CED (3-seed)'),
    plt.Line2D([0], [0], marker='^', color='w', mfc=COLORS['treatment'],
               mec=COLORS['treatment'], ms=6.5, lw=0, label='GRPO bf16'),
    plt.Line2D([0], [0], marker='X', color='w', mfc=COLORS['collapse'],
               mec=COLORS['collapse'], ms=6.5, lw=0, label='GRPO QLoRA (4-bit)'),
    plt.Line2D([0], [0], marker='s', color='w', mfc=COLORS['dpo'],
               mec=COLORS['dpo'], ms=6, lw=0, label='DPO (1ep → 3ep)'),
]
ax.legend(handles=handles, loc='lower left', fontsize=7, framealpha=0.95,
          edgecolor='#e0e0e0', borderpad=0.6, handletextpad=0.5)

ax.set_xlabel('Rel-F1', fontsize=11)
ax.set_ylabel('Evi-F1 (TP)', fontsize=11)
ax.set_xlim(-0.02, 0.55)
ax.set_ylim(0.785, 0.858)
ax.grid(True, alpha=0.08, color='#999999', linestyle='-', linewidth=0.3)

fig.tight_layout()
out_dir = os.path.dirname(os.path.abspath(__file__))
for ext in ('pdf', 'png'):
    fig.savefig(f'{out_dir}/fig_spectrum.{ext}', bbox_inches='tight', dpi=300)
plt.close()
print('Saved fig_spectrum.pdf and .png')
