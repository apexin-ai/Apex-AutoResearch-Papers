import pandas as pd
import numpy as np
import json
from numpy.random import default_rng

df = pd.read_csv('results/analysis/cross_model_4way_bf16.csv')
N = len(df)
grand_mean = df['correct'].mean()
total_var = df['correct'].var()
ss_total = total_var * (N - 1)

n_m, n_t, n_p, n_s, n_o, n_i = 4, 3, 6, 6, 4, 200

print(f"N={N}, grand_mean={grand_mean:.6f}, total_var={total_var:.6f}")

model_acc = df.groupby('model')['correct'].mean().to_dict()
print("\nModel accuracies:")
for m, a in sorted(model_acc.items()):
    print(f"  {m}: {a:.6f}")

# Build 6D array
models_sorted = sorted(df['model'].unique())
temps_sorted = sorted(df['temperature'].unique())
prompts_sorted = sorted(df['prompt_template'].unique())
seeds_sorted = sorted(df['seed'].unique())
orders_sorted = sorted(df['ordering'].unique())
items_sorted = sorted(df['item_id'].unique())

model_map = {v: i for i, v in enumerate(models_sorted)}
temp_map = {v: i for i, v in enumerate(temps_sorted)}
prompt_map = {v: i for i, v in enumerate(prompts_sorted)}
seed_map = {v: i for i, v in enumerate(seeds_sorted)}
order_map = {v: i for i, v in enumerate(orders_sorted)}
item_map = {v: i for i, v in enumerate(items_sorted)}

Y = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)
for _, row in df.iterrows():
    Y[model_map[row['model']], temp_map[row['temperature']], prompt_map[row['prompt_template']],
      seed_map[row['seed']], order_map[row['ordering']], item_map[row['item_id']]] = row['correct']

print(f"Array shape: {Y.shape}, NaN: {np.isnan(Y).sum()}")

def compute_gstudy(Y_arr):
    nm, nt, np_, ns, no, ni = Y_arr.shape
    N_arr = nm * nt * np_ * ns * no * ni
    gm = np.nanmean(Y_arr)
    
    mean_m = np.nanmean(Y_arr, axis=(1,2,3,4,5))
    mean_t = np.nanmean(Y_arr, axis=(0,2,3,4,5))
    mean_p = np.nanmean(Y_arr, axis=(0,1,3,4,5))
    mean_s = np.nanmean(Y_arr, axis=(0,1,2,4,5))
    mean_o = np.nanmean(Y_arr, axis=(0,1,2,3,5))
    mean_i = np.nanmean(Y_arr, axis=(0,1,2,3,4))
    
    ss = {}
    ss['model'] = (nt*np_*ns*no*ni) * np.sum((mean_m - gm)**2)
    ss['temperature'] = (nm*np_*ns*no*ni) * np.sum((mean_t - gm)**2)
    ss['prompt_template'] = (nm*nt*ns*no*ni) * np.sum((mean_p - gm)**2)
    ss['seed'] = (nm*nt*np_*no*ni) * np.sum((mean_s - gm)**2)
    ss['ordering'] = (nm*nt*np_*ns*ni) * np.sum((mean_o - gm)**2)
    ss['item_id'] = (nm*nt*np_*ns*no) * np.sum((mean_i - gm)**2)
    
    def ss_interaction(mean_ab, mean_a, mean_b, scale, shape_a, shape_b):
        total = 0.0
        for a in range(shape_a):
            for b in range(shape_b):
                exp = gm + (mean_a[a] - gm) + (mean_b[b] - gm)
                total += (mean_ab[a, b] - exp)**2
        return total * scale
    
    mean_mi = np.nanmean(Y_arr, axis=(1,2,3,4))
    ss['model:item_id'] = ss_interaction(mean_mi, mean_m, mean_i, nt*np_*ns*no, nm, ni)
    
    mean_mt = np.nanmean(Y_arr, axis=(2,3,4,5))
    ss['model:temperature'] = ss_interaction(mean_mt, mean_m, mean_t, np_*ns*no*ni, nm, nt)
    
    mean_mp = np.nanmean(Y_arr, axis=(1,3,4,5))
    ss['model:prompt_template'] = ss_interaction(mean_mp, mean_m, mean_p, nt*ns*no*ni, nm, np_)
    
    mean_ms = np.nanmean(Y_arr, axis=(1,2,4,5))
    ss['model:seed'] = ss_interaction(mean_ms, mean_m, mean_s, nt*np_*no*ni, nm, ns)
    
    mean_mo = np.nanmean(Y_arr, axis=(1,2,3,5))
    ss['model:ordering'] = ss_interaction(mean_mo, mean_m, mean_o, nt*np_*ns*ni, nm, no)
    
    mean_ti = np.nanmean(Y_arr, axis=(0,2,3,4))
    ss['temperature:item_id'] = ss_interaction(mean_ti, mean_t, mean_i, nm*np_*ns*no, nt, ni)
    
    mean_pi = np.nanmean(Y_arr, axis=(0,1,3,4))
    ss['prompt_template:item_id'] = ss_interaction(mean_pi, mean_p, mean_i, nm*nt*ns*no, np_, ni)
    
    mean_si = np.nanmean(Y_arr, axis=(0,1,2,4))
    ss['seed:item_id'] = ss_interaction(mean_si, mean_s, mean_i, nm*nt*np_*no, ns, ni)
    
    mean_oi = np.nanmean(Y_arr, axis=(0,1,2,3))
    ss['ordering:item_id'] = ss_interaction(mean_oi, mean_o, mean_i, nm*nt*np_*ns, no, ni)
    
    ss_total_b = np.nansum((Y_arr - gm)**2)
    ss_resid = max(0, ss_total_b - sum(ss.values()))
    ss['residual'] = ss_resid
    
    df_dict = {
        'model': nm-1, 'temperature': nt-1, 'prompt_template': np_-1,
        'seed': ns-1, 'ordering': no-1, 'item_id': ni-1,
        'model:item_id': (nm-1)*(ni-1), 'model:temperature': (nm-1)*(nt-1),
        'model:prompt_template': (nm-1)*(np_-1), 'model:seed': (nm-1)*(ns-1),
        'model:ordering': (nm-1)*(no-1), 'temperature:item_id': (nt-1)*(ni-1),
        'prompt_template:item_id': (np_-1)*(ni-1), 'seed:item_id': (ns-1)*(ni-1),
        'ordering:item_id': (no-1)*(ni-1),
    }
    df_resid = N_arr - 1 - sum(df_dict.values())
    df_dict['residual'] = max(1, df_resid)
    
    ms = {k: ss[k]/df_dict[k] if df_dict.get(k,0) > 0 else 0 for k in ss}
    
    # EMS variance components
    s2 = {}
    s2['residual'] = ms['residual']
    s2['model:item_id'] = max(0, (ms['model:item_id'] - ms['residual']) / (nt*np_*ns*no))
    s2['temperature:item_id'] = max(0, (ms['temperature:item_id'] - ms['residual']) / (nm*np_*ns*no))
    s2['prompt_template:item_id'] = max(0, (ms['prompt_template:item_id'] - ms['residual']) / (nm*nt*ns*no))
    s2['seed:item_id'] = max(0, (ms['seed:item_id'] - ms['residual']) / (nm*nt*np_*no))
    s2['ordering:item_id'] = max(0, (ms['ordering:item_id'] - ms['residual']) / (nm*nt*np_*ns))
    s2['item_id'] = max(0, (ms['item_id'] - ms['model:item_id'] - ms['temperature:item_id'] - ms['prompt_template:item_id'] - ms['seed:item_id'] - ms['ordering:item_id'] + 4*ms['residual']) / (nm*nt*np_*ns*no))
    s2['model'] = max(0, (ms['model'] - ms['model:item_id']) / (nt*np_*ns*no*ni))
    s2['temperature'] = max(0, (ms['temperature'] - ms['temperature:item_id']) / (nm*np_*ns*no*ni))
    s2['prompt_template'] = max(0, (ms['prompt_template'] - ms['prompt_template:item_id']) / (nm*nt*ns*no*ni))
    s2['seed'] = max(0, (ms['seed'] - ms['seed:item_id']) / (nm*nt*np_*no*ni))
    s2['ordering'] = max(0, (ms['ordering'] - ms['ordering:item_id']) / (nm*nt*np_*ns*ni))
    s2['model:temperature'] = max(0, (ms['model:temperature'] - ms['residual']) / (np_*ns*no*ni))
    s2['model:prompt_template'] = max(0, (ms['model:prompt_template'] - ms['residual']) / (nt*ns*no*ni))
    s2['model:seed'] = max(0, (ms['model:seed'] - ms['residual']) / (nt*np_*no*ni))
    s2['model:ordering'] = max(0, (ms['model:ordering'] - ms['residual']) / (nt*np_*ns*ni))
    
    s2_total = sum(s2.values())
    vpct = {k: v/s2_total*100 if s2_total > 0 else 0 for k, v in s2.items()}
    
    delta = (
        s2['model:item_id'] / nm +
        s2['temperature:item_id'] / nt +
        s2['prompt_template:item_id'] / np_ +
        s2['seed:item_id'] / ns +
        s2['ordering:item_id'] / no +
        s2['residual'] / (nm * nt * np_ * ns * no)
    )
    g_item = s2['item_id'] / (s2['item_id'] + delta) if (s2['item_id'] + delta) > 0 else 0
    
    return {'vpct': vpct, 's2': s2, 'g_item': g_item, 'gm': gm, 'ss': ss, 'ms': ms, 'df': df_dict, 'delta': delta}

# Full dataset
res = compute_gstudy(Y)
print("\n=== EMS Variance Components (%) ===")
for k, v in sorted(res['vpct'].items(), key=lambda x: -x[1]):
    if v > 0.01:
        print(f"  {k}: {v:.4f}%")

print(f"\nG_item = {res['g_item']:.6f}")
print(f"  sigma2_item = {res['s2']['item_id']:.8f}")
print(f"  sigma2_delta = {res['delta']:.8f}")

# D-study
print("\n=== D-study ===")
d_study = []
for n_m_d in [1, 2, 3, 4, 5, 6, 8, 10]:
    delta = (
        res['s2']['model:item_id'] / n_m_d +
        res['s2']['temperature:item_id'] / n_t +
        res['s2']['prompt_template:item_id'] / n_p +
        res['s2']['seed:item_id'] / n_s +
        res['s2']['ordering:item_id'] / n_o +
        res['s2']['residual'] / (n_m_d * n_t * n_p * n_s * n_o)
    )
    g = res['s2']['item_id'] / (res['s2']['item_id'] + delta)
    d_study.append({'n_models': n_m_d, 'g_item': round(g, 6), 'sigma_delta': round(delta, 8)})
    print(f"  n_models={n_m_d:2d}: G_item={g:.6f}")

# Bootstrap
print("\n=== Bootstrap (200 resamples) ===")
rng = default_rng(42)
n_boot = 200
boot_results = []
for b in range(n_boot):
    if b % 50 == 0: print(f"  {b}/{n_boot}...")
    idx = rng.choice(n_i, size=n_i, replace=True)
    Y_b = Y[:, :, :, :, :, idx]
    boot_results.append(compute_gstudy(Y_b))

boot_vpcts = [r['vpct'] for r in boot_results]
boot_g_items = [r['g_item'] for r in boot_results]

ci = {}
for comp in ['item_id', 'model:item_id', 'model', 'temperature', 'prompt_template', 
             'seed', 'ordering', 'temperature:item_id', 'prompt_template:item_id',
             'seed:item_id', 'ordering:item_id', 'residual']:
    vals = [b.get(comp, 0) for b in boot_vpcts]
    lo, hi = np.percentile(vals, 2.5), np.percentile(vals, 97.5)
    ci[comp] = (lo, hi)
    if res['vpct'].get(comp, 0) > 0.01:
        print(f"  {comp}: {res['vpct'][comp]:.4f}% [{lo:.4f}, {hi:.4f}]")

g_arr = np.array(boot_g_items)
g_ci = (float(np.percentile(g_arr, 2.5)), float(np.percentile(g_arr, 97.5)))
print(f"\n  G_item: {res['g_item']:.6f} [{g_ci[0]:.6f}, {g_ci[1]:.6f}]")

# Per-model contribution to model×item
print("\n=== Per-model contribution to model×item ===")
mean_m_full = np.nanmean(Y, axis=(1,2,3,4,5))
mean_i_full = np.nanmean(Y, axis=(0,1,2,3,4))
mean_mi_full = np.nanmean(Y, axis=(1,2,3,4))

model_contribs = {}
total_sq = 0.0
for mi in range(n_m):
    c = 0.0
    for ii in range(n_i):
        exp = grand_mean + (mean_m_full[mi] - grand_mean) + (mean_i_full[ii] - grand_mean)
        c += (mean_mi_full[mi, ii] - exp)**2
    model_contribs[models_sorted[mi]] = c
    total_sq += c

for m in models_sorted:
    pct = model_contribs[m] / total_sq * 100
    print(f"  {m}: {pct:.2f}%")

# Save
output = {
    'dataset': 'A-4',
    'description': '4 models (Llama-3.1-8B, Gemma-2-9B, Mistral-7B, Qwen3-8B) x bf16 only, fully crossed',
    'n_observations': int(N),
    'n_levels': {'model': n_m, 'temperature': n_t, 'prompt_template': n_p, 'seed': n_s, 'ordering': n_o, 'item_id': n_i},
    'grand_mean': float(grand_mean),
    'total_variance': float(total_var),
    'model_accuracies': {k: float(v) for k, v in model_acc.items()},
    'variance_components_ems': {
        k: {
            'estimate': float(res['s2'][k]),
            'pct': float(res['vpct'][k]),
            'ci_95_lower_pct': float(ci[k][0]) if k in ci else None,
            'ci_95_upper_pct': float(ci[k][1]) if k in ci else None,
        }
        for k in res['s2']
    },
    'g_item': {
        'g': float(res['g_item']),
        'ci_95': list(g_ci),
        'sigma_tau': float(res['s2']['item_id']),
        'sigma_delta': float(res['delta']),
    },
    'd_study_model_sweep': d_study,
    'per_model_interaction_contribution': {m: round(model_contribs[m]/total_sq*100, 2) for m in models_sorted},
    'bootstrap': {'n_resamples': n_boot, 'seed': 42, 'method': 'item cluster resampling (numpy 6D array)'},
    'anova_table': {k: {'ss': float(res['ss'][k]), 'df': int(res['df'][k]), 'ms': float(res['ms'][k])} for k in res['ss']},
}

with open('results/analysis/dataset_a4_gstudy.json', 'w') as f:
    json.dump(output, f, indent=2, default=str)
print("\nSaved to results/analysis/dataset_a4_gstudy.json")
