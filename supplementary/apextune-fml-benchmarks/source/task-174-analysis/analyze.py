"""Aggregate task-174 A1/A2/A3 sweep results (runs under local python3)."""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RD = os.path.join(HERE, 'exp-results', 'results')


def load(tag):
    with open(os.path.join(RD, tag + '.json')) as fh:
        return json.load(fh)


def aod_rows(pa, y, yh):
    def r(m):
        pos, neg = m & (y == 1), m & (y == 0)
        return (yh[pos].mean() if pos.sum() else 0.0), (yh[neg].mean() if neg.sum() else 0.0)
    tu, fu = r(pa == 0)
    tp, fp = r(pa == 1)
    return 0.5 * ((tu - tp) + (fu - fp))


def boot(pa, y, yh, n=2000, seed=0):
    rng = np.random.default_rng(seed)
    k = len(y)
    v = np.array([abs(aod_rows(pa[i], y[i], yh[i]))
                  for i in (rng.integers(0, k, k) for _ in range(n))])
    return v.mean(), v.std()


def load_rows(tag):
    d = json.load(open(os.path.join(RD, tag + '_rows.json')))
    return np.array(d['pa']), np.array(d['y']), np.array(d['yhat'])


def stat(tags):
    xs = [load(t)['abs_aod'] for t in tags if os.path.exists(os.path.join(RD, t + '.json'))]
    return np.array(xs)


def main():
    seeds = [233, 1, 2, 3, 4, 5, 6, 7]
    print('=' * 68)
    # A1 determinism
    a = load('A1_baseline_s233_a')['abs_aod']
    b = load('A1_baseline_s233_b')['abs_aod']
    print(f'A1 determinism: run_a={a:.6f} run_b={b:.6f} -> '
          f'{"IDENTICAL (deterministic eval)" if abs(a-b) < 1e-9 else "DIFFER (non-deterministic)"}')

    # A2 / A3
    a2 = stat([f'A2_baseline_s{s}' for s in seeds])
    a3 = stat([f'A3_bestof3_s{s}' for s in seeds])
    print('-' * 68)
    print(f'A2 baseline   (n={len(a2)}): mean={a2.mean():.5f} std={a2.std(ddof=1):.5f} '
          f'min={a2.min():.5f} max={a2.max():.5f}')
    print(f'A3 best-of-3  (n={len(a3)}): mean={a3.mean():.5f} std={a3.std(ddof=1):.5f} '
          f'min={a3.min():.5f} max={a3.max():.5f}')
    delta = a3.mean() - a2.mean()
    print(f'delta mean (A3-A2): {delta:+.5f}  |  std ratio: {a3.std(ddof=1)/a2.std(ddof=1):.2f}x')

    # bootstrap measurement noise on a baseline run (canonical val abs_aod ~ campaign test scale)
    pa, y, yh = load_rows('A2_baseline_s233')
    m, sd = boot(pa, y, yh)
    print('-' * 68)
    print(f'bootstrap(val n={len(y)}) abs_aod mean={m:.5f} std={sd:.5f}  '
          f'-> ~{(sd/0.38246)*100:.0f}% relative measurement noise on this 475-row split')

    # per-seed table
    print('-' * 68)
    print('seed   A2_baseline   A3_bestof3   picked  proxy(A3)')
    for s in seeds:
        t2 = os.path.join(RD, f'A2_baseline_s{s}.json')
        t3 = os.path.join(RD, f'A3_bestof3_s{s}.json')
        v2 = json.load(open(t2))['abs_aod'] if os.path.exists(t2) else float('nan')
        if os.path.exists(t3):
            d3 = json.load(open(t3))
            print(f'{s:<5}  {v2:.5f}       {d3["abs_aod"]:.5f}      {d3["picked"]}      '
                  f'{[round(x,3) for x in d3["proxy"]]}')
        else:
            print(f'{s:<5}  {v2:.5f}       (pending)')
    print('=' * 68)


def phase_b():
    seeds = [233, 1, 2, 3, 4, 5, 6, 7]
    print('\n=== Phase B: v5 champion mechanisms, seed sweep (val abs_aod) ===')
    rows = {}
    for tag in ('r1', 'r2', 'r3'):
        xs, errs = [], 0
        for s in seeds:
            p = os.path.join(RD, f'B_{tag}_s{s}.json')
            if not os.path.exists(p):
                continue
            d = json.load(open(p))
            if 'abs_aod' in d:
                xs.append(d['abs_aod'])
            else:
                errs += 1
        if xs:
            a = np.array(xs)
            rows[tag] = a
            print(f'  {tag}: n={len(a)} mean={a.mean():.5f} std={a.std(ddof=1):.5f} '
                  f'min={a.min():.5f} max={a.max():.5f}' + (f' errors={errs}' if errs else ''))
    if rows:
        allx = np.concatenate(list(rows.values()))
        print(f'  pooled champions: n={len(allx)} mean={allx.mean():.5f} std={allx.std(ddof=1):.5f}')


if __name__ == '__main__':
    rc = main()
    phase_b()
    sys.exit(rc)
