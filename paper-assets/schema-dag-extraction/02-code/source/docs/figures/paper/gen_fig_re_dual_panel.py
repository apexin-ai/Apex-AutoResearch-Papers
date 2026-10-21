import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# --- Panel A: Count Curve ---
counts = np.array([1, 4, 8, 16, 32, 40, 64, 80])
accs = np.array([0.8573, 0.8667, 0.8021, 0.6958, 0.6578, 0.5880, 0.5424, 0.5042])

mask_normal = counts != 40
mask_40 = counts == 40

ax1.plot(counts[mask_normal], accs[mask_normal], 'o-', color='#2166AC', markersize=7, linewidth=1.8, zorder=3)
# connect through count=40 with dashed segment
idx_32 = np.where(counts == 32)[0][0]
idx_40 = np.where(counts == 40)[0][0]
idx_64 = np.where(counts == 64)[0][0]
ax1.plot([counts[idx_32], counts[idx_40], counts[idx_64]],
         [accs[idx_32], accs[idx_40], accs[idx_64]],
         '--', color='#2166AC', linewidth=1.2, zorder=2)
ax1.plot(counts[mask_40], accs[mask_40], '^', color='#D6604D', markersize=9, zorder=4,
         label='40-type subset (from 80-rel pool)')

ax1.set_xscale('log', base=2)
ax1.set_xticks(counts)
ax1.set_xticklabels([str(c) for c in counts])
ax1.set_xlim(0.7, 110)
ax1.set_ylim(0.40, 1.0)
ax1.set_xlabel('Number of relation types')
ax1.set_ylabel('Accuracy')
ax1.legend(loc='upper right', fontsize=9, framealpha=0.9)
ax1.text(0.02, 0.98, '(a)', transform=ax1.transAxes, fontsize=13, fontweight='bold', va='top')

# --- Panel B: BCS-Controlled ---
count_labels = ['8', '16']
low_bcs = [0.8229, 0.8281]
high_bcs = [0.5104, 0.5156]
delta_ci_lower = [-42.7, -39.6]
delta_ci_upper = [-17.7, -22.9]
delta_val = [-31.2, -31.2]

x_pos = np.array([0, 1])
width = 0.3

bars_low = ax2.bar(x_pos - width/2, low_bcs, width, color='#4393C3', label='Low BCS', zorder=3)
bars_high = ax2.bar(x_pos + width/2, high_bcs, width, color='#D6604D', label='High BCS', zorder=3)

for i in range(2):
    mid_y = (low_bcs[i] + high_bcs[i]) / 2
    ax2.annotate('', xy=(x_pos[i] + width/2 + 0.05, high_bcs[i]),
                 xytext=(x_pos[i] - width/2 - 0.05, low_bcs[i]),
                 arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.5))
    ci_text = f'Δ = {delta_val[i]:.1f} pp\n[{delta_ci_lower[i]:.1f}, {delta_ci_upper[i]:.1f}]'
    ax2.text(x_pos[i] + width + 0.12, mid_y, ci_text, fontsize=9, va='center', color='#333333')

ax2.set_xticks(x_pos)
ax2.set_xticklabels(count_labels)
ax2.set_xlabel('Number of relation types')
ax2.set_ylabel('Accuracy')
ax2.set_ylim(0.40, 1.0)
ax2.set_xlim(-0.6, 1.8)
ax2.legend(loc='upper right', fontsize=9, framealpha=0.9)
ax2.text(0.02, 0.98, '(b)', transform=ax2.transAxes, fontsize=13, fontweight='bold', va='top')

plt.tight_layout(w_pad=3)
out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/figures/paper/fig_re_dual_panel.pdf'
fig.savefig(out_path, bbox_inches='tight', dpi=300)
plt.close()
print(f'Saved: {out_path}')
