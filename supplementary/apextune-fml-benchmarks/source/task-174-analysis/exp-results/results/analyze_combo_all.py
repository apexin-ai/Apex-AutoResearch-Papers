"""Aggregate task-174 phase D across all champions: {K1,K3} x {none,cal}."""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RD = os.path.join(HERE, 'exp-results', 'results')


def main(tags):
    print('=' * 92)
    print('phase D · 2x2 {K restarts} x {adaptive calibration} on champion mechanisms (val AOD)')
    print('=' * 92)
    print(f'{"champ":<6} {"K1_none":>18} {"K3_none":>18} {"K1_cal":>18} {"K3_cal":>18}')
    for tag in tags:
        recs = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(RD, f'D_{tag}_s*.json')))]
        if not recs:
            continue
        cols = []
        for k in ('K1_none', 'K3_none', 'K1_cal', 'K3_cal'):
            a = np.array([r[k]['abs_aod'] for r in recs if r.get(k)])
            cols.append(f'{a.mean():.4f}±{a.std(ddof=1):.4f}' if len(a) else '—')
        print(f'{tag:<6} {cols[0]:>18} {cols[1]:>18} {cols[2]:>18} {cols[3]:>18}')
    print('-' * 92)
    # verdict
    for tag in tags:
        recs = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(RD, f'D_{tag}_s*.json')))]
        if not recs:
            continue
        k1 = np.array([r['K1_none']['abs_aod'] for r in recs if r.get('K1_none')])
        k3c = np.array([r['K3_cal']['abs_aod'] for r in recs if r.get('K3_cal')])
        better = 'K1_none 最优(叠加有害)' if k1.mean() < k3c.mean() else 'K3_cal 最优(叠加有益)'
        print(f'  {tag}: K1_none={k1.mean():.4f} vs K3_cal={k3c.mean():.4f}  -> {better}')
    print('=' * 92)


if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['r1', 'r2', 'r3'])
