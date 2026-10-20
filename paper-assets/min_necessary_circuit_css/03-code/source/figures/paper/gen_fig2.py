import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

methods = ['CSS=1.0', 'ACDC\ntop-16', 'EAP-IG\ntop-16', 'EP\ntop-16', 'Random-16']
colors = ['#D55E00', '#E69F00', '#0072B2', '#56B4E9', '#999999']

zero_cpr = [0.0295, 0.0295, -0.0585, -0.0585, -0.05]
mean_cpr = [0.177, 0.177, 0.182, 0.183, 0.05]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5), sharey=False)

x = np.arange(len(methods))
bar_width = 0.6

# Left panel: Zero Ablation
bars1 = ax1.bar(x, zero_cpr, width=bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=2)
ax1.set_title('(a) Zero Ablation', fontweight='bold')
ax1.set_ylabel('CPR (↑ better)')
ax1.set_xticks(x)
ax1.set_xticklabels(methods, fontsize=9)
ax1.axhline(y=0, color='#CCCCCC', linestyle='--', linewidth=0.8, zorder=1)
ax1.set_ylim(-0.075, 0.065)

# "identical" annotation for CSS=1.0 and ACDC top-16
y_top = max(zero_cpr[0], zero_cpr[1]) + 0.008
ax1.annotate('', xy=(0, y_top + 0.005), xytext=(1, y_top + 0.005),
             arrowprops=dict(arrowstyle='<->', color='#444444', lw=1.2))
ax1.text(0.5, y_top + 0.012, 'identical', ha='center', va='bottom', fontsize=9,
         color='#444444', fontstyle='italic')

# Right panel: Mean Ablation
bars2 = ax2.bar(x, mean_cpr, width=bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=2)
ax2.set_title('(b) Mean Ablation', fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(methods, fontsize=9)
ax2.axhline(y=0, color='#CCCCCC', linestyle='--', linewidth=0.8, zorder=1)
ax2.set_ylim(0, 0.22)

# "identical" annotation for CSS=1.0 and ACDC top-16 in mean panel too
y_top_m = max(mean_cpr[0], mean_cpr[1]) + 0.005
ax2.annotate('', xy=(0, y_top_m + 0.003), xytext=(1, y_top_m + 0.003),
             arrowprops=dict(arrowstyle='<->', color='#444444', lw=1.2))
ax2.text(0.5, y_top_m + 0.008, 'identical', ha='center', va='bottom', fontsize=9,
         color='#444444', fontstyle='italic')

# Star on best bar (EP top-16, index 3, value 0.183)
best_idx = 3
ax2.text(best_idx, mean_cpr[best_idx] + 0.005, '★ best', ha='center', va='bottom',
         fontsize=9, color='#56B4E9', fontweight='bold')

plt.tight_layout(w_pad=3)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper'
plt.savefig(f'{outdir}/fig2_size_controlled.pdf')
plt.savefig(f'{outdir}/fig2_size_controlled.png')
plt.close()
print('Done.')
