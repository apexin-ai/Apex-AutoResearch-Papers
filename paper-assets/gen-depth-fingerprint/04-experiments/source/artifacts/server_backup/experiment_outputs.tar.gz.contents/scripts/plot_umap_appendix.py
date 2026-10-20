import numpy as np
import pandas as pd
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import umap

df = pd.read_csv('/root/gen-depth-fingerprint/data/features_8gen.csv')

feat_cols = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max',
             'tail_decay', 'ttr', 'hapax_ratio']

rng = np.random.RandomState(42)
n_per_depth = 1500
samples = []
for d in range(5):
    sub = df[df['depth'] == d]
    samples.append(sub.sample(n=min(n_per_depth, len(sub)), random_state=rng))
df_sample = pd.concat(samples, ignore_index=True)

X_scaled = StandardScaler().fit_transform(df_sample[feat_cols].values)
embedding = umap.UMAP(n_neighbors=30, min_dist=0.3, random_state=42).fit_transform(X_scaled)

depths = df_sample['depth'].values

def to_3class(d):
    if d == 0: return 'gen-0 (human)'
    elif d == 1: return 'gen-1'
    else: return 'gen-2+'
class_labels = np.array([to_3class(d) for d in depths])

# depth 0 lightest → depth 4 darkest: reverse plasma
depth_cmap = plt.cm.plasma_r
depth_colors = [depth_cmap(i / 5.5 + 0.05) for i in range(5)]

class_colors = {
    'gen-0 (human)': '#4C72B0',
    'gen-1': '#DD8452',
    'gen-2+': '#55A868',
}

scatter_kw = dict(s=8, alpha=0.55, edgecolors='none', linewidths=0, rasterized=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))

for d in range(5):
    mask = depths == d
    ax1.scatter(embedding[mask, 0], embedding[mask, 1],
                c=[depth_colors[d]], label=f'Depth {d}', **scatter_kw)
ax1.set_title('(a) UMAP by Generation Depth', fontsize=11, fontweight='bold')
ax1.set_xlabel('UMAP-1')
ax1.set_ylabel('UMAP-2')
ax1.legend(markerscale=2.5, fontsize=8, framealpha=0.8)

for cls_name, color in class_colors.items():
    mask = class_labels == cls_name
    ax2.scatter(embedding[mask, 0], embedding[mask, 1],
                c=[color], label=cls_name, **scatter_kw)
ax2.set_title('(b) UMAP by 3-Class Label', fontsize=11, fontweight='bold')
ax2.set_xlabel('UMAP-1')
ax2.set_ylabel('UMAP-2')
ax2.legend(markerscale=2.5, fontsize=8, framealpha=0.8)

plt.tight_layout()
out = '/root/gen-depth-fingerprint/chart/fig_appendix_umap.pdf'
fig.savefig(out, dpi=300, bbox_inches='tight')
fig.savefig(out.replace('.pdf', '.png'), dpi=200, bbox_inches='tight')
print(f"Saved: {out}")
