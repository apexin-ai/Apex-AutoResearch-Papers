import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

C_BASELINE   = '#999999'
C_PREDICTIVE = '#0072B2'
C_REACTIVE   = '#D55E00'
C_THRESHOLD  = '#009E73'

gens = np.arange(11)

# ── Data: s42 fp32 at α=1.0 (Pythia-410M) ──
# Baseline
baseline_ent = [3.2342, 1.9099, 1.4611, 1.3379, 1.2805, 1.2912, 1.2253, 1.2369, 1.2482, 1.2390, 1.2269]
baseline_ppl = [26.949, 57.415, 162.151, 279.174, 394.018, 508.854, 598.726, 722.577, 814.682, 934.959, 1017.811]

# Predictive: entropy trigger at gen 1, switch to α=0 for gen 2+
pred_ppl = [26.949, 56.99, 20.80, 20.74, 20.96, 20.77, 20.93, 20.99, 20.67, 20.95, 21.29]
pred_ent = [3.2342, 1.9099, 3.0489, 3.0526, 3.0669, 3.0467, 3.0512, 3.0553, 3.0575, 3.0325, 3.0487]

# Reactive: distinct-1 trigger at gen 2, switch to α=0 for gen 3+
react_ppl = [26.949, 57.415, 157.09, 21.98, 21.55, 21.22, 21.67, 21.32, 21.46, 21.36, 21.24]
react_ent = [3.2342, 1.9099, 1.4611, 3.1312, 3.0846, 3.0641, 3.0808, 3.0957, 3.0648, 3.0791, 3.0876]

threshold_ent = baseline_ent[0] * 0.85  # 2.749

# ── Figure ──
fig, (ax_ent, ax_ppl) = plt.subplots(
    1, 2, figsize=(7.0, 2.4),
    gridspec_kw={'wspace': 0.32}
)

# ══════════════════════════════════════════════════════════════════
# Panel (a): Token Entropy
# ══════════════════════════════════════════════════════════════════
ax_ent.plot(gens, baseline_ent, '--', color=C_BASELINE, linewidth=1.3,
            label='No intervention', zorder=2)
ax_ent.plot(gens, pred_ent, '-', color=C_PREDICTIVE, marker='o', markersize=3.5,
            markeredgewidth=0, label='Predictive (entropy)', zorder=3)
ax_ent.plot(gens, react_ent, '-', color=C_REACTIVE, marker='s', markersize=3,
            markeredgewidth=0, label='Reactive (distinct-1)', zorder=3)

# 15% threshold line
ax_ent.axhline(threshold_ent, color=C_THRESHOLD, linestyle=':', linewidth=1.1,
               alpha=0.6, zorder=1)
t = ax_ent.text(10.3, threshold_ent, r'$-15\%$',
                fontsize=7, color=C_THRESHOLD, va='center', ha='right')
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Trigger annotations with offset to avoid overlap
ax_ent.annotate('cease',
                xy=(1, pred_ent[1]), xytext=(0.0, 2.55),
                fontsize=7, color=C_PREDICTIVE, ha='center', va='bottom',
                fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=C_PREDICTIVE, lw=0.9,
                                connectionstyle='arc3,rad=0.15'),
                zorder=5)
t_pred = ax_ent.text(0.0, 2.48, 'gen 1', fontsize=6, color=C_PREDICTIVE,
                     ha='center', va='top', fontstyle='italic')
t_pred.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax_ent.annotate('cease',
                xy=(2, react_ent[2]), xytext=(3.3, 2.55),
                fontsize=7, color=C_REACTIVE, ha='center', va='bottom',
                fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=C_REACTIVE, lw=0.9,
                                connectionstyle='arc3,rad=-0.15'),
                zorder=5)
t_react = ax_ent.text(3.3, 2.48, 'gen 2', fontsize=6, color=C_REACTIVE,
                      ha='center', va='top', fontstyle='italic')
t_react.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax_ent.set_ylabel('Token entropy')
ax_ent.set_xlabel('Generation')
ax_ent.set_xticks(gens)
ax_ent.set_ylim(0.9, 3.5)
ax_ent.legend(loc='center right', framealpha=0.92, edgecolor='none',
              handlelength=1.5, borderpad=0.3)
ax_ent.text(-0.15, 1.02, '(a)', transform=ax_ent.transAxes,
            fontsize=11, fontweight='bold', va='bottom')

# ══════════════════════════════════════════════════════════════════
# Panel (b): Perplexity (log scale)
# ══════════════════════════════════════════════════════════════════
ax_ppl.plot(gens, baseline_ppl, '--', color=C_BASELINE, linewidth=1.3,
            label='No intervention', zorder=2)
ax_ppl.plot(gens, pred_ppl, '-', color=C_PREDICTIVE, marker='o', markersize=3.5,
            markeredgewidth=0, label='Predictive', zorder=3)
ax_ppl.plot(gens, react_ppl, '-', color=C_REACTIVE, marker='s', markersize=3,
            markeredgewidth=0, label='Reactive', zorder=3)

ax_ppl.set_yscale('log')
ax_ppl.set_ylabel('Perplexity')
ax_ppl.set_xlabel('Generation')
ax_ppl.set_xticks(gens)
ax_ppl.set_ylim(12, 1500)

# Shaded area between predictive and reactive (gen 1→2)
ax_ppl.fill_between([1, 2], [pred_ppl[1], pred_ppl[2]],
                    [react_ppl[1], react_ppl[2]],
                    alpha=0.10, color=C_PREDICTIVE, zorder=1)

# Peak markers (larger, highlighted)
ax_ppl.plot(1, pred_ppl[1], 'o', color=C_PREDICTIVE, markersize=6,
            markeredgecolor='white', markeredgewidth=1.0, zorder=6)
ax_ppl.plot(2, react_ppl[2], 's', color=C_REACTIVE, markersize=5.5,
            markeredgecolor='white', markeredgewidth=1.0, zorder=6)

# Bracket annotation: peak-to-peak comparison
# Horizontal dashed lines from peaks to annotation column
ax_col = 3.5  # x position for the bracket
ax_ppl.plot([1, ax_col], [pred_ppl[1], pred_ppl[1]], ':', color=C_PREDICTIVE,
            linewidth=0.6, alpha=0.5, zorder=1)
ax_ppl.plot([2, ax_col], [react_ppl[2], react_ppl[2]], ':', color=C_REACTIVE,
            linewidth=0.6, alpha=0.5, zorder=1)

# Vertical arrow between the two peak levels
ax_ppl.annotate('',
                xy=(ax_col, pred_ppl[1]), xytext=(ax_col, react_ppl[2]),
                arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.0,
                                shrinkA=1, shrinkB=1),
                zorder=5)
# "64%" label (1 - 56.99/157.09 = 63.7% ≈ 64%, this seed s42 fp32)
gmean = np.sqrt(pred_ppl[1] * react_ppl[2])  # geometric mean for log-scale centering
t2 = ax_ppl.text(ax_col + 0.3, gmean, '64%',
                 fontsize=8, color='#333333', va='center', ha='left',
                 fontweight='bold')
t2.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Peak value annotations
t_pv1 = ax_ppl.text(0.5, pred_ppl[1] * 1.25, f'{pred_ppl[1]:.0f}',
                     fontsize=6.5, color=C_PREDICTIVE, ha='center', va='bottom')
t_pv1.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
t_pv2 = ax_ppl.text(2.0, react_ppl[2] * 1.2, f'{react_ppl[2]:.0f}',
                     fontsize=6.5, color=C_REACTIVE, ha='center', va='bottom')
t_pv2.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax_ppl.legend(loc='upper left', framealpha=0.92, edgecolor='none',
              handlelength=1.5, borderpad=0.3)
ax_ppl.text(-0.15, 1.02, '(b)', transform=ax_ppl.transAxes,
            fontsize=11, fontweight='bold', va='bottom')

fig.subplots_adjust(left=0.07, right=0.97, top=0.94, bottom=0.17)

# ── Save ──
for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_intervention.{fmt}')
    print(f'Saved: {OUT / f"fig_intervention.{fmt}"}')
plt.close()
