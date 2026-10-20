import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 6.5,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 2.5,
    'ytick.major.size': 2.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

variants = ['9-Class', 'Binary', 'Scrambled', 'JB-MLM', 'Wiki-MLM', 'Topic', 'Vanilla']

dd_mean = [0.997, 1.000, 0.997, 0.914, 0.904, 0.541, 0.312]
dd_std  = [0.005, 0.000, 0.005, 0.115, 0.115, 0.207, 0.026]

aa_mean = [0.972, 0.990, 0.951, 0.893, 0.686, 0.625, 0.258]
aa_std  = [0.026, 0.008, 0.043, 0.080, 0.297, 0.141, 0.000]

tc_mean = [0.596, 0.705, 0.616, 0.837, 0.791, 0.496, 0.413]
tc_std  = [0.087, 0.072, 0.056, 0.013, 0.093, 0.042, 0.021]

n = len(variants)
x = np.arange(n)
bar_w = 0.22

fig, ax = plt.subplots(figsize=(3.25, 2.0))

ax.bar(x - bar_w, dd_mean, bar_w, yerr=dd_std,
       color='#2166ac', edgecolor='white', linewidth=0.3,
       error_kw=dict(lw=0.8, capsize=2, capthick=0.6),
       label='DD OOD', zorder=3)

ax.bar(x, aa_mean, bar_w, yerr=aa_std,
       color='#67a9cf', edgecolor='white', linewidth=0.3,
       error_kw=dict(lw=0.8, capsize=2, capthick=0.6),
       label='AA OOD', zorder=3)

ax.bar(x + bar_w, tc_mean, bar_w, yerr=tc_std,
       color='#ef8a62', edgecolor='white', linewidth=0.3,
       error_kw=dict(lw=0.8, capsize=2, capthick=0.6),
       label='ToxicChat', zorder=3)

ax.set_ylabel('F1 Score', fontsize=8)
ax.set_ylim(0.0, 1.05)
ax.set_xticks(x)
ax.set_xticklabels(variants, rotation=45, ha='right', fontsize=7)
ax.tick_params(axis='y', labelsize=7)
ax.tick_params(axis='x', labelsize=7)

ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.grid(axis='y', linestyle='--', linewidth=0.4, color='#cccccc', zorder=0)
ax.set_axisbelow(True)

ax.legend(fontsize=6, loc='upper right', frameon=True, fancybox=False,
          edgecolor='#cccccc', framealpha=0.9, handlelength=1.0,
          handletextpad=0.4, borderpad=0.3, labelspacing=0.3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy'
fig.savefig(out_base + '.pdf', bbox_inches='tight', pad_inches=0.02)
fig.savefig(out_base + '.png', bbox_inches='tight', pad_inches=0.02, dpi=300)
plt.close()
print('OK')
