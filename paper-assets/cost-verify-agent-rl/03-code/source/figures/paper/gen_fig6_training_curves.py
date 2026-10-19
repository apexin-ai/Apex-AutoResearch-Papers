import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 11,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

COLORS = {
    'collapse': '#D55E00',
    'oscillation': '#E69F00',
    'stable': '#0072B2',
    'baseline': '#999999',
}

OUT_DIR = '/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/figures/paper'

# ── Cell A (7o9bjszm, hsweep-h2-seed1): step_independent + step-level adv ──
# Monotonic collapse pattern
cellA_steps = np.arange(1, 15)
cellA_train_success = np.array([
    18.75, 14.84, 18.75, 5.47, 1.56,
    3.12, 4.69, 1.56, 0.0, 2.34,
    0.0, 0.0, 0.0, 0.0,
])
cellA_action_effective = np.array([
    97.30, 98.01, 97.20, 73.59, 63.12,
    52.91, 49.81, 45.78, 35.92, 20.61,
    14.69, 2.13, 0.69, 7.88,
])

# ── Cell B (6liw7fm1, factorial-h2-episode-adv): step_independent + episode-level adv ──
# Oscillation, no OOD generalization
cellB_steps = np.arange(1, 15)
cellB_train_success = np.array([
    20.31, 6.25, 5.47, 3.12, 15.62,
    25.78, 17.19, 2.34, 2.34, 3.12,
    7.81, 14.84, 7.03, 20.31,
])
cellB_action_effective = np.array([
    97.04, 97.32, 94.87, 94.29, 91.28,
    91.49, 87.84, 81.65, 90.36, 92.03,
    93.73, 95.02, 98.15, 97.16,
])

# ── Cell C (7a59sudo, exp029 episode-level): full_context + episode-level adv ──
# Real data from wandb_data_7a59sudo.json, 15 training steps
cellC_steps = np.arange(1, 16)
cellC_train_success = np.array([
    17.97, 10.16, 35.16, 32.81, 10.16,
    18.75, 28.91, 18.75, 29.69, 23.44,
    10.16, 23.44, 18.75, 43.75, 43.75,
])
cellC_action_effective = np.array([
    99.47, 97.18, 97.30, 98.21, 98.34,
    99.00, 99.35, 99.44, 97.46, 97.71,
    94.77, 85.44, 78.87, 93.74, 92.89,
])
# Val success (sparse, at eval steps)
cellC_val_steps = np.array([0, 5, 10, 15])
cellC_val_success = np.array([12.5, 25.0, 25.0, 28.125])

# ── Figure ──────────────────────────────────────────────────────────────

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))

# ── Panel (a): Train Success Rate ────────────────────────────────────────

ax1.axhline(y=12.5, color=COLORS['baseline'], linestyle='--',
            linewidth=0.9, alpha=0.6, zorder=1)
ax1.text(0.3, 13.8, 'SFT baseline (12.5%)', fontsize=7,
         color=COLORS['baseline'], va='bottom', ha='left')

ax1.plot(cellA_steps, cellA_train_success, '-o', color=COLORS['collapse'],
         markersize=3, zorder=3,
         label='Cell A: $h$=2, step-level adv')
ax1.plot(cellB_steps, cellB_train_success, '-s', color=COLORS['oscillation'],
         markersize=3, zorder=3,
         label='Cell B: $h$=2, episode-level adv')
ax1.plot(cellC_steps, cellC_train_success, '-^', color=COLORS['stable'],
         markersize=3.5, zorder=3,
         label='Cell C: full context, episode-level adv')
ax1.plot(cellC_val_steps, cellC_val_success, 'D',
         color=COLORS['stable'], markersize=5, zorder=4,
         markeredgecolor='white', markeredgewidth=0.8, alpha=0.7,
         label='Cell C: OOD val checkpoints')

ax1.set_xlabel('Training Step')
ax1.set_ylabel('Success Rate (%)')
ax1.set_title('(a) Train success rate', pad=8)
ax1.set_xlim(-0.5, 15.8)
ax1.set_ylim(-2, 50)
ax1.set_xticks([0, 3, 6, 9, 12, 15])
ax1.legend(loc='upper left', bbox_to_anchor=(0.01, 0.99),
           framealpha=0.92, edgecolor='none',
           handlelength=1.8, borderpad=0.4)

# ── Panel (b): Action Validity Rate ─────────────────────────────────────

ax2.plot(cellA_steps, cellA_action_effective, '-o', color=COLORS['collapse'],
         markersize=3, zorder=3, label='Cell A')
ax2.plot(cellB_steps, cellB_action_effective, '-s', color=COLORS['oscillation'],
         markersize=3, zorder=3, label='Cell B')
ax2.plot(cellC_steps, cellC_action_effective, '-^', color=COLORS['stable'],
         markersize=3.5, zorder=3, label='Cell C')

ax2.set_xlabel('Training Step')
ax2.set_ylabel('Action Validity (%)')
ax2.set_title('(b) Action validity rate', pad=8)
ax2.set_xlim(-0.5, 15.8)
ax2.set_ylim(-5, 108)
ax2.set_xticks([0, 3, 6, 9, 12, 15])
ax2.legend(loc='lower left', framealpha=0.92, edgecolor='none',
           handlelength=1.8, borderpad=0.4)

plt.tight_layout(w_pad=2.5)
plt.savefig(f'{OUT_DIR}/fig6_training_curves.pdf')
plt.savefig(f'{OUT_DIR}/fig6_training_curves.png')
plt.close()
print('Saved fig6_training_curves.pdf and .png')
