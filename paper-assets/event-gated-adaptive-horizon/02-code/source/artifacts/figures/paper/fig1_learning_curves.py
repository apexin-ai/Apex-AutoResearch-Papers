import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_style import apply_style
apply_style()

# --- Data ---
steps_base = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
eval_base = [31.77, 206.61, 395.27, 388.47, 513.77, 625.73, 615.86, 596.28, 713.93, 871.06, 915.67]

steps_006 = [5, 15, 25, 35, 45, 55, 65]
eval_006 = [31, 256.9, 321.4, 485.3, 477, 360.4, 132.86]

steps_007 = [5, 15, 25, 35, 45, 55]
eval_007 = [31, 129.6, 176.9, 126.7, 144.41, 152.49]

steps_005 = [5, 15, 35, 55, 65, 85, 105]
eval_005 = [31, 153.9, 290.8, 541.18, 465.67, 212.34, 276.08]

steps_008a = [35, 45, 55, 65, 75, 85, 95, 105]
eval_008a = [500.84, 563.41, 487.92, 608, 469.93, 583.73, 572.24, 777.66]

steps_008d = [25, 35, 45, 55]
eval_008d = [167.22, 146.34, 140.80, 82.75]

steps_008e_s1 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
eval_008e_s1 = [31, 131.2, 155.7, 276.5, 382.2, 486.8, 580.7, 574.1, 657.3, 851.9, 869.9]

steps_008e_s2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
eval_008e_s2 = [39.27, 180.85, 211.82, 320.39, 356.93, 418.32, 435.09, 576.54, 715.21, 452.43, 136.96]

# --- Plot ---
fig, ax = plt.subplots(figsize=(5.5, 3.5))
fig.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.14)

# Baseline
ax.plot(steps_base, eval_base, color='#0072B2', linestyle='-', linewidth=2.5,
        label='Baseline (dt=1)', zorder=5)

# Fixed dt>1
ax.plot(steps_006, eval_006, color='#D55E00', linestyle='-',
        label='Fixed dt=2 (006)')
ax.plot(steps_007, eval_007, color='#CC79A7', linestyle='-',
        label='Fixed dt=4 (007)')

# Learned gate
ax.plot(steps_005, eval_005, color='#E69F00', linestyle='--',
        label='Learned gate (005)')

# Factorial ablations
ax.plot(steps_008a, eval_008a, color='#009E73', linestyle='-',
        label='008a: untrained emb, H=15')
ax.plot(steps_008d, eval_008d, color='#D55E00', linestyle='--',
        marker='o', markersize=5, label='008d: trained emb, sub, H=8')
ax.plot(steps_008e_s1, eval_008e_s1, color='#56B4E9', linestyle='-',
        label='008e_v3 s1 (870@105K)')
ax.plot(steps_008e_s2, eval_008e_s2, color='#56B4E9', linestyle='--', alpha=0.6,
        marker='^', markersize=4, markevery=2,
        label='008e_v3 s2 (collapsed)')

# Collapse marker on 008d endpoint (orange Wong, was red #CC0000)
ax.plot(steps_008d[-1], eval_008d[-1], marker='X', color='#D55E00',
        markersize=10, zorder=6, markeredgecolor='#A04800', markeredgewidth=1.2)
ax.annotate('collapse', (steps_008d[-1], eval_008d[-1]),
            textcoords='offset points', xytext=(8, -2),
            fontsize=8, color='#D55E00', style='italic')

# Collapse marker on 008e_v3 s2 endpoint (orange Wong, was red #CC0000)
ax.plot(steps_008e_s2[-1], eval_008e_s2[-1], marker='X', color='#D55E00',
        markersize=10, zorder=6, markeredgecolor='#A04800', markeredgewidth=1.2)
ax.annotate('collapse', (steps_008e_s2[-1], eval_008e_s2[-1]),
            textcoords='offset points', xytext=(8, 6),
            fontsize=8, color='#D55E00', style='italic')

# Reference line
ax.axhline(y=915.67, color='#0072B2', linestyle=':', linewidth=1.0, alpha=0.5)
ax.text(107, 915.67, 'baseline\n@105K', fontsize=8, color='#0072B2',
        va='center', ha='left', alpha=0.7)

ax.set_xlim(0, 115)
ax.set_ylim(0, 1000)
ax.set_xlabel('Training Steps (K)', fontsize=12)
ax.set_ylabel('Eval Return', fontsize=12)
ax.tick_params(labelsize=10)
ax.legend(loc='upper left', frameon=True, framealpha=0.9, edgecolor='#CCCCCC',
          borderpad=0.6, handlelength=2.2, fontsize=8)

ax.grid(axis='y', alpha=0.2)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper'
plt.rcParams['savefig.bbox'] = None
fig.savefig(f'{out_dir}/fig1_learning_curves.pdf')
fig.savefig(f'{out_dir}/fig1_learning_curves.png')
plt.close(fig)
print('Saved fig1_learning_curves.pdf and .png')
