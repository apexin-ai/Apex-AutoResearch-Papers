#!/usr/bin/env python3
"""Parse registry JSON and generate 3 CSV files for ML experiment visualization."""

import json
import csv
import re
import math
import os

INPUT_FILE = "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/4e5e232f-6ca3-49ff-a24b-ef8d2e905fee/tool-results/mcp-agent-ml-research-read_registry-1778818810532.txt"
OUTPUT_DIR = "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures_data/"

# Experiment labels
LABELS = {
    "exp_001_baseline": "baseline (seed 0)",
    "exp_009a_baseline_walker_s2": "baseline (seed 2)",
    "exp_006_fixed_dt2": "dt=2 fixed (006)",
    "exp_007_fixed_dt4": "dt=4 fixed (007)",
    "exp_005_event_gated_v4": "learned gate (005)",
    "exp_008d_subsample_on_h8": "trained dt_emb H=8 (008d) seed 0/1",
    "exp_009b_008d_walker_s2": "trained dt_emb H=8 (008d) seed 2",
    "exp_008f_no_dt_embed_subsample_on_h8": "no dt_emb (008f) seed 0/1",
    "exp_009c_008f_walker_s2": "no dt_emb (008f) seed 2",
    "exp_008c_no_subsample_dt2_h8": "untrained dt_emb dt=2 H=8 (008c)",
    "exp_008a_no_subsample_dt2": "untrained dt_emb dt=2 H=15 (008a)",
    "exp_008e_v3_subsample_on_dt1_h15": "dt=1 imag (008e_v3) seed 0/1 (same seed=1)",
    "exp_008e_v3_walker_s1": "dt=1 imag (008e_v3) seed 1 (same seed=1)",
    "exp_008e_v3_walker_s2": "dt=1 imag (008e_v3) seed 2",
}

# Baseline v/e trajectory
BASELINE_VE = {
    25000: 0.087,
    35000: 0.241,
    45000: 0.331,
    55000: 0.404,
    65000: 0.563,
    75000: 0.719,
    85000: 0.701,
    95000: 0.632,
    105000: 0.656,
}


def parse_step_key(key):
    """Parse step from key like 'eval_return_35K' or '35K' or '35k' -> 35000."""
    m = re.search(r'(\d+)[Kk]', key)
    if m:
        return int(m.group(1)) * 1000
    m = re.search(r'(\d+)', key)
    if m:
        return int(m.group(1))
    return None


def load_data():
    with open(INPUT_FILE) as f:
        raw = json.load(f)
    inner = json.loads(raw['result'])
    return inner['data']['experiments']


def extract_eval_returns(metrics):
    """Extract {step: eval_return} from various metric formats."""
    results = {}

    # Format 1: eval_return_XXK keys in metrics dict
    for key, val in metrics.items():
        if key.startswith('eval_return_') and not key.endswith('_mean'):
            step = parse_step_key(key)
            if step is not None and isinstance(val, (int, float)):
                results[step] = val

    # Format 2: eval_return as dict {step_key: value}
    if 'eval_return' in metrics and isinstance(metrics['eval_return'], dict):
        for key, val in metrics['eval_return'].items():
            step = parse_step_key(key)
            if step is not None and isinstance(val, (int, float)):
                results[step] = val

    # Format 3: eval_checkpoints as list of dicts
    if 'eval_checkpoints' in metrics and isinstance(metrics['eval_checkpoints'], list):
        for cp in metrics['eval_checkpoints']:
            if isinstance(cp, dict) and 'step' in cp and 'eval_return' in cp:
                step = cp['step']
                val = cp['eval_return']
                if isinstance(val, (int, float)):
                    results[step] = val

    # Format 4: eval_checkpoints as dict of dicts
    if 'eval_checkpoints' in metrics and isinstance(metrics['eval_checkpoints'], dict):
        for key, cp in metrics['eval_checkpoints'].items():
            step = parse_step_key(key)
            if step is not None and isinstance(cp, dict) and 'eval_return' in cp:
                val = cp['eval_return']
                if isinstance(val, (int, float)):
                    results[step] = val

    # Format 5: eval_trajectory as list of dicts
    if 'eval_trajectory' in metrics and isinstance(metrics['eval_trajectory'], list):
        for cp in metrics['eval_trajectory']:
            if isinstance(cp, dict) and 'step' in cp and 'eval_return' in cp:
                step = cp['step']
                val = cp['eval_return']
                if isinstance(val, (int, float)):
                    results[step] = val

    return results


def extract_ve_ratios(metrics):
    """Extract {step: ve_ratio} from various metric formats."""
    results = {}

    # Format 1: value_eval_ratio_XXK keys
    for key, val in metrics.items():
        if key.startswith('value_eval_ratio_') and not key.endswith('_stable'):
            step = parse_step_key(key)
            if step is not None and isinstance(val, (int, float)):
                results[step] = val

    # Format 1b: ve_ratio_XXk standalone keys (e.g. ve_ratio_105k)
    for key, val in metrics.items():
        if key.startswith('ve_ratio_') and isinstance(val, (int, float)):
            step = parse_step_key(key)
            if step is not None and step not in results:
                results[step] = val

    # Format 2: value_eval_ratio as dict
    if 'value_eval_ratio' in metrics and isinstance(metrics['value_eval_ratio'], dict):
        for key, val in metrics['value_eval_ratio'].items():
            step = parse_step_key(key)
            if step is not None and isinstance(val, (int, float)):
                results[step] = val

    # Format 3: eval_checkpoints as list with ve_ratio
    if 'eval_checkpoints' in metrics and isinstance(metrics['eval_checkpoints'], list):
        for cp in metrics['eval_checkpoints']:
            if isinstance(cp, dict) and 'step' in cp and 've_ratio' in cp:
                step = cp['step']
                val = cp['ve_ratio']
                if isinstance(val, (int, float)) and val is not None:
                    results[step] = val

    # Format 4: eval_checkpoints as dict with ve_ratio
    if 'eval_checkpoints' in metrics and isinstance(metrics['eval_checkpoints'], dict):
        for key, cp in metrics['eval_checkpoints'].items():
            step = parse_step_key(key)
            if step is not None and isinstance(cp, dict) and 've_ratio' in cp:
                val = cp['ve_ratio']
                if isinstance(val, (int, float)):
                    results[step] = val

    # Format 5: Back-compute from eval_checkpoints that have value_mean + eval_return but no ve_ratio
    eval_returns = extract_eval_returns(metrics)
    if 'eval_checkpoints' in metrics and isinstance(metrics['eval_checkpoints'], dict):
        for key, cp in metrics['eval_checkpoints'].items():
            step = parse_step_key(key)
            if step is not None and step not in results and isinstance(cp, dict):
                if 'value_mean' in cp and 'eval_return' in cp:
                    vm = cp['value_mean']
                    er = cp['eval_return']
                    if isinstance(vm, (int, float)) and isinstance(er, (int, float)) and er > 0:
                        results[step] = round(vm / er, 4)

    return results


def extract_nve(metrics):
    """Extract {step: normalized_ve} from various metric formats."""
    results = {}

    # Format 1: normalized_ve_XXK keys
    for key, val in metrics.items():
        if key.startswith('normalized_ve_') and isinstance(val, (int, float)):
            step = parse_step_key(key)
            if step is not None:
                results[step] = val

    # Format 2: normalized_ve as dict
    if 'normalized_ve' in metrics and isinstance(metrics['normalized_ve'], dict):
        for key, val in metrics['normalized_ve'].items():
            step = parse_step_key(key)
            if step is not None and isinstance(val, (int, float)):
                results[step] = val

    # Format 3: eval_checkpoints as list with normalized_ve
    if 'eval_checkpoints' in metrics and isinstance(metrics['eval_checkpoints'], list):
        for cp in metrics['eval_checkpoints']:
            if isinstance(cp, dict) and 'step' in cp and 'normalized_ve' in cp:
                step = cp['step']
                val = cp['normalized_ve']
                if isinstance(val, (int, float)) and val is not None:
                    results[step] = val

    # Format 4: eval_checkpoints as dict with normalized_ve
    if 'eval_checkpoints' in metrics and isinstance(metrics['eval_checkpoints'], dict):
        for key, cp in metrics['eval_checkpoints'].items():
            step = parse_step_key(key)
            if step is not None and isinstance(cp, dict) and 'normalized_ve' in cp:
                val = cp['normalized_ve']
                if isinstance(val, (int, float)):
                    results[step] = val

    return results


def get_seed(exp_id, exp_data):
    """Extract seed from spec or label."""
    spec = exp_data.get('spec', {})
    if isinstance(spec, dict) and 'seed' in spec:
        return spec['seed']
    # Infer from exp_id
    if '_s2' in exp_id or 'seed_2' in exp_id or 'walker_s2' in exp_id:
        return 2
    if '_s1' in exp_id or 'seed_1' in exp_id or 'walker_s1' in exp_id:
        return 1
    return 1  # default seed


def main():
    exps = load_data()

    # Filter to target experiments
    target_exps = {}
    for eid in LABELS:
        if eid in exps:
            status = exps[eid].get('status', '')
            if status in ('DONE', 'RUNNING'):
                target_exps[eid] = exps[eid]
            else:
                print(f"SKIP {eid}: status={status}")
        else:
            print(f"NOT FOUND: {eid}")

    # ===== CSV 1: learning_curves.csv =====
    lc_rows = []
    for eid, exp in target_exps.items():
        metrics = exp.get('metrics', {})
        eval_returns = extract_eval_returns(metrics)
        label = LABELS[eid]
        for step in sorted(eval_returns.keys()):
            lc_rows.append({
                'exp_id': eid,
                'step': step,
                'eval_return': eval_returns[step],
                'config_label': label,
            })

    lc_path = os.path.join(OUTPUT_DIR, 'learning_curves.csv')
    with open(lc_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['exp_id', 'step', 'eval_return', 'config_label'])
        writer.writeheader()
        writer.writerows(lc_rows)

    # ===== CSV 2: nve_trajectories.csv =====
    nve_rows = []
    for eid, exp in target_exps.items():
        metrics = exp.get('metrics', {})
        ve_ratios = extract_ve_ratios(metrics)
        nve_data = extract_nve(metrics)
        label = LABELS[eid]

        # Collect all steps from ve_ratios and nve_data
        all_steps = sorted(set(list(ve_ratios.keys()) + list(nve_data.keys())))

        for step in all_steps:
            ve_ratio = ve_ratios.get(step, '')
            baseline_ve = BASELINE_VE.get(step, '')
            nve_val = nve_data.get(step, '')

            # Compute normalized_ve if we have ve_ratio and baseline_ve but not nve_val
            if nve_val == '' and isinstance(ve_ratio, (int, float)) and isinstance(baseline_ve, (int, float)) and baseline_ve > 0:
                nve_val = ve_ratio / baseline_ve

            nve_rows.append({
                'exp_id': eid,
                'step': step,
                've_ratio': ve_ratio,
                'baseline_ve': baseline_ve,
                'normalized_ve': round(nve_val, 4) if isinstance(nve_val, (int, float)) else nve_val,
                'config_label': label,
            })

    nve_path = os.path.join(OUTPUT_DIR, 'nve_trajectories.csv')
    with open(nve_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['exp_id', 'step', 've_ratio', 'baseline_ve', 'normalized_ve', 'config_label'])
        writer.writeheader()
        writer.writerows(nve_rows)

    # ===== CSV 3: summary_table.csv =====
    # Get baseline final eval_return
    baseline_metrics = exps.get('exp_001_baseline', {}).get('metrics', {})
    baseline_eval_returns = extract_eval_returns(baseline_metrics)
    if baseline_eval_returns:
        baseline_final_step = max(baseline_eval_returns.keys())
        baseline_final_return = baseline_eval_returns[baseline_final_step]
    else:
        baseline_final_return = None

    summary_rows = []
    for eid, exp in target_exps.items():
        metrics = exp.get('metrics', {})
        eval_returns = extract_eval_returns(metrics)
        ve_ratios = extract_ve_ratios(metrics)
        nve_data = extract_nve(metrics)
        label = LABELS[eid]

        # hypothesis and conclusion
        hypothesis = exp.get('hypothesis', '')
        conclusion = exp.get('conclusion', '')
        # Also check metrics-level verdict/causal_conclusion
        if not conclusion:
            conclusion = metrics.get('verdict', metrics.get('causal_conclusion', ''))

        # final and peak eval_return
        if eval_returns:
            sorted_steps = sorted(eval_returns.keys())
            final_step = sorted_steps[-1]
            final_eval_return = eval_returns[final_step]
            peak_eval_return = max(eval_returns.values())
            total_steps = final_step
        else:
            final_eval_return = ''
            peak_eval_return = ''
            total_steps = metrics.get('step', metrics.get('current_step', ''))
            final_step = total_steps

            # Try getting eval from other fields
            if 'eval_return_latest' in metrics:
                final_eval_return = metrics['eval_return_latest']
            if 'eval_return_peak' in metrics:
                peak_eval_return = metrics['eval_return_peak']
            if 'final_return' in metrics:
                final_eval_return = metrics['final_return']
            if 'peak_return' in metrics:
                peak_eval_return = metrics['peak_return']

        # Also check peak_return / final_return as overrides
        if 'peak_return' in metrics and isinstance(metrics['peak_return'], (int, float)):
            peak_from_metrics = metrics['peak_return']
            if isinstance(peak_eval_return, (int, float)):
                peak_eval_return = max(peak_eval_return, peak_from_metrics)
            else:
                peak_eval_return = peak_from_metrics

        # final ve_ratio
        if ve_ratios:
            final_ve_step = max(ve_ratios.keys())
            final_ve_ratio = ve_ratios[final_ve_step]
        else:
            # Try standalone fields like final_value_mean / final_eval_return
            fvm = metrics.get('final_value_mean')
            fer = metrics.get('final_eval_return', final_eval_return)
            if isinstance(fvm, (int, float)) and isinstance(fer, (int, float)) and fer > 0:
                final_ve_ratio = round(fvm / fer, 4)
            else:
                final_ve_ratio = ''

        # final nve
        if nve_data:
            final_nve_step = max(nve_data.keys())
            final_nve = nve_data[final_nve_step]
        elif isinstance(final_ve_ratio, (int, float)):
            # Try to find baseline_ve at the final_ve step
            fvs = max(ve_ratios.keys()) if ve_ratios else None
            bve = BASELINE_VE.get(fvs, None) if fvs else None
            if bve and bve > 0:
                final_nve = round(final_ve_ratio / bve, 4)
            else:
                final_nve = ''
        else:
            final_nve = ''

        # Special case: baseline experiment's nve is 1.0 by definition
        if eid == 'exp_001_baseline' and final_nve == '':
            final_nve = 1.0

        # vs_baseline_pct
        if isinstance(final_eval_return, (int, float)) and baseline_final_return is not None:
            vs_baseline_pct = round(((final_eval_return - baseline_final_return) / baseline_final_return) * 100, 2)
        else:
            vs_baseline_pct = ''

        seed = get_seed(eid, exp)

        # Override total_steps from explicit metrics fields (prefer total_steps > current_step > eval-derived)
        if 'total_steps' in metrics and isinstance(metrics['total_steps'], (int, float)):
            total_steps = int(metrics['total_steps'])
        elif 'current_step' in metrics and isinstance(metrics['current_step'], (int, float)):
            # Use current_step if it's larger than eval-derived step (RUNNING experiments)
            cs = int(metrics['current_step'])
            if isinstance(total_steps, int):
                total_steps = max(total_steps, cs)
            else:
                total_steps = cs
        elif 'step' in metrics and isinstance(metrics['step'], (int, float)):
            ms = int(metrics['step'])
            if isinstance(total_steps, int):
                total_steps = max(total_steps, ms)
            else:
                total_steps = ms

        summary_rows.append({
            'exp_id': eid,
            'config_label': label,
            'hypothesis': hypothesis,
            'conclusion': conclusion,
            'final_eval_return': final_eval_return,
            'peak_eval_return': peak_eval_return,
            'final_ve_ratio': final_ve_ratio,
            'final_nve': final_nve,
            'vs_baseline_pct': vs_baseline_pct,
            'seed': seed,
            'total_steps': total_steps,
        })

    summary_path = os.path.join(OUTPUT_DIR, 'summary_table.csv')
    fieldnames = ['exp_id', 'config_label', 'hypothesis', 'conclusion',
                  'final_eval_return', 'peak_eval_return', 'final_ve_ratio',
                  'final_nve', 'vs_baseline_pct', 'seed', 'total_steps']
    with open(summary_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_rows)

    # ===== Print summaries =====
    for name, path in [('learning_curves.csv', lc_path),
                       ('nve_trajectories.csv', nve_path),
                       ('summary_table.csv', summary_path)]:
        with open(path, encoding='utf-8') as f:
            lines = f.readlines()
        print(f"\n{'='*60}")
        print(f"{name}: {len(lines)-1} data rows")
        print(f"{'='*60}")
        for line in lines[:11]:
            print(line.rstrip())
        if len(lines) > 11:
            print(f"... ({len(lines)-11} more rows)")


if __name__ == '__main__':
    main()
