#!/usr/bin/env python3
"""Entropy breakdown: SC/SICA accuracy by majority-vote entropy group.
Directly reads raw experiment JSONs. No dependency on prior entropy scripts."""

import json
import sys
from collections import Counter

def analyze(results_path):
    with open(results_path) as f:
        data = json.load(f)
    
    if isinstance(data, dict):
        results = data.get('results', data.get('problems', []))
        k_config = data.get('summary', {}).get('k', 12)
    else:
        results = data
        k_config = 12
    
    high = {'n': 0, 'sc_correct': 0, 'sica_correct': 0}
    low = {'n': 0, 'sc_correct': 0, 'sica_correct': 0}
    
    for item in results:
        gt = item.get('ground_truth', item.get('correct_answer', item.get('label', '')))
        sica_answer = item.get('sica_answer', item.get('sica_prediction', ''))
        sc_answer = item.get('sc_answer', '')
        
        sc_vote_count = item.get('sc_vote_count', None)
        sc_vote_dist = item.get('sc_vote_distribution', {})
        
        if sc_vote_count is None and sc_vote_dist:
            sc_vote_count = max(sc_vote_dist.values()) if sc_vote_dist else 0
        
        if sc_vote_count is None:
            traces = item.get('traces', [])
            if traces:
                answers = [t.get('final_answer', t.get('answer', '')) for t in traces]
                counter = Counter(answers)
                sc_vote_count = max(counter.values()) if counter else 0
            else:
                continue
        
        K = sum(sc_vote_dist.values()) if sc_vote_dist else k_config
        
        # threshold: high entropy = majority <= 8/12 (i.e. <= 2K/3)
        threshold = K * 2 // 3  # 8 for K=12
        
        if sc_vote_count <= threshold:
            group = high
        else:
            group = low
        
        group['n'] += 1
        
        gt_norm = str(gt).strip()
        sc_norm = str(sc_answer).strip()
        sica_norm = str(sica_answer).strip()
        
        if sc_norm == gt_norm:
            group['sc_correct'] += 1
        if sica_norm == gt_norm:
            group['sica_correct'] += 1
    
    return high, low, len(results)

def to_row(exp_id, model, dataset, group_name, g):
    n = g['n']
    if n == 0:
        return {'exp': exp_id, 'model': model, 'dataset': dataset, 'group': group_name,
                'n': 0, 'sc_pct': None, 'sica_pct': None, 'delta_pp': None}
    sc_pct = round(g['sc_correct'] / n * 100, 1)
    sica_pct = round(g['sica_correct'] / n * 100, 1)
    delta = round(sica_pct - sc_pct, 1)
    return {'exp': exp_id, 'model': model, 'dataset': dataset, 'group': group_name,
            'n': n, 'sc_pct': sc_pct, 'sica_pct': sica_pct, 'delta_pp': delta}

EXPERIMENTS = [
    # (exp_id, model, dataset, path, server)
    ("exp033", "Mistral-7B", "FOLIO-204 (s42)", "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"),
    ("exp052", "Mistral-7B", "FOLIO-204 (s123)", "/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json"),
    ("exp053", "Mistral-7B", "FOLIO-204 (s456)", "/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json"),
    ("exp046", "Mistral-7B", "PW-600", "/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json"),
    ("exp036", "Qwen2.5-14B", "FOLIO-204", "/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json"),
    ("exp038", "Qwen2.5-14B", "LogiQA-200", "/root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200/results.json"),
    ("exp035", "Qwen2.5-7B", "FOLIO-204", "/root/symb_invariant_consensus/results/exp035_qwen25_7b_folio204/exp035_results.json"),
    ("exp048", "LLaMA-3.1-8B", "PW-600", "/root/symb_invariant_consensus/results/exp048_llama8b_pw600/exp048_results.json"),
]

if __name__ == '__main__':
    import os
    rows = []
    for exp_id, model, dataset, path in EXPERIMENTS:
        if not os.path.exists(path):
            print(f"SKIP {exp_id}: {path} not found", file=sys.stderr)
            continue
        high, low, total = analyze(path)
        rows.append(to_row(exp_id, model, dataset, "high_entropy (≤8/12)", high))
        rows.append(to_row(exp_id, model, dataset, "low_entropy (≥9/12)", low))
        
        sc_pct = round((high['sc_correct']+low['sc_correct'])/(high['n']+low['n'])*100, 1) if (high['n']+low['n'])>0 else None
        sica_pct = round((high['sica_correct']+low['sica_correct'])/(high['n']+low['n'])*100, 1) if (high['n']+low['n'])>0 else None
        delta = round(sica_pct - sc_pct, 1) if sc_pct and sica_pct else None
        rows.append({'exp': exp_id, 'model': model, 'dataset': dataset, 'group': 'total',
                     'n': high['n']+low['n'], 'sc_pct': sc_pct, 'sica_pct': sica_pct, 'delta_pp': delta})
    
    # Print table
    print(f"{'Exp':<8} {'Model':<14} {'Dataset':<18} {'Group':<24} {'n':>4} {'SC%':>6} {'SICA%':>6} {'Δpp':>6}")
    print("-" * 90)
    for r in rows:
        sc = f"{r['sc_pct']:.1f}" if r['sc_pct'] is not None else "N/A"
        sica = f"{r['sica_pct']:.1f}" if r['sica_pct'] is not None else "N/A"
        delta = f"{r['delta_pp']:+.1f}" if r['delta_pp'] is not None else "N/A"
        print(f"{r['exp']:<8} {r['model']:<14} {r['dataset']:<18} {r['group']:<24} {r['n']:>4} {sc:>6} {sica:>6} {delta:>6}")
    
    # Output JSON
    output = {"experiments": rows}
    json_path = "/tmp/entropy_breakdown_results.json"
    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved to {json_path}")
