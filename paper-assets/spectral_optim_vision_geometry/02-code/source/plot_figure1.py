"""Figure 1: Two-panel teaser — framework diagram + spectral gap lollipop."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
import os

from plot_style import COLORS, apply_style

apply_style()

# Override for this figure: serif font, NeurIPS-quality
plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm',
    'font.size': 9,
    'axes.linewidth': 0.6,
})

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(13, 4.8),
                                  gridspec_kw={'width_ratios': [1.15, 1],
                                               'wspace': 0.32})

# ============================================================
# Panel (a): Framework + Mechanism Pathway
# ============================================================
ax_a.set_xlim(0, 10)
ax_a.set_ylim(0, 7.5)
ax_a.axis('off')
ax_a.set_title('(a) Experimental Framework', fontsize=11, fontweight='bold',
               loc='left', pad=8)

# --- Architecture boxes ---
arch_specs = [
    {'name': 'ResNet-50',   'norm': 'BatchNorm',  'x': 0.8, 'y': 4.4, 'w': 2.4, 'h': 2.2},
    {'name': 'DeiT-S',      'norm': 'LayerNorm',  'x': 3.8, 'y': 4.4, 'w': 2.4, 'h': 2.2},
    {'name': 'ConvNeXt-T',  'norm': 'LayerNorm',  'x': 6.8, 'y': 4.4, 'w': 2.4, 'h': 2.2},
]

for spec in arch_specs:
    box = FancyBboxPatch((spec['x'], spec['y']), spec['w'], spec['h'],
                         boxstyle='round,pad=0.15', linewidth=1.0,
                         edgecolor='#333333', facecolor='#F7F7F7')
    ax_a.add_patch(box)
    cx = spec['x'] + spec['w'] / 2
    ax_a.text(cx, spec['y'] + spec['h'] - 0.5, spec['name'],
              ha='center', va='center', fontsize=10, fontweight='bold',
              color='#222222')
    # norm badge
    norm_color = '#D4E8F0' if spec['norm'] == 'BatchNorm' else '#E0D4F0'
    badge = FancyBboxPatch((cx - 0.85, spec['y'] + 0.35), 1.7, 0.7,
                           boxstyle='round,pad=0.08', linewidth=0.6,
                           edgecolor='#888888', facecolor=norm_color)
    ax_a.add_patch(badge)
    ax_a.text(cx, spec['y'] + 0.7, spec['norm'],
              ha='center', va='center', fontsize=8, color='#333333')

# --- Optimizer families boxes ---
# Spectral family (blue-green background)
spec_box = FancyBboxPatch((0.5, 2.3), 4.2, 1.4,
                          boxstyle='round,pad=0.12', linewidth=0.8,
                          edgecolor=COLORS['Muon'], facecolor='#E8F4F8',
                          linestyle='-')
ax_a.add_patch(spec_box)
ax_a.text(2.6, 3.3, 'Spectral Optimizers', ha='center', va='center',
          fontsize=9, fontweight='bold', color=COLORS['Muon'])
optim_labels_spec = [('Muon', COLORS['Muon']), ('SOAP', COLORS['SOAP']),
                     ('Shampoo', COLORS['Shampoo'])]
for i, (name, color) in enumerate(optim_labels_spec):
    ax_a.text(1.0 + i * 1.5, 2.65, name, ha='center', va='center',
              fontsize=8, color=color, fontweight='bold')

# First-order family (orange-red background)
fo_box = FancyBboxPatch((5.3, 2.3), 4.0, 1.4,
                        boxstyle='round,pad=0.12', linewidth=0.8,
                        edgecolor=COLORS['AdamW'], facecolor='#FFF3E8',
                        linestyle='-')
ax_a.add_patch(fo_box)
ax_a.text(7.3, 3.3, 'First-Order Baselines', ha='center', va='center',
          fontsize=9, fontweight='bold', color='#AA5522')
optim_labels_fo = [('AdamW', COLORS['AdamW']), ('SGD', COLORS['SGD'])]
for i, (name, color) in enumerate(optim_labels_fo):
    ax_a.text(6.2 + i * 2.0, 2.65, name, ha='center', va='center',
              fontsize=8, color=color, fontweight='bold')

# --- Causal arrow chain at bottom ---
chain_y = 0.7
chain_labels = ['Normalization\nType', 'Gradient Spectral\nStructure', 'Optimizer\nAdvantage']
chain_x = [1.5, 5.0, 8.5]
chain_colors = ['#555555', '#555555', '#555555']

for i, (cx, label) in enumerate(zip(chain_x, chain_labels)):
    cbox = FancyBboxPatch((cx - 1.2, chain_y - 0.5), 2.4, 1.0,
                          boxstyle='round,pad=0.1', linewidth=0.8,
                          edgecolor='#666666', facecolor='#FAFAFA')
    ax_a.add_patch(cbox)
    ax_a.text(cx, chain_y, label, ha='center', va='center',
              fontsize=8, color='#333333', fontweight='bold')

# Arrows between chain boxes
for i in range(len(chain_x) - 1):
    ax_a.annotate('', xy=(chain_x[i+1] - 1.3, chain_y),
                  xytext=(chain_x[i] + 1.3, chain_y),
                  arrowprops=dict(arrowstyle='->', color='#444444',
                                  lw=1.5, connectionstyle='arc3,rad=0'))

# Downward arrows from architecture boxes to optimizer boxes
for spec in arch_specs:
    cx = spec['x'] + spec['w'] / 2
    ax_a.annotate('', xy=(cx, 3.75),
                  xytext=(cx, spec['y'] - 0.02),
                  arrowprops=dict(arrowstyle='->', color='#999999',
                                  lw=0.8, linestyle='--'))

# ============================================================
# Panel (b): Spectral Gap Lollipop Chart
# ============================================================
ax_b.set_title('(b) Spectral Optimizer Advantage over AdamW', fontsize=11,
               fontweight='bold', loc='left', pad=8)

# Data
archs = ['R50-BN', 'R50-GN32', 'DeiT-LN', 'CNeXt-LN']
gaps = [9.03, 22.47, 10.30, 11.78]
best_spectral = ['Muon', 'Muon', 'Muon', 'Muon']
detail_labels = [
    '76.88 − 67.85',
    '78.20 − 55.73',
    '62.26 − 51.96',
    '78.49 − 66.71',
]
x_pos = np.arange(len(archs))

# Lollipop stems + markers
for i, (x, gap, opt, detail) in enumerate(zip(x_pos, gaps, best_spectral, detail_labels)):
    if gap is None:
        # Placeholder: dashed stem, gray
        ax_b.plot([x, x], [0, 6.0], color='#BBBBBB', lw=1.2, linestyle=':', zorder=1)
        ax_b.scatter(x, 6.0, s=80, color='#CCCCCC', edgecolor='#999999',
                     linewidth=0.8, zorder=3, marker='o')
        ax_b.text(x, 6.5, 'pending', ha='center', va='bottom', fontsize=7.5,
                  color='#999999', fontstyle='italic')
    else:
        color = COLORS.get(opt, '#333333')
        ax_b.plot([x, x], [0, gap], color=color, lw=2.0, zorder=2)
        ax_b.scatter(x, gap, s=100, color=color, edgecolor='white',
                     linewidth=1.0, zorder=4)
        ax_b.text(x, gap + 0.45, f'+{gap:.2f} pp', ha='center', va='bottom',
                  fontsize=9, fontweight='bold', color=color)
        ax_b.text(x, -0.8, detail, ha='center', va='top', fontsize=6.5,
                  color='#777777')

# Axes
ax_b.set_xticks(x_pos)
ax_b.set_xticklabels(archs, fontsize=9)
ax_b.set_ylabel('Spectral Gap (pp)', fontsize=10)
ax_b.set_xlim(-0.6, len(archs) - 0.4)
ax_b.set_ylim(-1.5, 26)

# Clean up
ax_b.spines['top'].set_visible(False)
ax_b.spines['right'].set_visible(False)
ax_b.spines['left'].set_linewidth(0.6)
ax_b.spines['bottom'].set_linewidth(0.6)
ax_b.axhline(y=0, color='#CCCCCC', lw=0.5, zorder=0)

# Light horizontal reference lines
for y in [3, 6, 9, 12, 15, 18, 21, 24]:
    ax_b.axhline(y=y, color='#EEEEEE', lw=0.4, zorder=0)

ax_b.tick_params(axis='both', length=3, width=0.5)

# Norm smoothing arrow annotation at bottom
ax_b.annotate('', xy=(len(archs) - 0.5, -1.3),
              xytext=(-0.5, -1.3),
              arrowprops=dict(arrowstyle='->', color='#888888', lw=1.0))
ax_b.text((len(archs) - 1) / 2, -1.45, 'Increasing norm smoothing →',
          ha='center', va='top', fontsize=7.5, color='#888888', fontstyle='italic')

# ============================================================
# Save
# ============================================================
out_dir = '/root/spectral_optim_vision_geometry/paper/figures'
os.makedirs(out_dir, exist_ok=True)
fig.savefig(os.path.join(out_dir, 'fig1_teaser.pdf'), bbox_inches='tight',
            pad_inches=0.15)
fig.savefig(os.path.join(out_dir, 'fig1_teaser.png'), bbox_inches='tight',
            pad_inches=0.15, dpi=200)
print(f"Saved to {out_dir}/fig1_teaser.pdf and .png")
plt.close()
