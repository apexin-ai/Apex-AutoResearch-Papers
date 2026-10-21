"""Train per-layer linear probes and evaluate cross-lingual transfer.

Loads .pt activation files from collect_activations.py, trains a logistic
regression probe per layer, and evaluates on all mono-/cross-lingual
transfer directions for the specified languages.

Statistical tests:
  - Binomial test: is each accuracy significantly above chance (50%)?
  - Permutation test (1000 iters): is the layer-wise peak accuracy above noise?

Output:
  - Console table with per-layer accuracy + p-values
  - probe_results.json   (structured results)
  - probe_accuracy_by_layer.png  (visualization)
"""

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_activations(path: str) -> dict:
    data = torch.load(path, map_location="cpu", weights_only=True)
    n_train = data["split_sizes"]["train"]
    acts = data["activations"]
    if acts.dtype == torch.bfloat16:
        acts = acts.float()
    return {
        "train_X": acts[:n_train],
        "train_y": data["labels"][:n_train],
        "test_X": acts[n_train:],
        "test_y": data["labels"][n_train:],
    }


def load_activations_unsplit(path: str) -> dict:
    data = torch.load(path, map_location="cpu", weights_only=True)
    acts = data["activations"]
    if acts.dtype == torch.bfloat16:
        acts = acts.float()
    n_train = data["split_sizes"]["train"]
    n_total = acts.shape[0]
    return {"X": acts, "y": data["labels"], "test_ratio": (n_total - n_train) / n_total}


def resplit_data(unsplit: dict, seed: int) -> dict:
    n = unsplit["X"].shape[0]
    indices = np.arange(n)
    y_np = unsplit["y"].numpy()
    tr_idx, te_idx = train_test_split(
        indices, test_size=unsplit["test_ratio"], random_state=seed, stratify=y_np)
    return {
        "train_X": unsplit["X"][tr_idx],
        "train_y": unsplit["y"][tr_idx],
        "test_X": unsplit["X"][te_idx],
        "test_y": unsplit["y"][te_idx],
    }


def train_and_eval(
    train_X: np.ndarray,
    train_y: np.ndarray,
    test_X: np.ndarray,
    test_y: np.ndarray,
    random_state: int = 42,
) -> tuple[float, float, float]:
    scaler = StandardScaler()
    train_X = scaler.fit_transform(train_X)
    test_X = scaler.transform(test_X)
    clf = LogisticRegression(
        class_weight='balanced', max_iter=1000, solver="lbfgs",
        random_state=random_state,
    )
    clf.fit(train_X, train_y)
    y_pred = clf.predict(test_X)
    acc = float(np.mean(y_pred == test_y))
    bal_acc = balanced_accuracy_score(test_y, y_pred)
    f1 = f1_score(test_y, y_pred)
    return acc, bal_acc, f1


def binomial_p(accuracy: float, n: int, chance: float = 0.5) -> float:
    k = int(round(accuracy * n))
    return stats.binomtest(k, n, chance, alternative="greater").pvalue


def permutation_test(
    train_X: np.ndarray,
    train_y: np.ndarray,
    test_X: np.ndarray,
    test_y: np.ndarray,
    observed_bal_acc: float,
    n_perm: int = 1000,
    rng_seed: int = 42,
) -> float:
    rng = np.random.RandomState(rng_seed)
    count = 0
    for _ in range(n_perm):
        perm_y = rng.permutation(train_y)
        _, bal_acc, _ = train_and_eval(train_X, perm_y, test_X, test_y, random_state=rng_seed)
        if bal_acc >= observed_bal_acc:
            count += 1
    return count / n_perm


def run_direction(
    train_data: dict,
    test_data: dict,
    num_layers: int,
    direction_name: str,
    run_permutation: bool = True,
    seed: int = 42,
    n_perm: int = 1000,
) -> list[dict]:
    train_y = train_data["train_y"].numpy()
    test_y = test_data["test_y"].numpy()
    n_test = len(test_y)

    results = []
    best_bal_acc, best_layer = 0.0, 0

    for layer in range(num_layers):
        train_X = train_data["train_X"][:, layer, :].numpy()
        test_X = test_data["test_X"][:, layer, :].numpy()

        acc, bal_acc, f1 = train_and_eval(train_X, train_y, test_X, test_y, random_state=seed)
        p_binom = binomial_p(acc, n_test)

        result = {
            "layer": layer,
            "accuracy": round(acc, 4),
            "balanced_accuracy": round(bal_acc, 4),
            "f1": round(f1, 4),
            "p_binomial": round(p_binom, 6),
            "p_permutation": None,
        }
        results.append(result)

        if bal_acc > best_bal_acc:
            best_bal_acc = bal_acc
            best_layer = layer

    if run_permutation:
        train_X = train_data["train_X"][:, best_layer, :].numpy()
        test_X = test_data["test_X"][:, best_layer, :].numpy()
        p_perm = permutation_test(train_X, train_y, test_X, test_y, best_bal_acc, n_perm, seed)
        results[best_layer]["p_permutation"] = round(p_perm, 6)
        print(f"  [{direction_name}] Best layer {best_layer}: bal_acc={best_bal_acc:.4f}, "
              f"p_perm={p_perm:.4f}")

    return results


def run_all_directions(lang_data, num_layers, run_perm=True, seed=42, n_perm=1000):
    all_results = {}
    langs = list(lang_data.keys())

    for src in langs:
        for tgt in langs:
            direction = f"{src.upper()}→{tgt.upper()}"
            print(f"\n[{direction}]")
            all_results[direction] = run_direction(
                lang_data[src], lang_data[tgt], num_layers, direction,
                run_permutation=run_perm, seed=seed, n_perm=n_perm,
            )
    return all_results


def print_table(all_results, num_layers, directions):
    header = f"{'Layer':>5}"
    for d in directions:
        header += f" | {d:>12}"
    print(header)
    print("-" * len(header))
    for layer in range(num_layers):
        row = f"{layer:5d}"
        for d in directions:
            if d in all_results:
                ba = all_results[d][layer]["balanced_accuracy"]
                row += f" | {ba:12.4f}"
            else:
                row += f" | {'':>12}"
        print(row)


def plot_results(all_results, num_layers, save_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    for direction, results in all_results.items():
        layers = [r["layer"] for r in results]
        accs = [r["balanced_accuracy"] for r in results]
        ax.plot(layers, accs, "o-", label=direction, markersize=3)
    ax.axhline(y=0.5, color="gray", linestyle="--", alpha=0.5, label="Chance")
    ax.set_xlabel("Layer")
    ax.set_ylabel("Balanced Accuracy")
    ax.set_title("Probe Accuracy by Layer")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"Plot saved to {save_path}")


def main():
    parser = argparse.ArgumentParser(description="Train per-layer linear probes")
    parser.add_argument("--activation_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--seeds", type=str, default=None,
                        help="Comma-separated seeds for multi-seed mode")
    parser.add_argument("--skip_permutation", action="store_true")
    parser.add_argument("--n_perm", type=int, default=1000)
    parser.add_argument("--output_filename", type=str, default="probe_results.json")
    args = parser.parse_args()

    output_dir = args.output_dir or args.activation_dir
    output_filename = args.output_filename
    run_perm = not args.skip_permutation

    langs = []
    lang_data = {}
    for lang in ["en", "zh", "de"]:
        path = Path(args.activation_dir) / f"{lang}_activations.pt"
        if path.exists():
            lang_data[lang] = load_activations(str(path))
            langs.append(lang)
            d = lang_data[lang]
            print(f"Loaded {lang.upper()}: train={d['train_X'].shape[0]}, test={d['test_X'].shape[0]}")

    if not langs:
        raise FileNotFoundError(f"No activation files found in {args.activation_dir}")

    num_layers = lang_data[langs[0]]["train_X"].shape[1]
    print(f"Number of layers: {num_layers}")

    directions = []
    for src in langs:
        for tgt in langs:
            directions.append(f"{src.upper()}→{tgt.upper()}")

    seeds = [int(s) for s in args.seeds.split(",")] if args.seeds else None

    if seeds is None:
        all_results = run_all_directions(lang_data, num_layers, run_perm)
        print_table(all_results, num_layers, directions)

        output = {
            "per_layer": {d: results for d, results in all_results.items()},
            "num_layers": num_layers,
            "langs": list(lang_data.keys()),
        }

        plot_path = Path(output_dir) / "probe_accuracy_by_layer.png"
        plot_results(all_results, num_layers, str(plot_path))
    else:
        lang_unsplit = {}
        for lang in langs:
            upath = Path(args.activation_dir) / f"{lang}_activations.pt"
            if upath.exists():
                lang_unsplit[lang] = load_activations_unsplit(str(upath))
                print(f"Loaded {lang.upper()} unsplit: {lang_unsplit[lang]['X'].shape[0]} samples")

        per_seed = {}
        all_seed_layer_results = {}

        for seed in seeds:
            print(f"\n{'='*60}")
            print(f"SEED {seed}")
            print(f"{'='*60}")
            np.random.seed(seed)
            lang_data_seed = {}
            for lang, unsplit in lang_unsplit.items():
                lang_data_seed[lang] = resplit_data(unsplit, seed)
                d = lang_data_seed[lang]
                print(f"  {lang.upper()}: train={d['train_X'].shape[0]}, test={d['test_X'].shape[0]}")
            all_results = run_all_directions(lang_data_seed, num_layers, run_perm, seed, n_perm=args.n_perm)
            all_seed_layer_results[seed] = all_results

            print_table(all_results, num_layers, directions)

            seed_summary = {}
            for direction, results in all_results.items():
                best = max(results, key=lambda r: r["balanced_accuracy"])
                seed_summary[direction] = {
                    "balanced_accuracy": best["balanced_accuracy"],
                    "f1": best["f1"],
                    "accuracy": best["accuracy"],
                    "peak_layer": best["layer"],
                    "p_binomial": best["p_binomial"],
                    "p_permutation": best["p_permutation"],
                }
            per_seed[str(seed)] = seed_summary

        summary = {}
        directions_seen = set()
        for s in per_seed.values():
            directions_seen.update(s.keys())

        for direction in directions:
            if direction not in directions_seen:
                continue
            bal_accs = [per_seed[str(s)][direction]["balanced_accuracy"] for s in seeds]
            f1s = [per_seed[str(s)][direction]["f1"] for s in seeds]
            accs = [per_seed[str(s)][direction]["accuracy"] for s in seeds]
            peak_layers = [per_seed[str(s)][direction]["peak_layer"] for s in seeds]

            summary[direction] = {
                "balanced_accuracy_mean": round(float(np.mean(bal_accs)), 4),
                "balanced_accuracy_std": round(float(np.std(bal_accs)), 4),
                "f1_mean": round(float(np.mean(f1s)), 4),
                "f1_std": round(float(np.std(f1s)), 4),
                "accuracy_mean": round(float(np.mean(accs)), 4),
                "accuracy_std": round(float(np.std(accs)), 4),
                "peak_layers": peak_layers,
            }

        print(f"\n{'='*60}")
        print("SUMMARY (mean +/- std across seeds)")
        print(f"{'='*60}")
        for direction, s in summary.items():
            print(f"  {direction}: bal_acc={s['balanced_accuracy_mean']:.4f}+/-{s['balanced_accuracy_std']:.4f}, "
                  f"f1={s['f1_mean']:.4f}+/-{s['f1_std']:.4f}, peaks={s['peak_layers']}")

        output = {
            "per_seed": per_seed,
            "summary": summary,
            "num_layers": num_layers,
            "seeds": seeds,
            "langs": list(lang_data.keys()),
        }

        first_results = all_seed_layer_results[seeds[0]]
        plot_path = Path(output_dir) / "probe_accuracy_by_layer.png"
        plot_results(first_results, num_layers, str(plot_path))

    json_path = Path(output_dir) / output_filename
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved results to {json_path}")


if __name__ == "__main__":
    main()
