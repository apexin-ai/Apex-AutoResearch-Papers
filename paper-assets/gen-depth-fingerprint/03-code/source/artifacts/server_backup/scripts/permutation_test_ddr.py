import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from scipy import stats

df = pd.read_csv('/root/gen-depth-fingerprint/data/features_8gen.csv')

FEATURES = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max',
            'tail_decay', 'ttr', 'hapax_ratio']

# 3/1/3 partition
TRUE_PARTITION = {
    'entropy_mean': 0, 'ttr': 0, 'hapax_ratio': 0,       # drifting
    'entropy_std': 1,                                       # intermediate
    'entropy_min': 2, 'entropy_max': 2, 'tail_decay': 2    # near-stationary
}

def compute_feature_metrics(df):
    metrics = {}
    for feat in FEATURES:
        rho, _ = stats.spearmanr(df['depth'], df[feat])
        gen1 = df[df['depth'] == 1][feat]
        gen2plus = df[df['depth'] >= 2][feat]
        pooled_std = np.sqrt((gen1.std()**2 + gen2plus.std()**2) / 2)
        d = abs(gen1.mean() - gen2plus.mean()) / pooled_std if pooled_std > 0 else 0
        metrics[feat] = {'abs_rho': abs(rho), 'd': d}
    return metrics

metrics = compute_feature_metrics(df)

print("=== Feature Metrics ===")
for f in FEATURES:
    print(f"  {f:15s}  |rho|={metrics[f]['abs_rho']:.4f}  d={metrics[f]['d']:.4f}")

feature_names = list(TRUE_PARTITION.keys())
X = np.array([[metrics[f]['abs_rho'], metrics[f]['d']] for f in feature_names])
X_scaled = StandardScaler().fit_transform(X)

# k=2: drifting vs non-drifting
true_labels_k2 = np.array([0 if TRUE_PARTITION[f] == 0 else 1 for f in feature_names])
true_silhouette = silhouette_score(X_scaled, true_labels_k2)
print(f"\nTrue k=2 silhouette: {true_silhouette:.4f}")
print(f"Labels: {dict(zip(feature_names, true_labels_k2))}")

# Permutation test
np.random.seed(42)
n_perm = 10000
perm_silhouettes = []
for _ in range(n_perm):
    perm_labels = np.random.permutation(true_labels_k2)
    if len(set(perm_labels)) < 2:
        continue
    s = silhouette_score(X_scaled, perm_labels)
    perm_silhouettes.append(s)

perm_silhouettes = np.array(perm_silhouettes)
p_value = (perm_silhouettes >= true_silhouette).mean()

print(f"\n=== Permutation Test Results ===")
print(f"N permutations (valid): {len(perm_silhouettes)}")
print(f"Permutation p-value: {p_value:.6f}")
print(f"Null distribution: mean={perm_silhouettes.mean():.4f}, std={perm_silhouettes.std():.4f}")
z_score = (true_silhouette - perm_silhouettes.mean()) / perm_silhouettes.std()
print(f"True silhouette is {z_score:.1f} SDs above null mean")
print(f"\nConclusion: {'SIGNIFICANT' if p_value < 0.05 else 'NOT SIGNIFICANT'} at alpha=0.05")
