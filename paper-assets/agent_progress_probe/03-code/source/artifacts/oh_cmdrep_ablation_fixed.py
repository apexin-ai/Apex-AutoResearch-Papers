#!/usr/bin/env python3
"""Ablation: remove command_repetition LF from OpenHands labeling (FIXED data).

Uses embeddings_fixed.pt (stag_rate ≈ 21.45%) instead of the buggy embeddings.pt.
Compares 3-LF vs 2-LF (no cmd_rep) on both zero-shot and fine-tuned probes.
"""

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
from probe_model import ProgressProbe, WindowDataset, collate_fn


def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


def relabel_2lf(file_diff, outcome_bp, min_conf=2):
    votes = [v for v in [file_diff, outcome_bp] if v != -1]
    if len(votes) == 0:
        return -1, 0
    if len(votes) == 2:
        if votes[0] == votes[1]:
            return votes[0], 2
        return -1, 0
    if min_conf <= 1:
        return votes[0], 1
    return -1, 1


def split_by_trajectory(tids, seed=42, train_ratio=0.7, val_ratio=0.15):
    unique = sorted(set(tids))
    rng = random.Random(seed)
    rng.shuffle(unique)
    n = len(unique)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)
    train_set = set(unique[:n_train])
    val_set = set(unique[n_train:n_train + n_val])
    train_idx, val_idx, test_idx = [], [], []
    for i, tid in enumerate(tids):
        if tid in train_set:
            train_idx.append(i)
        elif tid in val_set:
            val_idx.append(i)
        else:
            test_idx.append(i)
    return train_idx, val_idx, test_idx


@torch.no_grad()
def evaluate_model(model, loader, device):
    model.eval()
    all_labels, all_preds = [], []
    for padded, labels, lengths in loader:
        logits = model(padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
        all_labels.extend(labels.long().tolist())
        all_preds.extend(preds.tolist())
    return compute_metrics(all_labels, all_preds)


def train_probe(data, ckpt_path, device, embed_dim, output_dir, tag=""):
    set_seed(42)
    train_idx, val_idx, test_idx = split_by_trajectory(data["trajectory_ids"], seed=42)
    print(f"  Split: train={len(train_idx)}, val={len(val_idx)}, test={len(test_idx)}")

    def make_ds(indices):
        return WindowDataset(
            [data["embeddings"][i] for i in indices],
            [data["labels"][i] for i in indices],
        )

    train_ds, val_ds, test_ds = make_ds(train_idx), make_ds(val_idx), make_ds(test_idx)
    test_loader = DataLoader(test_ds, batch_size=64, shuffle=False, collate_fn=collate_fn)
    val_loader = DataLoader(val_ds, batch_size=64, shuffle=False, collate_fn=collate_fn)
    train_loader = DataLoader(train_ds, batch_size=32, shuffle=True, collate_fn=collate_fn)

    ckpt = torch.load(ckpt_path, weights_only=False, map_location=device)
    hidden_size = ckpt.get("hidden_size", 256)
    num_layers = ckpt.get("num_layers", 2)
    dropout = ckpt.get("dropout", 0.1)

    # --- Zero-shot ---
    print(f"\n  --- Zero-shot{tag} ---")
    model = ProgressProbe(embed_dim=embed_dim, hidden_size=hidden_size,
                          num_layers=num_layers, dropout=dropout).to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    zs_metrics = evaluate_model(model, test_loader, device)
    print(f"  macro_f1={zs_metrics['macro_f1']:.4f}, f1_stag={zs_metrics['f1_stagnation']:.4f}, "
          f"f1_prog={zs_metrics['f1_progress']:.4f}")

    full_loader = DataLoader(
        WindowDataset(data["embeddings"], data["labels"]),
        batch_size=64, shuffle=False, collate_fn=collate_fn)
    zs_full = evaluate_model(model, full_loader, device)
    print(f"  Zero-shot (full): macro_f1={zs_full['macro_f1']:.4f}")

    # --- Fine-tune ---
    print(f"\n  --- Fine-tune{tag} ---")
    model = ProgressProbe(embed_dim=embed_dim, hidden_size=hidden_size,
                          num_layers=num_layers, dropout=dropout).to(device)
    model.load_state_dict(ckpt["model_state_dict"])

    train_labels = [data["labels"][i] for i in train_idx]
    n_pos = sum(train_labels)
    n_neg = len(train_labels) - n_pos
    pos_weight = torch.tensor([n_neg / max(n_pos, 1)], device=device)
    print(f"  {n_neg} stag, {n_pos} prog, pos_weight={pos_weight.item():.2f}")

    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4, weight_decay=0.01)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    best_val_f1, patience_ctr = 0.0, 0

    ckpt_file = output_dir / "best_model.pt"
    for epoch in range(1, 21):
        model.train()
        total_loss, n_samp = 0.0, 0
        for padded, bl, lengths in train_loader:
            logits = model(padded.to(device), lengths)
            loss = criterion(logits, bl.to(device))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(bl)
            n_samp += len(bl)

        avg_loss = total_loss / n_samp
        vm = evaluate_model(model, val_loader, device)
        is_best = vm["macro_f1"] > best_val_f1
        if is_best:
            best_val_f1 = vm["macro_f1"]
            patience_ctr = 0
            torch.save({
                "model_state_dict": model.state_dict(),
                "embed_dim": embed_dim, "hidden_size": hidden_size,
                "num_layers": num_layers, "dropout": dropout,
                "epoch": epoch, "val_macro_f1": best_val_f1,
            }, ckpt_file)
        else:
            patience_ctr += 1

        mark = " *" if is_best else ""
        print(f"  Epoch {epoch:2d} | loss={avg_loss:.4f} | val_F1={vm['macro_f1']:.4f} "
              f"f1_stag={vm['f1_stagnation']:.4f}{mark}")

        if patience_ctr >= 5:
            print(f"  Early stop at epoch {epoch}")
            break

    best_ckpt = torch.load(ckpt_file, weights_only=False, map_location=device)
    model.load_state_dict(best_ckpt["model_state_dict"])
    ft_metrics = evaluate_model(model, test_loader, device)
    print(f"\n  Fine-tuned test: macro_f1={ft_metrics['macro_f1']:.4f}, "
          f"f1_stag={ft_metrics['f1_stagnation']:.4f}, f1_prog={ft_metrics['f1_progress']:.4f}")

    return {
        "splits": {"train": len(train_idx), "val": len(val_idx), "test": len(test_idx)},
        "zero_shot_test": {k: round(v, 4) for k, v in zs_metrics.items()},
        "zero_shot_full": {k: round(v, 4) for k, v in zs_full.items()},
        "fine_tuned_test": {k: round(v, 4) for k, v in ft_metrics.items()},
        "best_epoch": best_ckpt["epoch"],
        "best_val_f1": round(best_val_f1, 4),
    }


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda:1")
    args = parser.parse_args()

    set_seed(42)
    device = args.device if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    oh_dir = Path("/root/autodl-tmp/openhands_data")
    proj_dir = Path("/root/autodl-tmp/agent_progress_probe")
    swe_ckpt = proj_dir / "checkpoints_full" / "best_model.pt"
    output_dir = proj_dir / "checkpoints_oh_nocmdrep_fixed"
    output_dir.mkdir(exist_ok=True)

    # ===== Step 0: Load & verify fixed embeddings =====
    print("\n" + "=" * 60)
    print("Step 0: Verify fixed embeddings")
    print("=" * 60)

    emb_data = torch.load(oh_dir / "embeddings_fixed.pt", weights_only=False, map_location="cpu")
    embeddings = emb_data["embeddings"]
    old_labels = emb_data["labels"]
    trajectory_ids = emb_data["trajectory_ids"]
    instance_ids = emb_data["instance_ids"]
    embed_dim = emb_data["embed_dim"]
    n_total = len(embeddings)
    old_dist = Counter(old_labels)
    stag_rate = old_dist[0] / n_total * 100

    print(f"Total windows: {n_total}")
    print(f"3-LF distribution: {dict(old_dist)}")
    print(f"3-LF stag rate: {stag_rate:.2f}%")
    assert 20 < stag_rate < 23, f"Unexpected stag rate {stag_rate:.2f}%, expected ~21.45%"
    print("VERIFIED: stag rate ≈ 21.45%")

    # ===== Step 1: Re-label without command_repetition =====
    print("\n" + "=" * 60)
    print("Step 1: Re-label without command_repetition")
    print("=" * 60)

    all_windows = []
    with open(oh_dir / "windows_labeled.jsonl") as f:
        for line in f:
            line = line.strip()
            if line:
                all_windows.append(json.loads(line))

    usable_windows = [w for w in all_windows if w.get("majority_label", -1) != -1]
    print(f"Total windows: {len(all_windows)}, Usable (3-LF): {len(usable_windows)}")
    assert len(usable_windows) == n_total, \
        f"Mismatch: {len(usable_windows)} usable vs {n_total} embeddings"

    # Verify alignment
    n_check = min(200, len(usable_windows))
    for i in range(n_check):
        assert usable_windows[i]["trajectory_id"] == trajectory_ids[i], \
            f"Alignment mismatch at {i}"
    print(f"Alignment verified (first {n_check})")

    # LF coverage analysis
    for lf in ["file_diff_delta", "command_repetition", "outcome_backpropagation"]:
        n_active = sum(1 for w in usable_windows if w["labels"][lf] != -1)
        print(f"  {lf}: {n_active}/{n_total} ({n_active/n_total*100:.1f}%)")

    # cmd_rep false positive analysis
    cmd_rep_fp = 0
    for w in usable_windows:
        cr = w["labels"]["command_repetition"]
        fd = w["labels"]["file_diff_delta"]
        ob = w["labels"]["outcome_backpropagation"]
        if cr == 0:
            other_votes = [v for v in [fd, ob] if v != -1]
            if other_votes and all(v == 1 for v in other_votes):
                cmd_rep_fp += 1
    n_cr_stag = sum(1 for w in usable_windows if w["labels"]["command_repetition"] == 0)
    print(f"\ncmd_rep stagnation calls: {n_cr_stag}")
    print(f"  of which other LFs say progress: {cmd_rep_fp} ({cmd_rep_fp/max(n_cr_stag,1)*100:.1f}%)")

    # 2-LF relabeling
    results_by_conf = {}
    for min_conf in [2, 1]:
        new_labels, new_embeddings, new_tids, new_iids = [], [], [], []
        for i, w in enumerate(usable_windows):
            fd = w["labels"]["file_diff_delta"]
            ob = w["labels"]["outcome_backpropagation"]
            label, _ = relabel_2lf(fd, ob, min_conf=min_conf)
            if label != -1:
                new_labels.append(label)
                new_embeddings.append(embeddings[i])
                new_tids.append(trajectory_ids[i])
                new_iids.append(instance_ids[i])

        dist = Counter(new_labels)
        n = len(new_labels)
        sr = dist.get(0, 0) / n if n > 0 else 0

        print(f"\n--- 2-LF min_conf={min_conf} ---")
        print(f"Windows: {n} ({n/n_total*100:.1f}% of original)")
        print(f"Distribution: {dict(dist)}")
        print(f"Stag ratio: {sr*100:.2f}% (was {stag_rate:.2f}% with 3-LF)")

        results_by_conf[min_conf] = {
            "labels": new_labels,
            "embeddings": new_embeddings,
            "trajectory_ids": new_tids,
            "instance_ids": new_iids,
            "n_total": n,
            "stag_ratio": sr,
            "label_dist": dict(dist),
        }

    primary_conf = 2
    if results_by_conf[2]["n_total"] < 500:
        primary_conf = 1
    print(f"\nPrimary: min_conf={primary_conf} ({results_by_conf[primary_conf]['n_total']} windows)")

    # ===== Step 2: Save 2-LF embeddings =====
    print("\n" + "=" * 60)
    print("Step 2: Save 2-LF embeddings")
    print("=" * 60)
    p = results_by_conf[primary_conf]
    emb_2lf_path = oh_dir / "embeddings_no_cmdrep_fixed.pt"
    torch.save({
        "embeddings": p["embeddings"],
        "labels": p["labels"],
        "trajectory_ids": p["trajectory_ids"],
        "instance_ids": p["instance_ids"],
        "embed_dim": embed_dim,
        "confidences": [2] * p["n_total"],
        "step_indices_list": [],
        "source": "2-LF (file_diff + outcome_bp), no cmd_rep, from fixed embeddings",
    }, emb_2lf_path)
    print(f"Saved to {emb_2lf_path}")

    # ===== Step 3a: 3-LF zero-shot (SWE → OH fixed) =====
    print("\n" + "=" * 60)
    print("Step 3a: 3-LF zero-shot (SWE checkpoint → fixed OH)")
    print("=" * 60)

    data_3lf = {
        "embeddings": embeddings,
        "labels": old_labels,
        "trajectory_ids": trajectory_ids,
        "instance_ids": instance_ids,
    }
    train_idx_3, val_idx_3, test_idx_3 = split_by_trajectory(trajectory_ids, seed=42)
    test_ds_3 = WindowDataset(
        [embeddings[i] for i in test_idx_3],
        [old_labels[i] for i in test_idx_3],
    )
    test_loader_3 = DataLoader(test_ds_3, batch_size=64, shuffle=False, collate_fn=collate_fn)

    ckpt = torch.load(swe_ckpt, weights_only=False, map_location=device)
    model = ProgressProbe(embed_dim=embed_dim, hidden_size=ckpt["hidden_size"],
                          num_layers=ckpt["num_layers"], dropout=ckpt.get("dropout", 0.1)).to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    zs_3lf = evaluate_model(model, test_loader_3, device)
    print(f"3-LF zero-shot test: macro_f1={zs_3lf['macro_f1']:.4f}, "
          f"f1_stag={zs_3lf['f1_stagnation']:.4f}, f1_prog={zs_3lf['f1_progress']:.4f}")

    full_loader_3 = DataLoader(
        WindowDataset(embeddings, old_labels),
        batch_size=64, shuffle=False, collate_fn=collate_fn)
    zs_3lf_full = evaluate_model(model, full_loader_3, device)
    print(f"3-LF zero-shot full: macro_f1={zs_3lf_full['macro_f1']:.4f}")
    del model
    torch.cuda.empty_cache()

    # ===== Step 3b: 2-LF zero-shot + fine-tune =====
    print("\n" + "=" * 60)
    print("Step 3b: 2-LF (no cmd_rep) zero-shot + fine-tune")
    print("=" * 60)
    result_2lf = train_probe(p, swe_ckpt, device, embed_dim, output_dir,
                              tag=f" (2-LF conf>={primary_conf})")

    # ===== Step 3c: 3-LF fine-tune (use fix Worker result) =====
    print("\n" + "=" * 60)
    print("Step 3c: 3-LF fine-tune baseline (from fix Worker)")
    print("=" * 60)
    ft_3lf_path = proj_dir / "checkpoints_oh_fixed_ft" / "results.json"
    if ft_3lf_path.exists():
        with open(ft_3lf_path) as f:
            ft_3lf_result = json.load(f)
        ft_3lf_metrics = ft_3lf_result["test_metrics"]
        print(f"3-LF fine-tuned test: macro_f1={ft_3lf_metrics['macro_f1']:.4f}, "
              f"f1_stag={ft_3lf_metrics['f1_stagnation']:.4f}, f1_prog={ft_3lf_metrics['f1_progress']:.4f}")
    else:
        print("WARNING: No 3-LF fine-tune results found, training...")
        output_3lf = proj_dir / "checkpoints_oh_3lf_fixed"
        output_3lf.mkdir(exist_ok=True)
        r3 = train_probe(data_3lf, swe_ckpt, device, embed_dim, output_3lf, tag=" (3-LF)")
        ft_3lf_metrics = r3["fine_tuned_test"]

    # ===== Step 4: Summary =====
    print("\n" + "=" * 60)
    print("RESULTS COMPARISON")
    print("=" * 60)

    zs_2lf = result_2lf["zero_shot_test"]
    ft_2lf = result_2lf["fine_tuned_test"]

    print(f"\n{'Condition':<30} {'Macro-F1':>10} {'F1(stag)':>10} {'F1(prog)':>10} {'Acc':>10}")
    print("-" * 72)
    print(f"{'3-LF zero-shot (test)':<30} {zs_3lf['macro_f1']:>10.4f} {zs_3lf['f1_stagnation']:>10.4f} "
          f"{zs_3lf['f1_progress']:>10.4f} {zs_3lf['accuracy']:>10.4f}")
    print(f"{'2-LF zero-shot (test)':<30} {zs_2lf['macro_f1']:>10.4f} {zs_2lf['f1_stagnation']:>10.4f} "
          f"{zs_2lf['f1_progress']:>10.4f} {zs_2lf['accuracy']:>10.4f}")
    zs_delta = zs_2lf["macro_f1"] - zs_3lf["macro_f1"]
    print(f"{'  Δ zero-shot':<30} {zs_delta:>+10.4f}")
    print()
    print(f"{'3-LF fine-tuned (test)':<30} {ft_3lf_metrics['macro_f1']:>10.4f} {ft_3lf_metrics['f1_stagnation']:>10.4f} "
          f"{ft_3lf_metrics['f1_progress']:>10.4f} {ft_3lf_metrics['accuracy']:>10.4f}")
    print(f"{'2-LF fine-tuned (test)':<30} {ft_2lf['macro_f1']:>10.4f} {ft_2lf['f1_stagnation']:>10.4f} "
          f"{ft_2lf['f1_progress']:>10.4f} {ft_2lf['accuracy']:>10.4f}")
    ft_delta = ft_2lf["macro_f1"] - ft_3lf_metrics["macro_f1"]
    print(f"{'  Δ fine-tuned':<30} {ft_delta:>+10.4f}")

    print(f"\n{'SWE in-domain ref':<30} {'0.9055':>10}")
    print(f"{'Old 3-LF ft (unfixed)':<30} {'0.7512':>10}")
    print(f"{'Old 2-LF ft (unfixed)':<30} {'0.9272':>10}")
    print(f"{'Old delta':<30} {'+0.1760':>10}")
    print(f"{'New delta':<30} {ft_delta:>+10.4f}")

    # ===== Save results =====
    result = {
        "experiment": "oh-cmdrep-ablation-fixed",
        "data_source": "embeddings_fixed.pt (stag_rate=21.45%)",
        "swe_checkpoint": str(swe_ckpt),
        "relabeling": {
            "original_3lf_n": n_total,
            "original_3lf_dist": dict(old_dist),
            "original_3lf_stag_ratio": round(old_dist[0] / n_total, 4),
            "2lf_min_conf": primary_conf,
            "2lf_n": p["n_total"],
            "2lf_dist": p["label_dist"],
            "2lf_stag_ratio": round(p["stag_ratio"], 4),
            "cmd_rep_stag_calls": n_cr_stag,
            "cmd_rep_false_positives": cmd_rep_fp,
        },
        "3lf_zero_shot_test": {k: round(v, 4) for k, v in zs_3lf.items()},
        "3lf_zero_shot_full": {k: round(v, 4) for k, v in zs_3lf_full.items()},
        "3lf_fine_tuned_test": {k: round(v, 4) for k, v in ft_3lf_metrics.items()},
        "2lf_zero_shot_test": result_2lf["zero_shot_test"],
        "2lf_zero_shot_full": result_2lf["zero_shot_full"],
        "2lf_fine_tuned_test": result_2lf["fine_tuned_test"],
        "2lf_splits": result_2lf["splits"],
        "2lf_best_epoch": result_2lf["best_epoch"],
        "deltas": {
            "zero_shot_macro_f1": round(zs_delta, 4),
            "fine_tuned_macro_f1": round(ft_delta, 4),
        },
        "old_results_comparison": {
            "old_3lf_ft": 0.7512,
            "old_2lf_ft": 0.9272,
            "old_delta": 0.1760,
            "new_3lf_ft": round(ft_3lf_metrics["macro_f1"], 4),
            "new_2lf_ft": round(ft_2lf["macro_f1"], 4),
            "new_delta": round(ft_delta, 4),
        },
    }

    out_path = proj_dir / "oh_cmdrep_ablation_fixed_results.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print metrics for registry
    metrics = {
        "new_stag_ratio_3lf": round(old_dist[0] / n_total, 4),
        "new_stag_ratio_2lf": round(p["stag_ratio"], 4),
        "zeroshot_3lf_macro_f1": round(zs_3lf["macro_f1"], 4),
        "zeroshot_2lf_macro_f1": round(zs_2lf["macro_f1"], 4),
        "finetune_3lf_macro_f1": round(ft_3lf_metrics["macro_f1"], 4),
        "finetune_2lf_macro_f1": round(ft_2lf["macro_f1"], 4),
        "delta_zs": round(zs_delta, 4),
        "delta_ft": round(ft_delta, 4),
    }
    print(f"\nMETRICS_JSON={json.dumps(metrics)}")


if __name__ == "__main__":
    main()
