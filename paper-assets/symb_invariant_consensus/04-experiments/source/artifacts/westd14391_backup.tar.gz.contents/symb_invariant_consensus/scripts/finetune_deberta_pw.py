#!/usr/bin/env python3
"""Fine-tune DeBERTa-large-mnli on ProofWriter for NLI classification.

Usage:
    python scripts/finetune_deberta_pw.py --epochs 5 --lr 2e-5 --batch-size 16
    python scripts/finetune_deberta_pw.py --dry-run
    python scripts/finetune_deberta_pw.py --depth-filter D5  # only depth-5 training data
"""

# Environment setup for westd-16639:
#   export CUDA_VISIBLE_DEVICES=<free_gpu_id>
#   export LD_LIBRARY_PATH=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib:$LD_LIBRARY_PATH


import argparse
import json
import os
import numpy as np
import torch
from collections import Counter
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    TrainingArguments, Trainer, EarlyStoppingCallback,
    DataCollatorWithPadding
)
from sklearn.metrics import accuracy_score

MODEL_PATH = "/root/autodl-tmp/models/deberta-large-mnli"
PW_VAL_PATH = "/root/symb_invariant_consensus/data/proofwriter_full.json"
DEFAULT_OUTPUT_DIR = "/root/symb_invariant_consensus/checkpoints/deberta-large-pw-finetuned"

PW_TO_NLI = {"True": 2, "False": 0, "Unknown": 1}
NLI_TO_PW = {2: "True", 0: "False", 1: "Unknown"}
HF_ANSWER_MAP = {"A": "True", "B": "False", "C": "Unknown"}


def parse_pw_problem(text):
    for m in [
        "Determine whether the following statement is true, false, or unknown:\n",
        "Determine whether the following statement is True, False, or Unknown:\n",
    ]:
        i = text.find(m)
        if i != -1:
            return text[:i].strip(), text[i + len(m):].strip()
    return text, ""


def load_hf_train(depth_filter=None):
    from datasets import load_dataset
    print("Loading tasksource/proofwriter train split...")
    ds = load_dataset("tasksource/proofwriter", split="train", )
    print(f"Total: {len(ds)}, columns: {ds.column_names}")

    configs = Counter(ds["config"])
    print("Config distribution:")
    for c in sorted(configs):
        print(f"  {c}: {configs[c]}")

    indices = [i for i, c in enumerate(ds["config"]) if "OWA" in c]
    if not indices:
        print("No OWA configs found, using all data")
        indices = list(range(len(ds)))
    ds = ds.select(indices)
    print(f"OWA filtered: {len(ds)}")

    if depth_filter:
        indices = [i for i, c in enumerate(ds["config"]) if depth_filter.upper() in c.upper()]
        if indices:
            ds = ds.select(indices)
            print(f"Depth '{depth_filter}' filtered: {len(ds)}")
        else:
            print(f"WARNING: No rows match depth filter '{depth_filter}', using all OWA data")

    examples = []
    for row in ds:
        ctx = row["theory"].strip()
        q = row["question"].strip()
        prefix = "Based on the above information, is the following statement true, false, or unknown? "
        hyp = q[len(prefix):] if q.startswith(prefix) else q
        label_str = HF_ANSWER_MAP.get(row["answer"], row["answer"])
        if label_str not in PW_TO_NLI:
            continue
        examples.append({
            "premise": ctx, "hypothesis": hyp,
            "label": PW_TO_NLI[label_str], "label_str": label_str,
        })

    print(f"Train examples: {len(examples)}, dist: {dict(Counter(e['label_str'] for e in examples))}")
    return examples


def load_local_train(path, depth_filter=None):
    """Load training data from local JSONL (same format as HF tasksource/proofwriter)."""
    import json
    print(f"Loading local training data: {path}")
    rows = []
    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))
    print(f"Total rows: {len(rows)}")

    if depth_filter:
        rows = [r for r in rows if depth_filter.upper() in r.get("config", "").upper()]
        print(f"Depth '{depth_filter}' filtered: {len(rows)}")

    owa_rows = [r for r in rows if "OWA" in r.get("config", "")]
    if owa_rows:
        rows = owa_rows
        print(f"OWA filtered: {len(rows)}")

    examples = []
    for row in rows:
        ctx = row["context"].strip()
        q = row["question"].strip()
        prefix = "Based on the above information, is the following statement true, false, or unknown? "
        hyp = q[len(prefix):] if q.startswith(prefix) else q
        label_str = HF_ANSWER_MAP.get(row["answer"], row["answer"])
        if label_str not in PW_TO_NLI:
            continue
        examples.append({
            "premise": ctx, "hypothesis": hyp,
            "label": PW_TO_NLI[label_str], "label_str": label_str,
        })

    print(f"Train examples: {len(examples)}, dist: {dict(Counter(e['label_str'] for e in examples))}")
    return examples



def load_val():
    with open(PW_VAL_PATH) as f:
        data = json.load(f)
    examples = []
    for item in data:
        p, h = parse_pw_problem(item["problem"])
        if not h:
            continue
        examples.append({
            "id": item["id"], "premise": p, "hypothesis": h,
            "label": PW_TO_NLI[item["answer"]], "label_str": item["answer"],
        })
    print(f"Val examples: {len(examples)}, dist: {dict(Counter(e['label_str'] for e in examples))}")
    return examples


def remove_overlap(train_examples, val_examples):
    val_sigs = set()
    for e in val_examples:
        sig = (e["premise"][:100].strip().lower(), e["hypothesis"].strip().lower())
        val_sigs.add(sig)

    filtered = []
    for e in train_examples:
        sig = (e["premise"][:100].strip().lower(), e["hypothesis"].strip().lower())
        if sig not in val_sigs:
            filtered.append(e)

    removed = len(train_examples) - len(filtered)
    if removed:
        print(f"Removed {removed} overlapping examples from training data")
    return filtered


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    acc = accuracy_score(labels, preds)
    result = {"accuracy": acc}
    for lid, lstr in NLI_TO_PW.items():
        mask = labels == lid
        if mask.sum() > 0:
            result[f"acc_{lstr}"] = float(accuracy_score(labels[mask], preds[mask]))
    return result


def main():
    parser = argparse.ArgumentParser(description="Fine-tune DeBERTa-large-mnli on ProofWriter")
    parser.add_argument("--model-path", default=MODEL_PATH)
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--warmup-ratio", type=float, default=0.1)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--depth-filter", default=None, help="e.g. 'D5' to only use depth-5 training data")
    parser.add_argument("--train-data", default=None,
                        help="Path to local training data JSONL (fallback if HF download fails)")
    parser.add_argument("--max-steps", type=int, default=-1)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--gradient-accumulation", type=int, default=1)
    parser.add_argument("--patience", type=int, default=2)
    args = parser.parse_args()

    if args.dry_run:
        args.max_steps = 2
        args.batch_size = 2
        args.output_dir += "-dryrun"
        print("=== DRY RUN ===\n")

    os.makedirs(args.output_dir, exist_ok=True)

    print(f"Loading model: {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    model = AutoModelForSequenceClassification.from_pretrained(args.model_path)
    print(f"id2label: {model.config.id2label}")

    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)} ({torch.cuda.get_device_properties(0).total_memory // 1024**3}GB)")

    val_examples = load_val()

    if args.dry_run:
        # Dry-run uses local val data split 80/20 (avoids slow HF download)
        import random
        random.seed(args.seed)
        shuffled = list(val_examples)
        random.shuffle(shuffled)
        split = int(len(shuffled) * 0.8)
        train_examples = shuffled[:split]
        val_examples = shuffled[split:]
        print(f"Dry-run: using local data split {len(train_examples)}/{len(val_examples)}")
    else:
        if args.train_data:
            train_examples = load_local_train(args.train_data, args.depth_filter)
        else:
            local_jsonl = "/root/symb_invariant_consensus/data/proofwriter_train_hf.jsonl"
            if os.path.exists(local_jsonl):
                train_examples = load_local_train(local_jsonl, args.depth_filter)
            else:
                train_examples = load_hf_train(args.depth_filter)
        train_examples = remove_overlap(train_examples, val_examples)

    # Token length analysis
    sample = (train_examples[:200] + val_examples[:200])
    lengths = []
    for ex in sample:
        toks = tokenizer(ex["premise"], ex["hypothesis"], truncation=False)
        lengths.append(len(toks["input_ids"]))
    lengths = np.array(lengths)
    print(f"\nToken lengths (n={len(lengths)}): mean={lengths.mean():.0f} med={np.median(lengths):.0f} "
          f"P95={np.percentile(lengths,95):.0f} P99={np.percentile(lengths,99):.0f} max={lengths.max()}")
    trunc = (lengths > args.max_length).sum()
    print(f"Truncated at {args.max_length}: {trunc}/{len(lengths)} ({trunc/len(lengths)*100:.1f}%)")

    from datasets import Dataset

    def make_ds(examples):
        d = Dataset.from_dict({
            "premise": [e["premise"] for e in examples],
            "hypothesis": [e["hypothesis"] for e in examples],
            "label": [e["label"] for e in examples],
        })
        return d.map(
            lambda x: tokenizer(x["premise"], x["hypothesis"],
                                truncation=True, max_length=args.max_length, padding=False),
            batched=True, remove_columns=["premise", "hypothesis"],
        )

    train_ds = make_ds(train_examples)
    val_ds = make_ds(val_examples)
    print(f"\nDatasets: train={len(train_ds)}, val={len(val_ds)}")

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size * 2,
        gradient_accumulation_steps=args.gradient_accumulation,
        learning_rate=args.lr,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
        greater_is_better=True,
        save_total_limit=2,
        seed=args.seed,
        logging_steps=50,
        # DeBERTa v1 has attention mask overflow with fp16/bf16; use fp32
        # DeBERTa v2/v3 works fine with mixed precision
        fp16=False,
        bf16=False,
        max_steps=args.max_steps,
        report_to="none",
        dataloader_num_workers=4,
    )

    model.gradient_checkpointing_enable()

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=args.patience)],
    )

    print("\n=== Training ===")
    result = trainer.train()
    print(f"Training metrics: {result.metrics}")

    print("\n=== Final Evaluation ===")
    eval_result = trainer.evaluate()
    print(f"Val accuracy: {eval_result['eval_accuracy']:.4f}")
    for k, v in sorted(eval_result.items()):
        if "acc_" in k:
            print(f"  {k}: {v:.4f}")

    best_dir = os.path.join(args.output_dir, "best")
    trainer.save_model(best_dir)
    tokenizer.save_pretrained(best_dir)

    config = {
        "base_model": args.model_path,
        "epochs": args.epochs,
        "lr": args.lr,
        "batch_size": args.batch_size,
        "max_length": args.max_length,
        "depth_filter": args.depth_filter,
        "train_size": len(train_ds),
        "val_size": len(val_ds),
        "val_accuracy": eval_result["eval_accuracy"],
        "per_class": {k: v for k, v in eval_result.items() if "acc_" in k},
        "training_metrics": result.metrics,
    }
    with open(os.path.join(args.output_dir, "training_config.json"), "w") as f:
        json.dump(config, f, indent=2, default=str)

    print(f"\nCheckpoint: {best_dir}")
    print(f"Config: {os.path.join(args.output_dir, 'training_config.json')}")


if __name__ == "__main__":
    main()
