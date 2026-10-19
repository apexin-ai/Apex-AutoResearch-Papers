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

Dependencies: torch, numpy, sklearn, scipy, matplotlib
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

        results.append({
            "layer": layer,
            "accuracy": round(acc, 4),
            "balanced_accuracy": round(bal_acc, 4),
            "f1": round(f1, 4),
            "p_binomial": round(p_binom, 6),
        })

        if bal_acc > best_bal_acc:
            best_bal_acc = bal_acc
            best_layer = layer

    if run_permutation:
        print(f"  Running permutation test on best layer {best_layer} (bal_acc={best_bal_acc:.4f})...")
        train_X_best = train_data["train_X"][:, best_layer, :].numpy()
        test_X_best = test_data["test_X"][:, best_layer, :].numpy()
        p_perm = permutation_test(
            train_X_best, train_y, test_X_best, test_y, best_bal_acc,
            n_perm=n_perm, rng_seed=seed,
        )
        for r in results:
            r["p_permutation"] = None
        results[best_layer]["p_permutation"] = round(p_perm, 4)
    else:
        for r in results:
            r["p_permutation"] = None

    return results


def get_directions(langs):
    directions = []
    for lang in langs:
        directions.append(f"{lang.upper()}→{lang.upper()}")
    for src in langs:
        for tgt in langs:
            if src != tgt:
                directions.append(f"{src.upper()}→{tgt.upper()}")
    return directions


def run_all_directions(lang_data, num_layers, run_perm, seed, n_perm=1000):
    langs = list(lang_data.keys())
    all_results = {}

    for lang in langs:
        label = f"{lang.upper()}→{lang.upper()}"
        print(f"\n[{label}] Training probes (seed={seed})...")
        all_results[label] = run_direction(
            lang_data[lang], lang_data[lang], num_layers, label, run_perm, seed=seed, n_perm=n_perm)

    for src in langs:
        for tgt in langs:
            if src != tgt:
                label = f"{src.upper()}→{tgt.upper()}"
                print(f"\n[{label}] Training {src.upper()} probes, testing on {tgt.upper()} (seed={seed})...")
                all_results[label] = run_direction(
                    lang_data[src], lang_data[tgt], num_layers, label, run_perm, seed=seed, n_perm=n_perm)

    return all_results


def run_direction_bootstrap(train_data, test_data, num_layers, direction_name, n_bootstrap=20):
    train_X_all = train_data["train_X"].numpy()
    train_y_all = train_data["train_y"].numpy()
    test_X_all = test_data["test_X"].numpy()
    test_y = test_data["test_y"].numpy()
    all_results = []
    for seed in range(n_bootstrap):
        rng = np.random.RandomState(seed)
        idx = rng.choice(len(train_X_all), len(train_X_all), replace=True)
        X_boot = train_X_all[idx]
        y_boot = train_y_all[idx]
        best_bal_acc = 0
        best_result = None
        for layer in range(num_layers):
            scaler = StandardScaler()
            X_tr = scaler.fit_transform(X_boot[:, layer, :])
            X_te = scaler.transform(test_X_all[:, layer, :])
            clf = LogisticRegression(class_weight='balanced', max_iter=1000, solver='lbfgs', random_state=seed)
            clf.fit(X_tr, y_boot)
            y_pred = clf.predict(X_te)
            bal_acc = balanced_accuracy_score(test_y, y_pred)
            if bal_acc > best_bal_acc:
                best_bal_acc = bal_acc
                best_result = {
                    'balanced_accuracy': round(float(bal_acc), 4),
                    'accuracy': round(float(np.mean(y_pred == test_y)), 4),
                    'f1': round(float(f1_score(test_y, y_pred)), 4),
                    'peak_layer': layer,
                }
        all_results.append(best_result)
        print(f"  Bootstrap {seed}: bal_acc={best_result['balanced_accuracy']:.4f} @ L{best_result['peak_layer']}")
    bal_accs = [r['balanced_accuracy'] for r in all_results]
    f1s = [r['f1'] for r in all_results]
    peak_layers = [r['peak_layer'] for r in all_results]
    return {
        'direction': direction_name,
        'n_bootstrap': n_bootstrap,
        'balanced_accuracy_mean': round(float(np.mean(bal_accs)), 4),
        'balanced_accuracy_std': round(float(np.std(bal_accs)), 4),
        'f1_mean': round(float(np.mean(f1s)), 4),
        'f1_std': round(float(np.std(f1s)), 4),
        'peak_layers': peak_layers,
        'per_bootstrap': all_results,
    }


def run_bootstrap_directions(lang_data, num_layers, n_bootstrap):
    langs = list(lang_data.keys())
    results = {}

    for lang in langs:
        label = f"{lang.upper()}→{lang.upper()}"
        print(f"\n[{label}] Bootstrap ({n_bootstrap} seeds)...")
        results[label] = run_direction_bootstrap(
            lang_data[lang], lang_data[lang], num_layers, label, n_bootstrap)

    for src in langs:
        for tgt in langs:
            if src != tgt:
                label = f"{src.upper()}→{tgt.upper()}"
                print(f"\n[{label}] Bootstrap ({n_bootstrap} seeds)...")
                results[label] = run_direction_bootstrap(
                    lang_data[src], lang_data[tgt], num_layers, label, n_bootstrap)

    return results


def print_table(all_results: dict[str, list[dict]], num_layers: int, directions: list[str]):
    header = f"{'Layer':>5}"
    for d in directions:
        header += f"  {d + ' Acc':>12}  {d + ' BAcc':>12}  {d + ' F1':>10}"
    print(header)
    print("-" * len(header))

    for layer in range(num_layers):
        row = f"{layer:>5}"
        for d in directions:
            if d in all_results:
                r = all_results[d][layer]
                row += f"  {r['accuracy']:>12.4f}  {r['balanced_accuracy']:>12.4f}  {r['f1']:>10.4f}"
            else:
                row += f"  {'—':>12}  {'—':>12}  {'—':>10}"
        print(row)


def plot_results(all_results: dict[str, list[dict]], num_layers: int, output_path: str):
    fig, ax = plt.subplots(figsize=(12, 5))
    cmap = plt.cm.tab10

    for i, (direction, results) in enumerate(all_results.items()):
        layers = [r["layer"] for r in results]
        accs = [r["accuracy"] for r in results]
        ax.plot(layers, accs, label=direction, color=cmap(i % 10), linewidth=1.5)

    ax.axhline(y=0.5, color="gray", linestyle="--", linewidth=1, label="Chance (50%)")
    ax.set_xlabel("Layer")
    ax.set_ylabel("Accuracy")
    ax.set_title("Linear Probe Accuracy by Layer")
    ax.legend(fontsize=8)
    ax.set_xlim(0, num_layers - 1)
    ax.set_ylim(0.3, 1.0)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"Saved plot to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Train linear probes on residual stream activations")
    parser.add_argument("--activation_dir", type=str, default="outputs")
    parser.add_argument("--output_dir", type=str, default="outputs")
    parser.add_argument("--n_perm", type=int, default=1000, help="Number of permutation test iterations")
    parser.add_argument("--skip_permutation", action="store_true", help="Skip slow permutation test")
    parser.add_argument('--bootstrap_seeds', type=int, default=0,
                        help='Number of bootstrap resampling runs. 0=disabled.')
    parser.add_argument('--output_file', type=str, default=None,
                        help='Output JSON filename (default: probe_results.json)')
    parser.add_argument("--seeds", type=str, default="42",
                        help='Comma-separated seeds, e.g. "0,1,2,3,4"')
    parser.add_argument("--langs", type=str, default="en,zh",
                        help='Comma-separated language codes, e.g. "en,zh,de"')
    args = parser.parse_args()

    seeds = [int(s) for s in args.seeds.split(',')]
    langs = [l.strip().lower() for l in args.langs.split(",")]

    lang_data = {}
    for lang in langs:
        path = Path(args.activation_dir) / f"{lang}_activations.pt"
        if path.exists():
            lang_data[lang] = load_activations(str(path))
            d = lang_data[lang]
            print(f"Loaded {lang.upper()}: train={d['train_X'].shape[0]}, test={d['test_X'].shape[0]}")
        else:
            print(f"Warning: {path} not found, skipping {lang.upper()}")

    if not lang_data:
        raise FileNotFoundError(f"No activation files found in {args.activation_dir}")

    num_layers = next(iter(lang_data.values()))["train_X"].shape[1]
    print(f"Number of layers: {num_layers}")

    directions = get_directions(list(lang_data.keys()))
    run_perm = not args.skip_permutation

    if args.output_file:
        output_filename = Path(args.output_file).name
    else:
        output_filename = "probe_results.json"

    if args.bootstrap_seeds > 0:
        print(f"\nBOOTSTRAP MODE: {args.bootstrap_seeds} resampling runs (no permutation test)")
        bootstrap_results = run_bootstrap_directions(lang_data, num_layers, args.bootstrap_seeds)

        print(f"\n{'='*60}")
        print("BOOTSTRAP SUMMARY (mean +/- std)")
        print(f"{'='*60}")
        for direction in directions:
            if direction in bootstrap_results:
                s = bootstrap_results[direction]
                print(f"  {direction}: bal_acc={s['balanced_accuracy_mean']:.4f}+/-{s['balanced_accuracy_std']:.4f}, "
                      f"f1={s['f1_mean']:.4f}+/-{s['f1_std']:.4f}, peaks={s['peak_layers']}")

        output = {
            "mode": "bootstrap",
            "n_bootstrap": args.bootstrap_seeds,
            "num_layers": num_layers,
            "langs": list(lang_data.keys()),
            "directions": {d: r for d, r in bootstrap_results.items()},
        }

        json_path = Path(args.output_dir) / output_filename
        with open(json_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nSaved results to {json_path}")
        return

    elif len(seeds) == 1:
        seed = seeds[0]
        np.random.seed(seed)
        all_results = run_all_directions(lang_data, num_layers, run_perm, seed, n_perm=args.n_perm)

        print("\n" + "=" * 60)
        print("Probe Accuracy by Layer")
        print("=" * 60)
        print_table(all_results, num_layers, directions)

        print("\n--- Best layers ---")
        summary = {}
        for direction, results in all_results.items():
            best = max(results, key=lambda r: r["balanced_accuracy"])
            p_str = f", perm_p={best['p_permutation']:.4f}" if best["p_permutation"] is not None else ""
            print(f"  {direction}: layer {best['layer']}, acc={best['accuracy']:.4f}, "
                  f"bal_acc={best['balanced_accuracy']:.4f}, f1={best['f1']:.4f}, "
                  f"binom_p={best['p_binomial']:.6f}{p_str}")
            summary[direction] = {
                "best_layer": best["layer"],
                "best_accuracy": best["accuracy"],
                "best_balanced_accuracy": best["balanced_accuracy"],
                "best_f1": best["f1"],
                "p_binomial": best["p_binomial"],
                "p_permutation": best["p_permutation"],
            }

        output = {
            "per_layer": {d: results for d, results in all_results.items()},
            "summary": summary,
            "num_layers": num_layers,
            "langs": list(lang_data.keys()),
        }

        plot_path = Path(args.output_dir) / "probe_accuracy_by_layer.png"
        plot_results(all_results, num_layers, str(plot_path))

    else:
        per_seed = {}
        all_seed_layer_results = {}

        for seed in seeds:
            print(f"\n{'='*60}")
            print(f"SEED {seed}")
            print(f"{'='*60}")
            np.random.seed(seed)
            all_results = run_all_directions(lang_data, num_layers, run_perm, seed, n_perm=args.n_perm)
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
                print(f"  {direction}: layer {best['layer']}, bal_acc={best['balanced_accuracy']:.4f}, f1={best['f1']:.4f}")
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
        plot_path = Path(args.output_dir) / "probe_accuracy_by_layer.png"
        plot_results(first_results, num_layers, str(plot_path))

    json_path = Path(args.output_dir) / output_filename
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved results to {json_path}")


if __name__ == "__main__":
    main()
