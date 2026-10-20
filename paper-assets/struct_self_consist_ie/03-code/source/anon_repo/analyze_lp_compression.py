import json
import numpy as np
from scipy.stats import spearmanr
import os

def entity_key_set(sample):
    """Extract frozenset of (text, type, start, end) tuples for entities."""
    entities = sample.get('entities', [])
    return frozenset((e['text'], e['type'], e['start'], e['end']) for e in entities)

def compute_entity_f1(pred_entities, gold_entities):
    """Compute entity-level micro F1."""
    pred_set = set((e['text'], e['type'], e['start'], e['end']) for e in pred_entities)
    gold_set = set((e['text'], e['type'], e['start'], e['end']) for e in gold_entities)
    
    if len(pred_set) == 0 and len(gold_set) == 0:
        return 1.0
    if len(pred_set) == 0 or len(gold_set) == 0:
        return 0.0
    
    tp = len(pred_set & gold_set)
    precision = tp / len(pred_set) if pred_set else 0.0
    recall = tp / len(gold_set) if gold_set else 0.0
    
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)

def analyze_dataset(filepath, dataset_name, max_instances=None):
    """Analyze LP compression for one dataset."""
    data = []
    with open(filepath) as f:
        for i, line in enumerate(f):
            if max_instances and i >= max_instances:
                break
            data.append(json.loads(line))
    
    lp_ranges = []
    within_rhos = []
    degen_count = 0
    total = len(data)
    
    for inst in data:
        gold_entities = inst['gold']['entities']
        samples = inst['samples']
        
        # Extract per-sample logprobs and F1s
        lps = [s['cumulative_logprob'] for s in samples]
        f1s = [compute_entity_f1(s.get('entities', []), gold_entities) for s in samples]
        
        # LP range
        lp_range = max(lps) - min(lps)
        lp_ranges.append(lp_range)
        
        # Check degeneracy: all samples produce same entity set
        key_sets = [entity_key_set(s) for s in samples]
        unique_key_sets = len(set(key_sets))
        
        if unique_key_sets <= 1:
            degen_count += 1
        else:
            # Non-degenerate: compute within-instance correlation
            if len(set(lps)) > 1 and len(set(f1s)) > 1:
                rho, _ = spearmanr(lps, f1s)
                if not np.isnan(rho):
                    within_rhos.append(rho)
    
    lp_ranges = np.array(lp_ranges)
    median_range = float(np.median(lp_ranges))
    tied_fraction = float(np.mean(lp_ranges < 0.001))
    degen_frac = degen_count / total
    mean_within_rho = float(np.mean(within_rhos)) if within_rhos else None
    median_within_rho = float(np.median(within_rhos)) if within_rhos else None
    
    result = {
        'dataset': dataset_name,
        'n_instances': total,
        'degen_fraction': degen_frac,
        'median_lp_range': median_range,
        'tied_fraction': tied_fraction,
        'mean_within_rho': mean_within_rho,
        'median_within_rho': median_within_rho,
        'n_non_degen_with_rho': len(within_rhos),
        'lp_range_percentiles': {
            'p25': float(np.percentile(lp_ranges, 25)),
            'p50': float(np.percentile(lp_ranges, 50)),
            'p75': float(np.percentile(lp_ranges, 75)),
            'p90': float(np.percentile(lp_ranges, 90)),
        }
    }
    
    print(f"\n{dataset_name} (n={total}):")
    print(f"  Degen fraction: {degen_frac:.1%}")
    print(f"  Median LP range: {median_range:.4f} nats")
    print(f"  LP tied fraction (<0.001): {tied_fraction:.1%}")
    print(f"  LP range percentiles: p25={result['lp_range_percentiles']['p25']:.4f}, p75={result['lp_range_percentiles']['p75']:.4f}, p90={result['lp_range_percentiles']['p90']:.4f}")
    if mean_within_rho is not None:
        print(f"  Within-instance rho(LP,F1): mean={mean_within_rho:.4f}, median={median_within_rho:.4f}, n={len(within_rhos)}")
    else:
        print(f"  Within-instance rho(LP,F1): N/A (no valid instances)")
    
    return result

if __name__ == '__main__':
    datasets = [
        ('/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl', 'SciERC_rank8', None),
        ('/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl', 'SciERC_full_rank', None),
        ('/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl', 'FewNERD', 5000),
    ]
    
    results = []
    for path, name, max_inst in datasets:
        r = analyze_dataset(path, name, max_inst)
        results.append(r)
    
    # Print comparison table
    print("\n\n=== LP Compression Analysis (R17 W2) ===\n")
    print(f"{'Dataset':<20} | {'Degen%':>7} | {'Med LP Range':>12} | {'Tied Frac':>9} | {'Within rho mean':>15} | {'Within rho med':>14} | {'n_rho':>5}")
    print("-" * 100)
    for r in results:
        rho_mean = f"{r['mean_within_rho']:.4f}" if r['mean_within_rho'] is not None else "N/A"
        rho_med = f"{r['median_within_rho']:.4f}" if r['median_within_rho'] is not None else "N/A"
        print(f"{r['dataset']:<20} | {r['degen_fraction']:>6.1%} | {r['median_lp_range']:>12.4f} | {r['tied_fraction']:>8.1%} | {rho_mean:>15} | {rho_med:>14} | {r['n_non_degen_with_rho']:>5}")
    
    # Save results
    outdir = '/root/autodl-tmp/struct_self_consist_ie/output/r17_analyses'
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, 'lp_compression_comparison.json')
    with open(outpath, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {outpath}")
