#!/usr/bin/env python3
"""fig_rsa_perlayer_curve: Per-layer RSA rho for trained/reference OpenVLA."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Liberation Serif',
    'mathtext.it': 'Liberation Serif:italic',
    'mathtext.bf': 'Liberation Serif:bold',
    'font.size': 9,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
})

ti_m = np.array([0.6117, 0.6124, 0.6121, 0.6127, 0.6137, 0.6146, 0.6175, 0.6201,
                  0.6187, 0.6199, 0.6198, 0.6169, 0.6282, 0.6266, 0.6243, 0.6172,
                  0.6128, 0.6088, 0.6071, 0.6072, 0.6041, 0.5959, 0.572, 0.5558,
                  0.5459, 0.5346, 0.5159, 0.5136, 0.5125, 0.4971, 0.4395, 0.4328, 0.4223])
tp_m = np.array([np.nan, 0.5682, 0.5818, 0.588, 0.5892, 0.5836, 0.5617, 0.543,
                  0.5469, 0.5682, 0.5577, 0.5993, 0.6425, 0.6395, 0.6374, 0.6348,
                  0.6303, 0.6261, 0.6227, 0.6194, 0.6164, 0.6086, 0.606, 0.6003,
                  0.595, 0.5855, 0.5812, 0.5822, 0.5814, 0.5787, 0.5724, 0.5703, 0.5843])
ui_m = np.array([0.6117, 0.5712, 0.5604, 0.5597, 0.5576, 0.5576, 0.5588, 0.557,
                  0.5553, 0.5532, 0.551, 0.5509, 0.5496, 0.5496, 0.5494, 0.5493,
                  0.5497, 0.5495, 0.55, 0.5495, 0.5488, 0.5487, 0.5497, 0.5497,
                  0.5494, 0.5482, 0.548, 0.5467, 0.5457, 0.5454, 0.5454, 0.5448, 0.5446])
up_m = np.array([np.nan, 0.6262, 0.6207, 0.6156, 0.6119, 0.6084, 0.6053, 0.6029,
                  0.6013, 0.6008, 0.5977, 0.5966, 0.5953, 0.5939, 0.5934, 0.5936,
                  0.5941, 0.595, 0.5947, 0.5945, 0.5938, 0.5936, 0.5927, 0.5917,
                  0.5913, 0.5907, 0.5895, 0.5888, 0.5879, 0.5885, 0.5883, 0.587, 0.5866])

ti_lo = np.array([0.5184, 0.51, 0.5145, 0.5105, 0.5123, 0.5191, 0.5248, 0.5259, 0.518,
                   0.5248, 0.5277, 0.5137, 0.5312, 0.5246, 0.5252, 0.5151, 0.5088, 0.5041,
                   0.507, 0.4906, 0.4972, 0.4842, 0.4565, 0.4363, 0.4244, 0.4104, 0.3848,
                   0.3881, 0.3931, 0.3635, 0.3206, 0.3095, 0.3027])
ti_hi = 2 * ti_m - ti_lo

tp_lo = np.array([np.nan, 0.4548, 0.4752, 0.4871, 0.4916, 0.4838, 0.4557, 0.4342,
                   0.44, 0.4602, 0.4462, 0.4925, 0.5482, 0.5443, 0.5413, 0.5385,
                   0.5335, 0.5281, 0.5269, 0.5261, 0.5196, 0.5099, 0.5036, 0.4968,
                   0.4918, 0.4788, 0.4757, 0.4788, 0.4786, 0.475, 0.4682, 0.4664, 0.485])
tp_hi = 2 * tp_m - tp_lo

# Optimized color scheme: readout=blue, image_mean=orange; solid=trained, dashed=reference
C_READOUT = '#2166AC'
C_IMAGE   = '#E69F00'
C_READOUT_REF = '#92C5DE'
C_IMAGE_REF   = '#F0B27A'

fig, ax = plt.subplots(figsize=(7, 3.2))
layers = list(range(33))

ax.plot(layers, ti_m, '-', color=C_IMAGE, linewidth=1.8, label='Trained, image_mean', zorder=4)
ax.fill_between(layers, ti_lo, ti_hi, color=C_IMAGE, alpha=0.12, zorder=2)

valid = ~np.isnan(tp_m)
l_valid = np.array(layers)[valid]
ax.plot(l_valid, tp_m[valid], '-', color=C_READOUT, linewidth=1.8, label='Trained, readout', zorder=4)
ax.fill_between(l_valid, tp_lo[valid], tp_hi[valid], color=C_READOUT, alpha=0.12, zorder=2)

ax.plot(layers, ui_m, '--', color=C_IMAGE_REF, linewidth=1.3, label='Reference, image_mean', zorder=3)
valid_u = ~np.isnan(up_m)
l_valid_u = np.array(layers)[valid_u]
ax.plot(l_valid_u, up_m[valid_u], '--', color=C_READOUT_REF, linewidth=1.3, label='Reference, readout', zorder=3)

ti_peak = int(np.nanargmax(ti_m))
tp_peak = int(np.nanargmax(tp_m))
ax.plot(ti_peak, ti_m[ti_peak], 'v', color=C_IMAGE, markersize=7, zorder=5)
ax.plot(tp_peak, tp_m[tp_peak], 'v', color=C_READOUT, markersize=7, zorder=5)

ax.annotate('L%d (%.3f)' % (tp_peak, tp_m[tp_peak]),
            xy=(tp_peak, tp_m[tp_peak]), xytext=(tp_peak + 3, tp_m[tp_peak] + 0.022),
            fontsize=7.5, color=C_READOUT,
            arrowprops=dict(arrowstyle='-', color=C_READOUT, lw=0.6))
ax.annotate('L%d (%.3f)' % (ti_peak, ti_m[ti_peak]),
            xy=(ti_peak, ti_m[ti_peak]), xytext=(ti_peak - 8, ti_m[ti_peak] - 0.032),
            fontsize=7.5, color=C_IMAGE,
            arrowprops=dict(arrowstyle='-', color=C_IMAGE, lw=0.6))

ax.set_xlabel('Layer Index', fontsize=10)
ax.set_ylabel(r'RSA $\rho$ (Spearman)', fontsize=10)
ax.set_xlim(-0.5, 32.5)
ax.set_xticks([0, 4, 8, 12, 16, 20, 24, 28, 32])
ax.grid(True, alpha=0.25, linewidth=0.5, color='#888888')
ax.set_ylim(0.40, 0.75)
ax.legend(fontsize=7.5, loc='upper right', framealpha=0.9, edgecolor='#cccccc')
ax.tick_params(labelsize=8.5)

plt.tight_layout(pad=0.4)

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dirs = [
    os.path.join(_REPO_ROOT, 'docs', 'paper', 'figures'),
    os.path.join(_REPO_ROOT, 'artifacts', 'figures', 'paper'),
    os.path.join(_REPO_ROOT, 'artifacts', '_project', 'chart'),
]
for d in out_dirs:
    os.makedirs(d, exist_ok=True)
    fig.savefig(os.path.join(d, 'fig_rsa_perlayer_curve.pdf'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(d, 'fig_rsa_perlayer_curve.png'), dpi=300, bbox_inches='tight')

plt.close()
print('Saved fig_rsa_perlayer_curve.')
