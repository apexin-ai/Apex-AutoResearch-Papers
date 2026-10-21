"""Cross-task probe transfer: test if conflict and XNLI share a cross-lingual subspace.

Train language probes (en=0 vs zh=1) on one task, evaluate on the other.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_lang_data(base_path: str):
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
    clf = LogisticRegression(class_weight="balanced", max_iter=1000, solver="lbfgs", random_state=42)
    clf.fit(X_train_s, y_train)
    return clf, scaler


def evaluate(clf, scaler, X_test, y_test):
    X_test_s = scaler.transform(X_test)
    y_pred = clf.predict(X_test_s)
    return balanced_accuracy_score(y_test, y_pred)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", type=str, required=True,
                        help='JSON: {"model": {"conflict": "path", "xnli": "path"}}')
    parser.add_argument("--output", type=str, default="results/cross_task_transfer.json")
    args = parser.parse_args()

    models = json.loads(args.models)
    results = {}

    for model_name, paths in models.items():
        print(f"\n{'='*60}")
        print(f"MODEL: {model_name}")
        conflict_acts, conflict_labels = load_lang_data(paths["conflict"])
        xnli_acts, xnli_labels = load_lang_data(paths["xnli"])
        n_layers = conflict_acts.shape[1]

        c_train_idx, c_test_idx = train_test_split(
            np.arange(len(conflict_labels)), test_size=0.2, random_state=42, stratify=conflict_labels)
        x_train_idx, x_test_idx = train_test_split(
            np.arange(len(xnli_labels)), test_size=0.2, random_state=42, stratify=xnli_labels)

        model_results = []
        for layer in range(n_layers):
            c_X = conflict_acts[:, layer, :]
            x_X = xnli_acts[:, layer, :]
            c_probe, c_scaler = train_probe(c_X[c_train_idx], conflict_labels[c_train_idx])
            x_probe, x_scaler = train_probe(x_X[x_train_idx], xnli_labels[x_train_idx])

            c_bal = evaluate(c_probe, c_scaler, c_X[c_test_idx], conflict_labels[c_test_idx])
            x_bal = evaluate(x_probe, x_scaler, x_X[x_test_idx], xnli_labels[x_test_idx])
            cx_bal = evaluate(c_probe, c_scaler, x_X[x_test_idx], xnli_labels[x_test_idx])
            xc_bal = evaluate(x_probe, x_scaler, c_X[c_test_idx], conflict_labels[c_test_idx])

            model_results.append({
                "layer": layer,
                "conflict_same": round(c_bal, 4),
                "xnli_same": round(x_bal, 4),
                "conflict_to_xnli": round(cx_bal, 4),
                "xnli_to_conflict": round(xc_bal, 4),
            })
        results[model_name] = model_results

        peak_c2x = max(model_results, key=lambda r: r["conflict_to_xnli"])
        peak_x2c = max(model_results, key=lambda r: r["xnli_to_conflict"])
        print(f"  Peak C->XNLI: layer {peak_c2x['layer']}, bal_acc={peak_c2x['conflict_to_xnli']:.4f}")
        print(f"  Peak X->Conf: layer {peak_x2c['layer']}, bal_acc={peak_x2c['xnli_to_conflict']:.4f}")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
