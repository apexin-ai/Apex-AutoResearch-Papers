import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
})

injection = [0, 10, 25, 50]
taxei     = [61.7, 61.7, 48.9, 51.1]
random_   = [61.7, 68.1, 55.3, 57.4]

c_taxei  = '#D55E00'
c_random = '#0072B2'
c_vanilla = '#888888'

fig, ax = plt.subplots(figsize=(3.5, 2.5))

ax.axhline(y=61.7, color=c_vanilla, linestyle=':', linewidth=1.0, zorder=1,
           label='Vanilla (no injection)')

ax.plot(injection, taxei, color=c_taxei, marker='o', markersize=5,
        linestyle='-', label='TaxEI', zorder=3)
ax.plot(injection, random_, color=c_random, marker='s', markersize=5,
        linestyle='--', label='Random', zorder=3)

# Annotation: vertical drop bracket between 10% and 25% for TaxEI
x_annot = 16.0
ax.annotate('', xy=(x_annot, 49.5), xytext=(x_annot, 61.1),
            arrowprops=dict(arrowstyle='<->', color='#555555', lw=1.2,
                            shrinkA=0, shrinkB=0))
ax.text(x_annot - 1.0, 55.3, u'−12.8 pp', fontsize=7, color='#444444',
        va='center', ha='right',
        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85))

ax.set_xlabel('Injection Ratio (%)')
ax.set_ylabel('Clean Eval Accuracy (%)')
ax.set_xticks(injection)
ax.set_xlim(-3, 55)
ax.set_ylim(43, 75)
ax.yaxis.set_major_locator(plt.MultipleLocator(5))

ax.legend(loc='upper right', frameon=True, framealpha=0.9, edgecolor='#cccccc',
          borderpad=0.4, handlelength=1.8)

out = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/figures/paper/fig1_dose_response'
fig.savefig(out + '.pdf', format='pdf')
fig.savefig(out + '.png', format='png')
plt.close(fig)
print('Done.')
