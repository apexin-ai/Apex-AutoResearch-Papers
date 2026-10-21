import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

def create_document_icon(ax, position, label, color, faded=False):
    alpha = 0.6 if faded else 1.0
    ax.add_patch(FancyBboxPatch(position, 0.8, 0.5, boxstyle="round,pad=0.1", 
                                edgecolor='none', facecolor=color, alpha=alpha))
    ax.text(position[0] + 0.4, position[1] + 0.25, label, ha='center', va='center', 
            fontsize=8, color='black', alpha=alpha)

def create_arrow(ax, start, end, style='simple', color='black', linestyle='solid', faded=False):
    alpha = 0.6 if faded else 1.0
    arrow = FancyArrowPatch(start, end, connectionstyle="arc3,rad=0.3", 
                            arrowstyle=style, color=color, linewidth=1.0, 
                            linestyle=linestyle, alpha=alpha)
    ax.add_patch(arrow)

def create_textbox(ax, position, width, height, text, subtitle=None, color='black', bg_color='white'):
    ax.add_patch(FancyBboxPatch(position, width, height, boxstyle="round,pad=0.1", 
                                edgecolor=color, facecolor=bg_color, linewidth=0.8))
    ax.text(position[0] + width / 2, position[1] + height / 2 + (0.1 if subtitle else 0), text, 
            ha='center', va='center', fontsize=8, color=color)
    if subtitle:
        ax.text(position[0] + width / 2, position[1] + height / 2 - 0.1, subtitle, 
                ha='center', va='center', fontsize=6, color=color)

def main():
    fig, ax = plt.subplots(figsize=(6.5, 2.5), dpi=300)
    ax.set_xlim(0, 6.5)
    ax.set_ylim(0, 2.5)
    ax.axis('off')

    # Panel (a) Recursive Generation Chain
    ax.text(0.2, 2.3, '(a) Recursive Generation Chain', fontsize=9, fontweight='bold', ha='left')
    create_document_icon(ax, (0.2, 1.8), 'Human Text (gen-0)', '#B3D9FF')
    create_arrow(ax, (0.6, 1.8), (0.6, 1.5), color='black')
    create_textbox(ax, (0.3, 1.2), 0.6, 0.3, 'Generator G', '8 LLMs | 5 families | 0.6B-8B')
    create_arrow(ax, (0.6, 1.2), (0.6, 0.9), color='black')
    create_document_icon(ax, (0.2, 0.6), 'gen-1', '#4DA6FF')
    create_arrow(ax, (0.6, 0.6), (0.6, 0.3), color='black')
    create_arrow(ax, (0.3, 0.6), (0.3, 1.2), color='black', style='->')
    create_document_icon(ax, (0.2, 0.0), 'gen-2', '#0066CC')
    create_arrow(ax, (0.6, 0.0), (0.6, -0.3), color='black', faded=True, linestyle='dashed')
    create_document_icon(ax, (0.2, -0.6), 'gen-3, gen-4...', '#0066CC', faded=True)
    ax.text(0.0, 1.8, 'd=0', fontsize=8, ha='right')
    ax.text(0.0, 0.6, 'd=1', fontsize=8, ha='right')
    ax.text(0.0, 0.0, 'd=2+', fontsize=8, ha='right')
    ax.text(0.6, -1.0, r'$x^{(k)} = G(x^{(k-1)})$', fontsize=8, ha='center')

    # Panel (b) Feature Extraction
    ax.text(2.4, 2.3, '(b) Feature Extraction', fontsize=9, fontweight='bold', ha='left')
    create_document_icon(ax, (2.4, 1.8), 'Document', '#B3D9FF')
    create_arrow(ax, (2.8, 1.8), (2.8, 1.5), color='black')
    create_textbox(ax, (2.5, 1.2), 0.6, 0.3, 'Pythia-410M', '(Reference Model)')
    ax.plot([2.5, 3.1], [0.9, 0.9], color='black', linestyle='-', linewidth=0.8)
    ax.text(2.8, 0.8, 'NLL Distribution', fontsize=8, ha='center')
    create_textbox(ax, (2.4, 0.4), 0.7, 0.3, 'NLL Statistics', 
                   'mean, std, max, min, tail_decay', color='black', bg_color='#A9DFBF')
    create_textbox(ax, (3.2, 0.4), 0.6, 0.3, 'Surface Features', 
                   'TTR, hapax_ratio', color='black', bg_color='#A9DFBF')
    ax.plot([2.8, 3.5], [0.4, 0.4], color='black', linestyle='-', linewidth=0.8)
    create_textbox(ax, (2.8, 0.0), 0.8, 0.2, '7 DDR Features', color='black', bg_color='#A9DFBF')

    # Panel (c) LOGO Evaluation
    ax.text(4.6, 2.3, '(c) LOGO Evaluation', fontsize=9, fontweight='bold', ha='left')
    generator_names = [
        ('Pythia-2.8B', 'train'), ('Pythia-1B', 'train'), ('OLMo-2-1B', 'train'), ('Qwen3-1.7B', 'train'),
        ('Qwen3-0.6B', 'train'), ('Qwen3-8B', 'train'), ('Llama-3.2-3B', 'train'), ('Mistral-7B', 'test')
    ]
    for i, (name, status) in enumerate(generator_names):
        x = 4.6 + (i % 4) * 0.5
        y = 1.8 - (i // 4) * 0.4
        color = '#4DA6FF' if status == 'train' else '#E8712B'
        create_textbox(ax, (x, y), 0.4, 0.3, name, color='black', bg_color=color)
    create_arrow(ax, (6.0, 1.4), (6.0, 1.0), color='black')
    create_textbox(ax, (5.8, 0.7), 0.4, 0.3, 'XGBoost Classifier')
    create_arrow(ax, (6.0, 0.7), (6.0, 0.4), color='black')
    create_document_icon(ax, (5.8, 0.0), 'gen-0', '#B3D9FF')
    create_document_icon(ax, (6.2, 0.0), 'gen-1', '#4DA6FF')
    create_document_icon(ax, (6.6, 0.0), 'gen-2+', '#0066CC')
    ax.text(6.0, -0.4, 'Leave-One-Generator-Out', fontsize=8, ha='center')

    plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', pad_inches=0.05)

if __name__ == "__main__":
    main()