import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# Okabe-Ito inspired palette
C_BLUE_BG = '#DAEAF6'
C_GREEN_BG = '#D5F5E3'
C_S1_GOOD = '#009E73'
C_S2_FAIL = '#D55E00'
C_S3_GRAY = '#888888'
C_S4_WEAK = '#E69F00'
C_FUSION = '#0072B2'
C_IRT = '#56B4E9'
C_OUTPUT = '#CC79A7'
C_INPUT = '#F0E442'
C_ARROW = '#555555'
C_TEXT = '#222222'

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4.5)
ax.axis('off')


def add_box(ax, x, y, w, h, fc, text, fs=9, tc=C_TEXT, bold=False,
            ec='#666666', lw=0.8, alpha=0.92, zorder=3, va_offset=0):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                         facecolor=fc, edgecolor=ec, linewidth=lw,
                         alpha=alpha, zorder=zorder)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    ax.text(x + w / 2, y + h / 2 + va_offset, text,
            ha='center', va='center', fontsize=fs, color=tc,
            weight=weight, zorder=zorder + 1, linespacing=1.2)


def arrow(ax, x1, y1, x2, y2, color=C_ARROW, lw=1.2, style='-|>',
          rad=0.0, zorder=2):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                        color=color, linewidth=lw, mutation_scale=12,
                        connectionstyle=f"arc3,rad={rad}", zorder=zorder)
    ax.add_patch(a)


# ═══════════ Stage backgrounds ═══════════
bg1 = FancyBboxPatch((0.1, 0.1), 4.7, 4.25, boxstyle="round,pad=0.12",
                      facecolor=C_BLUE_BG, edgecolor='#8CB8D8',
                      linewidth=1.5, alpha=0.45, zorder=0)
ax.add_patch(bg1)

bg2 = FancyBboxPatch((5.15, 0.1), 4.75, 4.25, boxstyle="round,pad=0.12",
                      facecolor=C_GREEN_BG, edgecolor='#8CD8A8',
                      linewidth=1.5, alpha=0.45, zorder=0)
ax.add_patch(bg2)

# Stage labels
ax.text(2.45, 4.15, 'Stage 1: Multi-Signal Exposure Mapping',
        ha='center', va='center', fontsize=11, fontweight='bold',
        color='#1A3A5C', zorder=5)
ax.text(7.52, 4.15, 'Stage 2: Contamination-Augmented IRT',
        ha='center', va='center', fontsize=11, fontweight='bold',
        color='#1A5C3A', zorder=5)

# ═══════════ Stage 1: Left half ═══════════

# Input box (left edge)
inp_x, inp_y, inp_w, inp_h = 0.3, 1.85, 1.05, 0.75
add_box(ax, inp_x, inp_y, inp_w, inp_h, C_INPUT,
        'LLM +\nBenchmark\nItems', fs=8.5, bold=True, ec='#B8A800')

# 4 signal boxes (column, right of input)
sig_x = 1.75
sig_w = 2.3
sig_h = 0.52
sigs_data = [
    ('S1: Embedding Similarity\n(AUC > 0.95, reliable)',       C_S1_GOOD, '#006B4F'),
    ('S2: Min-K++\n(AUC ~ 0.47, ⚠ reversal at 0.5B)',         C_S2_FAIL, '#8B3A00'),
    ('S3: ConStat\n(needs paraphrase data)',                    C_S3_GRAY, '#555555'),
    ('S4: Self-Critique\n(AUC ~ 0.50, ineffective)',            C_S4_WEAK, '#946200'),
]

sig_centers_y = []
top_y = 3.55
gap = 0.09
for i, (label, fc, ec) in enumerate(sigs_data):
    sy = top_y - i * (sig_h + gap)
    add_box(ax, sig_x, sy, sig_w, sig_h, fc, label,
            fs=7.5, tc='white', ec=ec, lw=1.0, alpha=0.88)
    sig_centers_y.append(sy + sig_h / 2)

# Arrows: input → each signal
inp_cx = inp_x + inp_w
inp_cy = inp_y + inp_h / 2
for cy in sig_centers_y:
    arrow(ax, inp_cx + 0.02, inp_cy, sig_x - 0.04, cy, lw=0.8,
          style='->', rad=0.0)

# RRF Fusion box (below signals, centered)
fus_x, fus_y, fus_w, fus_h = 2.1, 0.45, 1.6, 0.6
add_box(ax, fus_x, fus_y, fus_w, fus_h, C_FUSION,
        'RRF Fusion → $e_{ij}$', fs=9.5, tc='white',
        bold=True, ec='#004C7F')

# Arrows: signals → fusion (converge)
fus_top_cx = fus_x + fus_w / 2
for cy in sig_centers_y:
    arrow(ax, sig_x + sig_w / 2, cy - sig_h / 2 + 0.01,
          fus_top_cx, fus_y + fus_h, lw=0.7, style='->')

# "Training-free" annotation (bottom-left)
ax.text(0.65, 0.55, 'Training-free\n(avoids meta-circularity)',
        ha='center', va='center', fontsize=7.5, fontstyle='italic',
        color='#005599', zorder=5,
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                  edgecolor='#0072B2', alpha=0.75, linewidth=0.7))

# ═══════════ Connecting arrows Stage1 → Stage2 ═══════════

# e_ij arrow (from fusion to IRT)
irt_x, irt_y, irt_w, irt_h = 5.55, 1.2, 2.55, 2.05
arrow(ax, fus_x + fus_w, fus_y + fus_h / 2,
      irt_x - 0.04, irt_y + 0.5,
      color=C_FUSION, lw=1.6, style='-|>')
ax.text(4.55, 0.98, '$e_{ij}$', fontsize=9.5, color=C_FUSION,
        ha='center', va='center', fontweight='bold', fontstyle='italic', zorder=5)

# y_ij arrow (from input down and across to IRT)
arrow(ax, inp_cx + 0.02, inp_y,
      irt_x - 0.04, irt_y + irt_h - 0.4,
      color='#777777', lw=1.0, style='->', rad=-0.25)
ax.text(3.2, 1.62, '$y_{ij}$ (responses)', fontsize=7.5,
        color='#555555', ha='center', va='center', fontstyle='italic',
        zorder=5, rotation=-8)

# ═══════════ Stage 2: Right half ═══════════

# IRT model box (large)
add_box(ax, irt_x, irt_y, irt_w, irt_h, C_IRT, '',
        ec='#2980B9', lw=1.3, alpha=0.35)

# IRT title
ax.text(irt_x + irt_w / 2, irt_y + irt_h - 0.25,
        'Domain-Level 2PL+γ IRT', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#1A4971', zorder=5)

# IRT equation (2PL+γ primary model)
irt_eq = (r'$P(y\!=\!1) = \frac{1}'
          r'{1 + e^{-a_i(\theta_j - b_i + \gamma_k \cdot e_{ij})}}$')
ax.text(irt_x + irt_w / 2, irt_y + irt_h / 2 + 0.05,
        irt_eq, ha='center', va='center', fontsize=8.5,
        color=C_TEXT, zorder=5)

# "Per-domain fitting" note
ax.text(irt_x + irt_w / 2, irt_y + 0.25,
        'Per-domain fitting within benchmark', ha='center', va='center',
        fontsize=7.5, fontstyle='italic', color='#1A5276', zorder=5)

# Output boxes (right of IRT)
out_x = 8.5
out_w = 1.3
out_h = 0.62
out_gap = 0.18
outputs = [
    'Per-domain\n$\\gamma_k$\n(diagnosis)',
    'Calibrated\n$\\hat{\\theta}_j^{\\mathrm{clean}}$\n(conditional)',
    'Bayesian CIs\n(uncertainty)',
]

out_centers_y = []
out_top = 3.35
for i, label in enumerate(outputs):
    oy = out_top - i * (out_h + out_gap)
    add_box(ax, out_x, oy, out_w, out_h, C_OUTPUT, label,
            fs=7.5, tc='white', ec='#8B4C75', bold=True, lw=1.0)
    out_centers_y.append(oy + out_h / 2)

# Arrows: IRT → outputs
irt_right = irt_x + irt_w
irt_mid_y = irt_y + irt_h / 2
for oy in out_centers_y:
    arrow(ax, irt_right + 0.01, irt_mid_y,
          out_x - 0.04, oy, color='#8B4C75', lw=1.1, style='-|>')

# ═══════════ Save ═══════════
out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig_pipeline.pdf', format='pdf')
fig.savefig(out_dir / 'fig_pipeline.png', format='png')
plt.close(fig)
print('Done: fig_pipeline.pdf + fig_pipeline.png')
