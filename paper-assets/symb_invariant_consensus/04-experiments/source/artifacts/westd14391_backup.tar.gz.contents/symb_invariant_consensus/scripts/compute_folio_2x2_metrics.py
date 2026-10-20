#!/usr/bin/env python3
"""Compute FOLIO 2x2 cross-model metrics matrix.

Reads 4 cell extraction JSONs + 2 intermediates dirs.
Outputs: SICA, SC, Delta, BR, BR_inf, Answer-kappa per cell.

Usage:
    python scripts/compute_folio_2x2_metrics.py
"""
import json, os, sys, glob
import numpy as np
from collections import Counter
from itertools import combinations

sys.path.insert(0, '/root/symb_invariant_consensus')

CELLS = {
    'cell_a': {
        'label': 'Mistral→Mistral',
        'gen': 'mistral', 'ext': 'mistral',
        'file': 'results/exp_folio_2x2/cell_a_mistral_mistral.json',
    },
    'cell_b': {
        'label': 'Mistral→Qwen3',
        'gen': 'mistral', 'ext': 'qwen3',
        'file': 'results/exp_folio_2x2/cell_b_mistral_qwen3.json',
    },
    'cell_c': {
        'label': 'Qwen3→Mistral',
        'gen': 'qwen3', 'ext': 'mistral',
        'file': 'results/exp_folio_2x2/cell_c_qwen3_mistral.json',
    },
    'cell_d': {
        'label': 'Qwen3→Qwen3',
        'gen': 'qwen3', 'ext': 'qwen3',
        'file': 'results/exp_folio_2x2/cell_d_qwen3_qwen3.json',
    },
}

INTERMEDIATES = {
    'mistral': 'results/exp033_mistral_7b_folio204/intermediates',
    'qwen3': 'results/exp_folio_2x2_qwen3/intermediates',
}

VALID_ANSWERS = {'True', 'False', 'Unknown'}
CATEGORIES = ['True', 'False', 'Unknown']

def normalize_answer(ans):
    s = str(ans).strip()
    if s.startswith('\\text{'):
        s = s[len('\\text{'):]
        if s.endswith('}'): s = s[:-1]
        s = s.strip()
    low = s.lower()
    mapping = {'true': 'True', 'false': 'False', 'unknown': 'Unknown',
               'yes': 'True', 'no': 'False', 'uncertain': 'Unknown',
               'undetermined': 'Unknown', 't': 'True', 'f': 'False', 'u': 'Unknown'}
    return mapping.get(low, s.capitalize() if s else '')


def load_intermediates(intermed_dir):
    data = {}
    for fpath in sorted(glob.glob(os.path.join(intermed_dir, '*.json'))):
        with open(fpath) as f:
            d = json.load(f)
        qid = d['problem']['id']
        data[qid] = {
            'traces': d['sica_result']['traces'],
            'gt': d['problem']['answer'],
        }
    return data


def compute_sc(intermediates):
    correct = 0
    total = 0
    for qid, d in intermediates.items():
        answers = [normalize_answer(t['answer']) for t in d['traces'] if t.get('answer')]
        valid = [a for a in answers if a in VALID_ANSWERS]
        if not valid:
            total += 1
            continue
        counts = Counter(valid)
        mx = max(counts.values())
        top = sorted([a for a, c in counts.items() if c == mx])
        sc_answer = top[0]
        if sc_answer == d['gt']:
            correct += 1
        total += 1
    return round(100 * correct / total, 2) if total > 0 else 0


def compute_answer_kappa(intermediates):
    cat_idx = {c: i for i, c in enumerate(CATEGORIES)}
    ratings = []
    for qid in sorted(intermediates.keys()):
        d = intermediates[qid]
        row = [0] * len(CATEGORIES)
        for t in d['traces']:
            ans = normalize_answer(t.get('answer', ''))
            if ans in cat_idx:
                row[cat_idx[ans]] += 1
            elif ans.strip():
                row[cat_idx['Unknown']] += 1
        ratings.append(row)

    M = np.array(ratings, dtype=float)
    n_i = M.sum(axis=1)
    valid = n_i >= 2
    M = M[valid]
    n_i = n_i[valid]
    N = M.shape[0]
    if N == 0:
        return float('nan')

    P_i = (np.sum(M**2, axis=1) - n_i) / (n_i * (n_i - 1))
    P_bar = np.mean(P_i)
    p_j = M.sum(axis=0) / n_i.sum()
    P_e = np.sum(p_j**2)
    if P_e >= 1.0:
        return 1.0
    return float((P_bar - P_e) / (1 - P_e))


def compute_cell_metrics(cell_data, sc_acc):
    results = cell_data.get('results', [])
    n = len(results)
    if n == 0:
        return {}

    sica_correct = sum(1 for r in results if r['cross_model_correct'])
    sica_acc = round(100 * sica_correct / n, 2)
    delta = round(sica_acc - sc_acc, 2)

    br_values = []
    br_inf_count = 0
    n_wrong = 0
    for r in results:
        if r['cross_model_correct']:
            continue
        n_wrong += 1
        scores = r.get('cross_model_scores', {})
        if not scores:
            continue
        sorted_scores = sorted(scores.values(), reverse=True)
        if len(sorted_scores) < 2:
            br_inf_count += 1
            continue
        top = sorted_scores[0]
        second = sorted_scores[1]
        if second <= 0:
            br_inf_count += 1
        else:
            br_values.append(top / second)

    br_mean = round(np.mean(br_values), 4) if br_values else float('inf')
    br_median = round(np.median(br_values), 4) if br_values else float('inf')
    br_inf_rate = round(br_inf_count / n_wrong, 4) if n_wrong > 0 else 0

    return {
        'sica_acc': sica_acc,
        'delta_pp': delta,
        'br_mean': br_mean,
        'br_median': br_median,
        'br_inf_rate': br_inf_rate,
        'n_wrong': n_wrong,
        'n_br_finite': len(br_values),
        'n_br_inf': br_inf_count,
        'n_total': n,
    }


def mcnemar_test(results_a, results_b):
    id_to_a = {r['problem_id']: r['cross_model_correct'] for r in results_a}
    id_to_b = {r['problem_id']: r['cross_model_correct'] for r in results_b}
    common = set(id_to_a.keys()) & set(id_to_b.keys())
    a_only = sum(1 for pid in common if id_to_a[pid] and not id_to_b[pid])
    b_only = sum(1 for pid in common if id_to_b[pid] and not id_to_a[pid])
    n = a_only + b_only
    if n == 0:
        return {'p': 1.0, 'a_only': 0, 'b_only': 0, 'n': 0}
    try:
        from scipy.stats import binomtest
        p = binomtest(min(a_only, b_only), n, 0.5).pvalue
    except ImportError:
        chi2 = (abs(a_only - b_only) - 1)**2 / max(n, 1)
        from math import erfc, sqrt
        p = erfc(sqrt(chi2 / 2))
    return {'p': round(p, 6), 'a_only': a_only, 'b_only': b_only, 'n': n}


def main():
    base = '/root/symb_invariant_consensus'

    # Load intermediates for SC and kappa
    print("Loading intermediates...")
    gen_data = {}
    gen_sc = {}
    gen_kappa = {}
    for gen_name, intermed_dir in INTERMEDIATES.items():
        full_path = os.path.join(base, intermed_dir)
        if not os.path.isdir(full_path):
            print(f"  WARN: {full_path} not found, skipping {gen_name}")
            continue
        data = load_intermediates(full_path)
        gen_data[gen_name] = data
        gen_sc[gen_name] = compute_sc(data)
        gen_kappa[gen_name] = round(compute_answer_kappa(data), 4)
        print(f"  {gen_name}: {len(data)} problems, SC={gen_sc[gen_name]}%, kappa={gen_kappa[gen_name]}")

    # Load cell results
    print("\nLoading cell results...")
    cell_results = {}
    for cell_key, cfg in CELLS.items():
        fpath = os.path.join(base, cfg['file'])
        if not os.path.isfile(fpath):
            print(f"  WARN: {fpath} not found, skipping {cell_key}")
            continue
        with open(fpath) as f:
            data = json.load(f)
        cell_results[cell_key] = data
        n = len(data.get('results', []))
        print(f"  {cell_key} ({cfg['label']}): {n} results")

    # Compute per-cell metrics
    print("\nComputing metrics...")
    matrix = {}
    for cell_key, cfg in CELLS.items():
        if cell_key not in cell_results:
            continue
        gen = cfg['gen']
        sc = gen_sc.get(gen, 0)
        kappa = gen_kappa.get(gen, 0)
        metrics = compute_cell_metrics(cell_results[cell_key], sc)
        metrics['sc_acc'] = sc
        metrics['process_kappa'] = kappa
        metrics['label'] = cfg['label']
        matrix[cell_key] = metrics
        print(f"  {cfg['label']}: SICA={metrics.get('sica_acc','?')}%, "
              f"Delta={metrics.get('delta_pp','?')}pp, "
              f"BR={metrics.get('br_mean','?')}, "
              f"kappa={kappa}")

    # McNemar tests: same extractor, different generator
    print("\nMcNemar tests...")
    mcnemar = {}
    pairs = [
        ('cell_a', 'cell_c', 'mistral_ext: A vs C'),
        ('cell_b', 'cell_d', 'qwen3_ext: B vs D'),
    ]
    for k1, k2, label in pairs:
        if k1 in cell_results and k2 in cell_results:
            r = mcnemar_test(cell_results[k1]['results'], cell_results[k2]['results'])
            mcnemar[label] = r
            print(f"  {label}: p={r['p']:.4f} ({r['a_only']} vs {r['b_only']})")

    # Save
    output = {
        'generator_stats': {
            gen: {'sc_acc': gen_sc[gen], 'answer_kappa': gen_kappa[gen],
                  'n_problems': len(gen_data[gen])}
            for gen in gen_data
        },
        'matrix': matrix,
        'mcnemar': mcnemar,
        'matrix_note': 'Generator(row) x Extractor(col). SC/Answer-kappa depend only on generator.',
    }

    out_path = os.path.join(base, 'results/exp_folio_2x2/folio_2x2_metrics.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")

    # Print 2x2 table
    print("\n" + "="*80)
    print("FOLIO-204 Cross-Model 2x2 Matrix")
    print("="*80)
    print(f"{'':30s} | {'Mistral ext':>20s} | {'Qwen3 ext':>20s}")
    print("-"*80)
    for gen in ['mistral', 'qwen3']:
        sc = gen_sc.get(gen, '?')
        kappa = gen_kappa.get(gen, '?')
        gen_label = f"{'Mistral' if gen=='mistral' else 'Qwen3'} gen (SC={sc}%)"
        
        cells_row = []
        for ext in ['mistral', 'qwen3']:
            cell_key = [k for k, v in CELLS.items() if v['gen']==gen and v['ext']==ext][0]
            m = matrix.get(cell_key, {})
            cell_str = f"SICA={m.get('sica_acc','?')}%,Δ={m.get('delta_pp','?')}"
            cells_row.append(cell_str)
        print(f"{gen_label:30s} | {cells_row[0]:>20s} | {cells_row[1]:>20s}")
        
        cells_row2 = []
        for ext in ['mistral', 'qwen3']:
            cell_key = [k for k, v in CELLS.items() if v['gen']==gen and v['ext']==ext][0]
            m = matrix.get(cell_key, {})
            cell_str = f"BR={m.get('br_mean','?')},κ={kappa}"
            cells_row2.append(cell_str)
        print(f"{'':30s} | {cells_row2[0]:>20s} | {cells_row2[1]:>20s}")
        print("-"*80)

    print("\nFOLIO_2X2_DONE")


if __name__ == '__main__':
    main()
