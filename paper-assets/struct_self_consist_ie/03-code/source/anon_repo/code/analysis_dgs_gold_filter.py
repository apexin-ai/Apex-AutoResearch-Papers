#!/usr/bin/env python3
# FIX(2026-05-18): SciERC data path corrected from exp001_n16_seed42 to exp_012_rerun_1024
# to match entity_consensus.py and ccs_selection.py (resolves 0.22pp greedy F1 discrepancy)
"""DGS selection analysis with gold_filter=True (skip instances with empty gold entities)."""

import json
import os
import sys
import numpy as np
sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from unified_metrics import compute_entity_f1, compute_degeneracy


def analyze_dataset(path, name, n_samples=8, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            instances.append(json.loads(line))

    n_total = len(instances)
    n_gold_nonempty = sum(1 for inst in instances if inst['gold']['entities'])
    n_filtered_out = 0

    greedy_f1s, lp_f1s, gated_f1s, oracle_f1s = [], [], [], []
    degen_greedy, degen_oracle = [], []
    nondegen_greedy, nondegen_lp, nondegen_oracle = [], [], []
    n_degen = 0

    for inst in instances:
        gold_ents = inst['gold']['entities']
        if gold_filter and not gold_ents:
            n_filtered_out += 1
            continue

        samples = inst['samples'][:n_samples]
        greedy = inst['greedy']

        sample_f1s = [compute_entity_f1(s.get('entities', []), gold_ents) for s in samples]
        greedy_f1 = compute_entity_f1(greedy.get('entities', []), gold_ents)
        oracle_f1 = max(sample_f1s)

        lp_idx = max(range(len(samples)), key=lambda i: samples[i]['mean_logprob'])
        lp_f1 = sample_f1s[lp_idx]

        is_degen = compute_degeneracy(sample_f1s)

        if is_degen:
            gated_f1 = greedy_f1
            n_degen += 1
            degen_greedy.append(greedy_f1)
            degen_oracle.append(oracle_f1)
        else:
            gated_f1 = lp_f1
            nondegen_greedy.append(greedy_f1)
            nondegen_lp.append(lp_f1)
            nondegen_oracle.append(oracle_f1)

        greedy_f1s.append(greedy_f1)
        lp_f1s.append(lp_f1)
        gated_f1s.append(gated_f1)
        oracle_f1s.append(oracle_f1)

    n_used = len(greedy_f1s)
    return {
        'name': name, 'n_total': n_total, 'n_used': n_used,
        'n_gold_nonempty': n_gold_nonempty, 'n_filtered_out': n_filtered_out,
        'n_degen': n_degen,
        'greedy': greedy_f1s, 'lp': lp_f1s, 'gated': gated_f1s, 'oracle': oracle_f1s,
        'degen_greedy': degen_greedy, 'degen_oracle': degen_oracle,
        'nondegen_greedy': nondegen_greedy, 'nondegen_lp': nondegen_lp, 'nondegen_oracle': nondegen_oracle,
    }

def bootstrap_ci(values, n_boot=10000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    arr = np.array(values)
    n = len(arr)
    if n == 0:
        return {'mean': 0.0, 'ci_lo': 0.0, 'ci_hi': 0.0}
    boot_means = [arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)]
    boot_means = sorted(boot_means)
    lo = boot_means[int((1 - ci) / 2 * n_boot)]
    hi = boot_means[int((1 + ci) / 2 * n_boot)]
    return {'mean': float(arr.mean()), 'ci_lo': float(lo), 'ci_hi': float(hi)}

def bootstrap_delta_ci(a, b, n_boot=10000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    a_arr, b_arr = np.array(a), np.array(b)
    n = len(a_arr)
    if n == 0:
        return {'delta': 0.0, 'ci_lo': 0.0, 'ci_hi': 0.0}
    deltas = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        deltas.append(a_arr[idx].mean() - b_arr[idx].mean())
    deltas = sorted(deltas)
    lo = deltas[int((1 - ci) / 2 * n_boot)]
    hi = deltas[int((1 + ci) / 2 * n_boot)]
    return {'delta': float((a_arr - b_arr).mean()), 'ci_lo': float(lo), 'ci_hi': float(hi)}


datasets = [
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl', 'SciERC', 8),
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl', 'CoNLL', 8),
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl', 'FewNERD', 8),
]

# Load old results for comparison
old_path = '/root/autodl-tmp/struct_self_consist_ie/output/dgs_selection_results.json'
old_results = {}
if os.path.exists(old_path):
    with open(old_path) as f:
        old_data = json.load(f)
    for entry in old_data.get('summary', []):
        old_results[entry['dataset']] = entry

all_results = []
for path, name, ns in datasets:
    r = analyze_dataset(path, name, ns, gold_filter=True)
    all_results.append(r)

# Print results
def avg(lst):
    return sum(lst) / len(lst) if lst else 0.0

print(f"\n{'='*90}")
print("DGS Selection Results (gold_filter=True)")
print(f"{'='*90}")

for r in all_results:
    n = r['n_used']
    nd = r['n_degen']
    dp = nd / n * 100
    g = avg(r['greedy'])
    l = avg(r['lp'])
    gt = avg(r['gated'])
    o = avg(r['oracle'])

    print(f"\n--- {r['name']} ---")
    print(f"Total: {r['n_total']}, Gold-nonempty: {r['n_gold_nonempty']}, Used: {r['n_used']}, Filtered: {r['n_filtered_out']}")
    print(f"Degenerate: {nd} ({dp:.1f}%), Non-degenerate: {n-nd} ({100-dp:.1f}%)")
    print(f"  Greedy: {g:.4f}  LP-all: {l:.4f}  DGS: {gt:.4f}  Oracle: {o:.4f}")
    print(f"  DGS-Greedy: {gt-g:+.4f}  DGS-LP: {gt-l:+.4f}")

# Comparison with old results
print(f"\n{'='*90}")
print("COMPARISON: old (no gold filter) vs new (gold_filter=True)")
print(f"{'='*90}")
print(f"{'Dataset':<12} {'Metric':<12} {'Old':>10} {'New':>10} {'Delta':>10}")
print(f"{'-'*56}")
for r in all_results:
    name = r['name']
    if name not in old_results:
        print(f"{name:<12} (no old results)")
        continue
    old = old_results[name]
    new_g = avg(r['greedy'])
    new_l = avg(r['lp'])
    new_gt = avg(r['gated'])
    new_o = avg(r['oracle'])
    for metric, old_key, new_val in [
        ('Greedy', 'greedy_f1', new_g),
        ('LP-all', 'lp_f1', new_l),
        ('DGS', 'gated_f1', new_gt),
        ('Oracle', 'oracle_f1', new_o),
    ]:
        ov = old[old_key]
        print(f"{name:<12} {metric:<12} {ov:>10.4f} {new_val:>10.4f} {new_val-ov:>+10.4f}")
    old_dp = old['degen_pct']
    new_dp = r['n_degen'] / r['n_used'] * 100
    print(f"{name:<12} {'Degen%':<12} {old_dp:>9.1f}% {new_dp:>9.1f}% {new_dp-old_dp:>+9.1f}%")
    print()

# Build JSON output with bootstrap CI
json_output = {
    'metadata': {
        'gold_filter': True,
        'description': 'DGS selection with gold_filter=True (instances with empty gold entities excluded)',
        'n_samples': 8,
        'n_bootstrap': 10000,
        'seed': 42,
    },
    'datasets': {},
    'summary': [],
}

for r in all_results:
    name = r['name']
    n = r['n_used']
    nd = r['n_degen']

    entry = {
        'n_instances_total': r['n_total'],
        'n_instances_used': n,
        'n_gold_nonempty': r['n_gold_nonempty'],
        'n_filtered_out': r['n_filtered_out'],
        'n_degenerate': nd,
        'n_nondegenerate': n - nd,
        'degen_pct': round(nd / n * 100, 1),
        'greedy': bootstrap_ci(r['greedy']),
        'lp_all': bootstrap_ci(r['lp']),
        'gated': bootstrap_ci(r['gated']),
        'oracle': bootstrap_ci(r['oracle']),
        'delta_gated_minus_greedy': bootstrap_delta_ci(r['gated'], r['greedy']),
        'delta_gated_minus_lp': bootstrap_delta_ci(r['gated'], r['lp']),
    }

    if r['degen_greedy']:
        entry['degenerate'] = {
            'greedy_eq_gated': bootstrap_ci(r['degen_greedy']),
            'oracle': bootstrap_ci(r['degen_oracle']),
        }

    if r['nondegen_lp']:
        entry['nondegenerate'] = {
            'greedy': bootstrap_ci(r['nondegen_greedy']),
            'lp': bootstrap_ci(r['nondegen_lp']),
            'oracle': bootstrap_ci(r['nondegen_oracle']),
            'delta_lp_minus_greedy': bootstrap_delta_ci(r['nondegen_lp'], r['nondegen_greedy']),
        }

    json_output['datasets'][name] = entry
    json_output['summary'].append({
        'dataset': name,
        'n_total': r['n_total'],
        'n_used': n,
        'n_filtered': r['n_filtered_out'],
        'degen_pct': entry['degen_pct'],
        'greedy_f1': round(entry['greedy']['mean'], 4),
        'lp_f1': round(entry['lp_all']['mean'], 4),
        'gated_f1': round(entry['gated']['mean'], 4),
        'oracle_f1': round(entry['oracle']['mean'], 4),
        'gated_minus_greedy_pp': round(entry['delta_gated_minus_greedy']['delta'] * 100, 2),
        'gated_minus_lp_pp': round(entry['delta_gated_minus_lp']['delta'] * 100, 2),
    })

# Print summary table
print(f"\n{'='*100}")
print("SUMMARY TABLE (gold_filter=True)")
print(f"{'='*100}")
print(f"{'Dataset':<12} {'Total':>6} {'Used':>6} {'Degen%':>8} {'Greedy':>8} {'LP-all':>8} {'DGS':>8} {'Oracle':>8} {'D-Gre':>8} {'D-LP':>8}")
print(f"{'-'*100}")
for s in json_output['summary']:
    print(f"{s['dataset']:<12} {s['n_total']:>6} {s['n_used']:>6} {s['degen_pct']:>7.1f}% {s['greedy_f1']:>8.4f} {s['lp_f1']:>8.4f} {s['gated_f1']:>8.4f} {s['oracle_f1']:>8.4f} {s['gated_minus_greedy_pp']:>+7.2f}% {s['gated_minus_lp_pp']:>+7.2f}%")

# Print bootstrap CIs for DGS vs Greedy
print(f"\nBootstrap 95% CI for DGS vs Greedy:")
for name, ds in json_output['datasets'].items():
    d = ds['delta_gated_minus_greedy']
    print(f"  {name}: {d['delta']:+.4f} [{d['ci_lo']:.4f}, {d['ci_hi']:.4f}]")

# Save
out_path = '/root/autodl-tmp/struct_self_consist_ie/output/dgs_selection_results.json'
with open(out_path, 'w') as f:
    json.dump(json_output, f, indent=2)
print(f"\nJSON saved to {out_path}")
