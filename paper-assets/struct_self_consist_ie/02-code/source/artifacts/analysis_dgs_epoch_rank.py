#!/usr/bin/env python3
"""DGS analysis for 3ep/10ep/rank8 experiments, compared to 5ep baseline."""

import json
import sys
import numpy as np
sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from unified_metrics import (
    compute_entity_f1, compute_degeneracy,
    bootstrap_ci, bootstrap_delta_ci
)

N_SAMPLES = 8
N_BOOT = 10000

def analyze_dgs(path, name, n_samples=N_SAMPLES, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))

    greedy_f1s, lp_f1s, gated_f1s, oracle_f1s = [], [], [], []
    n_degen = 0
    n_filtered = 0
    nondegen_greedy, nondegen_lp, nondegen_oracle = [], [], []

    for inst in instances:
        gold_ents = inst['gold']['entities']
        if gold_filter and not gold_ents:
            n_filtered += 1
            continue

        samples = inst['samples'][:n_samples]
        greedy = inst.get('greedy', samples[0])
        sample_f1s = [compute_entity_f1(s.get('entities', []), gold_ents) for s in samples]
        greedy_f1 = compute_entity_f1(greedy.get('entities', []), gold_ents)
        oracle_f1 = max(sample_f1s)

        lp_idx = max(range(len(samples)), key=lambda i: samples[i].get('mean_logprob', -1e9))
        lp_f1 = sample_f1s[lp_idx]

        is_degen = compute_degeneracy(sample_f1s)
        if is_degen:
            gated_f1 = greedy_f1
            n_degen += 1
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
        'name': name,
        'n_total': len(instances),
        'n_used': n_used,
        'n_filtered': n_filtered,
        'n_degen': n_degen,
        'degen_pct': round(n_degen / n_used * 100, 1) if n_used else 0,
        'greedy': bootstrap_ci(greedy_f1s, n_boot=N_BOOT),
        'lp_all': bootstrap_ci(lp_f1s, n_boot=N_BOOT),
        'gated': bootstrap_ci(gated_f1s, n_boot=N_BOOT),
        'oracle': bootstrap_ci(oracle_f1s, n_boot=N_BOOT),
        'delta_gated_minus_greedy': bootstrap_delta_ci(gated_f1s, greedy_f1s, n_boot=N_BOOT),
        'nondegen_delta_lp_minus_greedy': bootstrap_delta_ci(nondegen_lp, nondegen_greedy, n_boot=N_BOOT) if nondegen_lp else None,
    }

experiments = [
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_029a_scierc_3epoch/samples.jsonl', 'SciERC-3ep'),
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl', 'SciERC-5ep'),
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_029b_scierc_10epoch/samples.jsonl', 'SciERC-10ep'),
    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl', 'SciERC-rank8'),
]

results = {}
for path, name in experiments:
    print(f"Processing {name}...")
    r = analyze_dgs(path, name)
    results[name] = r

hdr = f"{'Exp':<16} {'N':>5} {'Degen%':>8} {'Greedy':>8} {'LP-all':>8} {'DGS':>8} {'Oracle':>8} {'DGS-Gre':>9} {'Headroom':>9}"
sep = "=" * 110

print(f"\n{sep}")
print("DGS ANALYSIS: Epoch & Rank Comparison (gold_filter=True, n_samples=8)")
print(sep)
print(hdr)
print("-" * 110)

for name in ['SciERC-3ep', 'SciERC-5ep', 'SciERC-10ep', 'SciERC-rank8']:
    r = results[name]
    g = r['greedy']['mean']
    lp = r['lp_all']['mean']
    d = r['gated']['mean']
    o = r['oracle']['mean']
    dg = r['delta_gated_minus_greedy']['delta']
    headroom = o - g
    print(f"{name:<16} {r['n_used']:>5} {r['degen_pct']:>7.1f}% {g:>8.4f} {lp:>8.4f} {d:>8.4f} {o:>8.4f} {dg*100:>+8.2f}pp {headroom*100:>+8.2f}pp")

print(f"\nBootstrap 95% CI for DGS-Greedy delta:")
for name in ['SciERC-3ep', 'SciERC-5ep', 'SciERC-10ep', 'SciERC-rank8']:
    d = results[name]['delta_gated_minus_greedy']
    print(f"  {name:<16} {d['delta']*100:+.2f}pp [{d['ci_lo']*100:.2f}, {d['ci_hi']*100:.2f}]")

print(f"\nDegeneracy trend (epoch):")
for name in ['SciERC-3ep', 'SciERC-5ep', 'SciERC-10ep']:
    r = results[name]
    print(f"  {name:<16} {r['degen_pct']:>5.1f}% degen, oracle headroom {(r['oracle']['mean'] - r['greedy']['mean'])*100:.2f}pp")

print(f"\nRank comparison (5ep-default vs rank8):")
for name in ['SciERC-5ep', 'SciERC-rank8']:
    r = results[name]
    print(f"  {name:<16} {r['degen_pct']:>5.1f}% degen, DGS-Greedy {r['delta_gated_minus_greedy']['delta']*100:+.2f}pp")

output = {
    'metadata': {
        'description': 'DGS analysis: epoch (3/5/10) and rank (8 vs default) comparison',
        'gold_filter': True, 'n_samples': 8, 'n_bootstrap': N_BOOT,
    },
    'results': {name: r for name, r in results.items()},
}

out_path = '/root/autodl-tmp/struct_self_consist_ie/output/dgs_epoch_rank_analysis.json'
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {out_path}")
