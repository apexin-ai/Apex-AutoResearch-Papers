import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from scipy import stats

df = pd.read_csv('/root/gen-depth-fingerprint/data/features_8gen.csv')

FEATURES = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max',
            'tail_decay', 'ttr', 'hapax_ratio']

# Compute per-feature (|rho|, d) in the pooled dataset
def compute_feature_metrics(df):
    metrics = {}
    for feat in FEATURES:
        rho, _ = stats.spearmanr(df['depth'], df[feat])
        gen0 = df[df['depth'] == 0][feat].dropna()
        gen1plus = df[df['depth'] >= 1][feat].dropna()
        pooled_std = np.sqrt((gen0.std()**2 + gen1plus.std()**2) / 2)
        d = abs(gen0.mean() - gen1plus.mean()) / pooled_std if pooled_std > 0 else 0
        metrics[feat] = {'abs_rho': abs(rho), 'd': d}
    return metrics

metrics = compute_feature_metrics(df)

print("=== Per-feature metrics (|rho|, d) ===")
for f in FEATURES:
    print(f"  {f:15s}  |rho|={metrics[f]['abs_rho']:.4f}  d={metrics[f]['d']:.4f}")

X = np.array([[metrics[f]['abs_rho'], metrics[f]['d']] for f in FEATURES])
X_scaled = StandardScaler().fit_transform(X)

# Feature order: entropy_mean(0), entropy_std(1), entropy_min(2), entropy_max(3),
#                tail_decay(4), ttr(5), hapax_ratio(6)

# 3/1/3 partition (original):
#   drifting(0): entropy_mean, ttr, hapax_ratio
#   intermediate(1): entropy_std
#   near-stationary(2): entropy_min, entropy_max, tail_decay
labels_313 = np.array([0, 1, 2, 2, 2, 0, 0])

# 3/2/2 partition (tail_decay -> intermediate):
#   drifting(0): entropy_mean, ttr, hapax_ratio
#   intermediate(1): entropy_std, tail_decay
#   near-stationary(2): entropy_min, entropy_max
labels_322 = np.array([0, 1, 2, 2, 1, 0, 0])

# k=2 binary (drifting vs non-drifting) — same under both partitions
labels_k2 = np.array([0, 1, 1, 1, 1, 0, 0])

sil_313 = silhouette_score(X_scaled, labels_313)
sil_322 = silhouette_score(X_scaled, labels_322)
sil_k2 = silhouette_score(X_scaled, labels_k2)

# Per-sample silhouette for diagnostics
from sklearn.metrics import silhouette_samples
sil_samples_313 = silhouette_samples(X_scaled, labels_313)
sil_samples_322 = silhouette_samples(X_scaled, labels_322)

print("\n=== DDR Partition Ablation ===")
print(f"3/1/3 (original)  silhouette (k=3): {sil_313:.4f}")
print(f"3/2/2 (alt)        silhouette (k=3): {sil_322:.4f}")
print(f"k=2 binary         silhouette:       {sil_k2:.4f}")
print(f"Delta silhouette (3/2/2 - 3/1/3):   {sil_322 - sil_313:+.4f}")

print("\n=== Per-feature silhouette scores ===")
print(f"{'Feature':15s}  {'3/1/3':>8s}  {'3/2/2':>8s}  {'delta':>8s}  {'label 3/1/3':>12s}  {'label 3/2/2':>12s}")
group_names = {0: 'drifting', 1: 'intermediate', 2: 'near-stat'}
for i, f in enumerate(FEATURES):
    s313 = sil_samples_313[i]
    s322 = sil_samples_322[i]
    l313 = group_names[labels_313[i]]
    l322 = group_names[labels_322[i]]
    print(f"  {f:15s}  {s313:+.4f}    {s322:+.4f}    {s322-s313:+.4f}    {l313:>12s}    {l322:>12s}")

print("\n=== Interpretation ===")
if sil_313 > sil_322:
    print(f"Original 3/1/3 partition has HIGHER silhouette (+{sil_313-sil_322:.4f}), confirming the chosen partition.")
elif sil_322 > sil_313:
    print(f"Alternative 3/2/2 partition has HIGHER silhouette (+{sil_322-sil_313:.4f}), suggesting tail_decay fits intermediate better.")
else:
    print("Both partitions have identical silhouette scores.")

print("\nNote: Classification (LOGO F1) uses all 7 features regardless of partition;")
print("the ablation tests partition interpretability, not classification performance.")
