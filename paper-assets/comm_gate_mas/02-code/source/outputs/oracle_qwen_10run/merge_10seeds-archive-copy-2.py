"""Merge 10-seed Qwen oracle results and compute TOST equivalence statistics."""
import json, sys, os
import numpy as np
from scipy import stats

BASE = os.path.dirname(os.path.abspath(__file__))
SEEDS = [42, 123, 456, 789, 1024, 2048, 3072, 4096, 5120, 6144]

deltas, baselines, pruned_accs, suppression_rates = [], [], [], []
per_seed = []

for s in SEEDS:
    path = os.path.join(BASE, f'seed_{s}.json')
    if not os.path.exists(path):
        print(f'MISSING: seed_{s}.json — aborting')
        sys.exit(1)
    with open(path) as f:
        d = json.load(f)
    bl = d['baseline']['accuracy'] * 100
    pr = d['oracle_pruned']['accuracy'] * 100
    delta = d['delta_pp']
    sr = d['oracle_pruned']['suppression_rate']
    deltas.append(delta)
    baselines.append(bl)
    pruned_accs.append(pr)
    suppression_rates.append(sr)
    per_seed.append({
        'seed': s,
        'baseline_acc': round(bl, 1),
        'pruned_acc': round(pr, 1),
        'delta_pp': delta,
        'suppression_rate': round(sr, 1),
        'num_tasks': d['num_tasks'],
        'num_skipped': d.get('num_skipped', 0),
    })
    print(f'  seed {s:5d}: baseline={bl:.1f}%, pruned={pr:.1f}%, '
          f'Δ={delta:+.1f}pp, suppress={sr:.1f}%')

deltas = np.array(deltas)
n = len(deltas)
mean_d = np.mean(deltas)
sd_d = np.std(deltas, ddof=1)
se_d = sd_d / np.sqrt(n)

print(f'\n{"="*60}')
print(f'10-SEED QWEN ORACLE AGGREGATE')
print(f'{"="*60}')
print(f'  N seeds        = {n}')
print(f'  Mean baseline  = {np.mean(baselines):.1f}%')
print(f'  Mean pruned    = {np.mean(pruned_accs):.1f}%')
print(f'  Mean Δ         = {mean_d:+.2f} pp')
print(f'  SD(Δ)          = {sd_d:.2f} pp')
print(f'  SE(Δ)          = {se_d:.4f} pp')
t_crit = stats.t.ppf(0.975, df=n-1)
print(f'  95% CI         = [{mean_d - t_crit*se_d:+.2f}, {mean_d + t_crit*se_d:+.2f}]  (t-based, df={n-1})')
print(f'  Mean suppress  = {np.mean(suppression_rates):.1f}%')

print(f'\nTOST Equivalence Tests:')
for margin in [1.0, 1.5, 3.0]:
    t_upper = (mean_d - margin) / se_d
    t_lower = (mean_d + margin) / se_d
    p_upper = stats.t.cdf(t_upper, df=n-1)
    p_lower = 1 - stats.t.cdf(t_lower, df=n-1)
    p_tost = max(p_upper, p_lower)
    sig = '✓ EQUIVALENT' if p_tost < 0.05 else '✗ not sig.'
    print(f'  ±{margin}pp: p = {p_tost:.6f}  {sig}')

t_ni = (mean_d - (-3.0)) / se_d
p_ni = 1 - stats.t.cdf(t_ni, df=n-1)
print(f'\nNon-inferiority (δ=-3pp): t = {t_ni:.2f}, p = {p_ni:.8f}  '
      f'{"✓ NON-INFERIOR" if p_ni < 0.05 else "✗ not sig."}')

aggregate = {
    'model': 'Qwen2.5-7B-Instruct',
    'dataset': 'GSM8K',
    'detection': 'oracle_5class',
    'n_seeds': n,
    'tasks_per_seed': 200,
    'mean_delta_pp': round(mean_d, 2),
    'sd_delta_pp': round(sd_d, 2),
    'se_delta_pp': round(se_d, 4),
    'ci_95': [round(mean_d - stats.t.ppf(0.975, df=n-1)*se_d, 2), round(mean_d + stats.t.ppf(0.975, df=n-1)*se_d, 2)],
    'mean_baseline_acc': round(np.mean(baselines), 1),
    'mean_pruned_acc': round(np.mean(pruned_accs), 1),
    'mean_suppression_rate': round(np.mean(suppression_rates), 1),
    'tost_1pp': round(float(max(
        stats.t.cdf((mean_d - 1.0)/se_d, df=n-1),
        1 - stats.t.cdf((mean_d + 1.0)/se_d, df=n-1)
    )), 6),
    'tost_1_5pp': round(float(max(
        stats.t.cdf((mean_d - 1.5)/se_d, df=n-1),
        1 - stats.t.cdf((mean_d + 1.5)/se_d, df=n-1)
    )), 6),
    'tost_3pp': round(float(max(
        stats.t.cdf((mean_d - 3.0)/se_d, df=n-1),
        1 - stats.t.cdf((mean_d + 3.0)/se_d, df=n-1)
    )), 6),
    'non_inferiority_3pp_p': round(float(p_ni), 8),
    'per_seed': per_seed,
}

out_path = os.path.join(BASE, 'aggregate_10seed.json')
with open(out_path, 'w') as f:
    json.dump(aggregate, f, indent=2)
print(f'\nSaved: {out_path}')
