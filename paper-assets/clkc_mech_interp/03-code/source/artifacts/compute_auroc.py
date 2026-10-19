"""Compute AUROC for probes across all models and directions.

Re-trains logistic regression probes and computes AUROC via predict_proba.
Uses the same multi-seed resplit strategy as train_probe.py.
"""

import json
import sys
from pathlib import Path

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


MODELS = {
    "llama31": {"display": "Llama-3.1-8B", "num_layers": 32},
    "gemma2_v2": {"display": "Gemma-2-9B", "num_layers": 42},
    "qwen3": {"display": "Qwen3-8B", "num_layers": 36},
}
SEEDS = [42, 123, 456]
DATA_ROOT = Path("/root/clkc_mech_interp/data")
OUTPUT_PATH = Path("/root/clkc_mech_interp/results/auroc_all_models.json")


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
    """Compute AUROC for one direction across seeds."""
    per_seed = []

    for seed in seeds:
        train_data = resplit(unsplit_train, seed)
        test_data = resplit(unsplit_test, seed)
        train_y = train_data["train_y"].numpy()
        test_y = test_data["test_y"].numpy()

        best_auroc = 0
        best_bal_acc = 0
        best_layer = 0
        layer_results = []

        for layer in range(num_layers):
            tr_X = train_data["train_X"][:, layer, :].numpy()
            te_X = test_data["test_X"][:, layer, :].numpy()
            bal_acc, auroc = compute_layer_metrics(tr_X, train_y, te_X, test_y, seed=seed)
            layer_results.append({"layer": layer, "bal_acc": bal_acc, "auroc": auroc})
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
            "layer_results": layer_results,
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
    results = {}

    for model_key, model_info in MODELS.items():
        print(f"\n{'='*50}")
        print(f"Model: {model_info['display']} ({model_key})")
        print(f"{'='*50}")

        langs_available = []
        unsplit = {}
        for lang in ["en", "zh"]:
            path = DATA_ROOT / model_key / f"{lang}_activations.pt"
            if path.exists():
                unsplit[lang] = load_activations_unsplit(str(path))
                n = unsplit[lang]["X"].shape[0]
                print(f"  Loaded {lang.upper()}: {n} samples, {unsplit[lang]['X'].shape[1]} layers")
                langs_available.append(lang)

        model_results = {}
        # Mono-lingual directions
        for lang in langs_available:
            direction = f"{lang.upper()}→{lang.upper()}"
            print(f"\n  [{direction}] Computing AUROC...")
            model_results[direction] = run_model_direction(
                unsplit[lang], unsplit[lang], model_info["num_layers"], SEEDS
            )
            r = model_results[direction]
            print(f"    AUROC: {r['auroc_mean']:.4f} +/- {r['auroc_std']:.4f}")
            print(f"    Bal Acc: {r['bal_acc_mean']:.4f} +/- {r['bal_acc_std']:.4f}")
            print(f"    Peak layers: {r['peak_layers']}")

        # Cross-lingual directions
        if len(langs_available) > 1:
            for src in langs_available:
                for tgt in langs_available:
                    if src != tgt:
                        direction = f"{src.upper()}→{tgt.upper()}"
                        print(f"\n  [{direction}] Computing AUROC...")
                        model_results[direction] = run_model_direction(
                            unsplit[src], unsplit[tgt], model_info["num_layers"], SEEDS
                        )
                        r = model_results[direction]
                        print(f"    AUROC: {r['auroc_mean']:.4f} +/- {r['auroc_std']:.4f}")
                        print(f"    Bal Acc: {r['bal_acc_mean']:.4f} +/- {r['bal_acc_std']:.4f}")

        results[model_key] = {
            "display_name": model_info["display"],
            "directions": model_results,
        }

    # Print summary table
    print(f"\n\n{'='*70}")
    print(f"{'Model':<18} | {'Direction':<8} | {'AUROC':<12} | {'Balanced Acc':<15}")
    print(f"{'-'*18}-+-{'-'*8}-+-{'-'*12}-+-{'-'*15}")
    for model_key, model_data in results.items():
        for direction, d in model_data["directions"].items():
            auroc_str = f"{d['auroc_mean']:.4f}±{d['auroc_std']:.4f}"
            bacc_str = f"{d['bal_acc_mean']*100:.1f}%±{d['bal_acc_std']*100:.1f}%"
            print(f"{model_data['display_name']:<18} | {direction:<8} | {auroc_str:<12} | {bacc_str:<15}")
    print(f"{'='*70}")

    # Strip per-seed layer_results for the saved JSON (too verbose)
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

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
