"""Random Labels Selectivity Control.

For each model's best probe layer, train probes with permuted labels
to establish chance-level baseline. Selectivity = real_acc - permuted_acc.
"""

import json
from pathlib import Path

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.preprocessing import StandardScaler


MODELS = {
    "Llama-3.1-8B": {
        "path": "data/llama31/en_activations.pt",
        "best_layer": 13,
    },
    "Gemma-2-9B-IT": {
        "path": "data/gemma2_v2/en_activations.pt",
        "best_layer": 17,
    },
    "Qwen3-8B": {
        "path": "data/qwen3/en_activations.pt",
        "best_layer": 14,
    },
}

PERMUTATION_SEEDS = [0, 1, 2, 3, 4]
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_layer_data(pt_path: str, layer: int) -> dict:
    data = torch.load(pt_path, map_location="cpu", weights_only=True)
    acts = data["activations"]
    if acts.dtype == torch.bfloat16:
        acts = acts.float()
    n_train = data["split_sizes"]["train"]
    return {
        "train_X": acts[:n_train, layer, :].numpy(),
        "train_y": data["labels"][:n_train].numpy(),
        "test_X": acts[n_train:, layer, :].numpy(),
        "test_y": data["labels"][n_train:].numpy(),
    }


def train_probe(train_X, train_y, test_X, test_y, random_state=42):
    scaler = StandardScaler()
    train_X = scaler.fit_transform(train_X)
    test_X = scaler.transform(test_X)
    clf = LogisticRegression(
        class_weight="balanced", max_iter=1000, solver="lbfgs",
        random_state=random_state,
    )
    clf.fit(train_X, train_y)
    y_pred = clf.predict(test_X)
    return balanced_accuracy_score(test_y, y_pred)


def main():
    results = {}

    print(f"{'Model':<16}| {'Real BA':>8} | {'Permuted BA (mean±std)':>23} | {'Selectivity':>12}")
    print("-" * 68)

    for model_name, cfg in MODELS.items():
        pt_path = str(PROJECT_ROOT / cfg["path"])
        layer = cfg["best_layer"]
        d = load_layer_data(pt_path, layer)

        real_ba = train_probe(d["train_X"], d["train_y"], d["test_X"], d["test_y"])

        perm_bas = []
        for seed in PERMUTATION_SEEDS:
            rng = np.random.RandomState(seed)
            perm_y = rng.permutation(d["train_y"])
            ba = train_probe(d["train_X"], perm_y, d["test_X"], d["test_y"],
                             random_state=seed)
            perm_bas.append(ba)

        mean_perm = np.mean(perm_bas)
        std_perm = np.std(perm_bas)
        selectivity = real_ba - mean_perm

        print(f"{model_name:<16}| {real_ba*100:>6.1f}% | {mean_perm*100:>5.1f}% ± {std_perm*100:>4.1f}%"
              f"             | {selectivity*100:>5.1f} pp")

        results[model_name] = {
            "best_layer": layer,
            "real_balanced_accuracy": round(real_ba, 4),
            "permuted_balanced_accuracies": [round(b, 4) for b in perm_bas],
            "permuted_mean": round(float(mean_perm), 4),
            "permuted_std": round(float(std_perm), 4),
            "selectivity_pp": round(selectivity * 100, 1),
        }

    out_dir = PROJECT_ROOT / "results"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "random_labels_selectivity.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
