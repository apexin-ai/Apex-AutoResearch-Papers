#!/usr/bin/env python3
"""
MF-1a: Adversarial Monotonicity Test for Conjecture 1.

Verifies ε-approximate envelope monotonicity of |B(C(δ))| along
C(δ)=(1-δ)I+δC₀ for δ∈[0,1] under 4 adversarial confusion matrix structures.

Grid: 4 adversarial C₀ types × ~9 param configs × 3 K × 7 topologies × 3 β × 100 C₀
"""

import json
import os
import sys
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exp_d_conjecture_verify_v2 import (
    ALL_TOPOS, NON_DECREASING, NON_INCREASING,
    _COMPUTE_SS, make_all_params, get_tau_true,
    compute_bias_curve,
)

K_VALUES = [3, 5, 7]
N_DELTA = 101
DELTA_STEP = 0.01
N_C0 = 1000
SEED = 2024
EPS_THRESHOLD = 0.001

BETA_CONFIGS = ['alternating_large', 'same_sign', 'alternating_small']
ADV_TYPES = ['near_perm', 'block_diag', 'sparse', 'near_uniform']
ADV_PARAMS = {
    'near_perm': [{'eps': 0.05}, {'eps': 0.1}, {'eps': 0.2}],
    'block_diag': [{}],
    'sparse': [{'p_diag': 0.3}, {'p_diag': 0.5}, {'p_diag': 0.7}],
    'near_uniform': [{'eps': 0.01}, {'eps': 0.05}],
}

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def make_beta_vec(name, K):
    pools = {
        'alternating_large': [0, 1, -0.5, 0.3, -0.2, 0.1, -0.08],
        'same_sign':         [0, 0.5, 0.3, 0.2, 0.1, 0.08, 0.05],
        'alternating_small': [0, 0.2, -0.1, 0.05, -0.03, 0.02, -0.01],
    }
    return np.array(pools[name][:K])


def make_params_with_beta(K, beta_name):
    params = make_all_params(K)
    bv = make_beta_vec(beta_name, K)
    params['exposure']['beta'] = bv.copy()
    params['iv']['beta'] = bv.copy()
    params['mediation']['beta'] = bv.copy()
    params['frontdoor']['beta'] = bv.copy()
    params['confounding']['beta_A'] = bv[1:].copy()
    params['collider']['dY'] = bv.copy()
    params['mbias']['a1'] = bv.copy()
    return params


def gen_C0(adv_type, cfg, K, rng):
    if adv_type == 'near_perm':
        perm = rng.permutation(K)
        P = np.zeros((K, K))
        P[perm, np.arange(K)] = 1.0
        e = cfg['eps']
        return (1 - e) * P + e / K

    if adv_type == 'block_diag':
        split = max(1, K // 2)
        C0 = np.zeros((K, K))
        for j in range(K):
            if j < split:
                C0[:split, j] = 1.0 / split
            else:
                C0[split:, j] = 1.0 / (K - split)
        return C0

    if adv_type == 'sparse':
        pd = cfg['p_diag']
        C0 = np.zeros((K, K))
        for k in range(K):
            C0[k, k] = pd
            off = [i for i in range(K) if i != k]
            C0[rng.choice(off), k] = 1 - pd
        return C0

    if adv_type == 'near_uniform':
        e = cfg['eps']
        dv = 1.0 / K + e
        ov = (1 - dv) / (K - 1)
        C0 = np.full((K, K), ov)
        np.fill_diagonal(C0, dv)
        return C0


def compute_fixed_curve(topo, C0, ss, tau_true):
    """Compute |B(C(δ))| for δ∈[0,1]. Returns (bias_abs[0:101], weak_iv)."""
    if topo == 'iv':
        FS = ss.FS
        a = float(FS[1])
        b = float((C0 @ FS)[1])
        if abs(a) < 1e-15:
            return None, True
        if abs(a - b) > 1e-15:
            d_cross = a / (a - b)
            if 0 < d_cross < 1:
                return None, True

    deltas_full, bias_full = compute_bias_curve(
        topo, C0, ss, tau_true, delta_step=DELTA_STEP)
    n = min(N_DELTA, len(bias_full))
    if n < N_DELTA:
        return None, False
    return bias_full[:N_DELTA], False


def measure_violation(bias_abs, topo):
    """Return max single-step violation magnitude."""
    valid = ~np.isnan(bias_abs)
    ba = bias_abs[valid]
    if len(ba) < 2:
        return 0.0
    diffs = np.diff(ba)
    if topo in NON_DECREASING:
        drops = -diffs[diffs < 0]
    else:
        drops = diffs[diffs > 0]
    return float(drops.max()) if len(drops) > 0 else 0.0


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)

    print("=" * 78)
    print("MF-1a: Adversarial Monotonicity Test")
    print(f"  K={K_VALUES}  β={BETA_CONFIGS}")
    print(f"  Adversarial: {ADV_TYPES}")
    print(f"  N_C0={N_C0}  δ steps={N_DELTA}  ε threshold={EPS_THRESHOLD}")
    print("=" * 78)
    sys.stdout.flush()

    all_eps = []
    by_adv = {a: {'n': 0, 'nm': 0, 'mx': 0.0} for a in ADV_TYPES}
    by_topo = {t: {'n': 0, 'nm': 0, 'mx': 0.0} for t in ALL_TOPOS}
    by_K = {str(k): {'n': 0, 'nm': 0, 'mx': 0.0} for k in K_VALUES}
    worst = []
    total_weak_iv = 0
    total_skipped = 0

    n_adv_cfgs = sum(len(v) for v in ADV_PARAMS.values())
    n_cells = len(K_VALUES) * len(BETA_CONFIGS) * len(ALL_TOPOS) * n_adv_cfgs
    cell_i = 0

    for K in K_VALUES:
        for beta_name in BETA_CONFIGS:
            params = make_params_with_beta(K, beta_name)

            for topo in ALL_TOPOS:
                ss = _COMPUTE_SS[topo](K, params[topo])
                tau_true = get_tau_true(topo, K, params, ss)

                if np.isnan(tau_true) or abs(tau_true) < 1e-12:
                    cell_i += n_adv_cfgs
                    total_skipped += n_adv_cfgs * N_C0
                    continue

                for adv_type in ADV_TYPES:
                    for adv_cfg in ADV_PARAMS[adv_type]:
                        cell_i += 1
                        cell_eps = []
                        cell_nm = 0
                        cell_weak = 0

                        for _ in range(N_C0):
                            C0 = gen_C0(adv_type, adv_cfg, K, rng)
                            curve, weak = compute_fixed_curve(
                                topo, C0, ss, tau_true)

                            if weak:
                                cell_weak += 1
                                continue
                            if curve is None:
                                continue

                            eps = measure_violation(curve, topo)
                            cell_eps.append(eps)
                            if eps > EPS_THRESHOLD:
                                cell_nm += 1

                        n_valid = len(cell_eps)
                        if n_valid == 0:
                            total_weak_iv += cell_weak
                            continue

                        mx = max(cell_eps)
                        total_weak_iv += cell_weak
                        all_eps.extend(cell_eps)

                        for acc, key in [(by_adv, adv_type),
                                         (by_topo, topo),
                                         (by_K, str(K))]:
                            acc[key]['n'] += n_valid
                            acc[key]['nm'] += cell_nm
                            acc[key]['mx'] = max(acc[key]['mx'], mx)

                        if mx > EPS_THRESHOLD:
                            worst.append({
                                'topology': topo, 'K': K,
                                'adversarial': adv_type,
                                'adv_config': json.dumps(adv_cfg)
                                              if adv_cfg else "{}",
                                'beta': beta_name,
                                'eps_abs': mx,
                                'non_mono_frac': cell_nm / n_valid,
                                'n_valid': n_valid,
                                'weak_iv': cell_weak,
                            })

                        if cell_i % 63 == 0 or cell_i == n_cells:
                            print(
                                f"  [{cell_i:>4}/{n_cells}] K={K} "
                                f"{topo:<12} {adv_type:<14} "
                                f"β={beta_name:<18} max_ε={mx:.6f} "
                                f"nm={cell_nm}/{n_valid}  "
                                f"({time.time()-t0:.1f}s)")
                            sys.stdout.flush()

    eps_arr = np.array(all_eps) if all_eps else np.array([0.0])
    total_curves = len(all_eps)
    total_nm = sum(1 for e in all_eps if e > EPS_THRESHOLD)

    safe_topos = {'confounding', 'mediation', 'exposure', 'frontdoor'}
    fragile_topos = {'collider', 'mbias', 'iv'}

    def fmt_acc(d):
        return {k: {
            'total_curves': v['n'],
            'non_monotone_count': v['nm'],
            'non_monotone_fraction': v['nm'] / max(v['n'], 1),
            'max_eps_abs': v['mx'],
        } for k, v in d.items()}

    worst.sort(key=lambda x: -x['eps_abs'])
    worst = worst[:20]

    output = {
        'description':
            'Adversarial envelope monotonicity test for Conjecture 1',
        'config': {
            'K_values': K_VALUES,
            'adversarial_types': ADV_TYPES,
            'adversarial_params': ADV_PARAMS,
            'topologies': ALL_TOPOS,
            'beta_configs': BETA_CONFIGS,
            'n_C0_per_cell': N_C0,
            'n_delta_steps': N_DELTA,
            'delta_step': DELTA_STEP,
            'eps_threshold': EPS_THRESHOLD,
            'seed': SEED,
        },
        'summary': {
            'total_curves': total_curves,
            'non_monotone_fraction':
                total_nm / max(total_curves, 1),
            'max_eps_abs': float(eps_arr.max()),
            'median_eps_abs': float(np.median(eps_arr)),
            'mean_eps_abs': float(np.mean(eps_arr)),
            'p95_eps_abs': float(np.percentile(eps_arr, 95)),
            'p99_eps_abs': float(np.percentile(eps_arr, 99)),
            'safe_topo_max_eps': float(
                max(by_topo[t]['mx'] for t in safe_topos)),
            'fragile_topo_max_eps': float(
                max(by_topo[t]['mx'] for t in fragile_topos)),
            'total_weak_iv_filtered': total_weak_iv,
            'total_skipped_zero_tau': total_skipped,
        },
        'by_adversarial_type': fmt_acc(by_adv),
        'by_topology': fmt_acc(by_topo),
        'by_K': fmt_acc(by_K),
        'worst_cases': worst,
        'elapsed_seconds': time.time() - t0,
    }

    out_path = os.path.join(OUT_DIR, 'adversarial_monotonicity_results.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nJSON -> {out_path}")
    print(f"\n{'='*60}")
    print(f"Total curves: {total_curves:,}  "
          f"Non-monotone: {total_nm} "
          f"({total_nm/max(total_curves,1)*100:.3f}%)")
    print(f"Max ε_abs: {eps_arr.max():.6f}  "
          f"Median: {np.median(eps_arr):.6f}")
    print(f"Safe max ε: "
          f"{max(by_topo[t]['mx'] for t in safe_topos):.6f}  "
          f"Fragile max ε: "
          f"{max(by_topo[t]['mx'] for t in fragile_topos):.6f}")
    print(f"Weak-IV filtered: {total_weak_iv}")

    print(f"\nBy topology:")
    for t in ALL_TOPOS:
        d = by_topo[t]
        dr = 'non-dec' if t in NON_DECREASING else 'non-inc'
        print(f"  {t:<14} [{dr}]  n={d['n']:>6}  nm={d['nm']:>5}  "
              f"({d['nm']/max(d['n'],1)*100:.2f}%)  "
              f"max_ε={d['mx']:.6f}")

    print(f"\nBy adversarial type:")
    for a in ADV_TYPES:
        d = by_adv[a]
        print(f"  {a:<14}  n={d['n']:>6}  nm={d['nm']:>5}  "
              f"({d['nm']/max(d['n'],1)*100:.2f}%)  "
              f"max_ε={d['mx']:.6f}")

    print(f"\nBy K:")
    for k in K_VALUES:
        d = by_K[str(k)]
        print(f"  K={k}  n={d['n']:>6}  nm={d['nm']:>5}  "
              f"({d['nm']/max(d['n'],1)*100:.2f}%)  "
              f"max_ε={d['mx']:.6f}")

    if worst:
        print(f"\nWorst cases (top 5):")
        for w in worst[:5]:
            print(f"  {w['topology']:<14} K={w['K']} "
                  f"{w['adversarial']:<14} "
                  f"β={w['beta']:<18} ε={w['eps_abs']:.6f}")

    print(f"\nElapsed: {time.time()-t0:.1f}s")
    print('=' * 60)


if __name__ == '__main__':
    main()
