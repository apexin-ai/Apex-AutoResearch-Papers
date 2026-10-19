"""Bootstrap CI for cross-task probe transfer (conflict <-> XNLI)."""

import json
import os
import time
from functools import partial
from multiprocessing import Pool

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

MODELS = {
    "llama31": {"conflict": "data/llama31", "xnli": "data/xnli/llama31", "n_layers": 32},
    "qwen3": {"conflict": "data/qwen3", "xnli": "data/xnli/qwen3", "n_layers": 36},
    "gemma2": {"conflict": "data/gemma2", "xnli": "data/xnli/gemma2", "n_layers": 42},
}

N_BOOTSTRAP = 1000
N_WORKERS = 64


def load_lang_data(base_path):
    en = torch.load(f"{base_path}/en_activations.pt", map_location="cpu", weights_only=True)
    zh = torch.load(f"{base_path}/zh_activations.pt", map_location="cpu", weights_only=True)
    en_acts = en["activations"].float()
    zh_acts = zh["activations"].float()
    acts = torch.cat([en_acts, zh_acts], dim=0).numpy()
    labels = np.concatenate([np.zeros(len(en_acts)), np.ones(len(zh_acts))])
    return acts, labels


def bootstrap_one_seed(seed, X_train, y_train, X_test, y_test):
    rng = np.random.RandomState(seed)
    idx = rng.choice(len(X_train), size=len(X_train), replace=True)
    scaler = StandardScaler()
    X_boot = scaler.fit_transform(X_train[idx])
    y_boot = y_train[idx]
    clf = LogisticRegression(max_iter=1000, class_weight="balanced", solver="lbfgs", random_state=seed)
    clf.fit(X_boot, y_boot)
    X_test_s = scaler.transform(X_test)
    return balanced_accuracy_score(y_test, clf.predict(X_test_s))


def run_bootstrap(X_train, y_train, X_test, y_test, n_bootstrap=N_BOOTSTRAP):
    fn = partial(bootstrap_one_seed, X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)
    with Pool(N_WORKERS) as pool:
        results = pool.map(fn, range(n_bootstrap))
    results = np.array(results)
    return float(np.mean(results)), float(np.percentile(results, 2.5)), float(np.percentile(results, 97.5))


def main():
    os.chdir("/root/clkc_mech_interp")
    all_results = {}
    t_total = time.time()

    for model_name, cfg in MODELS.items():
        conflict_acts, conflict_labels = load_lang_data(cfg["conflict"])
        xnli_acts, xnli_labels = load_lang_data(cfg["xnli"])
        n_layers = cfg["n_layers"]

        c_train_idx, c_test_idx = train_test_split(
            np.arange(len(conflict_labels)), test_size=0.2, random_state=42, stratify=conflict_labels
        )
        x_train_idx, x_test_idx = train_test_split(
            np.arange(len(xnli_labels)), test_size=0.2, random_state=42, stratify=xnli_labels
        )

        model_c2x = {}
        model_x2c = {}

        for layer in range(n_layers):
            c_X = conflict_acts[:, layer, :]
            x_X = xnli_acts[:, layer, :]

            c_X_train, c_X_test = c_X[c_train_idx], c_X[c_test_idx]
            c_y_train, c_y_test = conflict_labels[c_train_idx], conflict_labels[c_test_idx]
            x_X_train, x_X_test = x_X[x_train_idx], x_X[x_test_idx]
            x_y_train, x_y_test = xnli_labels[x_train_idx], xnli_labels[x_test_idx]

            # C -> XNLI: train on conflict, test on xnli
            t0 = time.time()
            mean_c2x, lo_c2x, hi_c2x = run_bootstrap(c_X_train, c_y_train, x_X_test, x_y_test)
            dt_c2x = time.time() - t0
            model_c2x[f"layer_{layer}"] = {"mean": round(mean_c2x, 4), "ci_lo": round(lo_c2x, 4), "ci_hi": round(hi_c2x, 4), "n": N_BOOTSTRAP}
            print(f"[{model_name} L{layer} C->X] mean={mean_c2x:.4f} CI=[{lo_c2x:.4f}, {hi_c2x:.4f}] ({N_BOOTSTRAP} seeds, {dt_c2x:.1f}s)", flush=True)

            # XNLI -> Conflict: train on xnli, test on conflict
            t0 = time.time()
            mean_x2c, lo_x2c, hi_x2c = run_bootstrap(x_X_train, x_y_train, c_X_test, c_y_test)
            dt_x2c = time.time() - t0
            model_x2c[f"layer_{layer}"] = {"mean": round(mean_x2c, 4), "ci_lo": round(lo_x2c, 4), "ci_hi": round(hi_x2c, 4), "n": N_BOOTSTRAP}
            print(f"[{model_name} L{layer} X->C] mean={mean_x2c:.4f} CI=[{lo_x2c:.4f}, {hi_x2c:.4f}] ({N_BOOTSTRAP} seeds, {dt_x2c:.1f}s)", flush=True)

        all_results[model_name] = {"c_to_xnli": model_c2x, "xnli_to_conflict": model_x2c}

        # Save intermediate
        out_path = "data/cross_task_transfer_bootstrap_n1000.json"
        with open(out_path, "w") as f:
            json.dump(all_results, f, indent=2)
        print(f"[{model_name}] saved intermediate to {out_path}", flush=True)

    elapsed = time.time() - t_total
    print(f"\nTotal time: {elapsed:.1f}s ({elapsed/60:.1f}min)")
    print(f"Final output: data/cross_task_transfer_bootstrap_n1000.json")


if __name__ == "__main__":
    main()
