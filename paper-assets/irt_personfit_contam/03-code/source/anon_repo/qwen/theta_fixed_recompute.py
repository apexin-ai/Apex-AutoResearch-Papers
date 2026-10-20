#!/usr/bin/env python3
"""
theta-fixed lz* recomputation.
Uses clean baseline theta (mean of clean_s1, clean_s2 theta_MLE) to recompute
lz* for all 4 conditions, isolating theta-shift contribution to signal.
"""
import json, os, csv, math
import numpy as np

RESULTS_DIR = '/path/to/project/qwen/results'
PARAMS_FILE = '/path/to/project/qwen/mmlu_params.csv'

# Load PSN-IRT 4PL parameters
params = []
with open(PARAMS_FILE) as f:
    reader = csv.DictReader(f)
    for row in reader:
        params.append({
            'a': float(row['a_discrimination']),
            'b': float(row['b_difficulty']),
            'c': float(row['c_guessing']),
            'd': float(row['d_feasibility'])
        })
n_items_params = len(params)
print(f"Loaded {n_items_params} item parameters")

def compute_lz_star(response_vector, params, theta):
    """Compute lz* statistic for given theta (fixed, not MLE)."""
    n = min(len(response_vector), len(params))
    l0 = 0.0
    el0 = 0.0
    var_l0 = 0.0
    
    for i in range(n):
        x = response_vector[i]
        p = params[i]
        a, b, c, d = p['a'], p['b'], p['c'], p['d']
        
        # 4PL ICC
        prob = c + (d - c) / (1.0 + math.exp(-a * (theta - b)))
        prob = max(min(prob, 1.0 - 1e-10), 1e-10)
        
        log_p = math.log(prob)
        log_q = math.log(1.0 - prob)
        
        l0 += x * log_p + (1 - x) * log_q
        el0 += prob * log_p + (1 - prob) * log_q
        var_l0 += prob * (1 - prob) * (log_p - log_q) ** 2
    
    if var_l0 <= 0:
        return float('nan')
    
    lz_star = (l0 - el0) / math.sqrt(var_l0)
    return lz_star

# Load all condition results
conditions = ['clean_s1', 'clean_s2', 'contam_15', 'contam_50']
data = {}
for cond in conditions:
    fpath = os.path.join(RESULTS_DIR, f'{cond}_results.json')
    if os.path.exists(fpath):
        data[cond] = json.load(open(fpath))
        print(f"Loaded {cond}: theta_mle={data[cond].get('theta_mle')}, lz_star={data[cond].get('lz_star')}")
    else:
        print(f"WARNING: {fpath} not found!")

# Compute theta_fixed = mean of clean thetas
theta_clean_s1 = data['clean_s1']['theta_mle']
theta_clean_s2 = data['clean_s2']['theta_mle']
theta_fixed = (theta_clean_s1 + theta_clean_s2) / 2.0
print(f"\ntheta_fixed = mean({theta_clean_s1}, {theta_clean_s2}) = {theta_fixed}")

# Recompute lz* for all conditions with theta_fixed
results = {}
for cond in conditions:
    if cond not in data or 'response_vector' not in data[cond]:
        print(f"Skipping {cond}: no response_vector")
        continue
    
    rv = data[cond]['response_vector']
    theta_mle = data[cond]['theta_mle']
    lz_free = data[cond]['lz_star']
    
    lz_fixed = compute_lz_star(rv, params, theta_fixed)
    lz_verify = compute_lz_star(rv, params, theta_mle)
    
    results[cond] = {
        'theta_mle': theta_mle,
        'theta_fixed': theta_fixed,
        'lz_star_free': lz_free,
        'lz_star_fixed': lz_fixed,
        'lz_star_verify': lz_verify,
        'accuracy': data[cond].get('accuracy_overall', None)
    }
    
    print(f"\n{cond}:")
    print(f"  theta_MLE={theta_mle:.4f}, theta_fixed={theta_fixed:.4f}")
    print(f"  lz*_free={lz_free:.4f}, lz*_fixed={lz_fixed:.4f}")
    print(f"  lz*_verify={lz_verify:.4f}")
    print(f"  Delta(fixed-free)={lz_fixed - lz_free:.4f}")

# Compute delta lz* relative to clean baseline
clean_lz_free = (results['clean_s1']['lz_star_free'] + results['clean_s2']['lz_star_free']) / 2
clean_lz_fixed = (results['clean_s1']['lz_star_fixed'] + results['clean_s2']['lz_star_fixed']) / 2

print(f"\n=== DELTA LZ* ANALYSIS ===")
print(f"Clean baseline lz*_free: {clean_lz_free:.4f}")
print(f"Clean baseline lz*_fixed: {clean_lz_fixed:.4f}")

summary = {
    'theta_fixed': theta_fixed,
    'conditions': results,
    'delta_analysis': {}
}

for cond in conditions:
    if cond in results:
        delta_free = results[cond]['lz_star_free'] - clean_lz_free
        delta_fixed = results[cond]['lz_star_fixed'] - clean_lz_fixed
        theta_shift = results[cond]['theta_mle'] - theta_fixed
        
        summary['delta_analysis'][cond] = {
            'delta_lz_free': round(delta_free, 4),
            'delta_lz_fixed': round(delta_fixed, 4),
            'theta_shift': round(theta_shift, 4),
            'signal_absorbed_by_theta': round(delta_fixed - delta_free, 4)
        }
        
        print(f"\n{cond}:")
        print(f"  delta_lz*_free={delta_free:.4f}, delta_lz*_fixed={delta_fixed:.4f}")
        print(f"  theta-shift={theta_shift:.4f}")
        print(f"  Signal absorbed by theta-shift: {delta_fixed - delta_free:.4f}")

# Check dose-response monotonicity
if 'contam_15' in summary['delta_analysis'] and 'contam_50' in summary['delta_analysis']:
    d15_free = summary['delta_analysis']['contam_15']['delta_lz_free']
    d50_free = summary['delta_analysis']['contam_50']['delta_lz_free']
    d15_fixed = summary['delta_analysis']['contam_15']['delta_lz_fixed']
    d50_fixed = summary['delta_analysis']['contam_50']['delta_lz_fixed']
    
    summary['dose_response'] = {
        'free_monotonic': abs(d50_free) > abs(d15_free),
        'fixed_monotonic': abs(d50_fixed) > abs(d15_fixed),
        'free_ratio': round(d50_free / d15_free, 4) if d15_free != 0 else None,
        'fixed_ratio': round(d50_fixed / d15_fixed, 4) if d15_fixed != 0 else None
    }
    
    print(f"\n=== DOSE-RESPONSE ===")
    print(f"Free:  |delta_lz*_50|={abs(d50_free):.4f} vs |delta_lz*_15|={abs(d15_free):.4f} -> monotonic={abs(d50_free) > abs(d15_free)}")
    print(f"Fixed: |delta_lz*_50|={abs(d50_fixed):.4f} vs |delta_lz*_15|={abs(d15_fixed):.4f} -> monotonic={abs(d50_fixed) > abs(d15_fixed)}")

# Save results
output_path = os.path.join(RESULTS_DIR, 'theta_fixed_analysis.json')
with open(output_path, 'w') as f:
    json.dump(summary, f, indent=2)
print(f"\nSaved to {output_path}")
