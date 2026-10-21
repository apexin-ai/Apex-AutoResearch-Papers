#!/usr/bin/env python3
"""Generate CKA paper figures from pre-extracted JSON data."""

import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 13,
    "axes.titlesize": 13,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

RESULTS_DIR = Path("/root/recovery_aware_struct_prune/results")
FIG_DIR = RESULTS_DIR / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    with open(RESULTS_DIR / "cka_per_layer.json") as f:
        per_layer = json.load(f)["per_layer"]
    with open(RESULTS_DIR / "cka_heatmap.json") as f:
        heatmap = json.load(f)
    return per_layer, heatmap


def plot_per_layer_overlap(per_layer):
    """Fig A: Per-layer mean CKA overlap - grouped bars for Attention vs MLP."""
    layers = sorted(int(k) for k in per_layer.keys())
    attn_means = [per_layer[str(i)]["attn_mean"] for i in layers]
    mlp_means = [per_layer[str(i)]["mlp_mean"] for i in layers]

    x = np.arange(len(layers))
    w = 0.38

    fig, ax = plt.subplots(figsize=(8, 3))
    bars_attn = ax.bar(x - w / 2, attn_means, w, label="Attention heads",
                       color="#4C72B0", edgecolor="white", linewidth=0.3)
    bars_mlp = ax.bar(x + w / 2, mlp_means, w, label="MLP neurons",
                      color="#DD8452", edgecolor="white", linewidth=0.3)

    # Annotate top-3 overlap layers (by combined mean)
    combined = [(attn_means[i] + mlp_means[i], i) for i in range(len(layers))]
    combined.sort(reverse=True)
    for _, idx in combined[:3]:
        y_top = max(attn_means[idx], mlp_means[idx])
        ax.plot(idx, y_top + 0.015, marker="v", markersize=7,
                color="#C44E52", clip_on=False)

    ax.set_xlabel("Layer index")
    ax.set_ylabel("Mean $\\mathcal{F}(h)$")
    ax.set_xticks(x[::2])
    ax.set_xticklabels([str(i) for i in layers[::2]])
    ax.set_ylim(0.4, 1.05)
    ax.legend(frameon=True, fontsize=10, loc="lower right",
              framealpha=0.9, edgecolor="0.8")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linewidth=0.5)

    out = FIG_DIR / "cka_per_layer_overlap.pdf"
    fig.savefig(out)
    plt.close(fig)
    print(f"Saved {out}")
    return attn_means, mlp_means, layers


def plot_cka_heatmaps(heatmap, attn_means, mlp_means, layers):
    """Fig B: CKA similarity heatmaps for highest- and lowest-overlap layers."""
    combined = [attn_means[i] + mlp_means[i] for i in range(len(layers))]
    hi_layer = layers[int(np.argmax(combined))]
    lo_layer = layers[int(np.argmin(combined))]

    fig, axes = plt.subplots(2, 2, figsize=(7.5, 6.5),
                             gridspec_kw={"hspace": 0.35, "wspace": 0.30})

    pairs = [(hi_layer, "High-overlap"), (lo_layer, "Low-overlap")]
    for col, (layer_idx, label) in enumerate(pairs):
        layer_data = heatmap[str(layer_idx)]
        attn_mat = np.array(layer_data["attn_cka_matrix"])
        mlp_mat = np.array(layer_data["mlp_cka_matrix"])

        # Attention heatmap
        ax = axes[0, col]
        im = ax.imshow(attn_mat, cmap="coolwarm", vmin=0.0, vmax=1.0, aspect="equal")
        ax.set_xlabel("Head index")
        ax.set_ylabel("Head index")
        ax.set_xticks(range(attn_mat.shape[0]))
        ax.set_yticks(range(attn_mat.shape[0]))
        ax.set_title(f"{label} layer {layer_idx} -- Attn", fontsize=11)
        for i in range(attn_mat.shape[0]):
            for j in range(attn_mat.shape[1]):
                ax.text(j, i, f"{attn_mat[i, j]:.2f}", ha="center", va="center",
                        fontsize=7.5, color="white" if attn_mat[i, j] < 0.5 else "black")

        # MLP heatmap (subsample if large)
        ax2 = axes[1, col]
        if mlp_mat.shape[0] > 16:
            step = mlp_mat.shape[0] // 14
            idx = list(range(0, mlp_mat.shape[0], step))
            mlp_sub = mlp_mat[np.ix_(idx, idx)]
            tick_labels = [str(i) for i in idx]
        else:
            mlp_sub = mlp_mat
            tick_labels = [str(i) for i in range(mlp_mat.shape[0])]

        im2 = ax2.imshow(mlp_sub, cmap="viridis", vmin=np.min(mlp_sub) * 0.98,
                         vmax=1.0, aspect="equal")
        ax2.set_xlabel("Neuron group")
        ax2.set_ylabel("Neuron group")
        ax2.set_xticks(range(len(tick_labels)))
        ax2.set_xticklabels(tick_labels, fontsize=7)
        ax2.set_yticks(range(len(tick_labels)))
        ax2.set_yticklabels(tick_labels, fontsize=7)
        ax2.set_title(f"{label} layer {layer_idx} -- MLP", fontsize=11)
        plt.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)

    # Shared colorbar for attention row
    plt.colorbar(im, ax=axes[0, :].tolist(), fraction=0.02, pad=0.04, label="CKA")

    out = FIG_DIR / "cka_heatmap.pdf"
    fig.savefig(out)
    plt.close(fig)
    print(f"Saved {out}")


if __name__ == "__main__":
    per_layer, heatmap = load_data()
    attn_means, mlp_means, layers = plot_per_layer_overlap(per_layer)
    plot_cka_heatmaps(heatmap, attn_means, mlp_means, layers)
    print("Done.")
