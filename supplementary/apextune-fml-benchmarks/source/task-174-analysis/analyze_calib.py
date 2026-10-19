"""Aggregate task-174 phase C: group-threshold calibration study."""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RD = os.path.join(HERE, 'exp-results', 'results')


def load_curves(tag):
    out = {}
    for p in sorted(glob.glob(os.path.join(RD, f'C_{tag}_s*_curve.json'))):
        d = json.load(open(p))
        out[d['seed']] = d
    return out


def main(tag):
    curves = load_curves(tag)
    if not curves:
        print(f'no curves for {tag}')
        return 1
    deltas = [r['delta'] for r in next(iter(curves.values()))['curve']]
    print('=' * 74)
    print(f'phase C · mechanism={tag} · {len(curves)} seeds · delta grid {deltas[0]}..{deltas[-1]}')
    print('-' * 74)

    best = []
    for s, d in sorted(curves.items(), key=lambda kv: kv[0]):
        bd, ba = d['best_delta'], d['best_abs_aod']
        d0 = d['at_delta0']['abs_aod']
        acc = d['at_delta0']['cls_acc']
        n_improved = sum(1 for r in d['curve'] if r['abs_aod'] < d0)
        best.append((s, bd, ba, d0, d['best_cls_acc']))
        print(f'  seed {s:>3}: delta*={bd:+.3f}  aod*={ba:.5f}  aod(delta=0)={d0:.5f}  '
              f'gain={d0-ba:+.5f}  acc*={d["best_cls_acc"]:.4f}  (improving deltas: {n_improved})')

    bs = np.array([b[1] for b in best])
    print('-' * 74)
    print(f'optimal delta*: mean={bs.mean():+.4f} std={bs.std(ddof=1):.4f} '
          f'min={bs.min():+.3f} max={bs.max():+.3f}')
    print(f'  near 0.08? |delta*-0.08| <= 0.05 for {int((abs(bs-0.08) <= 0.05).sum())}/{len(bs)} seeds')

    # fixed-vs-none-vs-oracle on AOD
    idx08 = int(np.argmin([abs(x - 0.08) for x in deltas]))
    aod0 = np.array([d['at_delta0']['abs_aod'] for d in curves.values()])
    aod008 = np.array([d['curve'][idx08]['abs_aod'] for d in curves.values()])
    oracle = np.array([b[2] for b in best])
    print('-' * 74)
    print(f'AOD on {len(curves)} seeds (val):')
    print(f'  no calibration (delta=0)   : mean={aod0.mean():.5f} std={aod0.std(ddof=1):.5f}')
    print(f'  fixed delta=0.08 (r1-style) : mean={aod008.mean():.5f} std={aod008.std(ddof=1):.5f}')
    print(f'  per-seed oracle delta*      : mean={oracle.mean():.5f} std={oracle.std(ddof=1):.5f}')

    # other fairness metrics at delta*=0.08 vs delta=0
    print('-' * 74)
    print('side metrics at delta=0 -> delta=0.08 (mean over seeds):')
    for key in ('abs_eod', 'abs_di_diff', 'abs_theil', 'cls_acc'):
        v0 = np.mean([d['at_delta0'][key] for d in curves.values()])
        v8 = np.mean([d['curve'][idx08][key] for d in curves.values()])
        print(f'  {key:<14}: {v0:.5f} -> {v8:.5f}  ({v8-v0:+.5f})')

    # accuracy floor check
    floor = 0.63510101010101
    below = sum(1 for d in curves.values() for r in d['curve']
                if r['cls_acc'] < floor and r['abs_aod'] < d['at_delta0']['abs_aod'])
    print('-' * 74)
    print(f'accuracy floor {floor}: {below} (seed,delta) points improve AOD but break the floor')
    print('=' * 74)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'baseline'))
