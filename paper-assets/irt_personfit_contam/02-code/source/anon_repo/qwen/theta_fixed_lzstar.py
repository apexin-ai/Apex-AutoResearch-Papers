#!/usr/bin/env python3
"""
theta_fixed lz* recomputation with Snijders (2001) correction.
Uses clean baseline theta (mean of n=3 clean seeds' theta_MLE).
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

def compute_lz_drasgow(response_vector, params, theta):
    """Drasgow (1985) lz — no variance correction."""
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

def compute_lz_star(response_vector, params, theta):
    """Snijders (2001) lz* with Var* = Var(l0) - C(theta)^2/I(theta) correction."""
    n = min(len(response_vector), len(params))
    l0, E_l0, Var_l0 = 0.0, 0.0, 0.0
    I_theta, C_theta = 0.0, 0.0
    for i in range(n):
        x = response_vector[i]
        p = params[i]
        a, b, c, d = p['a'], p['b'], p['c'], p['d']
        z = a * (theta - p['b'])
        sigma = 1.0 / (1.0 + math.exp(-max(min(z, 30), -30)))
        P = c + (d - c) * sigma
        P = max(min(P, 1.0 - 1e-10), 1e-10)
        Q = 1.0 - P
        log_P = math.log(P)
        log_Q = math.log(Q)

        l0 += x * log_P + (1 - x) * log_Q
        E_l0 += P * log_P + Q * log_Q
        g = log_P - log_Q
        Var_l0 += P * Q * g ** 2

        dP = a * (d - c) * sigma * (1.0 - sigma)
        h = dP / (P * Q)
        I_theta += P * Q * h ** 2
        C_theta += P * Q * h * g

    if Var_l0 < 1e-15:
        return 0.0
    Var_star = Var_l0 - C_theta ** 2 / I_theta if I_theta > 1e-15 else Var_l0
    if Var_star <= 0:
        Var_star = Var_l0
    return (l0 - E_l0) / math.sqrt(Var_star)

# Load all condition results (corrected Snijders lz* from eval_lz.py re-run)
conditions = ['clean_s1', 'clean_s2', 'clean_s3', 'contam_15', 'contam_50']
data = {}
for cond in conditions:
    fpath = os.path.join(RESULTS_DIR, f'{cond}_results.json')
    if os.path.exists(fpath):
        data[cond] = json.load(open(fpath))
        print(f"Loaded {cond}: theta_mle={data[cond].get('theta_mle'):.4f}, lz*={data[cond].get('lz_star'):.4f}")

# theta_fixed = mean of 3 clean theta_MLEs
clean_thetas = [data[f'clean_s{i}']['theta_mle'] for i in [1,2,3]]
theta_fixed = np.mean(clean_thetas)
print(f"\ntheta_fixed = mean({[f'{t:.4f}' for t in clean_thetas]}) = {theta_fixed:.4f}")

# Load old theta_fixed_n3.json for comparison
old_results = json.load(open(os.path.join(RESULTS_DIR, 'theta_fixed_n3.json')))
old_theta = old_results['theta_fixed']
print(f"Old theta_fixed = {old_theta} (should be identical: {abs(theta_fixed - old_theta) < 1e-6})")

# Recompute for all conditions
results = {'theta_fixed': round(theta_fixed, 6), 'conditions': {}, 'old_theta_fixed': old_theta}

print(f"\n{'='*60}")
print(f"{'Cond':<12} {'theta_free':>10} {'lz*_free(new)':>14} {'lz_fixed(old)':>14} {'lz*_fixed(new)':>15}")
print(f"{'='*60}")

for cond in conditions:
    rv = data[cond]['response_vector']
    theta_mle = data[cond]['theta_mle']
    lz_star_free = data[cond]['lz_star']  # corrected Snijders from eval_lz.py

    # Old values from theta_fixed_n3.json
    old_lz_free = old_results['conditions'][cond]['lz_free'] if cond in old_results['conditions'] else None
    old_lz_fixed = old_results['conditions'][cond]['lz_fixed'] if cond in old_results['conditions'] else None

    # Compute new lz*_fixed with Snijders correction
    lz_star_fixed = compute_lz_star(rv, params, theta_fixed)
    # Also compute old-style Drasgow for comparison
    lz_drasgow_fixed = compute_lz_drasgow(rv, params, theta_fixed)

    results['conditions'][cond] = {
        'theta_mle': theta_mle,
        'lz_star_free': lz_star_free,
        'lz_star_fixed': lz_star_fixed,
        'lz_drasgow_fixed_old': old_lz_fixed,
        'lz_drasgow_fixed_verify': lz_drasgow_fixed,
    }

    print(f"{cond:<12} {theta_mle:>10.4f} {lz_star_free:>14.4f} {old_lz_fixed:>14.4f} {lz_star_fixed:>15.4f}")

# Delta analysis
clean_conds = ['clean_s1', 'clean_s2', 'clean_s3']
baseline_lz_star_fixed = np.mean([results['conditions'][c]['lz_star_fixed'] for c in clean_conds])
baseline_lz_star_free = np.mean([results['conditions'][c]['lz_star_free'] for c in clean_conds])
old_baseline_fixed = np.mean([old_results['conditions'][c]['lz_fixed'] for c in clean_conds])

results['baseline'] = {
    'lz_star_free_mean': baseline_lz_star_free,
    'lz_star_fixed_mean': baseline_lz_star_fixed,
    'old_lz_fixed_mean': old_baseline_fixed
}

print(f"\n{'='*60}")
print(f"DELTA ANALYSIS (vs clean baseline)")
print(f"{'='*60}")
print(f"Clean baseline: lz*_fixed(new)={baseline_lz_star_fixed:.4f}, lz_fixed(old)={old_baseline_fixed:.4f}")

deltas = {}
for cond in conditions:
    r = results['conditions'][cond]
    d_fixed_new = r['lz_star_fixed'] - baseline_lz_star_fixed
    d_fixed_old = r['lz_drasgow_fixed_old'] - old_baseline_fixed
    d_free_new = r['lz_star_free'] - baseline_lz_star_free
    deltas[cond] = {
        'delta_lz_star_fixed_new': round(d_fixed_new, 4),
        'delta_lz_fixed_old': round(d_fixed_old, 4),
        'delta_lz_star_free_new': round(d_free_new, 4),
    }
    results['conditions'][cond]['delta_lz_star_fixed'] = round(d_fixed_new, 4)
    results['conditions'][cond]['delta_lz_fixed_old'] = round(d_fixed_old, 4)
    print(f"{cond:<12} Δlz*_fixed(new)={d_fixed_new:>8.4f}  Δlz_fixed(old)={d_fixed_old:>8.4f}")

# Dose-response ratio
d15_new = deltas['contam_15']['delta_lz_star_fixed_new']
d50_new = deltas['contam_50']['delta_lz_star_fixed_new']
d15_old = deltas['contam_15']['delta_lz_fixed_old']
d50_old = deltas['contam_50']['delta_lz_fixed_old']

ratio_new = d50_new / d15_new if d15_new != 0 else None
ratio_old = d50_old / d15_old if d15_old != 0 else None

results['dose_response'] = {
    'ratio_lz_star_fixed_new': round(ratio_new, 4) if ratio_new else None,
    'ratio_lz_fixed_old': round(ratio_old, 4) if ratio_old else None,
}

print(f"\n{'='*60}")
print(f"DOSE-RESPONSE RATIO (|Δcontam_50| / |Δcontam_15|)")
print(f"{'='*60}")
print(f"Old (Drasgow lz):     {ratio_old:.4f}")
print(f"New (Snijders lz*):   {ratio_new:.4f}")

# Save
out_path = os.path.join(RESULTS_DIR, 'theta_fixed_n3_lzstar.json')
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out_path}")
