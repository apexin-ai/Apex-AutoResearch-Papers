#!/usr/bin/env python3
"""
Exp-D: Conjecture 1 Extended Verification (Envelope Monotonicity)

Part 1: 10,000 random Dirichlet(1,...,1) C0 per (topology, K) -- 210,000 total tests
Part 2: Adversarial search via scipy.minimize for K in {3, 5} -- 500 starts per config

Conjecture 1:
  |B(delta)| non-decreasing for {confounding, mediation, exposure, frontdoor, iv}
  |B(delta)| non-increasing for {collider, mbias}

where B(delta) = plim(C(delta)) - tau_true, C(delta) = (1-delta)I + delta*C0.
"""

import numpy as np
import json
import time
import sys
import os
from scipy.optimize import minimize as scipy_minimize

# ====================================================================
# Configuration
# ====================================================================
K_VALUES = [3, 5, 7]
K_ADVERSARIAL = [3, 5]
N_RANDOM = 10_000
N_LARGE = 5_000_000
DELTA_STEP = 0.01
SEED = 12345
MONO_TOL = 1e-8

ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
             'mbias', 'iv', 'frontdoor']
TOPO_IDX = {t: i for i, t in enumerate(ALL_TOPOS)}
NON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}
NON_INCREASING = {'collider', 'mbias'}

ADV_DELTA_PAIRS = [(0.0, 0.2), (0.0, 0.5), (0.1, 0.3), (0.2, 0.5), (0.3, 0.7)]
ADV_N_STARTS = 100

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ====================================================================
# DGP Parameter Pools (from plan_002)
# ====================================================================
_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
_MBIAS_A1_POOL = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]
_MBIAS_A2_POOL = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]
_IV_DZ_POOL = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]
_IV_DU_POOL = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]
_FD_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_FD_DELTA_POOL = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]


def make_p_A(K):
    if K == 3:
        return np.array([0.40, 0.35, 0.25])
    raw = np.array([1.0 / i for i in range(1, K + 1)])
    return raw / raw.sum()


def make_all_params(K):
    p_A = make_p_A(K)
    return dict(
        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K - 1]),
                         beta_A=np.array(_BETA_A_POOL[:K - 1]), beta_T=2.0, sigma_T=1.0),
        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),
                       delta=np.array(_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
        collider=dict(tau=1.0, g=np.zeros(K), dT=np.array(_DT_POOL[:K]),
                      dY=np.array(_DY_POOL[:K])),
        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),
        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),
                   a1=np.array(_MBIAS_A1_POOL[:K]), a2=np.array(_MBIAS_A2_POOL[:K])),
        iv=dict(lam=1.0, g=np.zeros(K), dZ=np.array(_IV_DZ_POOL[:K]),
                dU=np.array(_IV_DU_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
        frontdoor=dict(alpha_U=1.0, lam_U=1.0, gamma=np.array(_FD_GAMMA_POOL[:K]),
                       delta=np.array(_FD_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
    )


# ====================================================================
# DGP Generators (from plan_002)
# ====================================================================
def _softmax_rows(logits):
    e = np.exp(logits - logits.max(axis=-1, keepdims=True))
    return e / e.sum(axis=-1, keepdims=True)


def _sample_cat(probs, rng):
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=probs.shape[0])[:, None]
    return (u >= cum).sum(axis=1).astype(int)


def gen_confounding(K, N, p, rng):
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
    return T, Y, A


def gen_mediation(K, N, p, rng):
    T = rng.binomial(1, 0.5, N).astype(float)
    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
    A = _sample_cat(_softmax_rows(logits), rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1)
    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
    return T, Y, A


def gen_collider(K, N, p, rng):
    T = rng.normal(0, 1, N)
    Y = p['tau'] * T + rng.normal(0, 1, N)
    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]
              + p['dY'][None, :] * Y[:, None])
    A = _sample_cat(_softmax_rows(logits), rng)
    return T, Y, A


def gen_exposure(K, N, p, rng):
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
    return None, Y, A


def gen_mbias(K, N, p, rng):
    U1 = rng.normal(0, 1, N)
    U2 = rng.normal(0, 1, N)
    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)
    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)
    logits = np.zeros((N, K))
    for j in range(1, K):
        logits[:, j] = p['g'][j] + p['a1'][j] * U1 + p['a2'][j] * U2
    A = _sample_cat(_softmax_rows(logits), rng)
    return T, Y, A


def gen_iv(K, N, p, rng):
    Z = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    eps = rng.normal(0, 1, N)
    logits = np.zeros((N, K))
    for j in range(1, K):
        logits[:, j] = p['g'][j] + p['dZ'][j] * Z + p['dU'][j] * U
    A = _sample_cat(_softmax_rows(logits), rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = D @ p['beta'][1:] + p['lam'] * U + eps
    return Z, Y, A


def gen_frontdoor(K, N, p, rng):
    U = rng.normal(0, 1, N)
    T = p['alpha_U'] * U + rng.normal(0, 1, N)
    logits = np.zeros((N, K))
    for j in range(1, K):
        logits[:, j] = p['gamma'][j] + p['delta'][j] * T
    M = _sample_cat(_softmax_rows(logits), rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (M == j + 1).astype(float)
    Y = D @ p['beta'][1:] + p['lam_U'] * U + rng.normal(0, 1, N)
    return T, Y, M


_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,
            collider=gen_collider, exposure=gen_exposure,
            mbias=gen_mbias, iv=gen_iv, frontdoor=gen_frontdoor)


# ====================================================================
# Sufficient Statistics
# ====================================================================
class SuffStats:
    def __init__(self, T, Y, A, K):
        self.K = K
        self.has_T = T is not None
        N = len(Y)
        DA = np.zeros((N, K))
        for k in range(K):
            DA[:, k] = (A == k).astype(float)
        self.p_A = DA.mean(0)
        self.E_Y = Y.mean()
        self.E_YD = (DA * Y[:, None]).mean(0)
        if self.has_T:
            self.E_T = T.mean()
            self.E_T2 = (T ** 2).mean()
            self.E_TY = (T * Y).mean()
            self.E_TD = (DA * T[:, None]).mean(0)


class IVSuffStats:
    def __init__(self, Z, Y, A, K):
        self.K = K
        z1 = Z == 1
        z0 = Z == 0
        self.RF = Y[z1].mean() - Y[z0].mean()
        self.FS = np.zeros(K)
        for k in range(K):
            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()


# ====================================================================
# Plim computation (single C)
# ====================================================================
def plim_ols_with_T(C, ss):
    K = ss.K
    q = C @ ss.p_A
    ct = C @ ss.E_TD
    cy = C @ ss.E_YD
    dim = K + 1
    EZZ = np.zeros((dim, dim))
    EZZ[0, 0] = 1.0
    EZZ[0, 1] = ss.E_T
    EZZ[1, 0] = ss.E_T
    EZZ[1, 1] = ss.E_T2
    EZZ[0, 2:] = q[1:]
    EZZ[2:, 0] = q[1:]
    EZZ[1, 2:] = ct[1:]
    EZZ[2:, 1] = ct[1:]
    for j in range(K - 1):
        EZZ[j + 2, j + 2] = q[j + 1]
    EZY = np.zeros(dim)
    EZY[0] = ss.E_Y
    EZY[1] = ss.E_TY
    EZY[2:] = cy[1:]
    try:
        return np.linalg.solve(EZZ, EZY)
    except np.linalg.LinAlgError:
        return np.full(dim, np.nan)


def plim_ols_exposure(C, ss):
    K = ss.K
    q = C @ ss.p_A
    cy = C @ ss.E_YD
    dim = K
    EZZ = np.zeros((dim, dim))
    EZZ[0, 0] = 1.0
    EZZ[0, 1:] = q[1:]
    EZZ[1:, 0] = q[1:]
    for j in range(K - 1):
        EZZ[j + 1, j + 1] = q[j + 1]
    EZY = np.zeros(dim)
    EZY[0] = ss.E_Y
    EZY[1:] = cy[1:]
    try:
        return np.linalg.solve(EZZ, EZY)
    except np.linalg.LinAlgError:
        return np.full(dim, np.nan)


def plim_iv_single(C, ss):
    FS_star = C @ ss.FS
    if abs(FS_star[1]) < 1e-8:
        return np.nan
    return ss.RF / FS_star[1]


def get_tau_at_C(topo, C, ss):
    if topo == 'iv':
        return plim_iv_single(C, ss)
    elif topo == 'exposure':
        return plim_ols_exposure(C, ss)[1]
    else:
        return plim_ols_with_T(C, ss)[1]


def get_tau_true(topo, K, params, ss):
    """True causal parameter for Conjecture 1.

    For correctly-identified topologies: tau_true = plim(I).
    For protective topologies (collider, mbias): tau_true = DGP tau,
    so B(0) = plim(I) - tau != 0 (Berkson/M-bias at perfect classification).
    """
    p = params[topo]
    if topo == 'collider':
        return p['tau']
    elif topo == 'mbias':
        return p['tau']
    else:
        return get_tau_at_C(topo, np.eye(K), ss)


# ====================================================================
# Batched bias curve computation
# ====================================================================
def compute_bias_curve(topo, C0, ss, tau_true, delta_step=DELTA_STEP):
    K = C0.shape[0]
    min_diag = np.diag(C0).min()
    if min_diag >= 1.0:
        delta_max = 10.0
    else:
        delta_max = min(1.0 / (1.0 - min_diag), 10.0)

    deltas = np.arange(0, delta_max + delta_step / 2, delta_step)
    n = len(deltas)
    d = deltas[:, None]

    if topo == 'iv':
        FS0 = C0 @ ss.FS
        fs_star = (1 - d) * ss.FS[None, :] + d * FS0[None, :]
        denom = fs_star[:, 1]
        taus = np.where(np.abs(denom) < 1e-8, np.nan, ss.RF / denom)
    elif topo == 'exposure':
        pA0 = C0 @ ss.p_A
        YD0 = C0 @ ss.E_YD
        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]
        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]
        dim = K
        EZZ = np.zeros((n, dim, dim))
        EZZ[:, 0, 0] = 1.0
        EZZ[:, 0, 1:] = q[:, 1:]
        EZZ[:, 1:, 0] = q[:, 1:]
        for j in range(K - 1):
            EZZ[:, j + 1, j + 1] = q[:, j + 1]
        EZY = np.zeros((n, dim))
        EZY[:, 0] = ss.E_Y
        EZY[:, 1:] = cy[:, 1:]
        try:
            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]
            taus = coefs[:, 1]
        except np.linalg.LinAlgError:
            taus = np.full(n, np.nan)
    else:
        pA0 = C0 @ ss.p_A
        TD0 = C0 @ ss.E_TD
        YD0 = C0 @ ss.E_YD
        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]
        ct = (1 - d) * ss.E_TD[None, :] + d * TD0[None, :]
        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]
        dim = K + 1
        EZZ = np.zeros((n, dim, dim))
        EZZ[:, 0, 0] = 1.0
        EZZ[:, 0, 1] = ss.E_T
        EZZ[:, 1, 0] = ss.E_T
        EZZ[:, 1, 1] = ss.E_T2
        EZZ[:, 0, 2:] = q[:, 1:]
        EZZ[:, 2:, 0] = q[:, 1:]
        EZZ[:, 1, 2:] = ct[:, 1:]
        EZZ[:, 2:, 1] = ct[:, 1:]
        for j in range(K - 1):
            EZZ[:, j + 2, j + 2] = q[:, j + 1]
        EZY = np.zeros((n, dim))
        EZY[:, 0] = ss.E_Y
        EZY[:, 1] = ss.E_TY
        EZY[:, 2:] = cy[:, 1:]
        try:
            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]
            taus = coefs[:, 1]
        except np.linalg.LinAlgError:
            taus = np.full(n, np.nan)

    bias_abs = np.abs(taus - tau_true)
    return deltas, bias_abs


def check_monotonicity(bias_abs, topo, tol=MONO_TOL):
    valid = ~np.isnan(bias_abs)
    ba = bias_abs[valid]
    if len(ba) < 2:
        return 0
    diffs = np.diff(ba)
    if topo in NON_DECREASING:
        return int(np.sum(diffs < -tol))
    else:
        return int(np.sum(diffs > tol))


# ====================================================================
# Precompute sufficient statistics
# ====================================================================
def precompute_all():
    print("\nPrecomputing sufficient statistics (N={:,})...".format(N_LARGE))
    sys.stdout.flush()
    t0 = time.time()
    all_ss = {}
    all_tau_true = {}

    for K in K_VALUES:
        params = make_all_params(K)
        for topo in ALL_TOPOS:
            rng = np.random.default_rng(SEED + K * 100 + TOPO_IDX[topo])
            p = params[topo]
            if topo == 'iv':
                Z, Y, A = gen_iv(K, N_LARGE, p, rng)
                ss = IVSuffStats(Z, Y, A, K)
                del Z, Y, A
            elif topo == 'exposure':
                _, Y, A = gen_exposure(K, N_LARGE, p, rng)
                ss = SuffStats(None, Y, A, K)
                del Y, A
            else:
                T, Y, A = _GEN[topo](K, N_LARGE, p, rng)
                ss = SuffStats(T, Y, A, K)
                del T, Y, A

            tau_true = get_tau_true(topo, K, params, ss)
            all_ss[(topo, K)] = ss
            all_tau_true[(topo, K)] = tau_true

    print("  Done ({:.1f}s). tau_true samples:".format(time.time() - t0))
    for topo in ALL_TOPOS:
        vals = [all_tau_true[(topo, K)] for K in K_VALUES]
        vals_s = ", ".join(
            f"K{K}={v:.6f}" if v is not None and not np.isnan(v) else f"K{K}=NaN"
            for K, v in zip(K_VALUES, vals))
        direction = "non-dec" if topo in NON_DECREASING else "non-inc"
        print(f"    {topo:<14} [{direction}] {vals_s}")
    sys.stdout.flush()
    return all_ss, all_tau_true


# ====================================================================
# Part 1: Random Verification
# ====================================================================
def part1_random(all_ss, all_tau_true):
    print("\n" + "=" * 70)
    print("PART 1: Random Verification ({:,} C0 per topology x K)".format(N_RANDOM))
    print("=" * 70)
    sys.stdout.flush()

    results = {}
    total_tests = 0
    total_violations = 0

    for K in K_VALUES:
        print(f"\n  K = {K}")
        print(f"  {'Topology':<14} {'Direction':<10} {'Tested':>8} "
              f"{'Violations':>11} {'NaN_curves':>11} {'Time':>7}")
        print(f"  {'-' * 65}")
        sys.stdout.flush()

        for topo in ALL_TOPOS:
            t0 = time.time()
            ss = all_ss[(topo, K)]
            tau_true = all_tau_true[(topo, K)]

            rng_C = np.random.default_rng(SEED * 2 + K * 1000 + TOPO_IDX[topo])
            violations = 0
            nan_curves = 0
            worst_mag = 0.0

            for i in range(N_RANDOM):
                C0 = np.zeros((K, K))
                for j in range(K):
                    C0[:, j] = rng_C.dirichlet(np.ones(K))

                _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true)

                n_nan = np.isnan(bias_abs).sum()
                if n_nan > len(bias_abs) * 0.5:
                    nan_curves += 1
                    continue

                n_viol = check_monotonicity(bias_abs, topo)
                if n_viol > 0:
                    violations += 1
                    valid = ~np.isnan(bias_abs)
                    ba = bias_abs[valid]
                    diffs = np.diff(ba)
                    if topo in NON_DECREASING:
                        worst_mag = max(worst_mag, abs(diffs.min()))
                    else:
                        worst_mag = max(worst_mag, diffs.max())

            elapsed = time.time() - t0
            direction = "non-dec" if topo in NON_DECREASING else "non-inc"
            print(f"  {topo:<14} {direction:<10} {N_RANDOM:>8} "
                  f"{violations:>11} {nan_curves:>11} {elapsed:>6.1f}s")
            sys.stdout.flush()

            results[f"{topo}_K{K}"] = {
                "n_tested": N_RANDOM,
                "violations": violations,
                "nan_curves": nan_curves,
                "direction": direction,
                "worst_violation_magnitude": float(worst_mag),
                "tau_true": float(tau_true) if not np.isnan(tau_true) else None,
            }
            total_tests += N_RANDOM
            total_violations += violations

    print(f"\n  Grand total: {total_tests:,} tests, {total_violations} violations")
    return results


# ====================================================================
# Part 2: Adversarial Search
# ====================================================================
def part2_adversarial(all_ss, all_tau_true):
    print("\n" + "=" * 70)
    print(f"PART 2: Adversarial Search ({ADV_N_STARTS} starts x "
          f"{len(ADV_DELTA_PAIRS)} delta-pairs)")
    print("=" * 70)
    sys.stdout.flush()

    results = {}

    for K in K_ADVERSARIAL:
        print(f"\n  K = {K}")
        print(f"  {'Topology':<14} {'Direction':<10} {'best_obj':>11} "
              f"{'Counterex':>11} {'Time':>7}")
        print(f"  {'-' * 57}")
        sys.stdout.flush()

        for topo in ALL_TOPOS:
            t0 = time.time()
            ss = all_ss[(topo, K)]
            tau_true = all_tau_true[(topo, K)]

            best_objective = np.inf
            found_counterexample = False
            rng_adv = np.random.default_rng(
                SEED * 3 + K * 10000 + TOPO_IDX[topo] * 100)

            for d1, d2 in ADV_DELTA_PAIRS:
                for _ in range(ADV_N_STARTS):
                    theta0 = rng_adv.normal(0, 1, K * K)

                    def objective(theta, _topo=topo, _ss=ss, _tt=tau_true,
                                  _d1=d1, _d2=d2, _K=K):
                        logits = theta.reshape(_K, _K)
                        exp_l = np.exp(logits - logits.max(axis=0, keepdims=True))
                        C0 = exp_l / exp_l.sum(axis=0, keepdims=True)

                        C1 = (1 - _d1) * np.eye(_K) + _d1 * C0
                        C2 = (1 - _d2) * np.eye(_K) + _d2 * C0

                        tau1 = get_tau_at_C(_topo, C1, _ss)
                        tau2 = get_tau_at_C(_topo, C2, _ss)

                        if np.isnan(tau1) or np.isnan(tau2):
                            return 0.0

                        b1_sq = (tau1 - _tt) ** 2
                        b2_sq = (tau2 - _tt) ** 2

                        if _topo in NON_DECREASING:
                            return b2_sq - b1_sq
                        else:
                            return b1_sq - b2_sq

                    res = scipy_minimize(objective, theta0, method='L-BFGS-B',
                                         options={'maxiter': 100, 'ftol': 1e-12})

                    if res.fun < best_objective:
                        best_objective = res.fun

                    if res.fun < -1e-6:
                        found_counterexample = True

            elapsed = time.time() - t0
            direction = "non-dec" if topo in NON_DECREASING else "non-inc"
            ce_str = "YES!" if found_counterexample else "no"
            print(f"  {topo:<14} {direction:<10} {best_objective:>11.6f} "
                  f"{ce_str:>11} {elapsed:>6.1f}s")
            sys.stdout.flush()

            results[f"{topo}_K{K}"] = {
                "n_starts": ADV_N_STARTS * len(ADV_DELTA_PAIRS),
                "best_objective": float(best_objective),
                "found_counterexample": found_counterexample,
                "delta_pairs": [[d1, d2] for d1, d2 in ADV_DELTA_PAIRS],
            }

    return results


# ====================================================================
# Main
# ====================================================================
def main():
    t_total = time.time()
    print("Exp-D: Conjecture 1 Extended Verification")
    print(f"  Random: {N_RANDOM:,} C0 x 7 topologies x K in {K_VALUES}")
    print(f"  Adversarial: {ADV_N_STARTS} starts x {len(ADV_DELTA_PAIRS)} "
          f"delta-pairs x K in {K_ADVERSARIAL}")
    print(f"  N_large={N_LARGE:,}, delta_step={DELTA_STEP}, seed={SEED}")
    sys.stdout.flush()

    all_ss, all_tau_true = precompute_all()

    random_results = part1_random(all_ss, all_tau_true)
    adversarial_results = part2_adversarial(all_ss, all_tau_true)

    # Build output
    total_random = sum(r['n_tested'] for r in random_results.values())
    total_viol = sum(r['violations'] for r in random_results.values())
    total_ce = sum(1 for r in adversarial_results.values()
                   if r['found_counterexample'])

    if total_viol == 0 and total_ce == 0:
        summary = (f"Zero violations across {total_random:,} random tests + "
                   f"0 counterexamples found by adversarial search")
    else:
        summary = (f"{total_viol} violations across {total_random:,} random tests + "
                   f"{total_ce} counterexamples found by adversarial search")

    output = {"random_verification": {}, "adversarial_search": {}, "summary": summary}

    for topo in ALL_TOPOS:
        rv = {}
        for K in K_VALUES:
            key = f"{topo}_K{K}"
            if key in random_results:
                rv[f"K{K}"] = random_results[key]
        output["random_verification"][topo] = rv

    for topo in ALL_TOPOS:
        av = {}
        for K in K_ADVERSARIAL:
            key = f"{topo}_K{K}"
            if key in adversarial_results:
                av[f"K{K}"] = adversarial_results[key]
        output["adversarial_search"][topo] = av

    out_path = os.path.join(OUT_DIR, 'exp_d_conjecture_results.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nJSON -> {out_path}")

    total_time = time.time() - t_total
    print(f"\n{summary}")
    print(f"Total time: {total_time:.0f}s ({total_time/60:.1f}min)")


if __name__ == "__main__":
    main()
