"""Generate signal reversal figure: label distribution across three environments.

Three-panel grouped bar chart showing:
- ScienceWorld (N=245): strong det preference from death avoidance
- ALFWorld (N=135): moderate det preference from info gap (different mechanism)
- MATH (N=795): balanced labels, no routing signal (no catastrophic failure)
"""
import paper_style; paper_style.apply_style()
import matplotlib.pyplot as plt
import numpy as np
import os

envs = [
    'SciWorld\n(N=245)',
    'ALFWorld\n(N=135)',
    'MATH\n(N=795)',
]
det_pref = [35.1, 25.9, 7.3]
int_pref = [3.7, 1.5, 8.3]
no_pref = [61.2, 72.6, 84.4]

x = np.arange(len(envs))
width = 0.22

fig, ax = plt.subplots(figsize=(3.25, 2.6))

bars1 = ax.bar(x - width, det_pref, width, label='Det-preferred',
               color=paper_style.C_DETERMINISTIC, alpha=0.9,
               **paper_style.bar_edge_style())
bars2 = ax.bar(x, int_pref, width, label='Int-preferred',
               color=paper_style.C_INTERNAL, alpha=0.9,
               **paper_style.bar_edge_style())
bars3 = ax.bar(x + width, no_pref, width, label='No-preference',
               color=paper_style.C_NEUTRAL, alpha=0.65,
               **paper_style.bar_edge_style())

ax.set_ylabel('Proportion (%)')
ax.set_xticks(x)
ax.set_xticklabels(envs)
leg = ax.legend(loc='upper center', ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.12),
                fontsize=6.5)
ax.set_ylim(0, 95)

paper_style.add_y_grid(ax)

for gi, bars in enumerate([bars1, bars2, bars3]):
    for bi, bar in enumerate(bars):
        h = bar.get_height()
        y_off = 3
        if bi == 2 and gi < 2 and abs(det_pref[bi] - int_pref[bi]) < 5:
            y_off = 10 if gi == 1 else 3
        ax.annotate(f'{h:.1f}%',
                    xy=(bar.get_x() + bar.get_width()/2, h),
                    xytext=(0, y_off), textcoords='offset points',
                    ha='center', va='bottom', fontsize=6)

ax.axvline(x=1.5, color=paper_style.C_NEUTRAL, linestyle='--', linewidth=0.6, alpha=0.5)

ax.text(0.5, 92, 'death-prone', fontsize=6.5, ha='center', va='bottom',
        color='#555', style='italic')
ax.text(2.0, 92, 'death-free', fontsize=6.5, ha='center', va='bottom',
        color='#555', style='italic')

out_dir = os.path.dirname(os.path.abspath(__file__))
plt.tight_layout()
for ext in ('pdf', 'png'):
    path = os.path.join(out_dir, f'signal_reversal.{ext}')
    plt.savefig(path, bbox_inches='tight', pad_inches=0.08, dpi=300)
plt.close()
print(f"Saved: {os.path.join(out_dir, 'signal_reversal.pdf')} ({os.path.getsize(os.path.join(out_dir, 'signal_reversal.pdf'))} bytes)")
