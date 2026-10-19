#!/usr/bin/env python3
"""
Exp-E: ASV Stability Across DGPs

Demonstrates that ASV ranking (relative topology vulnerability ordering)
is stable across different DGP parameter configurations.

3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.
Each of 9 cells reports the median δ* over the 5 C₀s.
"""

import numpy as np
import json
import time

K = 3
STEP = 0.001

# ─── C(δ) parameterization ──────────────────────────────────────────────────

def make_C_delta(C0, delta):
    C = (1 - delta) * np.eye(K) + delta * C0
    C = np.maximum(C, 0.0)
    cs = C.sum(axis=0)
    cs = np.where(cs < 1e-10, 1.0, cs)
    return C / cs


def get_delta_max(C0):
    d = np.diag(C0).min()
    if d >= 1.0:
        return 10.0
    return min(1.0 / (1.0 - d), 10.0)


def make_fixed_C0(diag_val):
    off = (1 - diag_val) / (K - 1)
    C0 = np.full((K, K), off)
    np.fill_diagonal(C0, diag_val)
    return C0


# ─── Topology 1: Confounding ────────────────────────────────────────────────
# DAG: A → T, A → Y, T → Y, A → A*
# OLS: Y ~ 1 + T + D*₁ + D*₂
# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A

def plim_confounding(C, dgp):
    p = dgp['p']
    g = dgp['gamma']
    tau = dgp['tau']
    bA = dgp['beta'][1:]
    sT = dgp.get('sigma_T', 1.0)

    b = np.array([0.0, tau, bA[0], bA[1]])
    ET = g[0] * p[1] + g[1] * p[2]
    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2
    q = C @ p
    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]
                     for j in range(K)])

    EZZ = np.array([
        [1,    ET,      q[1],     q[2]    ],
        [ET,   ET2,     ETDs[1],  ETDs[2] ],
        [q[1], ETDs[1], q[1],     0       ],
        [q[2], ETDs[2], 0,        q[2]    ]])
    EZX = np.array([
        [1,    ET,      p[1],         p[2]        ],
        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],
        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],
        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])
    return np.linalg.solve(EZZ, EZX @ b)[1]


# ─── Topology 2: Exposure ───────────────────────────────────────────────────
# DAG: A → Y, A → A*
# OLS: Y ~ 1 + D*₁ + D*₂

def plim_exposure(C, dgp):
    p, beta = dgp['p'], dgp['beta']
    q = C @ p
    EZZ = np.array([
        [1,    q[1], q[2]],
        [q[1], q[1], 0   ],
        [q[2], 0,    q[2]]])
    EZX = np.array([
        [1,    p[1],           p[2]          ],
        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],
        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])
    return np.linalg.solve(EZZ, EZX @ beta)


# ─── Topology 3: IV ─────────────────────────────────────────────────────────
# DAG: Z → A, U → {A,Y}, A → Y, A → A*
# Wald estimator: RF / FS*₁

IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)


def _softmax_sample(logits, rng):
    e = np.exp(logits - logits.max(1, keepdims=True))
    p = e / e.sum(1, keepdims=True)
    c = np.cumsum(p, axis=1)
    u = rng.uniform(size=logits.shape[0])
    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)


def precomp_iv(beta, params, N=2_000_000, seed=999):
    rng = np.random.default_rng(seed)
    Z = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    logits = np.column_stack([
        np.zeros(N),
        params['g1'] + params['dZ'] * Z + params['dU'] * U,
        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])
    A = _softmax_sample(logits, rng)
    Y = (beta[1] * (A == 1).astype(float)
         + beta[2] * (A == 2).astype(float)
         + params['lam'] * U + rng.normal(0, 1, N))
    z1, z0 = Z == 1, Z == 0
    RF = Y[z1].mean() - Y[z0].mean()
    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()
                   for k in range(K)])
    return dict(RF=RF, FS=FS)


def plim_iv(C, st):
    fs = (C @ st['FS'])[1]
    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs


# ─── ASV computation ────────────────────────────────────────────────────────

def _make_grid(C0):
    dmax = get_delta_max(C0)
    n = int(round(dmax / STEP)) + 1
    return np.linspace(0, dmax, n)


def _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):
    if tau_abs < 1e-12:
        return 0.0
    thresh = threshold * tau_abs
    rmax = 0.0
    for i in range(len(deltas)):
        b = bias_abs[i]
        if not np.isnan(b):
            rmax = max(rmax, b)
        if rmax > thresh:
            return float(deltas[i])
    return None


def compute_cell_confounding(dgp, C0):
    deltas = _make_grid(C0)
    tau0 = plim_confounding(np.eye(K), dgp)
    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)
                      for d in deltas])
    ba = np.abs(curve - tau0)
    return {
        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),
        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),
    }


def compute_cell_exposure(dgp, C0):
    deltas = _make_grid(C0)
    beta0 = plim_exposure(np.eye(K), dgp)
    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)
                       for d in deltas])

    mr = np.zeros(len(deltas))
    for i in range(len(deltas)):
        for k in [1, 2]:
            if abs(beta0[k]) > 1e-10:
                mr[i] = max(mr[i],
                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))

    def _mag(threshold):
        rmax = 0.0
        for i in range(len(deltas)):
            rmax = max(rmax, mr[i])
            if rmax > threshold:
                return float(deltas[i])
        return None

    sf = None
    for i, d in enumerate(deltas):
        for k in [1, 2]:
            if (abs(beta0[k]) > 1e-10
                    and abs(curves[i, k]) > 1e-10
                    and curves[i, k] * beta0[k] < 0):
                sf = float(d)
                break
        if sf is not None:
            break

    return {
        'mag_asv_10pct': _mag(0.1),
        'mag_asv_50pct': _mag(0.5),
        'sign_flip_asv': sf,
    }


def compute_cell_iv(st, C0):
    deltas = _make_grid(C0)
    tau0 = plim_iv(np.eye(K), st)
    if np.isnan(tau0) or abs(tau0) < 1e-10:
        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}
    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])
    ba = np.abs(curve - tau0)
    return {
        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),
        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),
    }


def median_results(cells):
    keys = cells[0].keys()
    out = {}
    for k in keys:
        vals = [c[k] for c in cells if c[k] is not None]
        out[k] = round(float(np.median(vals)), 4) if vals else None
    return out


# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    t0 = time.time()

    DGPS = [
        {'name': 'alternating_large',
         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,
         'p': np.array([0.5, 0.33, 0.17]),
         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},
        {'name': 'same_sign_medium',
         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,
         'p': np.array([0.5, 0.33, 0.17]),
         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},
        {'name': 'alternating_small',
         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,
         'p': np.array([0.5, 0.33, 0.17]),
         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},
    ]

    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]
    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]
    TOPOS = ['confounding', 'exposure', 'iv']

    print("Exp-E: ASV Stability Across DGPs")
    print("=" * 70)

    print("Precomputing IV sufficient statistics...")
    iv_st = {}
    for dgp in DGPS:
        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)
        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])
        print(f"  {dgp['name']}: Wald(I) = {t_iv:.6f}")

    results = {t: {} for t in TOPOS}
    per_c0 = {t: {} for t in TOPOS}

    for dgp in DGPS:
        nm = dgp['name']
        print(f"\nDGP: {nm}  beta={dgp['beta'].tolist()}")

        for topo in TOPOS:
            cells = []
            for dv, C0 in C0S:
                if topo == 'confounding':
                    c = compute_cell_confounding(dgp, C0)
                elif topo == 'exposure':
                    c = compute_cell_exposure(dgp, C0)
                else:
                    c = compute_cell_iv(iv_st[nm], C0)
                cells.append(c)

            med = median_results(cells)
            results[topo][nm] = med
            per_c0[topo][nm] = [
                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]

            parts = [f"10%={med['mag_asv_10pct']}",
                     f"50%={med['mag_asv_50pct']}"]
            if 'sign_flip_asv' in med:
                parts.append(f"sf={med['sign_flip_asv']}")
            print(f"  {topo:>12}: {', '.join(parts)}")

    # ── Ranking analysis ─────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("Ranking (by delta*_10%, lower = more fragile)")
    print("=" * 70)
    rankings = {}
    for dgp in DGPS:
        nm = dgp['name']
        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))
                for t in TOPOS]
        vals.sort(key=lambda x: x[1])
        rankings[nm] = [t for t, _ in vals]
        vstr = ' < '.join(f"{t}({v:.4f})" for t, v in vals)
        print(f"  {nm}: {vstr}")

    stable = len(set(tuple(r) for r in rankings.values())) == 1
    stability_msg = ("Rankings preserved across all 3 DGPs" if stable
                     else "Rankings vary across DGPs")
    print(f"\nStable: {stable} -- {stability_msg}")

    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')
    print(f"Same-sign sign-flip: "
          f"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}")

    # ── Save JSON ────────────────────────────────────────────────────────────
    output = {
        'dgp_configs': [
            {'name': d['name'], 'beta': d['beta'].tolist(),
             'tau': d['tau'], 'p': d['p'].tolist()}
            for d in DGPS],
        'C0_diag_values': DIAG_VALS,
        'results': results,
        'per_C0_results': per_c0,
        'rankings': rankings,
        'ranking_stable': stable,
        'ranking_stability': stability_msg,
    }
    json_path = 'artifacts/exp_e_asv_stability_results.json'
    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {json_path}")

    # ── Save LaTeX table ─────────────────────────────────────────────────────
    labels = {
        'alternating_large': r'Alt.\ large: $\bm{\beta}=[0,\,1.0,\,-0.5]$',
        'same_sign_medium':  r'Same-sign: $\bm{\beta}=[0,\,0.5,\,0.3]$',
        'alternating_small': r'Alt.\ small: $\bm{\beta}=[0,\,0.2,\,-0.1]$',
    }
    tex = [
        r'\begin{table}[t]',
        r'\centering',
        r'\caption{ASV stability across DGP configurations. '
        r'Each cell shows $\delta^*$ at the 10\% relative bias threshold '
        r'(median over 5 confusion matrices with diagonal '
        r'$\in\{0.5,0.6,0.7,0.8,0.9\}$). '
        r'Lower $\delta^*$ indicates greater fragility. '
        r'Confounding is consistently most robust; '
        r'for alternating-sign $\bm{\beta}$, '
        r'the ranking Exposure $<$ IV $<$ Confounding holds. '
        r"``$\infty$\!\!'' = threshold never reached within $\delta$ range.}",
        r'\label{tab:asv_stability}',
        r'\small',
        r'\begin{tabular}{l ccc}',
        r'\toprule',
        r' & \multicolumn{3}{c}{Magnitude ASV $\delta^*_{10\%}$} \\',
        r'\cmidrule(lr){2-4}',
        r'DGP Configuration & Confounding & Exposure & IV \\',
        r'\midrule',
    ]
    for dgp in DGPS:
        nm = dgp['name']
        vals = []
        for t in TOPOS:
            v = results[t][nm]['mag_asv_10pct']
            vals.append(f'{v:.3f}' if v is not None else r'$\infty$')
        tex.append(
            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]} \\\\')
    tex += [r'\bottomrule', r'\end{tabular}', r'\end{table}']

    tex_path = 'artifacts/exp_e_asv_stability_table.tex'
    with open(tex_path, 'w') as f:
        f.write('\n'.join(tex))
    print(f"Saved: {tex_path}")

    print(f"\nTotal: {time.time() - t0:.1f}s")
