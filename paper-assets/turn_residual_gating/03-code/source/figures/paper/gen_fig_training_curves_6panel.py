#!/usr/bin/env python3
"""Item 8: 6-panel training curves (NTP + GAR loss) for all conditions."""
import sys, json
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np
from matplotlib.lines import Line2D

apply_style()

with open('/tmp/training_data.json') as f:
    all_data = json.load(f)


def to_global_steps(steps):
    global_steps = []
    offset = 0
    for i, s in enumerate(steps):
        if i > 0 and s < steps[i - 1]:
            step_size = steps[1] - steps[0]
            offset = global_steps[-1] + step_size
        global_steps.append(s + offset)
    return np.array(global_steps)


def smooth(y, window=5):
    if len(y) <= window:
        return y
    kernel = np.ones(window) / window
    return np.convolve(y, kernel, mode='valid')


def find_epoch_boundaries(steps):
    boundaries = []
    for i in range(1, len(steps)):
        if steps[i] < steps[i - 1]:
            boundaries.append(i)
    return boundaries


conditions = [
    ('tg', 'ThreadGate', C_TG),
    ('ug', 'Uniform Gate', C_UG),
    ('lo', 'LoRA-only', C_LO),
    ('pcgrad', 'PCGrad', C_PC),
    ('ss', 'Sched. Sampling', C_SS),
]

fig, axes = plt.subplots(3, 2, figsize=(5.0, 5.0))
axes_flat = axes.flatten()

for idx, (key, label, color) in enumerate(conditions):
    ax = axes_flat[idx]
    d = all_data[key]
    raw_steps = d['steps']
    steps = to_global_steps(raw_steps)
    ntp = np.array(d['ntp'])
    gar = np.array(d['gar'])

    epoch_bounds = find_epoch_boundaries(raw_steps)
    epoch_global = [steps[b] - (raw_steps[1] - raw_steps[0]) / 2 for b in epoch_bounds]

    win = 5 if len(ntp) > 20 else 3
    ntp_s = smooth(ntp, win)
    gar_s = smooth(gar, win)
    s_offset = (win - 1) // 2
    steps_s = steps[s_offset:s_offset + len(ntp_s)]

    ax.plot(steps_s, ntp_s, color='#333333', linewidth=1.2)
    ax.set_ylabel(r'$\mathcal{L}_{\mathrm{NTP}}$', fontsize=8)
    ax.set_xlabel('Step', fontsize=8)
    ax.set_title(label, fontsize=9, color=color, fontweight='bold')
    ax.tick_params(axis='y', labelsize=7)
    ax.tick_params(axis='x', labelsize=7, rotation=0)

    for eb in epoch_global:
        ax.axvline(eb, color=C_GRAY, linewidth=0.4, linestyle=':', alpha=0.5)

    if steps_s[-1] > 5000:
        from matplotlib.ticker import FuncFormatter
        ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x/1000:.0f}k'))

    if np.max(gar) > 0.001:
        ax2 = ax.twinx()
        ax2.plot(steps_s, gar_s, color=C_GAR, linewidth=1.0, linestyle='--', alpha=0.8)
        ax2.set_ylabel(r'$\mathcal{L}_{\mathrm{GAR}}$', fontsize=8, color=C_GAR)
        ax2.tick_params(axis='y', labelcolor=C_GAR, labelsize=7)
        ax2.spines['right'].set_visible(True)
        ax2.spines['right'].set_color(C_GAR)
        ax2.spines['right'].set_alpha(0.4)
        ax2.spines['top'].set_visible(False)

ax6 = axes_flat[5]
ax6.axis('off')
legend_elements = [
    Line2D([0], [0], color='#333333', linewidth=1.2,
           label=r'$\mathcal{L}_{\mathrm{NTP}}$ (left axis)'),
    Line2D([0], [0], color=C_GAR, linewidth=1.0, linestyle='--',
           label=r'$\mathcal{L}_{\mathrm{GAR}}$ (right axis)'),
    Line2D([0], [0], color=C_GRAY, linewidth=0.4, linestyle=':',
           label='Epoch boundary'),
]
ax6.legend(handles=legend_elements, loc='center', fontsize=8, frameon=False)
ax6.text(0.5, 0.18, 'Base (LoRA w/o GAR)\ntraining log unavailable',
         ha='center', va='center', fontsize=7, color=C_GRAY,
         transform=ax6.transAxes, style='italic')

fig.tight_layout(h_pad=1.5, w_pad=1.2)
save_fig(fig, 'fig_training_curves_6panel')
print("Done: fig_training_curves_6panel")
