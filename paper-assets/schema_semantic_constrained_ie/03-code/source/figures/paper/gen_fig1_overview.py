import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# Colors (Okabe-Ito)
C_GRAMMAR  = '#56B4E9'  # sky blue
C_SEMANTIC = '#E69F00'  # orange-yellow
C_LLM      = '#009E73'  # green
C_ONTOLOGY = '#CC79A7'  # pink-purple
C_AND      = '#D55E00'  # orange-red
C_BG       = '#FAFAFA'
C_TEXT     = '#333333'
C_LIGHT_GRAMMAR  = '#D6EEFB'
C_LIGHT_SEMANTIC = '#FFF0CC'
C_LIGHT_LLM      = '#CCF0E6'
C_LIGHT_ONTOLOGY = '#F5DDE8'

fig, ax = plt.subplots(1, 1, figsize=(12, 4.8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.set_aspect('equal')
ax.axis('off')

def draw_box(ax, xy, w, h, color, alpha=0.15, linewidth=1.5, label=None, label_size=11, label_weight='bold', round_size=0.08):
    box = FancyBboxPatch(xy, w, h,
                         boxstyle=f"round,pad={round_size}",
                         facecolor=color, edgecolor=plt.cm.colors.to_rgba(color, 1.0),
                         alpha=alpha, linewidth=linewidth, zorder=2)
    ax.add_patch(box)
    border = FancyBboxPatch(xy, w, h,
                            boxstyle=f"round,pad={round_size}",
                            facecolor='none', edgecolor=color,
                            linewidth=linewidth, zorder=3)
    ax.add_patch(border)
    if label:
        ax.text(xy[0] + w/2, xy[1] + h - 0.22, label,
                ha='center', va='top', fontsize=label_size, fontweight=label_weight,
                color=C_TEXT, zorder=5)

def draw_arrow(ax, posA, posB, color='#666666', style='->', lw=1.5, connectionstyle="arc3,rad=0", linestyle='-'):
    arrow = FancyArrowPatch(posA, posB,
                            arrowstyle=style, color=color,
                            connectionstyle=connectionstyle,
                            lw=lw, zorder=4, linestyle=linestyle,
                            mutation_scale=15)
    ax.add_patch(arrow)

def draw_small_box(ax, xy, w, h, color, text, fontsize=9, alpha=0.25, text_color=None):
    box = FancyBboxPatch(xy, w, h,
                         boxstyle="round,pad=0.04",
                         facecolor=color, edgecolor=color,
                         alpha=alpha, linewidth=1.0, zorder=2)
    ax.add_patch(box)
    border = FancyBboxPatch(xy, w, h,
                            boxstyle="round,pad=0.04",
                            facecolor='none', edgecolor=color,
                            linewidth=1.0, zorder=3)
    ax.add_patch(border)
    ax.text(xy[0] + w/2, xy[1] + h/2, text,
            ha='center', va='center', fontsize=fontsize,
            color=text_color or C_TEXT, zorder=5)

# ─── LEFT: Ontology Schema ─────────────────────────────────────
ont_x, ont_y, ont_w, ont_h = 0.1, 1.0, 2.9, 3.2
draw_box(ax, (ont_x, ont_y), ont_w, ont_h, C_ONTOLOGY, alpha=0.12, label="Ontology Schema", label_size=11)

ax.text(ont_x + 0.15, ont_y + ont_h - 0.55, r'$\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$',
        fontsize=11, color=C_TEXT, va='top', zorder=5, style='italic')

# Entity types
ey = ont_y + ont_h - 1.05
ax.text(ont_x + 0.15, ey, 'Entity Types $\\mathcal{E}$:', fontsize=8.5, fontweight='bold', color=C_TEXT, va='top', zorder=5)
ax.text(ont_x + 0.15, ey - 0.28, '{Method, Task, Material,\n Metric, OtherSciTerm, Generic}',
        fontsize=7.5, color='#555555', va='top', zorder=5, family='monospace')

# Relation types
ry = ey - 0.85
ax.text(ont_x + 0.15, ry, 'Relation Types $\\mathcal{R}$:', fontsize=8.5, fontweight='bold', color=C_TEXT, va='top', zorder=5)
ax.text(ont_x + 0.15, ry - 0.28, '{Used-for, Feature-of,\n Compare, Evaluate-for, …}',
        fontsize=7.5, color='#555555', va='top', zorder=5, family='monospace')

# Domain/Range
dy = ry - 0.78
ax.text(ont_x + 0.15, dy, 'Domain/Range $\\sigma$:', fontsize=8.5, fontweight='bold', color=C_TEXT, va='top', zorder=5)
ax.text(ont_x + 0.15, dy - 0.28, 'Used-for → {(Method,Task),\n  (Method,Material), …}',
        fontsize=7.5, color='#555555', va='top', zorder=5, family='monospace')

# ─── MIDDLE: Ontology Compiler ─────────────────────────────────
comp_x, comp_y, comp_w, comp_h = 3.6, 0.55, 4.7, 4.0
# Light background for compiler region
comp_bg = FancyBboxPatch((comp_x, comp_y), comp_w, comp_h,
                          boxstyle="round,pad=0.1",
                          facecolor='#F0F0F0', edgecolor='#AAAAAA',
                          alpha=0.3, linewidth=1.0, linestyle='--', zorder=1)
ax.add_patch(comp_bg)
ax.text(comp_x + comp_w/2, comp_y + comp_h - 0.05, 'Ontology Compiler',
        ha='center', va='top', fontsize=12, fontweight='bold', color=C_TEXT, zorder=5)

# --- Grammar Layer (upper path) ---
gl_x, gl_y, gl_w, gl_h = comp_x + 0.15, comp_y + comp_h - 1.85, comp_w - 0.3, 1.45
draw_box(ax, (gl_x, gl_y), gl_w, gl_h, C_GRAMMAR, alpha=0.12, round_size=0.06)
ax.text(gl_x + 0.12, gl_y + gl_h - 0.1, '(a) Grammar Layer — Purely Local',
        fontsize=9, fontweight='bold', color=C_GRAMMAR, va='top', zorder=5)

# Pipeline boxes inside grammar
gp_y = gl_y + 0.25
gp_h = 0.55
draw_small_box(ax, (gl_x + 0.1, gp_y), 1.25, gp_h, C_GRAMMAR,
               'JSON Schema\n(enum + struct)', fontsize=7.5, alpha=0.18)
draw_small_box(ax, (gl_x + 1.65, gp_y), 1.1, gp_h, C_GRAMMAR,
               'XGrammar\nCFG', fontsize=7.5, alpha=0.18)
draw_small_box(ax, (gl_x + 3.05, gp_y), 1.15, gp_h, C_GRAMMAR,
               'Token Mask\n$M_g$', fontsize=8, alpha=0.25, text_color=C_GRAMMAR)

# Arrows inside grammar pipeline
draw_arrow(ax, (gl_x + 1.35, gp_y + gp_h/2), (gl_x + 1.65, gp_y + gp_h/2), color=C_GRAMMAR, lw=1.2)
draw_arrow(ax, (gl_x + 2.75, gp_y + gp_h/2), (gl_x + 3.05, gp_y + gp_h/2), color=C_GRAMMAR, lw=1.2)

# annotation
ax.text(gl_x + gl_w/2, gl_y + 0.08, 'Enforces: valid JSON, type ∈ vocabulary',
        ha='center', va='bottom', fontsize=7, color='#666666', style='italic', zorder=5)

# --- Semantic Layer (lower path) ---
sl_x, sl_y, sl_w, sl_h = comp_x + 0.15, comp_y + 0.2, comp_w - 0.3, 1.65
draw_box(ax, (sl_x, sl_y), sl_w, sl_h, C_SEMANTIC, alpha=0.12, round_size=0.06)
ax.text(sl_x + 0.12, sl_y + sl_h - 0.1, '(b) Semantic Layer — Prefix-Decidable with State',
        fontsize=9, fontweight='bold', color='#B8860B', va='top', zorder=5)

# Pipeline boxes inside semantic
sp_y = sl_y + 0.52
sp_h = 0.55
draw_small_box(ax, (sl_x + 0.1, sp_y), 1.15, sp_h, C_SEMANTIC,
               'Domain/Range\nRules', fontsize=7.5, alpha=0.18)
draw_small_box(ax, (sl_x + 1.55, sp_y), 1.2, sp_h, C_SEMANTIC,
               'TypeConstraint\nProcessor', fontsize=7.5, alpha=0.18)
draw_small_box(ax, (sl_x + 3.05, sp_y), 1.15, sp_h, C_SEMANTIC,
               'Dynamic Mask\n$M_s$', fontsize=8, alpha=0.25, text_color='#B8860B')

# Entity Registry sub-box
draw_small_box(ax, (sl_x + 0.6, sl_y + 0.08), 1.8, 0.35, C_SEMANTIC,
               'Entity Registry  (name → type)', fontsize=7, alpha=0.12)

# Arrows inside semantic pipeline
draw_arrow(ax, (sl_x + 1.25, sp_y + sp_h/2), (sl_x + 1.55, sp_y + sp_h/2), color=C_SEMANTIC, lw=1.2)
draw_arrow(ax, (sl_x + 2.75, sp_y + sp_h/2), (sl_x + 3.05, sp_y + sp_h/2), color=C_SEMANTIC, lw=1.2)

# --- Dashed arrow: grammar enables semantic ---
draw_arrow(ax, (gl_x + gl_w/2 - 0.3, gl_y),
           (sl_x + sl_w/2 - 0.3, sl_y + sl_h),
           color='#888888', lw=1.2, style='->', linestyle='--',
           connectionstyle="arc3,rad=0")
ax.text(comp_x + comp_w/2 + 0.5, (gl_y + sl_y + sl_h)/2, 'grammar\nenables\nsemantic',
        ha='center', va='center', fontsize=7.5, color='#777777', style='italic', zorder=5)

# ─── Arrows: Ontology → Compiler ───────────────────────────────
# Upper arrow to grammar
ont_right_x = ont_x + ont_w
draw_arrow(ax, (ont_right_x, ont_y + ont_h - 1.1), (gl_x + 0.1, gl_y + 0.55),
           color=C_ONTOLOGY, lw=1.8, connectionstyle="arc3,rad=0.1")
# Lower arrow to semantic
draw_arrow(ax, (ont_right_x, ont_y + 0.9), (sl_x + 0.1, sl_y + 0.9),
           color=C_ONTOLOGY, lw=1.8, connectionstyle="arc3,rad=-0.1")

# ─── RIGHT: LLM Decoding ──────────────────────────────────────
llm_x, llm_y, llm_w, llm_h = 9.0, 0.8, 2.8, 3.6
draw_box(ax, (llm_x, llm_y), llm_w, llm_h, C_LLM, alpha=0.10, label="LLM Decoding", label_size=11)

# LLM box
draw_small_box(ax, (llm_x + 0.3, llm_y + llm_h - 1.2), 1.0, 0.6, C_LLM,
               'LLM\nLogits', fontsize=9, alpha=0.2, text_color=C_LLM)

# AND operation
and_x, and_y = llm_x + 1.65, llm_y + llm_h - 1.6
and_r = 0.28
circle = plt.Circle((and_x, and_y + and_r), and_r, facecolor='#FFEBE0',
                     edgecolor=C_AND, linewidth=1.5, zorder=3)
ax.add_patch(circle)
ax.text(and_x, and_y + and_r, '∧', ha='center', va='center',
        fontsize=14, fontweight='bold', color=C_AND, zorder=5)

# M_g and M_s labels arriving
ax.text(llm_x + 1.65, llm_y + llm_h - 0.55, '$M_g$', ha='center', va='center',
        fontsize=10, fontweight='bold', color=C_GRAMMAR,
        bbox=dict(boxstyle='round,pad=0.15', facecolor=C_LIGHT_GRAMMAR, edgecolor=C_GRAMMAR, linewidth=1),
        zorder=5)
ax.text(llm_x + 2.35, llm_y + llm_h - 0.55, '$M_s$', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#B8860B',
        bbox=dict(boxstyle='round,pad=0.15', facecolor=C_LIGHT_SEMANTIC, edgecolor=C_SEMANTIC, linewidth=1),
        zorder=5)

# Arrows: M_g, M_s → AND
draw_arrow(ax, (llm_x + 1.65, llm_y + llm_h - 0.72), (and_x, and_y + and_r + and_r),
           color=C_GRAMMAR, lw=1.3)
draw_arrow(ax, (llm_x + 2.35, llm_y + llm_h - 0.72), (and_x + 0.15, and_y + and_r + and_r),
           color=C_SEMANTIC, lw=1.3)

# M_final
mf_y = and_y - 0.55
ax.text(and_x, mf_y + 0.15, '$M_{final}$', ha='center', va='center',
        fontsize=10, fontweight='bold', color=C_AND,
        bbox=dict(boxstyle='round,pad=0.15', facecolor='#FFEBE0', edgecolor=C_AND, linewidth=1),
        zorder=5)
draw_arrow(ax, (and_x, and_y), (and_x, mf_y + 0.3),
           color=C_AND, lw=1.3)

# Logits → AND
draw_arrow(ax, (llm_x + 1.3, llm_y + llm_h - 0.9), (and_x - and_r, and_y + and_r),
           color=C_LLM, lw=1.3)

# Constrained Sampling box
cs_x, cs_y, cs_w, cs_h = llm_x + 0.3, llm_y + 0.55, 2.2, 0.6
draw_small_box(ax, (cs_x, cs_y), cs_w, cs_h, C_LLM,
               'Constrained Sampling', fontsize=8.5, alpha=0.18, text_color=C_LLM)

# M_final → Constrained Sampling
draw_arrow(ax, (and_x, mf_y), (cs_x + cs_w/2, cs_y + cs_h),
           color=C_AND, lw=1.3)

# Output JSON
ax.text(llm_x + llm_w/2, llm_y + 0.22, '→  JSON tokens',
        ha='center', va='center', fontsize=8.5, color=C_TEXT, zorder=5, family='monospace')

# S1 note
ax.text(llm_x + llm_w/2, llm_y + 0.02, 'S1: Single-pass (both layers active)',
        ha='center', va='top', fontsize=6.5, color='#999999', style='italic', zorder=5)

# ─── Arrows: Compiler → LLM (M_g and M_s outputs) ─────────────
# Grammar → M_g in LLM
gram_out_x = comp_x + comp_w
draw_arrow(ax, (gram_out_x, gl_y + 0.55), (llm_x + 1.45, llm_y + llm_h - 0.55),
           color=C_GRAMMAR, lw=1.8, connectionstyle="arc3,rad=0.05")
# Semantic → M_s in LLM
draw_arrow(ax, (gram_out_x, sl_y + 0.8), (llm_x + 2.15, llm_y + llm_h - 0.55),
           color=C_SEMANTIC, lw=1.8, connectionstyle="arc3,rad=-0.05")

# ─── Section labels at top ──────────────────────────────────────
ax.text(ont_x + ont_w/2, 4.65, 'Input', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#888888', zorder=5)
ax.text(comp_x + comp_w/2, 4.75, 'Compile', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#888888', zorder=5)
ax.text(llm_x + llm_w/2, 4.65, 'Decode', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#888888', zorder=5)

# Save
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/figures/paper'
fig.savefig(f'{out_dir}/fig1_overview.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig1_overview.png', format='png')
plt.close()
print("Done.")
