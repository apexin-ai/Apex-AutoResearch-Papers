"""Probe Weight Cosine Similarity between Conflict and XNLI probes."""

import argparse
import json
import os
import numpy as np
import torch
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SEED = 42
N_RANDOM = 10


def load_train_data(path):
    d = torch.load(path, map_location="cpu", weights_only=True)
    n_train = d["split_sizes"]["train"]
    X = d["activations"][:n_train].float().numpy()
    y = d["labels"][:n_train].numpy()
    return X, y


def train_probe_and_get_weight(X_layer, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_layer)
    clf = LogisticRegression(max_iter=2000, class_weight="balanced", random_state=SEED)
    clf.fit(X_scaled, y)
    w = clf.coef_.flatten() / scaler.scale_
    return w


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
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", type=str, required=True,
                        help='JSON: {"Name": {"conflict": {"en": "p", "zh": "p"}, "xnli": {"en": "p", "zh": "p"}, "num_layers": N}}')
    parser.add_argument("--output", type=str, default="results/probe_cosine_similarity.json")
    parser.add_argument("--plot_dir", type=str, default=None)
    args = parser.parse_args()

    models = json.loads(args.models)
    results = {}

    for model_name, cfg in models.items():
        print(f"\nModel: {model_name} ({cfg['num_layers']} layers)")
        model_results = {}
        for lang in ["en", "zh"]:
            X_conf, y_conf = load_train_data(cfg["conflict"][lang])
            X_xnli, y_xnli = load_train_data(cfg["xnli"][lang])
            hidden_dim = X_conf.shape[2]
            rand_mean, rand_std = random_baseline(hidden_dim)
            lang_results = {"random_baseline_mean": rand_mean, "layers": {}}
            for layer in range(cfg["num_layers"]):
                w_conf = train_probe_and_get_weight(X_conf[:, layer, :], y_conf)
                w_xnli = train_probe_and_get_weight(X_xnli[:, layer, :], y_xnli)
                sim = cosine_sim(w_conf, w_xnli)
                lang_results["layers"][str(layer)] = sim
            model_results[lang] = lang_results
        results[model_name] = model_results

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
