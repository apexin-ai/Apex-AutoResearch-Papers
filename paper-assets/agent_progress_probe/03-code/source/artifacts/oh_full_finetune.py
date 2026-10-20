#!/usr/bin/env python3
"""100% OpenHands fine-tuning of SWE-agent progress probe.

Input:
  - SWE-agent checkpoint: checkpoints/best_model.pt (probe weights to initialize from)
  - OpenHands embeddings: /root/autodl-tmp/openhands_data/embeddings.pt
  - SWE-agent embeddings: data/embeddings.pt (for backward transfer eval)

Output:
  - Fine-tuned checkpoint: checkpoints_oh_full/best_model.pt
  - METRICS_JSON line with oh_100pct_macro_f1, backward transfer metrics
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


def main():
    parser = argparse.ArgumentParser(description="100% OpenHands fine-tuning")
    parser.add_argument("--oh-embeddings", default="/root/autodl-tmp/openhands_data/embeddings.pt")
    parser.add_argument("--swe-checkpoint", default="checkpoints/best_model.pt")
    parser.add_argument("--swe-embeddings", default="data/embeddings.pt")
    parser.add_argument("--output-dir", default="checkpoints_oh_full")
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--patience", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    set_seed(args.seed)
    device = args.device
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # ---- Load SWE-agent checkpoint ----
    print("Loading SWE-agent checkpoint...")
    ckpt = torch.load(args.swe_checkpoint, weights_only=False, map_location="cpu")
    print(f"  embed_dim={ckpt['embed_dim']}, hidden={ckpt['hidden_size']}, layers={ckpt['num_layers']}")

    # ---- Load OpenHands data ----
    print("Loading OpenHands embeddings...")
    oh_data = torch.load(args.oh_embeddings, weights_only=False)
    oh_embeddings = oh_data["embeddings"]
    oh_labels = oh_data["labels"]
    oh_instance_ids = oh_data["instance_ids"]
    n_total = len(oh_labels)
    label_dist = Counter(oh_labels)
    n_unique = len(set(oh_instance_ids))
    print(f"  {n_total} windows, {n_unique} instances, dist={dict(label_dist)}, stag_rate={label_dist[0]/n_total:.4f}")

    # ---- Split by instance (70/15/15) ----
    train_idx, val_idx, test_idx = split_by_instance(oh_instance_ids, seed=args.seed)
    print(f"  Split: train={len(train_idx)}, val={len(val_idx)}, test={len(test_idx)}")

    train_labels = [oh_labels[i] for i in train_idx]
    train_dist = Counter(train_labels)
    print(f"  Train dist: {dict(train_dist)}")

    # pos_weight: match fewshot_probe.py convention for consistent comparison
    n_pos = train_dist.get(1, 0)
    n_neg = train_dist.get(0, 0)
    pw = torch.tensor([n_neg / n_pos], device=device) if n_pos > 0 else torch.tensor([1.0], device=device)
    print(f"  pos_weight={pw.item():.4f}")

    # ---- Build dataloaders ----
    train_ds = WindowDataset([oh_embeddings[i] for i in train_idx], train_labels)
    val_ds = WindowDataset([oh_embeddings[i] for i in val_idx], [oh_labels[i] for i in val_idx])
    test_ds = WindowDataset([oh_embeddings[i] for i in test_idx], [oh_labels[i] for i in test_idx])

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, collate_fn=collate_fn)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False, collate_fn=collate_fn)
    test_loader = DataLoader(test_ds, batch_size=args.batch_size, shuffle=False, collate_fn=collate_fn)

    # ---- Initialize model from SWE-agent checkpoint ----
    model = ProgressProbe(
        embed_dim=ckpt["embed_dim"],
        hidden_size=ckpt["hidden_size"],
        num_layers=ckpt["num_layers"],
        dropout=ckpt.get("dropout", 0.1),
    ).to(device)
    model.load_state_dict(ckpt["model_state_dict"])

    # ---- Zero-shot baseline (before fine-tuning) ----
    print("\nZero-shot (SWE-agent probe on OH test)...")
    zs_metrics = evaluate(model, test_loader, device)
    print(f"  macro_f1={zs_metrics['macro_f1']:.4f}  acc={zs_metrics['accuracy']:.4f}  "
          f"f1_stag={zs_metrics['f1_stagnation']:.4f}  f1_prog={zs_metrics['f1_progress']:.4f}")

    # ---- Fine-tune ----
    print(f"\nFine-tuning on 100% OH train ({len(train_idx)} windows)...")
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pw)

    best_val_f1 = 0.0
    best_state = None
    best_epoch = 0
    wait = 0

    for epoch in range(1, args.epochs + 1):
        model.train()
        total_loss, n_batches = 0.0, 0
        for padded, labels, lengths in train_loader:
            padded, labels = padded.to(device), labels.to(device)
            logits = model(padded, lengths)
            loss = criterion(logits, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            n_batches += 1

        avg_loss = total_loss / n_batches
        val_m = evaluate(model, val_loader, device)
        print(f"  Epoch {epoch:2d}: loss={avg_loss:.4f}  val_macro_f1={val_m['macro_f1']:.4f}  "
              f"val_f1_stag={val_m['f1_stagnation']:.4f}  val_f1_prog={val_m['f1_progress']:.4f}")

        if val_m["macro_f1"] > best_val_f1:
            best_val_f1 = val_m["macro_f1"]
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            best_epoch = epoch
            wait = 0
        else:
            wait += 1
            if wait >= args.patience:
                print(f"  Early stopping at epoch {epoch} (best={best_epoch})")
                break

    # ---- Load best model ----
    model.load_state_dict(best_state)
    model.to(device)

    # ---- Evaluate on OH test ----
    print(f"\nBest model (epoch {best_epoch}) on OH test:")
    oh_test_m = evaluate(model, test_loader, device)
    delta = oh_test_m["macro_f1"] - zs_metrics["macro_f1"]
    print(f"  macro_f1={oh_test_m['macro_f1']:.4f} (delta{delta:+.4f})  "
          f"acc={oh_test_m['accuracy']:.4f}  "
          f"f1_stag={oh_test_m['f1_stagnation']:.4f}  f1_prog={oh_test_m['f1_progress']:.4f}")

    # ---- Backward transfer: evaluate on SWE-agent test set ----
    print("\nBackward transfer: evaluating on SWE-agent test set...")
    swe_data = torch.load(args.swe_embeddings, weights_only=False, map_location="cpu")
    swe_instance_ids = swe_data["instance_ids"]
    _, _, swe_test_idx = split_by_instance(swe_instance_ids, seed=args.seed)
    swe_test_ds = WindowDataset(
        [swe_data["embeddings"][i] for i in swe_test_idx],
        [swe_data["labels"][i] for i in swe_test_idx],
    )
    swe_test_loader = DataLoader(swe_test_ds, batch_size=args.batch_size, shuffle=False, collate_fn=collate_fn)

    # OH-finetuned model on SWE test
    swe_bt_m = evaluate(model, swe_test_loader, device)
    print(f"  OH-finetuned on SWE test: macro_f1={swe_bt_m['macro_f1']:.4f}  "
          f"acc={swe_bt_m['accuracy']:.4f}  "
          f"f1_stag={swe_bt_m['f1_stagnation']:.4f}  f1_prog={swe_bt_m['f1_progress']:.4f}")

    # Original SWE checkpoint on SWE test (reference)
    orig_model = ProgressProbe(
        embed_dim=ckpt["embed_dim"],
        hidden_size=ckpt["hidden_size"],
        num_layers=ckpt["num_layers"],
        dropout=ckpt.get("dropout", 0.1),
    ).to(device)
    orig_model.load_state_dict(ckpt["model_state_dict"])
    swe_orig_m = evaluate(orig_model, swe_test_loader, device)
    bt_delta = swe_bt_m["macro_f1"] - swe_orig_m["macro_f1"]
    print(f"  Original SWE on SWE test:  macro_f1={swe_orig_m['macro_f1']:.4f}")
    print(f"  Backward transfer delta:   {bt_delta:+.4f}")
    del orig_model

    # ---- Save checkpoint ----
    save_path = output_dir / "best_model.pt"
    torch.save({
        "model_state_dict": best_state,
        "embed_dim": ckpt["embed_dim"],
        "hidden_size": ckpt["hidden_size"],
        "num_layers": ckpt["num_layers"],
        "dropout": ckpt.get("dropout", 0.1),
        "best_epoch": best_epoch,
        "oh_test_metrics": oh_test_m,
        "swe_backward_transfer": swe_bt_m,
    }, save_path)
    print(f"\nCheckpoint saved to {save_path}")

    # ---- Summary ----
    print("\n" + "=" * 80)
    print("SUMMARY: 100% OpenHands Fine-tuning")
    print("=" * 80)
    print(f"{'Method':<30} {'Macro-F1':>10} {'Accuracy':>10} {'F1(stag)':>10} {'F1(prog)':>10}")
    print("-" * 70)
    print(f"{'Zero-shot (SWE→OH)':<30} {zs_metrics['macro_f1']:>10.4f} {zs_metrics['accuracy']:>10.4f} "
          f"{zs_metrics['f1_stagnation']:>10.4f} {zs_metrics['f1_progress']:>10.4f}")
    print(f"{'100% OH fine-tuned':<30} {oh_test_m['macro_f1']:>10.4f} {oh_test_m['accuracy']:>10.4f} "
          f"{oh_test_m['f1_stagnation']:>10.4f} {oh_test_m['f1_progress']:>10.4f}")
    print(f"{'Backward (OH→SWE test)':<30} {swe_bt_m['macro_f1']:>10.4f} {swe_bt_m['accuracy']:>10.4f} "
          f"{swe_bt_m['f1_stagnation']:>10.4f} {swe_bt_m['f1_progress']:>10.4f}")
    print(f"{'Original SWE on SWE test':<30} {swe_orig_m['macro_f1']:>10.4f} {swe_orig_m['accuracy']:>10.4f} "
          f"{swe_orig_m['f1_stagnation']:>10.4f} {swe_orig_m['f1_progress']:>10.4f}")

    # ---- METRICS_JSON ----
    metrics = {
        "oh_100pct_macro_f1": round(oh_test_m["macro_f1"], 4),
        "oh_100pct_accuracy": round(oh_test_m["accuracy"], 4),
        "oh_100pct_f1_stag": round(oh_test_m["f1_stagnation"], 4),
        "oh_100pct_f1_prog": round(oh_test_m["f1_progress"], 4),
        "oh_zeroshot_macro_f1": round(zs_metrics["macro_f1"], 4),
        "swe_backward_macro_f1": round(swe_bt_m["macro_f1"], 4),
        "swe_original_macro_f1": round(swe_orig_m["macro_f1"], 4),
        "backward_transfer_delta": round(bt_delta, 4),
        "best_epoch": best_epoch,
        "n_train_windows": len(train_idx),
        "n_oh_instances": n_unique,
    }
    print(f"\nMETRICS_JSON={json.dumps(metrics)}")

    # Save results
    results_path = output_dir / "results.json"
    with open(results_path, "w") as f:
        json.dump({
            "oh_test": oh_test_m,
            "zero_shot": zs_metrics,
            "swe_backward_transfer": swe_bt_m,
            "swe_original": swe_orig_m,
            "meta": {
                "n_total_windows": n_total,
                "n_unique_instances": n_unique,
                "label_dist": dict(label_dist),
                "train_windows": len(train_idx),
                "val_windows": len(val_idx),
                "test_windows": len(test_idx),
                "best_epoch": best_epoch,
                "lr": args.lr,
                "epochs": args.epochs,
                "patience": args.patience,
                "batch_size": args.batch_size,
                "seed": args.seed,
                "pos_weight": pw.item(),
            },
        }, f, indent=2)
    print(f"Results saved to {results_path}")


if __name__ == "__main__":
    main()
