#!/usr/bin/env python3
"""Ablation: remove command_repetition LF from OpenHands labeling.

Hypothesis: cmd_rep has 71% false positive rate on OH (fires on progress windows),
so removing it yields cleaner labels and better measured cross-domain performance.
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
    """2-LF vote without command_repetition. Returns (label, confidence)."""
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


def run_eval_pipeline(data, ckpt_path, device, embed_dim, output_dir, tag=""):
    """Run zero-shot + fine-tune for a given relabeled dataset."""
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
          f"f1_prog={zs_metrics['f1_progress']:.4f}, acc={zs_metrics['accuracy']:.4f}")

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
    best_val_f1, patience_ctr, history = 0.0, 0, []

    ckpt_file = output_dir / "best_model.pt"
    for epoch in range(1, 16):
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
                "source": f"swe-agent-init + oh-nocmdrep-finetune{tag}",
            }, ckpt_file)
        else:
            patience_ctr += 1

        mark = " *" if is_best else ""
        print(f"  Epoch {epoch:2d} | loss={avg_loss:.4f} | val_F1={vm['macro_f1']:.4f} "
              f"f1_stag={vm['f1_stagnation']:.4f}{mark}")
        history.append({"epoch": epoch, "train_loss": avg_loss,
                        **{f"val_{k}": v for k, v in vm.items()}})

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
        "training_history": history,
    }


def main():
    set_seed(42)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    oh_dir = Path("/root/autodl-tmp/openhands_data")
    proj_dir = Path("/root/autodl-tmp/agent_progress_probe")
    ckpt_path = proj_dir / "checkpoints" / "best_model.pt"
    output_dir = proj_dir / "checkpoints_oh_nocmdrep"
    output_dir.mkdir(exist_ok=True)

    # ===== Phase A: Re-label =====
    print("\n" + "=" * 60)
    print("Phase A: Re-labeling without command_repetition")
    print("=" * 60)

    all_windows = []
    with open(oh_dir / "windows_labeled.jsonl") as f:
        for line in f:
            line = line.strip()
            if line:
                all_windows.append(json.loads(line))

    usable_windows = [w for w in all_windows if w.get("majority_label", -1) != -1]
    print(f"Total windows: {len(all_windows)}, Usable (3-LF): {len(usable_windows)}")

    emb_data = torch.load(oh_dir / "embeddings.pt", weights_only=False, map_location="cpu")
    embeddings = emb_data["embeddings"]
    old_labels = emb_data["labels"]
    trajectory_ids = emb_data["trajectory_ids"]
    embed_dim = emb_data["embed_dim"]

    assert len(usable_windows) == len(embeddings), \
        f"Mismatch: {len(usable_windows)} usable vs {len(embeddings)} embeddings"

    n_check = min(100, len(usable_windows))
    for i in range(n_check):
        assert usable_windows[i]["trajectory_id"] == trajectory_ids[i], \
            f"Alignment mismatch at {i}"
    print(f"Alignment verified (first {n_check})")

    lf_coverage = {}
    for lf in ["file_diff_delta", "command_repetition", "outcome_backpropagation"]:
        n_active = sum(1 for w in usable_windows if w["labels"][lf] != -1)
        lf_coverage[lf] = n_active
        print(f"  {lf}: {n_active}/{len(usable_windows)} ({n_active / len(usable_windows) * 100:.1f}%)")

    # Analyze label flip patterns
    cmd_rep_fp = 0
    for w in usable_windows:
        cr = w["labels"]["command_repetition"]
        fd = w["labels"]["file_diff_delta"]
        ob = w["labels"]["outcome_backpropagation"]
        if cr == 0:  # cmd_rep says stagnation
            other_votes = [v for v in [fd, ob] if v != -1]
            if other_votes and all(v == 1 for v in other_votes):
                cmd_rep_fp += 1
    n_cr_stag = sum(1 for w in usable_windows if w["labels"]["command_repetition"] == 0)
    print(f"\ncmd_rep stagnation calls: {n_cr_stag}")
    print(f"  of which other LFs say progress: {cmd_rep_fp} ({cmd_rep_fp / max(n_cr_stag, 1) * 100:.1f}%)")

    results_by_conf = {}
    for min_conf in [2, 1]:
        new_labels, new_embeddings, new_tids = [], [], []
        for i, w in enumerate(usable_windows):
            fd = w["labels"]["file_diff_delta"]
            ob = w["labels"]["outcome_backpropagation"]
            label, _ = relabel_2lf(fd, ob, min_conf=min_conf)
            if label != -1:
                new_labels.append(label)
                new_embeddings.append(embeddings[i])
                new_tids.append(trajectory_ids[i])

        dist = Counter(new_labels)
        n = len(new_labels)
        stag_ratio = dist.get(0, 0) / n if n > 0 else 0

        print(f"\n--- min_conf={min_conf} ---")
        print(f"Usable: {n} ({n / len(embeddings) * 100:.1f}%)")
        print(f"Labels: {dict(dist)}")
        print(f"Stag ratio: {stag_ratio:.4f} (was {Counter(old_labels).get(0, 0) / len(old_labels):.4f})")

        results_by_conf[min_conf] = {
            "labels": new_labels,
            "embeddings": new_embeddings,
            "trajectory_ids": new_tids,
            "n_total": n,
            "stag_ratio": stag_ratio,
            "label_dist": dict(dist),
        }

    primary_conf = 2
    if results_by_conf[2]["n_total"] < 500:
        print(f"\nconf>=2 only {results_by_conf[2]['n_total']} windows, switching to conf>=1")
        primary_conf = 1

    print(f"\nPrimary: min_conf={primary_conf} ({results_by_conf[primary_conf]['n_total']} windows)")

    # ===== Phase B: Zero-shot + Fine-tune =====
    print("\n" + "=" * 60)
    print(f"Phase B: Eval with min_conf={primary_conf}")
    print("=" * 60)

    primary_result = run_eval_pipeline(
        results_by_conf[primary_conf], ckpt_path, device, embed_dim, output_dir,
        tag=f" (conf>={primary_conf})")

    # Run secondary conf if primary was conf>=2 and we want comparison
    secondary_result = None
    alt_conf = 1 if primary_conf == 2 else 2
    if results_by_conf[alt_conf]["n_total"] >= 500:
        print(f"\n--- Also running conf>={alt_conf} for comparison ---")
        alt_dir = proj_dir / f"checkpoints_oh_nocmdrep_conf{alt_conf}"
        alt_dir.mkdir(exist_ok=True)
        secondary_result = run_eval_pipeline(
            results_by_conf[alt_conf], ckpt_path, device, embed_dim, alt_dir,
            tag=f" (conf>={alt_conf})")

    # ===== Phase C: Comparison =====
    print("\n" + "=" * 60)
    print("Phase C: Comparison")
    print("=" * 60)

    ref_zs = 0.5298
    ref_ft50 = 0.688
    zs_f1 = primary_result["zero_shot_test"]["macro_f1"]
    ft_f1 = primary_result["fine_tuned_test"]["macro_f1"]

    print(f"3-LF zero-shot:          {ref_zs:.4f}")
    print(f"No-cmd_rep zero-shot:    {zs_f1:.4f} ({zs_f1 - ref_zs:+.4f})")
    print(f"3-LF 50% fine-tune:      {ref_ft50:.4f}")
    print(f"No-cmd_rep 100% ft:      {ft_f1:.4f} ({ft_f1 - ref_ft50:+.4f})")

    if secondary_result:
        s_zs = secondary_result["zero_shot_test"]["macro_f1"]
        s_ft = secondary_result["fine_tuned_test"]["macro_f1"]
        print(f"\nAlternative (conf>={alt_conf}):")
        print(f"  zero-shot: {s_zs:.4f} ({s_zs - ref_zs:+.4f})")
        print(f"  fine-tune: {s_ft:.4f} ({s_ft - ref_ft50:+.4f})")

    # ===== Save =====
    old_dist = dict(Counter(old_labels))
    result = {
        "experiment": "oh-cmdrep-ablation",
        "hypothesis": "Removing cmd_rep LF improves cross-domain eval by eliminating noisy stagnation labels",
        "primary_min_conf": primary_conf,
        "relabeling": {
            "original_n": len(embeddings),
            "original_dist": old_dist,
            "original_stag_ratio": round(old_dist.get(0, 0) / len(embeddings), 4),
            "lf_coverage": lf_coverage,
            "cmd_rep_false_positives": cmd_rep_fp,
        },
        "primary": {
            "min_conf": primary_conf,
            "n_windows": results_by_conf[primary_conf]["n_total"],
            "label_dist": results_by_conf[primary_conf]["label_dist"],
            "stag_ratio": round(results_by_conf[primary_conf]["stag_ratio"], 4),
            **primary_result,
        },
        "comparison": {
            "ref_3lf_zs": ref_zs,
            "ref_3lf_ft50": ref_ft50,
            "nocmdrep_zs_delta": round(zs_f1 - ref_zs, 4),
            "nocmdrep_ft_delta": round(ft_f1 - ref_ft50, 4),
        },
    }

    if secondary_result:
        result["secondary"] = {
            "min_conf": alt_conf,
            "n_windows": results_by_conf[alt_conf]["n_total"],
            "label_dist": results_by_conf[alt_conf]["label_dist"],
            "stag_ratio": round(results_by_conf[alt_conf]["stag_ratio"], 4),
            **secondary_result,
        }

    # Add both conf stats to relabeling
    for c in [2, 1]:
        result["relabeling"][f"conf{c}_n"] = results_by_conf[c]["n_total"]
        result["relabeling"][f"conf{c}_dist"] = results_by_conf[c]["label_dist"]
        result["relabeling"][f"conf{c}_stag_ratio"] = round(results_by_conf[c]["stag_ratio"], 4)

    out = proj_dir / "oh_cmdrep_ablation_results.json"
    with open(out, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nResults saved to {out}")
    print(f"Checkpoint saved to {output_dir / 'best_model.pt'}")

    metrics = {
        "new_label_coverage": results_by_conf[primary_conf]["n_total"],
        "new_stag_ratio": round(results_by_conf[primary_conf]["stag_ratio"], 4),
        "zeroshot_nocmdrep_macro_f1": zs_f1,
        "zeroshot_nocmdrep_f1_stag": primary_result["zero_shot_test"]["f1_stagnation"],
        "finetune_nocmdrep_macro_f1": ft_f1,
        "finetune_nocmdrep_f1_stag": primary_result["fine_tuned_test"]["f1_stagnation"],
        "ref_3lf_zeroshot_macro_f1": ref_zs,
        "ref_3lf_ft50_macro_f1": ref_ft50,
        "zeroshot_delta": round(zs_f1 - ref_zs, 4),
        "finetune_delta": round(ft_f1 - ref_ft50, 4),
    }
    print(f"\nMETRICS_JSON={json.dumps(metrics)}")


if __name__ == "__main__":
    main()
