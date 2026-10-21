#!/usr/bin/env python3
"""Figure 1: Seven canonical DAG topologies — hero figure for EMNLP 2026.
Premium academic quality with elegant nodes, refined arrows, and semantic color coding."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch, Arc
from matplotlib.lines import Line2D
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'font.size': 16,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# ── Refined semantic palette ──
PAL = {
    'obs_fill':    '#FFFFFF',
    'obs_edge':    '#3A3A3A',
    'lat_fill':    '#F7F7F7',
    'lat_edge':    '#9A9A9A',
    'mis_fill':    '#0072B2',
    'mis_edge':    '#004F7F',
    'con_fill':    '#0072B2',
    'con_edge':    '#004F7F',
    'arrow':       '#2D2D2D',
    'meas_arrow':  '#7B94A8',
    'shadow':      '#B0B0B0',
    'panel_bg':    '#FAFBFC',
    'panel_edge':  '#E8ECF0',
    'hl_bg':       '#FFF0E0',
    'hl_edge':     '#E0A870',
    'hl_bg2':      '#FFECEC',
    'hl_edge2':    '#E09090',
}
SUB_COL = {
    'atten':  '#3A7CC0',
    'sign':   '#D55E00',
    'amp':    '#C07A20',
    'mod':    '#5A5A5A',
    'immune': '#009E73',
    'fragile':'#D55E00',
}

R = 0.13
SHRINK = R + 0.018

# ═══════════════════════════════════════════════════════════
#  Primitives
# ═══════════════════════════════════════════════════════════

def _node(ax, x, y, label, kind='obs'):
    sdx, sdy = 0.006, -0.010
    shadow_alpha = 0.12

    if kind == 'con':
        sz = R * 1.55
        ax.add_patch(FancyBboxPatch(
            (x - sz/2 + sdx, y - sz/2 + sdy), sz, sz,
            boxstyle='round,pad=0.02', fc=PAL['shadow'], ec='none',
            alpha=shadow_alpha, zorder=2))
        ax.add_patch(FancyBboxPatch(
            (x - sz/2, y - sz/2), sz, sz,
            boxstyle='round,pad=0.02', fc=PAL['con_fill'], ec=PAL['con_edge'],
            lw=1.8, zorder=3))
        ax.text(x, y, label, ha='center', va='center',
                fontsize=19, color='white', fontweight='bold', zorder=4,
                fontfamily='DejaVu Sans')
        return

    cfg = {
        'obs': (PAL['obs_fill'], PAL['obs_edge'], '-',  1.5, '#2A2A2A', 'normal'),
        'lat': (PAL['lat_fill'], PAL['lat_edge'], '--', 1.2, '#555555', 'normal'),
        'mis': (PAL['mis_fill'], PAL['mis_edge'], '-',  2.0, '#FFFFFF', 'bold'),
    }
    fc, ec, ls, lw, tc, fw = cfg[kind]

    # Glow for misclassified nodes
    if kind == 'mis':
        ax.add_patch(Circle((x, y), R + 0.025,
                            fc=PAL['mis_fill'], ec='none', alpha=0.12, zorder=1.5))
    # Subtle shadow
    ax.add_patch(Circle((x + sdx, y + sdy), R + 0.005,
                        fc=PAL['shadow'], ec='none', alpha=shadow_alpha, zorder=2))
    # Main circle
    ax.add_patch(Circle((x, y), R, fc=fc, ec=ec, lw=lw, ls=ls, zorder=3))
    # Label
    ax.text(x, y, label, ha='center', va='center',
            fontsize=19, color=tc, fontweight=fw, zorder=4,
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
        mutation_scale=15 if is_c else 12,
        color=PAL['arrow'] if is_c else PAL['meas_arrow'],
        lw=1.5 if is_c else 1.0,
        ls='-' if is_c else (0, (3.5, 3)),
        connectionstyle=f'arc3,rad={rad}',
        zorder=1))


def _panel_bg(ax, color, edge_color, lw=1.0):
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    pad = 0.02
    ax.add_patch(FancyBboxPatch(
        (xmin + pad, ymin + pad), xmax - xmin - 2*pad, ymax - ymin - 2*pad,
        boxstyle='round,pad=0.06',
        fc=color, ec=edge_color, lw=lw, alpha=0.60, zorder=-1))


def _title(ax, title, subtitle, sub_color, highlight=None):
    if highlight == 'warm':
        _panel_bg(ax, PAL['hl_bg'], PAL['hl_edge'], lw=1.5)
    elif highlight == 'danger':
        _panel_bg(ax, PAL['hl_bg2'], PAL['hl_edge2'], lw=1.5)
    else:
        _panel_bg(ax, PAL['panel_bg'], PAL['panel_edge'], lw=0.8)

    ax.text(0.5, 1.14, title, ha='center', va='bottom',
            fontsize=23, fontweight='bold', color='#1A1A1A',
            transform=ax.transAxes)
    ax.text(0.5, 1.03, subtitle, ha='center', va='bottom',
            fontsize=18, fontstyle='italic', color=sub_color,
            transform=ax.transAxes)


# ═══════════════════════════════════════════════════════════
#  Layout
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(14, 7.8))

pw = 0.195
ph = 0.380
hgap = 0.038
vgap = 0.070
top_margin = 0.045

top_y = 1 - top_margin - ph
top_total = 4*pw + 3*hgap
top_x0 = (1 - top_total) / 2

bot_y = top_y - vgap - ph
bot_total = 3*pw + 2*hgap
bot_x0 = (1 - bot_total) / 2

panel_w_in = pw * 14
panel_h_in = ph * 7.8
phys_ratio = panel_w_in / panel_h_in
ylim_span = 1.45
xlim_span = ylim_span * phys_ratio
xc, yc = 0.50, 0.28
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
#  DAGs
# ═══════════════════════════════════════════════════════════

# (a) Confounding
ax = panels[0]
_title(ax, '(a) Confounding', 'Attenuation (toward OVB)', SUB_COL['atten'])
_node(ax, 0.22, 0.70, 'A', 'lat')
_node(ax, 0.78, 0.70, 'A*', 'mis')
_node(ax, 0.10, 0.08, 'X', 'obs')
_node(ax, 0.90, 0.08, 'Y', 'obs')
_edge(ax, 0.22, 0.70, 0.78, 0.70, 'meas')
_edge(ax, 0.22, 0.70, 0.10, 0.08)
_edge(ax, 0.22, 0.70, 0.90, 0.08)
_edge(ax, 0.10, 0.08, 0.90, 0.08)

# (b) Exposure — highlighted warm (sign reversal = dangerous)
ax = panels[1]
_title(ax, '(b) Exposure', 'Sign reversal (83.4%)', SUB_COL['sign'], highlight='warm')
_node(ax, 0.22, 0.60, 'A', 'lat')
_node(ax, 0.78, 0.60, 'A*', 'mis')
_node(ax, 0.50, 0.00, 'Y', 'obs')
_edge(ax, 0.22, 0.60, 0.78, 0.60, 'meas')
_edge(ax, 0.22, 0.60, 0.50, 0.00)

# (c) Mediation
ax = panels[2]
_title(ax, '(c) Mediation', 'Amplification', SUB_COL['amp'])
_node(ax, 0.50, 0.66, 'A', 'lat')
_node(ax, 0.90, 0.66, 'A*', 'mis')
_node(ax, 0.10, 0.10, 'X', 'obs')
_node(ax, 0.90, 0.10, 'Y', 'obs')
_edge(ax, 0.50, 0.66, 0.90, 0.66, 'meas')
_edge(ax, 0.10, 0.10, 0.50, 0.66)
_edge(ax, 0.50, 0.66, 0.90, 0.10)

# (d) Collider
ax = panels[3]
_title(ax, '(d) Collider', 'Attenuation (no sign flip)', SUB_COL['atten'])
_node(ax, 0.15, 0.72, 'X', 'obs')
_node(ax, 0.85, 0.72, 'Y', 'obs')
_node(ax, 0.50, 0.38, 'A', 'lat')
_node(ax, 0.50, 0.00, 'A*', 'con')
_edge(ax, 0.15, 0.72, 0.50, 0.38)
_edge(ax, 0.85, 0.72, 0.50, 0.38)
_edge(ax, 0.50, 0.38, 0.50, 0.00, 'meas')

# (e) Front-door
ax = panels[4]
_title(ax, '(e) Front-door', 'Moderate sensitivity', SUB_COL['mod'])
_node(ax, 0.22, 0.70, 'A', 'lat')
_node(ax, 0.78, 0.70, 'A*', 'mis')
_node(ax, 0.05, 0.16, 'X', 'obs')
_node(ax, 0.95, 0.16, 'Y', 'obs')
_node(ax, 0.50, -0.16, 'U', 'lat')
_edge(ax, 0.22, 0.70, 0.78, 0.70, 'meas')
_edge(ax, 0.22, 0.70, 0.05, 0.16)
_edge(ax, 0.05, 0.16, 0.95, 0.16)
_edge(ax, 0.50, -0.16, 0.22, 0.70)
_edge(ax, 0.50, -0.16, 0.95, 0.16)

# (f) M-bias
ax = panels[5]
_title(ax, '(f) M-bias', 'Immune', SUB_COL['immune'])
_node(ax, 0.10, 0.75, 'U₁', 'lat')
_node(ax, 0.90, 0.75, 'U₂', 'lat')
_node(ax, 0.50, 0.45, 'A', 'lat')
_node(ax, 0.10, 0.08, 'X', 'obs')
_node(ax, 0.90, 0.08, 'Y', 'obs')
_node(ax, 0.50, -0.18, 'A*', 'mis')
_edge(ax, 0.10, 0.75, 0.10, 0.08)
_edge(ax, 0.10, 0.75, 0.50, 0.45)
_edge(ax, 0.90, 0.75, 0.50, 0.45)
_edge(ax, 0.90, 0.75, 0.90, 0.08)
_edge(ax, 0.10, 0.08, 0.90, 0.08)
_edge(ax, 0.50, 0.45, 0.50, -0.18, 'meas')

# (g) IV (Instrument) — highlighted danger
ax = panels[6]
_title(ax, '(g) IV (Instrument)', 'Fragile (Wald amplification)', SUB_COL['fragile'], highlight='danger')
_node(ax, 0.22, 0.70, 'A', 'lat')
_node(ax, 0.78, 0.70, 'A*', 'mis')
_node(ax, 0.10, 0.16, 'X', 'obs')
_node(ax, 0.90, 0.16, 'Y', 'obs')
_node(ax, 0.50, -0.16, 'U', 'lat')
_edge(ax, 0.22, 0.70, 0.78, 0.70, 'meas')
_edge(ax, 0.22, 0.70, 0.10, 0.16)
_edge(ax, 0.10, 0.16, 0.90, 0.16)
_edge(ax, 0.50, -0.16, 0.10, 0.16)
_edge(ax, 0.50, -0.16, 0.90, 0.16)

# ═══════════════════════════════════════════════════════════
#  Legend
# ═══════════════════════════════════════════════════════════
handles = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor=PAL['obs_fill'],
           markeredgecolor=PAL['obs_edge'], markersize=9, markeredgewidth=1.3,
           lw=0, label='Observed'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=PAL['lat_fill'],
           markeredgecolor=PAL['lat_edge'], markersize=9, markeredgewidth=1.0,
           lw=0, label='Latent (dashed ○)'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=PAL['mis_fill'],
           markeredgecolor=PAL['mis_edge'], markersize=9, markeredgewidth=1.3,
           lw=0, label='Misclassified (A*)'),
    Line2D([0],[0], marker='s', color='w', markerfacecolor=PAL['con_fill'],
           markeredgecolor=PAL['con_edge'], markersize=8, markeredgewidth=1.3,
           lw=0, label='Conditioned on (A*)'),
    Line2D([0],[0], color=PAL['arrow'], lw=1.6, marker='>',
           markersize=5.5, label='Causal'),
    Line2D([0],[0], color=PAL['meas_arrow'], lw=1.1, ls='--',
           marker='>', markersize=4.5, label='Measurement'),
]
fig.legend(handles=handles, loc='lower center', ncol=6, fontsize=16,
           frameon=False, handlelength=2.0, columnspacing=1.6,
           handletextpad=0.5, bbox_to_anchor=(0.5, 0.008))

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
