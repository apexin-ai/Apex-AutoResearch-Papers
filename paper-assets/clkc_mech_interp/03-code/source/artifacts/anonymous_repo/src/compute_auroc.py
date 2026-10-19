"""Compute AUROC for probes across all models and directions.

Re-trains logistic regression probes and computes AUROC via predict_proba.
Uses the same multi-seed resplit strategy as train_probe.py.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


SEEDS = [42, 123, 456]


def load_activations_unsplit(path: str) -> dict:
    data = torch.load(path, map_location="cpu", weights_only=True)
    acts = data["activations"]
    if acts.dtype == torch.bfloat16:
        acts = acts.float()
    n_train = data["split_sizes"]["train"]
    n_total = acts.shape[0]
    return {"X": acts, "y": data["labels"], "test_ratio": (n_total - n_train) / n_total}


def resplit(unsplit: dict, seed: int) -> dict:
    n = unsplit["X"].shape[0]
    y_np = unsplit["y"].numpy()
    tr_idx, te_idx = train_test_split(
        np.arange(n), test_size=unsplit["test_ratio"], random_state=seed, stratify=y_np
    )
    return {
        "train_X": unsplit["X"][tr_idx],
        "train_y": unsplit["y"][tr_idx],
        "test_X": unsplit["X"][te_idx],
        "test_y": unsplit["y"][te_idx],
    }


def compute_layer_metrics(train_X, train_y, test_X, test_y, seed=42):
    scaler = StandardScaler()
    train_X = scaler.fit_transform(train_X)
    test_X = scaler.transform(test_X)
    clf = LogisticRegression(
        class_weight="balanced", max_iter=1000, solver="lbfgs", random_state=seed
    )
    clf.fit(train_X, train_y)
    y_pred = clf.predict(test_X)
    y_prob = clf.predict_proba(test_X)[:, 1]
    bal_acc = balanced_accuracy_score(test_y, y_pred)
    auroc = roc_auc_score(test_y, y_prob)
    return bal_acc, auroc


def run_model_direction(unsplit_train, unsplit_test, num_layers, seeds):
    per_seed = []
    for seed in seeds:
        train_data = resplit(unsplit_train, seed)
        test_data = resplit(unsplit_test, seed)
        train_y = train_data["train_y"].numpy()
        test_y = test_data["test_y"].numpy()
        best_auroc = 0
        best_bal_acc = 0
        best_layer = 0
        for layer in range(num_layers):
            tr_X = train_data["train_X"][:, layer, :].numpy()
            te_X = test_data["test_X"][:, layer, :].numpy()
            bal_acc, auroc = compute_layer_metrics(tr_X, train_y, te_X, test_y, seed=seed)
            if auroc > best_auroc:
                best_auroc = auroc
                best_layer = layer
            if bal_acc > best_bal_acc:
                best_bal_acc = bal_acc
        per_seed.append({
            "seed": seed,
            "best_auroc": best_auroc,
            "best_layer": best_layer,
            "best_bal_acc": best_bal_acc,
        })
    aurocs = [s["best_auroc"] for s in per_seed]
    bal_accs = [s["best_bal_acc"] for s in per_seed]
    return {
        "auroc_mean": round(float(np.mean(aurocs)), 4),
        "auroc_std": round(float(np.std(aurocs)), 4),
        "bal_acc_mean": round(float(np.mean(bal_accs)), 4),
        "bal_acc_std": round(float(np.std(bal_accs)), 4),
        "peak_layers": [s["best_layer"] for s in per_seed],
        "per_seed": per_seed,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", type=str, required=True,
                        help='JSON: {"model_key": {"display": "Name", "num_layers": 32, "data_dir": "data/model"}}')
    parser.add_argument("--output", type=str, default="results/auroc_all_models.json")
    parser.add_argument("--seeds", type=str, default="42,123,456")
    args = parser.parse_args()

    models = json.loads(args.models)
    seeds = [int(s) for s in args.seeds.split(",")]
    results = {}

    for model_key, model_info in models.items():
        data_dir = Path(model_info["data_dir"])
        num_layers = model_info["num_layers"]
        print(f"\n{'='*50}")
        print(f"Model: {model_info['display']} ({model_key})")
        print(f"{'='*50}")

        unsplit = {}
        langs_available = []
        for lang in ["en", "zh"]:
            path = data_dir / f"{lang}_activations.pt"
            if path.exists():
                unsplit[lang] = load_activations_unsplit(str(path))
                n = unsplit[lang]["X"].shape[0]
                print(f"  Loaded {lang.upper()}: {n} samples, {unsplit[lang]['X'].shape[1]} layers")
                langs_available.append(lang)

        model_results = {}
        for lang in langs_available:
            direction = f"{lang.upper()}→{lang.upper()}"
            print(f"\n  [{direction}] Computing AUROC...")
            model_results[direction] = run_model_direction(
                unsplit[lang], unsplit[lang], num_layers, seeds
            )
            r = model_results[direction]
            print(f"    AUROC: {r['auroc_mean']:.4f} +/- {r['auroc_std']:.4f}")

        if len(langs_available) > 1:
            for src in langs_available:
                for tgt in langs_available:
                    if src != tgt:
                        direction = f"{src.upper()}→{tgt.upper()}"
                        print(f"\n  [{direction}] Computing AUROC...")
                        model_results[direction] = run_model_direction(
                            unsplit[src], unsplit[tgt], num_layers, seeds
                        )
                        r = model_results[direction]
                        print(f"    AUROC: {r['auroc_mean']:.4f} +/- {r['auroc_std']:.4f}")

        results[model_key] = {
            "display_name": model_info["display"],
            "directions": model_results,
        }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output = {}
    for model_key, model_data in results.items():
        output[model_key] = {
            "display_name": model_data["display_name"],
            "directions": {},
        }
        for direction, d in model_data["directions"].items():
            output[model_key]["directions"][direction] = {
                "auroc_mean": d["auroc_mean"],
                "auroc_std": d["auroc_std"],
                "bal_acc_mean": d["bal_acc_mean"],
                "bal_acc_std": d["bal_acc_std"],
                "peak_layers": d["peak_layers"],
                "per_seed_auroc": [s["best_auroc"] for s in d["per_seed"]],
                "per_seed_bal_acc": [s["best_bal_acc"] for s in d["per_seed"]],
            }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {output_path}")


if __name__ == "__main__":
    main()
