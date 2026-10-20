#!/usr/bin/env python3
"""Compute Fleiss' kappa for exp-033 and exp-046."""
import json, os, glob, sys
import numpy as np

def fleiss_kappa(M):
    """Generalized Fleiss' kappa allowing variable n_i per subject."""
    N = M.shape[0]
    n_i = M.sum(axis=1)  # raters per subject
    
    # Skip subjects with < 2 raters
    valid = n_i >= 2
    M = M[valid]
    n_i = n_i[valid]
    N = M.shape[0]
    
    if N == 0:
        return float('nan')
    
    # P_i for each subject
    P_i = (np.sum(M**2, axis=1) - n_i) / (n_i * (n_i - 1))
    P_bar = np.mean(P_i)
    
    # Category proportions
    p_j = M.sum(axis=0) / n_i.sum()
    P_e = np.sum(p_j**2)
    
    if (1 - P_e) == 0:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)

def process_experiment(results_dir, exp_name):
    files = sorted(glob.glob(os.path.join(results_dir, "*.json")))
    if not files:
        print(f"  No files found in {results_dir}")
        return None
    
    categories = ['True', 'False', 'Unknown']
    cat_idx = {c: i for i, c in enumerate(categories)}
    ratings = []
    n_invalid_traces = 0
    n_total_traces = 0
    per_question_n = []
    
    for f in sorted(files):
        with open(f) as fh:
            data = json.load(fh)
        
        sr = data.get('sica_result', {})
        
        # Method 1: use answer_counts directly
        ac = sr.get('answer_counts', {})
        row = [0, 0, 0]
        total_valid = 0
        for cat, count in ac.items():
            if cat in cat_idx:
                row[cat_idx[cat]] += count
                total_valid += count
        
        # Cross-check with traces
        traces = sr.get('traces', [])
        n_total_traces += len(traces)
        trace_votes = [0, 0, 0]
        for t in traces:
            ans = t.get('answer', '')
            if ans in cat_idx:
                trace_votes[cat_idx[ans]] += 1
            else:
                n_invalid_traces += 1
        
        # Use answer_counts (more reliable, already aggregated)
        ratings.append(row)
        per_question_n.append(sum(row))
    
    M = np.array(ratings, dtype=float)
    n_per_q = M.sum(axis=1)
    
    kappa = fleiss_kappa(M)
    K_nominal = 12
    K_effective_mean = np.mean(n_per_q)
    eff_k = K_effective_mean * (1 - kappa)
    
    # Unanimous: all valid votes go to one category
    unanimous = np.sum(M.max(axis=1) == n_per_q) / len(M) * 100
    
    # Category distribution
    total_votes = M.sum()
    cat_dist = {c: float(M[:, i].sum() / total_votes * 100) for i, c in enumerate(categories)}
    
    # Agreement distribution
    max_frac = M.max(axis=1) / n_per_q
    
    result = {
        'experiment': exp_name,
        'n_problems': len(M),
        'K_nominal': K_nominal,
        'K_effective_mean': float(K_effective_mean),
        'min_valid_votes': int(n_per_q.min()),
        'max_valid_votes': int(n_per_q.max()),
        'fleiss_kappa': float(kappa),
        'effective_K': float(eff_k),
        'unanimous_rate_pct': float(unanimous),
        'mean_max_agreement_pct': float(max_frac.mean() * 100),
        'category_distribution_pct': cat_dist,
        'n_invalid_traces': int(n_invalid_traces),
        'n_total_traces': int(n_total_traces),
    }
    
    print(f"\n{'='*50}")
    print(f"  {exp_name}")
    print(f"{'='*50}")
    print(f"  n_problems:          {result['n_problems']}")
    print(f"  K (nominal):         {result['K_nominal']}")
    print(f"  Mean valid votes/q:  {result['K_effective_mean']:.2f}")
    print(f"  Min/Max valid votes: {result['min_valid_votes']}/{result['max_valid_votes']}")
    print(f"  Invalid traces:      {result['n_invalid_traces']}/{result['n_total_traces']}")
    print(f"  ---")
    print(f"  Fleiss' kappa:       {result['fleiss_kappa']:.4f}")
    print(f"  Effective K:         {result['effective_K']:.3f}")
    print(f"  Unanimous rate:      {result['unanimous_rate_pct']:.1f}%")
    print(f"  Mean max agreement:  {result['mean_max_agreement_pct']:.1f}%")
    print(f"  Category dist:       True={cat_dist['True']:.1f}%  False={cat_dist['False']:.1f}%  Unknown={cat_dist['Unknown']:.1f}%")
    
    return result

if __name__ == '__main__':
    base = '/root/symb_invariant_consensus/results'
    
    results = {}
    
    # exp-033
    exp033_dir = os.path.join(base, 'exp033_mistral_7b_folio204', 'intermediates')
    r033 = process_experiment(exp033_dir, 'exp-033 (Mistral-7B FOLIO-204, K=12)')
    if r033:
        results['exp033'] = r033
    
    # exp-046
    exp046_dir = os.path.join(base, 'exp046_mistral_7b_pw600', 'intermediates')
    if os.path.isdir(exp046_dir):
        r046 = process_experiment(exp046_dir, 'exp-046 (Mistral-7B PW-600, K=12)')
        if r046:
            results['exp046'] = r046
    
    # Save results
    out_path = os.path.join(base, 'fleiss_kappa_exp033.json')
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")
