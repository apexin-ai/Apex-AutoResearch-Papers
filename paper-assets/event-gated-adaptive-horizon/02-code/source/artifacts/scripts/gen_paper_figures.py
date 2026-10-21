"""Generate paper figures for event-gated-adaptive-horizon project."""

import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 9,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

BASE = Path('/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts')
ANALYSIS = BASE / 'analysis'
FIGURES = BASE / 'figures'
FIGURES.mkdir(exist_ok=True)


def load_json(name):
    with open(ANALYSIS / name) as f:
        return json.load(f)


def save_fig(fig, name):
    fig.savefig(FIGURES / f'{name}.pdf', format='pdf')
    fig.savefig(FIGURES / f'{name}.png', format='png')
    plt.close(fig)


# =============================================================================
# Figure 1: NVE Trajectory Multi-Seed (Fan Chart)
# =============================================================================
def fig1_nve_trajectory():
    data = load_json('nve_trajectories_for_figure.json')

    trained_exps = [e for e in data['experiments'] if e['condition'] == 'trained_dt_emb' and e['env'] == 'walker_walk']
    no_dt_exps = [e for e in data['experiments'] if e['condition'] == 'no_dt_emb' and e['env'] == 'walker_walk']

    steps = np.array([5000, 15000, 25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000])

    def get_nve_array(exps):
        arrays = []
        for exp in exps:
            nve = np.array([v if v is not None else np.nan for v in exp['nve']], dtype=float)
            arrays.append(nve)
        return np.array(arrays)

    trained_nve = get_nve_array(trained_exps)
    no_dt_nve = get_nve_array(no_dt_exps)

    trained_mean = np.nanmean(trained_nve, axis=0)
    trained_min = np.nanmin(trained_nve, axis=0)
    trained_max = np.nanmax(trained_nve, axis=0)

    no_dt_mean = np.nanmean(no_dt_nve, axis=0)
    no_dt_min = np.nanmin(no_dt_nve, axis=0)
    no_dt_max = np.nanmax(no_dt_nve, axis=0)

    mask = ~np.isnan(trained_mean)
    steps_valid = steps[mask]

    fig, ax = plt.subplots(figsize=(3.5, 2.5))

    ax.fill_between(steps_valid / 1000, trained_min[mask], trained_max[mask],
                    alpha=0.2, color='#d62728')
    ax.plot(steps_valid / 1000, trained_mean[mask], color='#d62728', linewidth=1.5,
            label='Trained dt-emb (CIVO)', marker='o', markersize=3)

    ax.fill_between(steps_valid / 1000, no_dt_min[mask], no_dt_max[mask],
                    alpha=0.2, color='#1f77b4')
    ax.plot(steps_valid / 1000, no_dt_mean[mask], color='#1f77b4', linewidth=1.5,
            label='No dt-emb (control)', marker='s', markersize=3)

    ax.axhline(y=1.5, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax.text(100, 1.6, 'NVE = 1.5', fontsize=7, color='gray', ha='right')

    ax.axvline(x=35, color='gray', linestyle=':', linewidth=0.8, alpha=0.7)
    ax.text(36, ax.get_ylim()[1] * 0.9 if ax.get_ylim()[1] > 3 else 3.5,
            '35K', fontsize=7, color='gray')

    ax.axhline(y=1.0, color='black', linestyle='-', linewidth=0.5, alpha=0.3)

    ax.set_xlabel('Training Step (K)')
    ax.set_ylabel('NVE (Normalized Value Excess)')
    ax.set_xlim(5, 105)
    ax.legend(loc='upper right', framealpha=0.9)
    fig.tight_layout()
    save_fig(fig, 'fig1_nve_trajectory')


# =============================================================================
# Figure 2: CIVO Decomposition (Grouped Bar)
# =============================================================================
def fig2_civo_decomposition():
    civo_data = load_json('018v2_civo_analysis.json')
    decomp = civo_data['decomposition']

    conditions = ['Baseline\n(001)', 'Trained dt-emb\n(008d/009b)', 'Full-SGS\n(s1)', 'Full-SGS\n(s2)']

    nve_data = load_json('nve_trajectories_for_figure.json')
    baseline_exp = next(e for e in nve_data['experiments'] if e['exp_id'] == 'exp_009d_baseline_walker_s1')
    trained_exp = next(e for e in nve_data['experiments'] if e['exp_id'] == 'exp_008d_subsample_on_h8')
    sgs_exp = next(e for e in nve_data['experiments'] if e['exp_id'] == 'exp_018v2_full_sgs_walker_s1')

    baseline_peak = max(baseline_exp['eval_return'])
    trained_peak = max(trained_exp['eval_return'])
    sgs_s1_peak = max(sgs_exp['eval_return'])
    sgs_s2_peak = 488.0  # 018_s2 peak@75K

    baseline_final = decomp['baseline_eval_105K']
    trained_final = decomp['008d_eval_105K']
    sgs_s1_final = decomp['018v2_eval_105K']
    sgs_s2_final = 40.8  # 018_s2 collapsed@105K

    peaks = [baseline_peak, trained_peak, sgs_s1_peak, sgs_s2_peak]
    finals = [baseline_final, trained_final, sgs_s1_final, sgs_s2_final]

    fig, ax = plt.subplots(figsize=(4.0, 2.5))

    x = np.arange(len(conditions))
    width = 0.35

    bars1 = ax.bar(x - width/2, peaks, width,
                   label='Peak Eval Return', color='#2ca02c', alpha=0.8)
    bars2 = ax.bar(x + width/2, finals, width,
                   label='Final Eval Return (105K)', color='#ff7f0e', alpha=0.8)

    for i, (bp, bf) in enumerate(zip(peaks, finals)):
        if i > 0:
            deg_peak = (bp / baseline_peak - 1) * 100
            deg_final = (bf / baseline_final - 1) * 100
            ax.text(x[i] - width/2, bp + 15, f'{deg_peak:.0f}%', ha='center', fontsize=6.5, color='#2ca02c')
            ax.text(x[i] + width/2, max(bf, 0) + 15, f'{deg_final:.0f}%', ha='center', fontsize=6.5, color='#ff7f0e')

    # Annotate s2 collapse
    ax.annotate('collapsed', xy=(x[3] + width/2, sgs_s2_final + 5),
                fontsize=6, color='red', ha='center', style='italic')

    ax.set_xticks(x)
    ax.set_xticklabels(conditions)
    ax.set_ylabel('Eval Return')
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, max(baseline_peak, baseline_final) * 1.15)
    fig.tight_layout()
    save_fig(fig, 'fig2_civo_decomposition')


# =============================================================================
# Figure 3: Gradient Decomposition (Stacked Bar)
# =============================================================================
def fig3_gradient_decomposition():
    data = load_json('gradient_decomposition_008d_corrected.json')

    steps_data = data['steps']
    labels = [f"008d @ 55K", f"009e @ 112K"]

    obs_pcts = [s['correct_config']['obs_pct'] for s in steps_data]
    reward_pcts = [s['correct_config']['reward_pct'] for s in steps_data]
    kl_pcts = [s['correct_config']['kl_pct'] for s in steps_data]

    fig, ax = plt.subplots(figsize=(3.5, 2.5))

    x = np.arange(len(labels))
    width = 0.5

    bars_obs = ax.bar(x, obs_pcts, width, label='Obs', color='#1f77b4')
    bars_reward = ax.bar(x, reward_pcts, width, bottom=obs_pcts, label='Reward', color='#d62728')
    bottoms_kl = [o + r for o, r in zip(obs_pcts, reward_pcts)]
    bars_kl = ax.bar(x, kl_pcts, width, bottom=bottoms_kl, label='KL', color='#2ca02c')

    for i in range(len(labels)):
        ax.text(x[i], obs_pcts[i] / 2, f'{obs_pcts[i]:.1f}%',
                ha='center', va='center', fontsize=7.5, color='white', fontweight='bold')
        ax.text(x[i], obs_pcts[i] + reward_pcts[i] / 2, f'{reward_pcts[i]:.1f}%',
                ha='center', va='center', fontsize=7.5, color='white', fontweight='bold')
        ax.text(x[i], bottoms_kl[i] + kl_pcts[i] / 2, f'{kl_pcts[i]:.1f}%',
                ha='center', va='center', fontsize=7.5, color='white', fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel('Gradient Contribution (%)')
    ax.set_ylim(0, 112)
    ax.legend(loc='upper center', ncol=3, framealpha=0.9, bbox_to_anchor=(0.5, 1.12))
    fig.tight_layout()
    save_fig(fig, 'fig3_gradient_decomposition')


# =============================================================================
# Figure 4: Entropy Dynamics
# =============================================================================
def fig4_entropy_dynamics():
    data = load_json('entropy_dynamics_data.json')

    fig, ax = plt.subplots(figsize=(3.5, 2.5))

    colors = {
        '008d (CIVO trigger)': '#D55E00',
        '008f (no dt_emb)': '#0072B2',
        '018v2 (Full-SGS)': '#E69F00',
    }
    markers = {
        '008d (CIVO trigger)': 'o',
        '008f (no dt_emb)': 's',
        '018v2 (Full-SGS)': '^',
    }

    for key in ['008d (CIVO trigger)', '008f (no dt_emb)', '018v2 (Full-SGS)']:
        entries = data[key]
        steps = [e['step'] / 1000 for e in entries]
        entropy = [e['actor_entropy'] for e in entries]
        ax.plot(steps, entropy, color=colors[key], linewidth=1.5,
                label=key, marker=markers[key], markersize=3)

    ax.axvline(x=55, color='#D55E00', linestyle=':', linewidth=0.8, alpha=0.6)
    ax.text(56, -2, 'CIVO\nonset', fontsize=6.5, color='#D55E00', va='center')

    ax.set_xlabel('Training Step (K)')
    ax.set_ylabel('Actor Entropy')
    ax.legend(loc='upper right', framealpha=0.9)
    fig.tight_layout()
    save_fig(fig, 'fig4_entropy_dynamics')


if __name__ == '__main__':
    fig1_nve_trajectory()
    print('Figure 1: NVE Trajectory done')
    fig2_civo_decomposition()
    print('Figure 2: CIVO Decomposition done')
    fig3_gradient_decomposition()
    print('Figure 3: Gradient Decomposition done')
    fig4_entropy_dynamics()
    print('Figure 4: Entropy Dynamics done')
    print(f'\nAll figures saved to: {FIGURES}')
