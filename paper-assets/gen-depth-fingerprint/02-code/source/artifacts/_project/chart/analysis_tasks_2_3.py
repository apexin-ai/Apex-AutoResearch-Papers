"""Tasks 2+3: Data-driven clustering + TOST epsilon sensitivity."""
import json
import numpy as np
from scipy import stats
from pathlib import Path

ARTIFACTS = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project')

# ── Task 2: k-means clustering on pooled (|ρ|, d) ──
features = {
    'hapax_ratio':  (0.64, 0.76),
    'ttr':          (0.63, 0.88),
    'entropy_mean': (0.60, 1.17),
    'entropy_std':  (0.16, 0.55),
    'entropy_min':  (0.40, 0.03),
    'entropy_max':  (0.05, 0.08),
    'tail_decay':   (0.04, 0.08),
}

X = np.array(list(features.values()))
names = list(features.keys())

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

X_scaled = StandardScaler().fit_transform(X)

print("=" * 60)
print("TASK 2: Data-Driven Clustering (k-means)")
print("=" * 60)
print(f"\nInput: 7 features in (|ρ|, d) space")
print(f"Features: {names}\n")

results_t2 = {}
for k in [2, 3, 4, 5]:
    if k >= len(X):
        print(f"k={k}: skipped (k >= n_samples={len(X)})")
        continue
    km = KMeans(n_clusters=k, random_state=42, n_init=20)
    labels = km.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, labels) if k < len(X) else None
    results_t2[k] = {'labels': labels.tolist(), 'silhouette': round(sil, 4)}

    clusters = {}
    for i, name in enumerate(names):
        c = int(labels[i])
        clusters.setdefault(c, []).append(name)

    print(f"k={k}: silhouette={sil:.4f}")
    for c in sorted(clusters):
        print(f"  Cluster {c}: {clusters[c]}")
    print()

best_k = max(results_t2, key=lambda k: results_t2[k]['silhouette'])
print(f"Best k by silhouette: k={best_k} (score={results_t2[best_k]['silhouette']:.4f})")
print()

# ── Task 3: TOST ε sensitivity ──
print("=" * 60)
print("TASK 3: TOST Epsilon Sensitivity")
print("=" * 60)

with open(ARTIFACTS / 'rebuttal' / 'tost_per_generator.json') as f:
    tost_data = json.load(f)

near_stationary = ['entropy_min', 'entropy_max', 'tail_decay']
intermediate = ['entropy_std']
drifting = ['entropy_mean', 'ttr', 'hapax_ratio']
all_features = drifting + intermediate + near_stationary
epsilons = [0.15, 0.20, 0.25]
generators = list(tost_data['per_generator'].keys())

def compute_tost_pvalue(d_obs, n1, n2, epsilon):
    df = n1 + n2 - 2
    se = np.sqrt((n1 + n2) / (n1 * n2) + d_obs**2 / (2 * (n1 + n2 - 2)))
    t_lower = (d_obs + epsilon) / se
    t_upper = (d_obs - epsilon) / se
    p_lower = 1 - stats.t.cdf(t_lower, df)
    p_upper = stats.t.cdf(t_upper, df)
    return max(p_lower, p_upper)

print(f"\nGenerators: {generators}")
print(f"Features tested: {all_features}")
print(f"Epsilon values: {epsilons}\n")

results_t3 = {}
for feat in all_features:
    results_t3[feat] = {}
    for eps in epsilons:
        pass_count = 0
        total = 0
        for gen in generators:
            gen_data = tost_data['per_generator'][gen]
            n1 = gen_data['n_gen1']
            n2 = gen_data['n_gen2p']
            d_obs = gen_data['features'][feat]['observed_d']
            p = compute_tost_pvalue(d_obs, n1, n2, eps)
            equiv = p < 0.05
            if equiv:
                pass_count += 1
            total += 1
        results_t3[feat][eps] = {'pass': pass_count, 'total': total, 'rate': f"{pass_count}/{total}"}

# Verify against known ε=0.20 results
print("Verification against known ε=0.20 results:")
for gen in generators:
    gen_data = tost_data['per_generator'][gen]
    for feat in ['entropy_min']:
        known_p = gen_data['features'][feat]['p_tost']
        computed_p = compute_tost_pvalue(
            gen_data['features'][feat]['observed_d'],
            gen_data['n_gen1'], gen_data['n_gen2p'], 0.20
        )
        print(f"  {gen}/{feat}: known={known_p:.2e}, computed={computed_p:.2e}")
print()

print(f"{'Feature':<16} {'ε=0.15':>8} {'ε=0.20':>8} {'ε=0.25':>8}  Zone")
print("-" * 60)
for feat in all_features:
    zone = 'drifting' if feat in drifting else ('intermediate' if feat in intermediate else 'near-stat')
    row = f"{feat:<16}"
    for eps in epsilons:
        row += f" {results_t3[feat][eps]['rate']:>8}"
    row += f"  {zone}"
    print(row)

# Save results
output = {
    'task2_clustering': results_t2,
    'task2_best_k': best_k,
    'task3_tost_sensitivity': results_t3,
}
out_path = ARTIFACTS / 'rebuttal' / 'tasks_2_3_results.json'
with open(out_path, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nResults saved to {out_path}")
