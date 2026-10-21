"""
P_max Multiplicative Model for Distributional Canary Theory.

Model: P(det | alpha, T) = P_max * Phi(A * alpha^beta * sqrt(T) - z0)
  P_max = 0.75 (fixed, 6/8 MAUVE ceiling)
  alpha_inf = 0 (fixed, from profile likelihood)

Two analyses:
  (1) Fix beta=0.24 from old model, fit (A, z0) → isolate P_max effect
  (2) Profile over beta → show beta unidentifiability under P_max

Train: T={10,20}, Validate: T={5,15}, Extra: T=25.
"""

import json
import numpy as np
from scipy.optimize import differential_evolution, minimize
from scipy.stats import norm, binom
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).parent

P_MAX = 0.75

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
EXTRA = [(25, a, k, n) for a, k, n in DATA_T25]

# ============================================================
# MODELS
# ============================================================

def det_prob_pmax(alpha, T, A, beta, z0):
    alpha = np.asarray(alpha, dtype=float)
    T = np.asarray(T, dtype=float)
    s = A * np.power(np.maximum(alpha, 1e-30), beta)
    return P_MAX * norm.cdf(s * np.sqrt(T) - z0)


def det_prob_old(alpha, T, A, ainf, beta, z0):
    alpha = np.asarray(alpha, dtype=float)
    T = np.asarray(T, dtype=float)
    s = A * np.maximum(0.0, alpha - ainf) ** beta
    return norm.cdf(s * np.sqrt(T) - z0)


def nll_func(A, beta, z0, T_arr, a_arr, k_arr, n_arr):
    if A <= 0 or beta <= 0 or z0 < 0:
        return 1e12
    p = det_prob_pmax(a_arr, T_arr, A, beta, z0)
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return -np.sum(k_arr * np.log(p) + (n_arr - k_arr) * np.log(1 - p))


def nll_inner(inner_p, beta, T_arr, a_arr, k_arr, n_arr):
    A, z0 = inner_p
    return nll_func(A, beta, z0, T_arr, a_arr, k_arr, n_arr)


# ============================================================
# DATA ARRAYS
# ============================================================

T_tr  = np.array([x[0] for x in TRAIN], dtype=float)
a_tr  = np.array([x[1] for x in TRAIN], dtype=float)
k_tr  = np.array([x[2] for x in TRAIN], dtype=float)
n_tr  = np.array([x[3] for x in TRAIN], dtype=float)

T_te  = np.array([x[0] for x in TEST], dtype=float)
a_te  = np.array([x[1] for x in TEST], dtype=float)
k_te  = np.array([x[2] for x in TEST], dtype=float)
n_te  = np.array([x[3] for x in TEST], dtype=float)

ALL_DATA = TRAIN + TEST
T_all = np.array([x[0] for x in ALL_DATA], dtype=float)
a_all = np.array([x[1] for x in ALL_DATA], dtype=float)
k_all = np.array([x[2] for x in ALL_DATA], dtype=float)
n_all = np.array([x[3] for x in ALL_DATA], dtype=float)

# ============================================================
# OLD MODEL (reference)
# ============================================================

OLD = {
    'A': 1.3939686104887257, 'alpha_inf': 0.0,
    'beta': 0.24, 'z0': 4.486524832759895,
    'train_nll': 44.40394467503519,
}

# ============================================================
# ANALYSIS 1: Fix beta=0.24, fit (A, z0) with P_max
# ============================================================

print("=" * 65)
print("ANALYSIS 1: P_max model with beta=0.24 fixed (from old model)")
print("=" * 65)

BETA_FIXED = 0.24
inner_bounds = [(0.01, 10000.0), (0.01, 5000.0)]

best_fixed = None
for seed in [0, 42, 7, 99, 13, 55]:
    try:
        res = differential_evolution(
            nll_inner, inner_bounds,
            args=(BETA_FIXED, T_tr, a_tr, k_tr, n_tr),
            seed=seed, maxiter=2000, tol=1e-14, polish=True, popsize=30,
        )
        if best_fixed is None or res.fun < best_fixed.fun:
            best_fixed = res
    except:
        pass

A1, z01 = best_fixed.x
nll1 = best_fixed.fun
ratio1 = z01 / A1
gamma1 = 1.0 / (2 * BETA_FIXED)

print(f"\n  P_max     = {P_MAX}")
print(f"  beta      = {BETA_FIXED} (fixed)")
print(f"  z0/A      = {ratio1:.4f} (well-determined; A and z0 individually diverge)")
print(f"  A         = {A1:.1f} (quasi-complete separation)")
print(f"  z0        = {z01:.1f}")
print(f"  gamma     = {gamma1:.4f}")
print(f"  -logL     = {nll1:.4f}")

p_tr1 = det_prob_pmax(a_tr, T_tr, A1, BETA_FIXED, z01)
tr_mae1 = float(np.mean(np.abs(k_tr/n_tr - p_tr1)))

print(f"\n  Training predictions:")
for T, a, k, n in TRAIN:
    p = float(det_prob_pmax(a, T, A1, BETA_FIXED, z01))
    print(f"    T={T:2d} a={a:.2f}: {k}/{n} pred={p:.3f} ({p*n:.1f}/8)")

print(f"\n  Cross-validation (T=5, T=15):")
test_results1 = []
for T, a, k, n in TEST:
    p = float(det_prob_pmax(a, T, A1, BETA_FIXED, z01))
    r = k/n - p
    test_results1.append({'T': T, 'alpha': a, 'k_actual': k, 'n': n,
                          'p_pred': p, 'k_pred': p*n, 'residual': r})
    print(f"    T={T:2d} a={a:.2f}: {k}/{n} pred={p:.3f} ({p*n:.1f}/8) resid={r:+.3f}")

tst_mae1 = float(np.mean([abs(r['residual']) for r in test_results1]))
ci_cov1 = 0
ci_det1 = []
for r in test_results1:
    pc = np.clip(r['p_pred'], 1e-6, 1-1e-6)
    lo = binom.ppf(0.025, r['n'], pc) / r['n']
    hi = binom.ppf(0.975, r['n'], pc) / r['n']
    ok = lo <= r['k_actual']/r['n'] <= hi
    ci_cov1 += ok
    ci_det1.append({'lo': float(lo), 'hi': float(hi), 'covered': bool(ok)})
print(f"    MAE={tst_mae1:.4f}, CI coverage={ci_cov1}/{len(test_results1)}")

print(f"\n  Extra validation (T=25):")
extra_results1 = []
for T, a, k, n in EXTRA:
    p = float(det_prob_pmax(a, T, A1, BETA_FIXED, z01))
    r = k/n - p
    extra_results1.append({'T': T, 'alpha': a, 'k_actual': k, 'n': n,
                           'p_pred': p, 'k_pred': p*n, 'residual': r})
    print(f"    T={T:2d} a={a:.2f}: {k}/{n} pred={p:.3f} ({p*n:.1f}/8) resid={r:+.3f}")
extra_mae1 = float(np.mean([abs(r['residual']) for r in extra_results1]))

# alpha_c for P_max model
def alpha_c_pmax(T, A, beta, z0):
    s_need = z0 / np.sqrt(T)
    if s_need <= 0:
        return 0.0
    return (s_need / A) ** (1.0 / beta)

C1 = (z01 / A1) ** (1.0 / BETA_FIXED)
print(f"\n  alpha_c(T) = {C1:.2f} * T^(-{gamma1:.3f})")
for Tv in [5, 8, 10, 15, 20, 25, 50]:
    ac = alpha_c_pmax(Tv, A1, BETA_FIXED, z01)
    print(f"    T={Tv:2d}: {min(ac, 99.9):.4f}")

# ============================================================
# ANALYSIS 2: Profile likelihood over beta
# ============================================================

print(f"\n{'=' * 65}")
print("ANALYSIS 2: Profile likelihood over beta")
print("=" * 65)

beta_grid = np.concatenate([
    np.arange(0.05, 0.30, 0.01),
    np.arange(0.30, 0.60, 0.05),
    np.arange(0.60, 3.01, 0.10),
    np.arange(3.0, 6.01, 0.50),
])

profile_results = []
for beta_v in beta_grid:
    best_inner = None
    for seed in [0, 42, 7, 99]:
        try:
            res = differential_evolution(
                nll_inner, [(0.01, 10000.0), (0.01, 5000.0)],
                args=(beta_v, T_tr, a_tr, k_tr, n_tr),
                seed=seed, maxiter=1000, tol=1e-12, polish=True, popsize=25,
            )
            if best_inner is None or res.fun < best_inner.fun:
                best_inner = res
        except:
            pass
    if best_inner is None:
        continue

    A_opt, z0_opt = best_inner.x
    tnll = best_inner.fun

    # Test NLL
    p_te = det_prob_pmax(a_te, T_te, A_opt, beta_v, z0_opt)
    p_te_c = np.clip(p_te, 1e-12, 1-1e-12)
    test_nll = float(-np.sum(k_te * np.log(p_te_c) + (n_te - k_te) * np.log(1 - p_te_c)))

    # Test MAE
    test_mae = float(np.mean(np.abs(k_te/n_te - p_te)))

    profile_results.append({
        'beta': float(beta_v), 'A': float(A_opt), 'z0': float(z0_opt),
        'train_nll': float(tnll), 'test_nll': test_nll,
        'total_nll': float(tnll) + test_nll,
        'test_mae': test_mae,
        'gamma': 1.0 / (2 * float(beta_v)),
    })

# Show profile
profile_results.sort(key=lambda x: x['total_nll'])
print(f"\nTop 15 by total NLL (train+test):")
print(f"{'beta':>5s} {'A':>8s} {'z0':>8s} {'trNLL':>8s} {'teNLL':>8s} {'total':>8s} {'gamma':>6s}")
for r in profile_results[:15]:
    print(f"{r['beta']:5.2f} {r['A']:8.2f} {r['z0']:8.2f} "
          f"{r['train_nll']:8.2f} {r['test_nll']:8.2f} {r['total_nll']:8.2f} {r['gamma']:6.2f}")

# Show NLL flatness
nll_min = min(r['total_nll'] for r in profile_results)
within_2 = [r for r in profile_results if r['total_nll'] < nll_min + 2.0]
beta_range = (min(r['beta'] for r in within_2), max(r['beta'] for r in within_2))
print(f"\n  Beta range within delta-NLL < 2: [{beta_range[0]:.2f}, {beta_range[1]:.2f}]")
print(f"  Corresponding gamma range: [{1/(2*beta_range[1]):.2f}, {1/(2*beta_range[0]):.2f}]")
print(f"  -> beta is poorly identified; NLL plateau spans wide range")

# ============================================================
# COMPARISON: OLD vs P_MAX MODEL
# ============================================================

print(f"\n{'=' * 65}")
print("MODEL COMPARISON: Old vs P_max (both at beta=0.24)")
print("=" * 65)

comp_data = {
    'train': TRAIN, 'test': TEST, 'extra_T25': EXTRA,
}
comp = {}
for name, data in comp_data.items():
    old_res = []; new_res = []
    for T, a, k, n in data:
        p_old = float(det_prob_old(a, T, OLD['A'], OLD['alpha_inf'], OLD['beta'], OLD['z0']))
        p_new = float(det_prob_pmax(a, T, A1, BETA_FIXED, z01))
        old_res.append(abs(k/n - p_old))
        new_res.append(abs(k/n - p_new))
    comp[name] = {'old_mae': float(np.mean(old_res)), 'new_mae': float(np.mean(new_res))}
    print(f"\n  {name}: Old MAE={comp[name]['old_mae']:.4f} → New MAE={comp[name]['new_mae']:.4f} "
          f"(delta={comp[name]['new_mae'] - comp[name]['old_mae']:+.4f})")

print(f"\n  High-alpha detail (alpha >= 0.50):")
print(f"  {'T':>3s} {'a':>5s} {'k/n':>5s} {'old':>7s} {'new':>7s} {'|old|':>7s} {'|new|':>7s}")
all_pts = TRAIN + TEST + EXTRA
for T, a, k, n in sorted(all_pts, key=lambda x: (x[1], x[0])):
    if a < 0.50:
        continue
    p_old = float(det_prob_old(a, T, OLD['A'], OLD['alpha_inf'], OLD['beta'], OLD['z0']))
    p_new = float(det_prob_pmax(a, T, A1, BETA_FIXED, z01))
    actual = k/n
    print(f"  {T:3d} {a:5.2f} {actual:5.2f} {p_old:7.3f} {p_new:7.3f} "
          f"{abs(actual-p_old):7.3f} {abs(actual-p_new):7.3f}")

# ============================================================
# SAVE JSON
# ============================================================

# McFadden R² for train
p_null = np.mean(k_tr) / np.mean(n_tr)
ll_null = np.sum(k_tr*np.log(max(p_null,1e-12)) + (n_tr-k_tr)*np.log(max(1-p_null,1e-12)))
r2_1 = 1 - (-nll1) / ll_null

output = {
    'method': 'P_max Multiplicative Model (D102)',
    'description': (
        'P_max ceiling model with beta fixed from old model. '
        'P(det) = P_max * Phi(A*alpha^beta*sqrt(T) - z0). '
        'P_max=0.75 (6/8 MAUVE ceiling), alpha_inf=0, beta=0.24 (from D102 old model). '
        'Only A and z0 are fitted. Profile over beta shows beta is unidentifiable '
        'under P_max (NLL plateau from beta~0.24 to beta~3.0+).'
    ),
    'model': 'P(det|alpha,T) = P_max * Phi(A * alpha^beta * sqrt(T) - z0)',
    'P_max': P_MAX,
    'P_max_source': '6/8 PermG ceiling (2/8 pairs systematically fail, MAUVE bottleneck)',
    'fixed_params': {
        'P_max': P_MAX,
        'alpha_inf': 0.0,
        'beta': BETA_FIXED,
        'beta_source': 'D102 old model (profile likelihood best)',
    },
    'fitted_params': {
        'z0_over_A': float(ratio1),
        'A': float(A1), 'z0': float(z01),
        'n_free_params': 2,
        'neg_logL': float(nll1),
        'separation_note': (
            'T=10 data has quasi-complete separation (0/8 for alpha<=0.45, 6/8 for alpha>=0.50). '
            'A and z0 individually diverge to infinity but their ratio z0/A=%.4f converges. '
            'alpha_c(T) depends only on this ratio.' % ratio1
        ),
    },
    'derived': {
        'gamma': gamma1,
        'gamma_formula': '1/(2*beta)',
        'C_coefficient': float(C1),
        'scaling': f'alpha_c(T) = {C1:.2f} * T^(-{gamma1:.3f})',
        'alpha_c_values': {
            str(Tv): float(min(alpha_c_pmax(Tv, A1, BETA_FIXED, z01), 99))
            for Tv in [5, 8, 10, 15, 20, 25, 50]
        },
    },
    'training_fit': {
        'n_train': len(TRAIN), 'n_params': 2,
        'MAE': tr_mae1, 'McFadden_R2': float(r2_1),
        'points': [
            {'T': int(T), 'alpha': float(a), 'k_actual': int(k), 'n': int(n),
             'p_pred': float(det_prob_pmax(a, T, A1, BETA_FIXED, z01))}
            for T, a, k, n in TRAIN
        ],
    },
    'cross_validation': {
        'n_test': len(TEST), 'MAE': tst_mae1,
        'CI_95_coverage': f"{ci_cov1}/{len(test_results1)}",
        'CI_95_coverage_rate': float(ci_cov1 / len(test_results1)),
        'points': [{**r, 'CI_95': ci_det1[i]} for i, r in enumerate(test_results1)],
    },
    'extra_validation_T25': {
        'n_points': len(EXTRA),
        'MAE': extra_mae1,
        'points': extra_results1,
    },
    'beta_identifiability': {
        'note': (
            'Profile over beta shows NLL plateau: beta is poorly identified under P_max. '
            'The data is step-function-like (all 0/8 or 6/8 except one 5/8), '
            'so many beta values achieve near-identical likelihood. '
            'We fix beta=0.24 from the old model for direct comparability.'
        ),
        'delta_nll_2_range': {
            'beta_lo': float(beta_range[0]),
            'beta_hi': float(beta_range[1]),
            'gamma_lo': float(1 / (2 * beta_range[1])),
            'gamma_hi': float(1 / (2 * beta_range[0])),
        },
        'profile_top10': sorted(profile_results, key=lambda x: x['total_nll'])[:10],
    },
    'model_comparison': {
        'old_model': 'P(det) = Phi(A * alpha^beta * sqrt(T) - z0)',
        'new_model': 'P(det) = P_max * Phi(A * alpha^beta * sqrt(T) - z0)',
        'shared_params': {'beta': BETA_FIXED, 'gamma': gamma1, 'alpha_inf': 0.0},
        'old_fitted': {'A': OLD['A'], 'z0': OLD['z0'], 'n_params': 4, 'train_nll': OLD['train_nll']},
        'new_fitted': {'A': float(A1), 'z0': float(z01), 'P_max': P_MAX, 'n_params': 2, 'train_nll': float(nll1)},
        'comparison_by_dataset': comp,
        'key_improvement': (
            'Old model overpredicts at high alpha + high T (P→1.0), '
            'new model caps at P_max=0.75 matching the observed 6/8 ceiling. '
            'Largest improvements at T>=15, alpha>=0.50.'
        ),
        'high_alpha_detail': [
            {
                'T': int(T), 'alpha': float(a), 'k_actual': int(k), 'n': int(n),
                'p_old': float(det_prob_old(a, T, OLD['A'], OLD['alpha_inf'], OLD['beta'], OLD['z0'])),
                'p_new': float(det_prob_pmax(a, T, A1, BETA_FIXED, z01)),
            }
            for T, a, k, n in sorted(all_pts, key=lambda x: (x[1], x[0]))
            if a >= 0.50
        ],
    },
    'data_sources': {
        'training_T10': 'dose_response_5method_regime_m035.csv (seed=42, Pythia-410M)',
        'training_T20': 'heatmap_data_manifest.json (D102)',
        'validation_T5': 'heatmap_data_manifest.json (D102)',
        'validation_T15': 'heatmap + t15_a075_v2 leadlag (D102)',
        'extra_T25': 'Phase Diagram T=25 experiments (D170)',
    },
}

with open(OUT_DIR / 'theory_verification_d102_pmax.json', 'w') as f:
    json.dump(output, f, indent=2,
              default=lambda o: float(o) if isinstance(o, np.floating)
              else int(o) if isinstance(o, np.integer) else o)
print(f"\nJSON saved.")

# ============================================================
# FIGURE (4 panels)
# ============================================================

fig, axes = plt.subplots(1, 4, figsize=(20, 4.8))

sty = {
    5: ('#2196F3', '--', 's'),
    10: ('black', '-', 'o'),
    15: ('#4CAF50', '-.', '^'),
    20: ('#FF9800', ':', 'D'),
    25: ('#9C27B0', (0,(3,1,1,1)), 'P'),
}

# Panel A: P_max model dose-response
ax = axes[0]
alpha_f = np.linspace(0.001, 1.05, 500)
for Tv in [5, 10, 15, 20, 25]:
    c, ls, mk = sty[Tv]
    pf = det_prob_pmax(alpha_f, Tv, A1, BETA_FIXED, z01)
    ax.plot(alpha_f, pf, color=c, linestyle=ls, lw=1.8, label=f'T={Tv}')

ax.axhline(P_MAX, color='red', linestyle=':', alpha=0.5, lw=1)
ax.text(0.02, P_MAX + 0.02, f'$P_{{max}}$={P_MAX}', fontsize=8, color='red')

dsets = {5: DATA_T5, 10: DATA_T10, 15: DATA_T15, 20: DATA_T20, 25: DATA_T25}
for Tv, data in dsets.items():
    c, ls, mk = sty[Tv]
    aa = [d[0] for d in data]; rr = [d[1]/d[2] for d in data]
    is_tr = Tv in [10, 20]
    ax.scatter(aa, rr, c=c, marker=mk, s=40 if is_tr else 70, zorder=5,
              edgecolors='black' if not is_tr else 'none',
              linewidths=0.8 if not is_tr else 0)

ax.set_xlabel('Contamination $\\alpha$')
ax.set_ylabel('Detection rate')
ax.set_title(f'A. $P_{{max}}$ Model ($\\beta$={BETA_FIXED}, $\\gamma$={gamma1:.2f})')
ax.legend(fontsize=7, loc='center right')
ax.set_xlim(-0.02, 1.05); ax.set_ylim(-0.05, 1.05)

# Panel B: Old vs New at high alpha
ax = axes[1]
high_data = [(T, a, k, n) for T, a, k, n in sorted(all_pts, key=lambda x: (x[0], x[1]))
             if a >= 0.50]
x_idx = np.arange(len(high_data))
actuals = [k/n for _,_,k,n in high_data]
olds = [float(det_prob_old(a, T, OLD['A'], OLD['alpha_inf'], OLD['beta'], OLD['z0']))
        for T,a,k,n in high_data]
news = [float(det_prob_pmax(a, T, A1, BETA_FIXED, z01)) for T,a,k,n in high_data]

w = 0.25
ax.bar(x_idx - w, actuals, w, label='Actual', color='#333', alpha=0.7)
ax.bar(x_idx, olds, w, label='Old model', color='#FF7043', alpha=0.7)
ax.bar(x_idx + w, news, w, label='$P_{max}$ model', color='#42A5F5', alpha=0.7)
ax.axhline(P_MAX, color='red', linestyle=':', alpha=0.5, lw=1)

labels = [f'T{T}\n$\\alpha${a}' for T,a,k,n in high_data]
ax.set_xticks(x_idx)
ax.set_xticklabels(labels, fontsize=5.5)
ax.set_ylabel('Detection rate')
ax.set_title('B. Old vs $P_{max}$: high $\\alpha$')
ax.legend(fontsize=7, loc='upper left')
ax.set_ylim(0, 1.1)

# Panel C: Phase boundary
ax = axes[2]
Tf = np.linspace(3, 55, 500)
ac_new = np.array([alpha_c_pmax(T, A1, BETA_FIXED, z01) for T in Tf])
ac_old = np.array([OLD['alpha_inf'] + ((OLD['z0']/OLD['A'])**(1/OLD['beta'])) * T**(-1/(2*OLD['beta']))
                    for T in Tf])

ax.plot(Tf, np.clip(ac_new, 0, 1.5), 'b-', lw=2, label=f'$P_{{max}}$ model')
ax.plot(Tf, np.clip(ac_old, 0, 1.5), 'r--', lw=1.5, alpha=0.6, label='Old model')

ax.plot([5],[0.80], 'rv', ms=10, zorder=5, label='T=5: all 0/8')
ax.plot([10],[0.475],'ko', ms=10, zorder=5, label='T=10: step ~0.475')
ax.plot([15],[0.42], 'g^', ms=10, zorder=5, label='T=15: 6/8@0.45')
ax.plot([20],[0.42], color='#FF9800', marker='D', ms=10, zorder=5, label='T=20: 5/8@0.45')
ax.plot([25],[0.42], color='#9C27B0', marker='P', ms=10, zorder=5, label='T=25: 6/8@0.45')

ax.set_xlabel('$T$ (epochs)'); ax.set_ylabel('$\\alpha_c$')
ax.set_title('C. Phase Boundary')
ax.legend(fontsize=5.5, loc='upper right')
ax.set_xlim(2, 55); ax.set_ylim(0, 1.1)

# Panel D: Profile likelihood (beta identifiability)
ax = axes[3]
betas = [r['beta'] for r in profile_results]
nlls_total = [r['total_nll'] for r in profile_results]
nlls_train = [r['train_nll'] for r in profile_results]

ax.plot(betas, nlls_total, 'b-', lw=1.5, label='Total (train+test)')
ax.plot(betas, nlls_train, 'r--', lw=1, alpha=0.6, label='Train only')
ax.axvline(BETA_FIXED, color='green', linestyle=':', lw=1.5, label=f'$\\beta$={BETA_FIXED} (old)')
ax.axhline(nll_min + 2.0, color='gray', linestyle=':', alpha=0.5)
ax.text(max(betas)*0.6, nll_min + 2.5, '$\\Delta$NLL=2', fontsize=8, color='gray')

ax.set_xlabel('$\\beta$'); ax.set_ylabel('NLL')
ax.set_title('D. Profile: $\\beta$ unidentifiability')
ax.legend(fontsize=7)
ax.set_xlim(0, max(betas))

plt.tight_layout()
plt.savefig(OUT_DIR / 'fig_theory_d102_pmax.png', dpi=150, bbox_inches='tight')
plt.savefig(OUT_DIR / 'fig_theory_d102_pmax.pdf', bbox_inches='tight')
print("Figure saved.")
