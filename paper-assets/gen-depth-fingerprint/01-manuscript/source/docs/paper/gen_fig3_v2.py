#!/usr/bin/env python3
"""Figure 3: Baseline comparison — all 7 methods, binary F1 + cost.
Data source: results.tex Table 3 (8-gen pooled LOGO)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 8,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# --- Data from paper Table 3 (8-gen pooled LOGO) ---
# (label, binary_f1, 3class_f1, ms_per_text, memory_mb, group)
methods_raw = [
    ('4-det. + surface',  0.708, 0.795, 22.8, 2868, 'ensemble'),
    ('4-detector ens.',   0.700, 0.785, 22.8, 2868, 'ensemble'),
    ('7-feature (ours)',  0.705, 0.774,  9.7,  905, 'ours'),
    ('Avg-LogProb',       0.673, 0.707, None, None, 'single'),
    ('LD-Score',          0.675, 0.630, None, None, 'single'),
    ('FastDetectGPT',     0.569, 0.660, None, None, 'single'),
    ('Binoculars',        0.539, 0.411, None, None, 'single'),
]

# Sort by binary F1 descending
methods_raw.sort(key=lambda x: x[1], reverse=True)

C_OURS     = '#0072B2'
C_ENSEMBLE = '#E69F00'
C_SINGLE   = '#555555'
C_WEAK     = '#999999'

n = len(methods_raw)
y_pos = np.arange(n)[::-1]

fig, (ax_main, ax_cost) = plt.subplots(
    1, 2, figsize=(3.25, 2.4),
    gridspec_kw={'width_ratios': [3.5, 1], 'wspace': 0.05}
)

# Vertical reference line at our method's binary F1
ours_bin = [m[1] for m in methods_raw if m[5] == 'ours'][0]
ax_main.axvline(ours_bin, color=C_OURS, linewidth=0.5, linestyle=':', alpha=0.25, zorder=0)

# Separator between ensembles and single detectors
ensemble_count = sum(1 for m in methods_raw if m[5] in ('ensemble', 'ours'))
sep_y = y_pos[ensemble_count - 1] - 0.5
ax_main.axhline(sep_y, color='#e0e0e0', linewidth=0.5, zorder=0)
ax_cost.axhline(sep_y, color='#e0e0e0', linewidth=0.5, zorder=0)

for i, (label, bin_f1, cl3_f1, ms, mem, group) in enumerate(methods_raw):
    y = y_pos[i]

    if group == 'ours':
        color, marker, ms_size, fw, zo = C_OURS, 'D', 7, 'bold', 4
    elif group == 'ensemble':
        color, marker, ms_size, fw, zo = C_ENSEMBLE, 's', 5.5, 'normal', 3
    else:
        color = C_SINGLE if bin_f1 > 0.55 else C_WEAK
        marker, ms_size, fw, zo = 'o', 5, 'normal', 3

    # Binary F1 dot
    ax_main.plot(bin_f1, y, marker=marker, color=color, markersize=ms_size,
                 markeredgecolor='white', markeredgewidth=0.5, zorder=zo)

    # Value label to the right of dot
    offset = 0.009 if group != 'ours' else 0.012
    ax_main.text(bin_f1 + offset, y, f'{bin_f1:.3f}',
                 va='center', ha='left', fontsize=6, fontweight=fw, color=color)

    # Cost panel: inference speed + memory
    if ms is not None:
        speed_txt = f'{ms:.0f} ms'
        mem_txt = f'{mem:,d} MB'
        ax_cost.text(0.15, y + 0.12, speed_txt, va='bottom', ha='left',
                     fontsize=5.5, color='#666666', fontfamily='monospace')
        ax_cost.text(0.15, y - 0.12, mem_txt, va='top', ha='left',
                     fontsize=5.5, color='#999999', fontfamily='monospace')
    else:
        ax_cost.text(0.5, y, '—', va='center', ha='center',
                     fontsize=7, color='#cccccc')

# Main panel formatting
ax_main.set_yticks(y_pos)
ax_main.set_yticklabels([m[0] for m in methods_raw], fontsize=7)
ax_main.set_xlabel('Binary F1 (gen-1 vs. gen-2+)', fontsize=8)
ax_main.set_xlim(0.50, 0.76)
ax_main.set_ylim(-0.6, n - 0.4)
ax_main.spines['left'].set_visible(False)
ax_main.tick_params(axis='y', length=0)

# Group labels
ax_main.text(0.505, y_pos[0] + 0.35, 'Ensembles',
             fontsize=5.5, color='#aaaaaa', fontstyle='italic', va='bottom')
ax_main.text(0.505, sep_y - 0.05, 'Individual detectors',
             fontsize=5.5, color='#aaaaaa', fontstyle='italic', va='top')

# Cost panel formatting
ax_cost.set_xlim(0, 1)
ax_cost.set_ylim(-0.6, n - 0.4)
ax_cost.set_yticks([])
ax_cost.axis('off')
ax_cost.set_title('Cost', fontsize=7, color='#888888', pad=2)

plt.savefig('fig3_baseline_comparison.pdf', facecolor='white')
plt.savefig('fig3_baseline_comparison.png', dpi=300, facecolor='white')
print('Saved fig3_baseline_comparison.{pdf,png}')
plt.close()
