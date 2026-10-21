#!/usr/bin/env python3
"""DeBERTa-v3-base 4-class depth classification pilot.

Trains a LoRA-adapted DeBERTa-v3-base for ordinal generation depth
estimation (d0-d3) on a single atlas cell using 5-fold stratified CV.

Input:  data/<cell>/depth_{0,1,2,3}.jsonl  (each line: {"text": "..."})
Output: <output_dir>/<cell>/results.json

Usage:
    python scripts/deberta_depth_pilot.py --cell gpt2xl_temp09 --gpu 0
"""

import argparse
import json
import os
import shutil
import time
import warnings

os.environ.setdefault("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

import numpy as np
import torch
from sklearn.metrics import accuracy_score, balanced_accuracy_score, confusion_matrix
from sklearn.model_selection import StratifiedKFold

warnings.filterwarnings("ignore", category=FutureWarning)


def parse_args():
    p = argparse.ArgumentParser(description="DeBERTa depth pilot")
    p.add_argument("--cell", type=str, required=True, help="Atlas cell name")
    p.add_argument("--data_dir", type=str, default="data/", help="Data root")
    p.add_argument("--model_name", type=str,
                    default="microsoft/deberta-v3-base")
    p.add_argument("--output_dir", type=str, default="results/deberta_pilot")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--folds", type=int, default=5)
    p.add_argument("--epochs", type=int, default=5)
    p.add_argument("--lr", type=float, default=2e-5)
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--max_length", type=int, default=512)
    return p.parse_args()


def load_data(data_dir, cell):
    texts, labels = [], []
    cell_dir = os.path.join(data_dir, cell)
    for depth in range(4):
        fpath = os.path.join(cell_dir, f"depth_{depth}.jsonl")
        if not os.path.exists(fpath):
            raise FileNotFoundError(f"Missing: {fpath}")
        with open(fpath) as f:
            for line in f:
                obj = json.loads(line.strip())
                texts.append(obj["text"])
                labels.append(depth)
    return texts, labels


def main():
    args = parse_args()
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    from transformers import (
        AutoTokenizer,
        AutoModelForSequenceClassification,
        Trainer,
        TrainingArguments,
        EarlyStoppingCallback,
        DataCollatorWithPadding,
    )
    from peft import LoraConfig, get_peft_model, TaskType

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    print(f"[INFO] Loading data for cell={args.cell}")
    texts, labels = load_data(args.data_dir, args.cell)
    print(f"[INFO] Loaded {len(texts)} samples, {len(set(labels))} classes")

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)

    skf = StratifiedKFold(n_splits=args.folds, shuffle=True,
                          random_state=args.seed)
    fold_results = []
    all_preds, all_labels = [], []
    total_start = time.time()

    for fold_idx, (train_idx, val_idx) in enumerate(
            skf.split(texts, labels)):
        print(f"\n{'='*50}")
        print(f"[FOLD {fold_idx+1}/{args.folds}]")
        fold_start = time.time()

        train_texts = [texts[i] for i in train_idx]
        train_labels = [labels[i] for i in train_idx]
        val_texts = [texts[i] for i in val_idx]
        val_labels = [labels[i] for i in val_idx]

        train_enc = tokenizer(train_texts, truncation=True,
                              max_length=args.max_length)
        val_enc = tokenizer(val_texts, truncation=True,
                            max_length=args.max_length)

        class DepthDataset(torch.utils.data.Dataset):
            def __init__(self, encodings, labs):
                self.encodings = encodings
                self.labels = labs

            def __len__(self):
                return len(self.labels)

            def __getitem__(self, idx):
                item = {k: v[idx] for k, v in self.encodings.items()}
                item["labels"] = self.labels[idx]
                return item

        train_ds = DepthDataset(train_enc, train_labels)
        val_ds = DepthDataset(val_enc, val_labels)

        model = AutoModelForSequenceClassification.from_pretrained(
            args.model_name, num_labels=4,
            ignore_mismatched_sizes=True
        )

        lora_config = LoraConfig(
            r=8, lora_alpha=16, lora_dropout=0.1,
            target_modules=["query_proj", "value_proj"],
            task_type=TaskType.SEQ_CLS,
        )
        model = get_peft_model(model, lora_config)
        if fold_idx == 0:
            model.print_trainable_parameters()

        fold_out = os.path.join(args.output_dir, args.cell,
                                f"fold_{fold_idx}")
        os.makedirs(fold_out, exist_ok=True)

        def compute_metrics(eval_pred):
            logits, labs = eval_pred
            preds = np.argmax(logits, axis=-1)
            return {"accuracy": accuracy_score(labs, preds)}

        training_args = TrainingArguments(
            output_dir=fold_out,
            num_train_epochs=args.epochs,
            per_device_train_batch_size=args.batch_size,
            per_device_eval_batch_size=args.batch_size * 2,
            gradient_accumulation_steps=2,
            learning_rate=args.lr,
            warmup_ratio=0.1,
            weight_decay=0.01,
            fp16=True,
            eval_strategy="epoch",
            save_strategy="epoch",
            save_total_limit=1,
            load_best_model_at_end=True,
            metric_for_best_model="accuracy",
            greater_is_better=True,
            logging_steps=50,
            report_to="none",
            seed=args.seed,
            dataloader_num_workers=0,
        )

        collator = DataCollatorWithPadding(tokenizer=tokenizer)

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_ds,
            eval_dataset=val_ds,
            compute_metrics=compute_metrics,
            data_collator=collator,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=2)],
        )

        trainer.train()

        preds_out = trainer.predict(val_ds)
        preds = np.argmax(preds_out.predictions, axis=-1)
        fold_acc = accuracy_score(val_labels, preds)
        fold_bal_acc = balanced_accuracy_score(val_labels, preds)

        all_preds.extend(preds.tolist())
        all_labels.extend(val_labels)

        fold_time = time.time() - fold_start
        print(f"[FOLD {fold_idx+1}] acc={fold_acc:.4f} "
              f"bal_acc={fold_bal_acc:.4f} time={fold_time:.0f}s")

        fold_results.append({
            "fold": fold_idx,
            "accuracy": round(fold_acc, 4),
            "balanced_accuracy": round(fold_bal_acc, 4),
            "time_seconds": round(fold_time, 1),
        })

        # cleanup checkpoint to save disk
        if os.path.exists(fold_out):
            shutil.rmtree(fold_out, ignore_errors=True)

        del model, trainer
        torch.cuda.empty_cache()

    total_time = time.time() - total_start

    # aggregate
    accs = [r["accuracy"] for r in fold_results]
    cm = confusion_matrix(all_labels, all_preds, labels=[0, 1, 2, 3])
    per_class_recall = {}
    for c in range(4):
        total_c = cm[c].sum()
        per_class_recall[f"d{c}"] = round(cm[c, c] / total_c, 4) if total_c > 0 else 0.0

    results = {
        "cell_name": args.cell,
        "model_name": args.model_name,
        "lora_config": "r=8, alpha=16, query_proj+value_proj",
        "num_samples": len(texts),
        "folds": args.folds,
        "epochs": args.epochs,
        "fold_accuracies": accs,
        "mean_acc": round(float(np.mean(accs)), 4),
        "std_acc": round(float(np.std(accs)), 4),
        "per_class_recall": per_class_recall,
        "confusion_matrix": cm.tolist(),
        "total_time_seconds": round(total_time, 1),
        "fold_details": fold_results,
    }

    out_dir = os.path.join(args.output_dir, args.cell)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[DONE] Results saved to {out_path}")
    print(f"[DONE] Mean acc: {results['mean_acc']:.4f} ± {results['std_acc']:.4f}")
    print(f"[DONE] Per-class recall: {per_class_recall}")
    print(f"[DONE] Total time: {total_time:.0f}s")


if __name__ == "__main__":
    main()
