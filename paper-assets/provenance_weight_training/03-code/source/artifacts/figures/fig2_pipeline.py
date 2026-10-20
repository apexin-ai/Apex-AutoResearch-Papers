"""Figure 2: Detect-and-reweight pipeline concept diagram.
Replaces PaperBanana version with matplotlib for readability at column width.
4 large modules, title-level text only, no small print.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(7.5, 2.0))
ax.set_xlim(0, 11.2)
ax.set_ylim(0, 2.0)
ax.axis('off')

# Colors
C_corpus   = '#F5E6D3'  # warm beige
C_detector = '#D6EAF8'  # light blue
C_optim    = '#D5F5E3'  # light green
C_model    = '#FDEBD0'  # light orange
C_border_corpus   = '#B8860B'
C_border_detector = '#2980B9'
C_border_optim    = '#27AE60'
C_border_model    = '#E67E22'
C_arrow    = '#555555'
C_text     = '#2C3E50'

# Box params
box_h = 1.4
box_y = 0.3
rounding = 0.12
lw = 1.2

boxes = [
    (0.15, 2.0,  C_corpus,   C_border_corpus,   'Training\nCorpus',        r'$\rho$ contaminated'),
    (3.0,  2.0,  C_detector, C_border_detector,  'TF-IDF + LR\nDetector',   r'$q(x) \in [0,1]$'),
    (5.85, 2.5,  C_optim,    C_border_optim,     'Constrained\nOptimization', r'$w(x)=(1{-}q)^{b^*}$'),
    (9.2,  1.75, C_model,    C_border_model,     'Weighted\nLM Training',   r'$\downarrow$ PPL'),
]

for x, w, fc, ec, title, sub in boxes:
    fancy = mpatches.FancyBboxPatch(
        (x, box_y), w, box_h,
        boxstyle=f'round,pad=0.08,rounding_size={rounding}',
        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2
    )
    ax.add_patch(fancy)
    cx = x + w / 2
    cy = box_y + box_h / 2
    ax.text(cx, cy + 0.18, title, ha='center', va='center',
            fontsize=10, fontweight='bold', color=C_text,
            fontfamily='serif', linespacing=1.15, zorder=3)
    ax.text(cx, cy - 0.38, sub, ha='center', va='center',
            fontsize=8.5, color='#666666', fontstyle='italic',
            fontfamily='serif', zorder=3)

# Arrows between boxes
arrow_kw = dict(
    arrowstyle='->', color=C_arrow, lw=1.5,
    connectionstyle='arc3,rad=0', mutation_scale=14,
    shrinkA=3, shrinkB=3
)

arrow_pairs = [
    (0.15 + 2.0, 3.0),            # corpus → detector
    (3.0 + 2.0, 5.85),            # detector → optim
    (5.85 + 2.5, 9.2),            # optim → model
]

mid_y = box_y + box_h / 2
for x_end_box, x_start_next in arrow_pairs:
    gap_mid = (x_end_box + x_start_next) / 2
    ax.annotate('', xy=(x_start_next + 0.02, mid_y),
                xytext=(x_end_box - 0.02, mid_y),
                arrowprops=arrow_kw, zorder=1)


fig.savefig('/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/figures/dr_pipeline_concept.png',
            dpi=300, bbox_inches='tight', pad_inches=0.05, facecolor='white')
fig.savefig('/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/figures/dr_pipeline_concept.pdf',
            dpi=300, bbox_inches='tight', pad_inches=0.05, facecolor='white')
plt.close(fig)
print('✓ dr_pipeline_concept (pipeline diagram)')
