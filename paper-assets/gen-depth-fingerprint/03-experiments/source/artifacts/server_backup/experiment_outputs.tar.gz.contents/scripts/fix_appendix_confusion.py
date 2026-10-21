import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

cm = np.array([
    [5937, 35, 0],
    [368, 4437, 1113],
    [464, 3646, 11529]
])
cm_pct = cm / cm.sum(axis=1, keepdims=True) * 100

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

ax = axes[0]
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
            xticklabels=['Pred gen-0', 'Pred gen-1', 'Pred gen-2+'],
            yticklabels=['True gen-0', 'True gen-1', 'True gen-2+'],
            linewidths=0.5, linecolor='white', cbar_kws={'label': 'Count'})
ax.set_title('(a) Raw Counts (N = 27,529)', fontsize=11, fontweight='bold')
ax.set_xlabel('Predicted', fontsize=10)
ax.set_ylabel('Actual', fontsize=10)

ax = axes[1]
annot_labels = np.array([[f'{v:.1f}%' for v in row] for row in cm_pct])
sns.heatmap(cm_pct, annot=annot_labels, fmt='', cmap='Oranges', ax=ax,
            xticklabels=['Pred gen-0', 'Pred gen-1', 'Pred gen-2+'],
            yticklabels=['True gen-0', 'True gen-1', 'True gen-2+'],
            linewidths=0.5, linecolor='white', vmin=0, vmax=100,
            cbar_kws={'label': 'Recall (%)'})
ax.set_title('(b) Row-Normalized (%)', fontsize=11, fontweight='bold')
ax.set_xlabel('Predicted', fontsize=10)
ax.set_ylabel('Actual', fontsize=10)

plt.tight_layout(pad=2.0)
plt.savefig('/root/gen-depth-fingerprint/chart/fig_appendix_confusion.pdf', bbox_inches='tight', dpi=300)
print("Saved fig_appendix_confusion.pdf")
