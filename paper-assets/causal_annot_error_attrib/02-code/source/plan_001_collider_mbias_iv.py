"""
Collider + M-bias + Instrument DAG: bias via large-sample moments + MC verification.
K=3 LLM annotation error bias propagation in causal inference.
"""

import numpy as np
from collections import OrderedDict
import time

# ── Constants ────────────────────────────────────────────────────────────────

BETA_MIXED = np.array([0.0, 1.0, -0.5])
BETA_SAME  = np.array([0.0, 1.0,  0.5])

C1_SYMMETRIC_HIGH = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])
C2_ASYMMETRIC     = np.array([[0.65, 0.05, 0.10], [0.30, 0.85, 0.10], [0.05, 0.10, 0.80]])
C3_STRUCTURAL_12  = np.array([[0.96, 0.01, 0.01], [0.02, 0.69, 0.30], [0.02, 0.30, 0.69]])
C4_WEAK_DIAG      = np.array([[0.40, 0.35, 0.25], [0.35, 0.40, 0.35], [0.25, 0.25, 0.40]])
C5_NEAR_PERM      = np.array([[0.05, 0.05, 0.90], [0.90, 0.05, 0.05], [0.05, 0.90, 0.05]])
C6_DIFF_BASE      = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])

ALL_C = OrderedDict([
    ("C1_sym_high",   C1_SYMMETRIC_HIGH),
    ("C2_asymmetric", C2_ASYMMETRIC),
    ("C3_struct_12",  C3_STRUCTURAL_12),
    ("C4_weak_diag",  C4_WEAK_DIAG),
    ("C5_near_perm",  C5_NEAR_PERM),
    ("C6_diff_base",  C6_DIFF_BASE),
])

# ── Utilities ────────────────────────────────────────────────────────────────

def _generate_Astar(A, C, rng):
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)


def _generate_Astar_fixed_u(A, C, u):
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)


def _softmax_sample(logits, rng):
    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=logits.shape[0])
    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)


def _ols(Z, Y):
    return np.linalg.solve(Z.T @ Z, Z.T @ Y)


# ══════════════════════════════════════════════════════════════════════════════
# DAG 1: COLLIDER — T -> A <- Y
# ══════════════════════════════════════════════════════════════════════════════

COLLIDER_PARAMS = dict(tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)


def _gen_collider(N, params, rng):
    T = rng.normal(0, 1, N)
    eps = rng.normal(0, 1, N)
    Y = params['tau'] * T + eps
    logits = np.column_stack([
        np.zeros(N),
        params['g1'] + params['dT'] * T + params['dY'] * Y,
        params['g2'] + params['dT2'] * T + params['dY2'] * Y,
    ])
    A = _softmax_sample(logits, rng)
    return T, Y, A


def theory_collider(C, params, N_approx=2_000_000, seed=999):
    rng = np.random.default_rng(seed)
    T, Y, A = _gen_collider(N_approx, params, rng)
    Astar = _generate_Astar(A, C, rng)
    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
    ones = np.ones(N_approx)
    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
    return tau_ctrl, tau_nc


def mc_collider(C, params, N=10_000, n_reps=1000, seed=0):
    tau_ctrl_arr = np.empty(n_reps)
    tau_nc_arr = np.empty(n_reps)
    for r in range(n_reps):
        rng = np.random.default_rng(seed + r)
        T, Y, A = _gen_collider(N, params, rng)
        Astar = _generate_Astar(A, C, rng)
        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
        ones = np.ones(N)
        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]
    return tau_ctrl_arr.mean(), tau_nc_arr.mean()


# ══════════════════════════════════════════════════════════════════════════════
# DAG 2: M-BIAS — U1 -> {A,T}, U2 -> {A,Y}
# ══════════════════════════════════════════════════════════════════════════════

MBIAS_PARAMS = dict(tau=1.0, delta=1.0, lam=1.0,
                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)


def _gen_mbias(N, params, rng):
    U1 = rng.normal(0, 1, N)
    U2 = rng.normal(0, 1, N)
    T = params['delta'] * U1 + rng.normal(0, 1, N)
    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)
    logits = np.column_stack([
        np.zeros(N),
        params['g1'] + params['a1'] * U1 + params['a2'] * U2,
        params['g2'] + params['a3'] * U1 + params['a4'] * U2,
    ])
    A = _softmax_sample(logits, rng)
    return T, Y, A


def theory_mbias(C, params, N_approx=2_000_000, seed=999):
    rng = np.random.default_rng(seed)
    T, Y, A = _gen_mbias(N_approx, params, rng)
    Astar = _generate_Astar(A, C, rng)
    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
    ones = np.ones(N_approx)
    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
    return tau_ctrl, tau_nc


def mc_mbias(C, params, N=10_000, n_reps=1000, seed=0):
    tau_ctrl_arr = np.empty(n_reps)
    tau_nc_arr = np.empty(n_reps)
    for r in range(n_reps):
        rng = np.random.default_rng(seed + r)
        T, Y, A = _gen_mbias(N, params, rng)
        Astar = _generate_Astar(A, C, rng)
        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
        ones = np.ones(N)
        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]
    return tau_ctrl_arr.mean(), tau_nc_arr.mean()


# ══════════════════════════════════════════════════════════════════════════════
# DAG 3: INSTRUMENT — Z_iv -> A -> Y, U -> {A, Y}
# ══════════════════════════════════════════════════════════════════════════════

IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)


def _gen_iv(N, beta, params, rng):
    Z_iv = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    eps = rng.normal(0, 1, N)
    logits = np.column_stack([
        np.zeros(N),
        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
    ])
    A = _softmax_sample(logits, rng)
    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
         + params['lam'] * U + eps)
    return Z_iv, U, Y, A


def theory_iv(C, beta, params, N_approx=2_000_000, seed=999):
    rng = np.random.default_rng(seed)
    Z_iv, U, Y, A = _gen_iv(N_approx, beta, params, rng)
    Astar = _generate_Astar(A, C, rng)
    z1 = Z_iv == 1
    z0 = Z_iv == 0

    RF = Y[z1].mean() - Y[z0].mean()

    result = {'RF': RF}
    for k in [1, 2]:
        fs_star = (Astar[z1] == k).mean() - (Astar[z0] == k).mean()
        fs_true = (A[z1] == k).mean() - (A[z0] == k).mean()
        result[f'FS{k}_star'] = fs_star
        result[f'FS{k}_true'] = fs_true
        result[f'Wald{k}_star'] = RF / fs_star if abs(fs_star) > 1e-8 else np.nan
        result[f'Wald{k}_true'] = RF / fs_true if abs(fs_true) > 1e-8 else np.nan

    ones = np.ones(N_approx)
    X_star = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])
    result['ols_star'] = _ols(X_star, Y)
    X_true = np.column_stack([ones, (A == 1).astype(float), (A == 2).astype(float)])
    result['ols_true'] = _ols(X_true, Y)

    return result


def mc_iv(C, beta, params, N=10_000, n_reps=1000, seed=0):
    RF_arr = np.empty(n_reps)
    FS1_arr = np.empty(n_reps)
    FS2_arr = np.empty(n_reps)
    ols_arr = np.empty((n_reps, 3))
    for r in range(n_reps):
        rng = np.random.default_rng(seed + r)
        Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
        Astar = _generate_Astar(A, C, rng)
        z1 = Z_iv == 1
        z0 = Z_iv == 0
        RF_arr[r] = Y[z1].mean() - Y[z0].mean()
        FS1_arr[r] = (Astar[z1] == 1).mean() - (Astar[z0] == 1).mean()
        FS2_arr[r] = (Astar[z1] == 2).mean() - (Astar[z0] == 2).mean()
        ones = np.ones(N)
        X = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])
        ols_arr[r] = _ols(X, Y)

    wald1_mc = RF_arr.mean() / FS1_arr.mean()
    wald2_mc = RF_arr.mean() / FS2_arr.mean()
    ols_mc = ols_arr.mean(axis=0)
    return wald1_mc, wald2_mc, ols_mc


# ══════════════════════════════════════════════════════════════════════════════
# RANDOM C SEARCH (reuse base dataset, vary only C)
# ══════════════════════════════════════════════════════════════════════════════

def _fast_ols_tau(T, Y, A_star, N, sT, sTT, sY, sTY):
    """Inline OLS for Y ~ 1 + T + D1 + D2, returns coef on T. Avoids column_stack."""
    m1 = A_star == 1
    m2 = A_star == 2
    n1 = float(m1.sum())
    n2 = float(m2.sum())
    tD1 = T[m1].sum()
    tD2 = T[m2].sum()
    yD1 = Y[m1].sum()
    yD2 = Y[m2].sum()
    ZZ = np.array([[N, sT, n1, n2],
                   [sT, sTT, tD1, tD2],
                   [n1, tD1, n1, 0.0],
                   [n2, tD2, 0.0, n2]])
    ZY = np.array([sY, sTY, yD1, yD2])
    return np.linalg.solve(ZZ, ZY)[1]


def rand_search_collider(n_search=100_000, N_ap=50_000, seed=42):
    rng = np.random.default_rng(seed)
    T, Y, A = _gen_collider(N_ap, COLLIDER_PARAMS, rng)
    u = rng.uniform(size=N_ap)
    N = float(N_ap)
    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()
    tau_nc = sTY / sTT - sT * sY / (N * sTT)  # simplified no-control
    ones = np.ones(N_ap)
    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]

    rng_s = np.random.default_rng(seed + 1)
    biases = np.empty(n_search)
    for i in range(n_search):
        C = rng_s.dirichlet([1, 1, 1], size=3).T
        Astar = _generate_Astar_fixed_u(A, C, u)
        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - COLLIDER_PARAMS['tau']
    return biases, tau_nc - COLLIDER_PARAMS['tau']


def rand_search_mbias(n_search=100_000, N_ap=50_000, seed=42):
    rng = np.random.default_rng(seed)
    T, Y, A = _gen_mbias(N_ap, MBIAS_PARAMS, rng)
    u = rng.uniform(size=N_ap)
    N = float(N_ap)
    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()
    ones = np.ones(N_ap)
    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]

    rng_s = np.random.default_rng(seed + 1)
    biases = np.empty(n_search)
    for i in range(n_search):
        C = rng_s.dirichlet([1, 1, 1], size=3).T
        Astar = _generate_Astar_fixed_u(A, C, u)
        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - MBIAS_PARAMS['tau']
    return biases, tau_nc - MBIAS_PARAMS['tau']


def rand_search_iv(beta, n_search=100_000, N_ap=50_000, seed=42):
    rng = np.random.default_rng(seed)
    Z_iv, U, Y, A = _gen_iv(N_ap, beta, IV_PARAMS, rng)
    u = rng.uniform(size=N_ap)
    z1 = Z_iv == 1
    z0 = Z_iv == 0
    n1_z = float(z1.sum())
    n0_z = float(z0.sum())
    RF = Y[z1].sum() / n1_z - Y[z0].sum() / n0_z
    FS1_true = (A[z1] == 1).sum() / n1_z - (A[z0] == 1).sum() / n0_z
    FS2_true = (A[z1] == 2).sum() / n1_z - (A[z0] == 2).sum() / n0_z
    W1_true = RF / FS1_true if abs(FS1_true) > 1e-8 else np.nan
    W2_true = RF / FS2_true if abs(FS2_true) > 1e-8 else np.nan

    rng_s = np.random.default_rng(seed + 1)
    w1_vals = np.empty(n_search)
    w2_vals = np.empty(n_search)
    for i in range(n_search):
        C = rng_s.dirichlet([1, 1, 1], size=3).T
        Astar = _generate_Astar_fixed_u(A, C, u)
        fs1 = (Astar[z1] == 1).sum() / n1_z - (Astar[z0] == 1).sum() / n0_z
        fs2 = (Astar[z1] == 2).sum() / n1_z - (Astar[z0] == 2).sum() / n0_z
        w1_vals[i] = RF / fs1 if abs(fs1) > 1e-8 else np.nan
        w2_vals[i] = RF / fs2 if abs(fs2) > 1e-8 else np.nan
    return w1_vals, w2_vals, W1_true, W2_true


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def _print_section(title):
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def main():
    np.set_printoptions(precision=6, suppress=True)
    t0 = time.time()

    # ── DAG 1: Collider ─────────────────────────────────────────────────────
    _print_section("DAG 1: COLLIDER -- T -> A <- Y")
    p = COLLIDER_PARAMS
    print(f"DGP: T~N(0,1), Y={p['tau']}*T+eps, "
          f"A|T,Y softmax(dT={p['dT']}, dY={p['dY']}, dT2={p['dT2']}, dY2={p['dY2']})")
    print(f"Researcher error: controls A* in Y ~ 1 + T + D*1 + D*2")
    print(f"Truth: T and Y are NOT confounded => no-control OLS is consistent")
    print()

    hdr = (f"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}"
           f" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}")
    print(hdr)
    print("  " + "-" * 80)

    for cn, C in ALL_C.items():
        th_c, th_n = theory_collider(C, p)
        mc_c, mc_n = mc_collider(C, p)
        ok = "Y" if abs(th_c - mc_c) < 0.02 else "N"
        print(f"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}"
              f" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}")

    print()
    print("Violation analysis:")
    th_c1, th_n1 = theory_collider(C1_SYMMETRIC_HIGH, p)
    print(f"  No-control plim(tau_hat) = {th_n1:.4f}"
          f" (should = tau={p['tau']} since no confounding)")
    print(f"  Controlling collider A* induces spurious T-eps association")

    t1 = time.time()
    print(f"\nRandom C search (100k)... ", end="", flush=True)
    bc, bnc = rand_search_collider()
    print(f"done ({time.time()-t1:.0f}s)")
    print(f"  No-control bias: {bnc:+.4f}")
    print(f"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},"
          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
    worse = np.sum(np.abs(bc) > np.abs(bnc))
    print(f"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)")

    # ── DAG 2: M-bias ───────────────────────────────────────────────────────
    _print_section("DAG 2: M-BIAS -- U1 -> {A,T}, U2 -> {A,Y}")
    p = MBIAS_PARAMS
    print(f"DGP: U1,U2~N(0,1) indep, T={p['delta']}*U1+eta,"
          f" Y={p['tau']}*T+{p['lam']}*U2+eps")
    print(f"A|U1,U2 softmax(a1={p['a1']}, a2={p['a2']}, a3={p['a3']}, a4={p['a4']})")
    print(f"Researcher error: controls A* => opens U1->A<-U2 path (M-bias)")
    print(f"Truth: U2 indep T => no confounding of T->Y, no-control is consistent")
    print()

    hdr = (f"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}"
           f" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}")
    print(hdr)
    print("  " + "-" * 80)

    for cn, C in ALL_C.items():
        th_c, th_n = theory_mbias(C, p)
        mc_c, mc_n = mc_mbias(C, p)
        ok = "Y" if abs(th_c - mc_c) < 0.02 else "N"
        print(f"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}"
              f" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}")

    print()
    print("Violation analysis:")
    th_c1, th_n1 = theory_mbias(C1_SYMMETRIC_HIGH, p)
    print(f"  No-control plim(tau_hat) = {th_n1:.4f}"
          f" (should = tau={p['tau']} since U2 indep T)")
    print(f"  Controlling A* opens M-bias path: T <- U1 -> A <- U2 -> Y")

    t1 = time.time()
    print(f"\nRandom C search (100k)... ", end="", flush=True)
    bc, bnc = rand_search_mbias()
    print(f"done ({time.time()-t1:.0f}s)")
    print(f"  No-control bias: {bnc:+.4f}")
    print(f"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},"
          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
    worse = np.sum(np.abs(bc) > np.abs(bnc))
    print(f"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)")

    # ── DAG 3: Instrument ────────────────────────────────────────────────────
    for bname, beta in [("BETA_MIXED", BETA_MIXED), ("BETA_SAME", BETA_SAME)]:
        _print_section(
            f"DAG 3: INSTRUMENT -- Z->A->Y, U->{{A,Y}}  [{bname}: b={beta}]")
        p = IV_PARAMS
        print(f"DGP: Z~Bern(0.5), U~N(0,1), Y=b1*D1+b2*D2+{p['lam']}*U+eps")
        print(f"A|Z,U softmax(dZ={p['dZ']}, dU={p['dU']}, dZ2={p['dZ2']}, dU2={p['dU2']})")
        print(f"Under-identified: 1 IV for 2 endogenous dummies => per-dummy Wald")
        print(f"Wald_k = RF/FS*_k estimates (b1*pi1+b2*pi2)/pi*_k, not b_k")
        print()

        hdr2 = (f"  {'C':<16}"
                f" {'W1* th':>8} {'W1* mc':>8} {'ok':>3}"
                f" {'W2* th':>8} {'W2* mc':>8} {'ok':>3}"
                f" {'OLS b1':>8} {'mc':>8} {'ok':>3}"
                f" {'OLS b2':>8} {'mc':>8} {'ok':>3}")
        print(hdr2)
        print("  " + "-" * 110)

        for cn, C in ALL_C.items():
            th = theory_iv(C, beta, p)
            mc_w1, mc_w2, mc_ols = mc_iv(C, beta, p)

            o1 = "Y" if abs(th['Wald1_star'] - mc_w1) < 0.10 else "N"
            o2 = "Y" if abs(th['Wald2_star'] - mc_w2) < 0.10 else "N"
            o3 = "Y" if abs(th['ols_star'][1] - mc_ols[1]) < 0.02 else "N"
            o4 = "Y" if abs(th['ols_star'][2] - mc_ols[2]) < 0.02 else "N"

            def _fmt(v, w=8):
                return f"{v:>{w}.4f}" if np.isfinite(v) else f"{'nan':>{w}}"

            print(f"  {cn:<16}"
                  f" {_fmt(th['Wald1_star'])} {_fmt(mc_w1)} {o1:>3}"
                  f" {_fmt(th['Wald2_star'])} {_fmt(mc_w2)} {o2:>3}"
                  f" {th['ols_star'][1]:>8.4f} {mc_ols[1]:>8.4f} {o3:>3}"
                  f" {th['ols_star'][2]:>8.4f} {mc_ols[2]:>8.4f} {o4:>3}")

        print()
        th1 = theory_iv(C1_SYMMETRIC_HIGH, beta, p)
        print("Violation analysis (C1_sym_high):")
        print(f"  True beta = [{beta[1]}, {beta[2]}]")
        print(f"  Reduced form (ITT): {th1['RF']:.4f}")
        print(f"  First stage true:  pi1={th1['FS1_true']:.4f}, pi2={th1['FS2_true']:.4f}")
        print(f"  First stage A*:    pi*1={th1['FS1_star']:.4f}, pi*2={th1['FS2_star']:.4f}")
        print(f"  Wald true A:  W1={th1['Wald1_true']:.4f}, W2={th1['Wald2_true']:.4f}")
        print(f"  Wald A*:      W1={th1['Wald1_star']:.4f}, W2={th1['Wald2_star']:.4f}")
        print(f"  OLS true A:   [{th1['ols_true'][1]:.4f}, {th1['ols_true'][2]:.4f}]"
              f" (biased by U)")
        print(f"  OLS A*:       [{th1['ols_star'][1]:.4f}, {th1['ols_star'][2]:.4f}]"
              f" (biased by U + misclassification)")

        # Analytical insight: how C transforms first stages
        print(f"\n  FS transformation by C:")
        print(f"    FS*_k = sum_j C[k,j] * FS_j")
        for cn2, C2 in [("C1_sym_high", C1_SYMMETRIC_HIGH),
                        ("C4_weak_diag", C4_WEAK_DIAG),
                        ("C5_near_perm", C5_NEAR_PERM)]:
            th2 = theory_iv(C2, beta, p)
            fs_true = np.array([-(th2['FS1_true']+th2['FS2_true']),
                                th2['FS1_true'], th2['FS2_true']])
            fs_star_calc = C2 @ fs_true
            print(f"    {cn2}: FS_true={fs_true}, C@FS={fs_star_calc},"
                  f" FS*=[{th2['FS1_star']:.4f}, {th2['FS2_star']:.4f}]")

        t1 = time.time()
        print(f"\n  Random C search (100k)... ", end="", flush=True)
        w1v, w2v, w1t, w2t = rand_search_iv(beta)
        print(f"done ({time.time()-t1:.0f}s)")
        v1 = np.isfinite(w1v)
        v2 = np.isfinite(w2v)
        w1b = w1v - w1t
        w2b = w2v - w2t
        print(f"    Wald1 true={w1t:.4f}: A* vals mean={np.nanmean(w1v):+.4f},"
              f" std={np.nanstd(w1v):.4f},"
              f" range=[{np.nanmin(w1v):+.4f}, {np.nanmax(w1v):+.4f}],"
              f" valid={v1.sum()}/{len(w1v)}")
        print(f"    Wald2 true={w2t:.4f}: A* vals mean={np.nanmean(w2v):+.4f},"
              f" std={np.nanstd(w2v):.4f},"
              f" range=[{np.nanmin(w2v):+.4f}, {np.nanmax(w2v):+.4f}],"
              f" valid={v2.sum()}/{len(w2v)}")
        print(f"    Delta from true: W1 mean={np.nanmean(w1b):+.4f},"
              f" W2 mean={np.nanmean(w2b):+.4f}")

    print(f"\nTotal: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
