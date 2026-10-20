#!/usr/bin/env python3
"""Cross-environment CIVO trigger comparison: Walker Walk / Cheetah Run / Cartpole Swingup."""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
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

# ── Experiment registry ──────────────────────────────────────────────────────

EXPERIMENTS = {
    'walker_walk': {
        'display_name': 'Walker Walk',
        'trained_dt_emb': {
            'label': 'Trained dt\\_emb',
            'dirs': [
                'exp_008d_subsample_on_h8',
                'exp_009b_008d_walker_s2',
                'exp_008d_civo_trigger_s4',
                'exp_059_walker_trained_s5',
            ],
        },
        'no_dt_emb': {
            'label': 'No dt\\_emb (control)',
            'dirs': [
                'exp_008f_no_dt_embed_subsample_on_h8',
                'exp_008f_no_dt_emb_s2',
                'exp_008f_s3_no_dt_embed_walker',
                'exp_008f_no_dt_emb_s4',
            ],
        },
        'baseline': {
            'label': 'Baseline (dt=1)',
            'dirs': [
                'baseline_s1',
                'exp_001_baseline_s2',
                'exp_001_baseline_s3',
                'exp_001_baseline_s4',
            ],
        },
    },
    'cheetah_run': {
        'display_name': 'Cheetah Run',
        'trained_dt_emb': {
            'label': 'Trained dt\\_emb',
            'dirs': [
                'exp_010b_cheetah_civo_trigger_s0',
                'exp_048_cheetah_civo_extension',
            ],
        },
        'no_dt_emb': {
            'label': 'No dt\\_emb (control)',
            'dirs': [
                'exp_024b_cheetah_no_dt_emb_s0',
                'exp_024b_cheetah_no_dt_emb_s1',
            ],
        },
        'baseline': {
            'label': 'Baseline (dt=1)',
            'dirs': [
                'exp_023a_cheetah_baseline_s0',
                'exp_023b_cheetah_baseline_s1',
                'exp_023_cheetah_baseline_s3',
                'exp_023_cheetah_baseline_s4',
            ],
        },
    },
    'cartpole_swingup': {
        'display_name': 'Cartpole Swingup',
        'trained_dt_emb': {
            'label': 'Trained dt\\_emb',
            'dirs': [
                'exp_061_cartpole_civo_trigger_s0',
                'exp_061_cartpole_civo_trigger_s1',
                'exp_061_cartpole_civo_trigger_s2',
            ],
        },
        'no_dt_emb': {
            'label': 'No dt\\_emb (control)',
            'dirs': [
                # exp_062 not yet available
            ],
        },
        'baseline': {
            'label': 'Baseline (dt=1)',
            'dirs': [
                'exp_060_cartpole_baseline_s0',
                'exp_060_cartpole_baseline_s1',
                'exp_060_cartpole_baseline_s2',
            ],
        },
    },
}

NVE_THRESHOLD = 1.5


# ── Data loading ─────────────────────────────────────────────────────────────

def parse_metrics_jsonl(filepath):
    """Parse metrics.jsonl into {step: {field: value}} dict, merging lines at same step."""
    checkpoints = {}
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            step = d.get('step')
            if step is None:
                continue
            step = int(step)
            if step not in checkpoints:
                checkpoints[step] = {}
            checkpoints[step].update(d)
    return checkpoints


def extract_ve_ratio(data_at_step):
    """Extract ve_ratio from a single step's data, handling field name variants."""
    for key in ('ve_ratio', 'civo/ve_ratio'):
        if key in data_at_step:
            return data_at_step[key]
    if 'value_mean' in data_at_step and 'eval_return' in data_at_step:
        er = data_at_step['eval_return']
        if er > 0:
            return data_at_step['value_mean'] / er
    return None


def extract_eval_return(data_at_step):
    for key in ('eval_return', 'train_return'):
        if key in data_at_step:
            return data_at_step[key]
    return None


def load_experiment(logdir, exp_dir):
    """Load a single experiment run. Returns dict with trajectory data."""
    metrics_path = os.path.join(logdir, exp_dir, 'metrics.jsonl')
    if not os.path.exists(metrics_path):
        return None

    checkpoints = parse_metrics_jsonl(metrics_path)
    if not checkpoints:
        return None

    trajectory = []
    for step in sorted(checkpoints.keys()):
        d = checkpoints[step]
        ve = extract_ve_ratio(d)
        er = extract_eval_return(d)
        vm = d.get('value_mean')
        if ve is not None or er is not None:
            trajectory.append({
                'step': step,
                've_ratio': ve,
                'eval_return': er,
                'value_mean': vm,
            })

    if not trajectory:
        return None

    ve_values = [t['ve_ratio'] for t in trajectory if t['ve_ratio'] is not None]
    er_values = [t['eval_return'] for t in trajectory if t['eval_return'] is not None]

    return {
        'dir': exp_dir,
        'trajectory': trajectory,
        'max_ve_ratio': max(ve_values) if ve_values else None,
        'mean_ve_ratio': float(np.mean(ve_values)) if ve_values else None,
        'peak_return': max(er_values) if er_values else None,
        'final_return': er_values[-1] if er_values else None,
        'max_step': trajectory[-1]['step'],
    }


def load_config_group(logdir, config):
    """Load all seeds for a config group."""
    runs = []
    for d in config['dirs']:
        run = load_experiment(logdir, d)
        if run is not None:
            runs.append(run)
    return runs


def compute_nve_timeseries(treatment_runs, baseline_runs):
    """Compute NVE timeseries: ve_ratio(treatment) / mean(ve_ratio(baselines)) at each step."""
    bl_by_step = defaultdict(list)
    for run in baseline_runs:
        for t in run['trajectory']:
            if t['ve_ratio'] is not None:
                bl_by_step[t['step']].append(t['ve_ratio'])
    bl_mean = {s: np.mean(v) for s, v in bl_by_step.items()}

    all_nve = []
    for run in treatment_runs:
        nve_series = []
        for t in run['trajectory']:
            step = t['step']
            ve = t['ve_ratio']
            if ve is not None and step in bl_mean and bl_mean[step] > 1e-6:
                nve_series.append({'step': step, 'nve': ve / bl_mean[step]})
        all_nve.append(nve_series)
    return all_nve, bl_mean


def compute_summary(runs, baseline_runs=None):
    """Compute summary statistics for a config group."""
    if not runs:
        return {
            'n_seeds': 0,
            've_ratio_mean': None, 've_ratio_std': None,
            'peak_nve': None, 'peak_nve_std': None,
            'civo_triggered': None,
            'return_mean': None, 'return_std': None,
        }

    max_ves = [r['max_ve_ratio'] for r in runs if r['max_ve_ratio'] is not None]
    final_returns = [r['final_return'] for r in runs if r['final_return'] is not None]

    summary = {
        'n_seeds': len(runs),
        've_ratio_mean': float(np.mean(max_ves)) if max_ves else None,
        've_ratio_std': float(np.std(max_ves)) if len(max_ves) > 1 else 0.0,
        'return_mean': float(np.mean(final_returns)) if final_returns else None,
        'return_std': float(np.std(final_returns)) if len(final_returns) > 1 else 0.0,
    }

    if baseline_runs and max_ves:
        bl_max_ves = [r['max_ve_ratio'] for r in baseline_runs if r['max_ve_ratio'] is not None]
        if bl_max_ves:
            bl_mean_ve = np.mean(bl_max_ves)
            if bl_mean_ve > 1e-6:
                nves = [v / bl_mean_ve for v in max_ves]
                summary['peak_nve'] = float(np.mean(nves))
                summary['peak_nve_std'] = float(np.std(nves)) if len(nves) > 1 else 0.0
                summary['civo_triggered'] = summary['peak_nve'] > NVE_THRESHOLD
            else:
                summary['peak_nve'] = None
                summary['peak_nve_std'] = None
                summary['civo_triggered'] = None
        else:
            summary['peak_nve'] = None
            summary['peak_nve_std'] = None
            summary['civo_triggered'] = None
    else:
        summary['peak_nve'] = 1.0 if not baseline_runs else None
        summary['peak_nve_std'] = 0.0
        summary['civo_triggered'] = False

    return summary


# ── Output: Tables ───────────────────────────────────────────────────────────

def fmt_val(val, fmt_str='.3f', none_str='--'):
    if val is None:
        return none_str
    return f'{val:{fmt_str}}'


def fmt_pm(mean, std, fmt_str='.3f', none_str='--'):
    if mean is None:
        return none_str
    if std is None or std == 0:
        return f'{mean:{fmt_str}}'
    return f'{mean:{fmt_str}}±{std:{fmt_str}}'


def print_terminal_table(results):
    """Pretty-print comparison table to terminal."""
    header = f"{'Environment':<20} {'Config':<22} {'Seeds':>5} {'ve_ratio (max)':>18} {'NVE (peak)':>16} {'CIVO?':>6} {'Return':>16}"
    sep = '-' * len(header)
    print('\n' + sep)
    print(header)
    print(sep)

    for env_key, env_data in results.items():
        env_name = EXPERIMENTS[env_key]['display_name']
        for i, (config_key, summary) in enumerate(env_data.items()):
            name = env_name if i == 0 else ''
            config_label = config_key.replace('_', ' ').replace('dt emb', 'dt_emb')
            triggered = ''
            if summary['civo_triggered'] is True:
                triggered = 'YES'
            elif summary['civo_triggered'] is False:
                triggered = 'No'

            print(f"{name:<20} {config_label:<22} {summary['n_seeds']:>5} "
                  f"{fmt_pm(summary['ve_ratio_mean'], summary['ve_ratio_std']):>18} "
                  f"{fmt_pm(summary['peak_nve'], summary['peak_nve_std']):>16} "
                  f"{triggered:>6} "
                  f"{fmt_pm(summary['return_mean'], summary['return_std'], '.1f'):>16}")
        print(sep)
    print()


def generate_latex_table(results):
    """Generate LaTeX table string."""
    lines = [
        r'\begin{table}[t]',
        r'\centering',
        r'\caption{Cross-environment CIVO trigger comparison. NVE = peak ve\_ratio(treatment) / mean ve\_ratio(baseline). CIVO triggered if NVE $> 1.5\times$.}',
        r'\label{tab:cross-env-civo}',
        r'\small',
        r'\begin{tabular}{llccccr}',
        r'\toprule',
        r'Environment & Config & Seeds & ve\_ratio (max) & NVE (peak) & CIVO? & Return \\',
        r'\midrule',
    ]

    env_keys = list(results.keys())
    for ei, env_key in enumerate(env_keys):
        env_name = EXPERIMENTS[env_key]['display_name']
        env_data = results[env_key]
        configs = list(env_data.items())
        for i, (config_key, summary) in enumerate(configs):
            name = env_name if i == 0 else ''
            label = config_key.replace('_', r'\_').replace('dt emb', r'dt\_emb')

            triggered = ''
            if summary['civo_triggered'] is True:
                triggered = r'\textbf{Yes}'
            elif summary['civo_triggered'] is False:
                triggered = 'No'

            nve_str = fmt_pm(summary['peak_nve'], summary['peak_nve_std'])
            if summary['civo_triggered']:
                nve_str = r'\textbf{' + nve_str + '}'

            line = (f'  {name} & {label} & {summary["n_seeds"]} & '
                    f'{fmt_pm(summary["ve_ratio_mean"], summary["ve_ratio_std"])} & '
                    f'{nve_str} & {triggered} & '
                    f'{fmt_pm(summary["return_mean"], summary["return_std"], ".1f")} \\\\')
            lines.append(line)

        if ei < len(env_keys) - 1:
            lines.append(r'\midrule')

    lines.extend([
        r'\bottomrule',
        r'\end{tabular}',
        r'\end{table}',
    ])
    return '\n'.join(lines)


# ── Output: Figures ──────────────────────────────────────────────────────────

COLORS = {
    'trained_dt_emb': '#d62728',
    'no_dt_emb': '#2ca02c',
    'baseline': '#1f77b4',
}

HATCHES = {
    'trained_dt_emb': '///',
    'no_dt_emb': '...',
    'baseline': '',
}


def plot_nve_bar_chart(results, output_dir):
    """Figure 1: Grouped bar chart of peak NVE per environment."""
    envs = [k for k in results.keys()]
    env_names = [EXPERIMENTS[k]['display_name'] for k in envs]
    configs = ['trained_dt_emb', 'no_dt_emb', 'baseline']
    config_labels = ['Trained dt_emb', 'No dt_emb (ctrl)', 'Baseline (dt=1)']

    n_envs = len(envs)
    n_configs = len(configs)
    bar_width = 0.22
    x = np.arange(n_envs)

    fig, ax = plt.subplots(figsize=(7, 4))

    for j, (cfg, label) in enumerate(zip(configs, config_labels)):
        vals = []
        errs = []
        for env in envs:
            s = results[env].get(cfg)
            if s and s['peak_nve'] is not None:
                vals.append(s['peak_nve'])
                errs.append(s.get('peak_nve_std', 0) or 0)
            else:
                vals.append(0)
                errs.append(0)

        offset = (j - (n_configs - 1) / 2) * bar_width
        bars = ax.bar(x + offset, vals, bar_width * 0.9,
                      yerr=errs, capsize=3,
                      color=COLORS[cfg], alpha=0.85,
                      hatch=HATCHES[cfg], edgecolor='white',
                      label=label, zorder=3)

    ax.axhline(y=NVE_THRESHOLD, color='#555555', linestyle='--', linewidth=1.2,
               label=f'CIVO threshold ({NVE_THRESHOLD}×)', zorder=2)

    ax.set_xticks(x)
    ax.set_xticklabels(env_names)
    ax.set_ylabel('Peak NVE')
    ax.set_title('Cross-Environment CIVO Trigger Comparison')
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(bottom=0)
    ax.grid(axis='y', alpha=0.3, zorder=0)

    for fmt in ('png', 'pdf'):
        fig.savefig(os.path.join(output_dir, f'cross_env_nve_bars.{fmt}'))
    plt.close(fig)
    print(f'  Saved cross_env_nve_bars.png/pdf')


def plot_ve_ratio_timelines(all_env_data, output_dir):
    """Figure 2: ve_ratio timelines per environment (subplots)."""
    envs_with_data = [(k, v) for k, v in all_env_data.items() if v]
    n = len(envs_with_data)
    if n == 0:
        print('  No timeline data to plot.')
        return

    fig, axes = plt.subplots(1, n, figsize=(5 * n, 4), squeeze=False)

    for idx, (env_key, env_runs) in enumerate(envs_with_data):
        ax = axes[0, idx]
        env_name = EXPERIMENTS[env_key]['display_name']

        for cfg_key in ('baseline', 'no_dt_emb', 'trained_dt_emb'):
            runs = env_runs.get(cfg_key, [])
            if not runs:
                continue

            all_steps = set()
            for run in runs:
                for t in run['trajectory']:
                    if t['ve_ratio'] is not None:
                        all_steps.add(t['step'])

            steps = sorted(all_steps)
            if not steps:
                continue

            step_vals = defaultdict(list)
            for run in runs:
                run_dict = {t['step']: t['ve_ratio'] for t in run['trajectory'] if t['ve_ratio'] is not None}
                for s in steps:
                    if s in run_dict:
                        step_vals[s].append(run_dict[s])

            mean_curve = []
            std_curve = []
            valid_steps = []
            for s in steps:
                if step_vals[s]:
                    valid_steps.append(s / 1000)
                    mean_curve.append(np.mean(step_vals[s]))
                    std_curve.append(np.std(step_vals[s]) if len(step_vals[s]) > 1 else 0)

            mean_curve = np.array(mean_curve)
            std_curve = np.array(std_curve)

            label_map = {
                'trained_dt_emb': 'Trained dt_emb',
                'no_dt_emb': 'No dt_emb (ctrl)',
                'baseline': 'Baseline',
            }

            ax.plot(valid_steps, mean_curve, color=COLORS[cfg_key], label=label_map[cfg_key])
            if np.any(std_curve > 0):
                ax.fill_between(valid_steps, mean_curve - std_curve, mean_curve + std_curve,
                                color=COLORS[cfg_key], alpha=0.15)

        ax.set_xlabel('Step (×1000)')
        ax.set_ylabel('ve_ratio')
        ax.set_title(env_name)
        ax.legend(loc='upper left', framealpha=0.9, fontsize=8)
        ax.grid(alpha=0.3)

    fig.suptitle('Value Estimation Ratio Trajectories', y=1.02, fontsize=14)
    fig.tight_layout()

    for fmt in ('png', 'pdf'):
        fig.savefig(os.path.join(output_dir, f'cross_env_ve_ratio_timelines.{fmt}'))
    plt.close(fig)
    print(f'  Saved cross_env_ve_ratio_timelines.png/pdf')


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Cross-environment CIVO comparison')
    parser.add_argument('--data-dir', type=str,
                        default='/root/autodl-tmp/event-gated-adaptive-horizon/logdir',
                        help='Path to logdir containing experiment subdirectories')
    parser.add_argument('--output-dir', type=str, default=None,
                        help='Output directory for figures and tables (default: data-dir)')
    parser.add_argument('--no-figures', action='store_true',
                        help='Skip figure generation')
    args = parser.parse_args()

    logdir = args.data_dir
    output_dir = args.output_dir or logdir

    if not os.path.isdir(logdir):
        print(f'Error: data directory not found: {logdir}', file=sys.stderr)
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    # Load all data
    print('Loading experiment data...')
    all_runs = {}        # env -> config -> [runs]
    all_summaries = {}   # env -> config -> summary

    for env_key, env_config in EXPERIMENTS.items():
        env_name = env_config['display_name']
        all_runs[env_key] = {}

        for cfg_key in ('trained_dt_emb', 'no_dt_emb', 'baseline'):
            cfg = env_config[cfg_key]
            runs = load_config_group(logdir, cfg)
            all_runs[env_key][cfg_key] = runs
            n_found = len(runs)
            n_expected = len(cfg['dirs'])
            status = '✓' if n_found == n_expected else f'({n_found}/{n_expected})'
            if n_found > 0:
                print(f'  {env_name} / {cfg_key}: {n_found} seeds loaded {status}')
            else:
                print(f'  {env_name} / {cfg_key}: no data found')

    # Compute summaries
    print('\nComputing summaries...')
    for env_key in EXPERIMENTS:
        all_summaries[env_key] = {}
        baseline_runs = all_runs[env_key]['baseline']

        for cfg_key in ('trained_dt_emb', 'no_dt_emb', 'baseline'):
            runs = all_runs[env_key][cfg_key]
            bl = baseline_runs if cfg_key != 'baseline' else None
            all_summaries[env_key][cfg_key] = compute_summary(runs, bl)

    # Terminal table
    print_terminal_table(all_summaries)

    # LaTeX table
    latex = generate_latex_table(all_summaries)
    latex_path = os.path.join(output_dir, 'cross_env_civo_table.tex')
    with open(latex_path, 'w') as f:
        f.write(latex)
    print(f'LaTeX table saved to {latex_path}')
    print('\n--- LaTeX ---')
    print(latex)
    print('--- End LaTeX ---\n')

    # JSON dump for downstream use
    json_path = os.path.join(output_dir, 'cross_env_civo_summary.json')
    with open(json_path, 'w') as f:
        json.dump(all_summaries, f, indent=2, default=str)
    print(f'JSON summary saved to {json_path}')

    # Figures
    if not args.no_figures:
        print('\nGenerating figures...')
        plot_nve_bar_chart(all_summaries, output_dir)
        plot_ve_ratio_timelines(all_runs, output_dir)

    print('\nDone.')


if __name__ == '__main__':
    main()
