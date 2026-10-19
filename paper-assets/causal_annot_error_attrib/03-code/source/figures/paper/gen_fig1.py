#!/usr/bin/env python3
"""Figure 1: Seven canonical DAG topologies — hero figure for EMNLP 2026.
Premium academic quality with elegant nodes, refined arrows, and semantic color coding.
Layout: 4 top + 3 bottom (centered). Full-width figure*.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch
from matplotlib.lines import Line2D
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'font.size': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# ── Semantic palette ──
PAL = {
    'obs_fill':    '#FFFFFF',
    'obs_edge':    '#3A3A3A',
    'lat_fill':    '#FAFAFA',
    'lat_edge':    '#999999',
    'mis_fill':    '#0072B2',
    'mis_edge':    '#005A8C',
    'con_fill':    '#0072B2',
    'con_edge':    '#005A8C',
    'arrow':       '#2D2D2D',
    'meas_arrow':  '#5B8BA8',
    'shadow':      '#C0C0C0',
    'panel_bg':    '#F8F9FA',
    'panel_edge':  '#DEE2E6',
    'hl_warm':     '#FFF3E0',
    'hl_warm_e':   '#E0A870',
    'hl_red':      '#FFEBEE',
    'hl_red_e':    '#D09090',
}
SUB_COL = {
    'atten':  '#2E6DA4',
    'sign':   '#D35400',
    'amp':    '#C07A20',
    'mod':    '#666666',
    'immune': '#1B8C5A',
    'fragile':'#C0392B',
}

R = 0.13
SHRINK = R + 0.016


def _node(ax, x, y, label, kind='obs'):
    sdx, sdy = 0.005, -0.008
    shadow_a = 0.07

    if kind == 'con':
        sz = R * 1.6
        ax.add_patch(FancyBboxPatch(
            (x - sz/2 + sdx, y - sz/2 + sdy), sz, sz,
            boxstyle='round,pad=0.018', fc=PAL['shadow'], ec='none',
            alpha=shadow_a, zorder=2))
        ax.add_patch(FancyBboxPatch(
            (x - sz/2, y - sz/2), sz, sz,
            boxstyle='round,pad=0.018', fc=PAL['con_fill'], ec=PAL['con_edge'],
            lw=1.6, zorder=3))
        ax.text(x, y, label, ha='center', va='center',
                fontsize=17, color='white', fontweight='bold', zorder=4,
                fontfamily='DejaVu Sans')
        return

    cfg = {
        'obs': (PAL['obs_fill'], PAL['obs_edge'], '-',  1.3, '#2A2A2A', 'normal'),
        'lat': (PAL['lat_fill'], PAL['lat_edge'], '--', 1.1, '#555555', 'normal'),
        'mis': (PAL['mis_fill'], PAL['mis_edge'], '-',  1.6, '#FFFFFF', 'bold'),
    }
    fc, ec, ls, lw, tc, fw = cfg[kind]

    if kind == 'mis':
        ax.add_patch(Circle((x, y), R + 0.02,
                            fc=PAL['mis_fill'], ec='none', alpha=0.10, zorder=1.5))
    ax.add_patch(Circle((x + sdx, y + sdy), R + 0.004,
                        fc=PAL['shadow'], ec='none', alpha=shadow_a, zorder=2))
    ax.add_patch(Circle((x, y), R, fc=fc, ec=ec, lw=lw, ls=ls, zorder=3))
    ax.text(x, y, label, ha='center', va='center',
            fontsize=17, color=tc, fontweight=fw, zorder=4,
            fontfamily='DejaVu Sans')


def _edge(ax, x1, y1, x2, y2, kind='causal', rad=0):
    dx, dy = x2 - x1, y2 - y1
    d = np.sqrt(dx**2 + dy**2)
    if d < 1e-6:
        return
    is_c = (kind == 'causal')
    ax.add_patch(FancyArrowPatch(
        (x1 + SHRINK * dx/d, y1 + SHRINK * dy/d),
        (x2 - SHRINK * dx/d, y2 - SHRINK * dy/d),
        arrowstyle='-|>',
        mutation_scale=13 if is_c else 10,
        color=PAL['arrow'] if is_c else PAL['meas_arrow'],
        lw=1.3 if is_c else 0.9,
        ls='-' if is_c else (0, (3.5, 3)),
        connectionstyle=f'arc3,rad={rad}',
        zorder=1))


def _panel_bg(ax, color, edge_color, lw=0.8):
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    pad = 0.015
    ax.add_patch(FancyBboxPatch(
        (xmin + pad, ymin + pad), xmax - xmin - 2*pad, ymax - ymin - 2*pad,
        boxstyle='round,pad=0.05',
        fc=color, ec=edge_color, lw=lw, alpha=0.40, zorder=-1))


def _title(ax, title, subtitle, sub_color, highlight=None):
    if highlight == 'warm':
        _panel_bg(ax, PAL['hl_warm'], PAL['hl_warm_e'], lw=0.8)
    elif highlight == 'danger':
        _panel_bg(ax, PAL['hl_red'], PAL['hl_red_e'], lw=0.8)
    else:
        _panel_bg(ax, PAL['panel_bg'], PAL['panel_edge'], lw=0.6)

    ax.text(0.5, 1.10, title, ha='center', va='bottom',
            fontsize=17, fontweight='bold', color='#1A1A1A',
            transform=ax.transAxes)
    ax.text(0.5, 1.00, subtitle, ha='center', va='bottom',
            fontsize=12, fontstyle='italic', color=sub_color,
            transform=ax.transAxes)


# ═══════════════════════════════════════════════════════════
#  Layout: 4+3 grid, generous spacing
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(16, 8.5))

pw = 0.195
ph = 0.385
hgap = 0.035
vgap = 0.085
top_margin = 0.030

top_y = 1 - top_margin - ph
top_total = 4*pw + 3*hgap
top_x0 = (1 - top_total) / 2

bot_y = top_y - vgap - ph
bot_total = 3*pw + 2*hgap
bot_x0 = (1 - bot_total) / 2

panel_w_in = pw * 16
panel_h_in = ph * 9
phys_ratio = panel_w_in / panel_h_in
ylim_span = 1.35
xlim_span = ylim_span * phys_ratio
xc, yc = 0.50, 0.30
XL = (xc - xlim_span/2, xc + xlim_span/2)
YL = (yc - ylim_span/2, yc + ylim_span/2)

panels = []
for i in range(4):
    ax = fig.add_axes([top_x0 + i*(pw + hgap), top_y, pw, ph])
    ax.set_xlim(*XL); ax.set_ylim(*YL)
    ax.set_aspect('equal')
    ax.axis('off')
    panels.append(ax)
for i in range(3):
    ax = fig.add_axes([bot_x0 + i*(pw + hgap), bot_y, pw, ph])
    ax.set_xlim(*XL); ax.set_ylim(*YL)
    ax.set_aspect('equal')
    ax.axis('off')
    panels.append(ax)

# ═══════════════════════════════════════════════════════════
#  DAGs — precise node positions for clarity
# ═══════════════════════════════════════════════════════════

# (a) Confounding: A→X, A→Y, X→Y, A→A*
ax = panels[0]
_title(ax, '(a) Confounding', 'Attenuation (toward OVB)', SUB_COL['atten'])
_node(ax, 0.22, 0.72, 'A', 'lat')
_node(ax, 0.78, 0.72, 'A*', 'mis')
_node(ax, 0.10, 0.05, 'X', 'obs')
_node(ax, 0.90, 0.05, 'Y', 'obs')
_edge(ax, 0.22, 0.72, 0.78, 0.72, 'meas')
_edge(ax, 0.22, 0.72, 0.10, 0.05)
_edge(ax, 0.22, 0.72, 0.90, 0.05, rad=0.25)
_edge(ax, 0.10, 0.05, 0.90, 0.05)

# (b) Exposure: A→A*, A→Y — HIGHLIGHTED warm
ax = panels[1]
_title(ax, '(b) Exposure', 'Sign reversal (83.4%)', SUB_COL['sign'], highlight='warm')
_node(ax, 0.20, 0.55, 'A', 'lat')
_node(ax, 0.80, 0.55, 'A*', 'mis')
_node(ax, 0.50, 0.00, 'Y', 'obs')
_edge(ax, 0.20, 0.55, 0.80, 0.55, 'meas')
_edge(ax, 0.20, 0.55, 0.50, 0.00)

# (c) Mediation: X→A, A→Y, X→Y (direct), A→A*
ax = panels[2]
_title(ax, '(c) Mediation', 'Amplification', SUB_COL['amp'])
_node(ax, 0.50, 0.68, 'A', 'lat')
_node(ax, 0.90, 0.68, 'A*', 'mis')
_node(ax, 0.10, 0.08, 'X', 'obs')
_node(ax, 0.90, 0.08, 'Y', 'obs')
_edge(ax, 0.50, 0.68, 0.90, 0.68, 'meas')
_edge(ax, 0.10, 0.08, 0.50, 0.68)
_edge(ax, 0.50, 0.68, 0.90, 0.08)
_edge(ax, 0.10, 0.08, 0.90, 0.08)

# (d) Collider: X→A, Y→A, A→A* (conditioned square)
ax = panels[3]
_title(ax, '(d) Collider', 'Attenuation (no sign flip)', SUB_COL['atten'])
_node(ax, 0.15, 0.72, 'X', 'obs')
_node(ax, 0.85, 0.72, 'Y', 'obs')
_node(ax, 0.50, 0.30, 'A', 'lat')
_node(ax, 0.50, -0.10, 'A*', 'con')
_edge(ax, 0.15, 0.72, 0.50, 0.30)
_edge(ax, 0.85, 0.72, 0.50, 0.30)
_edge(ax, 0.50, 0.30, 0.50, -0.10, 'meas')

# (e) Front-door: X→A, A→Y, U→X, U→Y, A→A*
ax = panels[4]
_title(ax, '(e) Front-door', 'Moderate sensitivity', SUB_COL['mod'])
_node(ax, 0.50, 0.72, 'A', 'lat')
_node(ax, 0.90, 0.72, 'A*', 'mis')
_node(ax, 0.10, 0.22, 'X', 'obs')
_node(ax, 0.90, 0.22, 'Y', 'obs')
_node(ax, 0.50, -0.14, 'U', 'lat')
_edge(ax, 0.50, 0.72, 0.90, 0.72, 'meas')
_edge(ax, 0.10, 0.22, 0.50, 0.72)          # X→A
_edge(ax, 0.50, 0.72, 0.90, 0.22)          # A→Y
_edge(ax, 0.50, -0.14, 0.10, 0.22)         # U→X
_edge(ax, 0.50, -0.14, 0.90, 0.22)         # U→Y

# (f) M-bias: U1→X, U1→A, U2→A, U2→Y, X→Y, A→A*
ax = panels[5]
_title(ax, '(f) M-bias', 'Immune', SUB_COL['immune'])
_node(ax, 0.10, 0.75, u'U₁', 'lat')
_node(ax, 0.90, 0.75, u'U₂', 'lat')
_node(ax, 0.50, 0.45, 'A', 'lat')
_node(ax, 0.10, 0.06, 'X', 'obs')
_node(ax, 0.90, 0.06, 'Y', 'obs')
_node(ax, 0.50, -0.18, 'A*', 'mis')
_edge(ax, 0.10, 0.75, 0.10, 0.06)
_edge(ax, 0.10, 0.75, 0.50, 0.45)
_edge(ax, 0.90, 0.75, 0.50, 0.45)
_edge(ax, 0.90, 0.75, 0.90, 0.06)
_edge(ax, 0.10, 0.06, 0.90, 0.06)
_edge(ax, 0.50, 0.45, 0.50, -0.18, 'meas')

# (g) IV (Instrument): A→X, X→Y, U→X, U→Y, A→A* — HIGHLIGHTED danger
ax = panels[6]
_title(ax, '(g) IV (Instrument)', 'Fragile (Wald amplification)', SUB_COL['fragile'], highlight='danger')
_node(ax, 0.22, 0.72, 'A', 'lat')
_node(ax, 0.78, 0.72, 'A*', 'mis')
_node(ax, 0.10, 0.18, 'X', 'obs')
_node(ax, 0.90, 0.18, 'Y', 'obs')
_node(ax, 0.50, -0.14, 'U', 'lat')
_edge(ax, 0.22, 0.72, 0.78, 0.72, 'meas')
_edge(ax, 0.22, 0.72, 0.10, 0.18)          # A→X
_edge(ax, 0.10, 0.18, 0.90, 0.18)          # X→Y
_edge(ax, 0.50, -0.14, 0.10, 0.18)         # U→X
_edge(ax, 0.50, -0.14, 0.90, 0.18)         # U→Y

# ═══════════════════════════════════════════════════════════
#  Legend
# ═══════════════════════════════════════════════════════════
handles = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor=PAL['obs_fill'],
           markeredgecolor=PAL['obs_edge'], markersize=8, markeredgewidth=1.2,
           lw=0, label='Observed'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=PAL['lat_fill'],
           markeredgecolor=PAL['lat_edge'], markersize=8, markeredgewidth=1.0,
           lw=0, label='Latent'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=PAL['mis_fill'],
           markeredgecolor=PAL['mis_edge'], markersize=8, markeredgewidth=1.2,
           lw=0, label='Misclassified (A*)'),
    Line2D([0],[0], marker='s', color='w', markerfacecolor=PAL['con_fill'],
           markeredgecolor=PAL['con_edge'], markersize=7, markeredgewidth=1.2,
           lw=0, label='Conditioned on (A*)'),
    Line2D([0],[0], color=PAL['arrow'], lw=1.4, marker='>',
           markersize=5, label='Causal'),
    Line2D([0],[0], color=PAL['meas_arrow'], lw=1.0, ls='--',
           marker='>', markersize=4, label='Measurement'),
]
fig.legend(handles=handles, loc='lower center', ncol=6, fontsize=11,
           frameon=False, handlelength=1.8, columnspacing=1.2,
           handletextpad=0.4, bbox_to_anchor=(0.5, 0.01))

# ═══════════════════════════════════════════════════════════
#  Save
# ═══════════════════════════════════════════════════════════
out_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(out_dir, 'fig1_dag_taxonomy.pdf')
png_path = os.path.join(out_dir, 'fig1_dag_taxonomy.png')
fig.savefig(pdf_path, format='pdf')
fig.savefig(png_path, format='png')
plt.close()
print(f'PDF: {pdf_path}')
print(f'PNG: {png_path}')
for p in [pdf_path, png_path]:
    print(f'  {os.path.basename(p)}: {os.path.getsize(p):,} bytes')
