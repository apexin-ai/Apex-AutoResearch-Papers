"""Token Position Visualization: L2norm vs Random pruning spatial patterns on X-VLA.

Generates Fig 4: shows that L2norm pruning creates spatially clustered holes
in the 7x7 vision token grid (because nearby patches have similar L2 norms),
while random pruning distributes removals uniformly.
"""

import sys, os, json
import numpy as np
import torch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap
from pathlib import Path
from scipy import ndimage
from scipy.spatial.distance import cdist

MODEL_DIR = '/root/autodl-tmp/X-VLA-Libero'
OUTPUT_DIR = '/root/autodl-tmp/importance_margin_vla_compress/artifacts'
KEEP_RATIOS = [0.3, 0.5, 0.7]
N_RANDOM_SEEDS = 5  # average random pruning over multiple seeds


def load_xvla_model(device):
    sys.path.insert(0, MODEL_DIR)
    from configuration_xvla import XVLAConfig
    from modeling_xvla import XVLA
    from safetensors.torch import load_file

    config = XVLAConfig.from_pretrained(MODEL_DIR)
    model = XVLA(config)
    state_dict = load_file(os.path.join(MODEL_DIR, 'model.safetensors'))
    model.load_state_dict(state_dict, strict=False)
    model = model.to(device).eval()
    return model


def create_scene_image(seed=42):
    """Create a synthetic robotic scene with spatial structure."""
    rng = np.random.RandomState(seed)
    img = np.zeros((224, 224, 3), dtype=np.float32)
    # table-like background: brownish bottom, lighter top
    for j in range(224):
        t = j / 224.0
        img[j, :, 0] = 0.35 + 0.25 * t
        img[j, :, 1] = 0.25 + 0.15 * t
        img[j, :, 2] = 0.15 + 0.10 * t
    # add colored blobs as "objects"
    from scipy.ndimage import gaussian_filter
    object_colors = [
        [0.8, 0.2, 0.1],  # red
        [0.1, 0.7, 0.2],  # green
        [0.2, 0.3, 0.9],  # blue
        [0.9, 0.8, 0.1],  # yellow
    ]
    for color in object_colors:
        cx, cy = rng.randint(40, 184, size=2)
        blob = np.zeros((224, 224))
        blob[cy, cx] = 1.0
        blob = gaussian_filter(blob, sigma=15)
        blob = blob / (blob.max() + 1e-8) * 0.6
        for c in range(3):
            img[:, :, c] += blob * color[c]
    img = np.clip(img, 0, 1)
    return img


def get_vision_features(model, img_np, device):
    """Get vision token features from X-VLA."""
    pixel_values = torch.from_numpy(
        img_np.transpose(2, 0, 1)
    ).unsqueeze(0).float().to(device)
    with torch.no_grad():
        features = model.vlm._encode_image(pixel_values)
    return features[0].cpu()  # [N, D]


def compute_spatial_metrics(kept_mask_2d):
    """Compute spatial clustering metrics on a 2D boolean grid."""
    h, w = kept_mask_2d.shape
    n_kept = kept_mask_2d.sum()
    if n_kept == 0:
        return {'entropy': 0, 'n_clusters': 0, 'avg_nn_dist': 0,
                'largest_cluster_frac': 0, 'coverage': 0}

    # Spatial entropy: divide grid into 3x3 blocks
    block_h, block_w = max(1, h // 3), max(1, w // 3)
    block_counts = []
    for bi in range(3):
        for bj in range(3):
            r0, r1 = bi * block_h, min((bi + 1) * block_h, h)
            c0, c1 = bj * block_w, min((bj + 1) * block_w, w)
            block_counts.append(kept_mask_2d[r0:r1, c0:c1].sum())
    total = sum(block_counts)
    if total > 0:
        probs = np.array(block_counts, dtype=float) / total
        probs = probs[probs > 0]
        entropy = -np.sum(probs * np.log2(probs))
    else:
        entropy = 0
    max_entropy = np.log2(len(block_counts))

    # Connected components
    labeled, n_clusters = ndimage.label(kept_mask_2d.astype(int))

    # Average nearest neighbor distance
    kept_pos = np.argwhere(kept_mask_2d)
    if len(kept_pos) > 1:
        dists = cdist(kept_pos, kept_pos)
        np.fill_diagonal(dists, np.inf)
        avg_nn_dist = dists.min(axis=1).mean()
    else:
        avg_nn_dist = 0.0

    # Largest cluster fraction
    if n_clusters > 0:
        sizes = [np.sum(labeled == i) for i in range(1, n_clusters + 1)]
        largest_frac = max(sizes) / n_kept
    else:
        largest_frac = 0.0

    # Coverage: fraction of 3x3 blocks that have at least one kept token
    coverage = np.mean([1.0 if c > 0 else 0.0 for c in block_counts])

    return {
        'entropy': entropy,
        'norm_entropy': entropy / max_entropy if max_entropy > 0 else 0,
        'n_clusters': n_clusters,
        'avg_nn_dist': avg_nn_dist,
        'largest_cluster_frac': largest_frac,
        'coverage': coverage,
    }


def pruning_mask_2d(norms_spatial, k, method, h, w, seed=42):
    """Get 2D boolean mask for kept tokens in the spatial grid.

    norms_spatial: [h*w] L2 norms for spatial tokens only
    Returns: [h, w] boolean mask (True = kept)
    """
    N = len(norms_spatial)
    if method == 'l2_norm':
        indices = np.argsort(norms_spatial)[::-1][:k]
    elif method == 'random':
        rng = np.random.RandomState(seed)
        indices = rng.choice(N, size=k, replace=False)
    mask = np.zeros(N, dtype=bool)
    mask[indices] = True
    return mask.reshape(h, w)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    device = torch.device('cuda:2')

    print("Loading X-VLA model...")
    model = load_xvla_model(device)

    print("Creating scene image...")
    img = create_scene_image()

    print("Extracting vision features...")
    features = get_vision_features(model, img, device)
    N, D = features.shape
    print(f"  Total tokens: {N}, dim: {D}")

    # Token 0 = spatial_avg_pool (global), tokens 1..N-1 = spatial grid
    n_spatial = N - 1
    h = w = int(n_spatial ** 0.5)
    assert h * w == n_spatial, f"Not square grid: {n_spatial}"
    print(f"  Spatial grid: {h}x{w} = {n_spatial} tokens + 1 global")

    # All token norms and spatial-only norms
    all_norms = features.norm(dim=-1).numpy()  # [N]
    spatial_norms = all_norms[1:]  # [h*w]

    print(f"  Norm stats (spatial): mean={spatial_norms.mean():.2f}, "
          f"std={spatial_norms.std():.2f}, CV={spatial_norms.std()/spatial_norms.mean():.4f}")

    # Norm heatmap
    norm_grid = spatial_norms.reshape(h, w)

    # ===== FIGURE 1: Main comparison (3 rows x 2 cols) =====
    fig, axes = plt.subplots(len(KEEP_RATIOS), 2, figsize=(5.5, 7.5),
                             gridspec_kw={'wspace': 0.15, 'hspace': 0.35})

    cmap_kept = ListedColormap(['#FFFFFF', '#2E86AB'])  # white=pruned, blue=kept
    cmap_random = ListedColormap(['#FFFFFF', '#A23B72'])  # white=pruned, purple=kept

    all_metrics = {}

    for ri, k_ratio in enumerate(KEEP_RATIOS):
        k = max(1, int(k_ratio * n_spatial))

        # L2 norm pruning
        mask_l2 = pruning_mask_2d(spatial_norms, k, 'l2_norm', h, w)
        metrics_l2 = compute_spatial_metrics(mask_l2)

        # Random pruning (average over seeds for metrics)
        random_metrics_list = []
        for s in range(N_RANDOM_SEEDS):
            mask_r = pruning_mask_2d(spatial_norms, k, 'random', h, w, seed=42 + s)
            random_metrics_list.append(compute_spatial_metrics(mask_r))
        mask_random = pruning_mask_2d(spatial_norms, k, 'random', h, w, seed=42)
        metrics_random = {
            key: np.mean([m[key] for m in random_metrics_list])
            for key in random_metrics_list[0]
        }

        all_metrics[k_ratio] = {'l2_norm': metrics_l2, 'random': metrics_random}

        # Plot L2 norm
        ax_l2 = axes[ri, 0]
        ax_l2.imshow(mask_l2.astype(float), cmap=cmap_kept, vmin=0, vmax=1,
                     interpolation='nearest', aspect='equal')
        for i in range(h):
            for j in range(w):
                ax_l2.plot(j, i, 's', markersize=14,
                          markerfacecolor='#2E86AB' if mask_l2[i, j] else '#E8E8E8',
                          markeredgecolor='#333333', markeredgewidth=0.5)
        ax_l2.set_xlim(-0.5, w - 0.5)
        ax_l2.set_ylim(h - 0.5, -0.5)
        ax_l2.set_xticks([])
        ax_l2.set_yticks([])
        if ri == 0:
            ax_l2.set_title('L2-Norm Pruning', fontsize=11, fontweight='bold', pad=8)
        ax_l2.set_ylabel(f'k = {k_ratio}', fontsize=11, fontweight='bold',
                         rotation=0, labelpad=30, va='center')
        # Metrics annotation
        ax_l2.text(0.5, -0.12,
                   f'Clusters: {metrics_l2["n_clusters"]}  |  '
                   f'Entropy: {metrics_l2["norm_entropy"]:.2f}  |  '
                   f'NN dist: {metrics_l2["avg_nn_dist"]:.2f}',
                   transform=ax_l2.transAxes, fontsize=6.5, ha='center',
                   color='#555555')

        # Plot Random
        ax_r = axes[ri, 1]
        for i in range(h):
            for j in range(w):
                ax_r.plot(j, i, 's', markersize=14,
                          markerfacecolor='#A23B72' if mask_random[i, j] else '#E8E8E8',
                          markeredgecolor='#333333', markeredgewidth=0.5)
        ax_r.set_xlim(-0.5, w - 0.5)
        ax_r.set_ylim(h - 0.5, -0.5)
        ax_r.set_xticks([])
        ax_r.set_yticks([])
        if ri == 0:
            ax_r.set_title('Random Pruning', fontsize=11, fontweight='bold', pad=8)
        ax_r.text(0.5, -0.12,
                  f'Clusters: {metrics_random["n_clusters"]:.1f}  |  '
                  f'Entropy: {metrics_random["norm_entropy"]:.2f}  |  '
                  f'NN dist: {metrics_random["avg_nn_dist"]:.2f}',
                  transform=ax_r.transAxes, fontsize=6.5, ha='center',
                  color='#555555')

    # Legend
    kept_patch = mpatches.Patch(facecolor='#2E86AB', edgecolor='#333', label='Kept (L2)')
    rand_patch = mpatches.Patch(facecolor='#A23B72', edgecolor='#333', label='Kept (Random)')
    pruned_patch = mpatches.Patch(facecolor='#E8E8E8', edgecolor='#333', label='Pruned')
    fig.legend(handles=[kept_patch, rand_patch, pruned_patch],
               loc='lower center', ncol=3, fontsize=9, frameon=False,
               bbox_to_anchor=(0.5, 0.01))

    fig.suptitle('Vision Token Spatial Patterns: L2-Norm vs Random Pruning\n(X-VLA, 7×7 token grid)',
                 fontsize=12, fontweight='bold', y=0.98)

    out_main = os.path.join(OUTPUT_DIR, 'token_position_viz.pdf')
    fig.savefig(out_main, bbox_inches='tight', dpi=200)
    plt.close(fig)
    print(f"Saved: {out_main}")

    # Also save PNG
    fig2, axes2 = plt.subplots(len(KEEP_RATIOS), 2, figsize=(5.5, 7.5),
                               gridspec_kw={'wspace': 0.15, 'hspace': 0.35})
    for ri, k_ratio in enumerate(KEEP_RATIOS):
        k = max(1, int(k_ratio * n_spatial))
        mask_l2 = pruning_mask_2d(spatial_norms, k, 'l2_norm', h, w)
        mask_random = pruning_mask_2d(spatial_norms, k, 'random', h, w, seed=42)
        metrics_l2 = all_metrics[k_ratio]['l2_norm']
        metrics_random = all_metrics[k_ratio]['random']

        for col, (mask, color, title, metrics) in enumerate([
            (mask_l2, '#2E86AB', 'L2-Norm Pruning', metrics_l2),
            (mask_random, '#A23B72', 'Random Pruning', metrics_random),
        ]):
            ax = axes2[ri, col]
            for i in range(h):
                for j in range(w):
                    ax.plot(j, i, 's', markersize=14,
                            markerfacecolor=color if mask[i, j] else '#E8E8E8',
                            markeredgecolor='#333333', markeredgewidth=0.5)
            ax.set_xlim(-0.5, w - 0.5)
            ax.set_ylim(h - 0.5, -0.5)
            ax.set_xticks([])
            ax.set_yticks([])
            if ri == 0:
                ax.set_title(title, fontsize=11, fontweight='bold', pad=8)
            if col == 0:
                ax.set_ylabel(f'k = {k_ratio}', fontsize=11, fontweight='bold',
                              rotation=0, labelpad=30, va='center')
            ent = metrics['norm_entropy'] if isinstance(metrics['norm_entropy'], float) else metrics['norm_entropy']
            nc = metrics['n_clusters'] if isinstance(metrics['n_clusters'], (int, np.integer)) else metrics['n_clusters']
            nn = metrics['avg_nn_dist'] if isinstance(metrics['avg_nn_dist'], float) else metrics['avg_nn_dist']
            ax.text(0.5, -0.12,
                    f'Clusters: {nc:.0f}  |  Entropy: {ent:.2f}  |  NN dist: {nn:.2f}',
                    transform=ax.transAxes, fontsize=6.5, ha='center', color='#555555')

    fig2.legend(handles=[kept_patch, rand_patch, pruned_patch],
                loc='lower center', ncol=3, fontsize=9, frameon=False,
                bbox_to_anchor=(0.5, 0.01))
    fig2.suptitle('Vision Token Spatial Patterns: L2-Norm vs Random Pruning\n(X-VLA, 7×7 token grid)',
                  fontsize=12, fontweight='bold', y=0.98)
    out_png = os.path.join(OUTPUT_DIR, 'token_position_viz.png')
    fig2.savefig(out_png, bbox_inches='tight', dpi=200)
    plt.close(fig2)
    print(f"Saved: {out_png}")

    # ===== FIGURE 2: L2 norm heatmap =====
    fig3, axes3 = plt.subplots(1, 2, figsize=(7, 3.2), gridspec_kw={'wspace': 0.3})

    ax = axes3[0]
    im = ax.imshow(norm_grid, cmap='YlOrRd', interpolation='nearest', aspect='equal')
    ax.set_title('L2 Norm Heatmap (7×7)', fontsize=10, fontweight='bold')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.colorbar(im, ax=ax, shrink=0.8, label='L2 Norm')

    ax2 = axes3[1]
    ax2.hist(spatial_norms, bins=20, color='#2E86AB', alpha=0.8, edgecolor='white')
    ax2.axvline(spatial_norms.mean(), color='red', linestyle='--', linewidth=1.5,
                label=f'Mean={spatial_norms.mean():.1f}')
    ax2.set_title('L2 Norm Distribution', fontsize=10, fontweight='bold')
    ax2.set_xlabel('L2 Norm')
    ax2.set_ylabel('Count')
    ax2.legend(fontsize=8)
    cv = spatial_norms.std() / spatial_norms.mean()
    ax2.text(0.95, 0.95, f'CV = {cv:.4f}', transform=ax2.transAxes,
             fontsize=9, ha='right', va='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

    out_heatmap = os.path.join(OUTPUT_DIR, 'token_norm_heatmap.pdf')
    fig3.savefig(out_heatmap, bbox_inches='tight', dpi=200)
    plt.close(fig3)
    print(f"Saved: {out_heatmap}")

    # ===== Print metrics summary =====
    print("\n" + "=" * 70)
    print("SPATIAL CLUSTERING METRICS SUMMARY")
    print("=" * 70)
    print(f"{'k':>5} | {'Method':>10} | {'Clusters':>8} | {'Entropy':>8} | "
          f"{'NormEnt':>8} | {'AvgNN':>8} | {'LrgClust':>8} | {'Coverage':>8}")
    print("-" * 70)
    for k_ratio in KEEP_RATIOS:
        for method in ['l2_norm', 'random']:
            m = all_metrics[k_ratio][method]
            print(f"{k_ratio:>5.1f} | {method:>10} | {m['n_clusters']:>8.1f} | "
                  f"{m['entropy']:>8.2f} | {m['norm_entropy']:>8.2f} | "
                  f"{m['avg_nn_dist']:>8.2f} | {m['largest_cluster_frac']:>8.2f} | "
                  f"{m['coverage']:>8.2f}")
    print("=" * 70)

    print(f"\nNorm CV = {cv:.4f} (low CV → similar norms → L2 pruning spatial clustering)")

    # Save metrics as JSON
    metrics_out = {
        'model': 'X-VLA',
        'grid_size': f'{h}x{w}',
        'n_total_tokens': int(N),
        'n_spatial_tokens': int(n_spatial),
        'norm_mean': float(spatial_norms.mean()),
        'norm_std': float(spatial_norms.std()),
        'norm_cv': float(cv),
        'metrics': {}
    }
    for k_ratio in KEEP_RATIOS:
        metrics_out['metrics'][str(k_ratio)] = {
            method: {k: float(v) for k, v in all_metrics[k_ratio][method].items()}
            for method in ['l2_norm', 'random']
        }

    metrics_path = os.path.join(OUTPUT_DIR, 'token_position_metrics.json')
    with open(metrics_path, 'w') as f:
        json.dump(metrics_out, f, indent=2)
    print(f"\nMetrics saved: {metrics_path}")

    # Cleanup
    del model
    torch.cuda.empty_cache()
    print("Done.")


if __name__ == '__main__':
    main()
