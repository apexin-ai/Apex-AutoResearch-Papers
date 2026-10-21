import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import json
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_style import apply_style
apply_style()

# === TOP PANEL DATA: NVE trajectories ===
experiments = {
    '008d/009e (seed 1, extended)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.78, 1.71, 2.09, 4.12, 1.23, 1.48, 1.15, 1.73, 1.57],
        'color': '#D55E00', 'linestyle': '-', 'marker': 'o',
        'group': 'trained',
    },
    '009b s2 (self-correction)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [2.05, 1.24, 1.62, 1.41, 0.94, 0.66, 0.51, 0.43, 0.38],
        'color': '#0072B2', 'linestyle': '-', 'marker': 's',
        'group': 'trained',
    },
    '008f s1 (no dt_emb)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.02, 0.73, 0.83, 0.97, 0.37, 0.42, 0.65, 0.54, 0.30],
        'color': '#009E73', 'linestyle': '--', 'marker': '^',
        'group': 'untrained',
    },
    '009c s2 (no dt_emb)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.26, 0.79, 0.72, 0.66, 0.53, 0.33, 0.60, 0.90, 1.14],
        'color': '#56B4E9', 'linestyle': '--', 'marker': 'v',
        'group': 'untrained',
    },
    '008e_v3 s1 (dt=1, healthy)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.93, 0.94, 0.88, 0.87, 0.72, 0.73, 0.76, 0.75, 0.80],
        'color': '#E69F00', 'linestyle': '-.', 'marker': 'P',
        'group': 'mitigation',
    },
    '008e_v3 s2 (dt=1, late-onset collapse)': {
        'steps': [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
        'nve': [1.64, 1.03, 1.06, 1.02, 0.90, 0.66, 0.68, 1.34, 3.78],
        'color': '#BDA800', 'linestyle': '-.', 'marker': 'X',
        'group': 'mitigation',
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

# [Fix 2] 008e_v3_s2 actor loss (hardcoded from metrics.jsonl)
actor_loss_data['008e_v3_s2'] = {
    'steps': [35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000],
    'actor_loss': [-0.167, -0.112, -0.092, -0.075, -0.098, -0.098, -0.027, 0.016],
}

has_bottom = bool(actor_loss_data)

# === FIGURE LAYOUT ===
if has_bottom:
    fig = plt.figure(figsize=(8, 6))
    gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1], hspace=0.28)
    ax_top = fig.add_subplot(gs[0])
    ax_bot = fig.add_subplot(gs[1])
else:
    fig = plt.figure(figsize=(8, 4))
    ax_top = fig.add_subplot(111)
    ax_bot = None

# === TOP PANEL: NVE trajectories ===
threshold = 1.5

# [Fix 1] 25K-35K pre-classification zone + 35K boundary
ax_top.axvspan(25000, 35000, color='#D0D0D0', alpha=0.22, zorder=0)
ax_top.axvline(x=35000, color='#888888', linestyle='--', linewidth=1.0, zorder=1)
ax_top.text(35800, 4.28, 'Classification\nwindow $\\rightarrow$', fontsize=6.5,
            color='#666666', va='top', ha='left')

ax_top.axhspan(threshold, 5.0, color='#FDECEC', alpha=0.5, zorder=0, label='_nolegend_')
ax_top.axhline(y=threshold, color='#999999', linestyle='--', linewidth=1.0, zorder=1)
ax_top.text(110500, threshold, 'nve = 1.5$\\times$', fontsize=8, color='#777777',
            va='center', ha='left', style='italic')

for name, d in experiments.items():
    steps_k = np.array(d['steps'])
    ax_top.plot(steps_k, d['nve'],
                color=d['color'], linestyle=d['linestyle'], marker=d['marker'],
                markersize=5, markeredgecolor='white', markeredgewidth=0.5,
                label=name, zorder=2)

ax_top.set_ylabel('Normalized V/E Ratio (nve)')
ax_top.set_ylim(0, 4.5)
ax_top.set_xlim(20000, 112000)

step_ticks = np.arange(25000, 110001, 10000)
ax_top.set_xticks(step_ticks)
ax_top.set_xticklabels([f'{int(s/1000)}K' for s in step_ticks], fontsize=9)

if not has_bottom:
    ax_top.set_xlabel('Training Steps')

ax_top.legend(loc='upper right', fontsize=8, ncol=2, framealpha=0.9,
              columnspacing=1.0, handletextpad=0.5)
ax_top.grid(True, alpha=0.2, color='gray')
ax_top.set_title('Normalized Value/Eval Ratio Trajectories -- Diagnostic Marker')

# === BOTTOM PANEL: Actor loss ===
if has_bottom and ax_bot is not None:
    actor_colors = {
        'baseline': '#2C3E50',
        '008d_009e': '#D55E00',
        '009b_s2': '#0072B2',
        '008e_v3_s2': '#9B59B6',
    }
    actor_labels = {
        'baseline': '001 baseline',
        '008d_009e': '008d/009e (seed 1)',
        '009b_s2': '009b s2 (self-correction)',
        '008e_v3_s2': '008e_v3 s2 (IRD)',
    }
    actor_markers = {
        'baseline': 'o',
        '008d_009e': 'D',
        '009b_s2': 's',
        '008e_v3_s2': 'P',
    }
    actor_linestyles = {
        'baseline': '-',
        '008d_009e': '-',
        '009b_s2': '-',
        '008e_v3_s2': '--',
    }

    ax_bot.axhline(y=0, color='gray', linestyle=':', linewidth=1.0, zorder=1)

    for key in ['baseline', '008d_009e', '009b_s2', '008e_v3_s2']:
        if actor_loss_data.get(key) is not None:
            steps = np.array(actor_loss_data[key]['steps'])
            losses = np.array(actor_loss_data[key]['actor_loss'])
            ax_bot.plot(steps, losses,
                        color=actor_colors[key], linestyle=actor_linestyles[key],
                        marker=actor_markers[key],
                        markersize=4, markeredgecolor='white', markeredgewidth=0.3,
                        label=actor_labels[key], zorder=2)

            if key == '008d_009e':
                for i in range(1, len(losses)):
                    if losses[i-1] < 0 and losses[i] >= 0:
                        ax_bot.annotate('sign flip',
                                        xy=(steps[i], losses[i]),
                                        xytext=(steps[i] + 8000, losses[i] + 0.03),
                                        fontsize=8, color='#D55E00',
                                        arrowprops=dict(arrowstyle='->', color='#D55E00',
                                                        lw=1.2),
                                        zorder=3)
                        break

            # [Fix 2] sign flip annotation for 008e_v3_s2
            if key == '008e_v3_s2':
                for i in range(1, len(losses)):
                    if losses[i-1] < 0 and losses[i] >= 0:
                        ax_bot.annotate('sign flip (+0.016)',
                                        xy=(steps[i], losses[i]),
                                        xytext=(steps[i] - 28000, losses[i] + 0.10),
                                        fontsize=7, color='#9B59B6',
                                        arrowprops=dict(arrowstyle='->', color='#9B59B6',
                                                        lw=1.0),
                                        zorder=3)
                        break

    ax_bot.set_ylabel('Actor Loss')
    ax_bot.set_xlabel('Training Steps')
    ax_bot.legend(loc='upper right', fontsize=7, ncol=2, framealpha=0.9,
                  columnspacing=1.0, handletextpad=0.5)
    ax_bot.grid(True, alpha=0.2, color='gray')
    ax_bot.set_xlim(0, 112000)

    step_ticks_bot = np.arange(0, 110001, 10000)
    ax_bot.set_xticks(step_ticks_bot)
    ax_bot.set_xticklabels([f'{int(s/1000)}K' for s in step_ticks_bot], fontsize=7)

# === SAVE ===
outdir = os.path.dirname(__file__)
pdf_path = os.path.join(outdir, 'fig2_nve_trajectory.pdf')
png_path = os.path.join(outdir, 'fig2_nve_trajectory.png')

artifact_dir = '/root/autodl-tmp/event-gated-adaptive-horizon/artifacts'
artifact_pdf = os.path.join(artifact_dir, 'fig2_nve_trajectory_d054.pdf')
artifact_png = os.path.join(artifact_dir, 'fig2_nve_trajectory_d054.png')

plt.savefig(pdf_path)
plt.savefig(png_path)
plt.savefig(artifact_pdf)
plt.savefig(artifact_png)
plt.close()
print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')
print(f'Saved: {artifact_pdf}')
print(f'Saved: {artifact_png}')
if not has_bottom:
    print('NOTE: Bottom panel (actor_loss) skipped -- actor_loss_data.json not found.')
# [Fix 3] exp_006 omitted — y-axis 5.2+ would compress other trajectories
print('\n[Fix 3] exp_006 (NVE=4.84x) omitted to preserve y-axis scale.')
print('Caption: "exp_006 (NVE=4.84x) omitted for clarity; see Appendix Table X."')
