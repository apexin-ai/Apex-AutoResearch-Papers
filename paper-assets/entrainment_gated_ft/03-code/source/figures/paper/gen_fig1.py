import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os
from palette import BLUE, CORAL, TEAL, AMBER, GRAY, DARK, LIGHT, RCPARAMS

plt.rcParams.update(RCPARAMS)

attn_ratios_a = [0, 4, 7.7, 14.3, 25]
sigma_1_3B    = [0.02405, 0.01624, 0.01360, 0.00606, 0.00494]
sigma_340M    = [0.0248,  0.0116,  0.0178,  0.0110,  0.0160]

attn_ratios_b = [4, 7.7, 14.3, 25]
j_helped      = [0.0945, 0.0951, 0.0922, 0.1002]
j_hurt        = [0.0873, 0.0809, 0.0988, 0.0928]

sigma_1_3B_ci_lower = [0.01930, 0.01162, 0.00969, 0.00240, 0.00180]
sigma_1_3B_ci_upper = [0.02955, 0.02172, 0.02019, 0.01165, 0.01057]

j_helped_ci_lower = [0.0826, 0.0834, 0.0790, 0.0844]
j_helped_ci_upper = [0.1066, 0.1075, 0.1023, 0.1088]
j_hurt_ci_lower   = [0.0745, 0.0667, 0.0857, 0.0814]
j_hurt_ci_upper   = [0.0978, 0.0891, 0.1105, 0.1057]

fig, (ax_a, ax_b) = plt.subplots(
    1, 2, figsize=(3.35, 1.90),
    gridspec_kw={'width_ratios': [1, 1], 'wspace': 0.58}
)

# === Panel (a): Aggregate σ decreases ===
ax_a.fill_between(attn_ratios_a, sigma_1_3B_ci_lower, sigma_1_3B_ci_upper,
                  color=BLUE, alpha=0.10, zorder=1, linewidth=0)
ax_a.plot(attn_ratios_a, sigma_1_3B, '-o', color=BLUE,
          linewidth=1.2, markersize=3.5, label='1.3B', zorder=3,
          markeredgecolor='white', markeredgewidth=0.3)
ax_a.plot(attn_ratios_a, sigma_340M, '--', color=GRAY,
          linewidth=0.7, zorder=2, alpha=0.50)
ax_a.plot(attn_ratios_a, sigma_340M, '^', color=GRAY,
          markersize=4.0, zorder=3, markeredgecolor='white', markeredgewidth=0.3,
          label='340M', alpha=0.50)

# Endpoint σ values for immediate quantification
t0 = ax_a.text(0.3, sigma_1_3B[0] + 0.0004, '.024', fontsize=5, color=BLUE,
               va='bottom', ha='left', alpha=0.6)
t0.set_path_effects([pe.withStroke(linewidth=1.2, foreground='white')])
t1 = ax_a.text(25.8, sigma_1_3B[-1], '.005', fontsize=5, color=BLUE,
               va='center', ha='left', alpha=0.6)
t1.set_path_effects([pe.withStroke(linewidth=1.2, foreground='white')])

ax_a.set_xlabel('Attention ratio (%)')
ax_a.set_ylabel(r'Cross-arch. $\sigma$')
ax_a.set_xticks(attn_ratios_a)
ax_a.set_xticklabels(['0', '4', '7.7', '14.3', '25'])
ax_a.set_ylim(0.002, 0.032)
ax_a.legend(loc='upper right', frameon=False, handlelength=1.2,
            borderpad=0.2, handletextpad=0.3)
ax_a.yaxis.set_major_locator(plt.MultipleLocator(0.010))
ax_a.grid(axis='y', alpha=0.08, linewidth=0.3, zorder=0, color='#AAAAAA')
ax_a.set_title(r'(a) Aggregate $\sigma$ decreases', fontsize=7, pad=4,
               fontstyle='italic', color='#555555')

# === Panel (b): Per-example J stays flat ===
# Independence baseline reference
ax_b.axhspan(0.035, 0.054, color='#F5F5F5', zorder=0)
ax_b.axhline(y=0.05, color='#CCCCCC', linewidth=0.4, linestyle=':', zorder=1)
t_ref = ax_b.text(14.5, 0.044, 'independence baseline', fontsize=4.5,
                  color='#999999', va='center', ha='center', fontstyle='italic')

ax_b.fill_between(attn_ratios_b, j_helped_ci_lower, j_helped_ci_upper,
                  color=DARK, alpha=0.06, zorder=1, linewidth=0)
ax_b.fill_between(attn_ratios_b, j_hurt_ci_lower, j_hurt_ci_upper,
                  color=DARK, alpha=0.04, zorder=1, linewidth=0)

ax_b.plot(attn_ratios_b, j_helped, '-o', color=DARK,
          linewidth=1.0, markersize=3.5, label='$J$(helped)', zorder=3,
          markeredgecolor='white', markeredgewidth=0.3)
ax_b.plot(attn_ratios_b, j_hurt, '--D', color=DARK,
          linewidth=0.8, markersize=3, markerfacecolor='white',
          markeredgecolor=DARK, markeredgewidth=0.6,
          label='$J$(hurt)', zorder=3)

ax_b.set_xlabel('Attention ratio (%)')
ax_b.set_ylabel('Pairwise Jaccard')
ax_b.set_xticks(attn_ratios_b)
ax_b.set_xticklabels(['4', '7.7', '14.3', '25'])
ax_b.set_ylim(0.035, 0.120)
ax_b.legend(loc='lower right', frameon=False, handlelength=1.2,
            borderpad=0.2, handletextpad=0.3,
            bbox_to_anchor=(1.0, 0.15))
ax_b.grid(axis='y', alpha=0.08, linewidth=0.3, zorder=0, color='#AAAAAA')
ax_b.set_title('(b) Per-example $J$ stays flat', fontsize=7, pad=4,
               fontstyle='italic', color='#555555')

out_dir = os.path.dirname(os.path.abspath(__file__))
paper_fig_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures'
os.makedirs(paper_fig_dir, exist_ok=True)

for d in [out_dir, paper_fig_dir]:
    fig.savefig(os.path.join(d, 'fig1_decoupling_hero.pdf'))
    fig.savefig(os.path.join(d, 'fig1_decoupling_hero.png'), dpi=300)
plt.close()
print('Saved fig1_decoupling_hero')
