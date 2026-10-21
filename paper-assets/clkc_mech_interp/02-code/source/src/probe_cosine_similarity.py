"""Experiment 2: Probe Weight Cosine Similarity between Conflict and XNLI probes."""

import json
import os
import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

MODELS = {
    "Llama-3.1-8B": {
        "conflict": {"en": "data/llama31/en_activations.pt", "zh": "data/llama31/zh_activations.pt"},
        "xnli": {"en": "data/xnli/llama31/en_activations.pt", "zh": "data/xnli/llama31/zh_activations.pt"},
        "num_layers": 32,
    },
    "Qwen3-8B": {
        "conflict": {"en": "data/qwen3/en_activations.pt", "zh": "data/qwen3/zh_activations.pt"},
        "xnli": {"en": "data/xnli/qwen3/en_activations.pt", "zh": "data/xnli/qwen3/zh_activations.pt"},
        "num_layers": 36,
    },
    "Gemma-2-9B": {
        "conflict": {"en": "data/gemma2/en_activations.pt", "zh": "data/gemma2/zh_activations.pt"},
        "xnli": {"en": "data/xnli/gemma2/en_activations.pt", "zh": "data/xnli/gemma2/zh_activations.pt"},
        "num_layers": 42,
    },
}

N_RANDOM = 10
SEED = 42


def load_train_data(path):
    d = torch.load(path, map_location="cpu")
    n_train = d["split_sizes"]["train"]
    X = d["activations"][:n_train].float().numpy()  # [n_train, layers, dim]
    y = d["labels"][:n_train].numpy()
    return X, y


def train_probe(X_layer, y):
    clf = LogisticRegression(max_iter=1000, class_weight="balanced", random_state=SEED)
    clf.fit(X_layer, y)
    return clf.coef_.flatten()  # [hidden_dim]


def cosine_sim(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def random_baseline(dim, n=N_RANDOM):
    rng = np.random.RandomState(SEED)
    sims = []
    for _ in range(n):
        u = rng.randn(dim)
        v = rng.randn(dim)
        sims.append(cosine_sim(u, v))
    return float(np.mean(sims)), float(np.std(sims))


def main():
    results = {}

    for model_name, cfg in MODELS.items():
        print(f"\n{'='*50}")
        print(f"Model: {model_name} ({cfg['num_layers']} layers)")
        print(f"{'='*50}")

        model_results = {}

        for lang in ["en", "zh"]:
            print(f"\n  Language: {lang}")
            X_conf, y_conf = load_train_data(cfg["conflict"][lang])
            X_xnli, y_xnli = load_train_data(cfg["xnli"][lang])
            hidden_dim = X_conf.shape[2]

            rand_mean, rand_std = random_baseline(hidden_dim)
            lang_results = {"random_baseline_mean": rand_mean, "random_baseline_std": rand_std, "layers": {}}

            for layer in range(cfg["num_layers"]):
                w_conf = train_probe(X_conf[:, layer, :], y_conf)
                w_xnli = train_probe(X_xnli[:, layer, :], y_xnli)
                sim = cosine_sim(w_conf, w_xnli)
                lang_results["layers"][str(layer)] = sim

                if layer % 8 == 0 or layer == cfg["num_layers"] - 1:
                    print(f"    Layer {layer:2d}: cos_sim = {sim:.4f}")

            model_results[lang] = lang_results

        # Average across languages
        avg_layers = {}
        for layer in range(cfg["num_layers"]):
            avg_layers[str(layer)] = (
                model_results["en"]["layers"][str(layer)]
                + model_results["zh"]["layers"][str(layer)]
            ) / 2
        model_results["avg"] = {
            "random_baseline_mean": rand_mean,
            "random_baseline_std": rand_std,
            "layers": avg_layers,
        }

        results[model_name] = model_results

    os.makedirs("data", exist_ok=True)
    with open("data/probe_cosine_similarity.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to data/probe_cosine_similarity.json")

    # === Plotting ===
    os.makedirs("figures/paper", exist_ok=True)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), sharey=True)
    colors = {"Llama-3.1-8B": "#E24A33", "Qwen3-8B": "#348ABD", "Gemma-2-9B": "#8EBA42"}

    for ax, lang, title in zip(axes, ["en", "zh"], ["English", "Chinese"]):
        for model_name, cfg in MODELS.items():
            n_layers = cfg["num_layers"]
            layers = list(range(n_layers))
            depths = [l / (n_layers - 1) for l in layers]
            sims = [results[model_name][lang]["layers"][str(l)] for l in layers]
            ax.plot(depths, sims, label=model_name, color=colors[model_name], linewidth=1.8)

        rand_mean = results["Llama-3.1-8B"]["en"]["random_baseline_mean"]
        rand_std = results["Llama-3.1-8B"]["en"]["random_baseline_std"]
        ax.axhline(y=rand_mean, color="gray", linestyle="--", linewidth=1, alpha=0.7, label="Random baseline")
        ax.axhspan(rand_mean - rand_std, rand_mean + rand_std, color="gray", alpha=0.1)

        ax.set_xlabel("Normalized Depth")
        ax.set_title(title)
        ax.set_xlim(0, 1)
        ax.grid(True, alpha=0.3)

    axes[0].set_ylabel("Cosine Similarity")
    axes[0].legend(fontsize=8, loc="upper right")

    fig.suptitle("Probe Weight Cosine Similarity: Conflict vs. XNLI", fontsize=13, y=1.02)
    plt.tight_layout()
    fig.savefig("figures/paper/cosine_similarity.pdf", bbox_inches="tight", dpi=300)
    fig.savefig("figures/paper/cosine_similarity.png", bbox_inches="tight", dpi=300)
    print("Figures saved to figures/paper/cosine_similarity.{pdf,png}")

    # === Summary ===
    print("\n" + "=" * 60)
    print("SUMMARY: Peak cosine similarity per model")
    print("=" * 60)
    for model_name in MODELS:
        for lang in ["en", "zh", "avg"]:
            sims = results[model_name][lang]["layers"]
            peak_layer = max(sims, key=sims.get)
            peak_val = sims[peak_layer]
            rand_m = results[model_name][lang]["random_baseline_mean"]
            print(f"  {model_name} [{lang}]: layer {peak_layer}, cos_sim = {peak_val:.4f} (random baseline = {rand_m:.4f})")


if __name__ == "__main__":
    main()
