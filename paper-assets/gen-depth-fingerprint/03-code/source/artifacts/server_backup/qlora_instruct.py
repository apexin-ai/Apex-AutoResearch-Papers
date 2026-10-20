#!/usr/bin/env python3
"""QLoRA fine-tune Qwen3-0.6B for single-generator within-model depth classification."""

import argparse
import json
import os
import time

import numpy as np
import torch
from torch.utils.data import Dataset
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, confusion_matrix
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, TaskType, prepare_model_for_kbit_training


class DepthDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {k: v[idx] for k, v in self.encodings.items()}
        item["labels"] = self.labels[idx]
        return item


def load_single_generator(data_path, generator):
    texts, depths = [], []
    with open(data_path) as f:
        for line in f:
            rec = json.loads(line)
            texts.append(rec["text"])
            depths.append(rec["depth"])
    depth_counts = {}
    for d in depths:
        depth_counts[d] = depth_counts.get(d, 0) + 1
    print(f"  {generator}: {len(texts)} samples")
    print(f"  Depth distribution: {dict(sorted(depth_counts.items()))}")
    return texts, depths


def map_to_3class(labels):
    return [min(l, 2) for l in labels]


def compute_binary_f1(true_labels, pred_labels):
    """Binary F1: gen-1 vs gen-2+, excluding gen-0."""
    mask = [i for i, t in enumerate(true_labels) if t >= 1]
    if not mask:
        return float("nan")
    true_bin = [0 if true_labels[i] == 1 else 1 for i in mask]
    pred_bin = [0 if pred_labels[i] == 1 else 1 for i in mask]
    return f1_score(true_bin, pred_bin, average="macro")


def compute_metrics_fn(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    f1_5 = f1_score(labels, preds, average="macro")
    labels_3 = [min(l, 2) for l in labels]
    preds_3 = [min(p, 2) for p in preds]
    f1_3 = f1_score(labels_3, preds_3, average="macro")
    return {"macro_f1_5class": f1_5, "macro_f1_3class": f1_3}


def run_fold(
    fold_idx, train_texts, train_labels, val_texts, val_labels,
    model_name, tokenizer, max_length, batch_size, lr, epochs, device, output_dir,
):
    print(f"\n{'='*60}")
    print(f"FOLD {fold_idx + 1}")
    print(f"  Train: {len(train_texts)}, Val: {len(val_texts)}")
    print(f"{'='*60}")

    train_enc = tokenizer(
        train_texts, truncation=True, padding="max_length",
        max_length=max_length, return_tensors="pt",
    )
    val_enc = tokenizer(
        val_texts, truncation=True, padding="max_length",
        max_length=max_length, return_tensors="pt",
    )

    train_ds = DepthDataset(train_enc, torch.tensor(train_labels, dtype=torch.long))
    val_ds = DepthDataset(val_enc, torch.tensor(val_labels, dtype=torch.long))

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        model_name, num_labels=5,
        quantization_config=bnb_config,
        device_map={"": device},
        torch_dtype=torch.bfloat16,
    )
    model.config.pad_token_id = tokenizer.pad_token_id

    model = prepare_model_for_kbit_training(model)

    lora_config = LoraConfig(
        task_type=TaskType.SEQ_CLS,
        r=32, lora_alpha=64, lora_dropout=0.05,
        target_modules=["q_proj", "v_proj"],
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    fold_dir = os.path.join(output_dir, f"fold_{fold_idx}")
    warmup_steps = int(0.1 * (len(train_ds) // batch_size) * epochs)

    training_args = TrainingArguments(
        output_dir=fold_dir,
        num_train_epochs=epochs,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size * 2,
        learning_rate=lr,
        warmup_steps=warmup_steps,
        weight_decay=0.01,
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=1,
        load_best_model_at_end=True,
        metric_for_best_model="macro_f1_3class",
        greater_is_better=True,
        logging_steps=50,
        bf16=True,
        dataloader_num_workers=2,
        report_to="none",
        seed=42,
    )

    trainer = Trainer(
        model=model, args=training_args,
        train_dataset=train_ds, eval_dataset=val_ds,
        compute_metrics=compute_metrics_fn,
    )

    trainer.train()

    preds_out = trainer.predict(val_ds)
    preds = np.argmax(preds_out.predictions, axis=-1)
    true = np.array(val_labels)

    f1_5 = f1_score(true, preds, average="macro")
    f1_per = f1_score(true, preds, average=None, labels=[0, 1, 2, 3, 4])
    cm_5 = confusion_matrix(true, preds, labels=[0, 1, 2, 3, 4])

    true_3 = np.array(map_to_3class(val_labels))
    preds_3 = np.array(map_to_3class(preds.tolist()))
    f1_3 = f1_score(true_3, preds_3, average="macro")
    f1_per_3 = f1_score(true_3, preds_3, average=None, labels=[0, 1, 2])
    cm_3 = confusion_matrix(true_3, preds_3, labels=[0, 1, 2])

    binary_f1 = compute_binary_f1(val_labels, preds.tolist())

    print(f"\nFold {fold_idx + 1} Results:")
    print(f"  5-class macro F1: {f1_5:.4f}")
    print(f"  5-class per-class: {dict(zip(range(5), [round(x, 4) for x in f1_per]))}")
    print(f"  3-class macro F1: {f1_3:.4f}")
    print(f"  3-class per-class: {dict(zip(['gen0','gen1','gen2+'], [round(x, 4) for x in f1_per_3]))}")
    print(f"  Binary F1 (gen1 vs gen2+): {binary_f1:.4f}")

    del model, trainer
    torch.cuda.empty_cache()

    return {
        "fold": fold_idx,
        "n_train": len(train_texts),
        "n_val": len(val_texts),
        "macro_f1_5class": round(f1_5, 4),
        "per_class_f1_5class": {f"depth_{i}": round(f1_per[i], 4) for i in range(5)},
        "confusion_matrix_5class": cm_5.tolist(),
        "macro_f1_3class": round(f1_3, 4),
        "per_class_f1_3class": {
            "gen0": round(f1_per_3[0], 4),
            "gen1": round(f1_per_3[1], 4),
            "gen2+": round(f1_per_3[2], 4),
        },
        "confusion_matrix_3class": cm_3.tolist(),
        "binary_f1_gen1_vs_gen2plus": round(binary_f1, 4),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--generator", required=True, help="Generator name (e.g. qwen3-1.7b-instruct)")
    parser.add_argument("--data_path", required=True, help="Path to JSONL file")
    parser.add_argument("--backbone", default="/root/autodl-tmp/models/qwen3-0.6b")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--output", required=True, help="JSON results output path")
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--n_folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=123)
    args = parser.parse_args()

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    print(f"Generator: {args.generator}")
    print(f"Data: {args.data_path}")
    print(f"Backbone: {args.backbone}")
    print(f"Device: {args.device}")
    print(f"Config: max_len={args.max_length}, bs={args.batch_size}, lr={args.lr}, epochs={args.epochs}")

    print("\nLoading data...")
    texts, depths = load_single_generator(args.data_path, args.generator)

    print("\nLoading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(args.backbone, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "right"

    skf = StratifiedKFold(n_splits=args.n_folds, shuffle=True, random_state=args.seed)
    depths_arr = np.array(depths)
    texts_arr = np.array(texts)

    output_dir = os.path.join("checkpoints", f"qlora_instruct_{args.generator}")
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    fold_results = []
    t0 = time.time()

    for fold_idx, (train_idx, val_idx) in enumerate(skf.split(texts_arr, depths_arr)):
        train_texts = texts_arr[train_idx].tolist()
        train_labels = depths_arr[train_idx].tolist()
        val_texts = texts_arr[val_idx].tolist()
        val_labels = depths_arr[val_idx].tolist()

        result = run_fold(
            fold_idx, train_texts, train_labels, val_texts, val_labels,
            args.backbone, tokenizer, args.max_length, args.batch_size,
            args.lr, args.epochs, args.device, output_dir,
        )
        fold_results.append(result)

    elapsed = time.time() - t0

    avg_f1_5 = np.mean([r["macro_f1_5class"] for r in fold_results])
    std_f1_5 = np.std([r["macro_f1_5class"] for r in fold_results])
    avg_f1_3 = np.mean([r["macro_f1_3class"] for r in fold_results])
    std_f1_3 = np.std([r["macro_f1_3class"] for r in fold_results])
    avg_bin = np.mean([r["binary_f1_gen1_vs_gen2plus"] for r in fold_results])
    std_bin = np.std([r["binary_f1_gen1_vs_gen2plus"] for r in fold_results])

    avg_per_5 = {}
    for i in range(5):
        k = f"depth_{i}"
        vals = [r["per_class_f1_5class"][k] for r in fold_results]
        avg_per_5[k] = round(np.mean(vals), 4)

    avg_per_3 = {}
    for k in ["gen0", "gen1", "gen2+"]:
        vals = [r["per_class_f1_3class"][k] for r in fold_results]
        avg_per_3[k] = round(np.mean(vals), 4)

    summary = {
        "experiment": f"qlora_instruct_{args.generator}",
        "generator": args.generator,
        "backbone": args.backbone,
        "method": "QLoRA_4bit_seqcls",
        "lora_config": {"r": 32, "alpha": 64, "target_modules": ["q_proj", "v_proj"]},
        "max_length": args.max_length,
        "batch_size": args.batch_size,
        "lr": args.lr,
        "epochs": args.epochs,
        "n_folds": args.n_folds,
        "n_samples": len(texts),
        "cv_type": "5-fold_stratified_within_model",
        "macro_f1_5class": round(float(avg_f1_5), 4),
        "macro_f1_5class_std": round(float(std_f1_5), 4),
        "macro_f1_3class": round(float(avg_f1_3), 4),
        "macro_f1_3class_std": round(float(std_f1_3), 4),
        "binary_f1_gen1_vs_gen2plus": round(float(avg_bin), 4),
        "binary_f1_gen1_vs_gen2plus_std": round(float(std_bin), 4),
        "per_class_f1_5class": avg_per_5,
        "per_class_f1_3class": avg_per_3,
        "fold_results": fold_results,
        "runtime_seconds": round(elapsed, 1),
        "seed": args.seed,
    }

    print(f"\n{'='*60}")
    print("FINAL RESULTS")
    print(f"{'='*60}")
    print(f"Generator: {args.generator}")
    print(f"5-class macro F1: {avg_f1_5:.4f} +/- {std_f1_5:.4f}")
    print(f"3-class macro F1: {avg_f1_3:.4f} +/- {std_f1_3:.4f}")
    print(f"Binary F1 (gen1 vs gen2+): {avg_bin:.4f} +/- {std_bin:.4f}")
    print(f"Per-class 5-class: {avg_per_5}")
    print(f"Per-class 3-class: {avg_per_3}")
    print(f"Runtime: {elapsed/60:.1f} min")

    with open(args.output, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
