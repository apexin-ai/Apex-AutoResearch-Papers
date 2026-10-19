"""
Evaluate trained perturbation classifiers.

Produces confusion matrices, per-class metrics, ROC-AUC (binary mode),
t-SNE/UMAP visualizations, per-layer accuracy breakdown, and sweep
result aggregation tables.

Usage:
    # Evaluate single model
    python eval_classifier.py \
        --model_path ./models/6class__mean__both__lr0.001/best_model.pt \
        --data_dir ./activations \
        --mode 6class \
        --activation_source both \
        --pooling mean \
        --output_dir ./eval_results

    # Aggregate sweep results
    python eval_classifier.py \
        --sweep_results_dir ./models \
        --mode 6class \
        --output_dir ./eval_results

Dependencies:
    torch, scikit-learn, matplotlib, numpy, (optional: umap-learn)
"""

import argparse
import csv
import json
import logging
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
from sklearn.manifold import TSNE
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    roc_auc_score,
    roc_curve,
)
from torch.utils.data import DataLoader, TensorDataset

from configs import (
    ACTIVATION_SOURCES,
    BINARY_NAMES,
    CLASS_3_NAMES,
    CLASS_6_NAMES,
    CLASSIFIER_HIDDEN_DIM,
    EXPERT_LAYERS,
    PALIGEMMA_LAYERS,
    POOLING_STRATEGIES,
    compute_input_dim,
    pooling_output_dim,
    PALIGEMMA_HIDDEN_DIM,
    EXPERT_HIDDEN_DIM,
)
from train_classifier import PerturbationClassifier, load_activation_dataset

log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Evaluation core
# ---------------------------------------------------------------------------

def evaluate_model(
    model: nn.Module,
    X: torch.Tensor,
    y: torch.Tensor,
    mode: str,
    output_dir: Path,
    device: str = "cpu",
) -> dict:
    """Full evaluation: metrics, confusion matrix, visualizations."""
    output_dir.mkdir(parents=True, exist_ok=True)

    model = model.to(device).eval()
    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=256, shuffle=False)

    all_preds = []
    all_probs = []
    with torch.no_grad():
        for X_batch, _ in loader:
            X_batch = X_batch.to(device)
            logits = model(X_batch)
            all_preds.append(logits.argmax(dim=1).cpu())
            all_probs.append(torch.softmax(logits, dim=1).cpu())

    y_pred = torch.cat(all_preds).numpy()
    y_prob = torch.cat(all_probs).numpy()
    y_true = y.numpy()

    class_names = _class_names(mode)

    # Overall metrics
    acc = accuracy_score(y_true, y_pred)
    macro_f1 = f1_score(y_true, y_pred, average="macro")
    report = classification_report(y_true, y_pred, target_names=class_names, output_dict=True)
    log.info("Accuracy: %.4f  Macro-F1: %.4f", acc, macro_f1)

    # Save classification report
    report_text = classification_report(y_true, y_pred, target_names=class_names)
    with open(output_dir / "classification_report.txt", "w") as f:
        f.write(report_text)
    log.info("\n%s", report_text)

    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred, normalize="true")
    _plot_confusion_matrix(cm, class_names, output_dir / "confusion_matrix.png")
    _save_confusion_matrix_csv(cm, class_names, output_dir / "confusion_matrix.csv")

    results = {
        "accuracy": acc,
        "macro_f1": macro_f1,
        "per_class": report,
    }

    # Binary-specific: ROC-AUC + PR curve
    if mode == "binary":
        pos_probs = y_prob[:, 1]
        roc_auc = roc_auc_score(y_true, pos_probs)
        results["roc_auc"] = roc_auc
        log.info("ROC-AUC: %.4f", roc_auc)

        _plot_roc_curve(y_true, pos_probs, roc_auc, output_dir / "roc_curve.png")
        _plot_pr_curve(y_true, pos_probs, output_dir / "pr_curve.png")

    # t-SNE visualization
    _plot_tsne(X.numpy(), y_true, class_names, output_dir / "tsne.png")

    # Save JSON results
    serializable = {k: v for k, v in results.items() if k != "per_class"}
    serializable["per_class"] = {
        k: {kk: float(vv) for kk, vv in v.items()} if isinstance(v, dict) else v
        for k, v in report.items()
    }
    with open(output_dir / "metrics.json", "w") as f:
        json.dump(serializable, f, indent=2)

    return results


# ---------------------------------------------------------------------------
# Per-layer accuracy breakdown
# ---------------------------------------------------------------------------

def per_layer_accuracy(
    data_dir: Path,
    mode: str,
    pooling: str,
    device: str,
    output_dir: Path,
) -> dict[str, float]:
    """Train a separate classifier on each layer individually to find most informative layers."""
    from train_classifier import cross_validate

    num_classes = _num_classes(mode)
    results = {}

    # PaliGemma layers
    for i in PALIGEMMA_LAYERS:
        layer_name = f"paligemma_layer_{i}"
        log.info("Per-layer eval: %s", layer_name)
        try:
            X, y = _load_single_layer(data_dir, mode, layer_name, pooling)
            dim = pooling_output_dim(pooling, PALIGEMMA_HIDDEN_DIM)
            cv = cross_validate(X, y, dim, num_classes, lr=1e-3, epochs=30, device=device)
            results[layer_name] = cv["mean_acc"]
            log.info("  %s: %.4f", layer_name, cv["mean_acc"])
        except Exception:
            log.exception("  Failed for %s", layer_name)

    # Expert layers
    for i in EXPERT_LAYERS:
        layer_name = f"expert_layer_{i}"
        log.info("Per-layer eval: %s", layer_name)
        try:
            X, y = _load_single_layer(data_dir, mode, layer_name, pooling)
            dim = pooling_output_dim(pooling, EXPERT_HIDDEN_DIM)
            cv = cross_validate(X, y, dim, num_classes, lr=1e-3, epochs=30, device=device)
            results[layer_name] = cv["mean_acc"]
            log.info("  %s: %.4f", layer_name, cv["mean_acc"])
        except Exception:
            log.exception("  Failed for %s", layer_name)

    # Plot
    _plot_per_layer(results, output_dir / "per_layer_accuracy.png")

    with open(output_dir / "per_layer_accuracy.json", "w") as f:
        json.dump(results, f, indent=2)

    return results


def _load_single_layer(
    data_dir: Path,
    mode: str,
    layer_name: str,
    pooling: str,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Load activations for a single layer across all episodes."""
    all_features = []
    all_labels = []

    for pt_file in sorted(data_dir.glob("*.pt")):
        is_nominal = pt_file.stem == "nominal"
        if is_nominal and mode != "binary":
            continue

        episodes = torch.load(pt_file, weights_only=False)
        for ep in episodes:
            label = ep[f"label_{mode}"]
            if label == -1 and mode != "binary":
                continue
            feat = ep["activations"][layer_name][pooling].squeeze(0).float()
            all_features.append(feat)
            all_labels.append(label)

    return torch.stack(all_features), torch.tensor(all_labels, dtype=torch.long)


# ---------------------------------------------------------------------------
# Sweep aggregation
# ---------------------------------------------------------------------------

def aggregate_sweep(sweep_dir: Path, mode: str, output_dir: Path) -> None:
    """Aggregate all sweep results into a sorted CSV table."""
    output_dir.mkdir(parents=True, exist_ok=True)
    records = []

    for result_file in sorted(sweep_dir.rglob("result.json")):
        with open(result_file) as f:
            r = json.load(f)
        if r.get("mode") == mode:
            records.append(r)

    if not records:
        log.warning("No sweep results found for mode=%s in %s", mode, sweep_dir)
        return

    records.sort(key=lambda r: r["mean_acc"], reverse=True)

    csv_path = output_dir / f"sweep_leaderboard_{mode}.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "rank", "config_name", "pooling", "activation_source", "lr",
            "mean_acc", "std_acc",
        ])
        writer.writeheader()
        for i, r in enumerate(records):
            writer.writerow({
                "rank": i + 1,
                "config_name": r["config_name"],
                "pooling": r["pooling"],
                "activation_source": r["activation_source"],
                "lr": r["lr"],
                "mean_acc": f"{r['mean_acc']:.4f}",
                "std_acc": f"{r['std_acc']:.4f}",
            })

    log.info("Sweep leaderboard saved to %s (%d configs)", csv_path, len(records))
    for i, r in enumerate(records[:5]):
        log.info("  #%d  %.4f ± %.4f  %s", i + 1, r["mean_acc"], r["std_acc"], r["config_name"])


# ---------------------------------------------------------------------------
# Plotting helpers
# ---------------------------------------------------------------------------

def _plot_confusion_matrix(cm: np.ndarray, class_names: list[str], path: Path) -> None:
    fig, ax = plt.subplots(figsize=(max(6, len(class_names)), max(5, len(class_names) - 1)))
    im = ax.imshow(cm, interpolation="nearest", cmap="Blues")
    ax.set_xticks(range(len(class_names)))
    ax.set_yticks(range(len(class_names)))
    ax.set_xticklabels(class_names, rotation=45, ha="right", fontsize=9)
    ax.set_yticklabels(class_names, fontsize=9)

    for i in range(len(class_names)):
        for j in range(len(class_names)):
            color = "white" if cm[i, j] > 0.5 else "black"
            ax.text(j, i, f"{cm[i, j]:.2f}", ha="center", va="center", color=color, fontsize=10)

    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    ax.set_title("Normalized Confusion Matrix")
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("Confusion matrix saved to %s", path)


def _save_confusion_matrix_csv(cm: np.ndarray, class_names: list[str], path: Path) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([""] + class_names)
        for i, name in enumerate(class_names):
            writer.writerow([name] + [f"{v:.4f}" for v in cm[i]])


def _plot_roc_curve(y_true: np.ndarray, y_prob: np.ndarray, auc: float, path: Path) -> None:
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(fpr, tpr, lw=2, label=f"ROC (AUC={auc:.3f})")
    ax.plot([0, 1], [0, 1], "k--", lw=1)
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curve")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("ROC curve saved to %s", path)


def _plot_pr_curve(y_true: np.ndarray, y_prob: np.ndarray, path: Path) -> None:
    precision, recall, _ = precision_recall_curve(y_true, y_prob)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(recall, precision, lw=2)
    ax.set_xlabel("Recall")
    ax.set_ylabel("Precision")
    ax.set_title("Precision-Recall Curve")
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("PR curve saved to %s", path)


def _plot_tsne(
    X: np.ndarray,
    y: np.ndarray,
    class_names: list[str],
    path: Path,
    max_samples: int = 2000,
) -> None:
    """t-SNE of activation space, colored by perturbation type."""
    if len(X) > max_samples:
        idx = np.random.RandomState(42).choice(len(X), max_samples, replace=False)
        X, y = X[idx], y[idx]

    log.info("Running t-SNE on %d samples...", len(X))
    tsne = TSNE(n_components=2, random_state=42, perplexity=min(30, len(X) - 1))
    emb = tsne.fit_transform(X)

    fig, ax = plt.subplots(figsize=(8, 6))
    unique_labels = sorted(np.unique(y))
    colors = plt.cm.tab10(np.linspace(0, 1, max(len(unique_labels), 2)))

    for label_idx in unique_labels:
        mask = y == label_idx
        name = class_names[label_idx] if label_idx < len(class_names) else str(label_idx)
        ax.scatter(emb[mask, 0], emb[mask, 1], c=[colors[label_idx]], label=name, s=15, alpha=0.7)

    ax.legend(fontsize=8, markerscale=2)
    ax.set_title("t-SNE of Activation Space")
    ax.set_xticks([])
    ax.set_yticks([])
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("t-SNE saved to %s", path)


def _plot_per_layer(results: dict[str, float], path: Path) -> None:
    layers = list(results.keys())
    accs = [results[l] for l in layers]

    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ["#4C72B0" if "paligemma" in l else "#DD8452" for l in layers]
    bars = ax.bar(range(len(layers)), accs, color=colors)
    ax.set_xticks(range(len(layers)))
    ax.set_xticklabels([l.replace("_layer_", " L") for l in layers], rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Accuracy")
    ax.set_title("Per-Layer Classification Accuracy")
    ax.axhline(y=1.0 / max(len(set(accs)), 2), color="gray", linestyle="--", alpha=0.5, label="Chance")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("Per-layer accuracy plot saved to %s", path)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _class_names(mode: str) -> list[str]:
    if mode == "6class":
        return CLASS_6_NAMES
    elif mode == "3class":
        return CLASS_3_NAMES
    elif mode == "binary":
        return BINARY_NAMES
    raise ValueError(f"Unknown mode: {mode}")


def _num_classes(mode: str) -> int:
    if mode == "6class":
        return 6
    elif mode == "3class":
        return 3
    elif mode == "binary":
        return 2
    raise ValueError(f"Unknown mode: {mode}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Evaluate perturbation classifiers and visualize results"
    )
    p.add_argument("--model_path", type=str, help="Path to best_model.pt (single model eval)")
    p.add_argument("--data_dir", type=str, help="Directory with activation .pt files")
    p.add_argument("--mode", type=str, default="6class", choices=["6class", "3class", "binary"])
    p.add_argument("--activation_source", type=str, default="both", choices=ACTIVATION_SOURCES)
    p.add_argument("--pooling", type=str, default="mean", choices=["mean", "first", "last", "first_last"])
    p.add_argument("--output_dir", type=str, default="./eval_results")
    p.add_argument("--device", type=str, default="cpu")
    p.add_argument("--per_layer", action="store_true", help="Run per-layer accuracy breakdown")
    p.add_argument("--sweep_results_dir", type=str, help="Aggregate sweep results from this dir")
    return p.parse_args()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    args = parse_args()
    output_dir = Path(args.output_dir)

    if args.sweep_results_dir:
        aggregate_sweep(Path(args.sweep_results_dir), args.mode, output_dir)

    if args.model_path:
        input_dim = compute_input_dim(args.activation_source, args.pooling)
        num_classes = _num_classes(args.mode)

        model = PerturbationClassifier(input_dim, num_classes)
        state = torch.load(args.model_path, weights_only=True, map_location="cpu")
        model.load_state_dict(state)

        X, y = load_activation_dataset(
            Path(args.data_dir), args.mode, args.activation_source, args.pooling,
        )
        evaluate_model(model, X, y, args.mode, output_dir, args.device)

    if args.per_layer and args.data_dir:
        per_layer_accuracy(
            Path(args.data_dir), args.mode, args.pooling, args.device,
            output_dir,
        )
