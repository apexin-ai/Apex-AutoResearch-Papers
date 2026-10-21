"""AdvBench hidden-state exploratory analysis: volatility, norms, HarmThoughts comparison."""
import os, json, glob
import numpy as np
import torch
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path("artifacts/advbench_preliminary")
OUT_DIR.mkdir(parents=True, exist_ok=True)

N_LAYERS = 25
BATCH_SIZE = 50


def process_dataset(file_list, name):
    print(f"Processing {name}: {len(file_list)} files")
    all_vols = [[] for _ in range(N_LAYERS)]
    layer_bin_norms = [[[] for _ in range(5)] for _ in range(N_LAYERS)]
    bin_edges = [0, 12.5, 37.5, 62.5, 87.5, 100.01]

    for start in range(0, len(file_list), BATCH_SIZE):
        batch_files = file_list[start:start + BATCH_SIZE]
        for f in batch_files:
            d = torch.load(f, map_location="cpu", weights_only=False)
            hs = d["hidden_states"].float()  # [T, L, D]
            T, L, D = hs.shape
            if T < 2:
                continue

            # Volatility
            for layer in range(L):
                a = hs[:-1, layer, :]
                b = hs[1:, layer, :]
                cos = torch.nn.functional.cosine_similarity(a, b, dim=1)
                vol = 1.0 - cos.mean().item()
                all_vols[layer].append(vol)

            # Norm trends at normalized positions
            norms = hs.norm(dim=2)  # [T, L]
            positions = np.linspace(0, 100, T)
            for t_idx in range(T):
                pos = positions[t_idx]
                for b_idx in range(5):
                    if bin_edges[b_idx] <= pos < bin_edges[b_idx + 1]:
                        for layer in range(L):
                            layer_bin_norms[layer][b_idx].append(norms[t_idx, layer].item())
                        break

        print(f"  batch {start}-{start+len(batch_files)}: done")

    norm_means = np.zeros((N_LAYERS, 5))
    for layer in range(N_LAYERS):
        for b in range(5):
            if layer_bin_norms[layer][b]:
                norm_means[layer, b] = np.mean(layer_bin_norms[layer][b])

    vol_means = np.array([np.mean(v) if v else 0.0 for v in all_vols])
    vol_stds = np.array([np.std(v) if v else 0.0 for v in all_vols])

    return {
        "vol_means": vol_means,
        "vol_stds": vol_stds,
        "vol_all": all_vols,
        "norm_means": norm_means,
    }


def main():
    advbench_dir = "artifacts/hidden_states_advbench"
    harmthoughts_dir = "artifacts/hidden_states_r1_8b_full"

    advbench_files = sorted(glob.glob(os.path.join(advbench_dir, "advbench_*.pt")))
    harmthoughts_files = sorted(glob.glob(os.path.join(harmthoughts_dir, "*.pt")))

    print(f"AdvBench: {len(advbench_files)} files")
    print(f"HarmThoughts: {len(harmthoughts_files)} files")

    adv = process_dataset(advbench_files, "AdvBench")
    ht = process_dataset(harmthoughts_files, "HarmThoughts")

    # --- Figure 1: Volatility curves ---
    fig, ax = plt.subplots(figsize=(8, 4))
    layers = np.arange(N_LAYERS)
    ax.plot(layers, adv["vol_means"], "o-", color="#1f77b4", label="AdvBench", linewidth=2, markersize=5)
    ax.fill_between(layers, adv["vol_means"] - adv["vol_stds"], adv["vol_means"] + adv["vol_stds"],
                     color="#1f77b4", alpha=0.15)
    ax.plot(layers, ht["vol_means"], "s-", color="#e67e22", label="HarmThoughts", linewidth=2, markersize=5)
    ax.fill_between(layers, ht["vol_means"] - ht["vol_stds"], ht["vol_means"] + ht["vol_stds"],
                     color="#e67e22", alpha=0.15)
    ax.set_xlabel("Layer", fontsize=11)
    ax.set_ylabel("Volatility (1 − cosine sim)", fontsize=11)
    ax.set_title("Per-Layer Consecutive-Step Volatility", fontsize=12)
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=10)
    ax.set_xticks(layers)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig1_volatility_curve.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Saved fig1_volatility_curve.png")

    # --- Figure 2: Norm heatmaps ---
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
    for ax, data, title in zip(axes, [adv["norm_means"], ht["norm_means"]], ["AdvBench", "HarmThoughts"]):
        im = ax.imshow(data, aspect="auto", cmap="viridis", interpolation="nearest")
        ax.set_xlabel("Step position", fontsize=11)
        ax.set_xticks(range(5))
        ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
        ax.set_ylabel("Layer", fontsize=11)
        ax.set_yticks(range(N_LAYERS))
        ax.set_title(f"{title} — L2 Norm", fontsize=12)
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig2_norm_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Saved fig2_norm_heatmap.png")

    # --- Figure 3: Shallow vs deep volatility boxplot ---
    shallow_layers = list(range(0, 5))
    deep_layers = list(range(12, 25))

    adv_shallow = [v for l in shallow_layers for v in adv["vol_all"][l]]
    adv_deep = [v for l in deep_layers for v in adv["vol_all"][l]]
    ht_shallow = [v for l in shallow_layers for v in ht["vol_all"][l]]
    ht_deep = [v for l in deep_layers for v in ht["vol_all"][l]]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    bp = ax.boxplot(
        [adv_shallow, adv_deep, ht_shallow, ht_deep],
        labels=["AdvBench\nL0-4", "AdvBench\nL12-24", "HarmThoughts\nL0-4", "HarmThoughts\nL12-24"],
        patch_artist=True,
        widths=0.5,
    )
    colors = ["#1f77b4", "#aec7e8", "#e67e22", "#f5cba7"]
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
    ax.set_ylabel("Volatility (1 − cosine sim)", fontsize=11)
    ax.set_title("Shallow vs Deep Layer Volatility", fontsize=12)
    ax.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "fig3_shallow_vs_deep_boxplot.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Saved fig3_shallow_vs_deep_boxplot.png")

    # --- Results JSON ---
    shallow_vol_adv = float(np.mean([np.mean(adv["vol_all"][l]) for l in shallow_layers]))
    deep_vol_adv = float(np.mean([np.mean(adv["vol_all"][l]) for l in deep_layers]))
    shallow_vol_ht = float(np.mean([np.mean(ht["vol_all"][l]) for l in shallow_layers]))
    deep_vol_ht = float(np.mean([np.mean(ht["vol_all"][l]) for l in deep_layers]))

    results = {
        "advbench": {
            "n_traces": len(advbench_files),
            "per_layer_volatility_mean": adv["vol_means"].tolist(),
            "per_layer_volatility_std": adv["vol_stds"].tolist(),
            "shallow_L0_L4_mean_volatility": shallow_vol_adv,
            "deep_L12_L24_mean_volatility": deep_vol_adv,
            "shallow_to_deep_ratio": shallow_vol_adv / deep_vol_adv if deep_vol_adv > 0 else None,
            "norm_trend_by_layer": adv["norm_means"].tolist(),
        },
        "harmthoughts": {
            "n_traces": len(harmthoughts_files),
            "per_layer_volatility_mean": ht["vol_means"].tolist(),
            "per_layer_volatility_std": ht["vol_stds"].tolist(),
            "shallow_L0_L4_mean_volatility": shallow_vol_ht,
            "deep_L12_L24_mean_volatility": deep_vol_ht,
            "shallow_to_deep_ratio": shallow_vol_ht / deep_vol_ht if deep_vol_ht > 0 else None,
            "norm_trend_by_layer": ht["norm_means"].tolist(),
        },
        "comparison": {
            "shallow_volatility_diff_adv_minus_ht": shallow_vol_adv - shallow_vol_ht,
            "deep_volatility_diff_adv_minus_ht": deep_vol_adv - deep_vol_ht,
            "prediction": (
                "shallow_CR_likely" if shallow_vol_adv >= deep_vol_adv
                else "deep_CR_likely"
            ),
        },
    }

    with open(OUT_DIR / "hs_exploratory_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Saved hs_exploratory_results.json")

    print("\n=== SUMMARY ===")
    print(f"AdvBench  shallow (L0-4) vol: {shallow_vol_adv:.6f}")
    print(f"AdvBench  deep (L12-24) vol:  {deep_vol_adv:.6f}")
    print(f"AdvBench  shallow/deep ratio: {shallow_vol_adv/deep_vol_adv:.3f}")
    print(f"HarmThoughts shallow (L0-4) vol: {shallow_vol_ht:.6f}")
    print(f"HarmThoughts deep (L12-24) vol:  {deep_vol_ht:.6f}")
    print(f"HarmThoughts shallow/deep ratio: {shallow_vol_ht/deep_vol_ht:.3f}")
    print(f"Prediction: {results['comparison']['prediction']}")


if __name__ == "__main__":
    main()
