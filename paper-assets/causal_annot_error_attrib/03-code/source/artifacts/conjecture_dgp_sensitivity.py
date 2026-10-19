#!/usr/bin/env python3
"""
Conjecture 1 robustness to DGP parameters (β, σ²).

Reviewer concern: "Only default DGP tested" in Conjecture 1 verification.
This sweeps a (β, σ²) × topology grid and reports per-cell ε-approximate
monotonicity statistics.

Grid:
  - β (coefficient magnitude scale) ∈ {0.1, 0.5, 1.0, 2.0, 5.0}
  - σ² (T-equation noise variance, where applicable) ∈ {0.5, 1.0, 2.0}
  - topology ∈ {confounding, mediation, collider, exposure, mbias, frontdoor, iv}
  - K = 3, N_C0 = 10,000 Dirichlet(1,1,1) per cell, δ step = 0.01

For each (β, σ², topology, C₀), build C(δ) = (1-δ)·I + δ·C₀ for δ ∈ [0, δ_max]
and compute the analytic plim curve |B(δ)| = |τ̂(C(δ)) - τ_true|.
The wrong-direction step is the largest single-δ violation against the
expected direction (non-decreasing for confounding/mediation/exposure/
frontdoor/iv; non-increasing for collider/mbias).

Outputs:
  artifacts/conjecture_dgp_sensitivity_results.json
  artifacts/conjecture_dgp_sensitivity_table.tex
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exp_d_conjecture_verify_v2 import (
    ALL_TOPOS, NON_DECREASING,
    GH_X, GH_W, GH_X2_a_flat, GH_X2_b_flat, GH_W2_flat,
    _softmax,
    AnalyticSuffStats, AnalyticIVSuffStats,
    compute_confounding_ss as _ss_conf_v2,
    compute_mediation_ss as _ss_med_v2,
    compute_exposure_ss as _ss_exp_v2,
    compute_iv_ss as _ss_iv_v2,
    compute_bias_curve, check_monotonicity,
    get_tau_at_C, make_p_A,
    _ALPHA_POOL, _BETA_A_POOL, _BETA_POOL,
    _GAMMA_POOL, _DELTA_POOL, _DT_POOL, _DY_POOL,
    _MBIAS_A1_POOL, _MBIAS_A2_POOL,
    _IV_DZ_POOL, _IV_DU_POOL,
    _FD_GAMMA_POOL, _FD_DELTA_POOL,
)

# ====================================================================
# Configuration
# ====================================================================
K = 3
N_C0 = 10_000
DELTA_STEP = 0.01
SEED = 42
MONO_TOL = 1e-12

BETA_GRID = [0.1, 0.5, 1.0, 2.0, 5.0]
SIGMA_SQ_GRID = [0.5, 1.0, 2.0]
EPS_DISPLAY_THRESHOLD = 0.06  # paper-claimed bound

DRY_RUN_N = int(os.environ.get('DRY_RUN_N', '0'))  # >0 overrides N_C0

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# σ² affects the T-equation noise variance for: confounding (sigma_T²),
# collider (T variance), mbias (eta_T variance), frontdoor (eta_T variance).
# For mediation (binary T), exposure (no T), iv (Wald, no T regression),
# σ² does not enter the plim — those cells will be identical across σ².
SIGMA_DEPENDENT = {'confounding', 'collider', 'mbias', 'frontdoor'}

# Weak-IV filter: for IV, the Wald denominator (1-δ)·FS[1] + δ·(C₀·FS)[1]
# is linear in δ. If FS[1] and (C₀·FS)[1] have opposite signs, the
# denominator crosses zero, the Wald plim has a pole, and |bias(δ)| diverges
# there — a weak-instrument pathology rather than a Conjecture-1 violation.
# We drop these C₀ from the violation count and report them separately.

# ====================================================================
# Parameter grid: scale coefficients by β, noise variance by σ²
# ====================================================================
def make_params(beta, sigma_sq):
    """DGP parameters scaled by β (coefficient magnitude) and σ² (T-noise variance).

    β scales all "effect" coefficients (those that enter the structural
    equations besides the target τ and U-confounder coefficients).
    σ² sets the variance of the T-equation noise (where T is a continuous
    variable: confounding/collider/mbias/frontdoor).
    """
    p_A = make_p_A(K)
    sigma = float(np.sqrt(sigma_sq))
    b = float(beta)
    return dict(
        confounding=dict(
            p_A=p_A,
            alpha=b * np.array(_ALPHA_POOL[:K - 1]),
            beta_A=b * np.array(_BETA_A_POOL[:K - 1]),
            beta_T=2.0,        # target τ kept fixed
            sigma_T=sigma,
        ),
        mediation=dict(
            tau=0.5,           # target τ kept fixed
            gamma=b * np.array(_GAMMA_POOL[:K]),
            delta=b * np.array(_DELTA_POOL[:K]),
            beta=b * np.array(_BETA_POOL[:K]),
        ),
        collider=dict(
            tau=1.0,
            g=np.zeros(K),
            dT=b * np.array(_DT_POOL[:K]),
            dY=b * np.array(_DY_POOL[:K]),
            sigma_T=sigma,
        ),
        exposure=dict(
            p_A=p_A,
            beta=b * np.array(_BETA_POOL[:K]),
        ),
        mbias=dict(
            tau=1.0,
            delta_coef=b,
            lam=b,
            g=np.zeros(K),
            a1=b * np.array(_MBIAS_A1_POOL[:K]),
            a2=b * np.array(_MBIAS_A2_POOL[:K]),
            sigma_eta=sigma,
        ),
        iv=dict(
            lam=b,
            g=np.zeros(K),
            dZ=b * np.array(_IV_DZ_POOL[:K]),
            dU=b * np.array(_IV_DU_POOL[:K]),
            beta=b * np.array(_BETA_POOL[:K]),
        ),
        frontdoor=dict(
            alpha_U=1.0,
            lam_U=b,
            gamma=b * np.array(_FD_GAMMA_POOL[:K]),
            delta=b * np.array(_FD_DELTA_POOL[:K]),
            beta=b * np.array(_BETA_POOL[:K]),
            sigma_eta=sigma,
        ),
    )


# ====================================================================
# Sufficient stats: confounding, mediation, exposure, iv reuse v2.
# Collider/mbias/frontdoor need σ²-aware variants.
# ====================================================================
def compute_collider_ss_scaled(p):
    """Collider with T ~ N(0, sigma_T²) instead of N(0,1).

    DGP: T ~ N(0, σ²), eps_Y ~ N(0,1) independent
         Y = τ·T + eps_Y
         A | T, Y ~ Cat(softmax(g + dT·T + dY·Y))
    Reparametrize Z1 = T/σ ~ N(0,1) so T = σ·Z1, Y = τσ·Z1 + Z2.
    """
    ss = AnalyticSuffStats(K, has_T=True)
    tau = p['tau']
    g = p['g']
    dT = p['dT']
    dY = p['dY']
    sigma_T = p['sigma_T']
    sigma_T2 = sigma_T ** 2

    # T = σ_T · Z1, eps_Y = Z2; Y = τ·σ_T·Z1 + Z2
    coeff1 = (dT + tau * dY) * sigma_T   # of Z1 in logits
    coeff2 = dY                           # of Z2 in logits

    logits = (g[None, :]
              + coeff1[None, :] * GH_X2_a_flat[:, None]
              + coeff2[None, :] * GH_X2_b_flat[:, None])
    probs = _softmax(logits)
    w = GH_W2_flat

    T_vals = sigma_T * GH_X2_a_flat
    Y_vals = tau * sigma_T * GH_X2_a_flat + GH_X2_b_flat

    ss.p_A = (w[:, None] * probs).sum(axis=0)
    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)
    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)

    ss.E_T = 0.0
    ss.E_T2 = sigma_T2
    ss.E_Y = 0.0
    ss.E_TY = tau * sigma_T2
    return ss


def compute_mbias_ss_scaled(p):
    """M-bias with eta_T ~ N(0, sigma_eta²) instead of N(0,1).

    DGP: U1, U2 ~ N(0,1) iid (latent confounders kept unit variance)
         T = δ·U1 + η,  η ~ N(0, σ_η²)
         Y = τ·T + λ·U2 + eps_Y
         A | U1, U2 ~ Cat(softmax(g + a1·U1 + a2·U2))
    """
    ss = AnalyticSuffStats(K, has_T=True)
    tau = p['tau']
    delta_coef = p['delta_coef']
    lam = p['lam']
    g = p['g']
    a1 = p['a1']
    a2 = p['a2']
    sigma_eta = p['sigma_eta']

    logits = (g[None, :]
              + a1[None, :] * GH_X2_a_flat[:, None]
              + a2[None, :] * GH_X2_b_flat[:, None])
    probs = _softmax(logits)
    w = GH_W2_flat
    U1_vals = GH_X2_a_flat
    U2_vals = GH_X2_b_flat

    ss.p_A = (w[:, None] * probs).sum(axis=0)
    E_U1_Dk = (w[:, None] * U1_vals[:, None] * probs).sum(axis=0)
    E_U2_Dk = (w[:, None] * U2_vals[:, None] * probs).sum(axis=0)
    # eta indep of A => E[eta·1(A=k)] = 0
    ss.E_TD = delta_coef * E_U1_Dk
    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk

    ss.E_T = 0.0
    ss.E_T2 = delta_coef ** 2 + sigma_eta ** 2
    ss.E_Y = 0.0
    ss.E_TY = tau * ss.E_T2
    return ss


def compute_frontdoor_ss_scaled(p):
    """Front-door with eta_T ~ N(0, sigma_eta²) instead of N(0,1).

    DGP: U ~ N(0,1), T = α_U·U + η, η ~ N(0, σ_η²)
         M | T ~ Cat(softmax(γ + δ·T))
         Y = D_M·β[1:] + λ_U·U + eps_Y
    """
    ss = AnalyticSuffStats(K, has_T=True)
    alpha_U = p['alpha_U']
    lam_U = p['lam_U']
    gamma = p['gamma']
    delta_coef = p['delta']
    beta = p['beta']
    sigma_eta = p['sigma_eta']

    sigma_T2 = alpha_U ** 2 + sigma_eta ** 2
    sigma_T = float(np.sqrt(sigma_T2))

    T_nodes = GH_X * sigma_T
    T_weights = GH_W

    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]
    probs = _softmax(logits)

    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)
    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)

    # E[U|T] = Cov(U,T)/Var(T)·T = α_U/σ_T² · T
    E_U_given_T = alpha_U / sigma_T2 * T_nodes
    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)

    ss.E_YD = np.zeros(K)
    for k in range(K):
        beta_k = beta[k] if k >= 1 else 0.0
        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]

    ss.E_T = 0.0
    ss.E_T2 = sigma_T2
    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))
    ss.E_TY = sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + lam_U * alpha_U
    return ss


_COMPUTE_SS = {
    'confounding': lambda p: _ss_conf_v2(K, p),
    'mediation':   lambda p: _ss_med_v2(K, p),
    'exposure':    lambda p: _ss_exp_v2(K, p),
    'iv':          lambda p: _ss_iv_v2(K, p),
    'collider':    lambda p: compute_collider_ss_scaled(p),
    'mbias':       lambda p: compute_mbias_ss_scaled(p),
    'frontdoor':   lambda p: compute_frontdoor_ss_scaled(p),
}


def get_tau_true(topo, params, ss):
    p = params[topo]
    if topo in ('collider', 'mbias'):
        return p['tau']
    return get_tau_at_C(topo, np.eye(K), ss)


def compute_iv_bias_curve_analytic(C0, ss, delta_step=DELTA_STEP):
    """Cancellation-free IV bias curve.

    Wald: τ̂(δ) = RF / fs_star_1(δ),  fs_star_1(δ) = (1-δ)·FS[1] + δ·(C₀·FS)[1].
    τ_true = RF / FS[1].  Then
       |B(δ)| = |RF| · δ · |Δ| / (|fs_star_1(δ)| · |FS[1]|),   Δ = (C₀·FS)[1] - FS[1].
    This avoids the catastrophic cancellation in `RF/fs - RF/FS[1]` that
    triggers spurious "violations" when |bias| is large.
    """
    Kloc = C0.shape[0]
    min_diag = np.diag(C0).min()
    if min_diag >= 1.0:
        delta_max = 10.0
    else:
        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
    deltas = np.arange(0, delta_max + delta_step / 2, delta_step)

    FS = ss.FS
    FS0_1 = float((C0 @ FS)[1])
    a = float(FS[1])
    b = FS0_1
    fs_star_1 = (1.0 - deltas) * a + deltas * b
    Delta = b - a

    # Sign-flip ⇒ denominator crosses zero in the δ range
    if np.any(np.diff(np.sign(fs_star_1)) != 0):
        return deltas, np.full(len(deltas), np.nan), True

    abs_RF = abs(float(ss.RF))
    abs_a = abs(a)
    if abs_a < 1e-15:
        return deltas, np.full(len(deltas), np.nan), True
    bias_abs = abs_RF * deltas * abs(Delta) / (np.abs(fs_star_1) * abs_a)
    return deltas, bias_abs, False


# ====================================================================
# Per-cell evaluation
# ====================================================================
def evaluate_cell(topo, beta, sigma_sq, n_c0):
    params = make_params(beta, sigma_sq)
    ss = _COMPUTE_SS[topo](params[topo])
    tau_true = get_tau_true(topo, params, ss)

    if np.isnan(tau_true) or abs(tau_true) < 1e-12:
        return {
            'beta': beta, 'sigma_sq': sigma_sq, 'topology': topo,
            'n_matrices': n_c0, 'violation_count': 0, 'violation_rate': 0.0,
            'worst_epsilon_abs': 0.0, 'worst_epsilon_rel': 0.0,
            'tau_true': float(tau_true) if not np.isnan(tau_true) else None,
            'direction': 'non-dec' if topo in NON_DECREASING else 'non-inc',
            'skipped': True,
            'reason': 'tau_true is NaN or near zero',
        }

    rng = np.random.default_rng(
        SEED * 17 + ALL_TOPOS.index(topo) * 100003
        + int(round(beta * 1000)) * 13 + int(round(sigma_sq * 1000))
    )

    violations = 0
    nan_curves = 0
    weak_iv_filtered = 0
    worst_abs = 0.0

    for _ in range(n_c0):
        C0 = np.empty((K, K))
        for j in range(K):
            C0[:, j] = rng.dirichlet(np.ones(K))

        if topo == 'iv':
            _, bias_abs, weak = compute_iv_bias_curve_analytic(C0, ss,
                                                                delta_step=DELTA_STEP)
            if weak:
                weak_iv_filtered += 1
                continue
        else:
            _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true,
                                             delta_step=DELTA_STEP)

        n_nan = int(np.isnan(bias_abs).sum())
        if n_nan > len(bias_abs) * 0.5:
            nan_curves += 1
            continue

        n_viol = check_monotonicity(bias_abs, topo, tol=MONO_TOL)
        if n_viol > 0:
            violations += 1
            valid = ~np.isnan(bias_abs)
            diffs = np.diff(bias_abs[valid])
            if topo in NON_DECREASING:
                step = float(-diffs.min())  # most negative => largest violation
            else:
                step = float(diffs.max())   # most positive => largest violation
            if step > worst_abs:
                worst_abs = step

    effective_denom = max(n_c0 - nan_curves - weak_iv_filtered, 1)
    return {
        'beta': beta,
        'sigma_sq': sigma_sq,
        'topology': topo,
        'n_matrices': n_c0,
        'nan_curves': nan_curves,
        'weak_iv_filtered': weak_iv_filtered,
        'violation_count': int(violations),
        'violation_rate': 100.0 * violations / effective_denom,
        'worst_epsilon_abs': float(worst_abs),
        'worst_epsilon_rel': float(worst_abs / abs(tau_true)),
        'tau_true': float(tau_true),
        'direction': 'non-dec' if topo in NON_DECREASING else 'non-inc',
        'sigma_affects_plim': topo in SIGMA_DEPENDENT,
    }


# ====================================================================
# Main
# ====================================================================
def main():
    t_total = time.time()
    n_c0 = DRY_RUN_N if DRY_RUN_N > 0 else N_C0
    if DRY_RUN_N > 0:
        print(f"DRY RUN: N_C0 = {n_c0} (env DRY_RUN_N override)")
    print("=" * 78)
    print(f"Conjecture 1 robustness across (β, σ²) × topology, K={K}")
    print(f"  β grid: {BETA_GRID}")
    print(f"  σ² grid: {SIGMA_SQ_GRID}")
    print(f"  topologies: {ALL_TOPOS}")
    print(f"  N_C0 per cell: {n_c0:,}, δ step: {DELTA_STEP}, seed: {SEED}")
    print(f"  σ²-dependent topologies: {sorted(SIGMA_DEPENDENT)}")
    print("=" * 78)
    sys.stdout.flush()

    grid_results = []
    n_cells = len(BETA_GRID) * len(SIGMA_SQ_GRID) * len(ALL_TOPOS)
    cell_i = 0

    print(f"\n  {'topo':<14} {'β':>6} {'σ²':>5} {'τ_true':>11} "
          f"{'viol':>7} {'rate%':>7} {'ε_abs':>10} {'ε_rel':>10} "
          f"{'wkIV':>5} {'time':>7}")
    print("  " + "-" * 86)
    sys.stdout.flush()

    for topo in ALL_TOPOS:
        for beta in BETA_GRID:
            for sigma_sq in SIGMA_SQ_GRID:
                cell_i += 1
                t0 = time.time()
                rec = evaluate_cell(topo, beta, sigma_sq, n_c0)
                elapsed = time.time() - t0
                tau_str = (f"{rec['tau_true']:>11.5f}"
                           if rec.get('tau_true') is not None
                           and not np.isnan(rec['tau_true'])
                           else f"{'NaN':>11}")
                wkiv = rec.get('weak_iv_filtered', 0)
                print(f"  {topo:<14} {beta:>6.2f} {sigma_sq:>5.2f} "
                      f"{tau_str} "
                      f"{rec['violation_count']:>7} "
                      f"{rec['violation_rate']:>7.3f} "
                      f"{rec['worst_epsilon_abs']:>10.2e} "
                      f"{rec['worst_epsilon_rel']:>10.2e} "
                      f"{wkiv:>5} "
                      f"{elapsed:>6.1f}s  [{cell_i}/{n_cells}]")
                sys.stdout.flush()
                grid_results.append(rec)

    # ----- Aggregate summary -----
    max_eps_overall = max(r['worst_epsilon_rel'] for r in grid_results)
    max_eps_abs_overall = max(r['worst_epsilon_abs'] for r in grid_results)
    by_topo_rel = {}
    by_topo_abs = {}
    for t in ALL_TOPOS:
        vals_rel = [r['worst_epsilon_rel'] for r in grid_results
                    if r['topology'] == t]
        vals_abs = [r['worst_epsilon_abs'] for r in grid_results
                    if r['topology'] == t]
        by_topo_rel[t] = max(vals_rel) if vals_rel else 0.0
        by_topo_abs[t] = max(vals_abs) if vals_abs else 0.0

    summary = {
        'max_epsilon_rel_overall': float(max_eps_overall),
        'max_epsilon_abs_overall': float(max_eps_abs_overall),
        'max_epsilon_rel_by_topology': {k: float(v)
                                         for k, v in by_topo_rel.items()},
        'max_epsilon_abs_by_topology': {k: float(v)
                                         for k, v in by_topo_abs.items()},
        'all_below_006': bool(max_eps_overall <= EPS_DISPLAY_THRESHOLD),
        'eps_display_threshold': EPS_DISPLAY_THRESHOLD,
        'total_cells': n_cells,
        'total_C0_samples': n_cells * n_c0,
    }

    elapsed_total = time.time() - t_total
    output = {
        'config': {
            'K': K,
            'n_C0_per_cell': n_c0,
            'beta_grid': BETA_GRID,
            'sigma_sq_grid': SIGMA_SQ_GRID,
            'topologies': ALL_TOPOS,
            'delta_step': DELTA_STEP,
            'seed': SEED,
            'mono_tol': MONO_TOL,
            'method': 'analytic_plim_via_GH_quadrature',
            'sigma_dependent_topologies': sorted(SIGMA_DEPENDENT),
            'tau_treatment': {
                'confounding': 'beta_T = 2.0 (fixed); β scales α (confounder→T) and β_A (confounder→Y)',
                'mediation': 'tau = 0.5 (fixed); β scales γ (mediator|T), δ (mediator|T,A), β (mediator→Y)',
                'collider': 'tau = 1.0 (fixed); β scales dT, dY; σ² is Var(T)',
                'exposure': 'no T; β scales β (A→Y) only',
                'mbias': 'tau = 1.0 (fixed); β scales δ, λ, a1, a2; σ² is Var(η_T)',
                'iv': 'β scales β (A→Y), dZ, dU, λ',
                'frontdoor': 'α_U = 1.0 (fixed); β scales γ, δ, β, λ_U; σ² is Var(η_T)',
            },
            'dry_run': DRY_RUN_N > 0,
        },
        'grid_results': grid_results,
        'summary': summary,
        'elapsed_seconds': elapsed_total,
    }

    out_path = os.path.join(OUT_DIR, 'conjecture_dgp_sensitivity_results.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nJSON -> {out_path}")

    # ----- LaTeX table -----
    tex = []
    tex.append("% Auto-generated by conjecture_dgp_sensitivity.py")
    tex.append("% Worst-case ε_rel = max wrong-direction step / |τ_true| over "
               f"{n_c0:,} random C₀ per cell.")
    tex.append("\\begin{table}[t]")
    tex.append("\\centering")
    tex.append("\\small")
    tex.append("\\setlength{\\tabcolsep}{4pt}")
    tex.append("\\begin{tabular}{cc" + "c" * len(ALL_TOPOS) + "}")
    tex.append("\\toprule")
    tex.append("$\\beta$ & $\\sigma^2$ & "
               + " & ".join("\\textsc{" + t[:5] + "}" for t in ALL_TOPOS)
               + " \\\\")
    tex.append("\\midrule")

    rec_by = {(r['topology'], r['beta'], r['sigma_sq']): r for r in grid_results}
    for beta in BETA_GRID:
        for sigma_sq in SIGMA_SQ_GRID:
            row = [f"{beta:g}", f"{sigma_sq:g}"]
            for topo in ALL_TOPOS:
                r = rec_by[(topo, beta, sigma_sq)]
                eps = r['worst_epsilon_rel']
                if eps <= 1e-10:
                    cell = "$0$"
                elif eps < 1e-4:
                    cell = f"${eps:.1e}$".replace("e-0", "e-").replace("e+0", "e")
                else:
                    cell = f"${eps:.4f}$"
                row.append(cell)
            tex.append(" & ".join(row) + " \\\\")
        if beta != BETA_GRID[-1]:
            tex.append("\\midrule")
    tex.append("\\bottomrule")
    tex.append("\\end{tabular}")
    cap = (f"Conjecture~1 robustness: worst-case $\\varepsilon_{{\\text{{rel}}}}"
           f" = \\max_{{C_0}} (\\text{{wrong-direction step}})/|\\tau_{{\\text{{true}}}}|$"
           f" across {len(BETA_GRID)} effect-magnitude scales $\\beta$, "
           f"{len(SIGMA_SQ_GRID)} noise variances $\\sigma^2$, and "
           f"{len(ALL_TOPOS)} topologies ($K{{=}}{K}$, "
           f"${n_c0:,}$ Dirichlet$(1,...,1)$ matrices per cell). "
           f"Overall maximum $\\varepsilon_{{\\text{{rel}}}}"
           f"={max_eps_overall:.4f}$; "
           f"all cells {'$\\le 0.06$' if summary['all_below_006'] else '> 0.06 at some cell'}.")
    tex.append("\\caption{" + cap + "}")
    tex.append("\\label{tab:conj1-dgp-sensitivity}")
    tex.append("\\end{table}")

    tex_path = os.path.join(OUT_DIR, 'conjecture_dgp_sensitivity_table.tex')
    with open(tex_path, 'w') as f:
        f.write("\n".join(tex) + "\n")
    print(f"LaTeX -> {tex_path}")

    # ----- Console summary -----
    print("\n" + "=" * 78)
    print(f"Overall max ε_rel = {max_eps_overall:.5f}"
          f" (abs = {max_eps_abs_overall:.5e})")
    print(f"All cells ≤ 0.06: {summary['all_below_006']}")
    print("Per-topology max ε_rel:")
    for t in ALL_TOPOS:
        print(f"  {t:<14} {by_topo_rel[t]:.5f}  (abs {by_topo_abs[t]:.3e})")
    print(f"Total cells: {n_cells}, total C₀ samples: {n_cells * n_c0:,}")
    print(f"Elapsed: {elapsed_total:.1f}s ({elapsed_total / 60:.2f} min)")
    print("=" * 78)


if __name__ == "__main__":
    main()
