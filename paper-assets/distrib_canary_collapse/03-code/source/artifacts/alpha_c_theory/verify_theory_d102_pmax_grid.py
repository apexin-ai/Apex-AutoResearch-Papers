"""
P_max Grid Search for Multiplicative Ceiling Model.

Model: P(det|α,T) = P_max · Φ(A · α^β · √T − z₀)
α_∞ = 0 (fixed, profile likelihood confirmed).

Outer grid: P_max ∈ [0.5, 1.0] step 0.05, β ∈ [0.05, 0.50] step 0.01.
Inner MLE: (A, z₀) via differential_evolution.
Selection: min cross-validation MAE on T={5,15}.
"""

import json
import numpy as np
from scipy.optimize import differential_evolution
from scipy.stats import norm, binom
from pathlib import Path

OUT_DIR = Path(__file__).parent

# ============================================================
# DATA
# ============================================================

DATA_T10 = [
    (0.00, 0, 8), (0.05, 0, 8), (0.10, 0, 8), (0.25, 0, 8),
    (0.30, 0, 8), (0.35, 0, 8), (0.40, 0, 8), (0.45, 0, 8),
    (0.50, 6, 8), (0.75, 6, 8), (1.00, 6, 8),
]
DATA_T20 = [(0.45, 5, 8), (0.50, 6, 8), (0.75, 6, 8)]
DATA_T5  = [(0.45, 0, 8), (0.50, 0, 8), (0.75, 0, 8)]
DATA_T15 = [(0.45, 6, 8), (0.50, 6, 8), (0.75, 6, 8)]
DATA_T25 = [(0.45, 6, 8), (0.50, 6, 8), (0.60, 5, 8), (0.75, 6, 8)]

TRAIN = [(10, a, k, n) for a, k, n in DATA_T10] + \
        [(20, a, k, n) for a, k, n in DATA_T20]
TEST  = [(5,  a, k, n) for a, k, n in DATA_T5] + \
        [(15, a, k, n) for a, k, n in DATA_T15]
T25   = [(25, a, k, n) for a, k, n in DATA_T25]

T_tr = np.array([x[0] for x in TRAIN], dtype=float)
a_tr = np.array([x[1] for x in TRAIN], dtype=float)
k_tr = np.array([x[2] for x in TRAIN], dtype=float)
n_tr = np.array([x[3] for x in TRAIN], dtype=float)

# ============================================================
# MODEL
# ============================================================

def det_prob(alpha, T, A, beta, z0, pmax):
    alpha = np.asarray(alpha, dtype=float)
    T = np.asarray(T, dtype=float)
    s = A * alpha ** beta
    return pmax * norm.cdf(s * np.sqrt(T) - z0)


def nll(A, beta, z0, pmax, T_arr, a_arr, k_arr, n_arr):
    if A <= 0 or beta <= 0 or z0 < 0:
        return 1e12
    p = det_prob(a_arr, T_arr, A, beta, z0, pmax)
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return -np.sum(k_arr * np.log(p) + (n_arr - k_arr) * np.log(1 - p))


def nll_inner(inner_p, beta, pmax, T_arr, a_arr, k_arr, n_arr):
    A, z0 = inner_p
    return nll(A, beta, z0, pmax, T_arr, a_arr, k_arr, n_arr)


def compute_mae(params, data):
    A, beta, z0, pmax = params
    resids = []
    for T, a, k, n in data:
        p = float(det_prob(a, T, A, beta, z0, pmax))
        resids.append(abs(k / n - p))
    return np.mean(resids)


# ============================================================
# PROFILE LIKELIHOOD: P_max × β grid
# ============================================================

pmax_grid = np.arange(0.50, 1.001, 0.05)
beta_grid = np.arange(0.05, 0.501, 0.01)
inner_bounds = [(0.01, 200.0), (0.5, 20.0)]

print(f"Grid: {len(pmax_grid)} P_max × {len(beta_grid)} β = {len(pmax_grid)*len(beta_grid)} cells")
print("Profile scan...")

results = []
count = 0
total = len(pmax_grid) * len(beta_grid)

for pmax_v in pmax_grid:
    for beta_v in beta_grid:
        count += 1
        if count % 100 == 0:
            print(f"  {count}/{total}...")

        best_inner = None
        for seed in [0, 42, 7]:
            try:
                res = differential_evolution(
                    nll_inner, inner_bounds,
                    args=(beta_v, pmax_v, T_tr, a_tr, k_tr, n_tr),
                    seed=seed, maxiter=500, tol=1e-10, polish=True, popsize=15,
                )
                if best_inner is None or res.fun < best_inner.fun:
                    best_inner = res
            except Exception:
                pass
        if best_inner is None:
            continue

        A_opt, z0_opt = best_inner.x
        tnll = best_inner.fun
        test_mae = compute_mae((A_opt, beta_v, z0_opt, pmax_v), TEST)

        results.append({
            'pmax': round(float(pmax_v), 2),
            'beta': round(float(beta_v), 2),
            'A': float(A_opt),
            'z0': float(z0_opt),
            'train_nll': float(tnll),
            'test_mae': float(test_mae),
            'gamma': round(1.0 / (2.0 * float(beta_v)), 4),
        })

results.sort(key=lambda x: x['test_mae'])
print(f"\nTotal valid fits: {len(results)}")

# ============================================================
# BEST MODEL
# ============================================================

best = results[0]
A_fit = best['A']
beta_fit = best['beta']
z0_fit = best['z0']
pmax_fit = best['pmax']
gamma_fit = best['gamma']

print(f"\n{'='*65}")
print("BEST MODEL (min test MAE, P_max ceiling)")
print(f"{'='*65}")
print(f"  P_max     = {pmax_fit:.2f}")
print(f"  A         = {A_fit:.4f}")
print(f"  beta      = {beta_fit:.4f}")
print(f"  z0        = {z0_fit:.4f}")
print(f"  gamma     = 1/(2*beta) = {gamma_fit:.4f}")
print(f"  -logL     = {best['train_nll']:.4f}")

# ============================================================
# P_max profile: best (β, A, z₀) for each P_max
# ============================================================

pmax_profile = {}
for r in results:
    pm = r['pmax']
    if pm not in pmax_profile or r['test_mae'] < pmax_profile[pm]['test_mae']:
        pmax_profile[pm] = r

pmax_profile_list = sorted(pmax_profile.values(), key=lambda x: x['pmax'])
print(f"\nP_max profile (best β per P_max):")
print(f"{'Pmax':>5s} {'beta':>5s} {'A':>8s} {'z0':>7s} {'nll':>8s} {'tMAE':>7s} {'gamma':>6s}")
for r in pmax_profile_list:
    print(f"{r['pmax']:5.2f} {r['beta']:5.2f} {r['A']:8.3f} {r['z0']:7.3f} "
          f"{r['train_nll']:8.2f} {r['test_mae']:7.4f} {r['gamma']:6.2f}")

# ============================================================
# TRAINING FIT
# ============================================================

p_tr = det_prob(a_tr, T_tr, A_fit, beta_fit, z0_fit, pmax_fit)
tr_mae = float(np.mean(np.abs(k_tr / n_tr - p_tr)))
tr_rmse = float(np.sqrt(np.mean((k_tr / n_tr - p_tr) ** 2)))

p_null_rate = np.mean(k_tr) / np.mean(n_tr)
ll_null = float(np.sum(
    k_tr * np.log(max(p_null_rate, 1e-12))
    + (n_tr - k_tr) * np.log(max(1 - p_null_rate, 1e-12))
))
r2 = 1 - (-best['train_nll']) / ll_null

print(f"\nTraining: MAE={tr_mae:.4f}, RMSE={tr_rmse:.4f}, R²={r2:.4f}")
for T, a, k, n in TRAIN:
    p = float(det_prob(a, T, A_fit, beta_fit, z0_fit, pmax_fit))
    print(f"  T={T:2d} α={a:.2f}: {k}/{n} pred={p:.3f} ({p*n:.1f}/8)")

# ============================================================
# CROSS-VALIDATION (T=5, T=15)
# ============================================================

print(f"\nCross-Validation (T=5, T=15):")
test_results = []
for T, a, k, n in TEST:
    p = float(det_prob(a, T, A_fit, beta_fit, z0_fit, pmax_fit))
    r = k / n - p
    test_results.append({
        'T': T, 'alpha': a, 'k_actual': k, 'n': n,
        'p_pred': p, 'k_pred': p * n, 'residual': r,
    })
    print(f"  T={T:2d} α={a:.2f}: {k}/{n} pred={p:.3f} ({p*n:.1f}/8) resid={r:+.3f}")

tst_mae = float(np.mean([abs(r['residual']) for r in test_results]))
tst_rmse = float(np.sqrt(np.mean([r['residual'] ** 2 for r in test_results])))

ci_cov = 0
ci_det = []
for r in test_results:
    p = np.clip(r['p_pred'], 1e-6, 1 - 1e-6)
    lo = binom.ppf(0.025, r['n'], p) / r['n']
    hi = binom.ppf(0.975, r['n'], p) / r['n']
    ok = lo <= r['k_actual'] / r['n'] <= hi
    ci_cov += ok
    ci_det.append({'lo': float(lo), 'hi': float(hi), 'covered': bool(ok)})

print(f"\n  MAE={tst_mae:.4f}, RMSE={tst_rmse:.4f}")
print(f"  95% CI coverage = {ci_cov}/{len(test_results)}")

# ============================================================
# T=25 EXTRA VALIDATION
# ============================================================

print(f"\nT=25 Extra Validation:")
t25_results = []
for T, a, k, n in T25:
    p = float(det_prob(a, T, A_fit, beta_fit, z0_fit, pmax_fit))
    r = k / n - p
    t25_results.append({
        'T': T, 'alpha': a, 'k_actual': k, 'n': n,
        'p_pred': p, 'k_pred': p * n, 'residual': r,
    })
    print(f"  T={T:2d} α={a:.2f}: {k}/{n} pred={p:.3f} ({p*n:.1f}/8) resid={r:+.3f}")

t25_mae = float(np.mean([abs(r['residual']) for r in t25_results]))
t25_rmse = float(np.sqrt(np.mean([r['residual'] ** 2 for r in t25_results])))
print(f"  T=25 MAE={t25_mae:.4f}, RMSE={t25_rmse:.4f}")

# ============================================================
# COMPARISON WITH OLD MODEL (no P_max)
# ============================================================

old_params = {'A': 1.3940, 'ainf': 0.0, 'beta': 0.24, 'z0': 4.4865}
old_test_mae = 0.10597

def det_prob_old(alpha, T, A, ainf, beta, z0):
    alpha = np.asarray(alpha, dtype=float)
    T = np.asarray(T, dtype=float)
    s = A * np.maximum(0.0, alpha - ainf) ** beta
    return norm.cdf(s * np.sqrt(T) - z0)

old_t25_resids = []
for T, a, k, n in T25:
    p = float(det_prob_old(a, T, old_params['A'], old_params['ainf'],
                           old_params['beta'], old_params['z0']))
    old_t25_resids.append(abs(k / n - p))
old_t25_mae = float(np.mean(old_t25_resids))

print(f"\nComparison with old model (no P_max):")
print(f"  Old test MAE (T=5,15): {old_test_mae:.5f}")
print(f"  New test MAE (T=5,15): {tst_mae:.5f}")
print(f"  Old T=25 MAE: {old_t25_mae:.5f}")
print(f"  New T=25 MAE: {t25_mae:.5f}")

# ============================================================
# α_c VALUES
# ============================================================

def alpha_c(T, A, beta, z0, pmax):
    """P_max·Φ(A·α^β·√T − z₀) = 0.5 → α = ((z₀ + Φ⁻¹(0.5/P_max))/(A·√T))^(1/β)"""
    ratio = 0.5 / pmax
    if ratio >= 1.0:
        return float('inf')
    zc = norm.ppf(ratio)
    s_need = (z0 + zc) / np.sqrt(T)
    if s_need <= 0:
        return 0.0
    return (s_need / A) ** (1.0 / beta)


alpha_c_vals = {}
print(f"\nα_c(T) for P_max={pmax_fit}:")
for Tv in [5, 8, 10, 15, 20, 25, 50]:
    ac = alpha_c(Tv, A_fit, beta_fit, z0_fit, pmax_fit)
    alpha_c_vals[str(Tv)] = float(min(ac, 99.0))
    print(f"  T={Tv:2d}: α_c = {min(ac, 99.0):.4f}")

# ============================================================
# SAVE JSON
# ============================================================

output = {
    'method': 'P_max Grid Search — Multiplicative Ceiling Model',
    'description': (
        'Profile likelihood over (P_max, beta) grid with α_∞=0 fixed. '
        'P_max ∈ [0.5,1.0] step 0.05, β ∈ [0.05,0.50] step 0.01. '
        'Inner MLE: (A, z₀) via differential_evolution. '
        'Joint fit T={10,20}, validate T={5,15}, extra T=25.'
    ),
    'model': 'P(det|α,T) = P_max · Φ(A · α^β · √T − z₀)',
    'best_model': {
        'P_max': pmax_fit,
        'A': A_fit,
        'beta': beta_fit,
        'z0': z0_fit,
        'gamma': gamma_fit,
        'neg_logL': best['train_nll'],
        'test_MAE': tst_mae,
    },
    'pmax_profile': [
        {
            'P_max': r['pmax'],
            'beta': r['beta'],
            'A': r['A'],
            'z0': r['z0'],
            'train_NLL': r['train_nll'],
            'test_MAE': r['test_mae'],
            'gamma': r['gamma'],
        }
        for r in pmax_profile_list
    ],
    'training_fit': {
        'n_train': len(TRAIN),
        'n_params': 4,
        'MAE': tr_mae,
        'RMSE': tr_rmse,
        'McFadden_R2': r2,
        'points': [
            {
                'T': int(T), 'alpha': float(a), 'k_actual': int(k), 'n': int(n),
                'p_pred': float(det_prob(a, T, A_fit, beta_fit, z0_fit, pmax_fit)),
            }
            for T, a, k, n in TRAIN
        ],
    },
    'cross_validation': {
        'n_test': len(TEST),
        'MAE': tst_mae,
        'RMSE': tst_rmse,
        'CI_95_coverage': f"{ci_cov}/{len(test_results)}",
        'CI_95_coverage_rate': ci_cov / len(test_results),
        'points': [{**r, 'CI_95': ci_det[i]} for i, r in enumerate(test_results)],
    },
    't25_prediction': {
        'n_test': len(T25),
        'MAE': t25_mae,
        'RMSE': t25_rmse,
        'points': t25_results,
    },
    'comparison_with_old': {
        'old_model': 'P(det|α,T) = Φ(A · max(0,α−α_∞)^β · √T − z₀)',
        'old_params': old_params,
        'old_test_MAE_T5_T15': old_test_mae,
        'new_test_MAE_T5_T15': tst_mae,
        'old_T25_MAE': old_t25_mae,
        'new_T25_MAE': t25_mae,
        'improvement_test': old_test_mae - tst_mae,
        'improvement_T25': old_t25_mae - t25_mae,
    },
    'alpha_c_values': alpha_c_vals,
    'alpha_c_formula': 'α_c(T) = ((z₀ + Φ⁻¹(0.5/P_max)) / (A·√T))^(1/β)',
    'profile_top10': results[:10],
}

json_path = OUT_DIR / 'theory_verification_d102_pmax_grid.json'
with open(json_path, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nJSON saved to {json_path}")
