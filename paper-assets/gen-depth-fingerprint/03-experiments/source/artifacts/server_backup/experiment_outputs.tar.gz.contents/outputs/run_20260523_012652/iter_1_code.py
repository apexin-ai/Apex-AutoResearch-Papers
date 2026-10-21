import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Define the output path
OUTPUT_PATH = 'academic_framework_figure.png'

# Create the figure and subplots
fig, axs = plt.subplots(1, 3, figsize=(16, 6), dpi=300, gridspec_kw={'width_ratios': [0.35, 0.35, 0.30]})

# Set up each axis
for ax in axs:
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

# Panel (a) Recursive Generation Chain
ax = axs[0]
ax.text(0.5, 0.95, '(a) Recursive Generation Chain', fontsize=13, fontweight='bold', ha='center', transform=ax.transAxes)

# Human Text (gen-0)
ax.add_patch(FancyBboxPatch((0.3, 0.82), 0.4, 0.08, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor='#B3D9FF', transform=ax.transAxes))
ax.text(0.3, 0.85, 'd=0', fontsize=8, color='gray', ha='right', transform=ax.transAxes)
ax.text(0.5, 0.86, 'Human Text (gen-0)', fontsize=8, ha='center', transform=ax.transAxes)

# Generator G
ax.add_patch(FancyBboxPatch((0.3, 0.65), 0.4, 0.08, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor='#E8E8E8', transform=ax.transAxes))
ax.text(0.5, 0.68, 'Generator G', fontsize=9, ha='center', transform=ax.transAxes)
ax.text(0.5, 0.63, '8 LLMs | 5 families | 0.6B–8B', fontsize=7, ha='center', style='italic', transform=ax.transAxes)

# gen-1
ax.add_patch(FancyBboxPatch((0.3, 0.49), 0.4, 0.08, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor='#4DA6FF', transform=ax.transAxes))
ax.text(0.3, 0.52, 'd=1', fontsize=8, color='gray', ha='right', transform=ax.transAxes)
ax.text(0.5, 0.52, 'gen-1', fontsize=9, ha='center', transform=ax.transAxes)

# Arrow from gen-1 to Generator G
ax.add_patch(FancyArrowPatch((0.5, 0.49), (0.5, 0.65), connectionstyle="arc3,rad=0.3", arrowstyle='->', color='#555555', linewidth=1.0, transform=ax.transAxes))

# gen-2
ax.add_patch(FancyBboxPatch((0.3, 0.29), 0.4, 0.08, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor='#0066CC', transform=ax.transAxes))
ax.text(0.3, 0.32, 'd=2+', fontsize=8, color='gray', ha='right', transform=ax.transAxes)
ax.text(0.5, 0.32, 'gen-2', fontsize=9, ha='center', color='white', transform=ax.transAxes)

# Dashed text
ax.text(0.5, 0.18, 'gen-3, gen-4...', fontsize=8, color='lightgray', ha='center', transform=ax.transAxes)

# Math formula
ax.text(0.5, 0.05, '$x^{(k)} = G(x^{(k-1)})$', fontsize=9, ha='center', transform=ax.transAxes)

# Panel (b) Feature Extraction
ax = axs[1]
ax.text(0.5, 0.95, '(b) Feature Extraction', fontsize=13, fontweight='bold', ha='center', transform=ax.transAxes)

# Input Text
ax.add_patch(FancyBboxPatch((0.4, 0.82), 0.2, 0.05, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor='#FFFFFF', transform=ax.transAxes))
ax.text(0.5, 0.85, 'Input Text', fontsize=8, ha='center', transform=ax.transAxes)

# Arrow to Pythia-410M
ax.add_patch(FancyArrowPatch((0.5, 0.77), (0.5, 0.72), arrowstyle='->', color='#555555', linewidth=1.0, transform=ax.transAxes))

# Pythia-410M
ax.add_patch(FancyBboxPatch((0.3, 0.65), 0.4, 0.06, boxstyle="round,pad=0.02", linewidth=1.0, edgecolor='#008080', facecolor='#FFFFFF', transform=ax.transAxes))
ax.text(0.5, 0.67, 'Pythia-410M', fontsize=9, ha='center', transform=ax.transAxes)
ax.text(0.5, 0.63, '(Reference Model)', fontsize=7, ha='center', style='italic', transform=ax.transAxes)

# Arrow to NLL Distribution
ax.add_patch(FancyArrowPatch((0.5, 0.62), (0.5, 0.55), arrowstyle='->', color='#555555', linewidth=1.0, transform=ax.transAxes))

# NLL Distribution
ax.text(0.5, 0.48, 'NLL Distribution', fontsize=7.5, ha='center', transform=ax.transAxes)

# NLL Statistics and Surface
ax.add_patch(FancyBboxPatch((0.15, 0.35), 0.3, 0.15, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor='#2E8B57', transform=ax.transAxes))
ax.text(0.3, 0.47, 'NLL Statistics', fontsize=8, ha='center', color='white', transform=ax.transAxes)
nll_stats = ['entropy_mean', 'entropy_std', 'entropy_max', 'entropy_min', 'tail_decay']
for i, stat in enumerate(nll_stats):
    ax.text(0.3, 0.46 - i * 0.03, stat, fontsize=7, ha='center', color='white', transform=ax.transAxes)

ax.add_patch(FancyBboxPatch((0.55, 0.35), 0.3, 0.15, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor='#20B2AA', transform=ax.transAxes))
ax.text(0.7, 0.47, 'Surface', fontsize=8, ha='center', color='white', transform=ax.transAxes)
surface_stats = ['TTR', 'hapax_ratio']
for i, stat in enumerate(surface_stats):
    ax.text(0.7, 0.46 - i * 0.03, stat, fontsize=7, ha='center', color='white', transform=ax.transAxes)

# Arrow to DDR Features
ax.add_patch(FancyArrowPatch((0.3, 0.32), (0.5, 0.12), arrowstyle='->', color='#555555', linewidth=1.0, transform=ax.transAxes))
ax.add_patch(FancyArrowPatch((0.7, 0.32), (0.5, 0.12), arrowstyle='->', color='#555555', linewidth=1.0, transform=ax.transAxes))

# DDR Features
ax.add_patch(FancyBboxPatch((0.35, 0.05), 0.3, 0.06, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor='#006400', transform=ax.transAxes))
ax.text(0.5, 0.07, '7 DDR Features', fontsize=9, ha='center', color='white', transform=ax.transAxes)

# Panel (c) LOGO Evaluation
ax = axs[2]
ax.text(0.5, 0.95, '(c) LOGO Evaluation', fontsize=13, fontweight='bold', ha='center', transform=ax.transAxes)

# 2x4 Grid of Models
models = ['Pythia-2.8B', 'Pythia-1B', 'OLMo-2-1B', 'Qwen3-1.7B', 'Qwen3-0.6B', 'Qwen3-8B', 'Llama-3.2-3B', 'Mistral-7B']
colors = ['#4DA6FF'] * 7 + ['#E8712B']
for i, (model, color) in enumerate(zip(models, colors)):
    x = 0.15 + (i % 4) * 0.2
    y = 0.75 - (i // 4) * 0.1
    ax.add_patch(FancyBboxPatch((x, y), 0.15, 0.08, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor=color, transform=ax.transAxes))
    ax.text(x + 0.075, y + 0.04, model, fontsize=7, ha='center', color='white' if color == '#E8712B' else 'black', transform=ax.transAxes)

# Label below grid
ax.text(0.5, 0.58, '← train (7)     test (1) →', fontsize=8, ha='center', transform=ax.transAxes)

# Arrow to XGBoost Classifier
ax.add_patch(FancyArrowPatch((0.5, 0.58), (0.5, 0.35), arrowstyle='->', color='#555555', linewidth=1.0, transform=ax.transAxes))

# XGBoost Classifier
ax.add_patch(FancyBboxPatch((0.3, 0.28), 0.4, 0.08, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor='#FFF3CD', transform=ax.transAxes))
ax.text(0.5, 0.32, 'XGBoost Classifier', fontsize=9, ha='center', transform=ax.transAxes)

# Arrow to generations
ax.add_patch(FancyArrowPatch((0.5, 0.28), (0.5, 0.12), arrowstyle='->', color='#555555', linewidth=1.0, transform=ax.transAxes))

# Generations
gens = ['gen-0', 'gen-1', 'gen-2+']
colors = ['#B3D9FF', '#4DA6FF', '#0066CC']
for i, (gen, color) in enumerate(zip(gens, colors)):
    ax.add_patch(FancyBboxPatch((0.2 + i * 0.2, 0.05), 0.15, 0.06, boxstyle="round,pad=0.02", linewidth=0.8, edgecolor='#888888', facecolor=color, transform=ax.transAxes))
    ax.text(0.275 + i * 0.2, 0.07, gen, fontsize=8, ha='center', color='white' if color == '#0066CC' else 'black', transform=ax.transAxes)

# Leave-One-Generator-Out
ax.text(0.5, 0.02, 'Leave-One-Generator-Out', fontsize=7.5, ha='center', style='italic', transform=ax.transAxes)

# Adjust layout
fig.tight_layout(pad=1.0)

# Save the figure
fig.savefig(OUTPUT_PATH, bbox_inches='tight', transparent=False)