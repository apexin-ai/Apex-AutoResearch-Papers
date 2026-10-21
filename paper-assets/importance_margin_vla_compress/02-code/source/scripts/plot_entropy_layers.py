import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

smolvla_ratio = [0.9826, 0.9561, 0.9597, 0.9434, 0.9408, 0.9406, 0.9474, 0.9628,
                 0.9614, 0.9572, 0.9455, 0.9510, 0.9485, 0.9311, 0.9482, 0.9566]
smolvla_std = [0.0011, 0.0021, 0.0025, 0.0026, 0.0034, 0.0034, 0.0034, 0.0023,
               0.0026, 0.0027, 0.0036, 0.0034, 0.0032, 0.0050, 0.0037, 0.0038]

openvla_ratio = [0.979, 0.9523, 0.7995, 0.7256, 0.7008, 0.678, 0.688, 0.6744,
                 0.6514, 0.6526, 0.6612, 0.6505, 0.622, 0.6508, 0.6618, 0.622,
                 0.6372, 0.6069, 0.597, 0.5662, 0.5672, 0.5904, 0.5861, 0.5806,
                 0.5653, 0.5719, 0.5709, 0.5419, 0.5298, 0.4774, 0.5241, 0.5739]
openvla_std = [0.0088, 0.0216, 0.0667, 0.0847, 0.1023, 0.1252, 0.1107, 0.1049,
               0.0941, 0.0766, 0.0692, 0.0704, 0.0634, 0.0796, 0.0761, 0.0966,
               0.0785, 0.0762, 0.0761, 0.0766, 0.0734, 0.0766, 0.0756, 0.0798,
               0.0806, 0.0695, 0.0842, 0.0695, 0.0717, 0.0702, 0.0750, 0.1141]

smolvla_x = np.arange(len(smolvla_ratio)) / (len(smolvla_ratio) - 1)
openvla_x = np.arange(len(openvla_ratio)) / (len(openvla_ratio) - 1)

smolvla_ratio = np.array(smolvla_ratio)
smolvla_std = np.array(smolvla_std)
openvla_ratio = np.array(openvla_ratio)
openvla_std = np.array(openvla_std)

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'legend.fontsize': 7,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
})

fig, ax = plt.subplots(figsize=(3.5, 2.5))

c_smol = '#2166AC'
c_open = '#D6604D'

ax.plot(smolvla_x, smolvla_ratio, color=c_smol, linewidth=1.4, marker='o',
        markersize=3, label=f'SmolVLA (16L, avg={0.95:.2f})', zorder=3)
ax.fill_between(smolvla_x, smolvla_ratio - smolvla_std, smolvla_ratio + smolvla_std,
                color=c_smol, alpha=0.18, zorder=2)

ax.plot(openvla_x, openvla_ratio, color=c_open, linewidth=1.4, marker='s',
        markersize=2.5, linestyle='--', label=f'OpenVLA (32L, avg={0.64:.2f})', zorder=3)
ax.fill_between(openvla_x, openvla_ratio - openvla_std, openvla_ratio + openvla_std,
                color=c_open, alpha=0.18, zorder=2)

ax.axhline(y=1.0, color='#AAAAAA', linestyle=':', linewidth=0.8, zorder=1)
ax.text(0.02, 1.005, '$H_{\\mathrm{max}}$', fontsize=6.5, color='#888888',
        va='bottom', ha='left', transform=ax.get_yaxis_transform())

ax.set_xlabel('Relative Depth (layer / total layers)')
ax.set_ylabel('Entropy Ratio ($H / H_{\\mathrm{max}}$)')
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(0.35, 1.08)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', color='#E0E0E0', linewidth=0.5, zorder=0)

ax.legend(loc='lower left', frameon=True, fancybox=False, edgecolor='#CCCCCC',
          framealpha=0.95, borderpad=0.4)

fig.tight_layout(pad=0.4)

out = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/fig_entropy_layers.pdf'
fig.savefig(out, dpi=300, bbox_inches='tight')
plt.close()

import os
size = os.path.getsize(out)
print(f"Saved: {out}")
print(f"File size: {size} bytes")
