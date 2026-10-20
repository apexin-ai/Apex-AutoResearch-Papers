#!/usr/bin/env python3
"""Evaluate the GRU probe and all baselines on the test set, output comparison table."""

import argparse
import json
import sys
from pathlib import Path

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).parent))
from baselines import (
    ALL_BASELINES,
    CosineSimilarityBaseline,
    RandomBaseline,
    Repeat3Baseline,
    compute_metrics,
)
from probe_model import ProgressProbe, WindowDataset, collate_fn


def parse_row_index(trajectory_id: str) -> int:
    """Extract row_index from trajectory_id 'instance_id__model_name__r{idx}'."""
    return int(trajectory_id.rsplit("__r", 1)[1])


def build_trajectory_index(traj_path: str) -> dict:
    """Map row_index (int) -> list of step dicts."""
    index = {}
    with open(traj_path) as f:
        for row_idx, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            steps = []
            for s in raw.get("trajectory") or []:
                steps.append({
                    "role": s.get("role", "unknown"),
                    "text": s.get("text") or s.get("system_prompt") or "",
                })
            index[row_idx] = steps
    return index


def load_windows(path: str) -> dict:
    """Load windows and index by trajectory_id__w{window_idx}."""
    index = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                w = json.loads(line)
                wid = f"{w['trajectory_id']}__w{w['window_idx']}"
                index[wid] = w
    return index


def build_baseline_data(
    data: dict, indices: list[int], traj_index: dict
) -> list[dict]:
    """Construct baseline-compatible data dicts for given indices."""
    result = []
    for i in indices:
        tid = data["trajectory_ids"][i]
        row_idx = parse_row_index(tid)
        traj_steps = traj_index.get(row_idx, [])

        steps = []
        for si in data["step_indices_list"][i]:
            if si < len(traj_steps):
                steps.append(traj_steps[si])
            else:
                steps.append({"role": "unknown", "text": ""})

        result.append({
            "label": data["labels"][i],
            "embeddings": data["embeddings"][i],
            "steps": steps,
        })
    return result


@torch.no_grad()
def evaluate_probe(model: ProgressProbe, loader: DataLoader, device: str) -> tuple[dict, list[int]]:
    model.eval()
    all_labels, all_preds = [], []
    for padded, labels, lengths in loader:
        logits = model(padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
        all_labels.extend(labels.long().tolist())
        all_preds.extend(preds.tolist())
    return compute_metrics(all_labels, all_preds), all_preds


def print_table(results: list[tuple[str, dict]]):
    header = "| Method | Macro-F1 | Accuracy | Precision | Recall | F1(stag) | F1(prog) |"
    sep = "|" + "|".join(["---"] * 7) + "|"
    print(header)
    print(sep)
    for name, m in results:
        print(
            f"| {name:20s} | {m['macro_f1']:.4f}   | {m['accuracy']:.4f}   | "
            f"{m['precision_macro']:.4f}    | {m['recall_macro']:.4f} | "
            f"{m['f1_stagnation']:.4f}   | {m['f1_progress']:.4f}   |"
        )


def main():
    parser = argparse.ArgumentParser(description="Evaluate probe + baselines on test set")
    parser.add_argument("--data_dir", required=True, help="Directory containing embeddings.pt")
    parser.add_argument("--checkpoint", required=True, help="Path to best_model.pt")
    parser.add_argument("--split_info", required=True, help="Path to split_info.json")
    parser.add_argument("--trajectories", required=True, help="Path to original trajectories JSONL")
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--device", default=None)
    args = parser.parse_args()

    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")

    # Load embeddings data
    data = torch.load(Path(args.data_dir) / "embeddings.pt", weights_only=False)

    # Apply same confidence filter used during training
    with open(args.split_info) as f:
        split_info = json.load(f)

    keep_indices = split_info.get("keep_indices")
    if keep_indices is not None:
        min_conf = split_info.get("min_confidence", 0)
        print(f"Applying confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(data['labels'])} windows")
        data = {
            "embeddings": [data["embeddings"][i] for i in keep_indices],
            "labels": [data["labels"][i] for i in keep_indices],
            "trajectory_ids": [data["trajectory_ids"][i] for i in keep_indices],
            "instance_ids": [data["instance_ids"][i] for i in keep_indices],
            "step_indices_list": [data["step_indices_list"][i] for i in keep_indices],
            "confidences": [data["confidences"][i] for i in keep_indices],
        }

    train_idx = split_info["train_indices"]
    val_idx = split_info["val_indices"]
    test_idx = split_info["test_indices"]

    print(f"Test set: {len(test_idx)} windows")

    # ── Probe evaluation ──
    ckpt = torch.load(args.checkpoint, weights_only=False)
    model = ProgressProbe(
        embed_dim=ckpt["embed_dim"],
        hidden_size=ckpt["hidden_size"],
        num_layers=ckpt["num_layers"],
    ).to(device)
    model.load_state_dict(ckpt["model_state_dict"])

    test_ds = WindowDataset(
        [data["embeddings"][i] for i in test_idx],
        [data["labels"][i] for i in test_idx],
    )
    test_loader = DataLoader(test_ds, batch_size=args.batch_size, collate_fn=collate_fn)
    probe_metrics, _ = evaluate_probe(model, test_loader, device)

    # ── Baseline evaluation ──
    print("Loading trajectory data for baselines ...")
    traj_index = build_trajectory_index(args.trajectories)

    train_bl = build_baseline_data(data, train_idx, traj_index)
    val_bl = build_baseline_data(data, val_idx, traj_index)
    test_bl = build_baseline_data(data, test_idx, traj_index)

    results = [("GRU Probe", probe_metrics)]

    for cls in ALL_BASELINES:
        bl = cls()
        bl.fit(train_bl, val_bl)
        metrics = bl.evaluate(test_bl)
        results.append((bl.name, metrics))

    # ── Output ──
    print()
    print_table(results)

    # Best baseline comparison
    baseline_results = results[1:]
    best_bl_name, best_bl_m = max(baseline_results, key=lambda x: x[1]["macro_f1"])
    delta = probe_metrics["macro_f1"] - best_bl_m["macro_f1"]
    pct = (delta / best_bl_m["macro_f1"] * 100) if best_bl_m["macro_f1"] > 0 else float("inf")

    print(f"\nBest baseline: {best_bl_name} (Macro-F1: {best_bl_m['macro_f1']:.4f})")
    print(f"GRU Probe improvement: {delta:+.4f} ({pct:+.1f}%)")


if __name__ == "__main__":
    main()
