#!/usr/bin/env python3
"""D127 Multispatial CCM: Causal analysis of canary -> downstream in iterative self-distillation.

Clark et al. (2015) multispatial extension: 8 canary-downstream pairs serve as spatial
replicates, concatenated to yield effective N ~80 from T=11 per replicate.
"""

import json
import os
import sys
import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import pearsonr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

RESULTS_DIR = "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep"
OUTPUT_DIR = "/root/autodl-tmp/distrib_canary_collapse/artifacts/d127_ccm"

EXPERIMENTS = {
    "alpha_1.0": "a100_s42_fp32",
    "alpha_0.50": "a050_s42_fp32",
    "alpha_0.0": "a000_s42_fp32",
}

CANARY_VARS = ["token_entropy", "ece"]
DOWNSTREAM_VARS = ["distinct_1", "distinct_2", "distinct_3", "mauve"]
TAU = 1
E_RANGE = [2, 3, 4]
N_SURROGATES = 200
N_CONV_REPS = 50


def delay_embed(x, E, tau=1):
    N = len(x)
    M = N - (E - 1) * tau
    if M <= 0:
        return np.array([]).reshape(0, E)
    emb = np.zeros((M, E))
    for i in range(E):
        s = (E - 1) * tau - i * tau
        emb[:, i] = x[s:s + M]
    return emb


def ccm_loo(shadow, target, E):
    N = len(shadow)
    k = min(E + 2, N)
    tree = cKDTree(shadow)
    dists, idx = tree.query(shadow, k=k)
    dists = dists[:, 1:E + 2]
    idx = idx[:, 1:E + 2]
    if dists.shape[1] < E + 1:
        return np.full(N, np.nan)
    d_min = dists[:, 0:1].copy()
    d_min[d_min < 1e-10] = 1e-10
    w = np.exp(-dists / d_min)
    w /= w.sum(axis=1, keepdims=True)
    return np.sum(w * target[idx], axis=1)


def rho_safe(pred, actual):
    ok = ~(np.isnan(pred) | np.isnan(actual))
    if ok.sum() < 3 or np.std(pred[ok]) < 1e-12 or np.std(actual[ok]) < 1e-12:
        return 0.0
    return float(pearsonr(pred[ok], actual[ok])[0])


def build_ms_data(cause_list, effect_list, E, tau=1):
    shadows, targets = [], []
    for c, e in zip(cause_list, effect_list):
        sh = delay_embed(e, E, tau)
        off = (E - 1) * tau
        tg = c[off:off + len(sh)]
        if len(sh) > 0 and len(tg) == len(sh):
            shadows.append(sh)
            targets.append(tg)
    if not shadows:
        return None, None
    return np.vstack(shadows), np.concatenate(targets)


def convergence_test(shadow, target, E, rng):
    N = len(target)
    mn = E + 2
    sizes = sorted(set([mn] + [int(x) for x in np.linspace(mn, N, 10)]))
    out = []
    for L in sizes:
        if L < mn or L > N:
            continue
        rhos = []
        for _ in range(N_CONV_REPS):
            perm = rng.permutation(N)
            li, pi = perm[:L], perm[L:]
            if len(pi) < 2:
                pi = perm
            sh_l, tg_l = shadow[li], target[li]
            sh_p, tg_p = shadow[pi], target[pi]
            k = min(E + 1, len(sh_l))
            if k < E + 1:
                continue
            tree = cKDTree(sh_l)
            d, ix = tree.query(sh_p, k=k)
            if d.ndim == 1:
                d, ix = d.reshape(1, -1), ix.reshape(1, -1)
            dm = d[:, 0:1].copy()
            dm[dm < 1e-10] = 1e-10
            w = np.exp(-d / dm)
            w /= w.sum(axis=1, keepdims=True)
            pred = np.sum(w * tg_l[ix], axis=1)
            rhos.append(rho_safe(pred, tg_p))
        if rhos:
            out.append({'lib_size': int(L), 'rho_mean': float(np.mean(rhos)),
                        'rho_std': float(np.std(rhos))})
    return out


def surrogate_test(shadow, target, E, rng):
    pred_obs = ccm_loo(shadow, target, E)
    rho_obs = rho_safe(pred_obs, target)
    surr = []
    for _ in range(N_SURROGATES):
        sh = rng.permutation(target)
        p = ccm_loo(shadow, sh, E)
        surr.append(rho_safe(p, sh))
    surr = np.array(surr)
    return rho_obs, float(np.mean(surr >= rho_obs)), surr


def run_direction(cause_list, effect_list, E, rng):
    shadow, target = build_ms_data(cause_list, effect_list, E, TAU)
    if shadow is None:
        return {'rho': float('nan'), 'p_value': 1.0, 'convergence': [], 'N': 0, 'E': E}
    conv = convergence_test(shadow, target, E, rng)
    rho_obs, p_val, surr = surrogate_test(shadow, target, E, rng)
    return {
        'rho': rho_obs, 'p_value': p_val,
        'convergence': conv,
        'surrogate_mean': float(np.mean(surr)),
        'surrogate_std': float(np.std(surr)),
        'N': int(len(target)), 'E': E, 'tau': TAU,
    }


def load_experiment(name):
    path = os.path.join(RESULTS_DIR, name, "all_metrics.json")
    with open(path) as f:
        data = json.load(f)
    data.sort(key=lambda x: x["generation"])
    return data


def extract_pairs(data):
    pairs = []
    for cv in CANARY_VARS:
        ts = np.array([d[cv] for d in data])
        z = (ts - ts.mean()) / (ts.std() + 1e-12)
        for dv in DOWNSTREAM_VARS:
            ts2 = np.array([d[dv] for d in data])
            z2 = (ts2 - ts2.mean()) / (ts2.std() + 1e-12)
            pairs.append({'c_var': cv, 'd_var': dv, 'c_z': z, 'd_z': z2})
    return pairs


def plot_convergence(results):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    keys = ["alpha_1.0", "alpha_0.50", "alpha_0.0"]
    titles = [r"$\alpha=1.0$ (full distill)", r"$\alpha=0.50$ (onset)", r"$\alpha=0.0$ (null)"]

    for ax, k, t in zip(axes, keys, titles):
        r = results[k]
        for direction, label, color, marker in [
            ('forward', 'Fwd: canary→ds', 'steelblue', 'o'),
            ('reverse', 'Rev: ds→canary', 'indianred', 's'),
        ]:
            conv = r[direction]['convergence']
            if not conv:
                continue
            L = [c['lib_size'] for c in conv]
            mu = np.array([c['rho_mean'] for c in conv])
            sd = np.array([c['rho_std'] for c in conv])
            ax.plot(L, mu, f'-{marker}', label=label, color=color, markersize=4)
            ax.fill_between(L, mu - sd, mu + sd, alpha=0.15, color=color)

        ax.set_title(t, fontsize=11)
        ax.set_xlabel('Library size')
        if ax == axes[0]:
            ax.set_ylabel(r'CCM $\rho$')
        ax.legend(fontsize=8)
        ax.axhline(0, color='gray', ls='--', alpha=0.4)
        ax.grid(True, alpha=0.25)

    plt.suptitle('Multispatial CCM Convergence (8 replicate pairs)', fontsize=13)
    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "d127_convergence_curves.png")
    plt.savefig(p, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved {p}")


def plot_summary(results):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 5))
    keys = ["alpha_1.0", "alpha_0.50", "alpha_0.0"]
    labels = [r"$\alpha$=1.0", r"$\alpha$=0.50", r"$\alpha$=0.0"]
    x = np.arange(len(labels))
    w = 0.35

    fr = [results[k]['forward']['rho'] for k in keys]
    rr = [results[k]['reverse']['rho'] for k in keys]
    fp = [results[k]['forward']['p_value'] for k in keys]
    rp = [results[k]['reverse']['p_value'] for k in keys]

    a1.bar(x - w/2, fr, w, label='Forward (canary→ds)', color='steelblue')
    a1.bar(x + w/2, rr, w, label='Reverse (ds→canary)', color='indianred')
    for i, (f, r) in enumerate(zip(fp, rp)):
        sym_f = '**' if f < 0.01 else ('*' if f < 0.05 else '')
        sym_r = '**' if r < 0.01 else ('*' if r < 0.05 else '')
        if sym_f:
            a1.text(i - w/2, fr[i] + 0.02, sym_f, ha='center', fontsize=10, fontweight='bold')
        if sym_r:
            a1.text(i + w/2, rr[i] + 0.02, sym_r, ha='center', fontsize=10, fontweight='bold')
    a1.set_ylabel(r'CCM $\rho$')
    a1.set_xticks(x); a1.set_xticklabels(labels)
    a1.legend(fontsize=9); a1.set_title('Cross-Mapping Skill')
    a1.axhline(0, color='gray', ls='--', alpha=0.4); a1.grid(True, alpha=0.25, axis='y')

    a2.bar(x - w/2, [-np.log10(max(p, 0.005)) for p in fp], w, label='Forward', color='steelblue')
    a2.bar(x + w/2, [-np.log10(max(p, 0.005)) for p in rp], w, label='Reverse', color='indianred')
    a2.axhline(-np.log10(0.05), color='red', ls='--', label='p=0.05', alpha=0.7)
    a2.axhline(-np.log10(0.01), color='orange', ls='--', label='p=0.01', alpha=0.7)
    a2.set_ylabel(r'$-\log_{10}(p)$')
    a2.set_xticks(x); a2.set_xticklabels(labels)
    a2.legend(fontsize=8); a2.set_title('Statistical Significance')
    a2.grid(True, alpha=0.25, axis='y')

    plt.suptitle('D127 Multispatial CCM Summary', fontsize=13)
    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "d127_summary.png")
    plt.savefig(p, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved {p}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    rng = np.random.default_rng(42)
    all_results = {}

    for alpha_name, folder in EXPERIMENTS.items():
        print(f"\n{'='*60}\n{alpha_name} ({folder})\n{'='*60}")
        data = load_experiment(folder)
        pairs = extract_pairs(data)
        c_list = [p['c_z'] for p in pairs]
        e_list = [p['d_z'] for p in pairs]

        best_E, best_rho = 2, -999
        E_sel = {}
        for E in E_RANGE:
            sh, tg = build_ms_data(c_list, e_list, E, TAU)
            if sh is None:
                continue
            r = rho_safe(ccm_loo(sh, tg, E), tg)
            E_sel[E] = r
            print(f"  E={E}  LOO rho={r:.4f}")
            if r > best_rho:
                best_rho, best_E = r, E
        print(f"  -> best E={best_E}")

        print("  Forward (canary->downstream)...")
        fwd = run_direction(c_list, e_list, best_E, rng)
        print("  Reverse (downstream->canary)...")
        rev = run_direction(e_list, c_list, best_E, rng)

        all_results[alpha_name] = {
            'experiment': folder, 'best_E': best_E,
            'E_selection': {str(k): float(v) for k, v in E_sel.items()},
            'forward': fwd, 'reverse': rev,
            'n_pairs': len(pairs), 'T_per_pair': len(data),
        }
        print(f"  Fwd rho={fwd['rho']:.4f} p={fwd['p_value']:.4f}")
        print(f"  Rev rho={rev['rho']:.4f} p={rev['p_value']:.4f}")
        d = "canary->downstream" if fwd['rho'] > rev['rho'] else "downstream->canary"
        print(f"  Direction: {d}")

    out = os.path.join(OUTPUT_DIR, "d127_multispatial_ccm.json")
    with open(out, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\nJSON: {out}")

    plot_convergence(all_results)
    plot_summary(all_results)
    print("\nDone.")


if __name__ == "__main__":
    main()
