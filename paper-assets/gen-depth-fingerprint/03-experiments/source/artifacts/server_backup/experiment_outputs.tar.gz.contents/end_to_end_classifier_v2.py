#!/usr/bin/env python3
"""QLoRA fine-tune Qwen3-0.6B-Base for depth classification (plan-012)."""

import argparse
import json
import os
import time
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import (
    f1_score,
    confusion_matrix,
    classification_report,
)
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


def load_generation_data(data_dir):
    generators = ["pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"]
    texts, depths, models = [], [], []

    for gen in generators:
        fpath = os.path.join(data_dir, gen, "generations.jsonl")
        if not os.path.exists(fpath):
            print(f"  SKIP {gen}: file not found")
            continue
        count = 0
        with open(fpath) as f:
            for line in f:
                rec = json.loads(line)
                texts.append(rec["text"])
                depths.append(rec["depth"])
                models.append(gen)
                count += 1
        print(f"  {gen}: {count} samples")

    print(f"  Total: {len(texts)} samples")
    depth_counts = {}
    for d in depths:
        depth_counts[d] = depth_counts.get(d, 0) + 1
    print(f"  Depth distribution: {dict(sorted(depth_counts.items()))}")
    return texts, depths, models


def map_to_3class(labels):
    return [min(l, 2) for l in labels]


def compute_metrics_fn(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    f1_5 = f1_score(labels, preds, average="macro")
    labels_3 = [min(l, 2) for l in labels]
    preds_3 = [min(p, 2) for p in preds]
    f1_3 = f1_score(labels_3, preds_3, average="macro")
    return {"macro_f1_5class": f1_5, "macro_f1_3class": f1_3}


def run_fold(
    fold_idx,
    train_texts,
    train_labels,
    val_texts,
    val_labels,
    model_name,
    tokenizer,
    max_length,
    batch_size,
    lr,
    epochs,
    device,
    output_dir,
):
    print(f"\n{'='*60}")
    print(f"FOLD {fold_idx + 1}")
    print(f"  Train: {len(train_texts)}, Val: {len(val_texts)}")
    print(f"{'='*60}")

    train_enc = tokenizer(
        train_texts,
        truncation=True,
        padding="max_length",
        max_length=max_length,
        return_tensors="pt",
    )
    val_enc = tokenizer(
        val_texts,
        truncation=True,
        padding="max_length",
        max_length=max_length,
        return_tensors="pt",
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
        model_name,
        num_labels=5,
        quantization_config=bnb_config,
        device_map={"": device},
        torch_dtype=torch.bfloat16,
    )
    model.config.pad_token_id = tokenizer.pad_token_id

    model = prepare_model_for_kbit_training(model)

    lora_config = LoraConfig(
        task_type=TaskType.SEQ_CLS,
        r=32,
        lora_alpha=64,
        lora_dropout=0.05,
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
        seed=123,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
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

    print(f"\nFold {fold_idx + 1} Results:")
    print(f"  5-class macro F1: {f1_5:.4f}")
    print(f"  5-class per-class: {dict(zip(range(5), [round(x, 4) for x in f1_per]))}")
    print(f"  3-class macro F1: {f1_3:.4f}")
    print(f"  3-class per-class: {dict(zip(['gen0','gen1','gen2+'], [round(x, 4) for x in f1_per_3]))}")

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
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="Qwen/Qwen3-0.6B")
    parser.add_argument("--model_path", default=None)
    parser.add_argument("--data_dir", default="data")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--output", default="results/plan012_qwen06b_seed123_r32_results.json")
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--n_folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=123)
    args = parser.parse_args()

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    model_name = args.model_path or args.model
    print(f"Model: {model_name}")
    print(f"Device: {args.device}")
    print(f"Max length: {args.max_length}, Batch size: {args.batch_size}")

    print("\nLoading data...")
    texts, depths, models = load_generation_data(args.data_dir)

    print("\nLoading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "right"

    skf = StratifiedKFold(n_splits=args.n_folds, shuffle=True, random_state=args.seed)
    depths_arr = np.array(depths)
    texts_arr = np.array(texts)

    output_dir = os.path.join("checkpoints", "plan012_qwen06b_v2")
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    fold_results = []
    t0 = time.time()

    for fold_idx, (train_idx, val_idx) in enumerate(skf.split(texts_arr, depths_arr)):
        train_texts = texts_arr[train_idx].tolist()
        train_labels = depths_arr[train_idx].tolist()
        val_texts = texts_arr[val_idx].tolist()
        val_labels = depths_arr[val_idx].tolist()

        result = run_fold(
            fold_idx,
            train_texts,
            train_labels,
            val_texts,
            val_labels,
            model_name,
            tokenizer,
            args.max_length,
            args.batch_size,
            args.lr,
            args.epochs,
            args.device,
            output_dir,
        )
        fold_results.append(result)

    elapsed = time.time() - t0

    avg_f1_5 = np.mean([r["macro_f1_5class"] for r in fold_results])
    std_f1_5 = np.std([r["macro_f1_5class"] for r in fold_results])
    avg_f1_3 = np.mean([r["macro_f1_3class"] for r in fold_results])
    std_f1_3 = np.std([r["macro_f1_3class"] for r in fold_results])

    avg_per_5 = {}
    for i in range(5):
        k = f"depth_{i}"
        vals = [r["per_class_f1_5class"][k] for r in fold_results]
        avg_per_5[k] = round(np.mean(vals), 4)

    avg_per_3 = {}
    for k in ["gen0", "gen1", "gen2+"]:
        vals = [r["per_class_f1_3class"][k] for r in fold_results]
        avg_per_3[k] = round(np.mean(vals), 4)

    xgb_5class = 0.5028
    xgb_3class = 0.7815

    summary = {
        "experiment": "plan-012-qwen06b-v2",
        "model": args.model,
        "model_path": model_name,
        "method": "QLoRA_4bit_seqcls",
        "lora_config": {"r": 32, "alpha": 64, "target_modules": ["q_proj", "v_proj"]},
        "max_length": args.max_length,
        "batch_size": args.batch_size,
        "lr": args.lr,
        "epochs": args.epochs,
        "n_folds": args.n_folds,
        "n_samples": len(texts),
        "generators": ["pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b"],
        "cv_type": "5-fold_stratified",
        "macro_f1_5class": round(float(avg_f1_5), 4),
        "macro_f1_5class_std": round(float(std_f1_5), 4),
        "macro_f1_3class": round(float(avg_f1_3), 4),
        "macro_f1_3class_std": round(float(std_f1_3), 4),
        "per_class_f1_5class": avg_per_5,
        "per_class_f1_3class": avg_per_3,
        "fold_results": fold_results,
        "baseline_xgboost": {
            "5class_macro_f1": xgb_5class,
            "3class_macro_f1": xgb_3class,
            "method": "HGBT_7features_LOGO",
        },
        "delta_vs_xgboost": {
            "5class": round(float(avg_f1_5) - xgb_5class, 4),
            "3class": round(float(avg_f1_3) - xgb_3class, 4),
        },
        "runtime_seconds": round(elapsed, 1),
        "seed": args.seed,
    }

    print(f"\n{'='*60}")
    print("FINAL RESULTS")
    print(f"{'='*60}")
    print(f"5-class macro F1: {avg_f1_5:.4f} +/- {std_f1_5:.4f} (XGBoost: {xgb_5class})")
    print(f"3-class macro F1: {avg_f1_3:.4f} +/- {std_f1_3:.4f} (XGBoost: {xgb_3class})")
    print(f"Delta 5-class: {avg_f1_5 - xgb_5class:+.4f}")
    print(f"Delta 3-class: {avg_f1_3 - xgb_3class:+.4f}")
    print(f"Per-class 5-class: {avg_per_5}")
    print(f"Per-class 3-class: {avg_per_3}")
    print(f"Runtime: {elapsed/60:.1f} min")

    with open(args.output, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
