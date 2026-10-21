#!/usr/bin/env python3
"""Generate NVE ROC curve and PRF threshold plots (D165-updated, τ=2.0)."""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# --- Dataset: D165-updated labels + new experiments ---
# Format: (name, env, nve_peak, civo_label)
# D165 changes from plan034: 009b_s2/008d_s3/018_s1 → No-CIVO; 008e_v3_s2 → CIVO
DATA = [
    # CIVO positive (9 experiments, min NVE = 3.78)
    ("006",         "walker",   4.83,   1),
    ("008d_s1",     "walker",   4.12,   1),
    ("008d_s4",     "walker",   4.62,   1),
    ("059_s5",      "walker",   4.72,   1),
    ("008e_v3_s2",  "walker",   3.78,   1),
    ("008e_v3_s3",  "walker",   4.02,   1),
    ("010b",        "cheetah",  8.27,   1),
    ("010b_s0",     "cheetah", 108.52,  1),
    ("021",         "cheetah",  9.94,   1),
    # No-CIVO (27 experiments, max NVE = 1.88)
    # Walker — original no-CIVO
    ("001_s1",      "walker",   1.00,   0),
    ("008f_s1",     "walker",   0.97,   0),
    ("008f_s4",     "walker",   1.41,   0),
    ("009c_s3",     "walker",   1.04,   0),
    ("008a_s0",     "walker",   0.93,   0),
    ("008a_s1",     "walker",   0.83,   0),
    ("008a_s2",     "walker",   0.89,   0),
    ("015b",        "walker",   1.45,   0),
    ("022b",        "walker",   0.63,   0),
    ("042",         "walker",   0.19,   0),
    ("047",         "walker",   1.71,   0),
    ("057",         "walker",   1.88,   0),
    ("008e_v3_s1",  "walker",   0.94,   0),
    ("008e_v3_s4",  "walker",   0.99,   0),
    # Walker — relabeled from CIVO (D165/D167)
    ("009b_s2",     "walker",   1.62,   0),
    ("008d_s3",     "walker",   1.53,   0),
    ("018_s1",      "walker",   1.66,   0),
    # Cheetah — original no-CIVO
    ("024b_s0",     "cheetah",  0.20,   0),
    ("024b_s1",     "cheetah",  0.10,   0),
    ("008a_ch_s0",  "cheetah",  1.08,   0),
    ("008a_ch_s1",  "cheetah",  1.29,   0),
    ("046",         "cheetah",  1.35,   0),
    ("058",         "cheetah",  0.78,   0),
    # New experiments (post-D165)
    ("008f_s0",     "walker",   1.69,   0),
    ("no_dt_s1",    "walker",   0.88,   0),
    ("ch_008a_s0",  "cheetah",  0.449,  0),
    ("ch_008a_s1",  "cheetah",  0.584,  0),
]

labels = np.array([d[3] for d in DATA])
scores = np.array([d[2] for d in DATA])
n_pos = labels.sum()
n_neg = len(labels) - n_pos

# --- ROC computation ---
thresholds_roc = np.sort(np.unique(np.concatenate([scores, [0.0, max(scores) + 1]])))
thresholds_roc = np.sort(thresholds_roc)[::-1]

tpr_list, fpr_list = [], []
for t in thresholds_roc:
    pred = (scores >= t).astype(int)
    tp = ((pred == 1) & (labels == 1)).sum()
    fp = ((pred == 1) & (labels == 0)).sum()
    tpr_list.append(tp / n_pos if n_pos > 0 else 0)
    fpr_list.append(fp / n_neg if n_neg > 0 else 0)

fpr_arr = np.array(fpr_list)
tpr_arr = np.array(tpr_list)

# AUROC via trapezoidal rule
sorted_idx = np.argsort(fpr_arr)
fpr_sorted = fpr_arr[sorted_idx]
tpr_sorted = tpr_arr[sorted_idx]
auroc = np.trapz(tpr_sorted, fpr_sorted)

# --- PRF computation ---
thresholds_prf = np.linspace(0.0, max(scores.max(), 10.0), 500)
precision_arr = np.zeros(len(thresholds_prf))
recall_arr = np.zeros(len(thresholds_prf))
f1_arr = np.zeros(len(thresholds_prf))

for i, t in enumerate(thresholds_prf):
    pred = (scores >= t).astype(int)
    tp = ((pred == 1) & (labels == 1)).sum()
    fp = ((pred == 1) & (labels == 0)).sum()
    fn = ((pred == 0) & (labels == 1)).sum()
    p = tp / (tp + fp) if (tp + fp) > 0 else 1.0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    precision_arr[i] = p
    recall_arr[i] = r
    f1_arr[i] = f

# Operating point at τ=2.0
tau = 2.0
pred_tau = (scores >= tau).astype(int)
tp_tau = ((pred_tau == 1) & (labels == 1)).sum()
fp_tau = ((pred_tau == 1) & (labels == 0)).sum()
fn_tau = ((pred_tau == 0) & (labels == 1)).sum()
tn_tau = ((pred_tau == 0) & (labels == 0)).sum()
p_tau = tp_tau / (tp_tau + fp_tau) if (tp_tau + fp_tau) > 0 else 1.0
r_tau = tp_tau / (tp_tau + fn_tau) if (tp_tau + fn_tau) > 0 else 0.0
f1_tau = 2 * p_tau * r_tau / (p_tau + r_tau) if (p_tau + r_tau) > 0 else 0.0
fpr_tau = fp_tau / n_neg if n_neg > 0 else 0.0
tpr_tau = r_tau

civo_min = scores[labels == 1].min()
nocivo_max = scores[labels == 0].max()

print(f"N = {len(DATA)} ({n_pos} CIVO + {n_neg} No-CIVO)")
print(f"AUROC = {auroc:.4f}")
print(f"τ=2.0: TP={tp_tau} FP={fp_tau} FN={fn_tau} TN={tn_tau} P={p_tau:.3f} R={r_tau:.3f} F1={f1_tau:.3f}")
print(f"CIVO min NVE = {civo_min:.2f}, No-CIVO max NVE = {nocivo_max:.2f}")
print(f"Separation gap: [{nocivo_max:.2f}, {civo_min:.2f}]")

# --- Style ---
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 13,
    'axes.titlesize': 14,
    'legend.fontsize': 10,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# === Figure 1: ROC Curve ===
fig1, ax1 = plt.subplots(figsize=(4.5, 4.2))

ax1.plot(fpr_sorted, tpr_sorted, color='#2166ac', linewidth=2.0, zorder=3)
ax1.plot([0, 1], [0, 1], '--', color='#999999', linewidth=0.8, zorder=1)

# Operating point
ax1.plot(fpr_tau, tpr_tau, marker='*', color='#d6604d', markersize=16, zorder=5,
         markeredgecolor='#b2182b', markeredgewidth=0.8)
ax1.annotate(
    f'$\\tau$=2.0\n(FPR=0, TPR=1)',
    xy=(fpr_tau, tpr_tau),
    xytext=(0.25, 0.72),
    fontsize=9.5,
    color='#b2182b',
    fontweight='bold',
    arrowprops=dict(arrowstyle='->', color='#b2182b', lw=1.2),
    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#b2182b', alpha=0.9),
)

# AUROC annotation
ax1.text(0.55, 0.15, f'AUROC = {auroc:.3f}',
         transform=ax1.transAxes, fontsize=12, fontweight='bold',
         color='#2166ac',
         bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#2166ac', alpha=0.9))

ax1.set_xlabel('False Positive Rate')
ax1.set_ylabel('True Positive Rate')
ax1.set_xlim(-0.02, 1.02)
ax1.set_ylim(-0.02, 1.08)
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.25, linewidth=0.5)
ax1.set_title(f'NVE CIVO Detection — ROC (N={len(DATA)})')

fig1.tight_layout()
fig1.savefig('/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/nve_roc_curve.pdf')
fig1.savefig('/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/nve_roc_curve.png')
print("Saved nve_roc_curve.pdf/png")

# === Figure 2: PRF Curve ===
fig2, ax2 = plt.subplots(figsize=(5.5, 4.0))

ax2.plot(thresholds_prf, precision_arr, color='#4393c3', linewidth=1.8, label='Precision')
ax2.plot(thresholds_prf, recall_arr, color='#f4a582', linewidth=1.8, label='Recall')
ax2.plot(thresholds_prf, f1_arr, color='#2166ac', linewidth=2.2, label='F1')

# Operating point vertical line
ax2.axvline(x=tau, color='#d6604d', linewidth=1.5, linestyle='--', alpha=0.8, zorder=4)
ax2.plot(tau, f1_tau, marker='*', color='#d6604d', markersize=16, zorder=5,
         markeredgecolor='#b2182b', markeredgewidth=0.8)

# Separation gap shading
ax2.axvspan(nocivo_max, civo_min, alpha=0.10, color='#4daf4a', zorder=1)
ax2.annotate(
    f'separation gap\n[{nocivo_max:.2f}, {civo_min:.2f}]',
    xy=((nocivo_max + civo_min) / 2, 0.5),
    fontsize=8.5, ha='center', color='#2d7d2d', style='italic',
)

# τ=2.0 annotation
ax2.annotate(
    f'$\\tau$=2.0\nF1={f1_tau:.2f}',
    xy=(tau, f1_tau),
    xytext=(tau + 1.5, 0.78),
    fontsize=10, fontweight='bold', color='#b2182b',
    arrowprops=dict(arrowstyle='->', color='#b2182b', lw=1.2),
    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#b2182b', alpha=0.9),
)

ax2.set_xlabel('NVE Threshold ($\\tau$)')
ax2.set_ylabel('Score')
ax2.set_xlim(0, 6.0)
ax2.set_ylim(-0.02, 1.12)
ax2.grid(True, alpha=0.25, linewidth=0.5)
ax2.legend(loc='lower left', framealpha=0.9, edgecolor='#cccccc')
ax2.set_title(f'NVE CIVO Detection — Precision / Recall / F1 (N={len(DATA)})')

fig2.tight_layout()
fig2.savefig('/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/nve_threshold_prf.pdf')
fig2.savefig('/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/nve_threshold_prf.png')
print("Saved nve_threshold_prf.pdf/png")

plt.close('all')
