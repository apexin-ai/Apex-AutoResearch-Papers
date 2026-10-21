"""
5T Leave-One-T-Out CV + Model Comparison + β Bootstrap.
Response to R8 W-C2: zero-degree-of-freedom concern.

Phase Diagram 20/20 gives 5 T values for proper LOO-CV.
Model: P(det|α,T) = P_max · Φ(A · α^β · √T − z₀)
Fixed: P_max=0.75, β=0.24. Free: A, z₀.
"""

import json
import numpy as np
from scipy.optimize import minimize, differential_evolution
from scipy.stats import norm, beta as beta_dist
from scipy.special import gammaln
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

OUT_DIR = Path(__file__).parent
P_MAX = 0.75
BETA_FIXED = 0.24

# ============================================================
# DATA: 20/20 Phase Diagram (PermG FDR forward, n=8)
# ============================================================
T_VALUES = [5, 10, 15, 20, 25]
ALPHA_ALL = [0.45, 0.50, 0.60, 0.75]
ALPHA_NOSYNC = [0.45, 0.50, 0.75]

S42 = {
    (5,0.45):0,  (5,0.50):0,  (5,0.60):0,  (5,0.75):0,
    (10,0.45):0, (10,0.50):6, (10,0.60):0, (10,0.75):6,
    (15,0.45):6, (15,0.50):6, (15,0.60):0, (15,0.75):6,
    (20,0.45):5, (20,0.50):6, (20,0.60):0, (20,0.75):6,
    (25,0.45):6, (25,0.50):6, (25,0.60):5, (25,0.75):6,
}

S43 = {
    (10,0.50):0, (10,0.75):6,
    (15,0.60):0, (15,0.75):6,
    (20,0.45):4, (20,0.60):3,
}


def make_arrays(alpha_list, seed_avg=False):
    Ts, As, Ks, Ns = [], [], [], []
    for T in T_VALUES:
        for a in alpha_list:
            if (T, a) not in S42:
                continue
            if seed_avg and (T, a) in S43:
                Ts.append(T); As.append(a)
                Ks.append(S42[(T, a)] + S43[(T, a)]); Ns.append(16)
            else:
                Ts.append(T); As.append(a)
                Ks.append(S42[(T, a)]); Ns.append(8)
    return tuple(np.array(x, dtype=float) for x in (Ts, As, Ks, Ns))


# ============================================================
# LIKELIHOOD
# ============================================================
def binom_ll(k, n, p):
    p = np.clip(np.asarray(p, dtype=float), 1e-10, 1 - 1e-10)
    return float(np.sum(
        gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1)
        + k * np.log(p) + (n - k) * np.log(1 - p)
    ))


def clopper_pearson(k, n, alpha=0.05):
    k, n = int(k), int(n)
    lo = 0.0 if k == 0 else float(beta_dist.ppf(alpha / 2, k, n - k + 1))
    hi = 1.0 if k == n else float(beta_dist.ppf(1 - alpha / 2, k + 1, n - k))
    return lo, hi


# ============================================================
# MODELS
# ============================================================
SHARP = 50.0  # fixed sharpness for step-function models


def pred_m2(a, T, A, z0, beta=BETA_FIXED):
    a = np.asarray(a, dtype=float)
    T = np.asarray(T, dtype=float)
    return P_MAX * norm.cdf(A * np.where(a > 0, a ** beta, 0.0) * np.sqrt(T) - z0)


def nll_m2(p, T, a, k, n, beta=BETA_FIXED):
    if p[0] <= 0:
        return 1e12
    return -binom_ll(k, n, pred_m2(a, T, p[0], p[1], beta))


def fit_m2(T, a, k, n, beta=BETA_FIXED):
    best = None
    for s in [0, 42, 99, 7, 13]:
        r = differential_evolution(nll_m2, [(0.01, 300), (0.1, 60)],
                                   args=(T, a, k, n, beta),
                                   seed=s, maxiter=2000, tol=1e-12, polish=True)
        if best is None or r.fun < best.fun:
            best = r
    return dict(A=float(best.x[0]), z0=float(best.x[1]), nll=float(best.fun))


def pred_m0(a, T, c):
    return P_MAX * norm.cdf(SHARP * (np.asarray(a) - c))


def nll_m0(p, T, a, k, n):
    return -binom_ll(k, n, pred_m0(a, T, p[0]))


def fit_m0(T, a, k, n):
    best = None
    for c0 in np.arange(0.1, 0.9, 0.05):
        r = minimize(nll_m0, [c0], args=(T, a, k, n), method='Nelder-Mead',
                     options={'xatol': 1e-8, 'maxiter': 5000})
        if best is None or r.fun < best.fun:
            best = r
    return dict(threshold=float(best.x[0]), nll=float(best.fun))


def pred_m1(a, T, ap, bp):
    ac = ap - bp * np.asarray(T, dtype=float)
    return P_MAX * norm.cdf(SHARP * (np.asarray(a) - ac))


def nll_m1(p, T, a, k, n):
    return -binom_ll(k, n, pred_m1(a, T, p[0], p[1]))


def fit_m1(T, a, k, n):
    best = None
    for s in [0, 42, 99]:
        r = differential_evolution(nll_m1, [(0.1, 2.0), (0.001, 0.1)],
                                   args=(T, a, k, n),
                                   seed=s, maxiter=1000, tol=1e-12, polish=True)
        if best is None or r.fun < best.fun:
            best = r
    return dict(a=float(best.x[0]), b=float(best.x[1]), nll=float(best.fun))


def pred_m3(a, T, c, d):
    ac = c * np.exp(-d * np.asarray(T, dtype=float))
    return P_MAX * norm.cdf(SHARP * (np.asarray(a) - ac))


def nll_m3(p, T, a, k, n):
    if p[0] <= 0 or p[1] <= 0:
        return 1e12
    return -binom_ll(k, n, pred_m3(a, T, p[0], p[1]))


def fit_m3(T, a, k, n):
    best = None
    for s in [0, 42, 99]:
        r = differential_evolution(nll_m3, [(0.1, 10.0), (0.001, 0.5)],
                                   args=(T, a, k, n),
                                   seed=s, maxiter=1000, tol=1e-12, polish=True)
        if best is None or r.fun < best.fun:
            best = r
    return dict(c=float(best.x[0]), d=float(best.x[1]), nll=float(best.fun))


# ============================================================
# LOO-CV
# ============================================================
def run_loocv(alpha_list, seed_avg=False, label=''):
    T_all, a_all, k_all, n_all = make_arrays(alpha_list, seed_avg)

    folds = []
    all_abs_resid, all_ci_ok = [], []

    for T_held in T_VALUES:
        te = T_all == T_held
        tr = ~te
        Tt, at, kt, nt = T_all[tr], a_all[tr], k_all[tr], n_all[tr]
        Te, ae, ke, ne = T_all[te], a_all[te], k_all[te], n_all[te]
        if len(Te) == 0:
            continue

        fit = fit_m2(Tt, at, kt, nt)
        pp = pred_m2(ae, Te, fit['A'], fit['z0'])

        cells = []
        for i in range(len(Te)):
            actual = ke[i] / ne[i]
            pred_val = float(pp[i])
            resid = actual - pred_val
            ci_lo, ci_hi = clopper_pearson(ke[i], ne[i])
            covered = ci_lo <= pred_val <= ci_hi

            cells.append(dict(
                T=int(Te[i]), alpha=float(ae[i]),
                k=int(ke[i]), n=int(ne[i]),
                actual=round(actual, 4), predicted=round(pred_val, 4),
                residual=round(resid, 4),
                CI_95=[round(ci_lo, 4), round(ci_hi, 4)],
                CI_covered=covered,
            ))
            all_abs_resid.append(abs(resid))
            all_ci_ok.append(covered)

        fold_mae = np.mean([abs(c['residual']) for c in cells])
        note = ''
        if T_held == 5 and all(c['k'] == 0 for c in cells):
            note = 'All 0/n — any reasonable model trivially predicts ~0 here.'

        folds.append(dict(
            T_held_out=T_held,
            n_train=int(len(Tt)), n_test=int(len(Te)),
            fit=dict(A=round(fit['A'], 4), z0=round(fit['z0'], 4)),
            fold_MAE=round(float(fold_mae), 4),
            cells=cells, note=note,
        ))

    cov = sum(all_ci_ok)
    tot = len(all_ci_ok)
    return dict(
        label=label, n_cells=tot,
        folds=folds,
        summary=dict(
            mean_MAE=round(float(np.mean(all_abs_resid)), 4),
            max_abs_residual=round(float(max(all_abs_resid)), 4),
            CI_coverage=f'{cov}/{tot}',
            CI_coverage_rate=round(cov / tot, 4) if tot else None,
        ),
    )


# ============================================================
# MODEL COMPARISON (AIC / BIC)
# ============================================================
def compare_models(alpha_list, label=''):
    T, a, k, n = make_arrays(alpha_list)
    n_obs = len(T)
    out = {}

    # M0
    f = fit_m0(T, a, k, n)
    ll = -f['nll']; kp = 1
    out['M0_constant'] = dict(
        desc='Constant threshold, no T dependence',
        params=dict(threshold=round(f['threshold'], 4)),
        n_params=kp, log_lik=round(ll, 2),
        AIC=round(2 * kp - 2 * ll, 2),
        BIC=round(kp * np.log(n_obs) - 2 * ll, 2),
    )

    # M1
    f = fit_m1(T, a, k, n)
    ll = -f['nll']; kp = 2
    out['M1_linear'] = dict(
        desc='α_c(T) = a − b·T',
        params=dict(a=round(f['a'], 4), b=round(f['b'], 6)),
        n_params=kp, log_lik=round(ll, 2),
        AIC=round(2 * kp - 2 * ll, 2),
        BIC=round(kp * np.log(n_obs) - 2 * ll, 2),
    )

    # M2
    f = fit_m2(T, a, k, n)
    ll = -f['nll']; kp = 2
    out['M2_power_probit'] = dict(
        desc='P = P_max·Φ(A·α^0.24·√T − z₀)',
        params=dict(A=round(f['A'], 4), z0=round(f['z0'], 4)),
        n_params=kp, log_lik=round(ll, 2),
        AIC=round(2 * kp - 2 * ll, 2),
        BIC=round(kp * np.log(n_obs) - 2 * ll, 2),
    )

    # M3
    f = fit_m3(T, a, k, n)
    ll = -f['nll']; kp = 2
    out['M3_exponential'] = dict(
        desc='α_c(T) = c·exp(−d·T)',
        params=dict(c=round(f['c'], 4), d=round(f['d'], 6)),
        n_params=kp, log_lik=round(ll, 2),
        AIC=round(2 * kp - 2 * ll, 2),
        BIC=round(kp * np.log(n_obs) - 2 * ll, 2),
    )

    best_aic = min(m['AIC'] for m in out.values())
    best_bic = min(m['BIC'] for m in out.values())
    for m in out.values():
        m['delta_AIC'] = round(m['AIC'] - best_aic, 2)
        m['delta_BIC'] = round(m['BIC'] - best_bic, 2)

    return dict(label=label, n_obs=n_obs, models=out)


# ============================================================
# β PROFILE LIKELIHOOD + BOOTSTRAP
# ============================================================
def profile_beta(T, a, k, n):
    """Profile likelihood over β: for each β, MLE of (A, z₀)."""
    beta_grid = np.unique(np.concatenate([
        np.arange(0.05, 0.30, 0.01),  # fine near our fixed β=0.24
        [0.24],  # include exact fixed value
        np.arange(0.30, 0.50, 0.02),
        np.arange(0.50, 1.01, 0.02),
        np.arange(1.00, 2.01, 0.05),
    ]))

    profile = []
    for bv in beta_grid:
        f = fit_m2(T, a, k, n, beta=bv)
        profile.append(dict(beta=round(float(bv), 4), nll=round(f['nll'], 4),
                            A=round(f['A'], 4), z0=round(f['z0'], 4)))

    best = min(profile, key=lambda x: x['nll'])
    threshold = best['nll'] + 1.9207  # χ²(1,0.95)/2

    in_ci = [p for p in profile if p['nll'] <= threshold]
    ci_lo = min(p['beta'] for p in in_ci)
    ci_hi = max(p['beta'] for p in in_ci)

    return dict(
        mle=dict(beta=best['beta'], A=best['A'], z0=best['z0'],
                 neg_ll=best['nll']),
        CI_95_profile=[round(ci_lo, 4), round(ci_hi, 4)],
        gamma_CI=[round(1 / (2 * ci_hi), 4), round(1 / (2 * ci_lo), 4)],
        fixed_beta_in_CI=ci_lo <= BETA_FIXED <= ci_hi,
        delta_nll_at_fixed=round(
            min(profile, key=lambda p: abs(p['beta'] - BETA_FIXED))['nll']
            - best['nll'], 4
        ),
        profile_curve=profile,
    )


def nll_m2_free(p, T, a, k, n):
    A, z0, beta = p
    if A <= 0 or beta < 0.01 or beta > 5:
        return 1e12
    return -binom_ll(k, n, pred_m2(a, T, A, z0, beta))


def run_bootstrap(T, a, k, n, B=1000, seed=42):
    """Parametric bootstrap for β: resample from fitted model, re-fit with β free."""
    rng = np.random.default_rng(seed)

    # Fit full model (β free) as generating distribution
    best = None
    bounds = [(0.01, 300), (0.1, 60), (0.01, 3.0)]
    for s in [0, 42, 99, 7, 13]:
        r = differential_evolution(nll_m2_free, bounds, args=(T, a, k, n),
                                   seed=s, maxiter=2000, tol=1e-12, polish=True)
        if best is None or r.fun < best.fun:
            best = r
    pt = dict(A=float(best.x[0]), z0=float(best.x[1]),
              beta=float(best.x[2]), nll=float(best.fun))
    p_hat = np.clip(pred_m2(a, T, pt['A'], pt['z0'], pt['beta']), 1e-10, 1 - 1e-10)

    betas = []
    for b in range(B):
        k_boot = rng.binomial(n.astype(int), p_hat).astype(float)

        # Try multiple starts for robustness
        best_b = None
        for start_beta in [pt['beta'], 0.24, 0.5, 1.0]:
            try:
                r = minimize(nll_m2_free,
                             [pt['A'], pt['z0'], start_beta],
                             args=(T, a, k_boot, n), method='L-BFGS-B',
                             bounds=bounds)
                if r.fun < 1e10 and (best_b is None or r.fun < best_b.fun):
                    best_b = r
            except Exception:
                pass
        if best_b is not None and 0.01 < best_b.x[2] < 3.0:
            betas.append(float(best_b.x[2]))
        if (b + 1) % 200 == 0:
            print(f'  bootstrap {b + 1}/{B}, valid={len(betas)}')

    betas = np.array(betas)
    return dict(
        point_estimate=pt,
        n_bootstrap=B, n_valid=len(betas),
        beta_95CI=[round(float(np.percentile(betas, 2.5)), 4),
                   round(float(np.percentile(betas, 97.5)), 4)],
        beta_mean=round(float(np.mean(betas)), 4),
        beta_std=round(float(np.std(betas)), 4),
        beta_median=round(float(np.median(betas)), 4),
    )


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print('=' * 65)
    print('5T LOO-CV + Model Comparison + β Bootstrap')
    print('=' * 65)

    # --- 1. LOO-CV Version A (16 cells, excl sync-dip α=0.60) ---
    print('\n[1/5] LOO-CV Version A (excl α=0.60, 15 cells)...')
    cv_A = run_loocv(ALPHA_NOSYNC, seed_avg=False,
                     label='Version A: 5T × {0.45,0.50,0.75}, single-seed s42')
    print(f'  MAE={cv_A["summary"]["mean_MAE"]:.4f}  '
          f'CI={cv_A["summary"]["CI_coverage"]}')

    # --- 2. LOO-CV Version B (20 cells, all α) ---
    print('\n[2/5] LOO-CV Version B (all 20 cells)...')
    cv_B = run_loocv(ALPHA_ALL, seed_avg=False,
                     label='Version B: 5T × {0.45,0.50,0.60,0.75}, single-seed s42')
    print(f'  MAE={cv_B["summary"]["mean_MAE"]:.4f}  '
          f'CI={cv_B["summary"]["CI_coverage"]}')

    # --- 3. LOO-CV Seed-averaged A ---
    print('\n[3/5] LOO-CV Seed-averaged Version A...')
    cv_SA = run_loocv(ALPHA_NOSYNC, seed_avg=True,
                      label='Seed-averaged Version A: s42+s43 where available')
    print(f'  MAE={cv_SA["summary"]["mean_MAE"]:.4f}  '
          f'CI={cv_SA["summary"]["CI_coverage"]}')

    # --- 4. Model Comparison ---
    print('\n[4/5] Model comparison (AIC/BIC)...')
    mc_16 = compare_models(ALPHA_NOSYNC, label='16-cell (excl sync-dip)')
    mc_20 = compare_models(ALPHA_ALL, label='20-cell (all)')
    for tag, mc in [('16-cell', mc_16), ('20-cell', mc_20)]:
        print(f'  {tag}:')
        for name, m in mc['models'].items():
            print(f'    {name}: LL={m["log_lik"]:.1f}  '
                  f'AIC={m["AIC"]:.1f}  ΔAIC={m["delta_AIC"]:.1f}')

    # --- 5. β Profile Likelihood ---
    print('\n[5/6] β profile likelihood...')
    T16, a16, k16, n16 = make_arrays(ALPHA_NOSYNC)
    prof = profile_beta(T16, a16, k16, n16)
    print(f'  β MLE = {prof["mle"]["beta"]:.4f}  '
          f'95% profile CI = {prof["CI_95_profile"]}')
    print(f'  β=0.24 in CI: {prof["fixed_beta_in_CI"]}  '
          f'ΔNLL = {prof["delta_nll_at_fixed"]}')

    # --- 6. β Bootstrap ---
    print('\n[6/6] β bootstrap (1000 resamples)...')
    boot = run_bootstrap(T16, a16, k16, n16, B=1000)
    print(f'  β bootstrap 95% CI = {boot["beta_95CI"]}')

    # ============================================================
    # SAVE JSON
    # ============================================================
    output = dict(
        description='5T LOO-CV for α_c(T) theory (R8 W-C2 response)',
        model='P(det|α,T) = P_max · Φ(A · α^β · √T − z₀)',
        fixed=dict(P_max=P_MAX, beta=BETA_FIXED),
        free_params=['A', 'z0'],
        data=dict(
            source='20/20 Phase Diagram, PermG FDR forward',
            T_values=T_VALUES,
            alpha_all=ALPHA_ALL,
            alpha_nosync=ALPHA_NOSYNC,
            cross_seed_cells={str(k): v for k, v in S43.items()},
        ),
        loocv_A=cv_A,
        loocv_B=cv_B,
        loocv_seed_avg_A=cv_SA,
        model_comparison_16=mc_16,
        model_comparison_20=mc_20,
        beta_profile=prof,
        beta_bootstrap=boot,
    )

    json_path = OUT_DIR / 'loocv_5t_results.json'
    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f'\nJSON → {json_path}')

    # ============================================================
    # MARKDOWN SUMMARY
    # ============================================================
    md_lines = []
    md_lines.append('# 5T LOO-CV + Model Comparison + β Bootstrap')
    md_lines.append('')
    md_lines.append('## Model')
    md_lines.append('P(det|α,T) = 0.75 · Φ(A · α^0.24 · √T − z₀)')
    md_lines.append('')
    md_lines.append('Fixed: P_max=0.75, β=0.24. Free per fold: A, z₀ (2 params).')
    md_lines.append('')

    # LOO-CV tables
    for tag, cv in [('A (excl sync-dip, 15 cells)', cv_A),
                    ('B (all 20 cells)', cv_B),
                    ('Seed-averaged A', cv_SA)]:
        md_lines.append(f'## LOO-CV Version {tag}')
        md_lines.append('')
        md_lines.append(f'**Mean MAE = {cv["summary"]["mean_MAE"]:.4f}, '
                        f'CI coverage = {cv["summary"]["CI_coverage"]}**')
        md_lines.append('')
        md_lines.append('| T held | A | z₀ | Fold MAE | Note |')
        md_lines.append('|--------|---|-----|----------|------|')
        for fold in cv['folds']:
            md_lines.append(
                f'| {fold["T_held_out"]} | {fold["fit"]["A"]:.3f} | '
                f'{fold["fit"]["z0"]:.3f} | {fold["fold_MAE"]:.4f} | '
                f'{fold["note"]} |'
            )
        md_lines.append('')
        md_lines.append('Cell-level predictions:')
        md_lines.append('')
        md_lines.append('| T | α | actual | predicted | residual | 95% CI | covered |')
        md_lines.append('|---|---|--------|-----------|----------|--------|---------|')
        for fold in cv['folds']:
            for c in fold['cells']:
                md_lines.append(
                    f'| {c["T"]} | {c["alpha"]:.2f} | '
                    f'{c["actual"]:.3f} | {c["predicted"]:.3f} | '
                    f'{c["residual"]:+.3f} | '
                    f'[{c["CI_95"][0]:.3f}, {c["CI_95"][1]:.3f}] | '
                    f'{"✓" if c["CI_covered"] else "✗"} |'
                )
        md_lines.append('')

    # Model comparison
    md_lines.append('## Model Comparison')
    md_lines.append('')
    for tag, mc in [('16-cell', mc_16), ('20-cell', mc_20)]:
        md_lines.append(f'### {tag} ({mc["label"]})')
        md_lines.append('')
        md_lines.append('| Model | k | LL | AIC | ΔAIC | BIC | ΔBIC |')
        md_lines.append('|-------|---|-----|-----|------|-----|------|')
        for name, m in mc['models'].items():
            md_lines.append(
                f'| {name} | {m["n_params"]} | {m["log_lik"]:.1f} | '
                f'{m["AIC"]:.1f} | {m["delta_AIC"]:.1f} | '
                f'{m["BIC"]:.1f} | {m["delta_BIC"]:.1f} |'
            )
        md_lines.append('')

    # β inference
    md_lines.append('## β Inference')
    md_lines.append('')
    md_lines.append('### Profile Likelihood (primary)')
    md_lines.append(f'- β MLE = {prof["mle"]["beta"]:.4f} '
                    f'(A={prof["mle"]["A"]:.3f}, z₀={prof["mle"]["z0"]:.3f})')
    md_lines.append(f'- 95% profile CI: {prof["CI_95_profile"]}')
    md_lines.append(f'- γ = 1/(2β) CI: {prof["gamma_CI"]}')
    md_lines.append(f'- Fixed β=0.24 in CI: {prof["fixed_beta_in_CI"]}')
    if prof["delta_nll_at_fixed"] is not None:
        md_lines.append(f'- ΔNLL(β=0.24 vs MLE): {prof["delta_nll_at_fixed"]:.2f}')
    md_lines.append('')
    md_lines.append('### Parametric Bootstrap (secondary)')
    md_lines.append(f'- 95% percentile CI: {boot["beta_95CI"]}')
    md_lines.append(f'- Mean ± SD: {boot["beta_mean"]:.4f} ± {boot["beta_std"]:.4f}')
    md_lines.append(f'- Valid: {boot["n_valid"]}/{boot["n_bootstrap"]}')
    md_lines.append('')

    md_path = OUT_DIR / 'loocv_5t_summary.md'
    with open(md_path, 'w') as f:
        f.write('\n'.join(md_lines))
    print(f'Markdown → {md_path}')
