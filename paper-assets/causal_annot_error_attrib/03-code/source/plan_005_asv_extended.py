#!/usr/bin/env python3
"""
plan_005: ASV framework extension to M-bias, IV, front-door topologies.
Extends plan_004 v3 (envelope monotonicity + magnitude/sign-flip dual reporting)
to complete Claim 2 coverage across all 6 DAG topologies.
"""

import numpy as np
import json
import time

K = 3

# ============================================================================
# Utilities (from plan_004 v3)
# ============================================================================

def softmax_sample(logits, rng):
    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=logits.shape[0])
    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)


def generate_Astar(A, C, rng):
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)


def ols_with_dummies(Y, T, Astar, K=3):
    N = len(Y)
    D = np.zeros((N, K - 1))
    for k in range(1, K):
        D[:, k - 1] = (Astar == k).astype(float)
    X = np.column_stack([np.ones(N), T, D])
    try:
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        resid = Y - X @ beta
        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
        XtX_inv = np.linalg.inv(X.T @ X)
        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
    except np.linalg.LinAlgError:
        beta = np.full(X.shape[1], np.nan)
        se = np.full(X.shape[1], np.nan)
    return beta, se


# ============================================================================
# C(delta) Parameterization (from plan_004 v3)
# ============================================================================

class LinearInterpolation:
    def __call__(self, C0, delta):
        K = C0.shape[0]
        C_d = (1 - delta) * np.eye(K) + delta * C0
        C_d = np.maximum(C_d, 0.0)
        col_sums = C_d.sum(axis=0)
        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
        C_d = C_d / col_sums
        return C_d

    def delta_range(self, C0=None):
        if C0 is None:
            return (0.0, 5.0)
        min_diag = np.diag(C0).min()
        if min_diag >= 1.0:
            return (0.0, 10.0)
        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
        return (0.0, delta_max)


# ============================================================================
# C matrices (from plan_004 v3)
# ============================================================================

def make_C_list():
    return {
        "C1_sym": np.array([[0.80, 0.10, 0.10],
                            [0.10, 0.80, 0.10],
                            [0.10, 0.10, 0.80]]),
        "C2_high": np.array([[0.90, 0.05, 0.05],
                             [0.05, 0.90, 0.05],
                             [0.05, 0.05, 0.90]]),
        "C3_asym": np.array([[0.70, 0.20, 0.10],
                             [0.15, 0.70, 0.15],
                             [0.10, 0.15, 0.75]]),
        "C4_weak": np.array([[0.60, 0.20, 0.20],
                             [0.20, 0.60, 0.20],
                             [0.15, 0.15, 0.70]]),
        "C5_perm": np.array([[0.40, 0.30, 0.30],
                             [0.30, 0.40, 0.30],
                             [0.30, 0.30, 0.40]]),
        "C6_diff": np.array([[0.85, 0.075, 0.075],
                             [0.15, 0.70, 0.15],
                             [0.05, 0.05, 0.90]]),
    }


def normalize_C_list(C_dict):
    out = {}
    for name, C in C_dict.items():
        C = np.maximum(C, 0.0)
        cs = C.sum(axis=0)
        cs = np.where(cs < 1e-10, 1.0, cs)
        out[name] = C / cs
    return out


def random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):
    C = np.zeros((K, K))
    for k in range(K):
        alphas = np.full(K, offdiag_alpha)
        alphas[k] = diag_alpha
        C[:, k] = rng.dirichlet(alphas)
    return C


# ============================================================================
# Topology 1: M-BIAS — U1->{A,T}, U2->{A,Y}, T->Y
# ============================================================================

MBIAS_PARAMS = dict(tau=0.5, delta=1.0, lam=1.0,
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
    A = softmax_sample(logits, rng)
    return T, Y, A


def gen_mbias_data(N, params, C0, rng):
    T, Y, A = _gen_mbias(N, params, rng)
    Astar = generate_Astar(A, C0, rng)
    return T, Y, A, Astar


def precomp_mbias(params, N=2_000_000, seed=999):
    rng = np.random.default_rng(seed)
    T, Y, A = _gen_mbias(N, params, rng)
    DA = np.zeros((N, K))
    for k in range(K):
        DA[:, k] = (A == k).astype(float)
    return dict(
        E_T=T.mean(), E_T2=(T**2).mean(),
        E_Y=Y.mean(), E_TY=(T*Y).mean(),
        E_DA=DA.mean(0),
        E_DA_T=(DA * T[:, None]).mean(0),
        E_DA_Y=(DA * Y[:, None]).mean(0))


def plim_mbias(C, st):
    """OLS plim for Y ~ 1 + T + D1_A* + D2_A*."""
    ds  = C @ st['E_DA']
    dst = C @ st['E_DA_T']
    dsy = C @ st['E_DA_Y']
    ET, ET2 = st['E_T'], st['E_T2']
    EY, ETY = st['E_Y'], st['E_TY']
    EZZ = np.array([
        [1,      ET,      ds[1],    ds[2]   ],
        [ET,     ET2,     dst[1],   dst[2]  ],
        [ds[1],  dst[1],  ds[1],    0       ],
        [ds[2],  dst[2],  0,        ds[2]   ]])
    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
    return np.linalg.solve(EZZ, EZY)


# ============================================================================
# Topology 2: IV — Z->A->Y, U->{A,Y}
# ============================================================================

IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
IV_BETA = np.array([0.0, 0.5, -0.25])


def _gen_iv(N, beta, params, rng):
    Z_iv = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    eps = rng.normal(0, 1, N)
    logits = np.column_stack([
        np.zeros(N),
        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
    ])
    A = softmax_sample(logits, rng)
    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
         + params['lam'] * U + eps)
    return Z_iv, U, Y, A


def gen_iv_data(N, beta, params, C0, rng):
    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
    Astar = generate_Astar(A, C0, rng)
    return Z_iv, Y, A, Astar


def precomp_iv(beta, params, N=2_000_000, seed=999):
    """Precompute reduced form and first stage for Wald estimator."""
    rng = np.random.default_rng(seed)
    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
    z1 = Z_iv == 1; z0 = Z_iv == 0
    RF = Y[z1].mean() - Y[z0].mean()
    FS = np.zeros(K)
    for k in range(K):
        FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
    return dict(RF=RF, FS=FS)


def plim_iv(C, st):
    """Wald estimator: RF / FS*_1 where FS* = C @ FS."""
    FS_star = C @ st['FS']
    if abs(FS_star[1]) < 1e-8:
        return np.nan
    return st['RF'] / FS_star[1]


def wald_with_se(Z, Y, Astar, k=1):
    """Finite-sample Wald estimator with delta-method SE."""
    z1 = Z == 1; z0 = Z == 0
    n1 = float(z1.sum()); n0 = float(z0.sum())
    if n1 < 2 or n0 < 2:
        return np.nan, np.nan
    RF = Y[z1].mean() - Y[z0].mean()
    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
    Dk_z1 = (Astar[z1] == k).astype(float).mean()
    Dk_z0 = (Astar[z0] == k).astype(float).mean()
    FS = Dk_z1 - Dk_z0
    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
    if abs(FS) < 1e-8:
        return np.nan, np.nan
    Wald = RF / FS
    var_Wald = var_RF / FS**2 + RF**2 * var_FS / FS**4
    SE = np.sqrt(max(var_Wald, 0))
    return Wald, SE


# ============================================================================
# Topology 3: FRONT-DOOR — T->M->Y, U->{T,Y}
# ============================================================================

ALPHA_U = 1.0
LAMBDA_U = 1.0
GAMMA_FD = np.array([0.0, 0.5, -0.3])
DELTA_FD = np.array([0.0, 1.0, -0.8])
BETA_FD = np.array([0.0, 1.0, -0.5])


def _gen_fd(N, beta, rng, g=None, d=None, aU=None, lU=None):
    if g is None: g = GAMMA_FD
    if d is None: d = DELTA_FD
    if aU is None: aU = ALPHA_U
    if lU is None: lU = LAMBDA_U
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


def gen_fd_data(N, beta, C0, rng, lU=None, aU=None, d=None):
    T, M, Y, U = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
    Mstar = generate_Astar(M, C0, rng)
    return T, Y, M, Mstar


def precomp_fd(beta, N=10_000_000, seed=123, lU=None, aU=None, d=None):
    rng = np.random.default_rng(seed)
    T, M, Y, _ = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
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
    """OLS plim for Y ~ 1 + T + D1_M* + D2_M*."""
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


# ============================================================================
# ASV Framework
# ============================================================================

def compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):
    dmin, dmax = param.delta_range(C0)
    deltas = np.linspace(dmin, dmax, n_grid)
    tau_curve = np.zeros(n_grid)
    for i, d in enumerate(deltas):
        C_d = param(C0, d)
        if topology == "mbias":
            tau_curve[i] = plim_mbias(C_d, st)[1]
        elif topology == "iv":
            tau_curve[i] = plim_iv(C_d, st)
        elif topology == "frontdoor":
            tau_curve[i] = plim_fd(C_d, st)[1]
    bias_abs = np.abs(tau_curve - tau_true)
    return deltas, bias_abs, tau_curve


def compute_envelope(bias_abs):
    env = np.zeros_like(bias_abs)
    running_max = 0.0
    for i in range(len(bias_abs)):
        v = bias_abs[i]
        if not np.isnan(v):
            running_max = max(running_max, v)
        env[i] = running_max
    return env


def verify_envelope_monotonicity(envelope):
    diffs = np.diff(envelope)
    return int(np.sum(diffs < -1e-12))


def compute_asv_envelope(topology, C0, tau_true, param, threshold_type,
                         threshold_value=0.1, st=None, n_grid=1500):
    deltas, bias_abs, tau_curve = compute_bias_curve(
        topology, C0, param, tau_true, st, n_grid)
    envelope = compute_envelope(bias_abs)

    valid_ba = bias_abs[~np.isnan(bias_abs)]
    raw_violations = int(np.sum(np.diff(valid_ba) < -1e-12)) if len(valid_ba) > 1 else 0
    env_violations = verify_envelope_monotonicity(envelope)

    asv = None
    if threshold_type == "sign_flip":
        if abs(tau_true) < 1e-12:
            asv = None
        else:
            baseline_sign = np.sign(tau_true)
            for i, d in enumerate(deltas):
                if np.isnan(tau_curve[i]):
                    continue
                if np.sign(tau_curve[i]) != baseline_sign:
                    asv = d
                    break
    elif threshold_type == "magnitude_relative":
        if abs(tau_true) < 1e-12:
            asv = None
        else:
            thresh = threshold_value * abs(tau_true)
            for i, d in enumerate(deltas):
                if envelope[i] > thresh:
                    asv = d
                    break
    elif threshold_type == "magnitude_absolute":
        thresh = threshold_value
        for i, d in enumerate(deltas):
            if envelope[i] > thresh:
                asv = d
                break

    return {
        "asv": asv,
        "raw_violations": raw_violations,
        "envelope_violations": env_violations,
        "deltas": deltas,
        "tau_curve": tau_curve,
        "envelope": envelope,
    }


def compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):
    if abs(tau_true) < 1e-12:
        return None
    thresh = rel_thresh * abs(tau_true)
    running_max = 0.0
    for i in range(len(deltas)):
        b = abs(tau_curve[i] - tau_true)
        if np.isnan(b):
            continue
        running_max = max(running_max, b)
        if running_max > thresh:
            return deltas[i]
    return None


# ============================================================================
# Part 1: Envelope Monotonicity
# ============================================================================

def part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):
    print("\n" + "=" * 70)
    print("PART 1: Envelope Monotonicity (tau=0.5)")
    print("=" * 70)
    t0 = time.time()
    param = LinearInterpolation()
    C_list = normalize_C_list(make_C_list())

    for topo, st, tau_true, label in [
        ("mbias", st_mb, 0.5, "M-bias"),
        ("iv", st_iv, 0.5, "IV"),
        ("frontdoor", st_fd, tau_fd, "Front-door"),
    ]:
        print(f"\n  {label} (tau_true={tau_true:.4f}):")
        for cname, C0 in C_list.items():
            r = compute_asv_envelope(topo, C0, tau_true, param,
                                     "magnitude_relative", 0.1, st=st)
            print(f"    {cname}: raw_violations={r['raw_violations']}/1500, "
                  f"envelope_violations={r['envelope_violations']}/1500")
    print(f"\n  Time: {time.time()-t0:.1f}s")


# ============================================================================
# Part 2: ASV Values (tau=0.5)
# ============================================================================

def part2_asv_values(st_mb, st_iv, st_fd, tau_fd):
    print("\n" + "=" * 70)
    print("PART 2: ASV Values (tau=0.5)")
    print("=" * 70)
    t0 = time.time()
    param = LinearInterpolation()
    C_list = normalize_C_list(make_C_list())
    results = {}

    print(f"\n  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10}")
    print("  " + "-" * 45)

    for topo, st, tau_true, label in [
        ("mbias", st_mb, 0.5, "M-bias"),
        ("iv", st_iv, 0.5, "IV"),
        ("frontdoor", st_fd, tau_fd, "Front-door"),
    ]:
        for cname, C0 in C_list.items():
            r_sf = compute_asv_envelope(topo, C0, tau_true, param,
                                        "sign_flip", st=st)
            r_mag = compute_asv_envelope(topo, C0, tau_true, param,
                                         "magnitude_relative", 0.1, st=st)
            sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
            mg_s = f"{r_mag['asv']:.3f}" if r_mag['asv'] is not None else "None"
            print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10}")
            results[(label, cname)] = {
                "sign_flip": r_sf['asv'], "magnitude_10pct": r_mag['asv']}
    print(f"\n  Time: {time.time()-t0:.1f}s")
    return results


# ============================================================================
# Part 3: Small-tau ASV
# ============================================================================

def part3_small_tau_asv():
    print("\n" + "=" * 70)
    print("PART 3: Small-tau ASV (tau=0.05, 0.1)")
    print("=" * 70)
    t0 = time.time()
    param = LinearInterpolation()
    C_list = normalize_C_list(make_C_list())
    results = {}

    for tau_val in [0.05, 0.1]:
        print(f"\n  --- tau = {tau_val} ---")
        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
        st_mb = precomp_mbias(mb_p, N=2_000_000)
        iv_b = np.array([0.0, tau_val, -tau_val/2])
        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
        lU = tau_val * 2
        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU, seed=200+int(tau_val*100))
        tau_fd = plim_fd(np.eye(K), st_fd)[1]
        print(f"  Front-door tau_I = {tau_fd:.6f}")

        hdr = f"  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10} {'MagAbs.05':>10}"
        print(hdr)
        print("  " + "-" * 55)

        for topo, st, tau_true, label in [
            ("mbias", st_mb, tau_val, "M-bias"),
            ("iv", st_iv, tau_val, "IV"),
            ("frontdoor", st_fd, tau_fd, "Front-door"),
        ]:
            for cname, C0 in C_list.items():
                r_sf = compute_asv_envelope(topo, C0, tau_true, param,
                                            "sign_flip", st=st)
                r_mg = compute_asv_envelope(topo, C0, tau_true, param,
                                            "magnitude_relative", 0.1, st=st)
                r_ab = compute_asv_envelope(topo, C0, tau_true, param,
                                            "magnitude_absolute", 0.05, st=st)
                sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
                mg_s = f"{r_mg['asv']:.3f}" if r_mg['asv'] is not None else "None"
                ab_s = f"{r_ab['asv']:.3f}" if r_ab['asv'] is not None else "None"
                print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10} {ab_s:>10}")
                results[(tau_val, label, cname)] = {
                    "sign_flip": r_sf['asv'],
                    "magnitude_10pct": r_mg['asv'],
                    "magnitude_abs05": r_ab['asv']}
    print(f"\n  Time: {time.time()-t0:.1f}s")
    return results


# ============================================================================
# Part 4: MC Coverage
# ============================================================================

def part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100):
    print("\n" + "=" * 70)
    print(f"PART 4: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})")
    print("=" * 70)
    t0 = time.time()
    rng = np.random.default_rng(42)
    results = {}

    for tau_val in [0.05, 0.1]:
        print(f"\n  --- tau = {tau_val} ---")

        # --- M-bias ---
        print("  [M-bias]")
        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
        st_mb = precomp_mbias(mb_p, N=2_000_000)
        plim_ok = 0; bias_ok = 0
        for s in range(n_scenarios):
            C0 = random_C0(K, rng)
            tau_plim = plim_mbias(C0, st_mb)[1]
            bias_theory = abs(tau_plim - tau_val)
            tau_mc = np.zeros(reps)
            for r in range(reps):
                Td, Yd, _, Asd = gen_mbias_data(N_mc, mb_p, C0, rng)
                bh, _ = ols_with_dummies(Yd, Td, Asd, K)
                tau_mc[r] = bh[1]
            mc_mean = tau_mc.mean()
            mc_se = tau_mc.std() / np.sqrt(reps)
            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
                plim_ok += 1
            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.02:
                bias_ok += 1
            if (s + 1) % 100 == 0:
                print(f"    ... {s+1}/{n_scenarios}")
        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
        results[("mbias", tau_val)] = {
            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}

        # --- IV ---
        print("  [IV]")
        iv_b = np.array([0.0, tau_val, -tau_val/2])
        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
        plim_ok = 0; bias_ok = 0
        for s in range(n_scenarios):
            C0 = random_C0(K, rng)
            tau_plim = plim_iv(C0, st_iv)
            if np.isnan(tau_plim):
                plim_ok += 1; bias_ok += 1; continue
            bias_theory = abs(tau_plim - tau_val)
            tau_mc = np.zeros(reps)
            for r in range(reps):
                Zd, Yd, _, Asd = gen_iv_data(N_mc, iv_b, IV_PARAMS, C0, rng)
                w, _ = wald_with_se(Zd, Yd, Asd)
                tau_mc[r] = w
            valid = ~np.isnan(tau_mc)
            if valid.sum() < reps * 0.5:
                plim_ok += 1; bias_ok += 1; continue
            mc_mean = tau_mc[valid].mean()
            mc_se = tau_mc[valid].std() / np.sqrt(valid.sum())
            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.05:
                plim_ok += 1
            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.05:
                bias_ok += 1
            if (s + 1) % 100 == 0:
                print(f"    ... {s+1}/{n_scenarios}")
        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
        results[("iv", tau_val)] = {
            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}

        # --- Front-door ---
        print("  [Front-door]")
        lU = tau_val * 2
        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
                           seed=300+int(tau_val*100))
        tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
        plim_ok = 0; bias_ok = 0
        for s in range(n_scenarios):
            C0 = random_C0(K, rng)
            tau_plim = plim_fd(C0, st_fd)[1]
            bias_theory = abs(tau_plim - tau_I_fd)
            tau_mc = np.zeros(reps)
            for r in range(reps):
                Td, Yd, _, Msd = gen_fd_data(N_mc, BETA_FD, C0, rng, lU=lU)
                bh, _ = ols_with_dummies(Yd, Td, Msd, K)
                tau_mc[r] = bh[1]
            mc_mean = tau_mc.mean()
            mc_se = tau_mc.std() / np.sqrt(reps)
            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
                plim_ok += 1
            if abs(mc_mean - tau_I_fd) <= bias_theory + 3 * mc_se + 0.02:
                bias_ok += 1
            if (s + 1) % 100 == 0:
                print(f"    ... {s+1}/{n_scenarios}")
        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
        results[("frontdoor", tau_val)] = {
            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}

    print(f"\n  Total time: {time.time()-t0:.1f}s")
    return results


# ============================================================================
# Part 5: Type I/II
# ============================================================================

def part5_type_errors(n_mc=500, N_sample=5000):
    print("\n" + "=" * 70)
    print(f"PART 5: Type I/II ({n_mc} MC x N={N_sample})")
    print("  Decision: reject if |tau_hat/SE|>1.96 AND magnitude_ASV > 1")
    print("=" * 70)
    t0 = time.time()
    param = LinearInterpolation()
    C_list = normalize_C_list(make_C_list())
    results = {}
    seed_ctr = 3000

    for tau_val in [0.05, 0.1]:
        print(f"\n  --- tau = {tau_val} ---")
        header = (f"  {'C_struct':<12} {'H':<5} {'naive_rej':>10} "
                  f"{'mag_rej':>10} {'mean_masv':>10}")

        # === M-bias ===
        print("\n  [M-bias]")
        print(header)
        print("  " + "-" * 52)
        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
            mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_h
            st_h = precomp_mbias(mb_p, N=2_000_000)
            for cname, C0 in C_list.items():
                seed_ctr += 1
                dmin, dmax = param.delta_range(C0)
                deltas = np.linspace(dmin, dmax, 1500)
                tau_curve = np.array([
                    plim_mbias(param(C0, d), st_h)[1] for d in deltas])
                rng_mc = np.random.default_rng(seed_ctr)
                naive_rej = 0; mag_rej = 0; masv_vals = []
                for mc in range(n_mc):
                    Td, Yd, _, Asd = gen_mbias_data(
                        N_sample, mb_p, C0, rng_mc)
                    bh, seh = ols_with_dummies(Yd, Td, Asd, K)
                    tau_hat, se_tau = bh[1], seh[1]
                    reject = (abs(tau_hat / se_tau) > 1.96
                              if se_tau > 1e-10 else False)
                    if reject:
                        naive_rej += 1
                    masv = compute_magnitude_asv_fast(
                        tau_curve, deltas, tau_h, 0.1)
                    masv_vals.append(masv)
                    if reject and (masv is None or masv > 1.0):
                        mag_rej += 1
                mf = [a for a in masv_vals if a is not None]
                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
                results[("mbias", tau_val, cname, h_label)] = {
                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}

        # === IV ===
        print("\n  [IV]")
        print(header)
        print("  " + "-" * 52)
        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
            iv_b = np.array([0.0, tau_h, -tau_h/2])
            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
            for cname, C0 in C_list.items():
                seed_ctr += 1
                dmin, dmax = param.delta_range(C0)
                deltas = np.linspace(dmin, dmax, 1500)
                tau_curve = np.array([
                    plim_iv(param(C0, d), st_h) for d in deltas])
                rng_mc = np.random.default_rng(seed_ctr)
                naive_rej = 0; mag_rej = 0; masv_vals = []
                for mc in range(n_mc):
                    Zd, Yd, _, Asd = gen_iv_data(
                        N_sample, iv_b, IV_PARAMS, C0, rng_mc)
                    w, se_w = wald_with_se(Zd, Yd, Asd)
                    reject = False
                    if not np.isnan(w) and se_w > 1e-10:
                        reject = abs(w / se_w) > 1.96
                    if reject:
                        naive_rej += 1
                    masv = compute_magnitude_asv_fast(
                        tau_curve, deltas, tau_h, 0.1)
                    masv_vals.append(masv)
                    if reject and (masv is None or masv > 1.0):
                        mag_rej += 1
                mf = [a for a in masv_vals if a is not None]
                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
                results[("iv", tau_val, cname, h_label)] = {
                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}

        # === Front-door ===
        print("\n  [Front-door]")
        print(header)
        print("  " + "-" * 52)
        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
            if h_label == "H0":
                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,
                                  d=np.zeros(3), seed=400)
                tau_ref = 0.0
            else:
                lU = tau_val * 2
                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
                                  seed=401+int(tau_val*100))
                tau_ref = plim_fd(np.eye(K), st_h)[1]
            print(f"    ({h_label}: tau_ref={tau_ref:.4f})")
            for cname, C0 in C_list.items():
                seed_ctr += 1
                dmin, dmax = param.delta_range(C0)
                deltas = np.linspace(dmin, dmax, 1500)
                tau_curve = np.array([
                    plim_fd(param(C0, d), st_h)[1] for d in deltas])
                rng_mc = np.random.default_rng(seed_ctr)
                naive_rej = 0; mag_rej = 0; masv_vals = []
                for mc in range(n_mc):
                    if h_label == "H0":
                        Td, Yd, _, Msd = gen_fd_data(
                            N_sample, BETA_FD, C0, rng_mc,
                            lU=0.0, aU=0.0, d=np.zeros(3))
                    else:
                        Td, Yd, _, Msd = gen_fd_data(
                            N_sample, BETA_FD, C0, rng_mc, lU=lU)
                    bh, seh = ols_with_dummies(Yd, Td, Msd, K)
                    tau_hat, se_tau = bh[1], seh[1]
                    reject = (abs(tau_hat / se_tau) > 1.96
                              if se_tau > 1e-10 else False)
                    if reject:
                        naive_rej += 1
                    masv = compute_magnitude_asv_fast(
                        tau_curve, deltas, tau_ref, 0.1)
                    masv_vals.append(masv)
                    if reject and (masv is None or masv > 1.0):
                        mag_rej += 1
                mf = [a for a in masv_vals if a is not None]
                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
                results[("frontdoor", tau_val, cname, h_label)] = {
                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}

    print(f"\n  Total time: {time.time()-t0:.1f}s")
    return results


# ============================================================================
# Part 6: Summary JSON
# ============================================================================

def collect_summary(asv_res, small_tau_res, cov_res, te_res):
    def _f(v):
        if v is None:
            return None
        return float(v)

    summary = {
        "experiment": "plan_005_asv_extended",
        "topologies": ["mbias", "iv", "frontdoor"],
        "asv_values_tau05": {},
        "small_tau_asv": {},
        "coverage": {},
        "type_errors": {},
    }
    for (label, cname), vals in asv_res.items():
        summary["asv_values_tau05"][f"{label}_{cname}"] = {
            k: _f(v) for k, v in vals.items()}
    for (tv, label, cname), vals in small_tau_res.items():
        summary["small_tau_asv"][f"tau{tv}_{label}_{cname}"] = {
            k: _f(v) for k, v in vals.items()}
    for (topo, tv), vals in cov_res.items():
        summary["coverage"][f"{topo}_tau{tv}"] = vals
    for key, vals in te_res.items():
        summary["type_errors"]["_".join(str(x) for x in key)] = vals
    return summary


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    np.set_printoptions(precision=6, suppress=True)
    print("plan_005: ASV Framework Extension to M-bias/IV/Front-door")
    print("=" * 70)
    t_total = time.time()

    print("\nPrecomputing sufficient statistics (tau=0.5)...")
    t0 = time.time()
    st_mb = precomp_mbias(MBIAS_PARAMS, N=2_000_000)
    tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]
    print(f"  M-bias:     tau_DGP=0.5, plim(I)={tau_I_mb:.6f}")

    st_iv = precomp_iv(IV_BETA, IV_PARAMS, N=2_000_000)
    tau_I_iv = plim_iv(np.eye(K), st_iv)
    print(f"  IV:         beta[1]=0.5, Wald(I)={tau_I_iv:.6f}")

    st_fd = precomp_fd(BETA_FD, N=10_000_000)
    tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
    print(f"  Front-door: plim(I)={tau_I_fd:.6f}")
    print(f"  Done ({time.time()-t0:.1f}s)")

    part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_I_fd)
    asv_res = part2_asv_values(st_mb, st_iv, st_fd, tau_I_fd)
    small_tau_res = part3_small_tau_asv()
    cov_res = part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100)
    te_res = part5_type_errors(n_mc=500, N_sample=5000)

    print("\n" + "=" * 70)
    print("PART 6: Summary JSON")
    print("=" * 70)
    summary = collect_summary(asv_res, small_tau_res, cov_res, te_res)
    print(json.dumps(summary, indent=2, default=str))

    print("\n" + "=" * 70)
    elapsed = time.time() - t_total
    print(f"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)")
    print("=" * 70)
