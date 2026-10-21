"""Visualize BEV occupancy maps for validation."""

import os
import sys
import argparse

os.environ["MUJOCO_GL"] = "egl"

import numpy as np
import h5py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

SEMANTIC_CMAP = ListedColormap(["white", "#8B4513", "#4169E1", "#FF6347"])
SEMANTIC_LABELS = ["free", "table", "robot", "target"]


def plot_bev_frames(bev_binary, bev_semantic, frame_indices, save_path, title_prefix=""):
    n = len(frame_indices)
    fig, axes = plt.subplots(2, n, figsize=(4 * n, 8))
    if n == 1:
        axes = axes[:, np.newaxis]

    for col, t in enumerate(frame_indices):
        axes[0, col].imshow(bev_binary[t].T, origin="lower", cmap="gray_r")
        axes[0, col].set_title(f"{title_prefix}Binary t={t}")
        axes[0, col].set_xlabel("x")
        axes[0, col].set_ylabel("y")

        im = axes[1, col].imshow(
            bev_semantic[t].T, origin="lower",
            cmap=SEMANTIC_CMAP, vmin=0, vmax=3,
        )
        axes[1, col].set_title(f"{title_prefix}Semantic t={t}")
        axes[1, col].set_xlabel("x")
        axes[1, col].set_ylabel("y")

    cbar = fig.colorbar(im, ax=axes[1, :].tolist(), shrink=0.6)
    cbar.set_ticks([0, 1, 2, 3])
    cbar.set_ticklabels(SEMANTIC_LABELS)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {save_path}")


def visualize_from_file(occ_file, demo_key, frame_indices, save_dir):
    """Visualize BEV from a pre-extracted occupancy HDF5."""
    with h5py.File(occ_file, "r") as f:
        bev_bin = f[f"data/{demo_key}/bev_binary"][:]
        bev_sem = f[f"data/{demo_key}/bev_semantic"][:]

    T = len(bev_bin)
    if frame_indices is None:
        frame_indices = [0, T // 4, T // 2, 3 * T // 4, T - 1]

    frame_indices = [min(t, T - 1) for t in frame_indices]

    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"bev_{demo_key}.png")
    plot_bev_frames(bev_bin, bev_sem, frame_indices, save_path)

    occ_rate = bev_bin.mean() * 100
    print(f"Demo: {demo_key}, frames: {T}, occ_rate: {occ_rate:.1f}%")
    for c in range(4):
        pct = (bev_sem == c).sum() / bev_sem.size * 100
        print(f"  {SEMANTIC_LABELS[c]}: {pct:.1f}%")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--occ_file", type=str, default=None)
    parser.add_argument("--demo", type=str, default="demo_0")
    parser.add_argument("--frames", type=str, default=None,
                        help="Comma-separated frame indices")
    parser.add_argument("--save_dir", type=str,
                        default="/root/occsafe_vla/artifacts/")
    args = parser.parse_args()

    if args.occ_file:
        frame_indices = None
        if args.frames:
            frame_indices = [int(x) for x in args.frames.split(",")]
        visualize_from_file(args.occ_file, args.demo, frame_indices, args.save_dir)
    else:
        print("Specify --occ_file")
        sys.exit(1)


if __name__ == "__main__":
    main()
