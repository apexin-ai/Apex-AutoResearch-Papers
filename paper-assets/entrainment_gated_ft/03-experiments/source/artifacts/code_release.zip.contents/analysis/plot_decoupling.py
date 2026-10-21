import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'lines.linewidth': 1.5,
    'figure.dpi': 300,
})

CB_BLUE = '#0072B2'
CB_ORANGE = '#D55E00'
CB_GREEN = '#009E73'

df = pd.read_csv("/root/entrainment_gated_ft/analysis/paper_data/fig1_decoupling_data.csv")

# Drop pure for Jaccard (NaN), keep for sigma
df_sigma = df.copy()
df_jaccard = df.dropna(subset=['mean_jaccard_helped']).copy()

fig, ax1 = plt.subplots(figsize=(7, 3.8))

# Left axis: Cross-architecture σ (decreasing)
ln1 = ax1.plot(df_sigma['attention_ratio'], df_sigma['cross_arch_std'],
               color=CB_BLUE, marker='o', markersize=6, zorder=3,
               label=r'Cross-arch $\sigma$')
ax1.set_xlabel('Attention ratio', fontsize=12)
ax1.set_ylabel(r'Cross-arch $\sigma$', color=CB_BLUE, fontsize=12)
ax1.tick_params(axis='y', labelcolor=CB_BLUE)
ax1.set_ylim(0, 0.028)

# Right axis: Mean Jaccard helped (saturates early)
ax2 = ax1.twinx()
ln2 = ax2.plot(df_jaccard['attention_ratio'], df_jaccard['mean_jaccard_helped'],
               color=CB_ORANGE, marker='s', markersize=6, linestyle='--', zorder=3,
               label='Mean Jaccard (helped)')
ln3 = ax2.plot(df_jaccard['attention_ratio'], df_jaccard['mean_net_asymmetry'],
               color=CB_GREEN, marker='^', markersize=6, linestyle=':', zorder=3,
               label='Net asymmetry')
ax2.set_ylabel('Jaccard / Asymmetry', color='#333333', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#333333')
ax2.set_ylim(0, 0.12)

# Shading: Jaccard saturation zone (0.04–0.25)
ax1.axvspan(0.04, 0.25, alpha=0.07, color='grey', zorder=0)
ax1.annotate('Jaccard saturated;\n' + r'$\sigma$ still declining',
             xy=(0.145, 0.0025), fontsize=9, color='#555555',
             ha='center', style='italic')

# X-axis ticks at data points
xticks = df_sigma['attention_ratio'].tolist()
xlabels = ['0\n(pure)', '0.04\n(h24-1)', '0.08\n(h12-1)', '0.14\n(h6-1)', '0.25\n(h3-1)']
ax1.set_xticks(xticks)
ax1.set_xticklabels(xlabels, fontsize=10)

# Remove grid
ax1.grid(False)
ax2.grid(False)

# Combined legend
lns = ln1 + ln2 + ln3
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='upper right', fontsize=9, frameon=False)

# Spines
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

plt.tight_layout()

out_dir = "/root/entrainment_gated_ft/analysis/figures"
fig.savefig(f"{out_dir}/fig_decoupling.pdf", bbox_inches='tight')
fig.savefig(f"{out_dir}/fig_decoupling.png", bbox_inches='tight', dpi=300)
plt.close()

print(f"Saved: {out_dir}/fig_decoupling.pdf")
print(f"Saved: {out_dir}/fig_decoupling.png")
