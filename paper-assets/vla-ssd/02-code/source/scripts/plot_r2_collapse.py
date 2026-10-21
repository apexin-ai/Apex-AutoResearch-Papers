#!/usr/bin/env python3
"""fig_r2_collapse: Three-panel per-layer R² profile (demo-split, bootstrap v3 MCCV)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Liberation Serif',
    'mathtext.it': 'Liberation Serif:italic',
    'mathtext.bf': 'Liberation Serif:bold',
    'font.size': 10,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

TRAINED      = '#0077BB'
TRAINED_EDGE = '#005588'
REFERENCE    = '#EE7733'
REF_EDGE     = '#CC5500'
NLP_GRAY     = '#AAAAAA'
ANNO_COLOR   = '#444444'
DELTA_SHADE  = '#F0F0F0'

# ── Demo-split per-layer R² (bootstrap v3 MCCV) ─────────────

L32 = np.arange(32)
L36 = np.arange(36)

# OpenVLA Goal trained: Peak L1, R²=0.418, Exit=0.331, ΔR²=0.086
openvla_tr = np.array([
    0.3329, 0.4177, 0.3571, 0.2243, 0.3962, 0.3624, 0.3390, 0.3076,
    0.2634, 0.2185, 0.4051, 0.3818, 0.3879, 0.3797, 0.3693, 0.3475,
    0.3410, 0.3418, 0.3293, 0.3235, 0.3190, 0.2901, 0.2764, 0.2825,
    0.2729, 0.2701, 0.2672, 0.2672, 0.4067, 0.3964, 0.3888, 0.3313])

# OpenVLA Goal reference (untrained): Peak L27, R²=0.423, Exit=0.367, ΔR²=0.056
openvla_ref = np.array([
    0.3256, 0.3964, 0.3521, 0.2713, 0.3598, 0.3436, 0.3228, 0.3094,
    0.3144, 0.3049, 0.3893, 0.3787, 0.3794, 0.3576, 0.3615, 0.3550,
    0.3396, 0.3484, 0.3390, 0.3338, 0.3308, 0.3105, 0.2984, 0.2840,
    0.4066, 0.4066, 0.4122, 0.4230, 0.4111, 0.4080, 0.3994, 0.3672])

NLP_VAL = 0.155

# TraceVLA Goal trained: Peak L13, R²=0.540, Exit=0.207, ΔR²=0.333
tracvla_tr = np.array([
    0.4550, 0.5002, 0.5105, 0.5059, 0.4393, 0.4509, 0.4767, 0.4736,
    0.4390, 0.5085, 0.5063, 0.4576, 0.4935, 0.5399, 0.5241, 0.4993,
    0.4998, 0.4547, 0.4685, 0.4149, 0.4452, 0.4244, 0.3947, 0.3503,
    0.2975, 0.2535, 0.2392, 0.1033, -0.0845, -0.1402, -0.4649, 0.2065])

# TraceVLA Goal reference (untrained): Peak L11, R²=0.505, Exit=0.440, ΔR²=0.065
tracvla_ref = np.array([
    0.4305, 0.4554, 0.4816, 0.4982, 0.4775, 0.4805, 0.4699, 0.4394,
    0.4493, 0.4916, 0.4870, 0.5048, 0.4626, 0.4641, 0.4141, 0.4814,
    0.4519, 0.4284, 0.4110, 0.4034, 0.3982, 0.4950, 0.4841, 0.4803,
    0.4708, 0.4671, 0.4537, 0.4209, 0.3699, 0.3528, 0.4700, 0.4403])

# NORA Goal trained: Peak L8, R²=0.449, Exit=-0.006, ΔR²=0.455
nora_tr = np.array([
    0.3683, 0.3361, 0.3191, 0.3626, 0.3550, 0.3564, 0.3921, 0.3838,
    0.4489, 0.4457, 0.4290, 0.4378, 0.4315, 0.4372, 0.4456, 0.4294,
    0.4071, 0.4058, 0.3767, 0.3639, 0.3527, 0.3491, 0.3185, 0.3133,
    0.3723, 0.3724, 0.3649, 0.3649, 0.3650, 0.3382, 0.2892, 0.2892,
    0.2769, 0.2769, 0.2773, -0.0062])

# NORA Goal reference (untrained): Peak L5, R²=0.420, Exit=0.340, ΔR²=0.081
nora_ref = np.array([
    0.3856, 0.3904, 0.3824, 0.3929, 0.3513, 0.4203, 0.3890, 0.3817,
    0.2603, 0.2475, 0.2566, 0.2681, 0.3183, 0.3262, 0.3468, 0.3561,
    0.3846, 0.3678, 0.4024, 0.3946, 0.3976, 0.4016, 0.4085, 0.3745,
    0.3534, 0.3478, 0.3084, 0.3002, 0.3774, 0.3783, 0.3709, 0.3646,
    0.3462, 0.3072, 0.2794, 0.3397])

# ── Plot ──────────────────────────────────────────────────────

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

ylims = [(0.05, 0.55), (-0.55, 0.65), (-0.10, 0.55)]

nlp_labels = [
    'NLP control (Llama-2-chat)',
    'NLP control (Phi-3-instruct)',
    'NLP control (Qwen2.5-Instruct)',
]

configs = [
    # ax, title, layers, trained, ref, peak_idx, peak_r2, delta_r2, peak_text_xy, delta_text_xy
    (axes[0], 'OpenVLA (VLA→VLA)', L32, openvla_tr, openvla_ref,
     1, 0.418, 0.086, (12, 0.50), (20, 0.18)),
    (axes[1], 'TraceVLA (VLM→VLA)', L32, tracvla_tr, tracvla_ref,
     13, 0.540, 0.333, (4, 0.62),  (25, -0.35)),
    (axes[2], 'NORA (VLM→VLA)',    L36, nora_tr,    nora_ref,
     8, 0.449, 0.455, (20, 0.52), (30, 0.05)),
]

for idx, (ax, title, layers, tr, ref, pi, pv, dr2, pk_xy, dr_xy) in enumerate(configs):
    ei = int(layers[-1])
    ax.axvspan(pi, ei, color=DELTA_SHADE, alpha=0.10, zorder=0)

    ax.plot(layers, tr, '-o', color=TRAINED, linewidth=2.0, markersize=3,
            markerfacecolor=TRAINED, markeredgecolor=TRAINED_EDGE, markeredgewidth=0.5,
            label='Trained', zorder=3)

    ax.plot(layers, ref, '--s', color=REFERENCE, linewidth=1.5, markersize=2.5,
            markerfacecolor=REFERENCE, markeredgecolor=REF_EDGE, markeredgewidth=0.5,
            label='Reference', zorder=2)

    ax.axhline(NLP_VAL, linestyle=':', color=NLP_GRAY, linewidth=1.5,
               label=nlp_labels[idx], zorder=1)

    ax.scatter(pi, pv, marker='*', s=100, color=ANNO_COLOR, zorder=5,
               edgecolors='white', linewidths=0.3)

    ax.annotate(f'Peak $R^2$ = {pv:.3f} (L{pi})',
                xy=(pi, pv), xytext=pk_xy,
                fontsize=9.5, color=ANNO_COLOR, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=ANNO_COLOR, lw=0.8, shrinkB=3),
                zorder=6)

    ax.text(dr_xy[0], dr_xy[1],
            f'$\\Delta R^2$ = {dr2:.3f}',
            fontsize=10, color=ANNO_COLOR, alpha=0.85, ha='center', va='center',
            fontweight='bold', zorder=4)

    ax.set_title(title, fontweight='bold', fontsize=13, pad=4)
    ax.set_xlabel('Layer index', fontsize=11)
    ax.set_xlim(-0.5, layers[-1] + 0.5)
    ax.set_ylim(ylims[idx])
    ax.set_ylabel('$R^2$', fontsize=11)
    ax.grid(True, alpha=0.15, linewidth=0.5)
    ax.legend(loc='lower left', framealpha=0.9, edgecolor='none',
              borderpad=0.3, handlelength=1.8, fontsize=9)

plt.subplots_adjust(wspace=0.22)
plt.tight_layout(pad=0.3)

# ── Save ──────────────────────────────────────────────────────

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dirs = [
    os.path.join(_REPO_ROOT, 'docs', 'paper', 'figures'),
    os.path.join(_REPO_ROOT, 'artifacts', 'figures', 'paper'),
]
for d in out_dirs:
    os.makedirs(d, exist_ok=True)
    plt.savefig(os.path.join(d, 'fig_r2_collapse.pdf'), dpi=300)
    plt.savefig(os.path.join(d, 'fig_r2_collapse.png'), dpi=300)

plt.close()
print('Saved fig_r2_collapse to both output directories.')
