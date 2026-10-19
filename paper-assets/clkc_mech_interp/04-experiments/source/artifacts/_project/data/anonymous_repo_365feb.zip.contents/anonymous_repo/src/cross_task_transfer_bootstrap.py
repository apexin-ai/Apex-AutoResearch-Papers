"""Bootstrap CI for cross-task probe transfer (conflict <-> XNLI).

Uses multiprocessing Pool with fork-based COW shared memory for efficiency.

Usage:
    python src/cross_task_transfer_bootstrap.py \
        --models '{"llama31": {"conflict": "data/llama31", "xnli": "data/xnli/llama31", "n_layers": 32}}' \
        --n_bootstrap 1000 --n_workers 64 \
        --output results/cross_task_transfer_bootstrap.json
"""

import argparse
import json
import time
from multiprocessing import Pool

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

_G = {}


def load_lang_data(base_path):
    en = torch.load(f"{base_path}/en_activations.pt", map_location="cpu", weights_only=True)
    zh = torch.load(f"{base_path}/zh_activations.pt", map_location="cpu", weights_only=True)
    en_acts = en["activations"].float()
    zh_acts = zh["activations"].float()
    acts = torch.cat([en_acts, zh_acts], dim=0).numpy()
    labels = np.concatenate([np.zeros(len(en_acts)), np.ones(len(zh_acts))])
    return acts, labels


def _worker(args):
    layer, direction, seed = args
    if direction == 0:
        X_train = _G["c_trains"][layer]
        y_train = _G["c_y_train"]
        X_test = _G["x_tests"][layer]
        y_test = _G["x_y_test"]
    else:
        X_train = _G["x_trains"][layer]
        y_train = _G["x_y_train"]
        X_test = _G["c_tests"][layer]
        y_test = _G["c_y_test"]

    rng = np.random.RandomState(seed)
    idx = rng.choice(len(X_train), size=len(X_train), replace=True)
    scaler = StandardScaler()
    X_boot = scaler.fit_transform(X_train[idx])
    clf = LogisticRegression(max_iter=1000, class_weight="balanced", solver="liblinear", random_state=seed)
    clf.fit(X_boot, y_train[idx])
    X_test_s = scaler.transform(X_test)
    return balanced_accuracy_score(y_test, clf.predict(X_test_s))


def main():
    global _G
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", type=str, required=True,
                        help='JSON: {"name": {"conflict": "path", "xnli": "path", "n_layers": N}}')
    parser.add_argument("--n_bootstrap", type=int, default=1000)
    parser.add_argument("--n_workers", type=int, default=64)
    parser.add_argument("--output", type=str, default="results/cross_task_transfer_bootstrap.json")
    args = parser.parse_args()

    models = json.loads(args.models)
    all_results = {}
    t_total = time.time()

    for model_name, cfg in models.items():
        t_model = time.time()
        print(f"[{model_name}] Loading data...", flush=True)
        conflict_acts, conflict_labels = load_lang_data(cfg["conflict"])
        xnli_acts, xnli_labels = load_lang_data(cfg["xnli"])
        n_layers = cfg["n_layers"]

        c_train_idx, c_test_idx = train_test_split(
            np.arange(len(conflict_labels)), test_size=0.2, random_state=42, stratify=conflict_labels
        )
        x_train_idx, x_test_idx = train_test_split(
            np.arange(len(xnli_labels)), test_size=0.2, random_state=42, stratify=xnli_labels
        )

        _G["c_trains"] = [np.ascontiguousarray(conflict_acts[:, l, :][c_train_idx]) for l in range(n_layers)]
        _G["c_tests"] = [np.ascontiguousarray(conflict_acts[:, l, :][c_test_idx]) for l in range(n_layers)]
        _G["x_trains"] = [np.ascontiguousarray(xnli_acts[:, l, :][x_train_idx]) for l in range(n_layers)]
        _G["x_tests"] = [np.ascontiguousarray(xnli_acts[:, l, :][x_test_idx]) for l in range(n_layers)]
        _G["c_y_train"] = conflict_labels[c_train_idx]
        _G["c_y_test"] = conflict_labels[c_test_idx]
        _G["x_y_train"] = xnli_labels[x_train_idx]
        _G["x_y_test"] = xnli_labels[x_test_idx]

        del conflict_acts, xnli_acts

        n_bootstrap = args.n_bootstrap
        n_jobs = n_layers * 2 * n_bootstrap
        print(f"[{model_name}] {n_jobs} jobs, Pool({args.n_workers})...", flush=True)

        jobs = []
        for layer in range(n_layers):
            for direction in [0, 1]:
                for seed in range(n_bootstrap):
                    jobs.append((layer, direction, seed))

        with Pool(args.n_workers) as pool:
            raw = pool.map(_worker, jobs, chunksize=100)

        scores = {}
        for i, acc in enumerate(raw):
            layer, direction, seed = jobs[i]
            key = (layer, direction)
            if key not in scores:
                scores[key] = []
            scores[key].append(acc)

        model_c2x = {}
        model_x2c = {}
        for layer in range(n_layers):
            for direction, store, label in [(0, model_c2x, "C->X"), (1, model_x2c, "X->C")]:
                arr = np.array(scores[(layer, direction)])
                m = float(np.mean(arr))
                lo = float(np.percentile(arr, 2.5))
                hi = float(np.percentile(arr, 97.5))
                store[f"layer_{layer}"] = {"mean": round(m, 4), "ci_lo": round(lo, 4), "ci_hi": round(hi, 4), "n": n_bootstrap}
                print(f"[{model_name} L{layer} {label}] mean={m:.4f} CI=[{lo:.4f}, {hi:.4f}]", flush=True)

        all_results[model_name] = {"c_to_xnli": model_c2x, "xnli_to_conflict": model_x2c}
        dt_model = time.time() - t_model
        print(f"[{model_name}] done in {dt_model:.1f}s ({dt_model/60:.1f}min)", flush=True)

    from pathlib import Path
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(all_results, f, indent=2)

    elapsed = time.time() - t_total
    print(f"\nTotal time: {elapsed:.1f}s ({elapsed/60:.1f}min)")
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
