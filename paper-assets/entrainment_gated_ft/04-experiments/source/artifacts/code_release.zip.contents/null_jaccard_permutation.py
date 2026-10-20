import json
import os
import numpy as np
from itertools import combinations

DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'
N_PERM = 10000
SEED = 42
ARCHS = ['GDN', 'HGRN2', 'RetNet']

def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

def load_json_samples(path, task='lambada_openai'):
    with open(path) as f:
        return json.load(f)['samples'][task]

# Load data (same sources as lambada_three_arch_comparison.py)
print("Loading data...")
model_data = {}
model_data['GDN-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')),
    key=lambda x: x['doc_id'])
model_data['GDN-h3-1'] = sorted(
    load_jsonl(os.path.join(DATA_DIR, '1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl')),
    key=lambda x: x['doc_id'])
model_data['HGRN2-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-pure.json')),
    key=lambda x: x['doc_id'])
model_data['HGRN2-h3-1'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-HGRN2-hybrid-3-1.json')),
    key=lambda x: x['doc_id'])
model_data['RetNet-pure'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-pure.json')),
    key=lambda x: x['doc_id'])
model_data['RetNet-h3-1'] = sorted(
    load_json_samples(os.path.join(DATA_DIR, '1.3B-100B-RetNet-hybrid-3-1.json')),
    key=lambda x: x['doc_id'])

N = len(model_data['GDN-pure'])
print(f"N = {N}")

acc = {name: np.array([s['acc'] for s in samples]) for name, samples in model_data.items()}

# Compute observed helped/hurt sets
stats = {}
for arch in ARCHS:
    pure = acc[f'{arch}-pure']
    hybrid = acc[f'{arch}-h3-1']
    helped_mask = (pure == 0) & (hybrid == 1)
    hurt_mask = (pure == 1) & (hybrid == 0)
    stats[arch] = {
        'helped_set': set(np.where(helped_mask)[0]),
        'hurt_set': set(np.where(hurt_mask)[0]),
        'helped_size': int(helped_mask.sum()),
        'hurt_size': int(hurt_mask.sum()),
    }
    print(f"  {arch}: helped={stats[arch]['helped_size']}, hurt={stats[arch]['hurt_size']}")

def jaccard(a, b):
    if len(a) == 0 and len(b) == 0:
        return 0.0
    return len(a & b) / len(a | b)

# Observed pairwise Jaccard
pairs = list(combinations(ARCHS, 2))
print("\nObserved pairwise Jaccard:")
obs = {'helped': {}, 'hurt': {}}
for a1, a2 in pairs:
    key = f"{a1}_vs_{a2}"
    for cat in ['helped', 'hurt']:
        j = jaccard(stats[a1][f'{cat}_set'], stats[a2][f'{cat}_set'])
        obs[cat][key] = j
    print(f"  {key}: helped={obs['helped'][key]:.4f}, hurt={obs['hurt'][key]:.4f}")

# Permutation test
print(f"\nRunning permutation test ({N_PERM} iterations)...")
rng = np.random.default_rng(SEED)
indices = np.arange(N)

null_jaccards = {cat: {f"{a1}_vs_{a2}": [] for a1, a2 in pairs} for cat in ['helped', 'hurt']}

for i in range(N_PERM):
    if (i + 1) % 2000 == 0:
        print(f"  iteration {i+1}/{N_PERM}")
    for cat in ['helped', 'hurt']:
        shuffled_sets = {}
        for arch in ARCHS:
            size = stats[arch][f'{cat}_size']
            shuffled_sets[arch] = set(rng.choice(indices, size=size, replace=False))
        for a1, a2 in pairs:
            key = f"{a1}_vs_{a2}"
            j = jaccard(shuffled_sets[a1], shuffled_sets[a2])
            null_jaccards[cat][key].append(j)

# Compute results
results = {'helped': {}, 'hurt': {}}
print("\n" + "=" * 80)
print("RESULTS: Null Jaccard Permutation Test (1.3B h3-1, 10000 permutations)")
print("=" * 80)

for cat in ['helped', 'hurt']:
    print(f"\n--- {cat.upper()} ---")
    print(f"{'Pair':<20} {'J_obs':>8} {'J_null_mean':>12} {'J_null_std':>11} {'z_score':>8} {'p_value':>10}")
    print("-" * 70)
    for a1, a2 in pairs:
        key = f"{a1}_vs_{a2}"
        null_arr = np.array(null_jaccards[cat][key])
        j_obs = obs[cat][key]
        j_null_mean = null_arr.mean()
        j_null_std = null_arr.std()
        p_value = (np.sum(null_arr >= j_obs) + 1) / (N_PERM + 1)
        z_score = (j_obs - j_null_mean) / j_null_std if j_null_std > 0 else float('inf')
        results[cat][key] = {
            'J_obs': round(j_obs, 6),
            'J_null_mean': round(j_null_mean, 6),
            'J_null_std': round(j_null_std, 6),
            'z_score': round(z_score, 2),
            'p_value': round(p_value, 6),
        }
        print(f"{key:<20} {j_obs:>8.4f} {j_null_mean:>12.4f} {j_null_std:>11.4f} {z_score:>8.2f} {p_value:>10.6f}")

# Overall null means
for cat in ['helped', 'hurt']:
    all_null_means = [results[cat][k]['J_null_mean'] for k in results[cat]]
    results[f'overall_null_mean_{cat}'] = round(np.mean(all_null_means), 6)

# Set sizes for reference
results['set_sizes'] = {arch: {'helped': stats[arch]['helped_size'], 'hurt': stats[arch]['hurt_size']} for arch in ARCHS}
results['N'] = N
results['n_permutations'] = N_PERM
results['seed'] = SEED

print(f"\nOverall null mean (helped): {results['overall_null_mean_helped']:.4f}")
print(f"Overall null mean (hurt):   {results['overall_null_mean_hurt']:.4f}")

# Save
out_path = '/root/entrainment_gated_ft/null_jaccard_results.json'
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {out_path}")
