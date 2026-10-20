#!/usr/bin/env python3
"""
Recompute theta-fixed lz (Drasgow 1985) for all 12 Qwen conditions using
the same computation that produced registry values.
theta_fixed = mean of 10 clean seeds' theta_MLE.
"""
import json, os, csv, math
import numpy as np

RESULTS_DIR = '/path/to/project/qwen/results'
PARAMS_FILE = '/path/to/project/qwen/mmlu_params.csv'

# --- Load 4PL IRT parameters (indexed by position, not item_idx) ---
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
print(f"Loaded {len(params)} item parameters")

# --- Same functions from theta_fixed_lzstar.py (registry source) ---

def compute_lz_drasgow(response_vector, params, theta):
    """Drasgow (1985) lz — no variance correction. This is the registry computation."""
    n = min(len(response_vector), len(params))
    l0, el0, var_l0 = 0.0, 0.0, 0.0
    for i in range(n):
        x = response_vector[i]
        p = params[i]
        a, b, c, d = p['a'], p['b'], p['c'], p['d']
        prob = c + (d - c) / (1.0 + math.exp(-a * (theta - b)))
        prob = max(min(prob, 1.0 - 1e-10), 1e-10)
        log_p = math.log(prob)
        log_q = math.log(1.0 - prob)
        l0 += x * log_p + (1 - x) * log_q
        el0 += prob * log_p + (1 - prob) * log_q
        var_l0 += prob * (1 - prob) * (log_p - log_q) ** 2
    if var_l0 <= 0:
        return float('nan')
    return (l0 - el0) / math.sqrt(var_l0)

# --- Load all 12 conditions ---
conditions = [f'clean_s{i}' for i in range(1, 11)] + ['contam_15', 'contam_50']
data = {}
for cond in conditions:
    fpath = os.path.join(RESULTS_DIR, f'{cond}_results.json')
    if os.path.exists(fpath):
        data[cond] = json.load(open(fpath))
        print(f"Loaded {cond}: theta_mle={data[cond]['theta_mle']:.6f}")
    else:
        print(f"WARNING: {fpath} not found!")

# --- theta_fixed = mean of 10 clean theta_MLEs ---
clean_thetas = {f'clean_s{i}': data[f'clean_s{i}']['theta_mle'] for i in range(1, 11)}
theta_fixed = np.mean(list(clean_thetas.values()))
print(f"\ntheta_fixed = mean of 10 clean seeds = {theta_fixed:.6f}")
for k, v in clean_thetas.items():
    print(f"  {k}: {v:.6f}")

# --- Step 1: Verify free-theta lz matches registry ---
print(f"\n{'='*70}")
print("VERIFICATION: free-theta lz (should match registry)")
print(f"{'='*70}")
for cond in conditions:
    rv = data[cond]['response_vector']
    theta_mle = data[cond]['theta_mle']
    lz_free = compute_lz_drasgow(rv, params, theta_mle)
    lz_uncorrected_field = data[cond].get('lz_uncorrected', None)
    match = ""
    if lz_uncorrected_field is not None:
        match = f" registry={lz_uncorrected_field:.4f} match={abs(lz_free - lz_uncorrected_field) < 1e-6}"
    print(f"  {cond:<12} lz_free={lz_free:.4f}{match}")

# --- Step 2: Compute theta-fixed lz for all 12 conditions ---
print(f"\n{'='*70}")
print(f"THETA-FIXED LZ (Drasgow 1985, theta_fixed={theta_fixed:.6f})")
print(f"{'='*70}")
print(f"{'Cond':<12} {'theta_MLE':>10} {'lz_free':>10} {'lz_fixed':>10}")

results = {'theta_fixed': theta_fixed, 'clean_thetas': clean_thetas, 'conditions': {}}
clean_lz_fixed = []
clean_lz_free = []

for cond in conditions:
    rv = data[cond]['response_vector']
    theta_mle = data[cond]['theta_mle']
    lz_free = compute_lz_drasgow(rv, params, theta_mle)
    lz_fixed = compute_lz_drasgow(rv, params, theta_fixed)

    results['conditions'][cond] = {
        'theta_mle': theta_mle,
        'lz_free': lz_free,
        'lz_fixed': lz_fixed,
        'accuracy': data[cond].get('accuracy_overall', None),
    }
    if cond.startswith('clean_'):
        clean_lz_fixed.append(lz_fixed)
        clean_lz_free.append(lz_free)

    print(f"  {cond:<12} {theta_mle:>10.4f} {lz_free:>10.4f} {lz_fixed:>10.4f}")

# --- Step 3: Cohen's d + Bootstrap CI ---
print(f"\n{'='*70}")
print("COHEN'S D + BOOTSTRAP CI")
print(f"{'='*70}")

clean_fixed_arr = np.array(clean_lz_fixed)
clean_free_arr = np.array(clean_lz_free)

def bootstrap_cohens_d(clean_values, contam_value, n_bootstrap=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(clean_values)
    ds = []
    for _ in range(n_bootstrap):
        sample = rng.choice(clean_values, size=n, replace=True)
        s = np.std(sample, ddof=1)
        if s < 1e-10:
            continue
        d = (np.mean(sample) - contam_value) / s
        ds.append(d)
    ds = np.array(ds)
    return np.mean(ds), np.percentile(ds, 2.5), np.percentile(ds, 97.5)

cohens_d_results = {}
for contam in ['contam_15', 'contam_50']:
    lz_fixed_contam = results['conditions'][contam]['lz_fixed']
    lz_free_contam = results['conditions'][contam]['lz_free']

    d_fixed, ci_lo_fixed, ci_hi_fixed = bootstrap_cohens_d(clean_fixed_arr, lz_fixed_contam)
    d_free, ci_lo_free, ci_hi_free = bootstrap_cohens_d(clean_free_arr, lz_free_contam)

    cohens_d_results[contam] = {
        'lz_fixed': {'d': d_fixed, 'ci_95': [ci_lo_fixed, ci_hi_fixed]},
        'lz_free': {'d': d_free, 'ci_95': [ci_lo_free, ci_hi_free]},
    }
    print(f"\n{contam}:")
    print(f"  lz_fixed: d={d_fixed:.4f}  95% CI=[{ci_lo_fixed:.4f}, {ci_hi_fixed:.4f}]")
    print(f"  lz_free:  d={d_free:.4f}  95% CI=[{ci_lo_free:.4f}, {ci_hi_free:.4f}]")

results['cohens_d'] = cohens_d_results
results['clean_summary'] = {
    'lz_fixed_mean': float(np.mean(clean_fixed_arr)),
    'lz_fixed_std': float(np.std(clean_fixed_arr, ddof=1)),
    'lz_free_mean': float(np.mean(clean_free_arr)),
    'lz_free_std': float(np.std(clean_free_arr, ddof=1)),
}

# --- Save ---
out_path = 'results/qwen_theta_fixed_consistent.json'
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2, default=lambda x: float(x) if isinstance(x, np.floating) else x)
print(f"\nSaved to {out_path}")

# Also save to results dir
out_path2 = os.path.join(RESULTS_DIR, 'theta_fixed_n10_consistent.json')
with open(out_path2, 'w') as f:
    json.dump(results, f, indent=2, default=lambda x: float(x) if isinstance(x, np.floating) else x)
print(f"Saved to {out_path2}")
