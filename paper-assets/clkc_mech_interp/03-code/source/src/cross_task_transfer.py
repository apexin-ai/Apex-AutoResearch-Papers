"""Cross-task probe transfer: test if conflict and XNLI share a cross-lingual subspace.

Train language probes (en=0 vs zh=1) on one task, evaluate on the other.
If piggyback hypothesis holds, cross-task accuracy >> 50%.
"""

import json
import os
from pathlib import Path

import joblib
import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


MODELS = {
    "llama31": {"conflict": "data/llama31", "xnli": "data/xnli/llama31"},
    "qwen3": {"conflict": "data/qwen3", "xnli": "data/xnli/qwen3"},
    "gemma2": {"conflict": "data/gemma2", "xnli": "data/xnli/gemma2"},
}


def load_lang_data(base_path: str):
    """Load en + zh activations, assign language labels (en=0, zh=1)."""
    en = torch.load(f"{base_path}/en_activations.pt", map_location="cpu", weights_only=True)
    zh = torch.load(f"{base_path}/zh_activations.pt", map_location="cpu", weights_only=True)

    en_acts = en["activations"].float()
    zh_acts = zh["activations"].float()

    acts = torch.cat([en_acts, zh_acts], dim=0).numpy()
    labels = np.concatenate([np.zeros(len(en_acts)), np.ones(len(zh_acts))])
    return acts, labels


def train_probe(X_train, y_train):
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    clf = LogisticRegression(
        class_weight="balanced", max_iter=1000, solver="lbfgs", random_state=42
    )
    clf.fit(X_train_s, y_train)
    return clf, scaler


def evaluate(clf, scaler, X_test, y_test):
    X_test_s = scaler.transform(X_test)
    y_pred = clf.predict(X_test_s)
    acc = float(np.mean(y_pred == y_test))
    bal_acc = balanced_accuracy_score(y_test, y_pred)
    return acc, bal_acc


def main():
    results = {}

    for model_name, paths in MODELS.items():
        print(f"\n{'='*60}")
        print(f"MODEL: {model_name}")
        print(f"{'='*60}")

        conflict_acts, conflict_labels = load_lang_data(paths["conflict"])
        xnli_acts, xnli_labels = load_lang_data(paths["xnli"])

        n_layers = conflict_acts.shape[1]
        print(f"  Conflict: {conflict_acts.shape[0]} samples, XNLI: {xnli_acts.shape[0]} samples, {n_layers} layers")

        c_train_idx, c_test_idx = train_test_split(
            np.arange(len(conflict_labels)), test_size=0.2, random_state=42, stratify=conflict_labels
        )
        x_train_idx, x_test_idx = train_test_split(
            np.arange(len(xnli_labels)), test_size=0.2, random_state=42, stratify=xnli_labels
        )

        probe_dir = Path(f"data/{model_name}/probe_weights")
        probe_dir.mkdir(parents=True, exist_ok=True)

        model_results = []

        for layer in range(n_layers):
            c_X = conflict_acts[:, layer, :]
            x_X = xnli_acts[:, layer, :]

            c_X_train, c_X_test = c_X[c_train_idx], c_X[c_test_idx]
            c_y_train, c_y_test = conflict_labels[c_train_idx], conflict_labels[c_test_idx]

            x_X_train, x_X_test = x_X[x_train_idx], x_X[x_test_idx]
            x_y_train, x_y_test = xnli_labels[x_train_idx], xnli_labels[x_test_idx]

            # Train probes
            c_probe, c_scaler = train_probe(c_X_train, c_y_train)
            x_probe, x_scaler = train_probe(x_X_train, x_y_train)

            # Same-task baselines
            c_acc, c_bal = evaluate(c_probe, c_scaler, c_X_test, c_y_test)
            x_acc, x_bal = evaluate(x_probe, x_scaler, x_X_test, x_y_test)

            # Cross-task: need to re-scale with the other task's scaler
            # conflict probe on XNLI test: fit scaler on conflict train, transform XNLI test
            cx_acc, cx_bal = evaluate(c_probe, c_scaler, x_X_test, x_y_test)
            # XNLI probe on conflict test
            xc_acc, xc_bal = evaluate(x_probe, x_scaler, c_X_test, c_y_test)

            model_results.append({
                "layer": layer,
                "conflict_same": round(c_bal, 4),
                "xnli_same": round(x_bal, 4),
                "conflict_to_xnli": round(cx_bal, 4),
                "xnli_to_conflict": round(xc_bal, 4),
                "transfer_ratio_c2x": round(cx_bal / max(c_bal, 0.01), 4),
                "transfer_ratio_x2c": round(xc_bal / max(x_bal, 0.01), 4),
            })

            # Save probes
            joblib.dump({"probe": c_probe, "scaler": c_scaler},
                        probe_dir / f"layer_{layer}_conflict_lang.pkl")
            joblib.dump({"probe": x_probe, "scaler": x_scaler},
                        probe_dir / f"layer_{layer}_xnli_lang.pkl")

        results[model_name] = model_results

        # Print table
        print(f"\n  {'Layer':>5} | {'Conflict':>8} | {'XNLI':>8} | {'C→XNLI':>8} | {'X→Conf':>8} | {'TR c2x':>7} | {'TR x2c':>7}")
        print(f"  {'-'*5}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*7}-+-{'-'*7}")
        for r in model_results:
            print(f"  {r['layer']:5d} | {r['conflict_same']:8.4f} | {r['xnli_same']:8.4f} | "
                  f"{r['conflict_to_xnli']:8.4f} | {r['xnli_to_conflict']:8.4f} | "
                  f"{r['transfer_ratio_c2x']:7.4f} | {r['transfer_ratio_x2c']:7.4f}")

        # Peak cross-task layers
        peak_c2x = max(model_results, key=lambda r: r["conflict_to_xnli"])
        peak_x2c = max(model_results, key=lambda r: r["xnli_to_conflict"])
        print(f"\n  Peak C→XNLI: layer {peak_c2x['layer']}, bal_acc={peak_c2x['conflict_to_xnli']:.4f} "
              f"(same-task baseline: {peak_c2x['conflict_same']:.4f}, TR={peak_c2x['transfer_ratio_c2x']:.4f})")
        print(f"  Peak X→Conf: layer {peak_x2c['layer']}, bal_acc={peak_x2c['xnli_to_conflict']:.4f} "
              f"(same-task baseline: {peak_x2c['xnli_same']:.4f}, TR={peak_x2c['transfer_ratio_x2c']:.4f})")

    # Save all results
    out_path = "data/cross_task_transfer_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved results to {out_path}")


if __name__ == "__main__":
    main()
