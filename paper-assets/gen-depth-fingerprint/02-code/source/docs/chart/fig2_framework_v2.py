"""
Framework figure for Depth Fingerprinting paper (Figure 2).
Professional academic style matching ACL/EMNLP publication standards.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# ── Global style ──────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 8,
    'axes.linewidth': 0.6,
    'text.usetex': False,
})

# ── Color palette (muted, professional) ───────────────────────────────────
C = {
    # Panel backgrounds
    'panel_bg':      '#F7F9FC',
    'panel_border':  '#C5CDD8',
    # Section headers
    'hdr_construct': '#2B6CB0',
    'hdr_feature':   '#2D7D46',
    'hdr_classify':  '#8B5E3C',
    # Boxes
    'seed':          '#EBF4FA',
    'seed_border':   '#4A90C4',
    'gen_light':     '#D6E9F8',
    'gen_mid':       '#A8D0EF',
    'gen_dark':      '#6AADE4',
    'gen_deeper':    '#3B8AD0',
    'gen_deepest':   '#1E6DB5',
    'generator':     '#FFF3E6',
    'gen_border':    '#D4883E',
    # Feature colors
    'drift_fill':    '#E8F5E9',
    'drift_border':  '#4CAF50',
    'drift_text':    '#2E7D32',
    'stat_fill':     '#FFF3E0',
    'stat_border':   '#FF9800',
    'stat_text':     '#E65100',
    'inter_fill':    '#F3E5F5',
    'inter_border':  '#9C27B0',
    'inter_text':    '#6A1B9A',
    # NLL curve
    'nll_fill':      '#C8E6C9',
    'nll_line':      '#388E3C',
    # Pythia box
    'pythia_fill':   '#E8F5E9',
    'pythia_border': '#4CAF50',
    # Classification
    'xgb_fill':      '#F3E8D9',
    'xgb_border':    '#8B6F4E',
    'cls0_fill':     '#E3F2FD',
    'cls1_fill':     '#BBDEFB',
    'cls2_fill':     '#90CAF9',
    'cls_border':    '#1976D2',
    # DDR plot lines
    'ddr_drift':     '#2E7D32',
    'ddr_stat':      '#E65100',
    'ddr_inter':     '#7B1FA2',
    # Arrows
    'arrow':         '#5A6A7A',
    'arrow_light':   '#8899AA',
}


def rounded_box(ax, x, y, w, h, text, fc, ec, fs=7.5, fw='normal',
                tc='#333333', rx=0.02, ry=0.02, alpha=1.0, zorder=3,
                text_offset_y=0, ha='center', va='center', ls='-', lw=0.8,
                mono=False):
    """Draw a rounded rectangle with centered text."""
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f"round,pad=0,rounding_size=0.012",
                         facecolor=fc, edgecolor=ec, linewidth=lw,
                         alpha=alpha, zorder=zorder, linestyle=ls)
    ax.add_patch(box)
    fontdict = {'fontsize': fs, 'fontweight': fw, 'color': tc,
                'fontfamily': 'monospace' if mono else 'sans-serif'}
    ax.text(x + w/2, y + h/2 + text_offset_y, text,
            ha=ha, va=va, fontdict=fontdict, zorder=zorder+1)
    return box


def draw_arrow(ax, x1, y1, x2, y2, color=None, lw=1.0, style='-|>',
               mutation_scale=8, zorder=2, connectionstyle='arc3,rad=0',
               ls='-'):
    """Draw a clean arrow between two points."""
    c = color or C['arrow']
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle=style, color=c,
                            linewidth=lw, mutation_scale=mutation_scale,
                            zorder=zorder, connectionstyle=connectionstyle,
                            linestyle=ls)
    ax.add_patch(arrow)
    return arrow


def draw_section_header(ax, x, y, text, color, fs=9.5):
    """Draw a section header label."""
    ax.text(x, y, text, fontsize=fs, fontweight='bold', color=color,
            ha='center', va='center', zorder=10)


# ── Figure setup ──────────────────────────────────────────────────────────
fig, ax = plt.subplots(1, 1, figsize=(6.5, 2.6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
fig.patch.set_facecolor('white')

# ══════════════════════════════════════════════════════════════════════════
# PANEL 1: Chain Construction (x: 0.01 - 0.33)
# ══════════════════════════════════════════════════════════════════════════
p1_x, p1_w = 0.012, 0.305
panel1 = FancyBboxPatch((p1_x, 0.03), p1_w, 0.90,
                         boxstyle="round,pad=0,rounding_size=0.015",
                         facecolor=C['panel_bg'], edgecolor=C['panel_border'],
                         linewidth=0.8, alpha=0.5, zorder=1)
ax.add_patch(panel1)

# Header
draw_section_header(ax, p1_x + p1_w/2, 0.955, 'Chain Construction',
                    C['hdr_construct'], fs=9)

# ── Recursive generation chain ──
# Show: text_0 → LLM → text_1 → LLM → text_2 → ...
chain_y_top = 0.82
chain_y_bot = 0.52
chain_cx = p1_x + p1_w/2  # center x

# Text boxes (staggered vertically with generator arrows)
txt_w, txt_h = 0.065, 0.075
gen_w, gen_h = 0.048, 0.055

# Positions for the chain elements
# Row layout: text_0  →G→  text_1  →G→  text_2  →...→  text_d
chain_items_x = [0.025, 0.095, 0.165, 0.235]
chain_y = 0.735

# Gen-0 (seed/human)
depth_colors = [C['seed'], C['gen_light'], C['gen_mid'], C['gen_dark']]
depth_borders = [C['seed_border'], '#6AADE4', '#3B8AD0', '#1E6DB5']
depth_labels = ['gen-0', 'gen-1', 'gen-2', 'gen-d']

# Small "Human text" label above gen-0
ax.text(chain_items_x[0] + txt_w/2, chain_y + txt_h + 0.025,
        'Human\ntext', fontsize=5.5, ha='center', va='center',
        color='#555555', style='italic', zorder=5)

for i, (xi, lbl, fc, ec) in enumerate(zip(chain_items_x, depth_labels,
                                            depth_colors, depth_borders)):
    rounded_box(ax, xi, chain_y, txt_w, txt_h, lbl,
                fc=fc, ec=ec, fs=6.5, fw='bold', tc='#333333')

    # Draw generator box + arrows between text boxes
    if i < len(chain_items_x) - 1:
        # Arrow from text_i to generator
        gx = xi + txt_w + 0.002
        gy = chain_y + txt_h/2
        # Small LLM/G box between
        g_box_x = (xi + txt_w + chain_items_x[i+1]) / 2 - gen_w/2 + 0.002
        g_box_y = chain_y + (txt_h - gen_h) / 2

        rounded_box(ax, g_box_x, g_box_y, gen_w, gen_h, 'G',
                    fc=C['generator'], ec=C['gen_border'],
                    fs=7, fw='bold', tc=C['gen_border'])

        # Arrows
        draw_arrow(ax, xi + txt_w + 0.003, chain_y + txt_h/2,
                   g_box_x - 0.002, chain_y + txt_h/2,
                   color=C['arrow_light'], lw=0.7, mutation_scale=6)
        draw_arrow(ax, g_box_x + gen_w + 0.002, chain_y + txt_h/2,
                   chain_items_x[i+1] - 0.003, chain_y + txt_h/2,
                   color=C['arrow_light'], lw=0.7, mutation_scale=6)

# Dots between gen-2 and gen-d
# Already handled by the chain layout

# "Generation depth d" label with arrow underneath
ax.annotate('', xy=(chain_items_x[-1] + txt_w, chain_y - 0.035),
            xytext=(chain_items_x[0], chain_y - 0.035),
            arrowprops=dict(arrowstyle='->', color='#888888', lw=0.7))
ax.text((chain_items_x[0] + chain_items_x[-1] + txt_w) / 2, chain_y - 0.065,
        'Generation depth d', fontsize=6, ha='center', va='center',
        color='#666666', style='italic')

# ── Dataset specs (small, compact) ──
spec_y = 0.10
spec_x = p1_x + 0.015
spec_items = [
    '8 base LLMs, 5 families',
    '0.6B – 8B parameters',
    '3 prompt types',
    'τ=0.7, top-p=0.9, max 256 tok',
]
for j, item in enumerate(spec_items):
    ax.text(spec_x + 0.005, spec_y + (3-j) * 0.085,
            item, fontsize=5.5, ha='left', va='center',
            color='#666666', zorder=5)

# Thin separator line
ax.plot([p1_x + 0.015, p1_x + p1_w - 0.015],
        [spec_y + 3.4 * 0.085, spec_y + 3.4 * 0.085],
        color='#D0D8E0', lw=0.5, zorder=2)

# ══════════════════════════════════════════════════════════════════════════
# PANEL 2: Feature Extraction + DDR (x: 0.34 - 0.67)
# ══════════════════════════════════════════════════════════════════════════
p2_x, p2_w = 0.335, 0.325
panel2 = FancyBboxPatch((p2_x, 0.03), p2_w, 0.90,
                         boxstyle="round,pad=0,rounding_size=0.015",
                         facecolor=C['panel_bg'], edgecolor=C['panel_border'],
                         linewidth=0.8, alpha=0.5, zorder=1)
ax.add_patch(panel2)

draw_section_header(ax, p2_x + p2_w/2, 0.955, 'Feature Extraction & DDR',
                    C['hdr_feature'], fs=9)

# ── Pythia reference model box ──
pythia_x, pythia_y = p2_x + 0.03, 0.855
pythia_w, pythia_h = 0.12, 0.055
rounded_box(ax, pythia_x, pythia_y, pythia_w, pythia_h,
            'Pythia-410M', fc=C['pythia_fill'], ec=C['pythia_border'],
            fs=6.5, fw='bold', tc=C['drift_text'])

# ── Mini NLL distribution curve ──
nll_cx = p2_x + p2_w/2 + 0.04
nll_cy = 0.87
nll_w, nll_h = 0.10, 0.06

# Draw a small bell-like NLL distribution
t = np.linspace(-3, 3, 80)
y_nll = np.exp(-0.5 * t**2) / (np.sqrt(2 * np.pi))
# Scale to fit in the allocated space
t_scaled = nll_cx + t / 6 * nll_w
y_scaled = nll_cy - nll_h/2 + y_nll / max(y_nll) * nll_h * 0.85

ax.fill_between(t_scaled, nll_cy - nll_h/2, y_scaled,
                color=C['nll_fill'], alpha=0.7, zorder=3)
ax.plot(t_scaled, y_scaled, color=C['nll_line'], lw=1.0, zorder=4)

# Small axis line
ax.plot([t_scaled[0], t_scaled[-1]], [nll_cy - nll_h/2, nll_cy - nll_h/2],
        color='#888888', lw=0.4, zorder=3)

# Label
ax.text(nll_cx, nll_cy + nll_h/2 + 0.015, 'Token NLL dist.',
        fontsize=5.5, ha='center', va='center', color='#555555', zorder=5)

# Arrow from Pythia to NLL curve
draw_arrow(ax, pythia_x + pythia_w + 0.005, pythia_y + pythia_h/2,
           t_scaled[0] + 0.01, nll_cy,
           color=C['arrow_light'], lw=0.6, mutation_scale=5)

# ── DDR Feature groups ──
# Three groups stacked vertically
group_x = p2_x + 0.018
group_w = p2_w - 0.036

# Drifting features
drift_y = 0.56
drift_h = 0.17
drift_box = FancyBboxPatch((group_x, drift_y), group_w, drift_h,
                            boxstyle="round,pad=0,rounding_size=0.01",
                            facecolor=C['drift_fill'], edgecolor=C['drift_border'],
                            linewidth=0.8, alpha=0.8, zorder=2)
ax.add_patch(drift_box)

# Drifting header with correlation threshold
ax.text(group_x + 0.008, drift_y + drift_h - 0.025,
        'Drifting', fontsize=7, fontweight='bold', color=C['drift_text'],
        ha='left', va='center', zorder=5)
ax.text(group_x + group_w - 0.008, drift_y + drift_h - 0.025,
        '|ρ| > 0.60', fontsize=5.5, color=C['drift_text'],
        ha='right', va='center', zorder=5, style='italic')

# Feature pills inside drifting
drift_features = ['entropy_mean', 'entropy_min', 'TTR', 'hapax_ratio']
pill_w = 0.068
pill_h = 0.04
pill_gap = 0.006
total_pills_w = len(drift_features) * pill_w + (len(drift_features)-1) * pill_gap
pills_start_x = group_x + (group_w - total_pills_w) / 2
pill_y = drift_y + 0.025

for k, feat in enumerate(drift_features):
    px = pills_start_x + k * (pill_w + pill_gap)
    rounded_box(ax, px, pill_y, pill_w, pill_h, feat,
                fc='white', ec=C['drift_border'], fs=5.2, fw='normal',
                tc=C['drift_text'], lw=0.5, mono=True)

# Small trend arrow (downward) beside drifting label
ax.annotate('', xy=(group_x + 0.072, drift_y + drift_h - 0.042),
            xytext=(group_x + 0.055, drift_y + drift_h - 0.012),
            arrowprops=dict(arrowstyle='->', color=C['drift_text'],
                           lw=0.8, connectionstyle='arc3,rad=-0.2'))

# Stationary features
stat_y = 0.33
stat_h = 0.14
stat_box = FancyBboxPatch((group_x, stat_y), group_w, stat_h,
                           boxstyle="round,pad=0,rounding_size=0.01",
                           facecolor=C['stat_fill'], edgecolor=C['stat_border'],
                           linewidth=0.8, alpha=0.8, zorder=2)
ax.add_patch(stat_box)

ax.text(group_x + 0.008, stat_y + stat_h - 0.025,
        'Stationary', fontsize=7, fontweight='bold', color=C['stat_text'],
        ha='left', va='center', zorder=5)
ax.text(group_x + group_w - 0.008, stat_y + stat_h - 0.025,
        '|ρ| < 0.10', fontsize=5.5, color=C['stat_text'],
        ha='right', va='center', zorder=5, style='italic')

stat_features = ['entropy_max', 'tail_decay']
total_stat_w = len(stat_features) * pill_w + (len(stat_features)-1) * pill_gap
stat_start_x = group_x + (group_w - total_stat_w) / 2
stat_pill_y = stat_y + 0.025

for k, feat in enumerate(stat_features):
    px = stat_start_x + k * (pill_w + pill_gap)
    rounded_box(ax, px, stat_pill_y, pill_w, pill_h, feat,
                fc='white', ec=C['stat_border'], fs=5.2, fw='normal',
                tc=C['stat_text'], lw=0.5, mono=True)

# Small flat arrow for stationary
ax.annotate('', xy=(group_x + 0.075, stat_y + stat_h - 0.027),
            xytext=(group_x + 0.058, stat_y + stat_h - 0.027),
            arrowprops=dict(arrowstyle='->', color=C['stat_text'], lw=0.8))

# Intermediate
inter_y = 0.18
inter_h = 0.10
inter_box = FancyBboxPatch((group_x, inter_y), group_w, inter_h,
                            boxstyle="round,pad=0,rounding_size=0.01",
                            facecolor=C['inter_fill'], edgecolor=C['inter_border'],
                            linewidth=0.7, alpha=0.6, zorder=2)
ax.add_patch(inter_box)

ax.text(group_x + 0.008, inter_y + inter_h - 0.025,
        'Intermediate', fontsize=6.5, fontweight='bold', color=C['inter_text'],
        ha='left', va='center', zorder=5)

# Single feature pill
int_feat_x = group_x + (group_w - pill_w) / 2
rounded_box(ax, int_feat_x, inter_y + 0.015, pill_w, pill_h, 'entropy_std',
            fc='white', ec=C['inter_border'], fs=5.2, fw='normal',
            tc=C['inter_text'], lw=0.5, mono=True)

# ── Arrow from NLL to feature groups ──
draw_arrow(ax, nll_cx, nll_cy - nll_h/2 - 0.005,
           nll_cx, drift_y + drift_h + 0.008,
           color=C['arrow'], lw=0.8, mutation_scale=7)

# ── "Surface features" label next to TTR/hapax ──
ax.text(group_x + group_w - 0.008, drift_y + 0.008,
        'incl. surface features', fontsize=4.5, ha='right', va='bottom',
        color='#888888', style='italic', zorder=5)


# ══════════════════════════════════════════════════════════════════════════
# PANEL 3: Classification & DDR Insight (x: 0.68 - 0.99)
# ══════════════════════════════════════════════════════════════════════════
p3_x, p3_w = 0.678, 0.310
panel3 = FancyBboxPatch((p3_x, 0.03), p3_w, 0.90,
                         boxstyle="round,pad=0,rounding_size=0.015",
                         facecolor=C['panel_bg'], edgecolor=C['panel_border'],
                         linewidth=0.8, alpha=0.5, zorder=1)
ax.add_patch(panel3)

draw_section_header(ax, p3_x + p3_w/2, 0.955, 'Classification',
                    C['hdr_classify'], fs=9)

# ── XGBoost box ──
xgb_x = p3_x + 0.06
xgb_y = 0.825
xgb_w = 0.19
xgb_h = 0.065
rounded_box(ax, xgb_x, xgb_y, xgb_w, xgb_h,
            'XGBoost (LOGO-CV)', fc=C['xgb_fill'], ec=C['xgb_border'],
            fs=7, fw='bold', tc='#5D4037')

# ── 3-class output boxes ──
cls_labels = ['gen-0', 'gen-1', 'gen-2+']
cls_fills = [C['cls0_fill'], C['cls1_fill'], C['cls2_fill']]
cls_w = 0.055
cls_h = 0.05
cls_gap = 0.006
total_cls_w = 3 * cls_w + 2 * cls_gap
cls_start_x = xgb_x + (xgb_w - total_cls_w) / 2
cls_y = 0.73

for k, (lbl, fc) in enumerate(zip(cls_labels, cls_fills)):
    cx = cls_start_x + k * (cls_w + cls_gap)
    rounded_box(ax, cx, cls_y, cls_w, cls_h, lbl,
                fc=fc, ec=C['cls_border'], fs=6, fw='bold',
                tc='#1565C0', lw=0.6)

# Arrow from XGBoost to output
draw_arrow(ax, xgb_x + xgb_w/2, xgb_y - 0.003,
           xgb_x + xgb_w/2, cls_y + cls_h + 0.008,
           color=C['arrow'], lw=0.7, mutation_scale=6)

# "3-class output" label
ax.text(xgb_x + xgb_w/2, cls_y - 0.02,
        '3-class depth prediction', fontsize=5.5, ha='center', va='center',
        color='#666666', style='italic', zorder=5)

# ── DDR Insight mini-plot ──
ddr_title_y = 0.65
ax.text(p3_x + p3_w/2, ddr_title_y,
        'Differential Depth Response (DDR)', fontsize=6.5, fontweight='bold',
        ha='center', va='center', color='#444444', zorder=5)

# Mini axes for DDR plot
ddr_left = p3_x + 0.05
ddr_bottom = 0.12
ddr_width = 0.21
ddr_height = 0.46

# Create an inset axes for the DDR plot
ax_ddr = fig.add_axes([ddr_left, ddr_bottom, ddr_width, ddr_height])

depths = np.array([0, 1, 2, 3, 4])
# Drifting: monotonic decrease (e.g., entropy_mean normalized)
drift_vals = np.array([0.85, 0.62, 0.45, 0.35, 0.28])
# Stationary: roughly flat
stat_vals = np.array([0.42, 0.44, 0.41, 0.43, 0.42])
# Intermediate: slight change then flat
inter_vals = np.array([0.55, 0.48, 0.44, 0.42, 0.40])

ax_ddr.plot(depths, drift_vals, '-o', color=C['ddr_drift'], lw=1.3,
            markersize=3.5, markerfacecolor='white', markeredgewidth=1.0,
            label='Drifting', zorder=5)
ax_ddr.plot(depths, stat_vals, '-s', color=C['ddr_stat'], lw=1.3,
            markersize=3.5, markerfacecolor='white', markeredgewidth=1.0,
            label='Stationary', zorder=5)
ax_ddr.plot(depths, inter_vals, '-^', color=C['ddr_inter'], lw=1.0,
            markersize=3, markerfacecolor='white', markeredgewidth=0.8,
            label='Intermediate', zorder=5, alpha=0.7, linestyle='--')

# Shade the "saturated" region (depth >= 2)
ax_ddr.axvspan(1.5, 4.2, alpha=0.06, color='#888888', zorder=1)
ax_ddr.text(2.8, 0.88, 'gen-2+\nmerged', fontsize=4.5, ha='center',
            va='center', color='#999999', style='italic')

# Vertical dashed line at depth boundary
ax_ddr.axvline(x=1.5, color='#CCCCCC', lw=0.6, ls='--', zorder=1)

ax_ddr.set_xlabel('Depth d', fontsize=6, labelpad=2)
ax_ddr.set_ylabel('Normalized feature value', fontsize=5.5, labelpad=2)
ax_ddr.set_xlim(-0.3, 4.3)
ax_ddr.set_ylim(0.15, 0.95)
ax_ddr.set_xticks([0, 1, 2, 3, 4])
ax_ddr.set_xticklabels(['0', '1', '2', '3', '4'], fontsize=5.5)
ax_ddr.set_yticks([0.2, 0.4, 0.6, 0.8])
ax_ddr.set_yticklabels(['', '', '', ''], fontsize=5)
ax_ddr.tick_params(axis='both', length=2, width=0.4, pad=1)
ax_ddr.spines['top'].set_visible(False)
ax_ddr.spines['right'].set_visible(False)
ax_ddr.spines['left'].set_linewidth(0.5)
ax_ddr.spines['bottom'].set_linewidth(0.5)

# Legend
leg = ax_ddr.legend(fontsize=5, loc='upper right', frameon=True,
                    framealpha=0.9, edgecolor='#DDDDDD', borderpad=0.3,
                    handlelength=1.2, handletextpad=0.3)
leg.get_frame().set_linewidth(0.4)

# ══════════════════════════════════════════════════════════════════════════
# INTER-PANEL ARROWS
# ══════════════════════════════════════════════════════════════════════════
# Panel 1 → Panel 2
arrow_y_mid = 0.5
draw_arrow(ax, p1_x + p1_w + 0.003, arrow_y_mid,
           p2_x - 0.003, arrow_y_mid,
           color=C['arrow'], lw=1.2, mutation_scale=10)

# Panel 2 → Panel 3
draw_arrow(ax, p2_x + p2_w + 0.003, arrow_y_mid,
           p3_x - 0.003, arrow_y_mid,
           color=C['arrow'], lw=1.2, mutation_scale=10)

# ── Section letter labels (a), (b), (c) ──
ax.text(p1_x + 0.012, 0.96, '(a)', fontsize=8, fontweight='bold',
        color='#444444', ha='left', va='center', zorder=10)
ax.text(p2_x + 0.012, 0.96, '(b)', fontsize=8, fontweight='bold',
        color='#444444', ha='left', va='center', zorder=10)
ax.text(p3_x + 0.012, 0.96, '(c)', fontsize=8, fontweight='bold',
        color='#444444', ha='left', va='center', zorder=10)


# ── Save ──────────────────────────────────────────────────────────────────
outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
fig.savefig(f'{outdir}/fig2_framework.pdf', dpi=600, bbox_inches='tight',
            pad_inches=0.02, facecolor='white')
fig.savefig(f'{outdir}/fig2_framework.png', dpi=300, bbox_inches='tight',
            pad_inches=0.02, facecolor='white')
print("Saved fig2_framework.pdf and .png")
plt.close()
