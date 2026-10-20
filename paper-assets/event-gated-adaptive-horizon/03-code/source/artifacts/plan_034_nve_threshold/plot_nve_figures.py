import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from collections import OrderedDict

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
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

OUT_DIR = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold'

# ── Raw data: all 56 samples (24 CIVO + 32 Healthy) ──
civo_nves = [
    4.835, 1.530, 4.620, 4.124, 4.020, 3.780, 1.620, 4.130,
    8.270, 70.640, 9.940, 3.965, 1.637, 2.765, 3.000, 10.666,
    3.300, 4.500, 2.300, 3.600, 4.910, 2.750, 4.720, 4.120,
]
healthy_nves = [
    0.490, 0.478, 0.930, 0.598, 0.463, 0.990, 1.930, 0.803,
    1.020, 1.490, 1.410, 0.520, 0.467, 0.983, 0.200, 0.100,
    0.908, 0.643, 1.100, 1.400, 0.194, 0.808, 1.350, 1.710,
    1.880, 0.780, 0.400, 0.660, 0.800, 0.974, 0.610, 0.760,
]

n_pos = len(civo_nves)
n_neg = len(healthy_nves)

# ── Compute full ROC curve ──
all_nve = sorted(set(civo_nves + healthy_nves), reverse=True)
roc_thresholds = [max(all_nve) + 1.0] + all_nve + [min(all_nve) - 1.0]

roc_raw = []
for t in roc_thresholds:
    tp = sum(1 for v in civo_nves if v >= t)
    fp = sum(1 for v in healthy_nves if v >= t)
    tpr = tp / n_pos
    fpr = fp / n_neg
    roc_raw.append((fpr, tpr))

roc_raw.sort(key=lambda x: (x[0], x[1]))
unique_fpr = OrderedDict()
for fpr, tpr in roc_raw:
    if fpr not in unique_fpr or tpr > unique_fpr[fpr]:
        unique_fpr[fpr] = tpr
roc_points = list(unique_fpr.items())

fprs = [p[0] for p in roc_points]
tprs = [p[1] for p in roc_points]

auroc = sum((fprs[i] - fprs[i-1]) * (tprs[i-1] + tprs[i]) / 2.0
            for i in range(1, len(fprs)))

# ── FPR/TPR at recommended threshold 1.5 ──
tp_15 = sum(1 for v in civo_nves if v >= 1.5)
fp_15 = sum(1 for v in healthy_nves if v >= 1.5)
fpr_15 = fp_15 / n_neg
tpr_15 = tp_15 / n_pos

# ══════════════════════════════════════════════════════════
# Figure 1: ROC Curve
# ══════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(3.5, 3.5))

ax.plot([0, 1], [0, 1], linestyle='--', color='#AAAAAA', linewidth=0.8, zorder=1)
ax.plot(fprs, tprs, color='#0072B2', linewidth=2.0, zorder=3, solid_capstyle='round')
ax.fill_between(fprs, tprs, alpha=0.05, color='#0072B2', zorder=2)

ax.plot(fpr_15, tpr_15, 'o', color='#D55E00', markersize=7,
        markeredgecolor='white', markeredgewidth=1.2, zorder=5)
t = ax.annotate(
    r'$\tau$=1.5',
    xy=(fpr_15, tpr_15),
    xytext=(fpr_15 + 0.14, tpr_15 - 0.10),
    fontsize=9, color='#D55E00', fontweight='bold',
    arrowprops=dict(arrowstyle='->', color='#D55E00', lw=1.0),
    zorder=6,
)
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax.text(0.97, 0.03, f'AUROC = {auroc:.3f}',
        transform=ax.transAxes, ha='right', va='bottom',
        fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                  edgecolor='#CCCCCC', alpha=0.9))

ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.05)
ax.set_aspect('equal')

plt.tight_layout()
for ext in ['pdf', 'png']:
    fig.savefig(f'{OUT_DIR}/fig_roc_curve.{ext}')
plt.close()
print(f'Saved fig_roc_curve.pdf/.png  (AUROC={auroc:.4f})')

# ══════════════════════════════════════════════════════════
# Figure 2: Threshold vs Precision / Recall / F1
# ══════════════════════════════════════════════════════════
thresholds = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4,
              1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.5, 3.0]
precisions, recalls, f1s = [], [], []
for t in thresholds:
    tp = sum(1 for v in civo_nves if v >= t)
    fp = sum(1 for v in healthy_nves if v >= t)
    fn = sum(1 for v in civo_nves if v < t)
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
    precisions.append(prec)
    recalls.append(rec)
    f1s.append(f1)

fig, ax = plt.subplots(figsize=(4.5, 3.2))

ax.plot(thresholds, precisions, '-o', color='#0072B2', markersize=4,
        markeredgecolor='white', markeredgewidth=0.8, label='Precision',
        linewidth=1.5, zorder=3)
ax.plot(thresholds, recalls, '-s', color='#009E73', markersize=3.5,
        markeredgecolor='white', markeredgewidth=0.6, label='Recall',
        linewidth=1.2, alpha=0.75, zorder=3)
ax.plot(thresholds, f1s, '-D', color='#D55E00', markersize=4.5,
        markeredgecolor='white', markeredgewidth=0.8, label='F1',
        linewidth=2.0, zorder=4)

best_idx = f1s.index(max(f1s))
ax.plot(thresholds[best_idx], f1s[best_idx], 'D', color='#D55E00',
        markersize=8, markeredgecolor='white', markeredgewidth=1.5, zorder=5)

ax.text(0.97, 0.03,
        f'Peak F1 = {f1s[best_idx]:.3f}\nat $\\tau$={thresholds[best_idx]:.1f}',
        transform=ax.transAxes, ha='right', va='bottom',
        fontsize=9, fontweight='bold', color='#D55E00',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                  edgecolor='#CCCCCC', alpha=0.9))

ax.axvline(x=1.5, color='#CC79A7', linestyle='--', linewidth=1.2, alpha=0.7, zorder=2)
t = ax.text(1.55, 0.15, r'$\tau$=1.5',
            fontsize=9, color='#CC79A7', fontweight='bold', rotation=90, va='bottom')
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax.set_xlabel('NVE Threshold')
ax.set_ylabel('Score')
ax.set_xlim(0.4, 3.1)
ax.set_ylim(-0.02, 1.05)
ax.legend(loc='lower left', framealpha=0.9, edgecolor='#CCCCCC')

plt.tight_layout()
for ext in ['pdf', 'png']:
    fig.savefig(f'{OUT_DIR}/fig_threshold_prf.{ext}')
plt.close()
print('Saved fig_threshold_prf.pdf/.png')

print('Done.')
