import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os, shutil

plt.rcParams.update({
    'font.family': 'sans-serif', 'font.sans-serif': ['DejaVu Sans'],
    'font.size': 10, 'figure.dpi': 300, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
})

# --- Data ---
indicators = ['SLV', 'RankMe', 'Token entropy', 'Stable rank',
              'Spectral norm', 'Isotropy', 'Raw PPL', 'PPL growth']

directions = [
    'Peak Gen 2, then ↓', 'Peak Gen 2, then ↓',
    '↓  monotonic', '↓  monotonic', '↑  monotonic',
    '↓  noisy', '↑  monotonic', '↑  monotonic',
]

dir_colors = ['#E8956A', '#E8956A',
              '#D6604D', '#D6604D', '#D6604D', '#D6604D', '#D6604D', '#D6604D']

rel_deltas = [11.8, 4.7, 9.6, 14.0, 8.0, 75.0, 643.0, None]
rel_delta_labels = ['11.8%', '4.7%', '9.6%', '14.0%', '8.0%', '75%', '643%', '—']
reverses = [True, True, True, True, True, True, False, True]

n_rows = len(indicators)
col_widths = [0.22, 0.30, 0.18, 0.30]
col_starts = [0.0]
for w in col_widths[:-1]:
    col_starts.append(col_starts[-1] + w)

headers = ['Indicator', 'Direction at r = 0', 'Rel Δ%', 'Reverses\nunder mixing?']

row_height = 0.08
header_height = 0.10
y_top = 0.92

fig, ax = plt.subplots(figsize=(7, 4))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# --- Color scale for Rel Delta ---
valid_deltas = [d for d in rel_deltas if d is not None]
log_min = np.log10(min(valid_deltas))
log_max = np.log10(max(valid_deltas))

def delta_color(val):
    if val is None:
        return '#f5f5f5'
    t = (np.log10(val) - log_min) / (log_max - log_min)
    t = np.clip(t, 0, 1)
    r = 0.96 - 0.38 * t
    g = 0.92 - 0.50 * t
    b = 0.90 - 0.42 * t
    return (r, g, b)

# --- Header ---
header_y = y_top - header_height
for j, (hdr, xs, w) in enumerate(zip(headers, col_starts, col_widths)):
    rect = mpatches.FancyBboxPatch(
        (xs + 0.005, header_y), w - 0.01, header_height - 0.005,
        boxstyle='round,pad=0.006', facecolor='#2c3e50', edgecolor='none',
    )
    ax.add_patch(rect)
    ax.text(xs + w / 2, header_y + header_height / 2, hdr,
            ha='center', va='center', fontsize=9, fontweight='bold', color='white')

# --- Rows ---
for i in range(n_rows):
    row_y = y_top - header_height - (i + 1) * row_height
    stripe = '#f9f9fb' if i % 2 == 0 else '#ffffff'
    is_slv = (i == 0)

    for j in range(4):
        xs = col_starts[j]
        w = col_widths[j]

        if j == 0:
            bg = '#dce9f4' if is_slv else stripe
        elif j == 2:
            bg = delta_color(rel_deltas[i])
        elif j == 3:
            bg = '#d5e8d4' if reverses[i] else '#fde0cc'
        else:
            bg = stripe

        rect = mpatches.FancyBboxPatch(
            (xs + 0.005, row_y + 0.003), w - 0.01, row_height - 0.006,
            boxstyle='round,pad=0.004', facecolor=bg,
            edgecolor='#e0e0e0', linewidth=0.4,
        )
        ax.add_patch(rect)

    # Col 0: Indicator name
    ax.text(col_starts[0] + 0.015, row_y + row_height / 2, indicators[i],
            ha='left', va='center', fontsize=9.5,
            fontweight='bold' if is_slv else 'normal',
            color='#1a5276' if is_slv else '#333333')

    # Col 1: Direction
    ax.text(col_starts[1] + col_widths[1] / 2, row_y + row_height / 2,
            directions[i], ha='center', va='center', fontsize=9,
            color=dir_colors[i], fontweight='semibold')

    # Col 2: Rel Delta
    delta_txt_color = '#333333' if rel_deltas[i] is not None else '#aaaaaa'
    fw = 'bold' if rel_deltas[i] is not None and rel_deltas[i] >= 50 else 'normal'
    ax.text(col_starts[2] + col_widths[2] / 2, row_y + row_height / 2,
            rel_delta_labels[i], ha='center', va='center', fontsize=9,
            color=delta_txt_color, fontweight=fw)

    # Col 3: Reverses?
    sym = '✓' if reverses[i] else '✗'
    sym_color = '#5B9F5B' if reverses[i] else '#D6604D'
    ax.text(col_starts[3] + col_widths[3] / 2, row_y + row_height / 2, sym,
            ha='center', va='center', fontsize=12, color=sym_color, fontweight='bold')

# --- Bottom annotation ---
ann_y = y_top - header_height - n_rows * row_height - 0.04
ax.text(0.5, ann_y,
        '7/8 indicators reverse under mixing;  Raw PPL is the sole exception.',
        ha='center', va='center', fontsize=8.5, color='#666666', style='italic')

# --- Save ---
OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/figures/paper'
PAPDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/figures'
os.makedirs(PAPDIR, exist_ok=True)
for d, n in [(OUTDIR, 'fig4_ews_heatmap'), (PAPDIR, 'ews_heatmap')]:
    fig.savefig(f'{d}/{n}.pdf')
    fig.savefig(f'{d}/{n}.png')
plt.close(fig)
print('Fig 4 done.')
