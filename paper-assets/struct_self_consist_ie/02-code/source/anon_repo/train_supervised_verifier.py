#!/usr/bin/env python3
"""exp-019: Train supervised verifier (DeBERTa-v3-large) for sample quality prediction.

5-fold GroupKFold CV on instances. Regression target: per-sample F1.
Outputs out-of-fold predictions for evaluation.

Usage:
    cd /root/autodl-tmp/struct_self_consist_ie
    python train_supervised_verifier.py \
        --data_path output/exp_012_rerun_1024/samples.jsonl \
        --subtask ner \
        --output_dir output/exp_019_supervised_verifier
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from collections import defaultdict

import numpy as np
import torch
from scipy.stats import spearmanr
from sklearn.model_selection import GroupKFold
from torch.utils.data import Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    set_seed,
)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "code"))
from evaluation import per_instance_f1

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="Train supervised verifier (DeBERTa regression)")
    p.add_argument("--data_path", type=str, required=True,
                    help="Path to samples.jsonl (exp_012 format)")
    p.add_argument("--subtask", type=str, default="ner", choices=["ner", "re"])
    p.add_argument("--model_name", type=str, default="microsoft/deberta-v3-large")
    p.add_argument("--num_folds", type=int, default=5)
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--lr", type=float, default=2e-5)
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--max_seq_len", type=int, default=512)
    p.add_argument("--output_dir", type=str, default="output/exp_019_supervised_verifier")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--warmup_ratio", type=float, default=0.1)
    return p.parse_args()


# ---------------------------------------------------------------------------
# Data preparation
# ---------------------------------------------------------------------------

def format_extraction_text(sample: dict) -> str:
    """Serialize entities and relations into a compact text string."""
    parts = []

    entities = sample.get("entities", [])
    if entities:
        ent_strs = [f'[{e["type"]}] {e["text"]}' for e in entities]
        parts.append("Entities: " + " | ".join(ent_strs))
    else:
        parts.append("Entities: none")

    relations = sample.get("relations", [])
    if relations:
        rel_strs = [f'{r["head"]} [{r["type"]}] {r["tail"]}' for r in relations]
        parts.append("Relations: " + " | ".join(rel_strs))
    else:
        parts.append("Relations: none")

    return " ".join(parts)


def prepare_data(data_path: str, subtask: str):
    """Load samples.jsonl -> flat list of sample dicts with F1 labels."""
    instances = []
    with open(data_path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))

    log.info(f"Loaded {len(instances)} instances from {data_path}")

    flat_samples = []
    for inst in instances:
        instance_id = inst["id"]
        text = inst["text"]
        gold = inst["gold"]

        for si, sample in enumerate(inst["samples"]):
            f1 = per_instance_f1(sample, gold, subtask)
            extraction_text = format_extraction_text(sample)
            flat_samples.append({
                "instance_id": instance_id,
                "sample_idx": si,
                "text": text,
                "extraction_text": extraction_text,
                "f1": f1,
                "mean_logprob": sample.get("mean_logprob", 0.0),
            })

    f1_vals = [s["f1"] for s in flat_samples]
    log.info(
        f"{len(flat_samples)} samples | {subtask} F1: "
        f"mean={np.mean(f1_vals):.4f} std={np.std(f1_vals):.4f} "
        f"median={np.median(f1_vals):.4f} zero_pct={100*np.mean(np.array(f1_vals)==0):.1f}%"
    )
    return instances, flat_samples


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

class VerifierDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {k: v[idx] for k, v in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx], dtype=torch.float)
        return item

    def __len__(self):
        return len(self.labels)


# ---------------------------------------------------------------------------
# Metrics callback
# ---------------------------------------------------------------------------

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = predictions.squeeze(-1)
    mse = float(np.mean((predictions - labels) ** 2))
    rho, _ = spearmanr(predictions, labels)
    return {
        "mse": mse,
        "spearman_rho": float(rho) if not np.isnan(rho) else 0.0,
    }


# ---------------------------------------------------------------------------
# Per-fold training
# ---------------------------------------------------------------------------

def train_fold(fold_idx: int, train_samples: list, val_samples: list,
               args, tokenizer) -> list[dict]:
    log.info(f"--- Fold {fold_idx} | train={len(train_samples)} val={len(val_samples)} ---")

    train_enc = tokenizer(
        [s["text"] for s in train_samples],
        [s["extraction_text"] for s in train_samples],
        max_length=args.max_seq_len, truncation=True, padding=True,
        return_tensors="pt",
    )
    val_enc = tokenizer(
        [s["text"] for s in val_samples],
        [s["extraction_text"] for s in val_samples],
        max_length=args.max_seq_len, truncation=True, padding=True,
        return_tensors="pt",
    )

    train_ds = VerifierDataset(train_enc, [s["f1"] for s in train_samples])
    val_ds = VerifierDataset(val_enc, [s["f1"] for s in val_samples])

    model = AutoModelForSequenceClassification.from_pretrained(
        args.model_name, num_labels=1, problem_type="regression",
    )

    fold_dir = os.path.join(args.output_dir, f"fold_{fold_idx}")

    training_args = TrainingArguments(
        output_dir=fold_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size * 2,
        learning_rate=args.lr,
        weight_decay=0.01,
        warmup_ratio=args.warmup_ratio,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="spearman_rho",
        greater_is_better=True,
        logging_steps=20,
        seed=args.seed,
        fp16=torch.cuda.is_available(),
        report_to="none",
        save_total_limit=1,
        dataloader_num_workers=2,
        dataloader_pin_memory=True,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        compute_metrics=compute_metrics,
    )

    trainer.train()

    eval_result = trainer.evaluate()
    log.info(f"Fold {fold_idx} eval: {eval_result}")

    preds_out = trainer.predict(val_ds)
    pred_scores = preds_out.predictions.squeeze(-1).tolist()
    if isinstance(pred_scores, float):
        pred_scores = [pred_scores]

    fold_results = []
    for i, s in enumerate(val_samples):
        fold_results.append({
            "instance_id": s["instance_id"],
            "sample_idx": s["sample_idx"],
            "true_f1": s["f1"],
            "predicted_score": pred_scores[i],
            "mean_logprob": s["mean_logprob"],
        })

    del model, trainer
    torch.cuda.empty_cache()

    return fold_results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    set_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    log.info(f"Config: {json.dumps(vars(args), indent=2)}")

    instances, flat_samples = prepare_data(args.data_path, args.subtask)

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)

    # GroupKFold: same instance's samples always in the same fold
    instance_ids = [s["instance_id"] for s in flat_samples]
    unique_ids = list(dict.fromkeys(instance_ids))
    id_to_group = {iid: g for g, iid in enumerate(unique_ids)}
    groups = np.array([id_to_group[iid] for iid in instance_ids])

    gkf = GroupKFold(n_splits=args.num_folds)
    dummy_y = np.zeros(len(flat_samples))

    all_predictions = []

    for fold_idx, (train_idx, val_idx) in enumerate(gkf.split(dummy_y, groups=groups)):
        train_samples = [flat_samples[i] for i in train_idx]
        val_samples = [flat_samples[i] for i in val_idx]

        train_ids = {s["instance_id"] for s in train_samples}
        val_ids = {s["instance_id"] for s in val_samples}
        assert train_ids.isdisjoint(val_ids), f"Instance leakage in fold {fold_idx}!"
        log.info(f"Fold {fold_idx}: {len(train_ids)} train / {len(val_ids)} val instances")

        fold_preds = train_fold(fold_idx, train_samples, val_samples, args, tokenizer)
        all_predictions.extend(fold_preds)

    # Save out-of-fold predictions
    output_path = os.path.join(args.output_dir, f"oof_predictions_{args.subtask}.json")
    payload = {
        "config": vars(args),
        "n_instances": len(unique_ids),
        "n_samples": len(flat_samples),
        "predictions": all_predictions,
    }
    with open(output_path, "w") as f:
        json.dump(payload, f, indent=2)
    log.info(f"Saved {len(all_predictions)} OOF predictions -> {output_path}")

    # --- Quick summary ---
    true_f1s = np.array([p["true_f1"] for p in all_predictions])
    pred_scores = np.array([p["predicted_score"] for p in all_predictions])
    rho, _ = spearmanr(pred_scores, true_f1s)
    log.info(f"Overall Spearman rho = {rho:.4f}")

    by_inst = defaultdict(list)
    for p in all_predictions:
        by_inst[p["instance_id"]].append(p)

    def _sel_f1(key):
        return np.mean([max(ps, key=lambda x: x[key])["true_f1"] for ps in by_inst.values()])

    log.info(f"Selection F1 ({args.subtask}):")
    log.info(f"  Supervised verifier : {_sel_f1('predicted_score'):.4f}")
    log.info(f"  LogProb             : {_sel_f1('mean_logprob'):.4f}")
    log.info(f"  Oracle              : {_sel_f1('true_f1'):.4f}")
    log.info(f"  Random (mean)       : {np.mean(true_f1s):.4f}")

    # Greedy
    greedy_f1s = []
    for inst in instances:
        if "greedy" in inst:
            gf = per_instance_f1(inst["greedy"], inst["gold"], args.subtask)
        else:
            gf = per_instance_f1(inst["samples"][0], inst["gold"], args.subtask)
        greedy_f1s.append(gf)
    log.info(f"  Greedy              : {np.mean(greedy_f1s):.4f}")

    log.info("Done.")


if __name__ == "__main__":
    main()
