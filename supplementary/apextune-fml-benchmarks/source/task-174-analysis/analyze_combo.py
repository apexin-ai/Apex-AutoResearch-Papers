"""Aggregate task-174 phase D: 2x2 combo {K restarts} x {adaptive calibration}."""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RD = os.path.join(HERE, 'exp-results', 'results')


def col(recs, key):
    vals = [r[key]['abs_aod'] for r in recs if r.get(key)]
    return np.array(vals)


def main(tag):
    recs = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(RD, f'D_{tag}_s*.json')))]
    if not recs:
        print('no D records'); return 1
    recs.sort(key=lambda r: r['seed'])
    print('=' * 80)
    print(f'phase D · champion={tag} · {len(recs)} seeds · 2x2 {{K1,K3}} x {{none,cal}} (val AOD)')
    print('-' * 80)
    for r in recs:
        g = lambda k: (f'{r[k]["abs_aod"]:.5f}' if r.get(k) else 'NONE ')
        print(f'  seed {r["seed"]:>3}: K1_none={g("K1_none")} K1_cal={g("K1_cal")} | '
              f'K3_none={g("K3_none")} K3_cal={g("K3_cal")} | d1={r["d1"]} d3={r["d3"]}')
    print('-' * 80)
    for k in ('K1_none', 'K1_cal', 'K3_none', 'K3_cal'):
        a = col(recs, k)
        print(f'  {k:<9}: mean={a.mean():.5f}  std={a.std(ddof=1):.5f}  '
              f'min={a.min():.5f}  max={a.max():.5f}  (n={len(a)})')
    print('=' * 80)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'r2'))
