#!/usr/bin/env python3
"""Figure 1: Seven canonical DAG topologies with starred-node annotation.
Hero figure — academic quality for EMNLP 2026.
figsize=(14,7) → LaTeX scales to textwidth (~7in) → all fonts halved."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch
from matplotlib.lines import Line2D
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'font.size': 18,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.10,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# Semantic colors (Okabe-Ito, color-blind safe)
C = dict(
    obs_f='#FFFFFF', obs_e='#3D3D3D',
    lat_f='#F5F5F5', lat_e='#8A8A8A',
    mis_f='#0072B2', mis_e='#005080',
    con_f='#0072B2', con_e='#005080',
    arr='#2A2A2A', mea='#7A8FA0', sh='#999999',
    hl_bg='#FFF3EB', hl_e='#D9956A',
)
SC = dict(atten='#0072B2', sign='#D55E00', amp='#CC7A00',
          mod='#555555', immune='#009E73', fragile='#D55E00')

R = 0.14  # node radius in data coords
SHRINK = R + 0.020

# ═══════════════════════════════════════════════════════════
#  Primitives
# ═══════════════════════════════════════════════════════════
def _node(ax, x, y, label, kind='obs'):
    sdx, sdy = 0.008, -0.012
    if kind == 'con':
        sz = R * 1.6
        ax.add_patch(FancyBboxPatch(
            (x-sz/2+sdx, y-sz/2+sdy), sz, sz,
            boxstyle='round,pad=0.018', fc=C['sh'], ec='none', alpha=0.20, zorder=2))
        ax.add_patch(FancyBboxPatch(
            (x-sz/2, y-sz/2), sz, sz,
            boxstyle='round,pad=0.018', fc=C['con_f'], ec=C['con_e'], lw=2.0, zorder=3))
        ax.text(x, y, label, ha='center', va='center',
                fontsize=18, color='white', fontweight='bold', zorder=4)
        return
    cfg = {
        'obs': (C['obs_f'], C['obs_e'], '-',  1.8, '#333', 'normal', 0.14),
        'lat': (C['lat_f'], C['lat_e'], '--', 1.5, '#555', 'normal', 0.12),
        'mis': (C['mis_f'], C['mis_e'], '-',  2.2, '#FFF', 'bold',   0.22),
    }
    fc, ec, ls, lw, tc, fw, sa = cfg[kind]
    ax.add_patch(Circle((x+sdx, y+sdy), R+0.006, fc=C['sh'], ec='none', alpha=sa, zorder=2))
    ax.add_patch(Circle((x, y), R, fc=fc, ec=ec, lw=lw, ls=ls, zorder=3))
    ax.text(x, y, label, ha='center', va='center',
            fontsize=18, color=tc, fontweight=fw, zorder=4)

def _edge(ax, x1, y1, x2, y2, kind='causal', rad=0):
    dx, dy = x2-x1, y2-y1
    d = np.sqrt(dx**2+dy**2)
    if d < 1e-6:
        return
    is_c = kind == 'causal'
    ax.add_patch(FancyArrowPatch(
        (x1+SHRINK*dx/d, y1+SHRINK*dy/d),
        (x2-SHRINK*dx/d, y2-SHRINK*dy/d),
        arrowstyle='-|>', mutation_scale=20 if is_c else 16,
        color=C['arr'] if is_c else C['mea'],
        lw=2.0 if is_c else 1.4,
        ls='-' if is_c else (0, (5, 4)),
        connectionstyle=f'arc3,rad={rad}', zorder=1))

def _title(ax, title, subtitle, sub_color, highlight=False):
    if highlight:
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        ax.add_patch(FancyBboxPatch(
            (xmin+0.02, ymin+0.02), xmax-xmin-0.04, ymax-ymin-0.04,
            boxstyle='round,pad=0.05',
            fc='#FFF0E5', ec=C['hl_e'], lw=2.2, alpha=0.70, zorder=0))
    ax.text(0.5, 1.12, title, ha='center', va='bottom',
            fontsize=22, fontweight='bold', color='#1A1A1A',
            transform=ax.transAxes)
    ax.text(0.5, 1.02, subtitle, ha='center', va='bottom',
            fontsize=17, fontstyle='italic', color=sub_color,
            transform=ax.transAxes)

# ═══════════════════════════════════════════════════════════
#  Layout: manual axes placement for precise square panels
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(15, 7))

pw = 0.195   # panel width (fraction of fig)
ph = 0.385   # panel height (fraction of fig)
hgap = 0.045 # horizontal gap between panels
vgap = 0.060 # vertical gap between rows
top_margin = 0.055

# Top row: 4 panels centered
top_y = 1 - top_margin - ph
top_total = 4*pw + 3*hgap
top_x0 = (1 - top_total) / 2

# Bottom row: 3 panels centered
bot_y = top_y - vgap - ph
bot_total = 3*pw + 2*hgap
bot_x0 = (1 - bot_total) / 2

# Match coordinate aspect to physical panel aspect → no whitespace with aspect='equal'
panel_w_in = pw * 15  # inches
panel_h_in = ph * 7   # inches
phys_ratio = panel_w_in / panel_h_in  # ~1.085
ylim_span = 1.30
xlim_span = ylim_span * phys_ratio
xc, yc = 0.50, 0.30  # coordinate center
XL = (xc - xlim_span/2, xc + xlim_span/2)
YL = (yc - ylim_span/2, yc + ylim_span/2)

panels = []
for i in range(4):
    ax = fig.add_axes([top_x0 + i*(pw+hgap), top_y, pw, ph])
    ax.set_xlim(*XL); ax.set_ylim(*YL)
    ax.set_aspect('equal')
    ax.axis('off')
    panels.append(ax)
for i in range(3):
    ax = fig.add_axes([bot_x0 + i*(pw+hgap), bot_y, pw, ph])
    ax.set_xlim(*XL); ax.set_ylim(*YL)
    ax.set_aspect('equal')
    ax.axis('off')
    panels.append(ax)

# ═══════════════════════════════════════════════════════════
#  DAGs
# ═══════════════════════════════════════════════════════════

# (a) Confounding: A→X, A→Y, X→Y, A⇢A*
ax = panels[0]
_title(ax, '(a) Confounding', 'Attenuation (toward OVB)', SC['atten'])
_node(ax, 0.22, 0.72, 'A', 'lat'); _node(ax, 0.78, 0.72, 'A*', 'mis')
_node(ax, 0.10, 0.10, 'X', 'obs'); _node(ax, 0.90, 0.10, 'Y', 'obs')
_edge(ax, 0.22, 0.72, 0.78, 0.72, 'meas')
_edge(ax, 0.22, 0.72, 0.10, 0.10)
_edge(ax, 0.22, 0.72, 0.90, 0.10)
_edge(ax, 0.10, 0.10, 0.90, 0.10)

# (b) Exposure: A→Y, A⇢A*
ax = panels[1]
_title(ax, '(b) Exposure', 'Sign reversal (83.4%)', SC['sign'], highlight=True)
_node(ax, 0.22, 0.62, 'A', 'lat'); _node(ax, 0.78, 0.62, 'A*', 'mis')
_node(ax, 0.50, 0.02, 'Y', 'obs')
_edge(ax, 0.22, 0.62, 0.78, 0.62, 'meas')
_edge(ax, 0.22, 0.62, 0.50, 0.02)

# (c) Mediation: X→A, A→Y, A⇢A*
ax = panels[2]
_title(ax, '(c) Mediation', 'Amplification', SC['amp'])
_node(ax, 0.50, 0.68, 'A', 'lat'); _node(ax, 0.92, 0.68, 'A*', 'mis')
_node(ax, 0.08, 0.10, 'X', 'obs'); _node(ax, 0.92, 0.10, 'Y', 'obs')
_edge(ax, 0.50, 0.68, 0.92, 0.68, 'meas')
_edge(ax, 0.08, 0.10, 0.50, 0.68)
_edge(ax, 0.50, 0.68, 0.92, 0.10)

# (d) Collider: X→A, Y→A, A⇢A*(conditioned)
ax = panels[3]
_title(ax, '(d) Collider', 'Attenuation (no sign flip)', SC['atten'])
_node(ax, 0.15, 0.72, 'X', 'obs'); _node(ax, 0.85, 0.72, 'Y', 'obs')
_node(ax, 0.50, 0.38, 'A', 'lat'); _node(ax, 0.50, -0.02, 'A*', 'con')
_edge(ax, 0.15, 0.72, 0.50, 0.38)
_edge(ax, 0.85, 0.72, 0.50, 0.38)
_edge(ax, 0.50, 0.38, 0.50, -0.02, 'meas')

# (e) Front-door: A→X, X→Y, U→A, U→Y, A⇢A*
ax = panels[4]
_title(ax, '(e) Front-door', 'Moderate sensitivity', SC['mod'])
_node(ax, 0.22, 0.72, 'A', 'lat'); _node(ax, 0.78, 0.72, 'A*', 'mis')
_node(ax, 0.05, 0.18, 'X', 'obs'); _node(ax, 0.95, 0.18, 'Y', 'obs')
_node(ax, 0.50, -0.15, 'U', 'lat')
_edge(ax, 0.22, 0.72, 0.78, 0.72, 'meas')
_edge(ax, 0.22, 0.72, 0.05, 0.18)
_edge(ax, 0.05, 0.18, 0.95, 0.18)
_edge(ax, 0.50, -0.15, 0.22, 0.72)
_edge(ax, 0.50, -0.15, 0.95, 0.18)

# (f) M-bias: U1→X, U1→A, U2→A, U2→Y, X→Y, A⇢A*
ax = panels[5]
_title(ax, '(f) M-bias', 'Immune', SC['immune'])
_node(ax, 0.10, 0.74, 'U₁', 'lat'); _node(ax, 0.90, 0.74, 'U₂', 'lat')
_node(ax, 0.50, 0.42, 'A', 'lat')
_node(ax, 0.10, 0.05, 'X', 'obs'); _node(ax, 0.90, 0.05, 'Y', 'obs')
_node(ax, 0.50, -0.22, 'A*', 'mis')
_edge(ax, 0.10, 0.74, 0.10, 0.05)
_edge(ax, 0.10, 0.74, 0.50, 0.42)
_edge(ax, 0.90, 0.74, 0.50, 0.42)
_edge(ax, 0.90, 0.74, 0.90, 0.05)
_edge(ax, 0.10, 0.05, 0.90, 0.05)
_edge(ax, 0.50, 0.42, 0.50, -0.22, 'meas')

# (g) IV (Instrument): A→X, X→Y, U→X, U→Y, A⇢A*
ax = panels[6]
_title(ax, '(g) IV (Instrument)', 'Fragile (Wald amplification)', SC['fragile'])
_node(ax, 0.22, 0.72, 'A', 'lat'); _node(ax, 0.78, 0.72, 'A*', 'mis')
_node(ax, 0.10, 0.18, 'X', 'obs'); _node(ax, 0.90, 0.18, 'Y', 'obs')
_node(ax, 0.50, -0.15, 'U', 'lat')
_edge(ax, 0.22, 0.72, 0.78, 0.72, 'meas')
_edge(ax, 0.22, 0.72, 0.10, 0.18)
_edge(ax, 0.10, 0.18, 0.90, 0.18)
_edge(ax, 0.50, -0.15, 0.10, 0.18)
_edge(ax, 0.50, -0.15, 0.90, 0.18)

# ═══════════════════════════════════════════════════════════
#  Legend
# ═══════════════════════════════════════════════════════════
handles = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor=C['obs_f'],
           markeredgecolor=C['obs_e'], markersize=10, lw=0, label='Observed'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=C['lat_f'],
           markeredgecolor=C['lat_e'], markersize=10, lw=0, label='Latent (dashed ○)'),
    Line2D([0],[0], marker='o', color='w', markerfacecolor=C['mis_f'],
           markeredgecolor=C['mis_e'], markersize=10, lw=0, label='Misclassified (A*)'),
    Line2D([0],[0], marker='s', color='w', markerfacecolor=C['con_f'],
           markeredgecolor=C['con_e'], markersize=9, lw=0, label='Conditioned on (A*)'),
    Line2D([0],[0], color=C['arr'], lw=2.0, marker='>', markersize=6, label='Causal'),
    Line2D([0],[0], color=C['mea'], lw=1.3, ls='--', marker='>', markersize=5, label='Measurement'),
]
fig.legend(handles=handles, loc='lower center', ncol=6, fontsize=15,
           frameon=False, handlelength=2.0, columnspacing=1.5,
           handletextpad=0.6, bbox_to_anchor=(0.5, 0.005))

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
