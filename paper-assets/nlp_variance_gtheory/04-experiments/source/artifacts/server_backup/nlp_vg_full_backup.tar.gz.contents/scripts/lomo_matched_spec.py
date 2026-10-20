"""LOMO analysis with matched dataset_a4 Henderson I EMS specification.

Same model as exp001_4model_gstudy_v2.py: 6 main effects + 9 two-way
interactions (5 model:X + 4 X:item_id) + residual.
"""

import json
import numpy as np
import pandas as pd
from pathlib import Path

INPUT = 'results/analysis/cross_model_4way_bf16.csv'
OUTPUT = 'results/analysis/lomo_matched_spec.json'

REF_ITEM_PCT = 42.07
REF_MI_PCT = 33.64
REF_G_ITEM = 0.8200


def build_6d_array(df, facet_order):
    facet_vals = {}
    facet_maps = {}
    for f in facet_order:
        vals = sorted(df[f].unique())
        facet_vals[f] = vals
        facet_maps[f] = {v: i for i, v in enumerate(vals)}
    shape = tuple(len(facet_vals[f]) for f in facet_order)
    Y = np.full(shape, np.nan)
    indices = tuple(df[f].map(facet_maps[f]).values for f in facet_order)
    Y[indices] = df['correct'].values
    return Y, facet_vals


def ss_interaction(mean_ab, mean_a, mean_b, gm, scale, sa, sb):
    total = 0.0
    for a in range(sa):
        for b in range(sb):
            exp = gm + (mean_a[a] - gm) + (mean_b[b] - gm)
            total += (mean_ab[a, b] - exp) ** 2
    return total * scale


def compute_gstudy(Y_arr):
    nm, nt, np_, ns, no, ni = Y_arr.shape
    N = nm * nt * np_ * ns * no * ni
    gm = float(np.nanmean(Y_arr))

    mm = np.nanmean(Y_arr, axis=(1,2,3,4,5))
    mt = np.nanmean(Y_arr, axis=(0,2,3,4,5))
    mp = np.nanmean(Y_arr, axis=(0,1,3,4,5))
    ms_ = np.nanmean(Y_arr, axis=(0,1,2,4,5))
    mo = np.nanmean(Y_arr, axis=(0,1,2,3,5))
    mi = np.nanmean(Y_arr, axis=(0,1,2,3,4))

    ss = {}
    ss['model']           = (nt*np_*ns*no*ni) * float(np.sum((mm - gm)**2))
    ss['temperature']     = (nm*np_*ns*no*ni) * float(np.sum((mt - gm)**2))
    ss['prompt_template'] = (nm*nt*ns*no*ni)  * float(np.sum((mp - gm)**2))
    ss['seed']            = (nm*nt*np_*no*ni) * float(np.sum((ms_ - gm)**2))
    ss['ordering']        = (nm*nt*np_*ns*ni) * float(np.sum((mo - gm)**2))
    ss['item_id']         = (nm*nt*np_*ns*no) * float(np.sum((mi - gm)**2))

    mean_mi = np.nanmean(Y_arr, axis=(1,2,3,4))
    ss['model:item_id'] = ss_interaction(mean_mi, mm, mi, gm, nt*np_*ns*no, nm, ni)

    mean_mt = np.nanmean(Y_arr, axis=(2,3,4,5))
    ss['model:temperature'] = ss_interaction(mean_mt, mm, mt, gm, np_*ns*no*ni, nm, nt)

    mean_mp = np.nanmean(Y_arr, axis=(1,3,4,5))
    ss['model:prompt_template'] = ss_interaction(mean_mp, mm, mp, gm, nt*ns*no*ni, nm, np_)

    mean_ms = np.nanmean(Y_arr, axis=(1,2,4,5))
    ss['model:seed'] = ss_interaction(mean_ms, mm, ms_, gm, nt*np_*no*ni, nm, ns)

    mean_mo = np.nanmean(Y_arr, axis=(1,2,3,5))
    ss['model:ordering'] = ss_interaction(mean_mo, mm, mo, gm, nt*np_*ns*ni, nm, no)

    mean_ti = np.nanmean(Y_arr, axis=(0,2,3,4))
    ss['temperature:item_id'] = ss_interaction(mean_ti, mt, mi, gm, nm*np_*ns*no, nt, ni)

    mean_pi = np.nanmean(Y_arr, axis=(0,1,3,4))
    ss['prompt_template:item_id'] = ss_interaction(mean_pi, mp, mi, gm, nm*nt*ns*no, np_, ni)

    mean_si = np.nanmean(Y_arr, axis=(0,1,2,4))
    ss['seed:item_id'] = ss_interaction(mean_si, ms_, mi, gm, nm*nt*np_*no, ns, ni)

    mean_oi = np.nanmean(Y_arr, axis=(0,1,2,3))
    ss['ordering:item_id'] = ss_interaction(mean_oi, mo, mi, gm, nm*nt*np_*ns, no, ni)

    ss_total = float(np.nansum((Y_arr - gm)**2))
    ss['residual'] = max(0.0, ss_total - sum(ss.values()))

    df = {
        'model': nm-1, 'temperature': nt-1, 'prompt_template': np_-1,
        'seed': ns-1, 'ordering': no-1, 'item_id': ni-1,
        'model:item_id': (nm-1)*(ni-1), 'model:temperature': (nm-1)*(nt-1),
        'model:prompt_template': (nm-1)*(np_-1), 'model:seed': (nm-1)*(ns-1),
        'model:ordering': (nm-1)*(no-1), 'temperature:item_id': (nt-1)*(ni-1),
        'prompt_template:item_id': (np_-1)*(ni-1), 'seed:item_id': (ns-1)*(ni-1),
        'ordering:item_id': (no-1)*(ni-1),
    }
    df['residual'] = max(1, N - 1 - sum(df.values()))

    ms = {k: ss[k] / df[k] if df.get(k, 0) > 0 else 0.0 for k in ss}

    # Henderson I EMS — exactly matching exp001_4model_gstudy_v2.py
    s2 = {}
    s2['residual']               = ms['residual']
    s2['model:item_id']          = max(0, (ms['model:item_id'] - ms['residual']) / (nt*np_*ns*no))
    s2['temperature:item_id']    = max(0, (ms['temperature:item_id'] - ms['residual']) / (nm*np_*ns*no))
    s2['prompt_template:item_id']= max(0, (ms['prompt_template:item_id'] - ms['residual']) / (nm*nt*ns*no))
    s2['seed:item_id']           = max(0, (ms['seed:item_id'] - ms['residual']) / (nm*nt*np_*no))
    s2['ordering:item_id']       = max(0, (ms['ordering:item_id'] - ms['residual']) / (nm*nt*np_*ns))
    # +4 = (num X:item interactions) - 1 = 5 - 1
    s2['item_id'] = max(0, (ms['item_id'] - ms['model:item_id'] - ms['temperature:item_id']
                            - ms['prompt_template:item_id'] - ms['seed:item_id']
                            - ms['ordering:item_id'] + 4*ms['residual']) / (nm*nt*np_*ns*no))
    s2['model']            = max(0, (ms['model'] - ms['model:item_id']) / (nt*np_*ns*no*ni))
    s2['temperature']      = max(0, (ms['temperature'] - ms['temperature:item_id']) / (nm*np_*ns*no*ni))
    s2['prompt_template']  = max(0, (ms['prompt_template'] - ms['prompt_template:item_id']) / (nm*nt*ns*no*ni))
    s2['seed']             = max(0, (ms['seed'] - ms['seed:item_id']) / (nm*nt*np_*no*ni))
    s2['ordering']         = max(0, (ms['ordering'] - ms['ordering:item_id']) / (nm*nt*np_*ns*ni))
    s2['model:temperature']      = max(0, (ms['model:temperature'] - ms['residual']) / (np_*ns*no*ni))
    s2['model:prompt_template']  = max(0, (ms['model:prompt_template'] - ms['residual']) / (nt*ns*no*ni))
    s2['model:seed']             = max(0, (ms['model:seed'] - ms['residual']) / (nt*np_*no*ni))
    s2['model:ordering']         = max(0, (ms['model:ordering'] - ms['residual']) / (nt*np_*ns*ni))

    s2_total = sum(s2.values())
    vpct = {k: v / s2_total * 100 if s2_total > 0 else 0.0 for k, v in s2.items()}

    delta = (
        s2['model:item_id'] / nm +
        s2['temperature:item_id'] / nt +
        s2['prompt_template:item_id'] / np_ +
        s2['seed:item_id'] / ns +
        s2['ordering:item_id'] / no +
        s2['residual'] / (nm * nt * np_ * ns * no)
    )
    g_item = s2['item_id'] / (s2['item_id'] + delta) if (s2['item_id'] + delta) > 0 else 0.0

    return {
        'vpct': vpct, 's2': {k: float(v) for k, v in s2.items()},
        'g_item': float(g_item), 'delta': float(delta), 'gm': gm,
        'n_levels': {'model': nm, 'temperature': nt, 'prompt_template': np_,
                     'seed': ns, 'ordering': no, 'item_id': ni},
    }


# ── Load ──────────────────────────────────────────────────────────────────
df = pd.read_csv(INPUT)
for f in ['model', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']:
    df[f] = df[f].astype(str)

models = sorted(df['model'].unique())
print(f"Loaded {len(df)} obs, models: {models}")
facet_order = ['model', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']

# ── Full 4-model validation ───────────────────────────────────────────────
Y_full, _ = build_6d_array(df, facet_order)
print(f"Full array: {Y_full.shape}, NaN: {np.isnan(Y_full).sum()}")

res_full = compute_gstudy(Y_full)

print(f"\n=== Full 4-model validation ===")
for comp in sorted(res_full['vpct'], key=lambda k: -res_full['vpct'][k]):
    if res_full['vpct'][comp] >= 0.01:
        print(f"  {comp:<28} {res_full['vpct'][comp]:>7.2f}%")
print(f"\n  item_id:       {res_full['vpct']['item_id']:.4f}% (ref: {REF_ITEM_PCT}%)")
print(f"  model:item_id: {res_full['vpct']['model:item_id']:.4f}% (ref: {REF_MI_PCT}%)")
print(f"  G_item:        {res_full['g_item']:.6f} (ref: {REF_G_ITEM})")

item_ok = abs(res_full['vpct']['item_id'] - REF_ITEM_PCT) <= 1.0
mi_ok   = abs(res_full['vpct']['model:item_id'] - REF_MI_PCT) <= 1.0
g_ok    = abs(res_full['g_item'] - REF_G_ITEM) <= 0.01

if not (item_ok and mi_ok and g_ok):
    print(f"\nVALIDATION FAILED!")
    print(f"  item_id diff:  {res_full['vpct']['item_id'] - REF_ITEM_PCT:+.4f}pp {'OK' if item_ok else 'FAIL'}")
    print(f"  m:i diff:      {res_full['vpct']['model:item_id'] - REF_MI_PCT:+.4f}pp {'OK' if mi_ok else 'FAIL'}")
    print(f"  G_item diff:   {res_full['g_item'] - REF_G_ITEM:+.6f} {'OK' if g_ok else 'FAIL'}")
    import sys; sys.exit(1)

print("  VALIDATION PASSED\n")

# ── Leave-one-out ─────────────────────────────────────────────────────────
print("=== Leave-one-model-out ===")
print(f"{'Dropped':<35} {'item_id%':>9} {'m:i%':>9} {'G_item':>9}")
print("-" * 65)
print(f"{'(full 4-model)':<35} {res_full['vpct']['item_id']:>9.2f} {res_full['vpct']['model:item_id']:>9.2f} {res_full['g_item']:>9.4f}")

loo_results = {}
for drop_model in models:
    subset = df[df['model'] != drop_model]
    Y_sub, _ = build_6d_array(subset, facet_order)
    res = compute_gstudy(Y_sub)

    loo_results[drop_model] = {
        'remaining_models': sorted(subset['model'].unique().tolist()),
        'n_observations': int(np.prod(Y_sub.shape)),
        'grand_mean': res['gm'],
        'variance_pct': {k: round(v, 4) for k, v in res['vpct'].items()},
        'variance_s2': res['s2'],
        'G_item': round(res['g_item'], 6),
        'sigma_tau': round(res['s2']['item_id'], 8),
        'sigma_delta': round(res['delta'], 8),
        'n_levels': res['n_levels'],
    }

    print(f"{drop_model:<35} {res['vpct']['item_id']:>9.2f} {res['vpct']['model:item_id']:>9.2f} {res['g_item']:>9.4f}")

# ── Stability ─────────────────────────────────────────────────────────────
item_pcts = [r['variance_pct']['item_id'] for r in loo_results.values()]
mi_pcts   = [r['variance_pct']['model:item_id'] for r in loo_results.values()]
g_items   = [r['G_item'] for r in loo_results.values()]

stability = {
    'item_id_range':  [round(min(item_pcts), 4), round(max(item_pcts), 4)],
    'item_id_spread': round(max(item_pcts) - min(item_pcts), 4),
    'model_item_range':  [round(min(mi_pcts), 4), round(max(mi_pcts), 4)],
    'model_item_spread': round(max(mi_pcts) - min(mi_pcts), 4),
    'G_item_range':  [round(min(g_items), 6), round(max(g_items), 6)],
    'G_item_spread': round(max(g_items) - min(g_items), 6),
}

print(f"\nStability:")
print(f"  item_id:    [{stability['item_id_range'][0]:.2f}, {stability['item_id_range'][1]:.2f}]  spread={stability['item_id_spread']:.2f}pp")
print(f"  model:item: [{stability['model_item_range'][0]:.2f}, {stability['model_item_range'][1]:.2f}]  spread={stability['model_item_spread']:.2f}pp")
print(f"  G_item:     [{stability['G_item_range'][0]:.4f}, {stability['G_item_range'][1]:.4f}]  spread={stability['G_item_spread']:.4f}")

# ── Save ──────────────────────────────────────────────────────────────────
output = {
    'description': 'LOMO with matched dataset_a4 Henderson I EMS (6 main + 9 two-way interactions)',
    'model_spec': {
        'main_effects': ['model', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id'],
        'interactions': [
            'model:item_id', 'model:temperature', 'model:prompt_template', 'model:seed', 'model:ordering',
            'temperature:item_id', 'prompt_template:item_id', 'seed:item_id', 'ordering:item_id',
        ],
    },
    'full_4model': {
        'n_observations': int(np.prod(Y_full.shape)),
        'grand_mean': res_full['gm'],
        'variance_pct': {k: round(v, 4) for k, v in res_full['vpct'].items()},
        'variance_s2': res_full['s2'],
        'G_item': round(res_full['g_item'], 6),
        'sigma_tau': round(res_full['s2']['item_id'], 8),
        'sigma_delta': round(res_full['delta'], 8),
        'n_levels': res_full['n_levels'],
        'validation': {'item_id_pct': round(res_full['vpct']['item_id'], 2),
                        'model_item_pct': round(res_full['vpct']['model:item_id'], 2),
                        'G_item': round(res_full['g_item'], 4), 'passed': True},
    },
    'leave_one_out': loo_results,
    'stability': stability,
}

Path(OUTPUT).parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {OUTPUT}")
