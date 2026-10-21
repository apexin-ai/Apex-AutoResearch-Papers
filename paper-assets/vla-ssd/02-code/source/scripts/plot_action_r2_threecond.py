#!/usr/bin/env python3
"""fig_action_r2_threecond: Per-layer action-probe R² for three OpenVLA conditions."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Liberation Serif',
    'mathtext.it': 'Liberation Serif:italic',
    'mathtext.bf': 'Liberation Serif:bold',
})
import numpy as np
import os

layers = np.arange(32)

trained_mean = np.array([0.6451, 0.6429, 0.6221, 0.6211, 0.6386, 0.6304, 0.6421, 0.6339,
    0.6362, 0.6434, 0.6245, 0.6245, 0.6205, 0.6348, 0.6282, 0.6391,
    0.6246, 0.6185, 0.6008, 0.5961, 0.5907, 0.5946, 0.5899, 0.5490,
    0.5711, 0.5696, 0.5557, 0.5221, 0.4963, 0.5153, 0.5186, 0.4724])
trained_std = np.array([0.0084, 0.0072, 0.0061, 0.0226, 0.0073, 0.0144, 0.0053, 0.0084,
    0.0184, 0.0137, 0.0162, 0.0182, 0.0084, 0.0039, 0.0067, 0.0081,
    0.0132, 0.0117, 0.0341, 0.0063, 0.0187, 0.0149, 0.0050, 0.0800,
    0.0205, 0.0161, 0.0354, 0.0679, 0.0646, 0.0451, 0.0034, 0.0671])

llama2base_mean = np.array([0.6451, 0.6276, 0.6204, 0.6287, 0.6279, 0.6220, 0.6271, 0.6321,
    0.6202, 0.6271, 0.6287, 0.6284, 0.6344, 0.6136, 0.6053, 0.6085,
    0.6137, 0.6062, 0.6117, 0.6032, 0.5788, 0.5875, 0.5860, 0.5905,
    0.5810, 0.5690, 0.5755, 0.5689, 0.5607, 0.5814, 0.5619, 0.5571])
llama2base_std = np.array([0.0084, 0.0098, 0.0088, 0.0115, 0.0197, 0.0076, 0.0106, 0.0041,
    0.0077, 0.0078, 0.0086, 0.0086, 0.0131, 0.0128, 0.0159, 0.0038,
    0.0018, 0.0069, 0.0225, 0.0148, 0.0278, 0.0184, 0.0073, 0.0047,
    0.0117, 0.0112, 0.0089, 0.0274, 0.0111, 0.0068, 0.0027, 0.0111])

untrained_mean = np.array([0.6451, 0.5470, 0.5202, 0.5361, 0.5147, 0.3973, 0.5048, 0.5033,
    0.4985, 0.4416, -0.0924, 0.1408, 0.2114, 0.2237, 0.4157, 0.5108,
    0.4242, 0.4500, 0.2569, 0.4703, 0.3451, 0.2755, -0.0631, 0.3638,
    0.4605, 0.2013, 0.3528, 0.2881, -0.0822, 0.1137, 0.1700, 0.1928])
untrained_std = np.array([0.0084, 0.0080, 0.0036, 0.0078, 0.0440, 0.1950, 0.0453, 0.0510,
    0.0411, 0.0668, 0.3342, 0.2991, 0.3536, 0.3627, 0.0715, 0.0123,
    0.0534, 0.0454, 0.1712, 0.0280, 0.1310, 0.1474, 0.3767, 0.1977,
    0.0405, 0.3765, 0.1109, 0.1623, 0.3156, 0.3250, 0.3541, 0.1379])

TRAINED_COLOR = '#2166AC'
LLAMA2_COLOR = '#EE7733'
UNTRAINED_COLOR = '#999999'

fig, ax = plt.subplots(figsize=(5.0, 3.0))

ax.plot(layers, trained_mean, '-o', color=TRAINED_COLOR, markersize=3, linewidth=1.5,
        label='VLA-trained', zorder=4)
ax.fill_between(layers, trained_mean - trained_std, trained_mean + trained_std,
                color=TRAINED_COLOR, alpha=0.15, zorder=2)

ax.plot(layers, llama2base_mean, '--s', color=LLAMA2_COLOR, markersize=3, linewidth=1.5,
        label='Llama-2 base', zorder=3)
ax.fill_between(layers, llama2base_mean - llama2base_std, llama2base_mean + llama2base_std,
                color=LLAMA2_COLOR, alpha=0.15, zorder=1)

ax.plot(layers, untrained_mean, ':^', color=UNTRAINED_COLOR, markersize=3, linewidth=1.5,
        label='Random init.', zorder=3)
ax.fill_between(layers, untrained_mean - untrained_std, untrained_mean + untrained_std,
                color=UNTRAINED_COLOR, alpha=0.10, zorder=1)

ax.axhline(y=0.645, color='gray', linestyle='--', alpha=0.3, linewidth=0.8)
ax.text(31.5, 0.650, 'L0 baseline', fontsize=7, color='gray', ha='right', va='bottom')

ax.set_xlabel('Layer', fontsize=10)
ax.set_ylabel('Action-probe $R^2$', fontsize=10)
ax.set_xlim(-0.5, 31.5)
ax.set_ylim(-0.15, 0.75)
ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
ax.tick_params(labelsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.2, linewidth=0.5)

ax.legend(loc='lower left', fontsize=8, framealpha=0.9, edgecolor='#CCCCCC',
          borderpad=0.4, handlelength=1.5)

plt.tight_layout(pad=0.3)

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dirs = [
    os.path.join(_REPO_ROOT, 'docs', 'paper', 'figures'),
    os.path.join(_REPO_ROOT, 'artifacts', 'figures', 'paper'),
]
for d in out_dirs:
    os.makedirs(d, exist_ok=True)
    fig.savefig(os.path.join(d, 'fig_action_r2_threecond.pdf'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(d, 'fig_action_r2_threecond.png'), dpi=300, bbox_inches='tight')

plt.close()
print('Saved fig_action_r2_threecond.')
