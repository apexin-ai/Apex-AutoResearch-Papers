#!/usr/bin/env python3
"""Generate Figure 1: Experiment overview diagram."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(1, 1, figsize=(7, 2.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')

spec_color = '#D6EAF8'
ling_color = '#D5F5E3'
eval_color = '#F2F3F4'
assess_color = '#FDEBD0'

# --- Stage 1: Ambiguity Taxonomy ---
tax_box = FancyBboxPatch((0.2, 0.5), 2.8, 2.2, boxstyle="round,pad=0.1",
                          facecolor='white', edgecolor='black', linewidth=1)
ax.add_patch(tax_box)
ax.text(1.6, 2.55, 'Ambiguity Taxonomy', ha='center', fontsize=8, fontweight='bold')

# Specification layer
spec_box = FancyBboxPatch((0.35, 1.5), 2.5, 0.85, boxstyle="round,pad=0.05",
                           facecolor=spec_color, edgecolor='gray', linewidth=0.5)
ax.add_patch(spec_box)
ax.text(0.45, 2.15, 'Specification', fontsize=6, fontstyle='italic', color='gray')
for i, name in enumerate(['Incomp.', 'Auth.Sc.', 'Cond.Pr.']):
    bx = FancyBboxPatch((0.45 + i*0.82, 1.6), 0.72, 0.4, boxstyle="round,pad=0.02",
                         facecolor='white', edgecolor='#5B9BD5', linewidth=0.5)
    ax.add_patch(bx)
    ax.text(0.45 + i*0.82 + 0.36, 1.8, name, ha='center', fontsize=5.5)

# Linguistic layer
ling_box = FancyBboxPatch((0.35, 0.55), 2.5, 0.85, boxstyle="round,pad=0.05",
                           facecolor=ling_color, edgecolor='gray', linewidth=0.5)
ax.add_patch(ling_box)
ax.text(0.45, 1.2, 'Linguistic', fontsize=6, fontstyle='italic', color='gray')
for i, name in enumerate(['Lexical', 'Scopal', 'Coref.']):
    bx = FancyBboxPatch((0.45 + i*0.82, 0.65), 0.72, 0.4, boxstyle="round,pad=0.02",
                         facecolor='white', edgecolor='#70AD47', linewidth=0.5)
    ax.add_patch(bx)
    ax.text(0.45 + i*0.82 + 0.36, 0.85, name, ha='center', fontsize=5.5)

ax.text(1.6, 0.25, '300 Matched Clause Pairs', ha='center', fontsize=6, fontstyle='italic')

# Arrow 1 → 2
ax.annotate('', xy=(3.5, 1.6), xytext=(3.1, 1.6),
            arrowprops=dict(arrowstyle='->', lw=2, color='gray'))

# --- Stage 2: Evaluation ---
eval_box = FancyBboxPatch((3.6, 0.5), 2.8, 2.2, boxstyle="round,pad=0.1",
                           facecolor=eval_color, edgecolor='black', linewidth=1)
ax.add_patch(eval_box)
ax.text(5.0, 2.55, 'τ²-bench Evaluation', ha='center', fontsize=8, fontweight='bold')
models = ['GPT-5.4', 'GPT-4.1', 'Claude Sonnet', 'Qwen3-235B', 'DeepSeek-V3']
for i, m in enumerate(models):
    ax.text(5.0, 2.1 - i*0.28, m, ha='center', fontsize=6)
ax.text(5.0, 0.65, '2,997 Episodes', ha='center', fontsize=6.5, fontstyle='italic')

# Arrow 2 → 3
ax.annotate('', xy=(6.9, 1.6), xytext=(6.5, 1.6),
            arrowprops=dict(arrowstyle='->', lw=2, color='gray'))

# --- Stage 3: Assessment ---
ass_box = FancyBboxPatch((7.0, 0.5), 2.8, 2.2, boxstyle="round,pad=0.1",
                          facecolor=assess_color, edgecolor='black', linewidth=1)
ax.add_patch(ass_box)
ax.text(8.4, 2.55, 'Cross-Judge Assessment', ha='center', fontsize=8, fontweight='bold')
ax.text(8.4, 2.1, 'Dual-Judge Pipeline', ha='center', fontsize=6.5)

colors_sev = ['#C0392B', '#E67E22', '#F1C40F', '#BDC3C7']
labels_sev = ['critical', 'moderate', 'minor', 'none']
for i, (c, l) in enumerate(zip(colors_sev, labels_sev)):
    y = 1.78 - i*0.27
    rect = plt.Rectangle((7.6, y-0.1), 0.35, 0.2, facecolor=c, edgecolor='gray', lw=0.5)
    ax.add_patch(rect)
    ax.text(8.08, y, l, fontsize=5.5, va='center')

ax.text(8.4, 0.58, 'Violation Classification', ha='center', fontsize=6.5, fontstyle='italic')

plt.tight_layout()
plt.savefig('figures/fig1_overview.pdf', bbox_inches='tight', pad_inches=0.05, dpi=300)
print('Saved figures/fig1_overview.pdf')
