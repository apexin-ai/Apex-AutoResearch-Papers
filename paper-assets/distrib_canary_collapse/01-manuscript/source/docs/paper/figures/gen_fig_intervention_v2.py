#!/usr/bin/env python3
"""Figure 4: Canary-triggered intervention comparison.
Unified style with project palette."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
    'lines.linewidth': 1.6,
})

C_BASELINE   = '#999999'
C_PREDICTIVE = '#4A90C4'
C_REACTIVE   = '#CC5A5A'
C_THRESHOLD  = '#E8A04C'

gens = np.arange(11)

# ── Data: s42 fp32 at α=1.0 (Pythia-410M) ──
baseline_ent = [3.2342, 1.9099, 1.4611, 1.3379, 1.2805, 1.2912, 1.2253, 1.2369, 1.2482, 1.2390, 1.2269]
baseline_ppl = [26.949, 57.415, 162.151, 279.174, 394.018, 508.854, 598.726, 722.577, 814.682, 934.959, 1017.811]

pred_ppl = [26.949, 56.99, 20.80, 20.74, 20.96, 20.77, 20.93, 20.99, 20.67, 20.95, 21.29]
pred_ent = [3.2342, 1.9099, 3.0489, 3.0526, 3.0669, 3.0467, 3.0512, 3.0553, 3.0575, 3.0325, 3.0487]

react_ppl = [26.949, 57.415, 157.09, 21.98, 21.55, 21.22, 21.67, 21.32, 21.46, 21.36, 21.24]
react_ent = [3.2342, 1.9099, 1.4611, 3.1312, 3.0846, 3.0641, 3.0808, 3.0957, 3.0648, 3.0791, 3.0876]

threshold_ent = baseline_ent[0] * 0.85

# ── Figure ──
fig, (ax_ent, ax_ppl) = plt.subplots(
    2, 1, figsize=(3.5, 4.2), sharex=True,
    gridspec_kw={'height_ratios': [1, 1.15], 'hspace': 0.10}
)

# ═══ Panel (a): Token Entropy ═══
ax_ent.plot(gens, baseline_ent, '--', color=C_BASELINE, linewidth=1.3,
            label='No intervention', zorder=2)
ax_ent.plot(gens, pred_ent, '-', color=C_PREDICTIVE, marker='o', markersize=3.5,
            markeredgewidth=0, label='Predictive (entropy)', zorder=3)
ax_ent.plot(gens, react_ent, '-', color=C_REACTIVE, marker='s', markersize=3,
            markeredgewidth=0, label='Reactive (distinct-1)', zorder=3)

ax_ent.axhline(threshold_ent, color=C_THRESHOLD, linestyle=':', linewidth=1.1,
               alpha=0.7, zorder=1)
t = ax_ent.text(10.3, threshold_ent, r'$-15\%$',
                fontsize=7, color='#B0922E', va='center', ha='right')
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Trigger annotations
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
ax_ent.set_ylim(0.9, 3.5)
ax_ent.legend(loc='center right', framealpha=0.92, edgecolor='none',
              handlelength=1.5, borderpad=0.3)
ax_ent.text(-0.14, 1.02, '(a)', transform=ax_ent.transAxes,
            fontsize=11, fontweight='bold', va='bottom')

# ═══ Panel (b): Perplexity (log scale) ═══
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
                    alpha=0.08, color=C_PREDICTIVE, zorder=1)

# Peak markers
ax_ppl.plot(1, pred_ppl[1], 'o', color=C_PREDICTIVE, markersize=6,
            markeredgecolor='white', markeredgewidth=1.0, zorder=6)
ax_ppl.plot(2, react_ppl[2], 's', color=C_REACTIVE, markersize=5.5,
            markeredgecolor='white', markeredgewidth=1.0, zorder=6)

# Bracket annotation
ax_col = 3.5
ax_ppl.plot([1, ax_col], [pred_ppl[1], pred_ppl[1]], ':', color=C_PREDICTIVE,
            linewidth=0.6, alpha=0.4, zorder=1)
ax_ppl.plot([2, ax_col], [react_ppl[2], react_ppl[2]], ':', color=C_REACTIVE,
            linewidth=0.6, alpha=0.4, zorder=1)

ax_ppl.annotate('',
                xy=(ax_col, pred_ppl[1]), xytext=(ax_col, react_ppl[2]),
                arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.0,
                                shrinkA=1, shrinkB=1),
                zorder=5)
gmean = np.sqrt(pred_ppl[1] * react_ppl[2])
t2 = ax_ppl.text(ax_col + 0.3, gmean, '64%',
                 fontsize=8, color='#333333', va='center', ha='left',
                 fontweight='bold')
t2.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Peak value annotations — offset to whitespace
t_pv1 = ax_ppl.text(0.6, pred_ppl[1] * 1.35, f'{pred_ppl[1]:.0f}',
                     fontsize=6.5, color=C_PREDICTIVE, ha='center', va='bottom')
t_pv1.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
t_pv2 = ax_ppl.text(2.8, react_ppl[2] * 1.4, f'{react_ppl[2]:.0f}',
                     fontsize=6.5, color=C_REACTIVE, ha='center', va='bottom')
t_pv2.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax_ppl.legend(loc='upper left', framealpha=0.92, edgecolor='none',
              handlelength=1.5, borderpad=0.3)
ax_ppl.text(-0.14, 1.02, '(b)', transform=ax_ppl.transAxes,
            fontsize=11, fontweight='bold', va='bottom')

# ── Save ──
for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_intervention.{fmt}', dpi=300)
    print(f'Saved: {OUT / f"fig_intervention.{fmt}"}')
plt.close()
