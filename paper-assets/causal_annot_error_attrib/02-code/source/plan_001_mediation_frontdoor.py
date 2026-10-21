#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Plan 001: Mediation + Front-door DAG — closed-form bias + MC verification."""
import numpy as np
import time
import warnings
from collections import OrderedDict

warnings.filterwarnings('ignore')

# ================================================================
# Configuration
# ================================================================
K = 3
N_MC = 10_000
N_REPS = 1_000
N_LARGE = 50_000_000
N_RANDOM = 100_000

BETA_MIXED = np.array([0.0, 1.0, -0.5])
BETA_SAME  = np.array([0.0, 1.0,  0.5])

TAU = 0.5
GAMMA_MED = np.array([0.0, 0.5, -0.3])
DELTA_MED = np.array([0.0, 0.8, -0.6])

ALPHA_U = 1.0
LAMBDA_U = 1.0
GAMMA_FD = np.array([0.0, 0.5, -0.3])
DELTA_FD = np.array([0.0, 1.0, -0.8])

C_DICT = OrderedDict([
    ("1_sym_high",   np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),
    ("2_asymmetric", np.array([[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]])),
    ("3_struct_12",  np.array([[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]])),
    ("4_weak_diag",  np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]])),
    ("5_near_perm",  np.array([[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]])),
    ("6_diff_base",  np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),
])

COEF_NAMES = ['β₀', 'τ', 'β₁', 'β₂']


# ================================================================
# Helpers
# ================================================================
def softmax(x):
    e = np.exp(x - x.max())
    return e / e.sum()


def p_cat(t, g, d):
    return softmax(g + d * t)


def gen_Astar(A, C, rng):
    pr = C[:, A]
    cu = np.cumsum(pr, axis=0)
    u = rng.uniform(size=len(A))
    return (u >= cu[0]).astype(int) + (u >= cu[1]).astype(int)


def ols(Z, Y):
    return np.linalg.lstsq(Z, Y, rcond=None)[0]


def fv(v, w=8, p=4):
    return '[' + ' '.join(f'{x:>{w}.{p}f}' for x in v) + ']'


def fm(th, mc, se, k=2):
    ok = np.abs(mc - th) < k * se
    return ''.join('✓' if o else '✗' for o in ok), ok.all()


# ================================================================
# DAG 1  Mediation: T -> A -> Y
#
# DGP:  T ~ Bern(0.5)
#        A | T ~ Cat(softmax(gamma + delta*T))
#        Y = beta0 + beta1*D1 + beta2*D2 + tau*T + eps
#        A* | A ~ Cat(C[:, A])
#
# Researcher regression:  Y ~ 1 + T + D*_1 + D*_2
#
# Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)
# eps indep of Z  =>  plim = (E[Z'Z])^{-1} E[Z'X] beta
#
# Key moments:
#   q_t = C @ p_{A|T=t}           (P(A*|T=t))
#   q_marg = 0.5*(q_0 + q_1)
#   E[D*_j * D_k] = C[j,k] * p_marg[k]
# ================================================================
def plim_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED):
    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
    q0, q1 = C @ p0, C @ p1
    pm = .5 * (p0 + p1)
    qm = .5 * (q0 + q1)

    EZZ = np.array([
        [1,      .5,        qm[1],      qm[2]     ],
        [.5,     .5,        .5*q1[1],   .5*q1[2]  ],
        [qm[1],  .5*q1[1],  qm[1],      0         ],
        [qm[2],  .5*q1[2],  0,          qm[2]     ]])

    EZX = np.array([
        [1,      .5,        pm[1],            pm[2]           ],
        [.5,     .5,        .5*p1[1],         .5*p1[2]        ],
        [qm[1],  .5*q1[1],  C[1,1]*pm[1],    C[1,2]*pm[2]   ],
        [qm[2],  .5*q1[2],  C[2,1]*pm[1],    C[2,2]*pm[2]   ]])

    b = np.array([beta[0], tau, beta[1], beta[2]])
    return np.linalg.solve(EZZ, EZX @ b)


def mc_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED,
           nr=N_REPS, N=N_MC, seed=42):
    rng = np.random.default_rng(seed)
    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
    out = np.zeros((nr, 4))
    for r in range(nr):
        T = rng.binomial(1, .5, N)
        pr = np.where(T[:, None] == 0, p0, p1)
        cu = np.cumsum(pr, axis=1)
        u = rng.uniform(size=N)
        A = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
        D1 = (A == 1).astype(float)
        D2 = (A == 2).astype(float)
        Y = beta[0] + beta[1]*D1 + beta[2]*D2 + tau*T + rng.normal(0, 1, N)
        As = gen_Astar(A, C, rng)
        Z = np.column_stack([np.ones(N), T.astype(float),
                             (As == 1).astype(float), (As == 2).astype(float)])
        out[r] = ols(Z, Y)
    return out.mean(0), out.std(0) / np.sqrt(nr)


def rsearch_med(beta, tau, g=GAMMA_MED, d=DELTA_MED,
                ns=N_RANDOM, seed=999):
    rng = np.random.default_rng(seed)
    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
    pm = .5 * (p0 + p1)
    b = np.array([beta[0], tau, beta[1], beta[2]])
    clean = plim_med(np.eye(K), beta, tau, g, d)

    Cs = np.zeros((ns, K, K))
    for i in range(K):
        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)

    q0 = Cs @ p0
    q1 = Cs @ p1
    qm = .5 * (q0 + q1)

    EZZ = np.zeros((ns, 4, 4))
    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = .5
    EZZ[:, 0, 2] = EZZ[:, 2, 0] = qm[:, 1]
    EZZ[:, 0, 3] = EZZ[:, 3, 0] = qm[:, 2]
    EZZ[:, 1, 1] = .5
    EZZ[:, 1, 2] = EZZ[:, 2, 1] = .5 * q1[:, 1]
    EZZ[:, 1, 3] = EZZ[:, 3, 1] = .5 * q1[:, 2]
    EZZ[:, 2, 2] = qm[:, 1]
    EZZ[:, 3, 3] = qm[:, 2]

    EZX = np.zeros((ns, 4, 4))
    EZX[:, 0, 0] = 1;       EZX[:, 0, 1] = .5
    EZX[:, 0, 2] = pm[1];   EZX[:, 0, 3] = pm[2]
    EZX[:, 1, 0] = .5;      EZX[:, 1, 1] = .5
    EZX[:, 1, 2] = .5 * p1[1]; EZX[:, 1, 3] = .5 * p1[2]
    EZX[:, 2, 0] = qm[:, 1];   EZX[:, 2, 1] = .5 * q1[:, 1]
    EZX[:, 2, 2] = Cs[:, 1, 1] * pm[1]; EZX[:, 2, 3] = Cs[:, 1, 2] * pm[2]
    EZX[:, 3, 0] = qm[:, 2];   EZX[:, 3, 1] = .5 * q1[:, 2]
    EZX[:, 3, 2] = Cs[:, 2, 1] * pm[1]; EZX[:, 3, 3] = Cs[:, 2, 2] * pm[2]

    rhs = np.einsum('nij,j->ni', EZX, b)
    pl = np.linalg.solve(EZZ, rhs[:, :, None])[:, :, 0]

    df = np.abs(pl - clean)
    viol = np.any(df > .01, 1).mean()
    nz = np.abs(clean) > 1e-6
    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()
    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()
    return viol, sign, amp


# ================================================================
# DAG 2  Front-door: T -> M -> Y,  U -> T,  U -> Y
#
# DGP:  U ~ N(0,1)
#        T = alpha_U * U + eta,  eta ~ N(0,1)
#        M | T ~ Cat(softmax(gamma + delta*T))
#        Y = beta1*D_{M,1} + beta2*D_{M,2} + lambda*U + eps
#        M* | M ~ Cat(C[:, M])
#
# Researcher regression:  Y ~ 1 + T + D*_{M,1} + D*_{M,2}
#
# T correlated with U (confounding), so E[Z'(lambda*U)] != 0.
# Use large-sample moment approximation:
#   plim = (E[Z'Z])^{-1} E[Z'Y]   estimated from N_LARGE samples.
#
# For fast random search, pre-compute sufficient statistics:
#   E[D_{M,k}], E[D_{M,k}*T], E[D_{M,k}*Y]  for k=0,1,2
# Then for any C:
#   E[D*_j] = sum_k C[j,k]*E[D_{M,k}]   etc.
# ================================================================
def _gen_fd(N, beta, rng, g=GAMMA_FD, d=DELTA_FD,
            aU=ALPHA_U, lU=LAMBDA_U):
    U = rng.normal(0, 1, N)
    T = aU * U + rng.normal(0, 1, N)
    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])
    lo -= lo.max(1, keepdims=True)
    e = np.exp(lo)
    p = e / e.sum(1, keepdims=True)
    cu = np.cumsum(p, axis=1)
    u = rng.uniform(size=N)
    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
    DM1 = (M == 1).astype(float)
    DM2 = (M == 2).astype(float)
    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)
    return T, M, Y, U


def precomp_fd(beta, N=N_LARGE, seed=123):
    rng = np.random.default_rng(seed)
    T, M, Y, _ = _gen_fd(N, beta, rng)
    DM = np.zeros((N, K))
    for k in range(K):
        DM[:, k] = (M == k).astype(float)
    return dict(
        E_T=T.mean(), E_T2=(T**2).mean(),
        E_Y=Y.mean(), E_TY=(T*Y).mean(),
        E_DM=DM.mean(0),
        E_DM_T=(DM * T[:, None]).mean(0),
        E_DM_Y=(DM * Y[:, None]).mean(0))


def plim_fd(C, st):
    ds  = C @ st['E_DM']
    dst = C @ st['E_DM_T']
    dsy = C @ st['E_DM_Y']
    ET, ET2 = st['E_T'], st['E_T2']
    EY, ETY = st['E_Y'], st['E_TY']

    EZZ = np.array([
        [1,      ET,      ds[1],    ds[2]   ],
        [ET,     ET2,     dst[1],   dst[2]  ],
        [ds[1],  dst[1],  ds[1],    0       ],
        [ds[2],  dst[2],  0,        ds[2]   ]])

    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
    return np.linalg.solve(EZZ, EZY)


def mc_fd(C, beta, nr=N_REPS, N=N_MC, seed=42):
    rng = np.random.default_rng(seed)
    out = np.zeros((nr, 4))
    for r in range(nr):
        T, M, Y, _ = _gen_fd(N, beta, rng)
        Ms = gen_Astar(M, C, rng)
        Z = np.column_stack([np.ones(N), T,
                             (Ms == 1).astype(float),
                             (Ms == 2).astype(float)])
        out[r] = ols(Z, Y)
    return out.mean(0), out.std(0) / np.sqrt(nr)


def rsearch_fd(st, ns=N_RANDOM, seed=999):
    rng = np.random.default_rng(seed)
    clean = plim_fd(np.eye(K), st)

    Cs = np.zeros((ns, K, K))
    for i in range(K):
        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)

    E_DMs   = Cs @ st['E_DM']
    E_DMs_T = Cs @ st['E_DM_T']
    E_DMs_Y = Cs @ st['E_DM_Y']
    ET, ET2 = st['E_T'], st['E_T2']
    EY, ETY = st['E_Y'], st['E_TY']

    EZZ = np.zeros((ns, 4, 4))
    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = ET
    EZZ[:, 0, 2] = EZZ[:, 2, 0] = E_DMs[:, 1]
    EZZ[:, 0, 3] = EZZ[:, 3, 0] = E_DMs[:, 2]
    EZZ[:, 1, 1] = ET2
    EZZ[:, 1, 2] = EZZ[:, 2, 1] = E_DMs_T[:, 1]
    EZZ[:, 1, 3] = EZZ[:, 3, 1] = E_DMs_T[:, 2]
    EZZ[:, 2, 2] = E_DMs[:, 1]
    EZZ[:, 3, 3] = E_DMs[:, 2]

    EZY = np.zeros((ns, 4))
    EZY[:, 0] = EY;   EZY[:, 1] = ETY
    EZY[:, 2] = E_DMs_Y[:, 1]
    EZY[:, 3] = E_DMs_Y[:, 2]

    pl = np.linalg.solve(EZZ, EZY[:, :, None])[:, :, 0]

    df = np.abs(pl - clean)
    viol = np.any(df > .01, 1).mean()
    nz = np.abs(clean) > 1e-6
    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()
    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()
    return viol, sign, amp


# ================================================================
# Main
# ================================================================
def main():
    t0 = time.time()
    np.set_printoptions(precision=4, suppress=True)

    for bn, beta in [("mixed [0,1,-0.5]", BETA_MIXED),
                      ("same [0,1,0.5]",   BETA_SAME)]:

        # ---- DAG 1: Mediation ----
        print(f"\n{'='*90}")
        print(f"  MEDIATION: T -> A -> Y  |  beta={bn}")
        print(f"{'='*90}")
        p0, p1 = p_cat(0, GAMMA_MED, DELTA_MED), p_cat(1, GAMMA_MED, DELTA_MED)
        print(f"  P(A|T=0)={fv(p0,6,3)}  P(A|T=1)={fv(p1,6,3)}  tau={TAU}")
        print(f"  Coefs: [{', '.join(COEF_NAMES)}]\n")

        hdr = f"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt"
        print(hdr)
        print(f"  {'-'*92}")

        all_ok = True
        for cn, C in C_DICT.items():
            th = plim_med(C, beta, TAU)
            mc, se = mc_med(C, beta, TAU)
            ms, ok = fm(th, mc, se)
            if not ok:
                all_ok = False
            print(f"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}")

        status = 'ALL MATCH' if all_ok else 'MISMATCH DETECTED'
        print(f"  >>> {status}")

        t1 = time.time()
        v, s, a = rsearch_med(beta, TAU)
        t2 = time.time()
        print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): "
              f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")

        # ---- DAG 2: Front-door ----
        print(f"\n{'='*90}")
        print(f"  FRONT-DOOR: T -> M -> Y, U -> T, U -> Y  |  beta={bn}")
        print(f"{'='*90}")
        print(f"  alpha_U={ALPHA_U}  lambda_U={LAMBDA_U}")
        print(f"  M|T softmax: gamma={GAMMA_FD}  delta={DELTA_FD}")
        print(f"  Coefs: [{', '.join(COEF_NAMES)}]\n")

        t1 = time.time()
        st = precomp_fd(beta)
        t2 = time.time()
        print(f"  Moments pre-computed (N={N_LARGE//10**6}M, {t2-t1:.1f}s)\n")

        hdr = f"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt"
        print(hdr)
        print(f"  {'-'*92}")

        all_ok = True
        for cn, C in C_DICT.items():
            th = plim_fd(C, st)
            mc, se = mc_fd(C, beta)
            ms, ok = fm(th, mc, se, k=3)
            if not ok:
                all_ok = False
            print(f"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}")

        status = 'ALL MATCH (3σ)' if all_ok else 'MISMATCH DETECTED'
        print(f"  >>> {status}")

        t1 = time.time()
        v, s, a = rsearch_fd(st)
        t2 = time.time()
        print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): "
              f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")

    print(f"\n{'='*90}")
    print(f"  Total: {time.time()-t0:.1f}s")
    print(f"{'='*90}")


if __name__ == "__main__":
    main()
