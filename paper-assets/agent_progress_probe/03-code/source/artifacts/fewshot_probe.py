#!/usr/bin/env python3
"""Few-shot fine-tuning: adapt SWE-agent probe to OpenHands with limited target data.

Claim 3 experiment: LF-based signals transfer cross-agent, but learned probe
needs agent-specific embedding adaptation. Few-shot fine-tuning on small amounts
of target agent data recovers probe effectiveness.

Label source: majority vote of 3 LFs (file_diff_delta, command_repetition,
outcome_backpropagation). command_repetition is unreliable on OpenHands (71%
false progress on stagnation windows), but file_diff_delta is highly accurate
(macro_f1=0.9582). We use majority_label as-is because:
  - file_diff_delta dominates when it fires (high precision)
  - the claim is about adaptation, not label quality
  - labels are consistent enough for supervised fine-tuning

Class imbalance: OpenHands has 6.6% stagnation vs SWE-agent's 36%.
Handled via pos_weight in BCEWithLogitsLoss.
"""

import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).parent))
from probe_model import ProgressProbe, WindowDataset, collate_fn, split_by_instance


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def compute_metrics(labels: list[int], preds: list[int]) -> dict:
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


@torch.no_grad()
def evaluate(model: nn.Module, loader: DataLoader, device: str) -> dict:
    model.eval()
    all_labels, all_preds = [], []
    for padded, labels, lengths in loader:
        logits = model(padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
        all_labels.extend(labels.long().tolist())
        all_preds.extend(preds.tolist())
    return compute_metrics(all_labels, all_preds)


def subsample_by_instance(
    instance_ids: list[str], indices: list[int], fraction: float, seed: int
) -> tuple[list[int], set[str]]:
    """Subsample a fraction of *instances* (not windows) to maintain instance integrity.

    Instance-level subsampling avoids data leakage: all windows from the same
    SWE-bench task stay in the same split.
    """
    inst_in_split = sorted(set(instance_ids[i] for i in indices))
    rng = random.Random(seed)
    n_keep = max(1, int(len(inst_in_split) * fraction))
    kept = set(rng.sample(inst_in_split, n_keep))
    kept_idx = [i for i in indices if instance_ids[i] in kept]
    return kept_idx, kept


def finetune_one(
    ckpt: dict,
    train_loader: DataLoader,
    val_loader: DataLoader,
    device: str,
    lr: float,
    epochs: int,
    patience: int,
    pos_weight: torch.Tensor,
) -> tuple[dict, dict]:
    """Fine-tune from checkpoint, return (best_state_dict, best_val_metrics)."""
    model = ProgressProbe(
        embed_dim=ckpt["embed_dim"],
        hidden_size=ckpt["hidden_size"],
        num_layers=ckpt["num_layers"],
        dropout=ckpt.get("dropout", 0.1),
    ).to(device)
    model.load_state_dict(ckpt["model_state_dict"])

    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.01)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    best_val_f1 = 0.0
    best_state = None
    best_val_metrics = {}
    wait = 0

    for epoch in range(1, epochs + 1):
        model.train()
        total_loss, n = 0.0, 0
        for padded, batch_labels, lengths in train_loader:
            logits = model(padded.to(device), lengths)
            loss = criterion(logits, batch_labels.to(device))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(batch_labels)
            n += len(batch_labels)

        val_m = evaluate(model, val_loader, device)
        marker = ""
        if val_m["macro_f1"] > best_val_f1:
            best_val_f1 = val_m["macro_f1"]
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            best_val_metrics = val_m
            wait = 0
            marker = " *"
        else:
            wait += 1

        print(
            f"  Epoch {epoch:2d} | loss={total_loss/n:.4f} | "
            f"val_F1={val_m['macro_f1']:.4f} f1_stag={val_m['f1_stagnation']:.4f}{marker}"
        )

        if wait >= patience:
            print(f"  Early stopping at epoch {epoch}")
            break

    return best_state, best_val_metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--oh_data", default="/root/autodl-tmp/openhands_data/embeddings.pt")
    parser.add_argument(
        "--checkpoint",
        default="/root/autodl-tmp/agent_progress_probe/checkpoints/best_model.pt",
    )
    parser.add_argument(
        "--output_dir",
        default="/root/autodl-tmp/agent_progress_probe/fewshot_results",
    )
    parser.add_argument("--device", default="cuda:1")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--fractions", nargs="+", type=float, default=[0.05, 0.10, 0.20, 0.50]
    )
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--patience", type=int, default=3)
    args = parser.parse_args()

    set_seed(args.seed)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    device = args.device if torch.cuda.is_available() else "cpu"

    # ---- Load OpenHands data ----
    print("Loading OpenHands embeddings...")
    data = torch.load(args.oh_data, weights_only=False, map_location="cpu")
    embeddings = data["embeddings"]
    labels = data["labels"]
    instance_ids = data["instance_ids"]
    embed_dim = data["embed_dim"]
    n_total = len(labels)
    label_dist = Counter(labels)
    print(f"Total: {n_total} windows, dist: {dict(label_dist)}")
    print(f"Stagnation rate: {label_dist[0] / n_total * 100:.1f}%")

    # ---- Instance-level split: 70/15/15 ----
    train_idx, val_idx, test_idx = split_by_instance(instance_ids, seed=args.seed)
    n_unique_instances = len(set(instance_ids))
    print(
        f"Split ({n_unique_instances} instances): "
        f"train={len(train_idx)}, val={len(val_idx)}, test={len(test_idx)}"
    )

    # Fixed test/val loaders shared across all conditions
    test_ds = WindowDataset(
        [embeddings[i] for i in test_idx], [labels[i] for i in test_idx]
    )
    test_loader = DataLoader(
        test_ds, batch_size=args.batch_size, collate_fn=collate_fn
    )
    val_ds = WindowDataset(
        [embeddings[i] for i in val_idx], [labels[i] for i in val_idx]
    )
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, collate_fn=collate_fn)

    # ---- Load SWE-agent checkpoint ----
    print(f"\nLoading SWE-agent checkpoint: {args.checkpoint}")
    ckpt = torch.load(args.checkpoint, weights_only=False, map_location="cpu")
    print(
        f"Checkpoint: embed_dim={ckpt['embed_dim']}, hidden={ckpt['hidden_size']}, "
        f"layers={ckpt['num_layers']}, val_f1={ckpt.get('val_macro_f1', 'N/A')}"
    )

    # ---- Zero-shot baseline ----
    print("\n" + "=" * 60)
    print("Zero-shot (SWE-agent probe -> OpenHands, no fine-tuning)")
    print("=" * 60)
    model = ProgressProbe(
        embed_dim=ckpt["embed_dim"],
        hidden_size=ckpt["hidden_size"],
        num_layers=ckpt["num_layers"],
        dropout=ckpt.get("dropout", 0.1),
    ).to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    zs_test = evaluate(model, test_loader, device)
    zs_val = evaluate(model, val_loader, device)
    print(
        f"  TEST:  macro_f1={zs_test['macro_f1']:.4f}  acc={zs_test['accuracy']:.4f}  "
        f"f1_stag={zs_test['f1_stagnation']:.4f}  f1_prog={zs_test['f1_progress']:.4f}"
    )
    del model
    torch.cuda.empty_cache()

    results = {
        "zero_shot": {
            "test_metrics": zs_test,
            "val_metrics": zs_val,
            "n_train_windows": 0,
            "n_instances": 0,
        }
    }

    # ---- Few-shot fine-tuning for each fraction ----
    for frac in sorted(args.fractions):
        print(f"\n{'=' * 60}")
        print(f"Few-shot {frac * 100:.0f}% of OH train data")
        print("=" * 60)
        set_seed(args.seed)

        fs_idx, kept_inst = subsample_by_instance(
            instance_ids, train_idx, frac, args.seed
        )
        fs_labels = [labels[i] for i in fs_idx]
        n_pos = sum(fs_labels)
        n_neg = len(fs_labels) - n_pos
        print(
            f"  {len(fs_idx)} windows from {len(kept_inst)} instances "
            f"(progress={n_pos}, stagnation={n_neg})"
        )

        if n_neg == 0 or n_pos == 0:
            print("  SKIP: single-class subset")
            results[f"fewshot_{frac}"] = {"skipped": True, "reason": "single-class"}
            continue

        # pos_weight: stagnation is label=0, progress is label=1
        # BCEWithLogitsLoss pos_weight upweights label=1; we want to upweight label=0
        # so pos_weight < 1 effectively makes false positives (predicting 1 when 0) costlier
        pw = torch.tensor([n_neg / n_pos]).to(device)
        print(f"  pos_weight={pw.item():.4f}")

        fs_ds = WindowDataset([embeddings[i] for i in fs_idx], fs_labels)
        fs_loader = DataLoader(
            fs_ds, batch_size=args.batch_size, shuffle=True, collate_fn=collate_fn
        )

        best_state, best_val_m = finetune_one(
            ckpt, fs_loader, val_loader, device, args.lr, args.epochs, args.patience, pw
        )

        # Evaluate best model on test
        model = ProgressProbe(
            embed_dim=ckpt["embed_dim"],
            hidden_size=ckpt["hidden_size"],
            num_layers=ckpt["num_layers"],
            dropout=ckpt.get("dropout", 0.1),
        ).to(device)
        model.load_state_dict(best_state)
        model.to(device)
        test_m = evaluate(model, test_loader, device)
        delta = test_m["macro_f1"] - zs_test["macro_f1"]
        print(
            f"  TEST:  macro_f1={test_m['macro_f1']:.4f} (Δ{delta:+.4f})  "
            f"acc={test_m['accuracy']:.4f}  "
            f"f1_stag={test_m['f1_stagnation']:.4f}  f1_prog={test_m['f1_progress']:.4f}"
        )

        results[f"fewshot_{frac}"] = {
            "test_metrics": test_m,
            "val_metrics": best_val_m,
            "n_train_windows": len(fs_idx),
            "n_instances": len(kept_inst),
            "n_pos": n_pos,
            "n_neg": n_neg,
        }

        torch.save(
            {
                "model_state_dict": best_state,
                "embed_dim": ckpt["embed_dim"],
                "hidden_size": ckpt["hidden_size"],
                "num_layers": ckpt["num_layers"],
                "fewshot_fraction": frac,
                "test_metrics": test_m,
            },
            output_dir / f"fewshot_{frac:.2f}_best.pt",
        )
        del model
        torch.cuda.empty_cache()

    # ---- Summary ----
    print("\n" + "=" * 90)
    print("SUMMARY: Few-shot Fine-tuning Results (Claim 3)")
    print("=" * 90)
    print(
        f"SWE-agent in-domain probe macro_f1: 0.9055 (reference)"
    )
    print(
        f"{'Method':<25} {'Macro-F1':>10} {'Accuracy':>10} "
        f"{'F1(stag)':>10} {'F1(prog)':>10} {'#Windows':>10} {'#Instances':>10}"
    )
    print("-" * 95)

    def print_row(name, metrics, n_win, n_inst):
        print(
            f"{name:<25} {metrics['macro_f1']:>10.4f} {metrics['accuracy']:>10.4f} "
            f"{metrics['f1_stagnation']:>10.4f} {metrics['f1_progress']:>10.4f} "
            f"{n_win:>10} {n_inst:>10}"
        )

    print_row("Zero-shot", zs_test, 0, 0)
    for frac in sorted(args.fractions):
        key = f"fewshot_{frac}"
        if key in results and "test_metrics" in results[key]:
            r = results[key]
            print_row(
                f"Few-shot {int(frac * 100)}%",
                r["test_metrics"],
                r["n_train_windows"],
                r["n_instances"],
            )

    # ---- Save results ----
    results["_meta"] = {
        "swe_agent_ref_macro_f1": 0.9055,
        "zero_shot_macro_f1": zs_test["macro_f1"],
        "oh_total_windows": n_total,
        "oh_label_dist": dict(label_dist),
        "oh_stagnation_rate": label_dist[0] / n_total,
        "n_unique_instances": n_unique_instances,
        "train_windows": len(train_idx),
        "val_windows": len(val_idx),
        "test_windows": len(test_idx),
        "lr": args.lr,
        "epochs": args.epochs,
        "patience": args.patience,
        "batch_size": args.batch_size,
        "seed": args.seed,
        "fractions": args.fractions,
        "label_source": "majority_vote of 3 LFs (file_diff_delta, command_repetition, outcome_backpropagation)",
        "note": "command_repetition unreliable on OpenHands (71% false progress on stagnation windows); "
        "file_diff_delta highly accurate (macro_f1=0.9582) but abstains on 58% windows",
    }

    out_path = output_dir / "fewshot_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
