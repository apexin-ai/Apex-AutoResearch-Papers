import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.text as mtext

# Define colors
gen0_blue = '#B3D9FF'
gen1_blue = '#4DA6FF'
gen2_blue = '#0066CC'
teal_dark = '#2E8B57'
teal_light = '#A8DBC5'
orange_held = '#E8712B'
gray_box = '#F0F0F0'
yellow_box = '#FFF3CD'

# Create figure and axes
fig, axes = plt.subplots(1, 3, figsize=(16, 5.5), gridspec_kw={'width_ratios': [0.35, 0.35, 0.30], 'wspace': 0.15})
for ax in axes:
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

# Panel (a)
ax = axes[0]
ax.text(0.5, 0.97, '(a) Recursive Generation Chain', ha='center', fontsize=10, transform=ax.transAxes)

# Human Text (gen-0)
ax.add_patch(patches.FancyBboxPatch((0.5-0.55/2, 0.88-0.07/2), 0.55, 0.07, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor=gen0_blue, edgecolor='none'))
ax.text(0.5, 0.88, 'Human Text (gen-0)', ha='center', va='center', fontsize=9, transform=ax.transAxes)
ax.text(0.08, 0.88, 'd=0', fontsize=8, color='gray', ha='center', transform=ax.transAxes)

# Generator G
ax.add_patch(patches.FancyBboxPatch((0.5-0.55/2, 0.72-0.09/2), 0.55, 0.09, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor=gray_box, edgecolor='none'))
ax.text(0.5, 0.72, 'Generator G', ha='center', va='center', fontsize=10, fontweight='bold', transform=ax.transAxes)
ax.text(0.5, 0.665, '8 LLMs | 5 families | 0.6B–8B', ha='center', va='center', fontsize=7, color='#666666', 
        fontstyle='italic', transform=ax.transAxes)

# Arrow from Human Text to Generator G
ax.add_patch(patches.FancyArrowPatch((0.5, 0.845), (0.5, 0.77), arrowstyle='->', mutation_scale=12, lw=1.2, 
                                     color='#555', transform=ax.transAxes))

# gen-1
ax.add_patch(patches.FancyBboxPatch((0.5-0.45/2, 0.53-0.07/2), 0.45, 0.07, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor=gen1_blue, edgecolor='none'))
ax.text(0.5, 0.53, 'gen-1', ha='center', va='center', fontsize=9, transform=ax.transAxes)
ax.text(0.08, 0.53, 'd=1', fontsize=8, color='gray', ha='center', transform=ax.transAxes)

# Arrow from Generator G to gen-1
ax.add_patch(patches.FancyArrowPatch((0.5, 0.63), (0.5, 0.57), arrowstyle='->', mutation_scale=12, lw=1.2, 
                                     color='#555', transform=ax.transAxes))

# Loop arrow from gen-1 to Generator G
ax.add_patch(patches.FancyArrowPatch((0.75, 0.53), (0.75, 0.72), arrowstyle='->', mutation_scale=12, lw=1.0, 
                                     color='#555', connectionstyle='arc3,rad=-0.4', transform=ax.transAxes))

# gen-2
ax.add_patch(patches.FancyBboxPatch((0.5-0.45/2, 0.35-0.07/2), 0.45, 0.07, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor=gen2_blue, edgecolor='none'))
ax.text(0.5, 0.35, 'gen-2', ha='center', va='center', fontsize=9, color='white', transform=ax.transAxes)
ax.text(0.08, 0.35, 'd=2+', fontsize=8, color='gray', ha='center', transform=ax.transAxes)

# Arrow from gen-1 to gen-2
ax.add_patch(patches.FancyArrowPatch((0.5, 0.48), (0.5, 0.38), arrowstyle='->', mutation_scale=12, lw=1.2, 
                                     color='#555', transform=ax.transAxes))

# Text for further generations
ax.text(0.5, 0.22, 'gen-3, gen-4...', ha='center', fontsize=8, color='#BBBBBB', fontstyle='italic', transform=ax.transAxes)

# Equation text
ax.text(0.5, 0.08, '$x^{(k)} = G(x^{(k-1)})$', ha='center', fontsize=10, transform=ax.transAxes)

# Panel (b)
ax = axes[1]
ax.text(0.5, 0.97, '(b) Feature Extraction', ha='center', fontsize=10, transform=ax.transAxes)

# Input Text
ax.add_patch(patches.FancyBboxPatch((0.5-0.35/2, 0.88-0.06/2), 0.35, 0.06, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor='white', edgecolor='#888'))
ax.text(0.5, 0.88, 'Input Text', ha='center', va='center', fontsize=9, transform=ax.transAxes)

# Arrow from Input Text to Pythia-410M
ax.add_patch(patches.FancyArrowPatch((0.5, 0.85), (0.5, 0.78), arrowstyle='->', mutation_scale=12, lw=1.0, 
                                     color='#555', transform=ax.transAxes))

# Pythia-410M
ax.add_patch(patches.FancyBboxPatch((0.5-0.55/2, 0.72-0.08/2), 0.55, 0.08, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor='white', edgecolor=teal_dark, lw=1.5))
ax.text(0.5, 0.72, 'Pythia-410M', ha='center', va='center', fontsize=9, transform=ax.transAxes)
ax.text(0.5, 0.67, '(Reference Model)', ha='center', fontsize=7, color='#666', transform=ax.transAxes)

# Arrow from Pythia-410M to NLL Distribution
ax.add_patch(patches.FancyArrowPatch((0.5, 0.67), (0.5, 0.60), arrowstyle='->', mutation_scale=12, lw=1.0, 
                                     color='#555', transform=ax.transAxes))

# NLL Distribution
ax.text(0.5, 0.57, 'NLL Distribution', ha='center', fontsize=8, fontstyle='italic', transform=ax.transAxes)

# NLL Statistics Group
ax.add_patch(patches.FancyBboxPatch((0.3-0.38/2, 0.40-0.22/2), 0.38, 0.22, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor=teal_light, alpha=0.3, edgecolor='none'))
ax.text(0.3, 0.51, 'NLL Statistics', ha='center', fontsize=8, fontweight='bold', color=teal_dark, transform=ax.transAxes)
nll_stats = ['entropy_mean', 'entropy_std', 'entropy_max', 'entropy_min', 'tail_decay']
for i, stat in enumerate(nll_stats):
    ax.text(0.3, 0.47 - i*0.03, stat, ha='center', fontsize=7, family='monospace', transform=ax.transAxes)

# Surface Group
ax.add_patch(patches.FancyBboxPatch((0.75-0.28/2, 0.43-0.14/2), 0.28, 0.14, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor='#E0F0E0', edgecolor='none'))
ax.text(0.75, 0.50, 'Surface', ha='center', fontsize=8, fontweight='bold', transform=ax.transAxes)
surface_items = ['TTR', 'hapax_ratio']
for i, item in enumerate(surface_items):
    ax.text(0.75, 0.46 - i*0.03, item, ha='center', fontsize=7, family='monospace', transform=ax.transAxes)

# Arrows from NLL Statistics and Surface to DDR Features
ax.add_patch(patches.FancyArrowPatch((0.3, 0.29), (0.5, 0.17), arrowstyle='->', mutation_scale=12, lw=1.0, 
                                     color='#555', transform=ax.transAxes))
ax.add_patch(patches.FancyArrowPatch((0.75, 0.36), (0.5, 0.17), arrowstyle='->', mutation_scale=12, lw=1.0, 
                                     color='#555', transform=ax.transAxes))

# DDR Features
ax.add_patch(patches.FancyBboxPatch((0.5-0.55/2, 0.10-0.07/2), 0.55, 0.07, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor=teal_dark, edgecolor='none'))
ax.text(0.5, 0.10, '7 DDR Features', ha='center', va='center', fontsize=9, color='white', fontweight='bold', transform=ax.transAxes)

# Panel (c)
ax = axes[2]
ax.text(0.5, 0.97, '(c) LOGO Evaluation', ha='center', fontsize=10, transform=ax.transAxes)

# Generator boxes grid
gen_boxes = [
    ('Pythia-2.8B', gen1_blue), ('Pythia-1B', gen1_blue), ('OLMo-2-1B', gen1_blue), ('Qwen3-1.7B', gen1_blue),
    ('Qwen3-0.6B', gen1_blue), ('Qwen3-8B', gen1_blue), ('Llama-3.2-3B', gen1_blue), ('Mistral-7B', orange_held)
]
x_positions = [0.12, 0.33, 0.54, 0.75]
y_positions = [0.84, 0.72]
for i, (label, color) in enumerate(gen_boxes):
    x = x_positions[i % 4]
    y = y_positions[i // 4]
    ax.add_patch(patches.FancyBboxPatch((x-0.19/2, y-0.08/2), 0.19, 0.08, boxstyle='round,pad=0.02', 
                                        transform=ax.transAxes, facecolor=color, edgecolor='none'))
    ax.text(x, y, label, ha='center', va='center', fontsize=6.5, transform=ax.transAxes)

# Train-test text
ax.text(0.5, 0.62, '← train (7)          test (1) →', ha='center', fontsize=7, color='#888', transform=ax.transAxes)

# Arrow to XGBoost Classifier
ax.add_patch(patches.FancyArrowPatch((0.5, 0.59), (0.5, 0.48), arrowstyle='->', mutation_scale=12, lw=1.0, 
                                     color='#555', transform=ax.transAxes))

# XGBoost Classifier
ax.add_patch(patches.FancyBboxPatch((0.5-0.55/2, 0.42-0.08/2), 0.55, 0.08, boxstyle='round,pad=0.02', 
                                    transform=ax.transAxes, facecolor=yellow_box, edgecolor='none'))
ax.text(0.5, 0.42, 'XGBoost Classifier', ha='center', va='center', fontsize=9, transform=ax.transAxes)

# Arrow to generation types
ax.add_patch(patches.FancyArrowPatch((0.5, 0.37), (0.5, 0.27), arrowstyle='->', mutation_scale=12, lw=1.0, 
                                     color='#555', transform=ax.transAxes))

# Generation types
gen_types = [('gen-0', gen0_blue), ('gen-1', gen1_blue), ('gen-2+', gen2_blue)]
x_positions = [0.2, 0.5, 0.8]
for i, (label, color) in enumerate(gen_types):
    x = x_positions[i]
    ax.add_patch(patches.FancyBboxPatch((x-0.18/2, 0.20-0.07/2), 0.18, 0.07, boxstyle='round,pad=0.02', 
                                        transform=ax.transAxes, facecolor=color, edgecolor='none'))
    ax.text(x, 0.20, label, ha='center', va='center', fontsize=9, color='white' if color == gen2_blue else 'black', 
            transform=ax.transAxes)

# Leave-One-Generator-Out text
ax.text(0.5, 0.08, 'Leave-One-Generator-Out', ha='center', fontsize=8, fontstyle='italic', color='#666', transform=ax.transAxes)

# Save figure
fig.patch.set_facecolor('white')
plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', pad_inches=0.1, facecolor='white')