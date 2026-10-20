"""Generate pipeline overview figure — horizontal (left-to-right) layout."""
import paper_style; paper_style.apply_style()
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import os

plt.rcParams.update({
    'font.size': 8,
    'mathtext.fontset': 'cm',
})

C = {
    'int_fill':    '#E0EAF5',
    'int_edge':    '#3578B2',
    'int_text':    '#1E5080',
    'det_fill':    '#D8E2ED',
    'det_edge':    '#14365A',
    'det_text':    '#0F2A45',
    'proc_fill':   '#E5F0ED',
    'proc_edge':   '#2A8F82',
    'neutral_fill': '#F0F1F3',
    'neutral_edge': '#4A5260',
    'result_fill': '#F5F7FA',
    'result_edge': '#8B95A0',
    'arrow':       '#6B7580',
    'shadow':      '#C0C6CD',
    'muted_text':  '#6B7580',
}

fig, ax = plt.subplots(figsize=(7.0, 2.0))
ax.set_xlim(-0.3, 20.3)
ax.set_ylim(0.3, 5.7)
ax.axis('off')


def _bstyle(fill, edge, pad=0.3, lw=0.8):
    return dict(boxstyle=f'round,pad={pad}', facecolor=fill,
                edgecolor=edge, linewidth=lw)


def draw_box(x, y, text, fill, edge, fs=8, fw='normal',
             tc='#1a1a1a', pad=0.3, lw=0.8, shadow=True, **kw):
    if shadow:
        ax.text(x + 0.04, y - 0.04, text, ha='center', va='center',
                fontsize=fs, fontweight=fw, color='none',
                bbox=dict(boxstyle=f'round,pad={pad}', facecolor=C['shadow'],
                          edgecolor='none', linewidth=0, alpha=0.18),
                zorder=1, **kw)
    ax.text(x, y, text, ha='center', va='center', fontsize=fs,
            fontweight=fw, color=tc, bbox=_bstyle(fill, edge, pad, lw),
            zorder=2, **kw)


def draw_arrow(x1, y1, x2, y2, rad=0):
    style = f'arc3,rad={rad}' if rad else 'arc3,rad=0'
    a = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='->,head_length=2.5,head_width=1.5',
        color=C['arrow'], lw=0.6, zorder=1,
        mutation_scale=1, shrinkA=0, shrinkB=0,
        connectionstyle=style,
    )
    ax.add_patch(a)


# ═══════════════════════════════════════════
# Horizontal layout — 5 columns
# ═══════════════════════════════════════════

Y_TOP = 4.3
Y_BOT = 1.7
Y_MID = 3.0

# --- Col 1: Task Instance ---
draw_box(1.0, Y_MID, 'Task\nInstance $t$',
         C['neutral_fill'], C['neutral_edge'], fs=8, fw='bold')

# Fork label + arrows
ax.text(2.2, 3.65, 'fork', ha='center', va='center', fontsize=6,
        style='italic', color=C['muted_text'], zorder=3)
draw_arrow(2.0, 3.4, 2.95, Y_TOP, rad=0.08)
draw_arrow(2.0, 2.6, 2.95, Y_BOT, rad=-0.08)

# --- Col 2: Two parallel strategies + score tuples ---
draw_box(4.2, Y_TOP, 'Internal  $\\tau_{\\mathrm{int}}$',
         C['int_fill'], C['int_edge'], fs=7.5, tc=C['int_text'])
draw_box(4.2, Y_BOT, 'Deterministic  $\\tau_{\\mathrm{det}}$',
         C['det_fill'], C['det_edge'], fs=7.5, tc=C['det_text'])

draw_arrow(5.45, Y_TOP, 5.95, Y_TOP)
draw_arrow(5.75, Y_BOT, 5.95, Y_BOT)

ax.text(6.7, Y_TOP, '$(s_{\\mathrm{int}},\\, d_{\\mathrm{int}})$',
        ha='center', va='center', fontsize=7,
        color=C['int_edge'], zorder=3)
ax.text(6.7, Y_BOT, '$(s_{\\mathrm{det}},\\, d_{\\mathrm{det}})$',
        ha='center', va='center', fontsize=7,
        color=C['det_edge'], zorder=3)

# Merge arrows → labeling
draw_arrow(7.4, Y_TOP - 0.3, 8.5, Y_MID + 0.25, rad=0.08)
draw_arrow(7.4, Y_BOT + 0.3, 8.5, Y_MID - 0.25, rad=-0.08)

# --- Col 3: Episode-Level Labeling ---
draw_box(10.0, Y_MID, 'Episode-Level\nLabeling (Alg. 1)',
         C['proc_fill'], C['proc_edge'], fs=7.5, fw='medium', lw=0.9)

draw_arrow(11.5, Y_MID, 12.0, Y_MID)

# --- Col 4: Label output ---
draw_box(13.3, Y_MID,
         '$\\ell \\in \\{$det-pref,\nint-pref, no-pref$\\}$',
         C['result_fill'], C['result_edge'],
         fs=6.5, pad=0.2, lw=0.5, shadow=False)

# --- Col 5: Death Decomposition (top) + DAF (bottom) ---
# Single arrow from label output to Decomposition
draw_arrow(14.7, Y_MID + 0.35, 16.4, Y_TOP - 0.2, rad=-0.08)

draw_box(17.8, Y_TOP, 'Death Decomposition\nAnalysis',
         C['proc_fill'], C['proc_edge'], fs=7.5, fw='medium', lw=0.9)

draw_arrow(17.8, 3.55, 17.8, 2.5)

draw_box(17.8, 1.8,
         '$\\Delta_{\\mathrm{full}} \\approx \\delta P + \\Delta_{\\mathrm{nd}}$\n'
         'DAF $= 1 - \\Delta_{\\mathrm{nd}} / \\Delta_{\\mathrm{full}}$',
         C['result_fill'], C['result_edge'],
         fs=6.5, pad=0.2, lw=0.5, shadow=False)

# ═══════════════════════════════════════════

plt.tight_layout(pad=0.1)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_pdf = os.path.join(out_dir, 'pipeline_overview.pdf')
out_png = os.path.join(out_dir, 'pipeline_overview.png')

fig.savefig(out_pdf, bbox_inches='tight', pad_inches=0.02, dpi=300)
fig.savefig(out_png, bbox_inches='tight', pad_inches=0.02, dpi=300)
plt.close()

print(f"Saved: {out_pdf} ({os.path.getsize(out_pdf)} bytes)")
print(f"Saved: {out_png} ({os.path.getsize(out_png)} bytes)")
