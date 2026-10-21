import json
import numpy as np

def load_results(path):
    results = []
    with open(path) as f:
        for line in f:
            results.append(json.loads(line))
    return results

def extreme_batch_analysis(results, n_extreme, n_bootstrap=1000):
    bcs = np.array([r['bcs'] for r in results])
    acc = np.array([r['accuracy'] for r in results])
    sort_idx = np.argsort(bcs)
    low_idx = sort_idx[:n_extreme]
    high_idx = sort_idx[-n_extreme:]
    
    delta = acc[low_idx].mean() - acc[high_idx].mean()
    
    np.random.seed(42)
    deltas = []
    for _ in range(n_bootstrap):
        boot_low = np.random.choice(acc[low_idx], size=n_extreme, replace=True)
        boot_high = np.random.choice(acc[high_idx], size=n_extreme, replace=True)
        deltas.append(boot_low.mean() - boot_high.mean())
    
    ci_lower = np.percentile(deltas, 2.5)
    ci_upper = np.percentile(deltas, 97.5)
    
    return {
        'n_extreme': n_extreme,
        'n_total': len(results),
        'delta_pp': round(delta * 100, 2),
        'ci_95_lower_pp': round(ci_lower * 100, 2),
        'ci_95_upper_pp': round(ci_upper * 100, 2),
        'low_bcs_batches': {
            'indices': low_idx.tolist(),
            'bcs_values': [round(float(bcs[i]), 4) for i in low_idx],
            'acc_values': [round(float(acc[i]), 4) for i in low_idx],
            'mean_bcs': round(float(bcs[low_idx].mean()), 4),
            'mean_acc': round(float(acc[low_idx].mean()), 4),
        },
        'high_bcs_batches': {
            'indices': high_idx.tolist(),
            'bcs_values': [round(float(bcs[i]), 4) for i in high_idx],
            'acc_values': [round(float(acc[i]), 4) for i in high_idx],
            'mean_bcs': round(float(bcs[high_idx].mean()), 4),
            'mean_acc': round(float(acc[high_idx].mean()), 4),
        },
    }

paths = {
    '16rel_independent': 'artifacts/fewrel_16rel_bootstrap/results_incremental.jsonl',
    '80pool_16sub': 'artifacts/fewrel_80pool_16sub/results_incremental.jsonl',
}

all_results = {}
for name, path in paths.items():
    results = load_results(path)
    print(f"\n{'='*60}")
    print(f"{name}: {len(results)} batches")
    print(f"{'='*60}")
    
    for n_ext in [1, 3, 5, 10]:
        r = extreme_batch_analysis(results, n_ext)
        print(f"\n  n_extreme={n_ext}:")
        print(f"    Δ(low_BCS - high_BCS) = {r['delta_pp']:+.2f} pp  CI [{r['ci_95_lower_pp']:.2f}, {r['ci_95_upper_pp']:.2f}]")
        print(f"    Low BCS group:  mean_bcs={r['low_bcs_batches']['mean_bcs']:.4f}, mean_acc={r['low_bcs_batches']['mean_acc']:.4f}")
        print(f"    High BCS group: mean_bcs={r['high_bcs_batches']['mean_bcs']:.4f}, mean_acc={r['high_bcs_batches']['mean_acc']:.4f}")
        all_results[f"{name}_n{n_ext}"] = r

output_path = 'artifacts/extreme_batch_analysis.json'
with open(output_path, 'w') as f:
    json.dump(all_results, f, indent=2)
print(f"\nResults saved to {output_path}")
