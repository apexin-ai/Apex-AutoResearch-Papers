import pandas as pd
import numpy as np
import json
import glob
import os
from numpy.random import default_rng

# ============================================================
# Task 1: Build 4-model bf16 balanced dataset (Dataset A-4)
# ============================================================
print("=" * 60)
print("Task 1: Building 4-model bf16 balanced dataset")
print("=" * 60)

records = []

# Llama (different filename pattern)
for f in sorted(glob.glob('results/exp001_llama/llama_shard_*.jsonl')):
    with open(f) as fh:
        for line in fh:
            records.append(json.loads(line))
print(f"After Llama: {len(records)}")

# Gemma bf16
for f in sorted(glob.glob('results/exp001_gemma/shard_*.jsonl')):
    with open(f) as fh:
        for line in fh:
            records.append(json.loads(line))
print(f"After Gemma: {len(records)}")

# Gemma fp32 (include for completeness but will be filtered out)
for f in sorted(glob.glob('results/exp001_gemma_fp32/shard_*.jsonl')):
    with open(f) as fh:
        for line in fh:
            records.append(json.loads(line))
print(f"After Gemma fp32: {len(records)}")

# Mistral
for f in sorted(glob.glob('results/exp001_mistral/shard_*.jsonl')):
    with open(f) as fh:
        for line in fh:
            records.append(json.loads(line))
print(f"After Mistral: {len(records)}")

# Qwen (only main shard files)
for f in sorted(glob.glob('results/exp001_qwen/shard_[0-3].jsonl')):
    with open(f) as fh:
        for line in fh:
            records.append(json.loads(line))
print(f"After Qwen: {len(records)}")

df = pd.DataFrame(records)
print(f"\nRaw total: {len(df)}")
print(f"Models (raw): {df['model'].unique()}")
print(f"Precisions: {df['precision'].unique()}")

# Normalize model names
def normalize_model(name):
    name_lower = name.lower()
    if 'llama' in name_lower:
        return 'llama-3.1-8b-instruct'
    elif 'gemma' in name_lower:
        return 'gemma-2-9b-it'
    elif 'mistral' in name_lower:
        return 'mistral-7b-instruct-v0.3'
    elif 'qwen' in name_lower:
        return 'qwen3-8b'
    else:
        return name

df['model'] = df['model'].apply(normalize_model)
print(f"Models (normalized): {sorted(df['model'].unique())}")
print(f"By model+precision:\n{df.groupby(['model', 'precision']).size().unstack(fill_value=0)}")

# Filter bf16 only
df_a4 = df[df['precision'] == 'bfloat16'].copy()
print(f"\nbf16 total: {len(df_a4)}")
print(f"By model: {df_a4.groupby('model').size().to_dict()}")

# Verify fully crossed design
print("\nDesign verification:")
for model in sorted(df_a4['model'].unique()):
    m_df = df_a4[df_a4['model'] == model]
    n_temps = m_df['temperature'].nunique()
    n_prompts = m_df['prompt_template'].nunique()
    n_seeds = m_df['seed'].nunique()
    n_orders = m_df['ordering'].nunique()
    n_items = m_df['item_id'].nunique()
    n_conds = m_df.groupby(['temperature', 'prompt_template', 'seed', 'ordering']).ngroups
    print(f"  {model}: {len(m_df)} records, {n_conds} conditions, "
          f"{n_temps}T x {n_prompts}P x {n_seeds}S x {n_orders}O x {n_items}I")

# Expected: 4 models x 3 temps x 6 prompts x 6 seeds x 4 orderings x 200 items = 345,600
expected = 4 * 3 * 6 * 6 * 4 * 200
print(f"\nExpected: {expected}, Got: {len(df_a4)}")

os.makedirs('results/analysis', exist_ok=True)
df_a4.to_csv('results/analysis/cross_model_4way_bf16.csv', index=False)
print(f"Dataset A-4 saved: {len(df_a4)} records")

# ============================================================
# Task 2: 4-model G-study (full ANOVA decomposition)
# ============================================================
print("\n" + "=" * 60)
print("Task 2: 4-model G-study")
print("=" * 60)

grand_mean = df_a4['correct'].mean()
N = len(df_a4)
total_var = df_a4['correct'].var()
ss_total = total_var * (N - 1)

print(f"Grand mean: {grand_mean:.6f}")
print(f"N: {N}")
print(f"Total variance: {total_var:.6f}")
print(f"SS_total: {ss_total:.2f}")

# Model accuracies
model_acc = df_a4.groupby('model')['correct'].mean().to_dict()
print(f"\nModel accuracies:")
for m, a in sorted(model_acc.items()):
    print(f"  {m}: {a:.6f}")

# Main effects
facets = ['model', 'temperature', 'prompt_template', 'seed', 'ordering', 'item_id']
anova = {}

for facet in facets:
    group_means = df_a4.groupby(facet)['correct'].mean()
    n_levels = len(group_means)
    n_per_level = N // n_levels
    ss = n_per_level * ((group_means - grand_mean) ** 2).sum()
    df_f = n_levels - 1
    anova[facet] = {'ss': float(ss), 'df': df_f, 'ms': float(ss / df_f), 
                    'n_levels': n_levels, 'mean_range': [float(group_means.min()), float(group_means.max())]}

# All 2-way interactions
interaction_pairs = []
for i, f1 in enumerate(facets):
    for f2 in facets[i+1:]:
        interaction_pairs.append((f1, f2))

for f1, f2 in interaction_pairs:
    cell_means = df_a4.groupby([f1, f2])['correct'].mean()
    marginal_A = df_a4.groupby(f1)['correct'].mean()
    marginal_B = df_a4.groupby(f2)['correct'].mean()
    n_a = df_a4[f1].nunique()
    n_b = df_a4[f2].nunique()
    n_per_cell = N // (n_a * n_b)
    
    interaction_ss = 0.0
    for (a, b), cell_mean in cell_means.items():
        expected = grand_mean + (marginal_A[a] - grand_mean) + (marginal_B[b] - grand_mean)
        interaction_ss += (cell_mean - expected) ** 2
    interaction_ss *= n_per_cell
    
    df_int = (n_a - 1) * (n_b - 1)
    key = f'{f1}:{f2}'
    anova[key] = {'ss': float(interaction_ss), 'df': df_int, 
                  'ms': float(interaction_ss / df_int) if df_int > 0 else 0}

# Residual
ss_explained = sum(v['ss'] for v in anova.values())
ss_residual = max(0, ss_total - ss_explained)
df_total = N - 1
df_explained = sum(v['df'] for v in anova.values())
df_residual = df_total - df_explained
anova['residual'] = {'ss': float(ss_residual), 'df': int(df_residual),
                     'ms': float(ss_residual / df_residual) if df_residual > 0 else 0}

# Variance percentages
all_ss = {k: v['ss'] for k, v in anova.items()}
total_ss_sum = sum(all_ss.values())
variance_pct = {k: v / total_ss_sum * 100 for k, v in all_ss.items()}

print("\n=== 4-Model Variance Components (SS%) ===")
for k, v in sorted(variance_pct.items(), key=lambda x: -x[1]):
    if v > 0.01:
        print(f"  {k}: {v:.4f}%  (SS={all_ss[k]:.2f})")

# Variance component estimates (EMS-based)
n_m, n_t, n_p, n_s, n_o, n_i = 4, 3, 6, 6, 4, 200

# sigma^2 estimates from MS
ms = {k: v['ms'] for k, v in anova.items()}
sigma2 = {}
sigma2['residual'] = ms['residual']
sigma2['model:item_id'] = (ms['model:item_id'] - ms['residual']) / (n_t * n_p * n_s * n_o)
sigma2['temperature:item_id'] = (ms['temperature:item_id'] - ms['residual']) / (n_m * n_p * n_s * n_o)
sigma2['prompt_template:item_id'] = (ms['prompt_template:item_id'] - ms['residual']) / (n_m * n_t * n_s * n_o)
sigma2['seed:item_id'] = (ms['seed:item_id'] - ms['residual']) / (n_m * n_t * n_p * n_o)
sigma2['ordering:item_id'] = (ms['ordering:item_id'] - ms['residual']) / (n_m * n_t * n_p * n_s)
sigma2['item_id'] = (ms['item_id'] - ms.get('model:item_id', 0) - ms.get('temperature:item_id', 0) - ms.get('prompt_template:item_id', 0) - ms.get('seed:item_id', 0) - ms.get('ordering:item_id', 0) + 4 * ms['residual']) / (n_m * n_t * n_p * n_s * n_o)
sigma2['model'] = (ms['model'] - ms['model:item_id']) / (n_t * n_p * n_s * n_o * n_i)
sigma2['temperature'] = (ms['temperature'] - ms['temperature:item_id']) / (n_m * n_p * n_s * n_o * n_i)
sigma2['prompt_template'] = (ms['prompt_template'] - ms['prompt_template:item_id']) / (n_m * n_t * n_s * n_o * n_i)
sigma2['seed'] = (ms['seed'] - ms['seed:item_id']) / (n_m * n_t * n_p * n_o * n_i)
sigma2['ordering'] = (ms['ordering'] - ms['ordering:item_id']) / (n_m * n_t * n_p * n_s * n_i)

# Other 2-way interactions (not involving item_id)
for f1, f2 in interaction_pairs:
    key = f'{f1}:{f2}'
    if 'item_id' in key or key in sigma2:
        continue
    # Approximate: (MS_AB - MS_residual) / n_per_cell_other
    denom = N // (anova[key]['df'] + 1)  # rough
    sigma2[key] = max(0, (ms[key] - ms['residual'])) / (N // (df_a4[f1].nunique() * df_a4[f2].nunique()))

# Clamp negative estimates to 0
for k in sigma2:
    sigma2[k] = max(0, sigma2[k])

sigma2_total = sum(sigma2.values())
var_comp_pct = {k: v / sigma2_total * 100 for k, v in sigma2.items()}

print("\n=== EMS-based Variance Components (%) ===")
for k, v in sorted(var_comp_pct.items(), key=lambda x: -x[1]):
    if v > 0.01:
        print(f"  {k}: {v:.4f}% (sigma2={sigma2[k]:.8f})")

# G_item calculation
sigma2_item = sigma2['item_id']
sigma2_delta_item = (
    sigma2['model:item_id'] / n_m +
    sigma2['temperature:item_id'] / n_t +
    sigma2['prompt_template:item_id'] / n_p +
    sigma2['seed:item_id'] / n_s +
    sigma2['ordering:item_id'] / n_o +
    sigma2['residual'] / (n_m * n_t * n_p * n_s * n_o)
)
G_item = sigma2_item / (sigma2_item + sigma2_delta_item)
print(f"\nG_item (4 models, EMS) = {G_item:.6f}")
print(f"  sigma2_item = {sigma2_item:.8f}")
print(f"  sigma2_delta = {sigma2_delta_item:.8f}")

# D-study: vary n_models
print("\n=== D-study (G_item vs n_models) ===")
d_study = []
for n_m_d in [1, 2, 3, 4, 5, 6, 8, 10]:
    delta = (
        sigma2['model:item_id'] / n_m_d +
        sigma2['temperature:item_id'] / n_t +
        sigma2['prompt_template:item_id'] / n_p +
        sigma2['seed:item_id'] / n_s +
        sigma2['ordering:item_id'] / n_o +
        sigma2['residual'] / (n_m_d * n_t * n_p * n_s * n_o)
    )
    g = sigma2_item / (sigma2_item + delta)
    d_study.append({'n_models': n_m_d, 'g_item': round(g, 6), 
                    'sigma_tau': round(sigma2_item, 8), 'sigma_delta': round(delta, 8)})
    print(f"  n_models={n_m_d:2d}: G_item={g:.6f} (delta={delta:.8f})")

# ============================================================
# Task 3: Bootstrap 200 resamples CI
# ============================================================
print("\n" + "=" * 60)
print("Task 3: Bootstrap confidence intervals (200 resamples)")
print("=" * 60)

rng = default_rng(42)
items = df_a4['item_id'].unique()
n_items_total = len(items)
n_boot = 200

# Pre-build numpy array for fast bootstrap
# Dimensions: model x temperature x prompt x seed x ordering x item
models_sorted = sorted(df_a4['model'].unique())
temps_sorted = sorted(df_a4['temperature'].unique())
prompts_sorted = sorted(df_a4['prompt_template'].unique())
seeds_sorted = sorted(df_a4['seed'].unique())
orders_sorted = sorted(df_a4['ordering'].unique())
items_sorted = sorted(df_a4['item_id'].unique())

model_map = {v: i for i, v in enumerate(models_sorted)}
temp_map = {v: i for i, v in enumerate(temps_sorted)}
prompt_map = {v: i for i, v in enumerate(prompts_sorted)}
seed_map = {v: i for i, v in enumerate(seeds_sorted)}
order_map = {v: i for i, v in enumerate(orders_sorted)}
item_map = {v: i for i, v in enumerate(items_sorted)}

Y = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)
for _, row in df_a4.iterrows():
    mi = model_map[row['model']]
    ti = temp_map[row['temperature']]
    pi = prompt_map[row['prompt_template']]
    si = seed_map[row['seed']]
    oi = order_map[row['ordering']]
    ii = item_map[row['item_id']]
    Y[mi, ti, pi, si, oi, ii] = row['correct']

nan_count = np.isnan(Y).sum()
print(f"6D array shape: {Y.shape}, NaN count: {nan_count}")

def compute_gstudy_from_array(Y_arr):
    """Compute G-study from 6D numpy array (model x temp x prompt x seed x order x item)"""
    nm, nt, np_, ns, no, ni = Y_arr.shape
    N = nm * nt * np_ * ns * no * ni
    gm = np.nanmean(Y_arr)
    
    # Main effect means
    mean_m = np.nanmean(Y_arr, axis=(1,2,3,4,5))
    mean_t = np.nanmean(Y_arr, axis=(0,2,3,4,5))
    mean_p = np.nanmean(Y_arr, axis=(0,1,3,4,5))
    mean_s = np.nanmean(Y_arr, axis=(0,1,2,4,5))
    mean_o = np.nanmean(Y_arr, axis=(0,1,2,3,5))
    mean_i = np.nanmean(Y_arr, axis=(0,1,2,3,4))
    
    # SS main effects
    ss_m = (nt*np_*ns*no*ni) * np.sum((mean_m - gm)**2)
    ss_t = (nm*np_*ns*no*ni) * np.sum((mean_t - gm)**2)
    ss_p = (nm*nt*ns*no*ni) * np.sum((mean_p - gm)**2)
    ss_s = (nm*nt*np_*no*ni) * np.sum((mean_s - gm)**2)
    ss_o = (nm*nt*np_*ns*ni) * np.sum((mean_o - gm)**2)
    ss_i = (nm*nt*np_*ns*no) * np.sum((mean_i - gm)**2)
    
    # Key 2-way interactions
    # model x item
    mean_mi = np.nanmean(Y_arr, axis=(1,2,3,4))  # (nm, ni)
    ss_mi = 0.0
    for m in range(nm):
        for i in range(ni):
            exp = gm + (mean_m[m] - gm) + (mean_i[i] - gm)
            ss_mi += (mean_mi[m, i] - exp)**2
    ss_mi *= (nt * np_ * ns * no)
    
    # model x temperature
    mean_mt = np.nanmean(Y_arr, axis=(2,3,4,5))
    ss_mt = 0.0
    for m in range(nm):
        for t in range(nt):
            exp = gm + (mean_m[m] - gm) + (mean_t[t] - gm)
            ss_mt += (mean_mt[m, t] - exp)**2
    ss_mt *= (np_ * ns * no * ni)
    
    # model x prompt
    mean_mp = np.nanmean(Y_arr, axis=(1,3,4,5))
    ss_mp = 0.0
    for m in range(nm):
        for p in range(np_):
            exp = gm + (mean_m[m] - gm) + (mean_p[p] - gm)
            ss_mp += (mean_mp[m, p] - exp)**2
    ss_mp *= (nt * ns * no * ni)
    
    # model x seed
    mean_ms = np.nanmean(Y_arr, axis=(1,2,4,5))
    ss_ms = 0.0
    for m in range(nm):
        for s in range(ns):
            exp = gm + (mean_m[m] - gm) + (mean_s[s] - gm)
            ss_ms += (mean_ms[m, s] - exp)**2
    ss_ms *= (nt * np_ * no * ni)
    
    # model x ordering
    mean_mo = np.nanmean(Y_arr, axis=(1,2,3,5))
    ss_mo = 0.0
    for m in range(nm):
        for o in range(no):
            exp = gm + (mean_m[m] - gm) + (mean_o[o] - gm)
            ss_mo += (mean_mo[m, o] - exp)**2
    ss_mo *= (nt * np_ * ns * ni)
    
    # temp x item
    mean_ti = np.nanmean(Y_arr, axis=(0,2,3,4))
    ss_ti = 0.0
    for t in range(nt):
        for i in range(ni):
            exp = gm + (mean_t[t] - gm) + (mean_i[i] - gm)
            ss_ti += (mean_ti[t, i] - exp)**2
    ss_ti *= (nm * np_ * ns * no)
    
    # prompt x item
    mean_pi = np.nanmean(Y_arr, axis=(0,1,3,4))
    ss_pi = 0.0
    for p in range(np_):
        for i in range(ni):
            exp = gm + (mean_p[p] - gm) + (mean_i[i] - gm)
            ss_pi += (mean_pi[p, i] - exp)**2
    ss_pi *= (nm * nt * ns * no)
    
    # seed x item
    mean_si = np.nanmean(Y_arr, axis=(0,1,2,4))
    ss_si = 0.0
    for s in range(ns):
        for i in range(ni):
            exp = gm + (mean_s[s] - gm) + (mean_i[i] - gm)
            ss_si += (mean_si[s, i] - exp)**2
    ss_si *= (nm * nt * np_ * no)
    
    # ordering x item
    mean_oi = np.nanmean(Y_arr, axis=(0,1,2,3))
    ss_oi = 0.0
    for o in range(no):
        for i in range(ni):
            exp = gm + (mean_o[o] - gm) + (mean_i[i] - gm)
            ss_oi += (mean_oi[o, i] - exp)**2
    ss_oi *= (nm * nt * np_ * ns)
    
    # Total SS
    ss_total_b = np.nansum((Y_arr - gm)**2)
    
    # All SS components
    all_ss_b = {
        'model': ss_m, 'temperature': ss_t, 'prompt_template': ss_p,
        'seed': ss_s, 'ordering': ss_o, 'item_id': ss_i,
        'model:item_id': ss_mi, 'model:temperature': ss_mt,
        'model:prompt_template': ss_mp, 'model:seed': ss_ms,
        'model:ordering': ss_mo, 'temperature:item_id': ss_ti,
        'prompt_template:item_id': ss_pi, 'seed:item_id': ss_si,
        'ordering:item_id': ss_oi
    }
    ss_resid_b = max(0, ss_total_b - sum(all_ss_b.values()))
    all_ss_b['residual'] = ss_resid_b
    
    # MS
    df_dict = {
        'model': nm-1, 'temperature': nt-1, 'prompt_template': np_-1,
        'seed': ns-1, 'ordering': no-1, 'item_id': ni-1,
        'model:item_id': (nm-1)*(ni-1), 'model:temperature': (nm-1)*(nt-1),
        'model:prompt_template': (nm-1)*(np_-1), 'model:seed': (nm-1)*(ns-1),
        'model:ordering': (nm-1)*(no-1), 'temperature:item_id': (nt-1)*(ni-1),
        'prompt_template:item_id': (np_-1)*(ni-1), 'seed:item_id': (ns-1)*(ni-1),
        'ordering:item_id': (no-1)*(ni-1),
    }
    df_resid = N - 1 - sum(df_dict.values())
    df_dict['residual'] = max(1, df_resid)
    
    ms_dict = {k: all_ss_b[k] / df_dict[k] if df_dict.get(k, 0) > 0 else 0 for k in all_ss_b}
    
    # EMS variance components
    s2 = {}
    s2['residual'] = ms_dict['residual']
    s2['model:item_id'] = max(0, (ms_dict['model:item_id'] - ms_dict['residual']) / (nt * np_ * ns * no))
    s2['temperature:item_id'] = max(0, (ms_dict['temperature:item_id'] - ms_dict['residual']) / (nm * np_ * ns * no))
    s2['prompt_template:item_id'] = max(0, (ms_dict['prompt_template:item_id'] - ms_dict['residual']) / (nm * nt * ns * no))
    s2['seed:item_id'] = max(0, (ms_dict['seed:item_id'] - ms_dict['residual']) / (nm * nt * np_ * no))
    s2['ordering:item_id'] = max(0, (ms_dict['ordering:item_id'] - ms_dict['residual']) / (nm * nt * np_ * ns))
    s2['item_id'] = max(0, (ms_dict['item_id'] - ms_dict.get('model:item_id', 0) - ms_dict.get('temperature:item_id', 0) - ms_dict.get('prompt_template:item_id', 0) - ms_dict.get('seed:item_id', 0) - ms_dict.get('ordering:item_id', 0) + 4*ms_dict['residual']) / (nm * nt * np_ * ns * no))
    
    s2_total = sum(s2.values())
    vpct = {k: v/s2_total*100 if s2_total > 0 else 0 for k, v in s2.items()}
    
    # G_item
    delta = (
        s2['model:item_id'] / nm +
        s2['temperature:item_id'] / nt +
        s2['prompt_template:item_id'] / np_ +
        s2['seed:item_id'] / ns +
        s2['ordering:item_id'] / no +
        s2['residual'] / (nm * nt * np_ * ns * no)
    )
    g_item = s2['item_id'] / (s2['item_id'] + delta) if (s2['item_id'] + delta) > 0 else 0
    
    return vpct, s2, g_item, gm

# Run on full dataset
vpct_full, s2_full, g_item_full, gm_full = compute_gstudy_from_array(Y)
print(f"\nFull dataset G_item = {g_item_full:.6f}")

# Bootstrap
boot_vpcts = []
boot_g_items = []
boot_s2s = []

for b in range(n_boot):
    if b % 50 == 0:
        print(f"  Bootstrap {b}/{n_boot}...")
    boot_idx = rng.choice(n_i, size=n_i, replace=True)
    Y_boot = Y[:, :, :, :, :, boot_idx]
    vpct_b, s2_b, g_b, _ = compute_gstudy_from_array(Y_boot)
    boot_vpcts.append(vpct_b)
    boot_g_items.append(g_b)
    boot_s2s.append(s2_b)

print(f"  Bootstrap complete.")

# CI results
print("\n=== Bootstrap 95% CI ===")
key_components = ['item_id', 'model:item_id', 'model', 'temperature:item_id', 
                  'prompt_template:item_id', 'seed:item_id', 'ordering:item_id', 'residual']
ci_results = {}
for comp in key_components:
    vals = [b.get(comp, 0) for b in boot_vpcts]
    mean_v = np.mean(vals)
    lo, hi = np.percentile(vals, 2.5), np.percentile(vals, 97.5)
    ci_results[comp] = {'mean': mean_v, 'ci_lo': lo, 'ci_hi': hi}
    if mean_v > 0.01 or vpct_full.get(comp, 0) > 0.01:
        print(f"  {comp}: {vpct_full.get(comp, 0):.4f}% (boot mean: {mean_v:.4f}%) [{lo:.4f}, {hi:.4f}]")

g_vals = np.array(boot_g_items)
print(f"\n  G_item: {g_item_full:.6f} (boot mean: {np.mean(g_vals):.6f}) "
      f"[{np.percentile(g_vals, 2.5):.6f}, {np.percentile(g_vals, 97.5):.6f}]")

# ============================================================
# Task 4: Model contribution to model×item interaction
# ============================================================
print("\n" + "=" * 60)
print("Task 4: Per-model contribution to model×item interaction")
print("=" * 60)

mean_m_full = np.nanmean(Y, axis=(1,2,3,4,5))
mean_i_full = np.nanmean(Y, axis=(0,1,2,3,4))
mean_mi_full = np.nanmean(Y, axis=(1,2,3,4))

for mi, mname in enumerate(models_sorted):
    contrib = 0.0
    for ii in range(n_i):
        exp = gm_full + (mean_m_full[mi] - gm_full) + (mean_i_full[ii] - gm_full)
        contrib += (mean_mi_full[mi, ii] - exp)**2
    contrib_pct = contrib / np.sum((mean_mi_full - (gm_full + (mean_m_full[:, None] - gm_full) + (mean_i_full[None, :] - gm_full)))**2) * 100
    print(f"  {mname}: {contrib_pct:.2f}% of model×item interaction")

# ============================================================
# Task 5: Save complete results
# ============================================================
print("\n" + "=" * 60)
print("Task 5: Saving results")
print("=" * 60)

output = {
    'dataset': 'A-4',
    'description': '4 models (Llama-3.1-8B, Gemma-2-9B, Mistral-7B, Qwen3-8B) x bf16 only, 6 facets',
    'n_observations': int(N),
    'n_levels': {
        'model': n_m, 'temperature': n_t, 'prompt_template': n_p,
        'seed': n_s, 'ordering': n_o, 'item_id': n_i
    },
    'facets': facets,
    'grand_mean': float(grand_mean),
    'total_variance': float(total_var),
    'model_accuracies': {k: float(v) for k, v in model_acc.items()},
    'variance_components_ems': {
        k: {
            'estimate': float(s2_full[k]),
            'pct': float(vpct_full[k]),
            'ci_95_lower': float(ci_results[k]['ci_lo']) if k in ci_results else None,
            'ci_95_upper': float(ci_results[k]['ci_hi']) if k in ci_results else None,
            'ci_95_lower_pct': float(ci_results[k]['ci_lo']) if k in ci_results else None,
            'ci_95_upper_pct': float(ci_results[k]['ci_hi']) if k in ci_results else None,
        }
        for k in s2_full
    },
    'g_item': {
        'g': float(g_item_full),
        'ci_95': [float(np.percentile(g_vals, 2.5)), float(np.percentile(g_vals, 97.5))],
        'sigma_tau': float(s2_full['item_id']),
        'sigma_delta': float(s2_full['model:item_id'] / n_m +
                            s2_full['temperature:item_id'] / n_t +
                            s2_full['prompt_template:item_id'] / n_p +
                            s2_full['seed:item_id'] / n_s +
                            s2_full['ordering:item_id'] / n_o +
                            s2_full['residual'] / (n_m * n_t * n_p * n_s * n_o)),
    },
    'd_study_model_sweep': d_study,
    'bootstrap': {
        'n_resamples': n_boot,
        'seed': 42,
        'method': 'item cluster resampling (numpy 6D array)'
    },
    'anova_table': {k: {'ss': float(v['ss']), 'df': int(v['df']), 'ms': float(v['ms'])} for k, v in anova.items()},
    'comparison_3model': {
        'note': '3-model values from dataset_a_gstudy.json',
        'item_id_pct_3m': 42.80,
        'model_item_pct_3m': 31.68,
        'g_item_3m': 0.7766,
    }
}

with open('results/analysis/dataset_a4_gstudy.json', 'w') as f:
    json.dump(output, f, indent=2, default=str)
print(f"Results saved to results/analysis/dataset_a4_gstudy.json")

print("\n" + "=" * 60)
print("DONE")
print("=" * 60)
