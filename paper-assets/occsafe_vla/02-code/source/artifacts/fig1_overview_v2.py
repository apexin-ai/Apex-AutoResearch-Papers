"""
fig1_overview_v2.py — CoRL 2026 Hero Figure (Figure 1).
Three panels: (a) The Problem, (b) Our Approach, (c) Key Finding.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# --- Color palette (Okabe-Ito inspired, colorblind-safe) ---
C = {
    'blue':      '#0072B2',
    'orange':    '#D55E00',
    'gray':      '#7F8C8D',
    'red':       '#CC3333',
    'green':     '#009E73',
    'text':      '#2C3E50',
    'subtle':    '#95A5A6',
    'enc_fill':  '#EBF0F7',
    'enc_edge':  '#0072B2',
    'llm_fill':  '#F5F0E8',
    'llm_edge':  '#937860',
    'act_fill':  '#E8F5E9',
    'act_edge':  '#009E73',
    'aux_fill':  '#FFF3E0',
    'aux_edge':  '#E8870E',
}

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'text.color': C['text'],
    'axes.labelcolor': C['text'],
    'axes.linewidth': 0.7,
    'xtick.major.width': 0.7,
    'ytick.major.width': 0.7,
})

fig = plt.figure(figsize=(14, 4.8), dpi=300, facecolor='white')

# Panel layout — wider gaps between panels
ax_a = fig.add_axes([0.01, 0.06, 0.26, 0.87])
ax_b = fig.add_axes([0.30, 0.06, 0.39, 0.87])
ax_c = fig.add_axes([0.74, 0.14, 0.25, 0.76])

for ax in [ax_a, ax_b]:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

# --- Panel separators (vertical lines, more visible) ---
for sep_x in [0.285, 0.715]:
    fig.add_artist(plt.Line2D([sep_x, sep_x], [0.06, 0.92],
                               transform=fig.transFigure, color='#C8CDD0',
                               lw=1.0, zorder=0))

# ============================================================
# Helper functions
# ============================================================
def draw_box(ax, xy, w, h, label, sublabel=None, fill='white', edge='#333',
             fontsize=8.5, lw=1.2, radius=0.15, alpha=1.0, label_color=None,
             sublabel_color=None, bold=True):
    box = FancyBboxPatch(xy, w, h, boxstyle=f"round,pad=0,rounding_size={radius}",
                         facecolor=fill, edgecolor=edge, linewidth=lw, alpha=alpha,
                         zorder=3)
    ax.add_patch(box)
    cx, cy = xy[0] + w/2, xy[1] + h/2
    lc = label_color or C['text']
    sc = sublabel_color or C['subtle']
    fw = 'bold' if bold else 'normal'
    if sublabel:
        ax.text(cx, cy + 0.18, label, ha='center', va='center', fontsize=fontsize,
                fontweight=fw, color=lc, zorder=4)
        ax.text(cx, cy - 0.25, sublabel, ha='center', va='center', fontsize=6.5,
                color=sc, zorder=4, style='italic')
    else:
        ax.text(cx, cy, label, ha='center', va='center', fontsize=fontsize,
                fontweight=fw, color=lc, zorder=4)

def draw_arrow(ax, start, end, color='#555', lw=1.2, style='->', mutation=12,
               linestyle='-', zorder=2):
    arrow = FancyArrowPatch(start, end, arrowstyle=style, color=color,
                            linewidth=lw, mutation_scale=mutation, zorder=zorder,
                            linestyle=linestyle)
    ax.add_patch(arrow)

# ============================================================
# PANEL (a): "The Problem" — Collision Scenario
# ============================================================
ax_a.text(0.15, 9.6, '(a)', fontsize=12, fontweight='bold', va='top', color=C['text'])
ax_a.text(1.2, 9.6, 'The Problem', fontsize=12, fontweight='bold', va='top',
          color=C['text'])

# Robot arm — thicker links, larger joints, better gripper
base_x, base_y = 1.8, 1.8
ax_a.add_patch(FancyBboxPatch((base_x - 1.0, base_y - 0.75), 2.0, 0.7,
               boxstyle="round,pad=0,rounding_size=0.1",
               facecolor='#BDC3C7', edgecolor='#7F8C8D', lw=1.5, zorder=5))
ax_a.text(base_x, base_y - 0.40, 'BASE', fontsize=6, ha='center', va='center',
          color='#555', fontweight='bold', zorder=6)

j0 = (base_x, base_y)
j1 = (base_x + 1.0, base_y + 2.0)
j2 = (base_x + 3.0, base_y + 3.0)
ee = (base_x + 4.5, base_y + 2.2)

for (s, e) in [(j0, j1), (j1, j2), (j2, ee)]:
    ax_a.plot([s[0], e[0]], [s[1], e[1]], color='#4A5568', lw=5.0,
              solid_capstyle='round', zorder=4)
    ax_a.plot([s[0], e[0]], [s[1], e[1]], color='#718096', lw=3.0,
              solid_capstyle='round', zorder=4)

for j, sz in [(j0, 12), (j1, 11), (j2, 10)]:
    ax_a.plot(j[0], j[1], 'o', color='#2C3E50', markersize=sz, zorder=6)
    ax_a.plot(j[0], j[1], 'o', color='#A0AEC0', markersize=sz-3, zorder=7)

gx, gy = ee
ax_a.plot([gx, gx+0.5], [gy, gy+0.6], color='#4A5568', lw=3.5,
          solid_capstyle='round', zorder=4)
ax_a.plot([gx, gx+0.5], [gy, gy-0.6], color='#4A5568', lw=3.5,
          solid_capstyle='round', zorder=4)
ax_a.plot([gx+0.5, gx+0.55], [gy+0.6, gy+0.35], color='#4A5568', lw=2.5,
          solid_capstyle='round', zorder=4)
ax_a.plot([gx+0.5, gx+0.55], [gy-0.6, gy-0.35], color='#4A5568', lw=2.5,
          solid_capstyle='round', zorder=4)
ax_a.plot(gx, gy, 'o', color='#2C3E50', markersize=8, zorder=6)
ax_a.plot(gx, gy, 'o', color='#A0AEC0', markersize=5, zorder=7)

# Obstacle
obs_x, obs_y = 7.8, 4.0
ax_a.add_patch(FancyBboxPatch((obs_x - 1.0, obs_y - 1.0), 2.0, 2.0,
               boxstyle="round,pad=0,rounding_size=0.15",
               facecolor=C['red'], edgecolor='#AA2222', lw=1.2,
               alpha=0.22, zorder=3))
ax_a.add_patch(FancyBboxPatch((obs_x - 1.0, obs_y - 1.0), 2.0, 2.0,
               boxstyle="round,pad=0,rounding_size=0.15",
               facecolor='none', edgecolor=C['red'], lw=1.5, zorder=4))
ax_a.text(obs_x, obs_y, 'OBSTACLE', fontsize=7, ha='center', va='center',
          color=C['red'], fontweight='bold', zorder=5)

# Collision zone
coll_cx = (gx + obs_x) / 2 + 0.3
coll_cy = (gy + obs_y) / 2
ax_a.add_patch(plt.Circle((coll_cx, coll_cy), 1.3, facecolor=C['red'],
                            edgecolor='none', alpha=0.08, lw=0, zorder=2))
ax_a.add_patch(plt.Circle((coll_cx, coll_cy), 1.3, facecolor='none',
                            edgecolor=C['red'], alpha=0.45, lw=1.5,
                            linestyle='--', zorder=3))

# Warning triangle
warn_cx, warn_cy = coll_cx, coll_cy + 1.7
tri_h = 0.7
tri = plt.Polygon([(warn_cx, warn_cy + tri_h*0.55),
                    (warn_cx - tri_h*0.5, warn_cy - tri_h*0.3),
                    (warn_cx + tri_h*0.5, warn_cy - tri_h*0.3)],
                   facecolor='#FFCC02', edgecolor=C['red'], lw=1.5,
                   zorder=6, closed=True)
ax_a.add_patch(tri)
ax_a.text(warn_cx, warn_cy + 0.0, '!', fontsize=10, ha='center', va='center',
          color=C['red'], fontweight='bold', zorder=7)

# Trajectory arrow
draw_arrow(ax_a, (gx + 0.35, gy + 0.1), (obs_x - 1.15, obs_y - 0.2),
           color=C['red'], lw=1.0, style='->', linestyle='--', mutation=10)

# Text
ax_a.text(5.0, 8.2, 'VLA policies lack\ncollision awareness', fontsize=8.5,
          ha='center', va='center', color=C['text'], fontweight='bold',
          linespacing=1.4)
ax_a.text(5.0, 7.0, 'Deployed in safety-critical\nenvironments where collisions\ncause irreversible damage',
          fontsize=7, ha='center', va='center', color=C['subtle'],
          linespacing=1.4, style='italic')

# Benchmark box
ax_a.add_patch(FancyBboxPatch((0.5, 0.05), 9.0, 0.7,
               boxstyle="round,pad=0,rounding_size=0.1",
               facecolor='#F0F4F8', edgecolor='#BDC3C7', lw=0.8, zorder=3))
ax_a.text(5.0, 0.4, 'SafeLIBERO benchmark: 10 tasks, collision-aware evaluation',
          fontsize=6.5, ha='center', va='center', color=C['text'], zorder=4)

# ============================================================
# PANEL (b): "Our Approach" — Architecture Overview
# ============================================================
ax_b.text(0.15, 9.6, '(b)', fontsize=11, fontweight='bold', va='top', color=C['text'])
ax_b.text(1.1, 9.6, 'Our Approach', fontsize=10.5, fontweight='bold', va='top',
          color=C['text'])

# RGB Observation
draw_box(ax_b, (3.0, 0.2), 4.0, 0.8, 'RGB Observation', fill='#F0F4F8',
         edge=C['subtle'], fontsize=8, lw=0.8, bold=False)

# Vision Encoders
enc_y = 1.8
draw_box(ax_b, (0.6, enc_y), 3.4, 1.0, 'DINOv2', sublabel='ViT-L patches',
         fill=C['enc_fill'], edge=C['enc_edge'], fontsize=8.5)
draw_box(ax_b, (6.0, enc_y), 3.4, 1.0, 'SigLIP', sublabel='ViT-So patches',
         fill=C['enc_fill'], edge=C['enc_edge'], fontsize=8.5)

# LoRA badges
for lx in [0.55, 5.95]:
    ax_b.text(lx + 0.15, enc_y + 1.15, 'LoRA', fontsize=6, color=C['blue'],
              fontweight='bold', ha='left', style='italic',
              bbox=dict(boxstyle='round,pad=0.12', facecolor='white',
                        edgecolor=C['blue'], lw=0.5, alpha=0.9), zorder=5)

# BN / LN badges (below encoders, prominent)
for ex in [2.3, 7.7]:
    ax_b.text(ex - 0.55, enc_y - 0.38, 'BN', fontsize=7, color='white',
              fontweight='bold', ha='center', va='center',
              bbox=dict(boxstyle='round,pad=0.12', facecolor=C['blue'],
                        edgecolor=C['blue'], lw=0.8), zorder=5)
    ax_b.text(ex, enc_y - 0.38, '/', fontsize=7, color=C['subtle'],
              ha='center', va='center', zorder=5)
    ax_b.text(ex + 0.55, enc_y - 0.38, 'LN', fontsize=7, color='white',
              fontweight='bold', ha='center', va='center',
              bbox=dict(boxstyle='round,pad=0.12', facecolor=C['orange'],
                        edgecolor=C['orange'], lw=0.8), zorder=5)

# Arrows: obs → encoders
draw_arrow(ax_b, (4.2, 1.0), (2.3, enc_y), color=C['enc_edge'], lw=1.0)
draw_arrow(ax_b, (5.8, 1.0), (7.7, enc_y), color=C['enc_edge'], lw=1.0)

# LLM Backbone
llm_y = 3.7
draw_box(ax_b, (2.0, llm_y), 6.0, 1.0, 'LLM Backbone', sublabel='Llama-2 7B',
         fill=C['llm_fill'], edge=C['llm_edge'], fontsize=9)
draw_arrow(ax_b, (2.3, enc_y + 1.0), (3.8, llm_y), color='#666', lw=1.0)
draw_arrow(ax_b, (7.7, enc_y + 1.0), (6.2, llm_y), color='#666', lw=1.0)
ax_b.text(5.0, llm_y - 0.28, 'project + concat', fontsize=6, ha='center',
          color=C['subtle'], style='italic')

# --- Fork ---
head_y = 5.6

# Action Head (main path, solid)
draw_box(ax_b, (0.4, head_y), 3.6, 0.95, 'Action Head', sublabel='7-DoF tokens',
         fill=C['act_fill'], edge=C['act_edge'], fontsize=8.5)
draw_arrow(ax_b, (3.5, llm_y + 1.0), (2.2, head_y), color=C['act_edge'], lw=2.0)
ax_b.text(1.5, head_y - 0.32, 'main path', fontsize=6, ha='center',
          color=C['act_edge'], fontweight='bold', style='italic')
ax_b.text(2.2, head_y + 1.4, r'$\mathcal{L}_{\mathrm{action}}$', fontsize=11,
          ha='center', color=C['act_edge'], fontweight='bold')
draw_arrow(ax_b, (2.2, head_y + 1.22), (2.2, head_y + 0.95), color=C['act_edge'], lw=1.0)

# Aux Head (auxiliary path, dashed)
draw_box(ax_b, (6.0, head_y), 3.4, 0.95, 'Aux OCC Head', sublabel='BEV occupancy',
         fill=C['aux_fill'], edge=C['aux_edge'], fontsize=8.5)
draw_arrow(ax_b, (6.5, llm_y + 1.0), (7.7, head_y), color=C['aux_edge'], lw=1.5,
           linestyle='--')
ax_b.text(8.6, head_y - 0.32, 'auxiliary', fontsize=6, ha='center',
          color=C['aux_edge'], fontweight='bold', style='italic')

# L_aux
ax_b.text(7.7, head_y + 1.55, r'$\lambda(t) \cdot \mathcal{L}_{\mathrm{aux}}$', fontsize=11,
          ha='center', color=C['aux_edge'], fontweight='bold')
draw_arrow(ax_b, (7.7, head_y + 1.37), (7.7, head_y + 0.95), color=C['aux_edge'], lw=1.0)

# Gradient flow path (right margin, dashed blue)
gf_x = 9.35
ax_b.annotate('', xy=(gf_x, llm_y + 1.0), xytext=(gf_x, head_y + 0.1),
              arrowprops=dict(arrowstyle='->', color=C['blue'],
                              lw=1.3, linestyle=(0, (3, 2))), zorder=2)
ax_b.annotate('', xy=(gf_x, enc_y + 1.0), xytext=(gf_x, llm_y + 0.1),
              arrowprops=dict(arrowstyle='->', color=C['blue'],
                              lw=1.3, linestyle=(0, (3, 2))), zorder=2)
ax_b.text(gf_x - 0.2, (llm_y + head_y) / 2, 'grad.\nflow', fontsize=6.5,
          ha='right', va='center', color=C['blue'], fontweight='bold',
          style='italic', linespacing=1.2)

# "Discarded at inference" + "Zero cost" (above aux head)
ax_b.text(7.7, 8.4, 'Discarded at inference', fontsize=7,
          ha='center', color=C['subtle'], style='italic',
          bbox=dict(boxstyle='round,pad=0.15', facecolor='#FFF8E1',
                    edgecolor='#D4C48A', lw=0.6, alpha=0.9))
ax_b.text(7.7, 8.0, 'Zero cost at test time', fontsize=6.5,
          ha='center', color=C['green'], fontweight='bold')

# ============================================================
# PANEL (c): "Key Finding" — Dual Main Effects (no interaction)
# ============================================================
ax_c.set_xlim(-0.55, 1.55)
ax_c.set_ylim(0.700, 0.830)

# Panel label
fig.text(0.74, 0.93, '(c)', fontsize=11, fontweight='bold', va='top', color=C['text'])
fig.text(0.77, 0.93, 'Key Finding', fontsize=10.5, fontweight='bold', va='top',
         color=C['text'])

# Data — v2 full factorial (all cells n>=3)
x_pos = [0, 1]
bn_means = [0.767, 0.725]    # [Grad OFF (Cell 3), Grad ON (Cell 1)]
ln_means = [0.802, 0.773]    # [Grad OFF (Cell 4), Grad ON (Cell 2)]
bn_sds   = [0.024, 0.064]    # cross-seed SD
ln_sds   = [0.024, 0.027]
vanilla_val = 0.745

# Vanilla baseline
ax_c.axhline(y=vanilla_val, color=C['gray'], linestyle='--', lw=0.9, zorder=1, alpha=0.55)
ax_c.text(1.43, vanilla_val + 0.002, 'Vanilla\n0.745', fontsize=6.5,
          color=C['gray'], va='bottom', ha='right', style='italic',
          linespacing=1.2)

# BN line (blue) — gradient flow hurts
ax_c.errorbar(x_pos, bn_means, yerr=bn_sds, color=C['blue'], lw=2.5,
              marker='o', markersize=8, markeredgecolor='white', markeredgewidth=1.8,
              capsize=4, capthick=1.2, elinewidth=1.2, zorder=5, label='BatchNorm (BN)')
ax_c.text(-0.12, bn_means[0] + 0.004, f'{bn_means[0]:.3f}', fontsize=8,
          color=C['blue'], ha='right', va='bottom', fontweight='bold')
ax_c.text(1.12, bn_means[1] - 0.005, f'{bn_means[1]:.3f}', fontsize=8,
          color=C['blue'], ha='left', va='top', fontweight='bold')

# LN line (orange) — gradient flow slightly hurts but stays above Vanilla
ax_c.errorbar(x_pos, ln_means, yerr=ln_sds, color=C['orange'], lw=2.5,
              marker='s', markersize=8, markeredgecolor='white', markeredgewidth=1.8,
              capsize=4, capthick=1.2, elinewidth=1.2, zorder=5, label='LayerNorm (LN)')
ax_c.text(-0.12, ln_means[0] + 0.004, f'{ln_means[0]:.3f}', fontsize=8,
          color=C['orange'], ha='right', va='bottom', fontweight='bold')
ax_c.text(1.12, ln_means[1] + 0.004, f'{ln_means[1]:.3f}', fontsize=8,
          color=C['orange'], ha='left', va='bottom', fontweight='bold')

# Axis styling
ax_c.set_xticks([0, 1])
ax_c.set_xticklabels(['Gradient OFF', 'Gradient ON'], fontsize=8.5, fontweight='bold')
ax_c.set_ylabel('Collision-Aware Rate (CAR)', fontsize=9, labelpad=6)
ax_c.set_yticks([0.720, 0.740, 0.760, 0.780, 0.800, 0.820])
ax_c.set_yticklabels(['.720', '.740', '.760', '.780', '.800', '.820'], fontsize=7.5)
ax_c.spines['top'].set_visible(False)
ax_c.spines['right'].set_visible(False)
ax_c.spines['left'].set_color('#BDC3C7')
ax_c.spines['bottom'].set_color('#BDC3C7')
ax_c.tick_params(colors='#7F8C8D', length=3)

# Interaction p-value (null — additive model)
ax_c.text(0.5, 0.705, 'Interaction: $p = 0.763$ (n.s.)', fontsize=8,
          ha='center', color=C['text'], fontweight='bold',
          bbox=dict(boxstyle='round,pad=0.15', facecolor='#FFF8E1',
                    edgecolor='#E8D5A0', lw=0.6))

# Legend
legend = ax_c.legend(loc='upper left', fontsize=7.5, frameon=True,
                      framealpha=0.95, edgecolor='#DEE2E6',
                      handlelength=1.5, handletextpad=0.5,
                      borderpad=0.4, labelspacing=0.3)
legend.get_frame().set_linewidth(0.6)

# Insight text below panel
fig.text(0.865, 0.025, 'Gradient flow and norm type act additively — LN consistently safer, gradient OFF consistently safer',
         fontsize=6.5, ha='center', va='bottom', color=C['subtle'], style='italic')

# ============================================================
# Save
# ============================================================
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts'
fig_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'
for d in [out_dir, fig_dir]:
    fig.savefig(f'{d}/fig1_overview_v2.png', dpi=300, bbox_inches='tight',
                pad_inches=0.06, facecolor='white')
    fig.savefig(f'{d}/fig1_overview_v2.pdf', dpi=300, bbox_inches='tight',
                pad_inches=0.06, facecolor='white')
fig.savefig(f'{fig_dir}/fig1_overview.pdf', dpi=300, bbox_inches='tight',
            pad_inches=0.06, facecolor='white')
plt.close()
print("Saved fig1_overview_v2 to artifacts and figures, plus fig1_overview.pdf")
