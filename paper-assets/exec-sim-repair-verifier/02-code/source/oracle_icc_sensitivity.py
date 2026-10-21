#!/usr/bin/env python3
"""
Oracle ICC Sensitivity Analysis (D107)

Sweeps ICC from 0 to 0.50, measuring per-test vs trajectory-level advantage
using a Beta-Binomial noise model to directly parameterize within-block ICC.

Shows that function-level ICC=0.191 is a conservative estimate:
the per-test advantage grows with ICC, and repo-level ICC=0.3146 gives
a larger advantage.
"""
import numpy as np, json, os, time
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(DIR, 'artifacts')
os.makedirs(ART, exist_ok=True)

# Synthetic SWE-bench Verified F2P distribution (500 instances)
# Matches paper: 68.7% T=1, 19.1% T=2, 7.0% T=3-5, 5.0% T>=6, mean=2.10
SYNTH_F2P = np.array(
    [1]*344 + [2]*96 +
    [3]*12 + [4]*12 + [5]*11 +
    [6]*7 + [7]*4 + [8]*3 + [10]*2 + [13]*2 + [16]*2 +
    [20]*1 + [28]*1 + [35]*1 + [50]*1 + [70]*1,
    dtype=int
)

ICC_VALUES = [0.00, 0.05, 0.10, 0.191, 0.25, 0.3146, 0.40, 0.50]
F2P_CAP = 100


def build_blocks(rng, T_vals, T_max):
    n = len(T_vals)
    bids = np.zeros((n, T_max), dtype=np.int32)
    nb = np.zeros(n, dtype=np.int32)
    for t in range(n):
        T = int(T_vals[t]); idx = bid = 0
        while idx < T:
            rem = T - idx
            if rem <= 8:
                bids[t, idx:T] = bid; bid += 1; break
            bs = min(int(rng.integers(2, 9)), rem)
            bids[t, idx:idx+bs] = bid; bid += 1; idx += bs
        nb[t] = max(bid, 1)
    return bids, nb


def best_patch(scores, rng):
    return (scores.astype(np.float64) + rng.random(scores.shape) * 1e-6).argmax(axis=1)


def from_resolved(preds, rng):
    tb = rng.random(preds.shape)
    ar = preds.any(axis=1, keepdims=True)
    m = np.where(preds, tb, -1.0)
    return np.where(ar, m, tb).argmax(axis=1)


def main():
    N, n_trials, seed = 16, 10000, 42
    acc_range = np.round(np.arange(0.55, 0.995, 0.01), 2)

    print("Oracle ICC Sensitivity Analysis (D107)")
    print(f"  N={N}, trials={n_trials}, seed={seed}")
    print(f"  F2P: {len(SYNTH_F2P)} instances, "
          f"median={int(np.median(SYNTH_F2P))}, mean={SYNTH_F2P.mean():.2f}")
    print(f"  ICC values: {ICC_VALUES}")

    rng = np.random.default_rng(seed)

    T_f2p = np.clip(rng.choice(SYNTH_F2P, size=n_trials), 1, F2P_CAP).astype(int)
    F_max = int(T_f2p.max())

    gt = np.ones((n_trials, N, F_max), dtype=bool)
    for t in range(n_trials):
        T = T_f2p[t]
        for p in range(1, N):
            fp = rng.beta(2, 5)
            fails = rng.random(T) < fp
            if not fails.any():
                fails[rng.integers(T)] = True
            gt[t, p, :T] = ~fails

    fmask = (np.arange(F_max)[None, :] < T_f2p[:, None])[:, None, :]

    bids, nb = build_blocks(rng, T_f2p, F_max)
    B_max = max(int(nb.max()), 1)

    tax = np.arange(n_trials)[:, None, None]
    pax = np.arange(N)[None, :, None]
    bax = bids[:, None, :]

    print(f"  F_max={F_max}, B_max={B_max}")
    print(f"  T_f2p: median={int(np.median(T_f2p))}, "
          f"mean={T_f2p.mean():.2f}, range=[{T_f2p.min()}, {T_f2p.max()}]")

    # Trajectory-level (ICC-independent)
    print("\nComputing trajectory-level baseline...")
    rng_traj = np.random.default_rng(seed + 99999)
    traj_resolve = []
    for acc in acc_range:
        err = 1.0 - acc
        tp = np.full((n_trials, N), err)
        tp[:, 0] = acc
        tpreds = rng_traj.random((n_trials, N)) < tp
        sel = from_resolved(tpreds, rng_traj)
        traj_resolve.append(float((sel == 0).mean()))

    all_results = {}
    wall_start = time.time()

    for icc in ICC_VALUES:
        print(f"\n  ICC = {icc:.4f}")
        rng_n = np.random.default_rng(seed + int(icc * 100000))
        pt_resolve = []
        t0 = time.time()

        for ai, acc in enumerate(acc_range):
            err = 1.0 - acc

            if icc < 0.001:
                noise = rng_n.random((n_trials, N, F_max)) < err
            elif icc > 0.999:
                bf = rng_n.random((n_trials, N, B_max)) < err
                noise = bf[tax, pax, bax]
            else:
                C = 1.0 / icc - 1.0
                a = max(err * C, 1e-8)
                b_param = max((1.0 - err) * C, 1e-8)
                block_p = rng_n.beta(a, b_param, size=(n_trials, N, B_max))
                block_p_test = block_p[tax, pax, bax]
                noise = rng_n.random((n_trials, N, F_max)) < block_p_test

            noisy = gt ^ noise
            score = (noisy & fmask).sum(axis=2)
            sel = best_patch(score, rng_n)
            pt_resolve.append(float((sel == 0).mean()))

            if (ai + 1) % 15 == 0:
                el = time.time() - t0
                eta = el / (ai + 1) * (len(acc_range) - ai - 1)
                print(f"    [{ai+1}/{len(acc_range)}] acc={acc:.2f} "
                      f"pt={pt_resolve[-1]:.3f} traj={traj_resolve[ai]:.3f} "
                      f"({el:.0f}s, ~{eta:.0f}s)")

        adv = [round(p - t, 4) for p, t in zip(pt_resolve, traj_resolve)]

        target_idx = [i for i, a in enumerate(acc_range) if 0.70 <= a <= 0.85]
        target_adv = [adv[i] for i in target_idx]

        result = {
            'icc': icc,
            'pertest': [round(x, 4) for x in pt_resolve],
            'advantage': adv,
            'target_zone': {
                'mean': round(float(np.mean(target_adv)), 4),
                'min': round(float(np.min(target_adv)), 4),
                'max': round(float(np.max(target_adv)), 4),
            }
        }
        all_results[f'icc_{icc:.4f}'] = result

        tz = result['target_zone']
        print(f"  -> Target zone: mean={tz['mean']:.4f} "
              f"[{tz['min']:.4f}, {tz['max']:.4f}] "
              f"({time.time()-t0:.1f}s)")

    # Summary
    print(f"\nTotal wall time: {time.time()-wall_start:.0f}s")
    print("\n" + "=" * 75)
    print("ICC SENSITIVITY: TARGET ZONE (70-85%) ADVANTAGE")
    print("=" * 75)
    print(f"{'ICC':>10} {'Mean Adv':>12} {'Mean Adv %':>12} {'Note':>25}")
    print("-" * 75)
    for icc in ICC_VALUES:
        key = f'icc_{icc:.4f}'
        tz = all_results[key]['target_zone']
        note = ""
        if icc == 0.0: note = "i.i.d. baseline"
        elif icc == 0.191: note = "<-- function-level"
        elif icc == 0.3146: note = "<-- repo-level"
        print(f"{icc:>10.4f} {tz['mean']:>12.4f} {tz['mean']*100:>11.2f}% {note:>25}")
    print("=" * 75)

    func_adv = all_results['icc_0.1910']['target_zone']['mean']
    repo_adv = all_results['icc_0.3146']['target_zone']['mean']
    iid_adv = all_results['icc_0.0000']['target_zone']['mean']
    print(f"\n  i.i.d. (ICC=0):             {iid_adv*100:.2f}%")
    print(f"  Function-level (ICC=0.191): {func_adv*100:.2f}%")
    print(f"  Repo-level (ICC=0.3146):    {repo_adv*100:.2f}%")
    print(f"  Repo vs Function:           {(repo_adv-func_adv)*100:+.2f}pp")
    if func_adv > 1e-6:
        print(f"  Repo / Function ratio:      {repo_adv/func_adv:.2f}x")

    # Save JSON
    output = {
        'params': {
            'N': N, 'n_trials': n_trials, 'seed': seed,
            'icc_values': ICC_VALUES,
            'accuracy': [round(float(a), 2) for a in acc_range],
            'f2p_stats': {
                'n': len(SYNTH_F2P),
                'median': int(np.median(SYNTH_F2P)),
                'mean': round(float(SYNTH_F2P.mean()), 2),
            },
        },
        'trajectory': [round(x, 4) for x in traj_resolve],
        'results': all_results,
    }
    json_path = os.path.join(ART, 'oracle_icc_sensitivity.json')
    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved {json_path}")

    plot_results(output, acc_range)


def plot_results(data, acc_range):
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 11,
        'axes.spines.top': False, 'axes.spines.right': False,
        'figure.dpi': 300, 'savefig.dpi': 300,
        'savefig.bbox': 'tight', 'savefig.pad_inches': 0.08,
    })

    results = data['results']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

    # Panel A: advantage curves per ICC
    cmap = plt.cm.viridis_r
    norm = plt.Normalize(0, 0.5)

    for icc in ICC_VALUES:
        key = f'icc_{icc:.4f}'
        r = results[key]
        color = cmap(norm(icc))
        lw, ls, alpha = 1.2, '-', 0.7

        if icc == 0.191:
            lw, ls, alpha, color = 2.5, '--', 1.0, '#d62728'
        elif icc == 0.3146:
            lw, ls, alpha, color = 2.5, '-.', 1.0, '#2ca02c'
        elif icc == 0.0:
            lw, ls, alpha, color = 2.0, ':', 0.8, '#888888'

        label = f'ICC={icc:.3f}'
        if icc == 0.191: label = 'ICC=0.191 (function)'
        elif icc == 0.3146: label = 'ICC=0.315 (repo)'
        elif icc == 0.0: label = 'ICC=0 (i.i.d.)'

        ax1.plot(acc_range, [a * 100 for a in r['advantage']],
                 color=color, lw=lw, ls=ls, alpha=alpha, label=label)

    ax1.axvspan(0.70, 0.85, alpha=0.06, color='green')
    ax1.axhline(0, color='gray', lw=0.5)
    ax1.set_xlabel('Per-test Accuracy', fontsize=12)
    ax1.set_ylabel('Advantage (pp)', fontsize=12)
    ax1.set_title('Per-test Advantage vs Accuracy\nby ICC Level', fontsize=13)
    ax1.legend(fontsize=8, loc='upper left')
    ax1.grid(True, alpha=0.15)
    ax1.set_xlim(min(acc_range), max(acc_range))

    # Panel B: bar chart of target zone advantage
    means = [results[f'icc_{icc:.4f}']['target_zone']['mean'] for icc in ICC_VALUES]
    bar_colors = []
    for icc in ICC_VALUES:
        if icc == 0.0: bar_colors.append('#888888')
        elif icc == 0.191: bar_colors.append('#d62728')
        elif icc == 0.3146: bar_colors.append('#2ca02c')
        else: bar_colors.append('#1f77b4')

    x = np.arange(len(ICC_VALUES))
    ax2.bar(x, [m * 100 for m in means], color=bar_colors, alpha=0.85, width=0.6,
            edgecolor='white', linewidth=0.8)
    ax2.set_xticks(x)
    labels = []
    for icc in ICC_VALUES:
        if icc == 0.191: labels.append('0.191\n(func.)')
        elif icc == 0.3146: labels.append('0.315\n(repo)')
        elif icc == 0.0: labels.append('0\n(i.i.d.)')
        else: labels.append(f'{icc:.2f}')
    ax2.set_xticklabels(labels, fontsize=9)
    ax2.set_xlabel('ICC', fontsize=12)
    ax2.set_ylabel('Mean Advantage (pp)\n70-85% accuracy zone', fontsize=11)
    ax2.set_title('Target Zone Advantage vs ICC', fontsize=13)
    ax2.grid(axis='y', alpha=0.15)

    for i, (xi, m) in enumerate(zip(x, means)):
        ax2.text(xi, m * 100 + 0.2, f'{m*100:.1f}', ha='center',
                 fontsize=8, fontweight='bold',
                 color=bar_colors[i] if bar_colors[i] != '#888888' else '#555555')

    plt.tight_layout()

    for fmt in ['pdf', 'png']:
        path = os.path.join(ART, f'oracle_icc_sensitivity.{fmt}')
        plt.savefig(path, format=fmt)
    plt.close()
    print("Saved oracle_icc_sensitivity.pdf + .png")


if __name__ == '__main__':
    main()
