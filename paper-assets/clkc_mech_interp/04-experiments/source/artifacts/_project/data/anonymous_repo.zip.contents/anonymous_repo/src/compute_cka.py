"""Compute layer-wise Linear CKA and SVCCA between EN vs ZH activations.

Runs all 4 combinations (2 tasks x 2 alignment modes: aligned vs shuffled)
to control for sample pairing confounds.

Usage:
    python src/compute_cka.py \
        --models '{"qwen3": {"conflict": {"en": "data/qwen3/en_activations.pt", "zh": "data/qwen3/zh_activations.pt"}, "xnli": {"en": "data/xnli/qwen3/en_activations.pt", "zh": "data/xnli/qwen3/zh_activations.pt"}}}' \
        --output results/cka_svcca_results.json
"""

import argparse
import json
import time
import numpy as np
import torch
from pathlib import Path
from scipy.linalg import eigh

SEED = 42


def load_test_data(path):
    d = torch.load(path, map_location="cpu", weights_only=True)
    n_train = d["split_sizes"]["train"]
    act = d["activations"][n_train:].float().numpy()
    labels = d["labels"][n_train:].numpy()
    return act, labels


def shuffle_activations(act, rng):
    perm = rng.permutation(act.shape[0])
    return act[perm]


def linear_cka(X, Y):
    X = X - X.mean(axis=0, keepdims=True)
    Y = Y - Y.mean(axis=0, keepdims=True)
    YtX = Y.T @ X
    XtX = X.T @ X
    YtY = Y.T @ Y
    num = np.linalg.norm(YtX, "fro") ** 2
    denom = np.linalg.norm(XtX, "fro") * np.linalg.norm(YtY, "fro")
    if denom < 1e-12:
        return 0.0
    return float(num / denom)


def fast_truncated_svd(M, threshold=0.99):
    n, d = M.shape
    if n <= d:
        G = M @ M.T
        eigvals, eigvecs = eigh(G)
        eigvals = eigvals[::-1]
        eigvecs = eigvecs[:, ::-1]
        eigvals = np.maximum(eigvals, 0)
        s = np.sqrt(eigvals)
        cumvar = np.cumsum(eigvals)
        total = cumvar[-1]
        if total < 1e-12:
            return eigvecs[:, :1] * s[:1]
        k = np.searchsorted(cumvar / total, threshold) + 1
        k = min(k, len(s))
        return eigvecs[:, :k] * s[:k]
    else:
        U, s, _ = np.linalg.svd(M, full_matrices=False)
        cumvar = np.cumsum(s ** 2)
        total = cumvar[-1]
        if total < 1e-12:
            return U[:, :1] * s[:1]
        k = np.searchsorted(cumvar / total, threshold) + 1
        k = min(k, len(s))
        return U[:, :k] * s[:k]


def svcca(X, Y, variance_threshold=0.99):
    X = X - X.mean(axis=0, keepdims=True)
    Y = Y - Y.mean(axis=0, keepdims=True)
    Xr = fast_truncated_svd(X, variance_threshold)
    Yr = fast_truncated_svd(Y, variance_threshold)
    Qx, _ = np.linalg.qr(Xr)
    Qy, _ = np.linalg.qr(Yr)
    d = min(Qx.shape[1], Qy.shape[1])
    _, s, _ = np.linalg.svd(Qx.T @ Qy, full_matrices=False)
    correlations = np.clip(s[:d], 0, 1)
    return float(np.mean(correlations))


def compute_layerwise(en_act, zh_act, n_layers):
    layer_results = {}
    for l in range(n_layers):
        tl = time.time()
        X = en_act[:, l, :]
        Y = zh_act[:, l, :]
        cka_val = linear_cka(X, Y)
        svcca_val = svcca(X, Y)
        layer_results[l] = {"cka": round(cka_val, 6), "svcca": round(svcca_val, 6)}
        dt = time.time() - tl
        if l % 4 == 0 or l == n_layers - 1:
            print(f"    Layer {l:2d}: CKA={cka_val:.4f}, SVCCA={svcca_val:.4f}  ({dt:.1f}s)", flush=True)
    return layer_results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", type=str, required=True,
                        help='JSON: {"model": {"conflict": {"en": "path", "zh": "path"}, "xnli": {"en": "path", "zh": "path"}}}')
    parser.add_argument("--output", type=str, default="results/cka_svcca_results.json")
    args = parser.parse_args()

    rng = np.random.RandomState(SEED)
    models = json.loads(args.models)
    results = {}
    t0 = time.time()

    for model, data_paths in models.items():
        results[model] = {}
        for task in ["conflict", "xnli"]:
            if task not in data_paths:
                continue
            paths = data_paths[task]
            print(f"\n=== {model} / {task} ===", flush=True)
            en_act, en_labels = load_test_data(paths["en"])
            zh_act, zh_labels = load_test_data(paths["zh"])

            n = min(en_act.shape[0], zh_act.shape[0])
            en_act = en_act[:n]
            zh_act = zh_act[:n]
            n_layers = en_act.shape[1]

            for mode in ["aligned", "shuffled"]:
                key = f"{task}_{mode}"
                print(f"\n  [{key}] n={n}, layers={n_layers}")
                if mode == "shuffled":
                    zh_act_use = shuffle_activations(zh_act, rng)
                else:
                    zh_act_use = zh_act
                results[model][key] = compute_layerwise(en_act, zh_act_use, n_layers)

        for mode in ["aligned", "shuffled"]:
            c_key = f"conflict_{mode}"
            x_key = f"xnli_{mode}"
            if c_key in results[model] and x_key in results[model]:
                diff_key = f"conflict_minus_xnli_{mode}"
                results[model][diff_key] = {}
                for l_str in results[model][c_key]:
                    c = results[model][c_key][l_str]
                    x = results[model][x_key][l_str]
                    results[model][diff_key][l_str] = {
                        "cka_diff": round(c["cka"] - x["cka"], 6),
                        "svcca_diff": round(c["svcca"] - x["svcca"], 6),
                    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)

    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.1f}s")
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
