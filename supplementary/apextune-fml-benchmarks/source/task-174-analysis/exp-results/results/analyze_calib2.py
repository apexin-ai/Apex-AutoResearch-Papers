"""Aggregate task-174 phase C2: adaptive vs fixed calibration."""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RD = os.path.join(HERE, 'exp-results', 'results')


def main(tag):
    recs = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(RD, f'C2_{tag}_s*.json')))]
    if not recs:
        print('no C2 records'); return 1
    print('=' * 76)
    print(f'phase C2 · mechanism={tag} · {len(recs)} seeds · 训练侧选 delta 应用到 val')
    print('-' * 76)
    da, va, vn, vf, vo = [], [], [], [], []
    for r in sorted(recs, key=lambda x: x['seed']):
        s = r['seed']
        ad = r['val_adaptive']
        da.append(r['delta_adaptive'] if r['delta_adaptive'] is not None else np.nan)
        if ad: va.append(ad['abs_aod'])
        vn.append(r['val_none']['abs_aod'])
        vf.append(r['val_fixed008']['abs_aod'])
        vo.append(r['val_oracle']['abs_aod'] if r['val_oracle'] else np.nan)
        a_adapt = f'{ad["abs_aod"]:.5f}' if ad else 'NONE(floor)'
        print(f'  seed {s:>3}: d_adapt={r["delta_adaptive"]} | val AOD adapt={a_adapt} '
              f'none={r["val_none"]["abs_aod"]:.5f} fixed.08={r["val_fixed008"]["abs_aod"]:.5f} '
              f'oracle={r["val_oracle"]["abs_aod"] if r["val_oracle"] else float("nan"):.5f}')
    va, vn, vf, vo, da = map(np.array, (va, vn, vf, vo, da))
    print('-' * 76)
    print(f'val AOD (mean ± std over seeds):')
    print(f'  no calibration      : {vn.mean():.5f} ± {vn.std(ddof=1):.5f}')
    print(f'  fixed delta=0.08     : {vf.mean():.5f} ± {vf.std(ddof=1):.5f}')
    print(f'  adaptive (train-fit) : {va.mean():.5f} ± {va.std(ddof=1):.5f}  (n={len(va)})')
    print(f'  val oracle (upper bd): {np.nanmean(vo):.5f} ± {np.nanstd(vo, ddof=1):.5f}')
    print('-' * 76)
    print(f'adaptive delta chosen: mean={np.nanmean(da):+.4f} std={np.nanstd(da, ddof=1):.4f} '
          f'range=[{np.nanmin(da):+.3f},{np.nanmax(da):+.3f}]')
    print(f'  (correlates with val oracle delta* ? see per-seed above)')
    print('=' * 76)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'baseline'))
