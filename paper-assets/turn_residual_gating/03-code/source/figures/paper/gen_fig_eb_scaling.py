"""Generate appendix figure: Exposure Bias Scaling Analysis.
(a) TF/AR gap ratio across conditions.
(b) Gap scaling with conversation length (3.6 vs 10 mean turns).
"""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.5, 5.5),
                                gridspec_kw={'height_ratios': [1.3, 1]})

# ── Panel (a): TF/AR gap ratio across conditions ──
conditions = ['TG', '+PCGrad', 'UG', 'LoRA', 'SS']
tf_vals = [0.5002, 0.5002, 0.50, 0.50, 0.50]
ar_vals = [0.064, 0.030, 0.033, 0.037, 0.347]
ratios = [t / a for t, a in zip(tf_vals, ar_vals)]

llama_conds = ['TG', 'LoRA']
llama_tf = [0.484, 0.481]
llama_ar_med = [0.018, 0.018]
llama_ratios = [t / a for t, a in zip(llama_tf, llama_ar_med)]

cond_colors = [C_TG, C_ROSE, C_GREEN, C_PURPLE, C_SS]
x_q = np.arange(len(conditions))
bars_q = ax1.bar(x_q, ratios, width=0.35, color=cond_colors, alpha=0.85,
                 label='Qwen-2.5-7B', zorder=3, edgecolor='white', linewidth=0.5)

x_l_offset = [0 + 0.38, 3 + 0.38]
llama_bar_colors = [C_TG, C_PURPLE]
bars_l = ax1.bar(x_l_offset, llama_ratios, width=0.35, color=llama_bar_colors, alpha=0.50,
                 label='Llama-3.1-8B', zorder=3, edgecolor='white', linewidth=0.5, hatch='//')

for bar, ratio in zip(bars_q, ratios):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f'{ratio:.1f}×', ha='center', va='bottom', fontsize=6.5, fontweight='bold',
             color='#333333')

for bar, ratio in zip(bars_l, llama_ratios):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f'{ratio:.1f}×', ha='center', va='bottom', fontsize=6.5, fontweight='bold',
             color=C_AR)

ax1.axhline(y=1, color=C_GRAY, linestyle='--', linewidth=0.8, zorder=1)
ax1.text(4.6, 1.3, 'no gap', fontsize=6.5, color=C_GRAY, fontstyle='italic')

ax1.set_xticks(x_q)
ax1.set_xticklabels(conditions)
ax1.set_ylabel('TF / AR Gap Ratio')
ax1.set_ylim(0, 32)
ax1.set_title('(a) TF-AR gap by training variant', fontsize=9,
              fontweight='bold', loc='left', pad=6)
ax1.legend(loc='upper right')
ax1.grid(axis='y', alpha=0.15, zorder=0)

# ── Panel (b): Gap scaling with conversation length ──
conditions_b = ['TG', '+PCG', 'UG', 'LoRA']
ar_short = [0.064, 0.030, 0.033, 0.037]
ar_long = [0.016, 0.015, 0.015, 0.025]
gap_short = [0.50 / v for v in ar_short]
gap_long = [0.50 / v for v in ar_long]

x_b = np.arange(len(conditions_b))
w = 0.32
bars_s = ax2.bar(x_b - w/2, gap_short, width=w, color=C_GOLD, alpha=0.75,
                 label='N=50 (3.6 turns)', zorder=3, edgecolor='white', linewidth=0.5)
bars_l2 = ax2.bar(x_b + w/2, gap_long, width=w, color=C_TEAL, alpha=0.85,
                  label='N=5 (10 turns)', zorder=3, edgecolor='white', linewidth=0.5)

for bar, g in zip(bars_s, gap_short):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f'{g:.0f}×', ha='center', va='bottom', fontsize=6, color='#B89A5A')
for bar, g in zip(bars_l2, gap_long):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f'{g:.0f}×', ha='center', va='bottom', fontsize=6, color='#5AA89A', fontweight='bold')

ax2.set_xticks(x_b)
ax2.set_xticklabels(conditions_b)
ax2.set_ylabel('TF / AR Gap Ratio')
ax2.set_ylim(0, 38)
ax2.set_title('(b) Gap scales with conversation length', fontsize=9,
              fontweight='bold', loc='left', pad=6)
ax2.legend(loc='upper left')
ax2.grid(axis='y', alpha=0.15, zorder=0)

plt.tight_layout(h_pad=2.0)
save_fig(fig, 'fig_eb_scaling')
