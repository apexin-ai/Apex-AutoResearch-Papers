#!/usr/bin/env python3
"""Parse experiment registry and produce full_results_summary.csv and .md"""

import json
import csv
import re
import sys
from pathlib import Path

INPUT_FILE = "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/6ba878cc-0f61-428c-b0ea-a881d7a90e87/tool-results/mcp-agent-ml-research-read_registry-1778918210690.txt"
OUTPUT_DIR = Path("/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts")
CSV_OUT = OUTPUT_DIR / "full_results_summary.csv"
MD_OUT = OUTPUT_DIR / "full_results_summary.md"

# Baselines
BASELINE_PPL = {0.4: 17.694, 0.6: 17.766}

def load_experiments():
    with open(INPUT_FILE) as f:
        data = json.load(f)
    result = json.loads(data['result'])
    return result['data']['experiments']

def classify_method(exp_id):
    """Classify method based on exp_id, checked in order."""
    # bs8/batchsize BEFORE nmin check (bs8_nmin2 is a batchsize experiment)
    if "bs8" in exp_id or "batchsize" in exp_id:
        return "batchsize"
    if "uniform" in exp_id:
        return "uniform"
    # contamination_60 with tau variant -> adaptive at rho=0.6 (tau_sweep within rho=0.6)
    if "contamination_60" in exp_id and "tau0" in exp_id:
        return "adaptive"  # rho=0.6 adaptive with different tau
    if "contamination_60" in exp_id and "adaptive" in exp_id:
        return "adaptive"
    if "contamination_60" in exp_id and "grid_b" in exp_id:
        return "grid_b"
    if "contamination_60" in exp_id and "ess_only" in exp_id:
        return "ess_only"
    if "contamination_60" in exp_id and "uniform" in exp_id:
        return "uniform"
    if "contamination_60" in exp_id and "seed" in exp_id:
        return "adaptive"  # contamination_60_seed42_r2 is adaptive at rho=0.6
    if "adaptive_fix" in exp_id or "adaptive" in exp_id:
        return "adaptive"
    if "grid_b" in exp_id or "grid_b0" in exp_id:
        return "grid_b"
    if "ess_only" in exp_id:
        return "ess_only"
    # tau_sweep: only rho=0.4 experiments (tau_05_seed42, tau_06_seed42, etc.)
    if re.match(r'^tau_0', exp_id) or "tau_05" in exp_id or "tau_06" in exp_id or "tau_07" in exp_id or "tau_09" in exp_id:
        return "tau_sweep"
    if "nmin" in exp_id:
        return "nmin_ablation"
    if "golden" in exp_id:
        return "golden_ratio"
    if "detect_remove" in exp_id:
        return "detect_remove"
    if "threshold" in exp_id:
        return "threshold"
    if "random" in exp_id:
        return "random_reweight"
    return "other"

def extract_rho(exp_id, exp):
    """Extract rho from exp_id or command."""
    if "contamination_60" in exp_id or "rho06" in exp_id:
        return 0.6
    if "rho04" in exp_id:
        return 0.4
    # Check command
    cmd = exp.get('spec', {}).get('command', '')
    if not cmd and exp.get('reproduce', {}).get('command'):
        cmd = exp['reproduce']['command']
    m = re.search(r'--contamination_ratio\s+([\d.]+)', cmd)
    if m:
        return float(m.group(1))
    # Default: rho=0.4 for most experiments
    return 0.4

def extract_tau(exp_id, exp):
    """Extract tau from exp_id or command."""
    # From exp_id patterns
    m = re.search(r'tau[_]?(0[._]?\d+)', exp_id)
    if m:
        val = m.group(1).replace('_', '.').replace('..', '.')
        # Handle cases like "tau_05" -> 0.5, "tau_06" -> 0.6
        if '.' not in val and len(val) >= 2:
            val = '0.' + val[1:]
        try:
            return float(val)
        except:
            pass

    # contamination_60_tau06 -> 0.6, contamination_60_tau07 -> 0.7
    m = re.search(r'tau(\d)(\d)', exp_id)
    if m:
        return float(f"0.{m.group(1)}{m.group(2)}")

    # From command
    cmd = exp.get('spec', {}).get('command', '')
    if not cmd and exp.get('reproduce', {}).get('command'):
        cmd = exp['reproduce']['command']
    m = re.search(r'--tau\s+([\d.]+)', cmd)
    if m:
        return float(m.group(1))

    return None

def extract_b(exp_id, exp):
    """Extract b value from exp_id or command."""
    # grid_b0_3_seed42 -> 0.3, grid_b0_5_seed123 -> 0.5, grid_b1_0 -> 1.0 etc.
    m = re.search(r'grid_b(\d+)_(\d+)', exp_id)
    if m:
        return float(f"{m.group(1)}.{m.group(2)}")

    # contamination_60_grid_b0_5 -> 0.5
    m = re.search(r'grid_b(\d+)_(\d+)', exp_id)
    if m:
        return float(f"{m.group(1)}.{m.group(2)}")

    # From command --b or --bias_strength
    cmd = exp.get('spec', {}).get('command', '')
    m = re.search(r'--(?:b|bias_strength)\s+([\d.]+)', cmd)
    if m:
        return float(m.group(1))

    return None

def extract_nmin(exp_id, exp):
    """Extract n_min from exp_id or command."""
    # nmin1, nmin4, nmin5
    m = re.search(r'nmin(\d+)', exp_id)
    if m:
        return int(m.group(1))

    # From spec
    spec = exp.get('spec', {})
    if 'n_min' in spec:
        return spec['n_min']

    # From command
    cmd = spec.get('command', '')
    if not cmd and exp.get('reproduce', {}).get('command'):
        cmd = exp['reproduce']['command']
    m = re.search(r'--n_min\s+(\d+)', cmd)
    if m:
        return int(m.group(1))

    return None

def extract_seed(exp_id, exp):
    """Extract seed from exp_id or spec."""
    # seedXXX pattern
    m = re.search(r'seed(\d+)', exp_id)
    if m:
        return int(m.group(1))

    # From spec
    spec = exp.get('spec', {})
    if 'seed' in spec:
        return spec['seed']

    # From command
    cmd = spec.get('command', '')
    m = re.search(r'--seed\s+(\d+)', cmd)
    if m:
        return int(m.group(1))

    return 42

def extract_ppl(exp_id, exp):
    """Extract eval_ppl_holdout from metrics."""
    metrics = exp.get('metrics', {})
    if not metrics:
        return None

    # Try various field names
    for key in ['eval_ppl_holdout', 'eval_ppl']:
        if key in metrics and metrics[key] is not None:
            return metrics[key]

    return None

def get_conclusion(exp):
    """Get conclusion field."""
    return exp.get('conclusion', '')

def get_notes(exp):
    """Get notes or hypothesis as brief description."""
    notes = exp.get('notes', '')
    if notes:
        # Truncate to reasonable length
        return notes[:150].replace('\n', ' ').strip()
    hyp = exp.get('hypothesis', '')
    if hyp:
        return hyp[:150].replace('\n', ' ').strip()
    return ''

def get_claim(exp_id, method, rho):
    """Assign claim based on method and experiment type."""
    # Claim 1: Adaptive weighting improves over uniform (rho=0.4)
    # Claim 2: Method generalizes to higher contamination (rho=0.6)
    # Claim 3: Grid-b landscape / ablations
    if rho == 0.6:
        return 2
    if method in ['adaptive', 'uniform', 'ess_only']:
        return 1
    if method in ['grid_b']:
        return 3
    if method in ['tau_sweep', 'nmin_ablation', 'batchsize']:
        return 3
    if method in ['golden_ratio', 'detect_remove', 'threshold', 'random_reweight']:
        return 1
    return ''

def should_include(exp_id, exp):
    """Filter out infrastructure/non-training experiments."""
    skip_ids = [
        'datagen_synthetic_4gpu', 'detector_modernbert', 'detector_tfidf_lr',
        'diagnostic_contamination100', 'p0_contamination_60_datagen', 'baseline_qwen3_0.6b'
    ]
    if exp_id in skip_ids:
        return False
    # Skip killed/failed experiments with no PPL
    ppl = extract_ppl(exp_id, exp)
    conclusion = get_conclusion(exp)
    if ppl is None and conclusion in ('killed', 'failed'):
        return False
    if ppl is None:
        return False
    return True

def process_grid_b_batch(exp_id, exp):
    """Special handling for grid_b_seed42_batch which has multiple b values."""
    metrics = exp.get('metrics', {})
    rows = []
    b_values = metrics.get('b_values', [0.5, 1.0, 1.5, 2.0, 3.0, 5.0])
    for b in b_values:
        b_key = f"b{str(b).replace('.','_')}_eval_ppl"
        # Try different key formats
        ppl = None
        for fmt in [f"b{b:.1f}_eval_ppl".replace('.','_'), f"b{int(b)}_0_eval_ppl" if b == int(b) else None]:
            if fmt and fmt in metrics:
                ppl = metrics[fmt]
                break
        # Try simpler formats
        if ppl is None:
            b_str = str(b).replace('.', '_')
            if f"b{b_str}_eval_ppl" in metrics:
                ppl = metrics[f"b{b_str}_eval_ppl"]
        # Try the format in the actual data: b0_5_eval_ppl, b1_0_eval_ppl etc.
        if ppl is None:
            if b < 1:
                key_try = f"b0_{int(b*10)}_eval_ppl"
            else:
                key_try = f"b{int(b)}_{int((b-int(b))*10)}_eval_ppl"
            if key_try in metrics:
                ppl = metrics[key_try]

        if ppl is not None:
            row = {
                'exp_id': f"grid_b{b:.1f}_seed42".replace('.', '_'),
                'method': 'grid_b',
                'rho': 0.4,
                'tau': None,
                'b': b,
                'n_min': 2,
                'seed': 42,
                'eval_ppl_holdout': ppl,
                'conclusion': 'success',
                'notes': f'From batch run grid_b_seed42_batch, b={b}'
            }
            rows.append(row)
    return rows

def main():
    exps = load_experiments()

    rows = []

    # Handle grid_b_seed42_batch specially
    if 'grid_b_seed42_batch' in exps:
        batch_rows = process_grid_b_batch('grid_b_seed42_batch', exps['grid_b_seed42_batch'])
        rows.extend(batch_rows)

    for exp_id, exp in sorted(exps.items()):
        if exp_id == 'grid_b_seed42_batch':
            continue  # Already handled

        if not should_include(exp_id, exp):
            continue

        method = classify_method(exp_id)
        if method == 'other':
            continue

        rho = extract_rho(exp_id, exp)
        tau = extract_tau(exp_id, exp)
        b = extract_b(exp_id, exp)
        n_min = extract_nmin(exp_id, exp)
        seed = extract_seed(exp_id, exp)
        ppl = extract_ppl(exp_id, exp)
        conclusion = get_conclusion(exp)
        notes = get_notes(exp)

        # For adaptive methods, default tau=0.8 if not specified
        if method == 'adaptive' and tau is None:
            tau = 0.8

        # Default n_min=2 for methods that use it
        if method in ['adaptive', 'ess_only', 'grid_b', 'tau_sweep', 'golden_ratio'] and n_min is None:
            n_min = 2

        row = {
            'exp_id': exp_id,
            'method': method,
            'rho': rho,
            'tau': tau,
            'b': b,
            'n_min': n_min,
            'seed': seed,
            'eval_ppl_holdout': ppl,
            'conclusion': conclusion,
            'notes': notes
        }
        rows.append(row)

    # Compute delta_vs_uniform and claim
    for row in rows:
        ppl = row['eval_ppl_holdout']
        rho = row['rho']
        if ppl is not None and rho in BASELINE_PPL:
            row['delta_vs_uniform'] = round(ppl - BASELINE_PPL[rho], 4)
        else:
            row['delta_vs_uniform'] = None
        row['claim'] = get_claim(row['exp_id'], row['method'], row['rho'])

    # Write CSV
    fieldnames = ['exp_id', 'method', 'rho', 'tau', 'b', 'n_min', 'seed',
                  'eval_ppl_holdout', 'delta_vs_uniform', 'conclusion', 'claim', 'notes']

    with open(CSV_OUT, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in sorted(rows, key=lambda r: (r['method'], r.get('rho', 0), r.get('eval_ppl_holdout') or 99)):
            writer.writerow(row)

    print(f"Written {len(rows)} rows to {CSV_OUT}")

    # Write Markdown
    write_markdown(rows)
    print(f"Written markdown to {MD_OUT}")

def fmt_ppl(val):
    if val is None:
        return "-"
    return f"{val:.4f}"

def fmt_delta(val):
    if val is None:
        return "-"
    return f"{val:+.3f}"

def fmt_val(val, default="-"):
    if val is None:
        return default
    return str(val)

def write_markdown(rows):
    """Write grouped markdown table."""

    # Group definitions
    main_methods = ['uniform', 'adaptive', 'ess_only']
    ablation_methods = ['nmin_ablation', 'tau_sweep', 'batchsize']
    baseline_methods = ['golden_ratio', 'detect_remove', 'threshold', 'random_reweight']
    grid_method = ['grid_b']

    header = "| exp_id | method | rho | tau | b | n_min | seed | eval_ppl_holdout | delta_vs_uniform | conclusion | claim | notes |"
    sep = "|--------|--------|-----|-----|---|-------|------|------------------|------------------|------------|-------|-------|"

    def row_to_md(r):
        return f"| {r['exp_id']} | {r['method']} | {r['rho']} | {fmt_val(r['tau'])} | {fmt_val(r['b'])} | {fmt_val(r['n_min'])} | {r['seed']} | {fmt_ppl(r['eval_ppl_holdout'])} | {fmt_delta(r['delta_vs_uniform'])} | {r['conclusion']} | {fmt_val(r['claim'])} | {r['notes'][:80]} |"

    lines = []
    lines.append("# Full Results Summary")
    lines.append("")
    lines.append(f"Generated: 2026-05-16 | Total experiments with PPL: {len(rows)}")
    lines.append("")
    lines.append(f"Baselines: rho=0.4 uniform PPL = {BASELINE_PPL[0.4]}, rho=0.6 uniform PPL = {BASELINE_PPL[0.6]}")
    lines.append("")

    # 1. Main results
    lines.append("## 1. Main Results (uniform, adaptive, ess_only)")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    main_rows = [r for r in rows if r['method'] in main_methods]
    # Best grid_b per rho (lowest PPL)
    grid_rows_04 = [r for r in rows if r['method'] == 'grid_b' and r['rho'] == 0.4]
    grid_rows_06 = [r for r in rows if r['method'] == 'grid_b' and r['rho'] == 0.6]
    best_grid = []
    if grid_rows_04:
        best_grid.append(min(grid_rows_04, key=lambda r: r['eval_ppl_holdout'] or 99))
    if grid_rows_06:
        best_grid.append(min(grid_rows_06, key=lambda r: r['eval_ppl_holdout'] or 99))

    combined_main = main_rows + best_grid
    combined_main.sort(key=lambda r: (r['rho'], r['eval_ppl_holdout'] or 99))
    for r in combined_main:
        lines.append(row_to_md(r))
    lines.append("")

    # 2. Ablations
    lines.append("## 2. Ablations (nmin, tau_sweep, batchsize)")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    abl_rows = sorted([r for r in rows if r['method'] in ablation_methods],
                      key=lambda r: (r['method'], r['eval_ppl_holdout'] or 99))
    for r in abl_rows:
        lines.append(row_to_md(r))
    lines.append("")

    # 3. Baselines
    lines.append("## 3. Alternative Baselines (golden_ratio, detect_remove, threshold, random_reweight)")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    base_rows = sorted([r for r in rows if r['method'] in baseline_methods],
                       key=lambda r: (r['eval_ppl_holdout'] or 99))
    for r in base_rows:
        lines.append(row_to_md(r))
    lines.append("")

    # 4. Grid sweep full
    lines.append("## 4. Grid Sweep (all grid_b points)")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    all_grid = sorted([r for r in rows if r['method'] == 'grid_b'],
                      key=lambda r: (r['rho'], r.get('b') or 0, r['eval_ppl_holdout'] or 99))
    for r in all_grid:
        lines.append(row_to_md(r))
    lines.append("")

    with open(MD_OUT, 'w') as f:
        f.write('\n'.join(lines))

if __name__ == '__main__':
    main()
