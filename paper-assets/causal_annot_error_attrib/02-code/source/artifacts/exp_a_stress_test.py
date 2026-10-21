#!/usr/bin/env python3
"""
Exp-A: Non-differential Misclassification Stress Test Expansion

Tests sign flip rate and bias ratio under increasing differential
misclassification departure ε.

4 topologies × 2 K × 3 CM qualities × 4 ε = 96 configs
N=10,000 × 100 MC reps per config
"""
import numpy as np
import json
import time
import os

TOPOLOGIES = ['confounding', 'mediation', 'exposure', 'iv']
K_VALUES = [3, 10]
EPSILONS = [0.0, 0.01, 0.05, 0.10]
CM_QUALS = {'high': 0.8, 'medium': 0.6, 'low': 0.4}
N_SAMPLES = 10_000
N_REPS = 100
N_LARGE = 2_000_000
SEED = 42

_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]


def softmax_rows(x):
    e = np.exp(x - x.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)


def sample_cat(probs, rng):
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=probs.shape[0])[:, None]
    return (u >= cum[:, :-1]).sum(axis=1).astype(int)


def make_p_A(K):
    if K == 3:
        return np.array([0.40, 0.35, 0.25])
    raw = np.array([1.0 / (i + 1) for i in range(K)])
    return raw / raw.sum()


def make_dgp_params(K):
    p_A = make_p_A(K)
    params = {
        'confounding': {
            'p_A': p_A, 'alpha': np.array(_ALPHA_POOL[:K-1]),
            'beta_A': np.array(_BETA_A_POOL[:K-1]),
            'beta_T': 2.0, 'sigma_T': 1.0,
        },
        'mediation': {
            'tau': 0.5, 'gamma': np.array(_GAMMA_POOL[:K]),
            'delta': np.array(_DELTA_POOL[:K]),
            'beta': np.array(_BETA_POOL[:K]),
        },
        'exposure': {'beta': np.array(_BETA_POOL[:K]), 'p_A': p_A},
    }
    if K == 3:
        params['iv'] = {
            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),
            'g': np.zeros(3), 'dZ': np.array([0.0, 1.0, -0.5]),
            'dU': np.array([0.0, 0.8, 0.6]),
        }
    else:
        iv_b = np.array(_BETA_POOL[:K]) * 0.5
        iv_b[0] = 0.0
        params['iv'] = {
            'lam': 1.0, 'beta': iv_b, 'g': np.zeros(K),
            'dZ': np.array([0.0] + [_ALPHA_POOL[i]*0.7 for i in range(K-1)]),
            'dU': np.array([0.0] + [_BETA_A_POOL[i]*0.6 for i in range(K-1)]),
        }
    return params


# ── DGP generators ──────────────────────────────────────────

def gen_confounding(K, N, p, rng):
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K-1))
    for j in range(K-1):
        D[:, j] = (A == j+1).astype(float)
    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
    Y = p['beta_T']*T + D @ p['beta_A'] + rng.normal(0, 1, N)
    return T, Y, A


def gen_mediation(K, N, p, rng):
    T = rng.binomial(1, 0.5, N).astype(float)
    logits = p['gamma'][None, :] + p['delta'][None, :]*T[:, None]
    A = sample_cat(softmax_rows(logits), rng)
    D = np.zeros((N, K-1))
    for j in range(K-1):
        D[:, j] = (A == j+1).astype(float)
    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau']*T + rng.normal(0, 1, N)
    return T, Y, A


def gen_exposure(K, N, p, rng):
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K-1))
    for j in range(K-1):
        D[:, j] = (A == j+1).astype(float)
    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
    return None, Y, A


def gen_iv(K, N, p, rng):
    Z = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    logits = (p['g'][None, :] + p['dZ'][None, :]*Z[:, None]
              + p['dU'][None, :]*U[:, None])
    A = sample_cat(softmax_rows(logits), rng)
    D = np.zeros((N, K-1))
    for j in range(K-1):
        D[:, j] = (A == j+1).astype(float)
    Y = D @ p['beta'][1:] + p['lam']*U + rng.normal(0, 1, N)
    return Z, Y, A


GEN = {'confounding': gen_confounding, 'mediation': gen_mediation,
       'exposure': gen_exposure, 'iv': gen_iv}


# ── Estimators ──────────────────────────────────────────────

def est_tau(topo, fv, Y, Ak, K):
    N = len(Y)
    D = np.zeros((N, K-1))
    for k in range(1, K):
        D[:, k-1] = (Ak == k).astype(float)
    if topo == 'iv':
        z1, z0 = fv == 1, fv == 0
        if z1.sum() < 2 or z0.sum() < 2:
            return np.nan
        RF = Y[z1].mean() - Y[z0].mean()
        FS = D[z1, 0].mean() - D[z0, 0].mean()
        return RF / FS if abs(FS) > 1e-8 else np.nan
    elif topo == 'exposure':
        X = np.column_stack([np.ones(N), D])
    else:
        X = np.column_stack([np.ones(N), fv, D])
    try:
        return np.linalg.lstsq(X, Y, rcond=None)[0][1]
    except np.linalg.LinAlgError:
        return np.nan


# ── Confusion matrix construction & perturbation ────────────

def make_cm(K, diag):
    C = np.full((K, K), (1.0 - diag) / (K - 1))
    np.fill_diagonal(C, diag)
    return C


def perturb(C, eps):
    K = C.shape[0]
    Cp = C.copy()
    Cp[~np.eye(K, dtype=bool)] += eps
    for j in range(K):
        Cp[:, j] /= Cp[:, j].sum()
    return Cp


def gen_Astar(A, Y, Cb, eps, rng):
    if eps <= 0:
        probs = Cb[:, A]
    else:
        Cp = perturb(Cb, eps)
        high = Y > np.median(Y)
        probs = np.where(high[None, :], Cp[:, A], Cb[:, A])
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)


# ── Main ────────────────────────────────────────────────────

def main():
    t0 = time.time()
    out_dir = os.path.dirname(os.path.abspath(__file__))
    n_total = len(TOPOLOGIES) * len(K_VALUES) * len(EPSILONS) * len(CM_QUALS)
    print(f"Exp-A: {n_total} configs x {N_REPS} MC reps, N={N_SAMPLES}")

    # Validate CMs
    for K in K_VALUES:
        for dv in CM_QUALS.values():
            C = make_cm(K, dv)
            assert np.allclose(C.sum(axis=0), 1.0), f"K={K} diag={dv}: bad CM"
            for eps in EPSILONS:
                if eps > 0:
                    Cp = perturb(C, eps)
                    assert np.allclose(Cp.sum(axis=0), 1.0)
                    assert (Cp >= -1e-12).all()

    all_params = {K: make_dgp_params(K) for K in K_VALUES}

    # True parameters (oracle with N=2M)
    tau_trues = {}
    print("\nTrue parameters (N=2M oracle):")
    for K in K_VALUES:
        for topo in TOPOLOGIES:
            rng = np.random.default_rng(K*1000 + abs(hash(topo)) % 1000)
            fv, Y, A = GEN[topo](K, N_LARGE, all_params[K][topo], rng)
            tau_trues[(K, topo)] = est_tau(topo, fv, Y, A, K)
            print(f"  K={K:>2} {topo:<13} tau_true={tau_trues[(K,topo)]:>10.6f}")

    # MC simulation
    results = []
    idx = 0
    print(f"\nMC simulation ({n_total} configs):")
    for topo in TOPOLOGIES:
        for K in K_VALUES:
            p = all_params[K][topo]
            tt = tau_trues[(K, topo)]
            for qn, dv in CM_QUALS.items():
                Cb = make_cm(K, dv)
                for eps in EPSILONS:
                    idx += 1
                    rng = np.random.default_rng(SEED + idx*1000)
                    hats = np.empty(N_REPS)
                    for m in range(N_REPS):
                        fv, Y, A = GEN[topo](K, N_SAMPLES, p, rng)
                        As = gen_Astar(A, Y, Cb, eps, rng)
                        hats[m] = est_tau(topo, fv, Y, As, K)

                    ok = np.isfinite(hats)
                    nv = int(ok.sum())
                    if nv > 0 and abs(tt) > 1e-12:
                        vh = hats[ok]
                        sfr = float((np.sign(vh) != np.sign(tt)).mean())
                        ratios = np.abs(vh / tt)
                        br = float(ratios.mean())
                        br_std = float(ratios.std())
                        br_med = float(np.median(ratios))
                        mt = float(vh.mean())
                    else:
                        sfr = br = br_std = br_med = mt = None

                    results.append({
                        'topology': topo, 'K': K, 'epsilon': eps,
                        'cm_quality': qn, 'cm_diag': dv,
                        'sign_flip_rate': sfr,
                        'mean_bias_ratio': br,
                        'std_bias_ratio': br_std,
                        'median_bias_ratio': br_med,
                        'tau_true': float(tt),
                        'mean_tau_hat': mt,
                        'n_reps': nv,
                    })

                    if idx % 12 == 0 or idx == n_total:
                        el = time.time() - t0
                        eta = el / idx * (n_total - idx)
                        s = f"SF={sfr:.3f} BR={br:.3f}" if sfr is not None else "N/A"
                        print(f"  [{idx:>3}/{n_total}] {topo:<13} K={K:>2} "
                              f"eps={eps:.2f} {qn:<6} {s}  "
                              f"({el:.0f}s, ETA {eta:.0f}s)")

    # Summaries
    def sm(vals):
        v = [x for x in vals if x is not None]
        return float(np.mean(v)) if v else None

    by_eps = {}
    for eps in EPSILONS:
        sub = [r for r in results if r['epsilon'] == eps]
        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]
        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]
        by_eps[str(eps)] = {
            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,
            'mean_bias_ratio': float(np.mean(brs)) if brs else None,
            'max_sign_flip_rate': float(max(sfs)) if sfs else None,
        }

    by_topo = {}
    for topo in TOPOLOGIES:
        sub = [r for r in results if r['topology'] == topo]
        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]
        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]
        by_topo[topo] = {
            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,
            'mean_bias_ratio': float(np.mean(brs)) if brs else None,
        }

    by_K = {}
    for K in K_VALUES:
        sub = [r for r in results if r['K'] == K]
        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]
        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]
        by_K[str(K)] = {
            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,
            'mean_bias_ratio': float(np.mean(brs)) if brs else None,
        }

    output = {
        'results': results,
        'summary': {'by_epsilon': by_eps, 'by_topology': by_topo, 'by_K': by_K},
    }

    def clean(o):
        if isinstance(o, (float, np.floating)):
            v = float(o)
            return None if (np.isnan(v) or np.isinf(v)) else v
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, dict):
            return {k: clean(v) for k, v in o.items()}
        if isinstance(o, list):
            return [clean(v) for v in o]
        return o

    output = clean(output)
    jpath = os.path.join(out_dir, 'exp_a_stress_test_results.json')
    with open(jpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON -> {jpath}")

    tpath = os.path.join(out_dir, 'exp_a_stress_test_table.tex')
    write_tex(results, tpath)
    print(f"TeX  -> {tpath}")

    total = time.time() - t0
    print(f"\nDone in {total:.0f}s ({total/60:.1f}min)")
    print("\nBy epsilon:")
    for eps, s in by_eps.items():
        sf = s['mean_sign_flip_rate']
        br = s['mean_bias_ratio']
        mx = s['max_sign_flip_rate']
        print(f"  eps={eps}: meanSF={sf:.4f} meanBR={br:.4f} maxSF={mx:.4f}")
    print("\nBy topology:")
    for topo, s in by_topo.items():
        print(f"  {topo:<13}: SF={s['mean_sign_flip_rate']:.4f} "
              f"BR={s['mean_bias_ratio']:.4f}")
    print("\nBy K:")
    for k, s in by_K.items():
        print(f"  K={k}: SF={s['mean_sign_flip_rate']:.4f} "
              f"BR={s['mean_bias_ratio']:.4f}")


def write_tex(results, path):
    ncols = 3 + 2 * len(EPSILONS)
    lines = [
        r'\begin{table*}[t]',
        r'\centering',
        r'\caption{Non-differential misclassification stress test: sign flip rate (SF) '
        r'and mean bias ratio (BR\,$=\overline{|\hat\tau/\tau|}$) under increasing '
        r'differential departure $\varepsilon$.}',
        r'\label{tab:stress-test}',
        r'\small\setlength{\tabcolsep}{3.5pt}',
        r'\begin{tabular}{llc' + 'rr' * len(EPSILONS) + '}',
        r'\toprule',
    ]

    h1 = r'Topology & $K$ & Q'
    for e in EPSILONS:
        h1 += rf' & \multicolumn{{2}}{{c}}{{$\varepsilon\!=\!{e}$}}'
    lines.append(h1 + r' \\')

    clines = ' '.join(
        rf'\cmidrule(lr){{{4+2*i}-{5+2*i}}}' for i in range(len(EPSILONS)))
    lines.append(clines)

    h2 = r' & &'
    for _ in EPSILONS:
        h2 += r' & {\scriptsize SF} & {\scriptsize BR}'
    lines.append(h2 + r' \\')
    lines.append(r'\midrule')

    for ti, topo in enumerate(TOPOLOGIES):
        if ti > 0:
            lines.append(r'\midrule')
        first_t = True
        for ki, K in enumerate(K_VALUES):
            if ki > 0:
                lines.append(rf'\cmidrule{{2-{ncols}}}')
            first_k = True
            for qn in CM_QUALS:
                TOPO_LABELS = {'confounding': 'Confounding', 'mediation': 'Mediation',
                               'exposure': 'Exposure', 'iv': 'IV'}
                tl = TOPO_LABELS.get(topo, topo.capitalize()) if first_t else ''
                kl = str(K) if first_k else ''
                row = f'{tl} & {kl} & {qn[0].upper()}'
                for eps in EPSILONS:
                    r = next(x for x in results
                             if x['topology'] == topo and x['K'] == K
                             and x['epsilon'] == eps and x['cm_quality'] == qn)
                    sf = r['sign_flip_rate']
                    br = r['mean_bias_ratio']
                    sfs = f'{sf:.2f}' if sf is not None else '--'
                    brs = f'{br:.2f}' if br is not None else '--'
                    row += f' & {sfs} & {brs}'
                lines.append(row + r' \\')
                first_t = False
                first_k = False

    lines += [
        r'\bottomrule',
        r'\end{tabular}',
        r'\vspace{1mm}',
        r'\parbox{\textwidth}{\footnotesize '
        r'SF\,=\,sign flip rate; BR\,=\,mean $|\hat\tau/\tau|$ '
        r'(1.00 = unbiased). '
        r'$\varepsilon\!=\!0$: non-differential; $\varepsilon\!>\!0$: '
        r'outcome-dependent misclassification. '
        r'Q: H/M/L\,=\,CM diagonal 0.8/0.6/0.4 with uniform off-diagonal. '
        r'Each cell: $N\!=\!10{,}000\!\times\!100$ MC replications.}',
        r'\end{table*}',
    ]
    with open(path, 'w') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
