import json
import sys
import os
import numpy as np
from itertools import combinations
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import _ner_soft_jaccard_pair
from evaluation import per_instance_f1

N = 8
OUTPUT_DIR = '/root/autodl-tmp/struct_self_consist_ie/output'

CONFIGS = {
    'qwen_scierc_ner': f'{OUTPUT_DIR}/exp_012_rerun_1024/samples.jsonl',
    'llama_scierc_ner': f'{OUTPUT_DIR}/exp007_llama_inference/samples.jsonl',
    'qwen_conll_ner': f'{OUTPUT_DIR}/exp002_conll2003/samples.jsonl',
    'llama_conll_ner': f'{OUTPUT_DIR}/exp_017_llama_conll_infer/samples.jsonl',
    'wnut17_ner': f'{OUTPUT_DIR}/exp003_wnut17_eval/samples.jsonl',
}

def entities_to_frozenset(entities):
    return frozenset((e['text'], e['type'], e['start'], e['end']) for e in entities)

def analyze_dataset(path):
    instances = []
    with open(path) as f:
        for line in f:
            instances.append(json.loads(line))

    valid = [inst for inst in instances if len(inst['gold'].get('entities', [])) > 0]

    unique_counts = []
    logprob_stds = []
    f1_stds = []
    pairwise_sj_means = []
    has_logprobs = True

    for inst in valid:
        samples = inst['samples'][:N]
        gold = inst['gold']

        # (a) unique fraction
        entity_sets = [entities_to_frozenset(s.get('entities', [])) for s in samples]
        n_unique = len(set(entity_sets))
        unique_counts.append(n_unique)

        # (b) logprob std
        logprobs = []
        for s in samples:
            lp = s.get('mean_logprob')
            if lp is not None:
                logprobs.append(lp)
        if len(logprobs) == N:
            logprob_stds.append(float(np.std(logprobs, ddof=0)))
        else:
            has_logprobs = False

        # (c) F1 std
        f1s = [per_instance_f1(s, gold, subtask='ner') for s in samples]
        f1_stds.append(float(np.std(f1s, ddof=0)))

        # (d) pairwise SJ
        sj_scores = []
        for i, j in combinations(range(N), 2):
            sj = _ner_soft_jaccard_pair(
                samples[i].get('entities', []),
                samples[j].get('entities', [])
            )
            sj_scores.append(sj)
        pairwise_sj_means.append(float(np.mean(sj_scores)))

    # aggregate (a)
    unique_arr = np.array(unique_counts)
    unique_hist = Counter(unique_counts)
    unique_histogram = {str(k): unique_hist.get(k, 0) for k in range(1, N+1)}

    # aggregate (b)
    if has_logprobs and logprob_stds:
        lp_arr = np.array(logprob_stds)
        logprob_result = {
            'mean': round(float(np.mean(lp_arr)), 6),
            'median': round(float(np.median(lp_arr)), 6),
            'p25': round(float(np.percentile(lp_arr, 25)), 6),
            'p75': round(float(np.percentile(lp_arr, 75)), 6),
        }
    else:
        logprob_result = 'N/A'

    # aggregate (c)
    f1_arr = np.array(f1_stds)

    # aggregate (d)
    sj_arr = np.array(pairwise_sj_means)
    sj_bins = {}
    for lo in np.arange(0, 1.0, 0.1):
        hi = lo + 0.1
        label = f'{lo:.1f}-{hi:.1f}'
        if lo >= 0.9:
            count = int(np.sum((sj_arr >= lo) & (sj_arr <= hi)))
        else:
            count = int(np.sum((sj_arr >= lo) & (sj_arr < hi)))
        sj_bins[label] = count

    result = {
        'n_valid': len(valid),
        'n_total': len(instances),
        'unique_fraction': {
            'mean': round(float(np.mean(unique_arr / N)), 4),
            'median': round(float(np.median(unique_arr / N)), 4),
            'histogram': unique_histogram,
        },
        'logprob_std': logprob_result,
        'f1_std': {
            'mean': round(float(np.mean(f1_arr)), 4),
            'median': round(float(np.median(f1_arr)), 4),
        },
        'pairwise_sj': {
            'mean': round(float(np.mean(sj_arr)), 4),
            'median': round(float(np.median(sj_arr)), 4),
            'p25': round(float(np.percentile(sj_arr, 25)), 4),
            'p75': round(float(np.percentile(sj_arr, 75)), 4),
            'histogram': sj_bins,
        },
    }
    return result

if __name__ == '__main__':
    os.makedirs(f'{OUTPUT_DIR}/review_round2', exist_ok=True)
    
    results = {}
    for name, path in CONFIGS.items():
        print(f'Processing {name}...', flush=True)
        results[name] = analyze_dataset(path)
        print(f'  n_valid={results[name]["n_valid"]}, unique_frac_mean={results[name]["unique_fraction"]["mean"]}, sj_mean={results[name]["pairwise_sj"]["mean"]}')

    out_path = f'{OUTPUT_DIR}/review_round2/diversity_analysis.json'
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f'\nSaved to {out_path}')
    print('\n' + json.dumps(results, indent=2, ensure_ascii=False))
