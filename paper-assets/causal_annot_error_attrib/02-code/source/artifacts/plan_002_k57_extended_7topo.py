#!/usr/bin/env python3
"""
Plan 002 Extended: All 7 topologies × K={3,5,7}

Topologies:
  1. Confounding: A→T, A→Y, T→Y
  2. Mediation: T→A→Y
  3. Collider: T→A←Y
  4. Exposure: A→Y
  5. M-bias: U1→{A,T}, U2→{A,Y}, T→Y
  6. IV: Z→A→Y, U→{A,Y}
  7. Front-door: T→M→Y, U→{T,Y}

For each topology × K: 100k random K×K confusion matrices (Dirichlet),
plim-based bias metrics including tau_specific_sign_flip (key paper claim).
"""

import torch
import numpy as np
import time
import os
import sys

K_VALUES = [3, 5, 7]
N_RANDOM = 100_000
N_LARGE = 5_000_000
SEED = 42
DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
DTYPE = torch.float64
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ================================================================
# Parameter Pools (K=3 values match plan_001 exactly)
# ================================================================
_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
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
        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K-1]),
                         beta_A=np.array(_BETA_A_POOL[:K-1]), beta_T=2.0, sigma_T=1.0),
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


# ================================================================
# DGP Generators
# ================================================================
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
    logits = p['g'][None, :] + p['dT'][None, :] * T[:, None] + p['dY'][None, :] * Y[:, None]
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


_GEN_OLS = dict(confounding=gen_confounding, mediation=gen_mediation,
                collider=gen_collider, mbias=gen_mbias, frontdoor=gen_frontdoor)


# ================================================================
# Sufficient Statistics
# ================================================================
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

    def to_device(self, dev):
        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)
        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)
        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)
        if self.has_T:
            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)
            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)
            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)
            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)
        return self


class IVSuffStats:
    def __init__(self, Z, Y, A, K):
        self.K = K
        z1 = Z == 1; z0 = Z == 0
        self.RF = Y[z1].mean() - Y[z0].mean()
        self.FS = np.zeros(K)
        for k in range(K):
            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()

    def to_device(self, dev):
        self.t_RF = torch.tensor(self.RF, dtype=DTYPE, device=dev)
        self.t_FS = torch.tensor(self.FS, dtype=DTYPE, device=dev)
        return self


# ================================================================
# GPU-Batched Plim
# ================================================================
def plim_with_T(ss, C):
    B, K = C.shape[0], ss.K
    dim = K + 1
    q = C @ ss.t_p_A
    ct = C @ ss.t_E_TD
    cy = C @ ss.t_E_YD
    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1] = ss.t_E_T; EZZ[:, 1, 0] = ss.t_E_T
    EZZ[:, 1, 1] = ss.t_E_T2
    EZZ[:, 0, 2:] = q[:, 1:]; EZZ[:, 2:, 0] = q[:, 1:]
    EZZ[:, 1, 2:] = ct[:, 1:]; EZZ[:, 2:, 1] = ct[:, 1:]
    idx = torch.arange(K - 1, device=C.device)
    EZZ[:, idx + 2, idx + 2] = q[:, 1:]
    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
    EZY[:, 0] = ss.t_E_Y; EZY[:, 1] = ss.t_E_TY; EZY[:, 2:] = cy[:, 1:]
    return torch.linalg.solve(EZZ, EZY)


def plim_exposure(ss, C):
    B, K = C.shape[0], ss.K
    dim = K
    q = C @ ss.t_p_A
    cy = C @ ss.t_E_YD
    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1:] = q[:, 1:]; EZZ[:, 1:, 0] = q[:, 1:]
    idx = torch.arange(K - 1, device=C.device)
    EZZ[:, idx + 1, idx + 1] = q[:, 1:]
    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
    EZY[:, 0] = ss.t_E_Y; EZY[:, 1:] = cy[:, 1:]
    return torch.linalg.solve(EZZ, EZY)


def plim_iv_batched(ss, C):
    FS_star = C @ ss.t_FS
    denom = FS_star[:, 1]
    nan_val = torch.tensor(float('nan'), dtype=DTYPE, device=C.device)
    result = torch.where(denom.abs() < 1e-8, nan_val, ss.t_RF / denom)
    return result.unsqueeze(1)


# ================================================================
# Random C Generation
# ================================================================
def gen_random_C(K, N, device, seed=SEED, min_diag=None):
    rng = np.random.default_rng(seed)
    C = np.zeros((N, K, K))
    if min_diag is not None and min_diag > 0:
        for j in range(K):
            diag = rng.uniform(min_diag, 1.0, N)
            offdiag = rng.dirichlet(np.ones(K - 1), N) * (1.0 - diag)[:, None]
            col = np.zeros((N, K))
            col[:, j] = diag
            off_idx = 0
            for i in range(K):
                if i != j:
                    col[:, i] = offdiag[:, off_idx]
                    off_idx += 1
            C[:, :, j] = col
    else:
        for j in range(K):
            C[:, :, j] = rng.dirichlet(np.ones(K), N)
    return torch.tensor(C, dtype=DTYPE, device=device)


# ================================================================
# Metrics (threshold=0.01 for violation, matching plan_001)
# ================================================================
def compute_metrics(plim_batch, plim_true, tau_idx=None):
    valid = torch.isfinite(plim_batch).all(dim=1)
    n_valid = valid.sum().item()
    if n_valid == 0:
        base = {k: float('nan') for k in
                ['violation', 'sign_flip', 'amplification']}
        base['n_valid'] = 0
        return base

    pb = plim_batch[valid]
    diff = pb - plim_true.unsqueeze(0)

    violation = (diff.abs() > 0.01).any(dim=1).float().mean().item()

    nz = plim_true.abs() > 1e-6
    if nz.any():
        sign_flip = ((torch.sign(pb[:, nz]) != torch.sign(plim_true[nz]).unsqueeze(0))
                     ).any(dim=1).float().mean().item()
    else:
        sign_flip = 0.0

    amplification = (pb.abs() > plim_true.abs().unsqueeze(0) + 1e-6
                     ).any(dim=1).float().mean().item()

    m = dict(violation=violation, sign_flip=sign_flip,
             amplification=amplification, n_valid=n_valid)

    if tau_idx is not None:
        tb = pb[:, tau_idx]
        tt = plim_true[tau_idx]
        td = tb - tt
        m['tau_violation'] = (td.abs() > 0.01).float().mean().item()
        m['tau_sign_flip'] = (
            (torch.sign(tb) != torch.sign(tt)) & (tt.abs() > 1e-6)
        ).float().mean().item()
        m['tau_amplification'] = (tb.abs() > tt.abs() + 1e-6).float().mean().item()
        m['tau_bias_mean'] = td.mean().item()
        m['tau_bias_std'] = td.std().item()
        m['tau_bias_max'] = td.abs().max().item()
    return m


# ================================================================
# Worst-case bounds (diag >= threshold)
# ================================================================
def worst_case_ols(plim_fn, ss, K, device, tau_idx=1, thresholds=(0.5, 0.7, 0.9)):
    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
    plim_I = plim_fn(ss, I_batch).squeeze(0)
    results = {}
    for thr in thresholds:
        Cb = gen_random_C(K, 50_000, device, seed=SEED + int(thr * 1000), min_diag=thr)
        pb = plim_fn(ss, Cb)
        valid = torch.isfinite(pb).all(dim=1)
        pb_v = pb[valid]
        if len(pb_v) == 0:
            results[thr] = dict(max_bias=float('nan'), mean_bias=float('nan'), p95_bias=float('nan'))
            continue
        bias = (pb_v[:, tau_idx] - plim_I[tau_idx]).abs()
        results[thr] = dict(
            max_bias=bias.max().item(),
            mean_bias=bias.mean().item(),
            p95_bias=torch.quantile(bias, 0.95).item(),
        )
    return results


def worst_case_iv(ss, K, device, thresholds=(0.5, 0.7, 0.9)):
    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
    tau_I = plim_iv_batched(ss, I_batch)[0, 0]
    results = {}
    for thr in thresholds:
        Cb = gen_random_C(K, 50_000, device, seed=SEED + int(thr * 1000), min_diag=thr)
        pb = plim_iv_batched(ss, Cb)[:, 0]
        valid = torch.isfinite(pb)
        pb_v = pb[valid]
        if len(pb_v) == 0:
            results[thr] = dict(max_bias=float('nan'), mean_bias=float('nan'), p95_bias=float('nan'))
            continue
        bias = (pb_v - tau_I).abs()
        results[thr] = dict(
            max_bias=bias.max().item(),
            mean_bias=bias.mean().item(),
            p95_bias=torch.quantile(bias, 0.95).item(),
        )
    return results


# ================================================================
# Main
# ================================================================
def main():
    t0 = time.time()
    print("=" * 100)
    print("  PLAN 002 EXTENDED: 7 TOPOLOGIES x K={3,5,7}")
    print("=" * 100)
    print(f"  Device: {DEVICE}")
    if DEVICE.type == 'cuda':
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
        print(f"  VRAM: {torch.cuda.get_device_properties(0).total_mem // 1024**3} GB")
    print(f"  N_random={N_RANDOM:,}, N_large={N_LARGE:,}, seed={SEED}")
    sys.stdout.flush()

    ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
                 'mbias', 'iv', 'frontdoor']
    all_results = {}

    for K in K_VALUES:
        params = make_all_params(K)
        print(f"\n{'='*100}")
        print(f"  K = {K}")
        print(f"{'='*100}")
        sys.stdout.flush()

        for topo in ALL_TOPOS:
            tk = time.time()
            p = params[topo]

            if topo == 'iv':
                rng = np.random.default_rng(SEED)
                Z, Y, A = gen_iv(K, N_LARGE, p, rng)
                ss = IVSuffStats(Z, Y, A, K).to_device(DEVICE)

                I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
                tau_true_t = plim_iv_batched(ss, I_batch)[0, 0]
                tau_true = tau_true_t.item()

                C_rand = gen_random_C(K, N_RANDOM, DEVICE, seed=SEED)
                plim_all = plim_iv_batched(ss, C_rand)
                metrics = compute_metrics(plim_all, tau_true_t.unsqueeze(0), tau_idx=0)

                wc = worst_case_iv(ss, K, DEVICE)
                metrics['worst_case'] = wc
                all_results[f"{topo}_K{K}"] = metrics

                print(f"\n  {topo} K={K}: tau_true(Wald)={tau_true:.6f}  "
                      f"RF={ss.RF:.6f}  FS={np.array2string(ss.FS, precision=4)}  "
                      f"valid={metrics['n_valid']}/{N_RANDOM}")

            elif topo == 'exposure':
                rng = np.random.default_rng(SEED)
                _, Y, A = gen_exposure(K, N_LARGE, p, rng)
                ss = SuffStats(None, Y, A, K).to_device(DEVICE)

                I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
                plim_true = plim_exposure(ss, I_batch).squeeze(0)

                C_rand = gen_random_C(K, N_RANDOM, DEVICE, seed=SEED)
                plim_all = plim_exposure(ss, C_rand)
                metrics = compute_metrics(plim_all, plim_true, tau_idx=None)

                wc = worst_case_ols(plim_exposure, ss, K, DEVICE, tau_idx=1)
                metrics['worst_case'] = wc
                all_results[f"{topo}_K{K}"] = metrics
                tau_true = plim_true[1].item()

                print(f"\n  {topo} K={K}: plim_true={plim_true.cpu().numpy()}")

            else:
                rng = np.random.default_rng(SEED)
                T, Y, A = _GEN_OLS[topo](K, N_LARGE, p, rng)
                ss = SuffStats(T, Y, A, K).to_device(DEVICE)

                I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
                plim_true = plim_with_T(ss, I_batch).squeeze(0)
                tau_true = plim_true[1].item()

                C_rand = gen_random_C(K, N_RANDOM, DEVICE, seed=SEED)
                plim_all = plim_with_T(ss, C_rand)
                metrics = compute_metrics(plim_all, plim_true, tau_idx=1)

                wc = worst_case_ols(plim_with_T, ss, K, DEVICE, tau_idx=1)
                metrics['worst_case'] = wc
                all_results[f"{topo}_K{K}"] = metrics

                print(f"\n  {topo} K={K}: tau_true={tau_true:.6f}")

            m = metrics
            def _pct(x): return f"{x:.1%}" if x == x else "nan"

            print(f"    all_coef: violation={_pct(m['violation'])}  "
                  f"sign_flip={_pct(m['sign_flip'])}  amplif={_pct(m['amplification'])}")
            if 'tau_violation' in m:
                print(f"    tau_spec: violation={_pct(m['tau_violation'])}  "
                      f"sign_flip={_pct(m['tau_sign_flip'])}  amplif={_pct(m['tau_amplification'])}")
                print(f"    tau_bias: mean={m['tau_bias_mean']:.6f}  "
                      f"std={m['tau_bias_std']:.6f}  max={m['tau_bias_max']:.6f}")
            for thr, wv in m.get('worst_case', {}).items():
                print(f"    worst-case (diag>={thr}): max|dt|={wv['max_bias']:.6f}  "
                      f"mean={wv['mean_bias']:.6f}  P95={wv['p95_bias']:.6f}")
            print(f"    [{time.time()-tk:.1f}s]")
            sys.stdout.flush()

    # ================================================================
    # Summary Table
    # ================================================================
    print(f"\n{'='*140}")
    print("  COMPLETE 7-TOPOLOGY x K={{3,5,7}} COMPARISON")
    print(f"{'='*140}")

    hdr = (f"  {'Topology':<14} {'K':>3} {'t_spec_sflip':>14} {'all_sflip':>11} "
           f"{'violation':>11} {'amplif':>11} {'WC_d50':>10} {'WC_d70':>10} {'WC_d90':>10}")
    print(hdr)
    print(f"  {'-'*105}")

    for topo in ALL_TOPOS:
        for K_val in K_VALUES:
            m = all_results[f"{topo}_K{K_val}"]
            ts = m.get('tau_sign_flip', m.get('sign_flip', float('nan')))
            sf = m.get('sign_flip', float('nan'))
            v = m.get('tau_violation', m.get('violation', float('nan')))
            a = m.get('tau_amplification', m.get('amplification', float('nan')))

            wc = m.get('worst_case', {})
            wc50 = wc.get(0.5, {}).get('max_bias', float('nan'))
            wc70 = wc.get(0.7, {}).get('max_bias', float('nan'))
            wc90 = wc.get(0.9, {}).get('max_bias', float('nan'))

            def _f(x, w=11):
                return f"{x:>{w}.1%}" if x == x else f"{'nan':>{w}}"
            def _fw(x, w=10):
                return f"{x:>{w}.4f}" if x == x else f"{'nan':>{w}}"

            print(f"  {topo:<14} {K_val:>3} {_f(ts,14)} {_f(sf)} "
                  f"{_f(v)} {_f(a)} {_fw(wc50)} {_fw(wc70)} {_fw(wc90)}")
        print()

    # K-trend analysis
    print("  K-TREND ANALYSIS (tau_specific_sign_flip)")
    for topo in ALL_TOPOS:
        vals = []
        for K_val in K_VALUES:
            m = all_results[f"{topo}_K{K_val}"]
            v = m.get('tau_sign_flip', m.get('sign_flip', 0.0))
            vals.append(v if v == v else 0.0)
        d = vals[-1] - vals[0]
        trend = "WORSENS" if d > 0.005 else ("STABLE" if abs(d) <= 0.005 else "IMPROVES")
        print(f"  {topo:<14}: K=3 {vals[0]:.1%} -> K=5 {vals[1]:.1%} -> K=7 {vals[2]:.1%}  [{trend}]")

    print(f"\nTotal: {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
