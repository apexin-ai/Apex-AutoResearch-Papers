import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_style import apply_style
apply_style()
plt.rcParams.update({
    'font.weight': 'bold',
    'axes.labelweight': 'bold',
    'axes.titleweight': 'bold',
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
})

# === Muted academic palette (seaborn-inspired) ===
C_CIVO_1   = '#C44E52'  # muted red — CIVO onset seed
C_CIVO_2   = '#DD8452'  # muted orange — CIVO transient seed
C_CTRL_1   = '#55A868'  # muted green — no-emb control
C_CTRL_2   = '#8C8C8C'  # gray — no-emb control 2
C_DT1_1    = '#4C72B0'  # muted blue — dt=1 imagination
C_DT1_2    = '#8172B3'  # muted purple — dt=1 late-onset
C_BASELINE = '#4C72B0'  # muted blue — baseline reference
C_THRESH   = '#937860'  # muted brown — threshold

# === TOP PANEL DATA: NVE trajectories ===
experiments = {
    '008d/009e s1': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.78, 1.71, 2.09, 4.12, 1.23, 1.48, 1.15, 1.73, 1.57],
        'color': C_CIVO_1, 'linestyle': '-', 'marker': 'o',
    },
    '009b s2': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [2.05, 1.24, 1.62, 1.41, 0.94, 0.66, 0.51, 0.43, 0.38],
        'color': C_CIVO_2, 'linestyle': '-', 'marker': 's',
    },
    '008f s1 (no emb)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.02, 0.73, 0.83, 0.97, 0.37, 0.42, 0.65, 0.54, 0.30],
        'color': C_CTRL_1, 'linestyle': '--', 'marker': '^',
    },
    '009c s2 (no emb)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.26, 0.79, 0.72, 0.66, 0.53, 0.33, 0.60, 0.90, 1.14],
        'color': C_CTRL_2, 'linestyle': '--', 'marker': 'v',
    },
    '008e_v3 s1 (dt=1)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.93, 0.94, 0.88, 0.87, 0.72, 0.73, 0.76, 0.75, 0.80],
        'color': C_DT1_1, 'linestyle': '-.', 'marker': 'P',
    },
    '008e_v3 s2 (late)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.64, 1.03, 1.06, 1.02, 0.90, 0.66, 0.68, 1.34, 3.78],
        'color': C_DT1_2, 'linestyle': '-.', 'marker': 'X',
    },
}

# === BOTTOM PANEL DATA: Actor loss ===
actor_loss_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'actor_loss_data.json')
actor_loss_data = {}
if os.path.exists(actor_loss_file):
    with open(actor_loss_file) as f:
        raw = json.load(f)
    if 'exp_001_baseline' in raw and raw['exp_001_baseline']:
        entries = [e for e in raw['exp_001_baseline'] if e['step'] <= 105000]
        actor_loss_data['baseline'] = {
            'steps': [e['step'] for e in entries],
            'actor_loss': [e['actor_loss'] for e in entries],
        }
    if 'exp_009b_008d_walker_s2' in raw and raw['exp_009b_008d_walker_s2']:
        entries = raw['exp_009b_008d_walker_s2']
        actor_loss_data['009b_s2'] = {
            'steps': [e['step'] for e in entries],
            'actor_loss': [e['actor_loss'] for e in entries],
        }
    d008 = raw.get('exp_008d_subsample_on_h8', [])
    d009 = raw.get('exp_009e_008d_walker_s1', [])
    if d008 or d009:
        max_008d_step = max(e['step'] for e in d008) if d008 else 0
        merged = list(d008) + [e for e in d009 if e['step'] > max_008d_step]
        actor_loss_data['008d_009e'] = {
            'steps': [e['step'] for e in merged],
            'actor_loss': [e['actor_loss'] for e in merged],
        }

actor_loss_data['008e_v3_s2'] = {
    'steps': [35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
    'actor_loss': [-0.167, -0.112, -0.092, -0.075, -0.098, -0.098, -0.027, 0.016],
}

has_right = bool(actor_loss_data)

# === FIGURE: vertically stacked subplots ===
fig, (ax_top, ax_bottom) = plt.subplots(2, 1, figsize=(10, 10),
                                         constrained_layout=True)

for ax in (ax_top, ax_bottom):
    for spine in ax.spines.values():
        spine.set_linewidth(1.8)

# =====================================================
# TOP: NVE Trajectories
# =====================================================

# Background zones
ax_top.axhspan(2.0, 5.5, color='#F5E6D3', alpha=0.35, zorder=0)
ax_top.axvspan(25000, 35000, color='#E8E8E8', alpha=0.3, zorder=0)

# Baseline reference: NVE=1.0
ax_top.axhline(y=1.0, color=C_BASELINE, linestyle=':', linewidth=1.5, zorder=1, alpha=0.6)
ax_top.text(21500, 1.05, 'baseline', fontsize=7, color=C_BASELINE,
            va='bottom', ha='left', fontweight='bold', alpha=0.7)

# Threshold line
ax_top.axhline(y=2.0, color=C_THRESH, linestyle='--', linewidth=1.2, zorder=1, alpha=0.7)
ax_top.text(111500, 2.0, r'$\tau{=}2.0\times$', fontsize=7, color=C_THRESH,
             va='center', ha='left', fontweight='bold')

# Diagnostic window onset
ax_top.axvline(x=35000, color='#999999', linestyle='--', linewidth=0.8, zorder=1)
ax_top.text(36500, 4.8, '35K+', fontsize=7, color='#666666', va='top', fontweight='bold')

# Plot NVE trajectories
for name, d in experiments.items():
    ax_top.plot(d['steps'], d['nve'],
                 color=d['color'], linestyle=d['linestyle'], marker=d['marker'],
                 markersize=5, markeredgecolor='white', markeredgewidth=0.5,
                 label=name, zorder=3, linewidth=2.8)

# Key value annotations on panel (a)
# 008d/009e s1 peak: 4.12× at 55K
ax_top.annotate(r'$4.12\times$', xy=(55000, 4.12), xytext=(62000, 4.55),
                fontsize=8, fontweight='bold', color=C_CIVO_1,
                arrowprops=dict(arrowstyle='->', color=C_CIVO_1, lw=1.0),
                zorder=5)

# 008e_v3 s2 late onset: 3.78× at 105K
ax_top.annotate(r'$3.78\times$' + '\n(late onset)', xy=(105000, 3.78),
                xytext=(88000, 4.45),
                fontsize=7.5, fontweight='bold', color=C_DT1_2,
                arrowprops=dict(arrowstyle='->', color=C_DT1_2, lw=0.9),
                zorder=5)

# 009b s2 early transient then self-correction
ax_top.annotate(r'$2.05\times$' + '\n(self-corrects)', xy=(25000, 2.05),
                xytext=(28000, 3.0),
                fontsize=7, fontweight='bold', color=C_CIVO_2,
                arrowprops=dict(arrowstyle='->', color=C_CIVO_2, lw=0.8),
                zorder=5)

ax_top.set_ylabel('Normalized Value Excess (NVE)', fontsize=9)
ax_top.set_xlabel('Training Steps', fontsize=9)
ax_top.set_ylim(0, 5.2)
ax_top.set_xlim(20000, 115000)
ax_top.set_xticks(np.arange(25000, 110001, 20000))
ax_top.set_xticklabels([f'{int(s/1000)}K' for s in np.arange(25000, 110001, 20000)], fontsize=8)
ax_top.tick_params(labelsize=8)
ax_top.legend(loc='upper right', fontsize=9, ncol=3, frameon=True,
               framealpha=0.92, edgecolor='#CCCCCC',
               columnspacing=0.8, handletextpad=0.4, handlelength=1.5)
ax_top.grid(True, alpha=0.12, color='gray')
ax_top.set_title('(a) NVE Trajectories', fontsize=11, fontweight='bold')

# =====================================================
# BOTTOM: Actor Loss
# =====================================================
if has_right:
    actor_colors = {
        'baseline': C_BASELINE, '008d_009e': C_CIVO_1,
        '009b_s2': C_CIVO_2, '008e_v3_s2': C_DT1_2,
    }
    actor_labels = {
        'baseline': 'baseline', '008d_009e': '008d/009e',
        '009b_s2': '009b', '008e_v3_s2': '008e_v3',
    }
    actor_markers = {'baseline': 'o', '008d_009e': 'D', '009b_s2': 's', '008e_v3_s2': 'P'}
    actor_ls = {'baseline': '-', '008d_009e': '-', '009b_s2': '-', '008e_v3_s2': '--'}

    # Zero reference line
    ax_bottom.axhline(y=0, color='#999999', linestyle=':', linewidth=1.2, zorder=1)
    ax_bottom.text(2000, 0.008, 'zero', fontsize=7, color='#888888',
                   va='bottom', fontweight='bold', alpha=0.6)

    for key in ['baseline', '008d_009e', '009b_s2', '008e_v3_s2']:
        if actor_loss_data.get(key) is not None:
            steps = np.array(actor_loss_data[key]['steps'])
            losses = np.array(actor_loss_data[key]['actor_loss'])
            ax_bottom.plot(steps, losses,
                          color=actor_colors[key], linestyle=actor_ls[key],
                          marker=actor_markers[key],
                          markersize=5, markeredgecolor='white', markeredgewidth=0.5,
                          label=actor_labels[key], zorder=3, linewidth=2.8)

            if key == '008d_009e':
                for i in range(1, len(losses)):
                    if losses[i-1] < 0 and losses[i] >= 0:
                        ax_bottom.annotate('sign flip',
                                          xy=(steps[i], losses[i]),
                                          xytext=(steps[i] - 30000, losses[i] + 0.07),
                                          fontsize=8, fontweight='bold', color=C_CIVO_1,
                                          arrowprops=dict(arrowstyle='->', color=C_CIVO_1, lw=1.0),
                                          zorder=5)
                        break

            if key == '008e_v3_s2':
                for i in range(1, len(losses)):
                    if losses[i-1] < 0 and losses[i] >= 0:
                        ax_bottom.annotate('sign flip',
                                          xy=(steps[i], losses[i]),
                                          xytext=(steps[i] - 18000, losses[i] + 0.06),
                                          fontsize=8, fontweight='bold', color=C_DT1_2,
                                          arrowprops=dict(arrowstyle='->', color=C_DT1_2, lw=0.9),
                                          zorder=5)
                        break

    ax_bottom.set_ylabel('Actor Loss', fontsize=9)
    ax_bottom.set_xlabel('Training Steps', fontsize=9)
    ax_bottom.legend(loc='lower right', fontsize=11, ncol=1, frameon=True,
                    framealpha=0.92, edgecolor='#CCCCCC',
                    handletextpad=0.4, handlelength=1.5)
    ax_bottom.grid(True, alpha=0.12, color='gray')
    ax_bottom.set_xlim(0, 112000)
    ax_bottom.set_xticks(np.arange(0, 110001, 20000))
    ax_bottom.set_xticklabels([f'{int(s/1000)}K' for s in np.arange(0, 110001, 20000)], fontsize=8)
    ax_bottom.tick_params(labelsize=8)
    ax_bottom.set_title('(b) Actor Loss', fontsize=11, fontweight='bold')

outdir = os.path.dirname(__file__)
preview_dir = os.path.join(outdir, '..', '..', '..', 'artifacts')
plt.savefig(os.path.join(outdir, 'fig2_nve_trajectory.pdf'), dpi=300)
plt.savefig(os.path.join(outdir, 'fig2_nve_trajectory.png'), dpi=150)
plt.savefig(os.path.join(preview_dir, 'fig3_preview_bold.pdf'), dpi=300)
plt.savefig(os.path.join(preview_dir, 'fig3_preview_bold.png'), dpi=150)
plt.close()
print('Done: muted academic style, vertically stacked.')
