#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plan 008: Binarization Collapse Bias Analysis

Tests whether folding K=3 LLM annotation to binary is safe across 6 DAG topologies.
For each DAG: K=3 bias, K=2 bias (3 folds), Delta = |K3 - K2|.
Random search: 100k Dirichlet(1,1,1) confusion matrices per topology.

Method: pre-compute sufficient statistics from large-sample DGP, then compute
plim as a function of C via moment algebra (no per-C simulation needed).
"""

import numpy as np
from collections import OrderedDict
import time
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# Configuration
# ============================================================
N_LARGE = 5_000_000
N_RANDOM = 100_000
SEED_DGP = 42
SEED_RSEARCH = 123

# Named confusion matrices (column-stochastic)
C_DICT = OrderedDict([
    ("C1_sym_high",    np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),
    ("C2_asymmetric",  np.array([[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]])),
    ("C3_struct_12",   np.array([[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]])),
    ("C4_weak_diag",   np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]])),
    ("C5_near_perm",   np.array([[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]])),
    ("C6_differential",np.array([[.85,.15,.05],[.075,.70,.05],[.075,.15,.90]])),
])

# ============================================================
# DGP Parameters
# ============================================================
P_A = np.array([0.4, 0.35, 0.25])

# Confounding: A->T, A->Y, T->Y
CONF = dict(alpha=np.array([1.5, -1.0]), beta_T=2.0,
            beta_A=np.array([1.0, -0.5]), sigma_T=1.0)

# Exposure: A->Y
EXP_BETA = np.array([0.0, 1.0, -0.5])

# Mediation: T->A->Y
MED = dict(tau=0.5, gamma=np.array([0.0, 0.5, -0.3]),
           delta=np.array([0.0, 0.8, -0.6]),
           beta=np.array([0.0, 1.0, -0.5]))

# Collider: T->A<-Y
COLL = dict(tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)

# M-bias: U1->{A,T}, U2->{A,Y}
MBIAS = dict(tau=1.0, delta=1.0, lam=1.0,
             g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)

# IV: Z->A->Y, U->A, U->Y
IV = dict(dZ=1.5, dU=0.5, dZ2=-1.0, dU2=-0.3, lam=0.8,
          beta=np.array([0.0, 1.0, -0.5]))


# ============================================================
# Utilities
# ============================================================
def softmax_vec(x):
    e = np.exp(x - x.max())
    return e / e.sum()


def softmax_sample(logits, rng):
    e = np.exp(logits - logits.max(axis=1, keepdims=True))
    p = e / e.sum(axis=1, keepdims=True)
    cu = np.cumsum(p, axis=1)
    u = rng.uniform(size=logits.shape[0])
    return (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)


def fold_C_to_binary(C, p_A, keep_k):
    """Fold 3x3 C to 2x2 by isolating category keep_k as B=1."""
    merge = [j for j in range(3) if j != keep_k]
    p_merge = sum(p_A[j] for j in merge)
    c11 = C[keep_k, keep_k]
    c01 = 1 - c11
    c10 = sum(C[keep_k, j] * p_A[j] for j in merge) / p_merge if p_merge > 0 else 0
    c00 = 1 - c10
    C_bin = np.array([[c00, c01], [c10, c11]])
    p_bin = np.array([p_merge, p_A[keep_k]])
    return C_bin, p_bin


# ============================================================
# DGP Generators
# ============================================================
def gen_confounding(N, rng):
    A = rng.choice(3, size=N, p=P_A)
    D1 = (A == 1).astype(float)
    D2 = (A == 2).astype(float)
    T = CONF['alpha'][0]*D1 + CONF['alpha'][1]*D2 + rng.normal(0, CONF['sigma_T'], N)
    Y = CONF['beta_T']*T + CONF['beta_A'][0]*D1 + CONF['beta_A'][1]*D2 + rng.normal(0, 1, N)
    return T, Y, A


def gen_exposure(N, rng):
    A = rng.choice(3, size=N, p=P_A)
    D1 = (A == 1).astype(float)
    D2 = (A == 2).astype(float)
    Y = EXP_BETA[0] + EXP_BETA[1]*D1 + EXP_BETA[2]*D2 + rng.normal(0, 1, N)
    return None, Y, A


def gen_mediation(N, rng):
    T = rng.binomial(1, 0.5, N).astype(float)
    p0 = softmax_vec(MED['gamma'] + MED['delta'] * 0)
    p1 = softmax_vec(MED['gamma'] + MED['delta'] * 1)
    pr = np.where(T[:, None] == 0, p0, p1)
    cu = np.cumsum(pr, axis=1)
    u = rng.uniform(size=N)
    A = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
    D1 = (A == 1).astype(float)
    D2 = (A == 2).astype(float)
    Y = MED['beta'][0] + MED['beta'][1]*D1 + MED['beta'][2]*D2 + MED['tau']*T + rng.normal(0, 1, N)
    return T, Y, A


def gen_collider(N, rng):
    T = rng.normal(0, 1, N)
    Y = COLL['tau']*T + rng.normal(0, 1, N)
    logits = np.column_stack([
        np.zeros(N),
        COLL['g1'] + COLL['dT']*T + COLL['dY']*Y,
        COLL['g2'] + COLL['dT2']*T + COLL['dY2']*Y,
    ])
    A = softmax_sample(logits, rng)
    return T, Y, A


def gen_mbias(N, rng):
    U1 = rng.normal(0, 1, N)
    U2 = rng.normal(0, 1, N)
    T = MBIAS['delta']*U1 + rng.normal(0, 1, N)
    Y = MBIAS['tau']*T + MBIAS['lam']*U2 + rng.normal(0, 1, N)
    logits = np.column_stack([
        np.zeros(N),
        MBIAS['g1'] + MBIAS['a1']*U1 + MBIAS['a3']*U2,
        MBIAS['g2'] + MBIAS['a2']*U1 + MBIAS['a4']*U2,
    ])
    A = softmax_sample(logits, rng)
    return T, Y, A


def gen_iv(N, rng):
    Z = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    logits = np.column_stack([
        np.zeros(N),
        IV['dZ']*Z + IV['dU']*U,
        IV['dZ2']*Z + IV['dU2']*U,
    ])
    A = softmax_sample(logits, rng)
    D1 = (A == 1).astype(float)
    D2 = (A == 2).astype(float)
    Y = IV['beta'][1]*D1 + IV['beta'][2]*D2 + IV['lam']*U + rng.normal(0, 1, N)
    return None, Y, A


# ============================================================
# Sufficient Statistics
# ============================================================
class Stats:
    """Pre-computed moments for O(1) plim calculation over arbitrary C."""

    def __init__(self, T, Y, A, tau_true, has_T=True):
        self.has_T = has_T
        self.tau_true = tau_true
        N = len(Y)
        if has_T:
            self.ET = T.mean()
            self.ET2 = (T**2).mean()
            self.ETY = (T * Y).mean()
        self.EY = Y.mean()
        self.p = np.zeros(3)
        self.ETD = np.zeros(3)
        self.EYD = np.zeros(3)
        for j in range(3):
            m = (A == j).astype(float)
            self.p[j] = m.mean()
            if has_T:
                self.ETD[j] = (T * m).mean()
            self.EYD[j] = (Y * m).mean()

    def tau_k3(self, C):
        """tau from Y ~ 1 + T + D*_1 + D*_2."""
        q = C @ self.p
        ETDs = C @ self.ETD
        EYDs = C @ self.EYD
        EZZ = np.array([
            [1,       self.ET,  q[1],    q[2]],
            [self.ET, self.ET2, ETDs[1], ETDs[2]],
            [q[1],    ETDs[1],  q[1],    0],
            [q[2],    ETDs[2],  0,       q[2]],
        ])
        EZY = np.array([self.EY, self.ETY, EYDs[1], EYDs[2]])
        return np.linalg.solve(EZZ, EZY)[1]

    def tau_k2(self, C, fold):
        """tau from Y ~ 1 + T + D*_fold."""
        q_k = (C @ self.p)[fold]
        ETDs_k = (C @ self.ETD)[fold]
        EYDs_k = (C @ self.EYD)[fold]
        EZZ = np.array([
            [1,       self.ET,  q_k],
            [self.ET, self.ET2, ETDs_k],
            [q_k,     ETDs_k,  q_k],
        ])
        EZY = np.array([self.EY, self.ETY, EYDs_k])
        return np.linalg.solve(EZZ, EZY)[1]

    def gamma_k3(self, C):
        """(g0, g1, g2) from Y ~ 1 + D*_1 + D*_2 (exposure-type)."""
        q = C @ self.p
        EYDs = C @ self.EYD
        EZZ = np.array([
            [1,    q[1], q[2]],
            [q[1], q[1], 0],
            [q[2], 0,    q[2]],
        ])
        EZY = np.array([self.EY, EYDs[1], EYDs[2]])
        return np.linalg.solve(EZZ, EZY)

    def gamma_k2(self, C, fold):
        """(g0, gB) from Y ~ 1 + D*_fold (exposure-type)."""
        q_k = (C @ self.p)[fold]
        EYDs_k = (C @ self.EYD)[fold]
        EZZ = np.array([[1, q_k], [q_k, q_k]])
        EZY = np.array([self.EY, EYDs_k])
        return np.linalg.solve(EZZ, EZY)


# ============================================================
# Vectorized random search (DAGs with T)
# ============================================================
def rand_search_tau(ss, n_random=N_RANDOM, seed=SEED_RSEARCH):
    rng = np.random.default_rng(seed)
    C_all = np.zeros((n_random, 3, 3))
    for col in range(3):
        C_all[:, :, col] = rng.dirichlet([1, 1, 1], size=n_random)

    q = np.einsum('nkj,j->nk', C_all, ss.p)
    ETDs = np.einsum('nkj,j->nk', C_all, ss.ETD)
    EYDs = np.einsum('nkj,j->nk', C_all, ss.EYD)

    # K=3: batch 4x4 solve
    EZZ = np.zeros((n_random, 4, 4))
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1] = EZZ[:, 1, 0] = ss.ET
    EZZ[:, 0, 2] = EZZ[:, 2, 0] = q[:, 1]
    EZZ[:, 0, 3] = EZZ[:, 3, 0] = q[:, 2]
    EZZ[:, 1, 1] = ss.ET2
    EZZ[:, 1, 2] = EZZ[:, 2, 1] = ETDs[:, 1]
    EZZ[:, 1, 3] = EZZ[:, 3, 1] = ETDs[:, 2]
    EZZ[:, 2, 2] = q[:, 1]
    EZZ[:, 3, 3] = q[:, 2]

    EZY = np.zeros((n_random, 4))
    EZY[:, 0] = ss.EY
    EZY[:, 1] = ss.ETY
    EZY[:, 2] = EYDs[:, 1]
    EZY[:, 3] = EYDs[:, 2]

    try:
        plim_k3 = np.linalg.solve(EZZ, EZY[..., np.newaxis]).squeeze(-1)
        tau_k3 = plim_k3[:, 1]
    except np.linalg.LinAlgError:
        tau_k3 = np.full(n_random, np.nan)
        for i in range(n_random):
            try:
                tau_k3[i] = np.linalg.solve(EZZ[i], EZY[i])[1]
            except:
                tau_k3[i] = np.nan

    # K=2: batch 3x3 solve for each fold
    tau_k2 = np.zeros((n_random, 3))
    for fold in range(3):
        EZZ2 = np.zeros((n_random, 3, 3))
        EZZ2[:, 0, 0] = 1.0
        EZZ2[:, 0, 1] = EZZ2[:, 1, 0] = ss.ET
        EZZ2[:, 0, 2] = EZZ2[:, 2, 0] = q[:, fold]
        EZZ2[:, 1, 1] = ss.ET2
        EZZ2[:, 1, 2] = EZZ2[:, 2, 1] = ETDs[:, fold]
        EZZ2[:, 2, 2] = q[:, fold]
        EZY2 = np.zeros((n_random, 3))
        EZY2[:, 0] = ss.EY
        EZY2[:, 1] = ss.ETY
        EZY2[:, 2] = EYDs[:, fold]
        try:
            plim_k2 = np.linalg.solve(EZZ2, EZY2[..., np.newaxis]).squeeze(-1)
            tau_k2[:, fold] = plim_k2[:, 1]
        except np.linalg.LinAlgError:
            for i in range(n_random):
                try:
                    tau_k2[i, fold] = np.linalg.solve(EZZ2[i], EZY2[i])[1]
                except:
                    tau_k2[i, fold] = np.nan

    delta_per_fold = np.abs(tau_k3[:, None] - tau_k2)
    delta_max = np.nanmax(delta_per_fold, axis=1)
    valid = np.isfinite(delta_max)
    dm = delta_max[valid]

    bias_k3 = tau_k3 - ss.tau_true
    sign_flip = np.any(np.sign(tau_k3[:, None]) != np.sign(tau_k2), axis=1)

    return {
        'delta_mean': dm.mean(), 'delta_median': np.median(dm),
        'delta_p95': np.percentile(dm, 95), 'delta_max': dm.max(),
        'frac_gt_001': (dm > 0.01).mean(), 'frac_gt_005': (dm > 0.05).mean(),
        'sign_flip_rate': sign_flip[valid].mean(), 'n_valid': int(valid.sum()),
    }


# ============================================================
# Vectorized random search (exposure / IV)
# ============================================================
def rand_search_gamma(ss, gamma_ref_k3, gamma_ref_k2, n_random=N_RANDOM, seed=SEED_RSEARCH):
    """Random search for exposure-type DAGs.
    gamma_ref_k3: plim with C=I (3-vector)
    gamma_ref_k2: dict {fold: plim with C=I (2-vector)}
    """
    rng = np.random.default_rng(seed)
    C_all = np.zeros((n_random, 3, 3))
    for col in range(3):
        C_all[:, :, col] = rng.dirichlet([1, 1, 1], size=n_random)

    q = np.einsum('nkj,j->nk', C_all, ss.p)
    EYDs = np.einsum('nkj,j->nk', C_all, ss.EYD)

    # K=3: batch 3x3
    EZZ = np.zeros((n_random, 3, 3))
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1] = EZZ[:, 1, 0] = q[:, 1]
    EZZ[:, 0, 2] = EZZ[:, 2, 0] = q[:, 2]
    EZZ[:, 1, 1] = q[:, 1]
    EZZ[:, 2, 2] = q[:, 2]
    EZY = np.zeros((n_random, 3))
    EZY[:, 0] = ss.EY
    EZY[:, 1] = EYDs[:, 1]
    EZY[:, 2] = EYDs[:, 2]

    try:
        plim_k3 = np.linalg.solve(EZZ, EZY[..., np.newaxis]).squeeze(-1)
    except np.linalg.LinAlgError:
        plim_k3 = np.full((n_random, 3), np.nan)
        for i in range(n_random):
            try: plim_k3[i] = np.linalg.solve(EZZ[i], EZY[i])
            except: pass

    # K=3 misclassification bias on components 1,2
    dbias_k3 = plim_k3[:, 1:] - gamma_ref_k3[1:]  # (N, 2)

    # K=2 for folds 1 and 2
    dbias_k2 = np.zeros((n_random, 2))
    for fi, fold in enumerate([1, 2]):
        EZZ2 = np.zeros((n_random, 2, 2))
        EZZ2[:, 0, 0] = 1.0
        EZZ2[:, 0, 1] = EZZ2[:, 1, 0] = q[:, fold]
        EZZ2[:, 1, 1] = q[:, fold]
        EZY2 = np.zeros((n_random, 2))
        EZY2[:, 0] = ss.EY
        EZY2[:, 1] = EYDs[:, fold]
        try:
            plim_k2 = np.linalg.solve(EZZ2, EZY2[..., np.newaxis]).squeeze(-1)
            dbias_k2[:, fi] = plim_k2[:, 1] - gamma_ref_k2[fold][1]
        except np.linalg.LinAlgError:
            for i in range(n_random):
                try:
                    dbias_k2[i, fi] = np.linalg.solve(EZZ2[i], EZY2[i])[1] - gamma_ref_k2[fold][1]
                except:
                    dbias_k2[i, fi] = np.nan

    delta_diff = np.abs(dbias_k3 - dbias_k2)
    delta_max = np.nanmax(delta_diff, axis=1)
    valid = np.isfinite(delta_max)
    dm = delta_max[valid]

    sf = np.any(np.sign(dbias_k3) != np.sign(dbias_k2), axis=1)

    return {
        'delta_mean': dm.mean(), 'delta_median': np.median(dm),
        'delta_p95': np.percentile(dm, 95), 'delta_max': dm.max(),
        'frac_gt_001': (dm > 0.01).mean(), 'frac_gt_005': (dm > 0.05).mean(),
        'sign_flip_rate': sf[valid].mean(), 'n_valid': int(valid.sum()),
    }


# ============================================================
# Main
# ============================================================
def main():
    t0 = time.time()
    np.set_printoptions(precision=4, suppress=True)

    print("=" * 90)
    print("Plan 008: Binarization Collapse Bias Analysis")
    print(f"  K=3 vs K=2 annotation folding | N_large={N_LARGE//10**6}M, N_random={N_RANDOM//1000}k")
    print("=" * 90)

    all_results = OrderedDict()
    I3 = np.eye(3)

    # =============================================
    # PART 1: DAGs with T (clean tau comparison)
    # =============================================
    tau_dags = OrderedDict([
        ("confounding", (gen_confounding, CONF['beta_T'],
                         f"A->T, A->Y, T->Y | alpha={CONF['alpha']}, beta_A={CONF['beta_A']}")),
        ("mediation",   (gen_mediation,   MED['tau'],
                         f"T->A->Y | gamma={MED['gamma']}, delta={MED['delta']}")),
        ("collider",    (gen_collider,    COLL['tau'],
                         f"T->A<-Y | dT={COLL['dT']}, dY={COLL['dY']}")),
        ("M-bias",      (gen_mbias,       MBIAS['tau'],
                         f"U1->{{A,T}}, U2->{{A,Y}} | delta={MBIAS['delta']}, lam={MBIAS['lam']}")),
    ])

    for dag_name, (gen_fn, tau_true, desc) in tau_dags.items():
        print(f"\n{'='*90}")
        print(f"  {dag_name.upper()} DAG  |  tau_true = {tau_true}")
        print(f"  {desc}")
        print(f"{'='*90}")

        t1 = time.time()
        rng = np.random.default_rng(SEED_DGP)
        T, Y, A = gen_fn(N_LARGE, rng)
        ss = Stats(T, Y, A, tau_true, has_T=True)
        print(f"  Stats ({time.time()-t1:.1f}s) | P(A)=[{ss.p[0]:.3f},{ss.p[1]:.3f},{ss.p[2]:.3f}]")

        # Verify: tau with C=I should match tau_true
        tau_clean = ss.tau_k3(I3)
        print(f"  Sanity: tau(C=I)={tau_clean:.4f} (true={tau_true})")

        # Named C
        print(f"\n  {'C':<16} {'tau_K3':>8} {'bias_K3':>8}"
              f" {'tau_f0':>8} {'tau_f1':>8} {'tau_f2':>8}"
              f" {'D_max':>7} {'worst':>5}")
        print(f"  {'-'*80}")

        for cn, C in C_DICT.items():
            tk3 = ss.tau_k3(C)
            tk2 = [ss.tau_k2(C, k) for k in range(3)]
            bk3 = tk3 - tau_true
            deltas = [abs(tk3 - tk2[k]) for k in range(3)]
            d_max = max(deltas)
            worst = int(np.argmax(deltas))
            print(f"  {cn:<16} {tk3:>8.4f} {bk3:>+8.4f}"
                  f" {tk2[0]:>8.4f} {tk2[1]:>8.4f} {tk2[2]:>8.4f}"
                  f" {d_max:>7.4f} {worst:>5}")

        # Folded 2x2 C for one example
        print(f"\n  Folded 2x2 (C1_sym_high, each fold):")
        C_ex = C_DICT["C1_sym_high"]
        for k in range(3):
            Cb, pb = fold_C_to_binary(C_ex, ss.p, k)
            Se, Sp = Cb[1,1], Cb[0,0]
            print(f"    fold={k}: Se={Se:.3f} Sp={Sp:.3f} atten={Se+Sp-1:.3f}"
                  f"  C_bin=[[{Cb[0,0]:.3f},{Cb[0,1]:.3f}],[{Cb[1,0]:.3f},{Cb[1,1]:.3f}]]")

        # Random search
        t1 = time.time()
        rs = rand_search_tau(ss)
        t2 = time.time()
        print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s):")
        print(f"    Delta: mean={rs['delta_mean']:.4f} med={rs['delta_median']:.4f}"
              f" P95={rs['delta_p95']:.4f} max={rs['delta_max']:.4f}")
        print(f"    Delta>0.01: {rs['frac_gt_001']:.1%}  Delta>0.05: {rs['frac_gt_005']:.1%}")
        print(f"    sign_flip: {rs['sign_flip_rate']:.1%}  valid: {rs['n_valid']}/{N_RANDOM}")

        all_results[dag_name] = rs

    # =============================================
    # PART 2: Exposure DAG
    # =============================================
    print(f"\n{'='*90}")
    print(f"  EXPOSURE DAG  |  beta = {EXP_BETA}")
    print(f"  A->Y, A->A* | P(A)={P_A}")
    print(f"{'='*90}")

    t1 = time.time()
    rng = np.random.default_rng(SEED_DGP)
    _, Y, A = gen_exposure(N_LARGE, rng)
    ss_exp = Stats(None, Y, A, None, has_T=False)
    print(f"  Stats ({time.time()-t1:.1f}s)")

    gamma_ref_k3 = ss_exp.gamma_k3(I3)
    gamma_ref_k2 = {k: ss_exp.gamma_k2(I3, k) for k in range(3)}
    print(f"  Clean K3: gamma={gamma_ref_k3}")
    for k in [1, 2]:
        print(f"  Clean K2 fold={k}: gamma_B={gamma_ref_k2[k][1]:.4f}")

    print(f"\n  {'C':<16} {'g1_K3':>8} {'g2_K3':>8}"
          f" {'gB_f1':>8} {'gB_f2':>8}"
          f" {'D1':>7} {'D2':>7} {'D_max':>7}")
    print(f"  {'-'*78}")

    for cn, C in C_DICT.items():
        gk3 = ss_exp.gamma_k3(C)
        gk2_1 = ss_exp.gamma_k2(C, 1)
        gk2_2 = ss_exp.gamma_k2(C, 2)
        d_k3_1 = gk3[1] - gamma_ref_k3[1]
        d_k3_2 = gk3[2] - gamma_ref_k3[2]
        d_k2_1 = gk2_1[1] - gamma_ref_k2[1][1]
        d_k2_2 = gk2_2[1] - gamma_ref_k2[2][1]
        delta_1 = abs(d_k3_1 - d_k2_1)
        delta_2 = abs(d_k3_2 - d_k2_2)
        d_max = max(delta_1, delta_2)
        print(f"  {cn:<16} {gk3[1]:>8.4f} {gk3[2]:>8.4f}"
              f" {gk2_1[1]:>8.4f} {gk2_2[1]:>8.4f}"
              f" {delta_1:>7.4f} {delta_2:>7.4f} {d_max:>7.4f}")

    t1 = time.time()
    rs_exp = rand_search_gamma(ss_exp, gamma_ref_k3, gamma_ref_k2)
    t2 = time.time()
    print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s):")
    print(f"    Delta: mean={rs_exp['delta_mean']:.4f} med={rs_exp['delta_median']:.4f}"
          f" P95={rs_exp['delta_p95']:.4f} max={rs_exp['delta_max']:.4f}")
    print(f"    Delta>0.01: {rs_exp['frac_gt_001']:.1%}  Delta>0.05: {rs_exp['frac_gt_005']:.1%}")
    print(f"    sign_flip: {rs_exp['sign_flip_rate']:.1%}  valid: {rs_exp['n_valid']}/{N_RANDOM}")
    all_results['exposure'] = rs_exp

    # =============================================
    # PART 3: IV DAG (OLS comparison)
    # =============================================
    print(f"\n{'='*90}")
    print(f"  IV DAG  |  beta = {IV['beta']}, lambda = {IV['lam']}")
    print(f"  Z->A->Y, U->A, U->Y | OLS comparison (biased by confounding)")
    print(f"{'='*90}")

    t1 = time.time()
    rng = np.random.default_rng(SEED_DGP)
    _, Y_iv, A_iv = gen_iv(N_LARGE, rng)
    ss_iv = Stats(None, Y_iv, A_iv, None, has_T=False)
    print(f"  Stats ({time.time()-t1:.1f}s)")

    gamma_ref_k3_iv = ss_iv.gamma_k3(I3)
    gamma_ref_k2_iv = {k: ss_iv.gamma_k2(I3, k) for k in range(3)}
    print(f"  Clean K3 (OLS, biased by U): gamma={gamma_ref_k3_iv}")

    print(f"\n  {'C':<16} {'g1_K3':>8} {'g2_K3':>8}"
          f" {'gB_f1':>8} {'gB_f2':>8}"
          f" {'D1':>7} {'D2':>7} {'D_max':>7}")
    print(f"  {'-'*78}")

    for cn, C in C_DICT.items():
        gk3 = ss_iv.gamma_k3(C)
        gk2_1 = ss_iv.gamma_k2(C, 1)
        gk2_2 = ss_iv.gamma_k2(C, 2)
        d_k3_1 = gk3[1] - gamma_ref_k3_iv[1]
        d_k3_2 = gk3[2] - gamma_ref_k3_iv[2]
        d_k2_1 = gk2_1[1] - gamma_ref_k2_iv[1][1]
        d_k2_2 = gk2_2[1] - gamma_ref_k2_iv[2][1]
        delta_1 = abs(d_k3_1 - d_k2_1)
        delta_2 = abs(d_k3_2 - d_k2_2)
        d_max = max(delta_1, delta_2)
        print(f"  {cn:<16} {gk3[1]:>8.4f} {gk3[2]:>8.4f}"
              f" {gk2_1[1]:>8.4f} {gk2_2[1]:>8.4f}"
              f" {delta_1:>7.4f} {delta_2:>7.4f} {d_max:>7.4f}")

    t1 = time.time()
    rs_iv = rand_search_gamma(ss_iv, gamma_ref_k3_iv, gamma_ref_k2_iv)
    t2 = time.time()
    print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s):")
    print(f"    Delta: mean={rs_iv['delta_mean']:.4f} med={rs_iv['delta_median']:.4f}"
          f" P95={rs_iv['delta_p95']:.4f} max={rs_iv['delta_max']:.4f}")
    print(f"    Delta>0.01: {rs_iv['frac_gt_001']:.1%}  Delta>0.05: {rs_iv['frac_gt_005']:.1%}")
    print(f"    sign_flip: {rs_iv['sign_flip_rate']:.1%}  valid: {rs_iv['n_valid']}/{N_RANDOM}")
    all_results['IV'] = rs_iv

    # =============================================
    # SUMMARY
    # =============================================
    print(f"\n{'='*90}")
    print("SUMMARY: Binarization Collapse Delta Across All DAGs")
    print(f"{'='*90}")
    print(f"\n  {'DAG':<14} {'D_mean':>8} {'D_med':>8} {'D_P95':>8} {'D_max':>8}"
          f" {'>0.01':>7} {'>0.05':>7} {'sflip':>7}")
    print(f"  {'-'*72}")
    for name, rs in all_results.items():
        sf = rs.get('sign_flip_rate', 0)
        print(f"  {name:<14} {rs['delta_mean']:>8.4f} {rs['delta_median']:>8.4f}"
              f" {rs['delta_p95']:>8.4f} {rs['delta_max']:>8.4f}"
              f" {rs['frac_gt_001']:>6.1%} {rs['frac_gt_005']:>6.1%}"
              f" {sf:>6.1%}")

    print(f"\nTotal: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
