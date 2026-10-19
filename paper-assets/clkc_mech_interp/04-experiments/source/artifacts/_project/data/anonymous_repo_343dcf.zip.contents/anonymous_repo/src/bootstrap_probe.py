"""Fast parallel bootstrap probe training using multiprocessing fork (COW shared memory)."""

import argparse
import json
import time
from pathlib import Path
from multiprocessing import get_context

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler

_train_X = None
_train_y = None
_test_X = None
_test_y = None
_num_layers = None


def _init_worker(tx, ty, ex, ey, nl):
    global _train_X, _train_y, _test_X, _test_y, _num_layers
    _train_X, _train_y, _test_X, _test_y, _num_layers = tx, ty, ex, ey, nl


def _one_bootstrap(seed):
    rng = np.random.RandomState(seed)
    idx = rng.choice(len(_train_X), len(_train_X), replace=True)
    X_boot = _train_X[idx]
    y_boot = _train_y[idx]
    best_bal_acc = 0
    best_result = None
    for layer in range(_num_layers):
        scaler = StandardScaler()
        X_tr = scaler.fit_transform(X_boot[:, layer, :])
        X_te = scaler.transform(_test_X[:, layer, :])
        clf = LogisticRegression(class_weight='balanced', max_iter=1000,
                                 solver='lbfgs', random_state=seed)
        clf.fit(X_tr, y_boot)
        y_pred = clf.predict(X_te)
        bal_acc = balanced_accuracy_score(_test_y, y_pred)
        if bal_acc > best_bal_acc:
            best_bal_acc = bal_acc
            best_result = {
                'balanced_accuracy': round(float(bal_acc), 4),
                'accuracy': round(float(np.mean(y_pred == _test_y)), 4),
                'f1': round(float(f1_score(_test_y, y_pred)), 4),
                'peak_layer': layer,
            }
    return best_result


def load_activations(path):
    d = torch.load(path, map_location="cpu", weights_only=True)
    n_train = d["split_sizes"]["train"]
    act = d["activations"]
    if act.dtype == torch.bfloat16:
        act = act.float()
    return {
        "train_X": act[:n_train].numpy(),
        "train_y": d["labels"][:n_train].numpy(),
        "test_X": act[n_train:].numpy(),
        "test_y": d["labels"][n_train:].numpy(),
    }


def run_direction(train_data, test_data, num_layers, direction, n_bootstrap, n_workers):
    print(f"\n[{direction}] Bootstrap ({n_bootstrap} seeds, {n_workers} workers)...", flush=True)
    t0 = time.time()
    ctx = get_context('fork')
    with ctx.Pool(n_workers, initializer=_init_worker,
                  initargs=(train_data["train_X"], train_data["train_y"],
                           test_data["test_X"], test_data["test_y"], num_layers)) as pool:
        results = pool.map(_one_bootstrap, range(n_bootstrap), chunksize=50)
    elapsed = time.time() - t0
    bal_accs = [r['balanced_accuracy'] for r in results]
    f1s = [r['f1'] for r in results]
    summary = {
        'direction': direction,
        'n_bootstrap': n_bootstrap,
        'balanced_accuracy_mean': round(float(np.mean(bal_accs)), 4),
        'balanced_accuracy_std': round(float(np.std(bal_accs)), 4),
        'f1_mean': round(float(np.mean(f1s)), 4),
        'f1_std': round(float(np.std(f1s)), 4),
        'peak_layers': [r['peak_layer'] for r in results],
        'per_bootstrap': results,
    }
    print(f"  {direction}: bal_acc={summary['balanced_accuracy_mean']:.4f}"
          f"+/-{summary['balanced_accuracy_std']:.4f} ({elapsed:.1f}s)", flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--activation_dir", required=True)
    parser.add_argument("--output_file", required=True)
    parser.add_argument("--n_bootstrap", type=int, default=2000)
    parser.add_argument("--n_workers", type=int, default=64)
    args = parser.parse_args()

    en_path = Path(args.activation_dir) / "en_activations.pt"
    zh_path = Path(args.activation_dir) / "zh_activations.pt"
    en_data = load_activations(str(en_path))
    zh_data = load_activations(str(zh_path))
    num_layers = en_data["train_X"].shape[1]
    print(f"Layers: {num_layers}, n_bootstrap: {args.n_bootstrap}", flush=True)

    directions_config = [
        ("EN→EN", en_data, en_data),
        ("ZH→ZH", zh_data, zh_data),
        ("EN→ZH", en_data, zh_data),
        ("ZH→EN", zh_data, en_data),
    ]
    all_results = {}
    for name, train_d, test_d in directions_config:
        all_results[name] = run_direction(train_d, test_d, num_layers, name,
                                          args.n_bootstrap, args.n_workers)

    output = {
        "mode": "bootstrap",
        "n_bootstrap": args.n_bootstrap,
        "num_layers": num_layers,
        "directions": all_results,
    }
    with open(args.output_file, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {args.output_file}", flush=True)


if __name__ == "__main__":
    main()
