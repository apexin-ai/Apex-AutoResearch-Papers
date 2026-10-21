"""Generate fig5_f1_vs_bias: F1 does NOT predict causal bias; topology does.

Standalone script extracted from gen_diagnostic_plots.py with improved aesthetics
for single-column ACL format (~3.25in width).

Output:
  fig5_f1_vs_bias.pdf / .png
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch

# === UNIFIED PAPER COLOR PALETTE ===
COLOR_SAFE = '#154360'      # Deep navy — structural guarantee topologies
COLOR_DANGER = '#922B21'    # Deep crimson — sign-flip topologies

TOPOLOGY_COLORS = {
    'confounding': '#1B4F72',   # Royal navy
    'exposure': '#C0392B',      # Vermillion red
    'mediation': '#117A65',     # Dark emerald teal
    'frontdoor': '#6C3483',     # Deep purple
    'collider': '#1A5276',      # Petrol blue
    'mbias': '#2E4053',         # Dark slate
    'iv': '#922B21',            # Dark crimson
}

COLOR_NEUTRAL = '#1C2833'    # Near-black for text/axes
COLOR_GRID = '#D5D8DC'       # Light gray for grids
COLOR_ACCENT = '#B7950B'     # Burnished gold (sparing use)

# ── Style for single-column ACL figure ──────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.size': 3,
    'ytick.major.size': 3,
})

# Safe vs dangerous classification for marker shapes
SAFE_TOPOS = {'confounding', 'mediation', 'frontdoor', 'collider', 'mbias'}

TOPO_MARKERS = {
    'iv':          'D',   # diamond (danger)
    'exposure':    'D',   # diamond (danger)
    'mediation':   'o',   # circle (safe)
    'frontdoor':   'o',   # circle (safe)
    'confounding': 'o',   # circle (safe)
    'collider':    'o',   # circle (safe)
    'mbias':       'o',   # circle (safe)
}

TOPO_LABELS = {
    'iv':          'IV',
    'exposure':    'Exposure',
    'mediation':   'Mediation',
    'frontdoor':   'Front-door',
    'confounding': 'Confounding',
    'collider':    'Collider',
    'mbias':       'M-bias',
}

# Plot order: high bias first for legend clarity
PLOT_ORDER = ['iv', 'exposure', 'mediation', 'frontdoor', 'confounding', 'collider', 'mbias']

# ── Data loading ────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(SCRIPT_DIR, '../../artifacts/plan006/asv_empirical_results.json')

with open(JSON_PATH) as f:
    data = json.load(f)

# Filter out zero-F1 configs
zero_configs = {(e['model'], e['prompt'])
                for e in data['f1_vs_bias'] if e['macro_f1'] == 0}
entries = [e for e in data['f1_vs_bias']
           if (e['model'], e['prompt']) not in zero_configs and e['macro_f1'] > 0]

# ── Plot ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(1, 1, figsize=(3.3, 2.5))

# Subtle grid
ax.grid(True, alpha=0.08, lw=0.3, color=COLOR_GRID, zorder=0)

# Scatter by topology
for tk in PLOT_ORDER:
    pts = [e for e in entries if e['topology'] == tk]
    if not pts:
        continue
    f1s = np.array([e['macro_f1'] for e in pts])
    biases = np.array([abs(e['bias_pct']) * 100 for e in pts])
    ax.scatter(f1s, biases,
               c=TOPOLOGY_COLORS[tk],
               marker=TOPO_MARKERS[tk],
               s=48,
               alpha=0.9,
               linewidths=0.6,
               edgecolors='white',
               label=TOPO_LABELS[tk],
               zorder=3)

# ── Compute ranges ──────────────────────────────────────────────────────────
f1_all = [e['macro_f1'] for e in entries]
bias_all = [abs(e['bias_pct']) * 100 for e in entries]
f1_min, f1_max = min(f1_all), max(f1_all)
bias_min, bias_max = min(bias_all), max(bias_all)

# ── Annotation: vertical bracket showing full bias range ────────────────────
brace_x = f1_max + 0.005
ax.annotate('', xy=(brace_x, bias_max), xytext=(brace_x, bias_min),
            arrowprops=dict(arrowstyle='<->', color='#555555', lw=0.8,
                            shrinkA=1, shrinkB=1))
bracket_mid = (bias_min + bias_max) / 2
ratio = bias_max / max(bias_min, 0.1)
ax.text(brace_x + 0.003, bracket_mid,
        f'{ratio:.0f}$\\times$\nbias\nrange',
        fontsize=6, color='#555555', va='center', ha='left',
        linespacing=1.05)

# ── Horizontal F1 span annotation near top ──────────────────────────────────
span_y = 44.5
ax.annotate('', xy=(f1_max, span_y), xytext=(f1_min, span_y),
            arrowprops=dict(arrowstyle='<->', color='#888888', lw=0.6,
                            shrinkA=1, shrinkB=1))
ax.text(f1_min + (f1_max - f1_min) / 2, span_y + 0.5,
        f'$\\Delta$F1 = {f1_max - f1_min:.2f}',
        fontsize=6, color='#888888', va='bottom', ha='center')

# ── 10% bias threshold line ─────────────────────────────────────────────────
ax.axhline(10, color=COLOR_DANGER, ls='--', lw=0.7, alpha=0.35, zorder=1)
ax.text(0.645, 10.8, '10% threshold', fontsize=6,
        color=COLOR_DANGER, alpha=0.55, va='bottom', ha='center', fontstyle='italic',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# ── Axis formatting ─────────────────────────────────────────────────────────
ax.set_xlabel('Macro F1', labelpad=4)
ax.set_ylabel('|Relative Bias| (%)', labelpad=4)
ax.set_xlim(f1_min - 0.008, f1_max + 0.022)
ax.set_ylim(0, 47)

# ── Legend: compact 2-column, in the empty center area ──────────────────────
leg = ax.legend(loc='center',
                bbox_to_anchor=(0.44, 0.68),
                frameon=True,
                framealpha=0.93,
                edgecolor='#dddddd',
                handletextpad=0.2,
                labelspacing=0.25,
                columnspacing=0.8,
                borderpad=0.35,
                markerscale=0.7,
                ncol=2)
leg.get_frame().set_linewidth(0.4)

plt.tight_layout(pad=0.3)

# ── Save ────────────────────────────────────────────────────────────────────
out_base = os.path.join(SCRIPT_DIR, 'fig5_f1_vs_bias')
for ext in ['pdf', 'png']:
    fig.savefig(f'{out_base}.{ext}', dpi=300, bbox_inches='tight')
plt.close()

print(f"fig5_f1_vs_bias: {len(entries)} points, F1=[{f1_min:.3f}, {f1_max:.3f}], saved to {out_base}.pdf/.png")
