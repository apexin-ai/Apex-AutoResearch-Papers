#!/usr/bin/env python3
# MVP-A Total (F2P+P2P) Oracle Simulation
# Models both FAIL_TO_PASS and PASS_TO_PASS tests with real SWE-bench distributions.
# Wrong patches: high F2P fail rate (Beta(2,5)) + low P2P regression rate (sweep: 5%/10%/20%).
# Sweeps accuracy x regression_rate x noise_model (i.i.d. + block-correlated).
import numpy as np, json, time, os
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR, 'swebench_test_stats.json')) as f:
    _stats = json.load(f)
    RAW_F2P = np.array(_stats['raw_f2p'])
    RAW_P2P = np.array(_stats['raw_p2p'])

F2P_CAP = 100
P2P_CAP = 500


def build_f2p_gt(rng, n_trials, N, T_f2p, F2P_max):
    gt = np.ones((n_trials, N, F2P_max), dtype=bool)
    for t in range(n_trials):
        T = T_f2p[t]
        for p in range(1, N):
            fp = rng.beta(2, 5)
            fails = rng.random(T) < fp
            if not fails.any():
                fails[rng.integers(T)] = True
            gt[t, p, :T] = ~fails
    return gt


def build_p2p_gt(rng, n_trials, N, T_p2p, P2P_max, regression_rate):
    gt = np.ones((n_trials, N, P2P_max), dtype=bool)
    for t in range(n_trials):
        T = T_p2p[t]
        if T == 0:
            continue
        for p in range(1, N):
            fails = rng.random(T) < regression_rate
            gt[t, p, :T] = ~fails
    return gt


def build_blocks(rng, T_vals, T_max):
    n = len(T_vals)
    bids = np.zeros((n, T_max), dtype=np.int32)
    nb = np.zeros(n, dtype=np.int32)
    for t in range(n):
        T = T_vals[t]; idx = bid = 0
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


def run_one_regression_rate(rng_seed, N, n_trials, acc_range, regression_rate):
    rng = np.random.default_rng(rng_seed)

    T_f2p = np.clip(rng.choice(RAW_F2P, size=n_trials), 1, F2P_CAP)
    T_p2p = np.clip(rng.choice(RAW_P2P, size=n_trials), 0, P2P_CAP)
    T_total = T_f2p + T_p2p

    F_max = int(T_f2p.max())
    P_max = max(int(T_p2p.max()), 1)

    print(f"\n  Regression rate = {regression_rate:.0%}")
    print(f"  F2P: median={np.median(T_f2p):.0f}, mean={T_f2p.mean():.1f}, "
          f"range=[{T_f2p.min()}, {T_f2p.max()}]")
    print(f"  P2P: median={np.median(T_p2p):.0f}, mean={T_p2p.mean():.1f}, "
          f"range=[{T_p2p.min()}, {T_p2p.max()}]")
    print(f"  Total: median={np.median(T_total):.0f}, mean={T_total.mean():.1f}")

    gt_f = build_f2p_gt(rng, n_trials, N, T_f2p, F_max)
    gt_p = build_p2p_gt(rng, n_trials, N, T_p2p, P_max, regression_rate)

    fmask = (np.arange(F_max)[None, :] < T_f2p[:, None])[:, None, :]
    pmask = (np.arange(P_max)[None, :] < T_p2p[:, None])[:, None, :]

    f_bids, f_nb = build_blocks(rng, T_f2p, F_max)
    p_bids, p_nb = build_blocks(rng, T_p2p, P_max)
    FB_max = max(int(f_nb.max()), 1)
    PB_max = max(int(p_nb.max()), 1)

    tax = np.arange(n_trials)[:, None, None]
    pax = np.arange(N)[None, :, None]
    f_bax = f_bids[:, None, :]
    p_bax = p_bids[:, None, :]

    iid_pt, blk_pt, traj = [], [], []
    t0 = time.time()

    for ai, acc in enumerate(acc_range):
        # I.I.D. per-test
        fi_f = rng.random((n_trials, N, F_max)) >= acc
        noisy_f = gt_f ^ fi_f
        score_f = (noisy_f & fmask).sum(axis=2)

        fi_p = rng.random((n_trials, N, P_max)) >= acc
        noisy_p = gt_p ^ fi_p
        score_p = (noisy_p & pmask).sum(axis=2)

        sel_i = best_patch(score_f + score_p, rng)
        iid_pt.append(float((sel_i == 0).mean()))

        # Block-correlated per-test
        bf_f = rng.random((n_trials, N, FB_max)) < (1.0 - acc)
        tf_f = bf_f[tax, pax, f_bax]
        noisy_bf = gt_f ^ tf_f
        score_bf = (noisy_bf & fmask).sum(axis=2)

        bf_p = rng.random((n_trials, N, PB_max)) < (1.0 - acc)
        tf_p = bf_p[tax, pax, p_bax]
        noisy_bp = gt_p ^ tf_p
        score_bp = (noisy_bp & pmask).sum(axis=2)

        sel_b = best_patch(score_bf + score_bp, rng)
        blk_pt.append(float((sel_b == 0).mean()))

        # Trajectory-level
        tp = np.full((n_trials, N), 1.0 - acc)
        tp[:, 0] = acc
        tpreds = rng.random((n_trials, N)) < tp
        sel_t = from_resolved(tpreds, rng)
        traj.append(float((sel_t == 0).mean()))

        if (ai + 1) % 10 == 0:
            el = time.time() - t0
            eta = el / (ai + 1) * (len(acc_range) - ai - 1)
            print(f"    [{ai+1}/{len(acc_range)}] p={acc:.2f} "
                  f"iid={iid_pt[-1]:.3f} blk={blk_pt[-1]:.3f} "
                  f"traj={traj[-1]:.3f} ({el:.0f}s, ~{eta:.0f}s)")

    print(f"    Done in {time.time() - t0:.1f}s")

    acc_list = [round(float(a), 2) for a in acc_range]
    iid_adv = [round(p - t, 4) for p, t in zip(iid_pt, traj)]
    blk_adv = [round(p - t, 4) for p, t in zip(blk_pt, traj)]

    ti = [(i, a) for i, a in enumerate(acc_list) if 0.70 <= a <= 0.85]
    iid_t = [iid_adv[i] for i, _ in ti]
    blk_t = [blk_adv[i] for i, _ in ti]

    return {
        'regression_rate': regression_rate,
        'T_f2p_median': float(np.median(T_f2p)),
        'T_f2p_mean': round(float(T_f2p.mean()), 1),
        'T_p2p_median': float(np.median(T_p2p)),
        'T_p2p_mean': round(float(T_p2p.mean()), 1),
        'T_total_median': float(np.median(T_total)),
        'T_total_mean': round(float(T_total.mean()), 1),
        'pct_p2p_zero': round(float((T_p2p == 0).mean()), 4),
        'accuracy': acc_list,
        'iid_pt': [round(x, 4) for x in iid_pt],
        'block_pt': [round(x, 4) for x in blk_pt],
        'trajectory': [round(x, 4) for x in traj],
        'iid_advantage': iid_adv,
        'block_advantage': blk_adv,
        'target_iid': {'mean': round(float(np.mean(iid_t)), 4),
                       'min': round(float(min(iid_t)), 4),
                       'max': round(float(max(iid_t)), 4)},
        'target_block': {'mean': round(float(np.mean(blk_t)), 4),
                         'min': round(float(min(blk_t)), 4),
                         'max': round(float(max(blk_t)), 4)},
    }


def plot_results(all_results, regression_rates):
    fig, axes = plt.subplots(1, 3, figsize=(21, 6))

    for idx, rr in enumerate(regression_rates):
        key = f"rr_{int(rr*100):02d}"
        r = all_results[key]
        acc = r['accuracy']
        ax = axes[idx]

        ax.plot(acc, r['block_pt'], color='#d62728', lw=2, label='Block per-test')
        ax.plot(acc, r['iid_pt'], color='#1f77b4', lw=2, label='I.I.D. per-test')
        ax.plot(acc, r['trajectory'], color='gray', lw=2, ls='--', label='Trajectory')
        ax.axvspan(0.70, 0.85, alpha=0.08, color='green')

        bm = r['target_block']['mean']
        im = r['target_iid']['mean']
        bp = "PASS" if bm >= 0.05 else "FAIL"
        ip = "PASS" if im >= 0.05 else "FAIL"

        ax.set_xlabel('Per-test Accuracy', fontsize=11)
        ax.set_ylabel('P(correct patch selected)', fontsize=11)
        ax.set_title(f'P2P Regression = {rr:.0%}\n'
                     f'Block 70-85%: {bm:.1%} ({bp}), '
                     f'I.I.D.: {im:.1%} ({ip})', fontsize=11)
        ax.legend(fontsize=9, loc='upper left')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(min(acc), max(acc))

    plt.suptitle('MVP-A Total (F2P+P2P) Oracle Simulation — Real SWE-bench Distribution',
                 fontsize=14, y=1.02)
    plt.tight_layout()
    pdf_path = os.path.join(DIR, 'mvp_a_total_curves.pdf')
    plt.savefig(pdf_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved {pdf_path}")


def main():
    N, n_trials, seed = 16, 10000, 42
    acc_range = np.round(np.arange(0.55, 0.995, 0.01), 2)
    regression_rates = [0.05, 0.10, 0.20]

    print("MVP-A Total (F2P+P2P) Oracle Simulation")
    print(f"  N={N}, trials={n_trials}, seed={seed}")
    print(f"  Regression rates: {regression_rates}")
    print(f"  F2P pool: {len(RAW_F2P)} instances, P2P pool: {len(RAW_P2P)} instances")

    all_results = {}
    for rr in regression_rates:
        result = run_one_regression_rate(
            seed + int(rr * 100), N, n_trials, acc_range, rr)
        all_results[f"rr_{int(rr*100):02d}"] = result

    # Summary table
    print("\n" + "=" * 85)
    print("TOTAL (F2P+P2P) SIMULATION RESULTS")
    print("=" * 85)
    print(f"{'Reg.Rate':>10} {'Noise':>8} {'70-85% Mean Adv':>18} "
          f"{'Min':>8} {'Max':>8} {'Pass(>=5%)':>12}")
    print("-" * 85)
    for rr in regression_rates:
        key = f"rr_{int(rr*100):02d}"
        r = all_results[key]
        for noise, tkey in [("i.i.d.", "target_iid"), ("block", "target_block")]:
            d = r[tkey]
            passed = "PASS" if d['mean'] >= 0.05 else "FAIL"
            print(f"{rr:>10.0%} {noise:>8} {d['mean']:>18.4f} "
                  f"{d['min']:>8.4f} {d['max']:>8.4f} {passed:>12}")
    print("=" * 85)

    # F2P-only comparison
    f2p_path = os.path.join(DIR, 'mvp_a_real_f2p_results.json')
    if os.path.exists(f2p_path):
        with open(f2p_path) as f:
            f2p = json.load(f)['result']
        print("\n" + "=" * 85)
        print("COMPARISON: F2P-only vs Total (F2P+P2P)")
        print("=" * 85)
        print(f"{'Scenario':>25} {'Noise':>8} {'70-85% Mean Adv':>18} {'Pass':>8}")
        print("-" * 85)
        for noise, tkey in [("i.i.d.", "target_iid"), ("block", "target_block")]:
            d = f2p[tkey]
            p = "PASS" if d['mean'] >= 0.05 else "FAIL"
            print(f"{'F2P-only':>25} {noise:>8} {d['mean']:>18.4f} {p:>8}")
        for rr in regression_rates:
            key = f"rr_{int(rr*100):02d}"
            r = all_results[key]
            for noise, tkey in [("i.i.d.", "target_iid"), ("block", "target_block")]:
                d = r[tkey]
                p = "PASS" if d['mean'] >= 0.05 else "FAIL"
                label = f"Total (reg={rr:.0%})"
                print(f"{label:>25} {noise:>8} {d['mean']:>18.4f} {p:>8}")
        print("=" * 85)

    # Save JSON
    output = {
        'params': {'N': N, 'n_trials': n_trials, 'seed': seed,
                   'regression_rates': regression_rates,
                   'f2p_cap': F2P_CAP, 'p2p_cap': P2P_CAP},
        'results': all_results
    }
    json_path = os.path.join(DIR, 'mvp_a_total_results.json')
    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved {json_path}")

    plot_results(all_results, regression_rates)


if __name__ == '__main__':
    main()
