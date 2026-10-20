#!/usr/bin/env python3
"""Runner: process all experiments and produce combined Wild 6 results."""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from wild6_kappa_sc_analysis import analyze_experiment, load_results

EXPERIMENTS = [
    # (results_json_path, display_name, model, dataset)
    ("results/exp033_mistral_7b_folio204/exp033_results.json", "exp033", "Mistral-7B", "FOLIO-204"),
    ("results/exp067_mistral_folio_seed789/exp067_results.json", "exp067_seed789", "Mistral-7B (s789)", "FOLIO-204"),
    ("results/exp052_mistral_folio204_seed123/exp052_results.json", "exp052_seed123", "Mistral-7B (s123)", "FOLIO-204"),
    ("results/exp061_qwen25_7b_folio204/exp061_results.json", "exp061", "Qwen2.5-7B", "FOLIO-204"),
    ("results/exp066_qwen14b_folio_seed123/exp066_results.json", "exp066", "Qwen2.5-14B", "FOLIO-204"),
    ("results/exp036_qwen25_14b_folio204/results.json", "exp036", "Qwen2.5-14B (s42)", "FOLIO-204"),
    ("results/exp062_gemma27b_folio204/exp062_results.json", "exp062", "Gemma2-27B", "FOLIO-204"),
    ("results/exp-063-llama8b-folio204-16639/results.json", "exp063", "LLaMA-3.1-8B", "FOLIO-204"),
    ("results/exp034_llama31_8b_folio204/exp034_results.json", "exp034", "LLaMA-3.1-8B (25068)", "FOLIO-204"),
    ("results/exp069_mistral_logiqa200/exp069_results.json", "exp069_logiqa", "Mistral-7B", "LogiQA-200"),
    ("results/exp070_qwen7b_logiqa200/exp070_results.json", "exp070_logiqa", "Qwen2.5-7B", "LogiQA-200"),
    ("results/exp069_llama8b_logiqa200/exp069_results.json", "exp069_llama_logiqa", "LLaMA-3.1-8B", "LogiQA-200"),
]

ROOT = "/root/symb_invariant_consensus"

def main():
    all_results = []
    for rel_path, name, model, dataset in EXPERIMENTS:
        full_path = os.path.join(ROOT, rel_path)
        if not os.path.exists(full_path):
            print(f"SKIP {name}: {full_path} not found", file=sys.stderr)
            continue
        try:
            data = load_results(full_path)
            result = analyze_experiment(data, name)
            result['model'] = model
            result['dataset'] = dataset
            all_results.append(result)
            print(f"OK   {name}: {model} {dataset} — SC={result['standard_sc']['accuracy']:.4f}", file=sys.stderr)
        except Exception as e:
            print(f"ERR  {name}: {e}", file=sys.stderr)

    combined = {
        'wild6_kappa_aware_sc': {
            'description': 'κ-aware adaptive SC threshold analysis',
            'n_experiments': len(all_results),
            'experiments': all_results,
        }
    }

    # Summary table
    summary_rows = []
    for r in all_results:
        sc = r['standard_sc']['accuracy']
        best_name, best_acc, best_delta = 'standard_sc', sc, 0.0

        for sname, sdata in r.get('adaptive_forward', {}).items():
            if sdata['accuracy'] > best_acc:
                best_name = f'fwd_{sname}'
                best_acc = sdata['accuracy']
                best_delta = sdata['delta_vs_sc']

        for sname, sdata in r.get('threshold_sweep', {}).items():
            if sdata['overall_acc'] > best_acc:
                best_name = f'thresh_{sname}'
                best_acc = sdata['overall_acc']
                best_delta = sdata['overall_acc'] - sc

        for sname, sdata in r.get('entropy_adaptive', {}).items():
            if sdata['accuracy'] > best_acc:
                best_name = f'entropy_{sname}'
                best_acc = sdata['accuracy']
                best_delta = sdata['delta_vs_sc']

        summary_rows.append({
            'model': r['model'],
            'dataset': r['dataset'],
            'experiment': r['experiment'],
            'n': r['n'],
            'standard_sc': round(sc, 4),
            'best_adaptive': round(best_acc, 4),
            'delta': round(best_delta, 4),
            'best_strategy': best_name,
        })

    combined['summary_table'] = summary_rows

    outpath = os.path.join(ROOT, 'results/wild6_kappa_aware_sc/results.json')
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, 'w') as f:
        json.dump(combined, f, indent=2)
    print(f"\nSaved to {outpath}", file=sys.stderr)
    print(json.dumps(combined['summary_table'], indent=2))


if __name__ == '__main__':
    main()
