#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plan 002: K={3,5,7} Bias Taxonomy Extension

Extends plan_001's K=3 bias analysis to general K across 4 core DAG topologies.
For each topology x K, generates 100k random K×K confusion matrices (Dirichlet),
computes plim via pre-computed sufficient statistics, and reports violation/sign-flip/
amplification rates. Includes eigendecomposition, worst-case bounds, and sensitivity
heatmaps as interpretability tools.

Input:  DGP parameters per topology (auto-generated for each K)
Output: Cross-K comparison tables, sensitivity heatmaps (PNG)

Dependencies: torch (GPU), numpy, matplotlib
"""

import torch
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time
import os
import sys

# ================================================================
# Configuration
# ================================================================
K_VALUES = [3, 5, 7]
N_RANDOM = 100_000
N_LARGE = 5_000_000
SEED = 42
DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
DTYPE = torch.float64
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ================================================================
# DGP Parameters for general K
# ================================================================
# Base coefficient pools — K=3 values match plan_001 exactly,
# K=5,7 extend with alternating-sign decreasing magnitudes.
_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]


def make_p_A(K):
    """Slightly imbalanced category probabilities."""
    if K == 3:
        return np.array([0.40, 0.35, 0.25])
    raw = np.array([1.0 / i for i in range(1, K + 1)])
    return raw / raw.sum()


def make_params(K):
    """DGP parameters for all topologies at given K."""
    p_A = make_p_A(K)

    conf = dict(
        p_A=p_A,
        alpha=np.array(_ALPHA_POOL[:K-1]),
        beta_A=np.array(_BETA_A_POOL[:K-1]),
        beta_T=2.0,
        sigma_T=1.0,
    )

    med = dict(
        tau=0.5,
        gamma=np.array(_GAMMA_POOL[:K]),
        delta=np.array(_DELTA_POOL[:K]),
        beta=np.array(_BETA_POOL[:K]),
    )

    coll = dict(
        tau=1.0,
        g=np.zeros(K),
        dT=np.array(_DT_POOL[:K]),
        dY=np.array(_DY_POOL[:K]),
    )

    exp = dict(
        beta=np.array(_BETA_POOL[:K]),
        p_A=p_A,
    )

    return dict(confounding=conf, mediation=med, collider=coll, exposure=exp)


# ================================================================
# DGP Generators
# ================================================================
def _softmax_rows(logits):
    e = np.exp(logits - logits.max(axis=-1, keepdims=True))
    return e / e.sum(axis=-1, keepdims=True)


def _sample_cat(probs, rng):
    """Sample from row-wise categorical probabilities [N, K]."""
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=probs.shape[0])[:, None]
    return (u >= cum).sum(axis=1).astype(int)


def gen_confounding(K, N, p, rng):
    """A→T, A→Y, T→Y. Researcher omits true A, uses A*."""
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
    return T, Y, A


def gen_mediation(K, N, p, rng):
    """T→A→Y. A mediates T's effect; researcher controls for A*."""
    T = rng.binomial(1, 0.5, N).astype(float)
    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
    probs = _softmax_rows(logits)
    A = _sample_cat(probs, rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
    return T, Y, A


def gen_collider(K, N, p, rng):
    """T→A←Y. Controlling for collider A* opens a backdoor path."""
    T = rng.normal(0, 1, N)
    Y = p['tau'] * T + rng.normal(0, 1, N)
    logits = (p['g'][None, :]
              + p['dT'][None, :] * T[:, None]
              + p['dY'][None, :] * Y[:, None])
    probs = _softmax_rows(logits)
    A = _sample_cat(probs, rng)
    return T, Y, A


def gen_exposure(K, N, p, rng):
    """A→Y. A is the treatment of interest."""
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
    return None, Y, A


_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,
            collider=gen_collider, exposure=gen_exposure)


# ================================================================
# Sufficient Statistics
# ================================================================
class SuffStats:
    """Pre-compute population moments from a large DGP sample.

    Stores:
      p_A[k]   = P(A=k)
      E_Y      = E[Y]
      E_YD[k]  = E[Y · 1(A=k)]
    For topologies with T:
      E_T, E_T2, E_TY, E_TD[k] = E[T · 1(A=k)]
    """

    def __init__(self, T, Y, A, K):
        self.K = K
        self.has_T = T is not None

        self.p_A = np.array([(A == k).mean() for k in range(K)])
        self.E_Y = Y.mean()
        self.E_YD = np.array([(Y * (A == k)).mean() for k in range(K)])

        if self.has_T:
            self.E_T = T.mean()
            self.E_T2 = (T ** 2).mean()
            self.E_TY = (T * Y).mean()
            self.E_TD = np.array([(T * (A == k)).mean() for k in range(K)])

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


# ================================================================
# GPU-Batched Plim
# ================================================================
def plim_with_T(ss, C):
    """Batched plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.

    Generalizes K=3 plan_001 formula. Z* = (1, T, D*_1,...,D*_{K-1}).
    plim = (E[Z*'Z*])^{-1} E[Z*'Y].

    E[Z*'Z*] and E[Z*'Y] depend on C through:
      q = C @ p_A              (marginal of A*)
      E[T·D*_j] = (C @ E_TD)[j]
      E[Y·D*_j] = (C @ E_YD)[j]
      E[D*_i·D*_j] = q[i] δ_{ij}  (A* is categorical)

    Args:
        ss: SuffStats on device
        C:  [B, K, K] confusion matrices
    Returns:
        [B, K+1] plim coefficients
    """
    B, K = C.shape[0], ss.K
    dim = K + 1

    q = C @ ss.t_p_A                   # [B, K]
    ct = C @ ss.t_E_TD                 # [B, K]
    cy = C @ ss.t_E_YD                 # [B, K]

    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1] = ss.t_E_T
    EZZ[:, 1, 0] = ss.t_E_T
    EZZ[:, 1, 1] = ss.t_E_T2
    EZZ[:, 0, 2:] = q[:, 1:]
    EZZ[:, 2:, 0] = q[:, 1:]
    EZZ[:, 1, 2:] = ct[:, 1:]
    EZZ[:, 2:, 1] = ct[:, 1:]
    idx = torch.arange(K - 1, device=C.device)
    EZZ[:, idx + 2, idx + 2] = q[:, 1:]

    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
    EZY[:, 0] = ss.t_E_Y
    EZY[:, 1] = ss.t_E_TY
    EZY[:, 2:] = cy[:, 1:]

    return torch.linalg.solve(EZZ, EZY)


def plim_exposure(ss, C):
    """Batched plim for Y ~ 1 + D*_1 + ... + D*_{K-1} (no T).

    Same moment algebra as plim_with_T but without the T row/column.
    """
    B, K = C.shape[0], ss.K
    dim = K

    q = C @ ss.t_p_A
    cy = C @ ss.t_E_YD

    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1:] = q[:, 1:]
    EZZ[:, 1:, 0] = q[:, 1:]
    idx = torch.arange(K - 1, device=C.device)
    EZZ[:, idx + 1, idx + 1] = q[:, 1:]

    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
    EZY[:, 0] = ss.t_E_Y
    EZY[:, 1:] = cy[:, 1:]

    return torch.linalg.solve(EZZ, EZY)


# ================================================================
# Random C Generation
# ================================================================
def gen_random_C(K, N, device, seed=SEED, min_diag=None):
    """Sample N column-stochastic K×K matrices via Dirichlet(1,...,1).

    Each column independently drawn. If min_diag is set, each diagonal
    element is drawn from U[min_diag, 1] and the remaining mass is
    distributed Dirichlet among off-diagonal entries.
    """
    rng = np.random.default_rng(seed)
    C = np.zeros((N, K, K))

    if min_diag is not None and min_diag > 0:
        for j in range(K):
            diag = rng.uniform(min_diag, 1.0, N)
            offdiag = rng.dirichlet(np.ones(K - 1), N) * (1.0 - diag)[:, None]
            col = np.zeros((N, K))
            col[:, j] = diag
            idx = 0
            for i in range(K):
                if i != j:
                    col[:, i] = offdiag[:, idx]
                    idx += 1
            C[:, :, j] = col
    else:
        for j in range(K):
            C[:, :, j] = rng.dirichlet(np.ones(K), N)

    return torch.tensor(C, dtype=DTYPE, device=device)


# ================================================================
# Metrics
# ================================================================
def compute_metrics(plim_batch, plim_true, tau_idx=None):
    """Violation / sign-flip / amplification rates.

    tau_idx: index of τ coefficient (1 for topologies with T, None for exposure).
    """
    diff = plim_batch - plim_true.unsqueeze(0)

    violation = (diff.abs() > 1e-8).any(dim=1).float().mean().item()

    s0 = torch.sign(plim_true).unsqueeze(0)
    s1 = torch.sign(plim_batch)
    sign_flip = ((s0 != s1) & (s0 != 0) & (s1 != 0)).any(dim=1).float().mean().item()

    amplification = (plim_batch.abs() > plim_true.abs().unsqueeze(0) + 1e-10
                     ).any(dim=1).float().mean().item()

    m = dict(violation=violation, sign_flip=sign_flip, amplification=amplification)

    if tau_idx is not None:
        tb = plim_batch[:, tau_idx]
        tt = plim_true[tau_idx]
        td = tb - tt
        m['tau_violation'] = (td.abs() > 1e-8).float().mean().item()
        m['tau_sign_flip'] = ((torch.sign(tb) != torch.sign(tt)) &
                              (torch.sign(tt) != 0) &
                              (torch.sign(tb) != 0)).float().mean().item()
        m['tau_amplification'] = (tb.abs() > tt.abs() + 1e-10).float().mean().item()
        m['tau_bias_mean'] = td.mean().item()
        m['tau_bias_std'] = td.std().item()
        m['tau_bias_max'] = td.abs().max().item()
    return m


# ================================================================
# MC Verification (small-scale, a few named C matrices)
# ================================================================
def mc_verify(K, topo, params, C_np, n_reps=500, n_mc=10_000, seed=0):
    """Monte Carlo OLS estimate of plim for a single C, as validation."""
    gen_fn = _GEN[topo]
    coefs = []
    for r in range(n_reps):
        rng = np.random.default_rng(seed + r)
        T, Y, A = gen_fn(K, n_mc, params, rng)

        # Misclassify
        probs = C_np[:, A]       # [K, N]
        cum = np.cumsum(probs, axis=0)
        u = rng.uniform(size=n_mc)
        Astar = np.zeros(n_mc, dtype=int)
        for k in range(K - 1):
            Astar += (u >= cum[k]).astype(int)

        Dstar = np.zeros((n_mc, K - 1))
        for j in range(K - 1):
            Dstar[:, j] = (Astar == j + 1).astype(float)

        ones = np.ones((n_mc, 1))
        if T is not None:
            Z = np.hstack([ones, T[:, None], Dstar])
        else:
            Z = np.hstack([ones, Dstar])
        b = np.linalg.lstsq(Z, Y, rcond=None)[0]
        coefs.append(b)
    return np.mean(coefs, axis=0), np.std(coefs, axis=0) / np.sqrt(n_reps)


# ================================================================
# Interpretability (a): Eigendecomposition of bias vectors
# ================================================================
def eigen_analysis(plim_batch, plim_true):
    """PCA on bias = plim(C) - plim(I). Returns top-3 variance ratios.

    The bias vectors live in R^{K+1} (or R^K for exposure).
    Eigendecomposition of bias covariance identifies which linear
    combinations of coefficients carry most of the bias variance.
    """
    bias = (plim_batch - plim_true.unsqueeze(0)).cpu().numpy()
    bias_c = bias - bias.mean(axis=0)
    _, S, Vt = np.linalg.svd(bias_c, full_matrices=False)
    var = S ** 2
    ratios = var / var.sum()
    return ratios[:min(3, len(ratios))]


# ================================================================
# Interpretability (b): Worst-case bounds under diagonal constraint
# ================================================================
def worst_case_bounds(ss, plim_fn, K, device, thresholds=(0.5, 0.7, 0.9)):
    """max|τ̂ − τ_true| over column-stochastic C with min diag(C) ≥ thr.

    For each threshold, sample 50k constrained C matrices and report
    the maximum, mean, and 95th-percentile |bias|.
    """
    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
    plim_I = plim_fn(ss, I_batch).squeeze(0)
    has_T = plim_I.shape[0] > K
    idx = 1 if has_T else 1

    results = {}
    for thr in thresholds:
        Cb = gen_random_C(K, 50_000, device, seed=SEED + int(thr * 1000), min_diag=thr)
        pb = plim_fn(ss, Cb)
        valid = torch.isfinite(pb).all(dim=1)
        pb = pb[valid]
        if has_T:
            bias = (pb[:, idx] - plim_I[idx]).abs()
        else:
            bias = (pb[:, 1:] - plim_I[1:].unsqueeze(0)).abs().max(dim=1).values
        results[thr] = dict(
            max_bias=bias.max().item(),
            mean_bias=bias.mean().item(),
            p95_bias=torch.quantile(bias, 0.95).item(),
        )
    return results


# ================================================================
# Interpretability (c): Sensitivity heatmap via finite differences
# ================================================================
def sensitivity_heatmap(ss, plim_fn, K, device, out_path, topo_name):
    """∂|bias(τ)|/∂C_ij evaluated at C = I via finite differences.

    For off-diagonal (i,j): perturb C[i,j] += δ and C[j,j] -= δ to keep
    column j stochastic. Measures which misclassification patterns most
    affect the τ estimate.
    """
    delta = 0.01
    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
    plim_I = plim_fn(ss, I_batch).squeeze(0)
    has_T = plim_I.shape[0] > K
    tau_idx = 1 if has_T else 1
    tau_I = plim_I[tau_idx].item()

    sens = np.zeros((K, K))
    for i in range(K):
        for j in range(K):
            if i == j:
                continue
            C = torch.eye(K, dtype=DTYPE, device=device)
            C[i, j] += delta
            C[j, j] -= delta
            p = plim_fn(ss, C.unsqueeze(0)).squeeze(0)
            sens[i, j] = abs(p[tau_idx].item() - tau_I) / delta

    fig, ax = plt.subplots(figsize=(max(3.5, K * 0.7), max(3.5, K * 0.7)))
    im = ax.imshow(sens, cmap='YlOrRd', aspect='equal')
    ax.set_xlabel('True category j')
    ax.set_ylabel('Observed category i')
    ax.set_title(f'{topo_name} K={K}: |∂bias(τ)/∂C_ij|')
    ax.set_xticks(range(K))
    ax.set_yticks(range(K))
    for i in range(K):
        for j in range(K):
            color = 'w' if sens[i, j] > sens.max() * 0.6 else 'k'
            ax.text(j, i, f'{sens[i,j]:.3f}', ha='center', va='center',
                    fontsize=max(5, 8 - K), color=color)
    plt.colorbar(im, ax=ax, shrink=0.8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return sens


# ================================================================
# Main
# ================================================================
def main():
    t0 = time.time()
    print("=" * 90)
    print("  Plan 002: K={3,5,7} Bias Taxonomy Extension")
    print("=" * 90)
    print(f"Device: {DEVICE}")
    if torch.cuda.is_available():
        gp = torch.cuda.get_device_properties(0)
        print(f"GPU: {gp.name}  ({gp.total_memory / 1024**3:.1f} GB)")
    print(f"N_RANDOM={N_RANDOM:,}  N_LARGE={N_LARGE:,}")

    topologies = ['confounding', 'mediation', 'collider', 'exposure']
    all_results = {}

    # ------------------------------------------------------------------
    # Named C matrices for MC verification (K=3 only, matching plan_001)
    # ------------------------------------------------------------------
    C_named_3 = {
        'sym_high': np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]]),
        'weak_diag': np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]]),
    }

    for topo in topologies:
        print(f"\n{'=' * 90}")
        print(f"  TOPOLOGY: {topo.upper()}")
        print(f"{'=' * 90}")

        plim_fn = plim_exposure if topo == 'exposure' else plim_with_T
        tau_idx = None if topo == 'exposure' else 1

        for K in K_VALUES:
            print(f"\n  --- K={K} ---")
            tk = time.time()

            params = make_params(K)
            p = params[topo]
            rng = np.random.default_rng(SEED)

            # 1. Large DGP → sufficient statistics
            T, Y, A = _GEN[topo](K, N_LARGE, p, rng)
            ss = SuffStats(T, Y, A, K).to_device(DEVICE)
            print(f"  p_A = {ss.p_A}")
            if ss.has_T:
                print(f"  E[T]={ss.E_T:.4f}  E[T²]={ss.E_T2:.4f}  E[TY]={ss.E_TY:.4f}")

            # 2. plim(I) = τ_true
            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
            plim_true = plim_fn(ss, I_batch).squeeze(0)
            print(f"  plim(I) = {plim_true.cpu().numpy()}")

            # 3. MC verification for K=3
            if K == 3:
                print(f"\n  MC Verification (K=3, 500 reps × 10k samples):")
                for cn, Cnp in C_named_3.items():
                    Ct = torch.tensor(Cnp, dtype=DTYPE, device=DEVICE).unsqueeze(0)
                    th = plim_fn(ss, Ct).squeeze(0).cpu().numpy()
                    mc, se = mc_verify(K, topo, p, Cnp)
                    match = np.abs(th - mc) < 2.5 * se
                    tag = ''.join('✓' if m else '✗' for m in match)
                    print(f"    {cn:<10}  theory={th}  MC={mc}  {tag}")

            # 4. Random C search
            C_batch = gen_random_C(K, N_RANDOM, DEVICE)
            plim_all = plim_fn(ss, C_batch)

            valid = torch.isfinite(plim_all).all(dim=1)
            n_valid = valid.sum().item()
            if n_valid < N_RANDOM:
                print(f"  WARNING: {N_RANDOM - n_valid} singular, using {n_valid}")
                plim_all = plim_all[valid]

            metrics = compute_metrics(plim_all, plim_true, tau_idx=tau_idx)
            key = f"{topo}_K{K}"
            all_results[key] = metrics

            print(f"\n  Overall: violation={metrics['violation']:.1%}  "
                  f"sign_flip={metrics['sign_flip']:.1%}  "
                  f"amplification={metrics['amplification']:.1%}")
            if tau_idx is not None:
                print(f"  τ-specific: violation={metrics['tau_violation']:.1%}  "
                      f"sign_flip={metrics['tau_sign_flip']:.1%}  "
                      f"amplification={metrics['tau_amplification']:.1%}")
                print(f"  τ bias: mean={metrics['tau_bias_mean']:+.6f}  "
                      f"std={metrics['tau_bias_std']:.6f}  "
                      f"max={metrics['tau_bias_max']:.6f}")

            # 5. Eigendecomposition
            top3 = eigen_analysis(plim_all, plim_true)
            print(f"  Eigen top-{len(top3)} var explained: "
                  + '  '.join(f'{v:.1%}' for v in top3))

            # 6. Worst-case bounds
            wc = worst_case_bounds(ss, plim_fn, K, DEVICE)
            for thr, v in wc.items():
                print(f"  Worst-case (diag≥{thr}): "
                      f"max|Δτ|={v['max_bias']:.6f}  "
                      f"mean={v['mean_bias']:.6f}  "
                      f"P95={v['p95_bias']:.6f}")

            # 7. Sensitivity heatmap
            hm_path = os.path.join(OUT_DIR, f"plan002_sensitivity_{topo}_K{K}.png")
            sensitivity_heatmap(ss, plim_fn, K, DEVICE, hm_path, topo)
            print(f"  Heatmap → {os.path.basename(hm_path)}")

            print(f"  [{time.time() - tk:.1f}s]")

    # ==================================================================
    # Cross-K Summary
    # ==================================================================
    print(f"\n{'=' * 90}")
    print("  CROSS-K COMPARISON")
    print(f"{'=' * 90}")

    hdr = (f"  {'Topology':<14} {'K':>3}"
           f" {'violat':>8} {'sflip':>8} {'amplif':>8}"
           f" {'τ_viol':>8} {'τ_sflip':>8} {'τ_amp':>8}")
    print(hdr)
    print(f"  {'-' * 73}")

    for topo in topologies:
        for K in K_VALUES:
            m = all_results[f"{topo}_K{K}"]
            tv = m.get('tau_violation', None)
            ts = m.get('tau_sign_flip', None)
            ta = m.get('tau_amplification', None)
            tvs = f"{tv:.1%}" if tv is not None else "  —"
            tss = f"{ts:.1%}" if ts is not None else "  —"
            tas = f"{ta:.1%}" if ta is not None else "  —"
            print(f"  {topo:<14} {K:>3}"
                  f" {m['violation']:>8.1%} {m['sign_flip']:>8.1%}"
                  f" {m['amplification']:>8.1%}"
                  f" {tvs:>8} {tss:>8} {tas:>8}")
        print()

    # Trend analysis
    print("  K-TREND ANALYSIS (does bias worsen with K?)")
    for topo in topologies:
        if topo == 'exposure':
            vals = [all_results[f"{topo}_K{K}"]['violation'] for K in K_VALUES]
            label = 'violation'
        else:
            vals = [all_results[f"{topo}_K{K}"]['tau_violation'] for K in K_VALUES]
            label = 'τ_violation'
        d = vals[-1] - vals[0]
        trend = "WORSENS" if d > 0.01 else ("STABLE" if abs(d) <= 0.01 else "IMPROVES")
        print(f"  {topo:<14} ({label}): "
              f"K=3 {vals[0]:.1%} → K=5 {vals[1]:.1%} → K=7 {vals[2]:.1%}  [{trend}]")

    # ==================================================================
    # Combined sensitivity figure (K=5 and K=7 side by side per topology)
    # ==================================================================
    fig, axes = plt.subplots(len(topologies), 2, figsize=(12, 4 * len(topologies)))
    for row, topo in enumerate(topologies):
        for col, K in enumerate([5, 7]):
            ax = axes[row, col]
            hm_path = os.path.join(OUT_DIR, f"plan002_sensitivity_{topo}_K{K}.png")
            if os.path.exists(hm_path):
                img = plt.imread(hm_path)
                ax.imshow(img)
                ax.axis('off')
                ax.set_title(f'{topo} K={K}', fontsize=10)
            else:
                ax.text(0.5, 0.5, 'N/A', ha='center', va='center', transform=ax.transAxes)
                ax.set_title(f'{topo} K={K}', fontsize=10)
    fig.suptitle('Sensitivity Heatmaps: |∂bias(τ)/∂C_ij|', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    combined_path = os.path.join(OUT_DIR, 'plan002_sensitivity_combined.png')
    fig.savefig(combined_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"\n  Combined heatmap → {os.path.basename(combined_path)}")

    print(f"\nTotal: {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
