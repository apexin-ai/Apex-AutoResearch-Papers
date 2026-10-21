"""
Train a ModernBERT-base binary classifier: human vs synthetic text.

Pipeline position: Step 2 — takes depth-0 human data + synthetic JSONL from generate_synthetic.py,
trains a calibrated detector whose output q(x) = sigmoid(logit / T) is used by downstream alpha_eff.py.

Output: model checkpoint, calibration_results.json, predictions.jsonl.
"""

import argparse
import json
import os
import random
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import f1_score, roc_auc_score
from torch.utils.data import Dataset
from tqdm import tqdm
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    EarlyStoppingCallback,
    Trainer,
    TrainingArguments,
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fine-tune ModernBERT-base as a human vs synthetic text detector with temperature scaling."
    )
    parser.add_argument("--human_data_dir", type=str, required=True,
                        help="Directory of human text JSONL files")
    parser.add_argument("--synthetic_data_dir", type=str, required=True,
                        help="Directory of synthetic text JSONL files")
    parser.add_argument("--output_dir", type=str, required=True,
                        help="Output directory for model and results")
    parser.add_argument("--model_name", type=str, default="answerdotai/ModernBERT-base",
                        help="Base model for classification")
    parser.add_argument("--max_length", type=int, default=512,
                        help="Max token length")
    parser.add_argument("--batch_size", type=int, default=32,
                        help="Training batch size")
    parser.add_argument("--learning_rate", type=float, default=2e-5,
                        help="Learning rate")
    parser.add_argument("--num_epochs", type=int, default=3,
                        help="Number of training epochs")
    parser.add_argument("--warmup_ratio", type=float, default=0.1,
                        help="Warmup ratio for lr scheduler")
    parser.add_argument("--eval_steps", type=int, default=500,
                        help="Evaluation interval in steps")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed")
    parser.add_argument("--use_wandb", action="store_true",
                        help="Enable W&B logging")
    parser.add_argument("--wandb_project", type=str, default="provenance-detector",
                        help="W&B project name")
    return parser.parse_args()


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_jsonl_texts(data_dir):
    """Load all texts from JSONL files in a directory."""
    texts = []
    data_dir = Path(data_dir)
    for fpath in sorted(data_dir.glob("*.jsonl")):
        with open(fpath, "r") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                    text = rec.get("text", "")
                    if text.strip():
                        texts.append(text)
                except json.JSONDecodeError:
                    continue
    return texts


def build_balanced_dataset(human_texts, synthetic_texts, seed):
    """Balance classes by undersampling the majority class, then split 80/10/10."""
    rng = random.Random(seed)
    min_size = min(len(human_texts), len(synthetic_texts))
    if len(human_texts) > min_size:
        human_texts = rng.sample(human_texts, min_size)
    elif len(synthetic_texts) > min_size:
        synthetic_texts = rng.sample(synthetic_texts, min_size)

    data = [(t, 0) for t in human_texts] + [(t, 1) for t in synthetic_texts]
    rng.shuffle(data)

    n = len(data)
    n_train = int(0.8 * n)
    n_val = int(0.1 * n)

    train_data = data[:n_train]
    val_data = data[n_train:n_train + n_val]
    test_data = data[n_train + n_val:]

    print(f"Dataset: {n} total ({min_size} per class)")
    print(f"  Train: {len(train_data)}, Val: {len(val_data)}, Test: {len(test_data)}")
    return train_data, val_data, test_data


class TextClassificationDataset(Dataset):
    def __init__(self, data, tokenizer, max_length):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text, label = self.data[idx]
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            truncation=True,
            padding="max_length",
            return_tensors="pt",
        )
        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "labels": torch.tensor(label, dtype=torch.long),
        }


class TemperatureScaling(nn.Module):
    """Learns a single temperature parameter T to calibrate logits.

    Calibrated probability: q(x) = sigmoid(logit / T)
    T is optimized via NLL on validation logits.
    """

    def __init__(self, init_temperature=1.5):
        super().__init__()
        self.temperature = nn.Parameter(torch.tensor(init_temperature))

    def forward(self, logits):
        return logits / self.temperature

    def calibrate(self, logits, labels, lr=0.01, max_iter=500):
        """Fit T on validation set by minimizing NLL."""
        self.cuda() if logits.is_cuda else self.cpu()
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.LBFGS([self.temperature], lr=lr, max_iter=max_iter)

        def closure():
            optimizer.zero_grad()
            scaled = self.forward(logits)
            loss = criterion(scaled, labels)
            loss.backward()
            return loss

        optimizer.step(closure)
        return self.temperature.item()


def collect_logits_and_labels(trainer, dataset):
    """Run inference and collect raw logits + labels."""
    output = trainer.predict(dataset)
    logits = torch.tensor(output.predictions, dtype=torch.float32)
    labels = torch.tensor(output.label_ids, dtype=torch.long)
    return logits, labels


def compute_ece(probs, labels, n_bins=15):
    """Expected Calibration Error with equal-width bins."""
    bin_boundaries = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    bin_data = []
    for i in range(n_bins):
        lo, hi = bin_boundaries[i], bin_boundaries[i + 1]
        mask = (probs >= lo) & (probs < hi)
        if i == n_bins - 1:
            mask = (probs >= lo) & (probs <= hi)
        if mask.sum() == 0:
            bin_data.append({"bin_lo": lo, "bin_hi": hi, "count": 0,
                             "avg_confidence": 0, "avg_accuracy": 0})
            continue
        bin_probs = probs[mask]
        bin_labels = labels[mask]
        avg_conf = bin_probs.mean()
        avg_acc = bin_labels.mean()
        bin_size = mask.sum()
        ece += (bin_size / len(probs)) * abs(avg_conf - avg_acc)
        bin_data.append({
            "bin_lo": float(lo), "bin_hi": float(hi),
            "count": int(bin_size),
            "avg_confidence": float(avg_conf),
            "avg_accuracy": float(avg_acc),
        })
    return float(ece), bin_data


def compute_metrics_fn(eval_pred):
    """Metrics function for HF Trainer."""
    logits, labels = eval_pred
    probs = torch.softmax(torch.tensor(logits, dtype=torch.float32), dim=-1)[:, 1].numpy()
    preds = (probs >= 0.5).astype(int)
    auc = roc_auc_score(labels, probs)
    f1_human = f1_score(labels, preds, pos_label=0)
    f1_synthetic = f1_score(labels, preds, pos_label=1)
    return {
        "auc": auc,
        "f1_human": f1_human,
        "f1_synthetic": f1_synthetic,
        "eval_auc": auc,
    }


def save_predictions(logits, labels, temperature, output_path, split_name):
    """Save per-sample predictions to JSONL."""
    scaled_logits = logits / temperature
    probs = torch.softmax(scaled_logits, dim=-1)[:, 1].numpy()
    preds = (probs >= 0.5).astype(int)
    records = []
    for i in range(len(labels)):
        records.append({
            "split": split_name,
            "label": int(labels[i]),
            "predicted": int(preds[i]),
            "prob_synthetic": float(probs[i]),
            "logit_0": float(logits[i][0]),
            "logit_1": float(logits[i][1]),
            "temperature": temperature,
        })
    with open(output_path, "a") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")
    return records


def main():
    args = parse_args()
    set_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    if args.use_wandb:
        os.environ["WANDB_PROJECT"] = args.wandb_project
    else:
        os.environ["WANDB_DISABLED"] = "true"

    print("Loading data...")
    human_texts = load_jsonl_texts(args.human_data_dir)
    synthetic_texts = load_jsonl_texts(args.synthetic_data_dir)
    print(f"Loaded {len(human_texts)} human, {len(synthetic_texts)} synthetic texts")

    if not human_texts or not synthetic_texts:
        raise ValueError("Both human and synthetic data directories must contain JSONL files with text.")

    train_data, val_data, test_data = build_balanced_dataset(
        human_texts, synthetic_texts, args.seed
    )

    print(f"Loading tokenizer and model: {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    model = AutoModelForSequenceClassification.from_pretrained(
        args.model_name,
        num_labels=2,
        trust_remote_code=True,
        classifier_dropout=0.1,
    )

    train_dataset = TextClassificationDataset(train_data, tokenizer, args.max_length)
    val_dataset = TextClassificationDataset(val_data, tokenizer, args.max_length)
    test_dataset = TextClassificationDataset(test_data, tokenizer, args.max_length)

    training_args = TrainingArguments(
        output_dir=os.path.join(args.output_dir, "checkpoints"),
        num_train_epochs=args.num_epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size * 2,
        learning_rate=args.learning_rate,
        warmup_ratio=args.warmup_ratio,
        lr_scheduler_type="linear",
        eval_strategy="steps",
        eval_steps=args.eval_steps,
        save_strategy="steps",
        save_steps=args.eval_steps,
        load_best_model_at_end=True,
        metric_for_best_model="eval_auc",
        greater_is_better=True,
        save_total_limit=3,
        logging_steps=50,
        fp16=torch.cuda.is_available(),
        dataloader_num_workers=4,
        seed=args.seed,
        report_to="wandb" if args.use_wandb else "none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        compute_metrics=compute_metrics_fn,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=3)],
    )

    print("Starting training...")
    trainer.train()

    # --- Temperature Scaling Calibration ---
    print("Calibrating with temperature scaling on validation set...")
    val_logits, val_labels = collect_logits_and_labels(trainer, val_dataset)

    temp_scaler = TemperatureScaling(init_temperature=1.5)
    device = val_logits.device
    optimal_T = temp_scaler.calibrate(val_logits.to(device), val_labels.to(device))
    print(f"Optimal temperature: {optimal_T:.4f}")

    # --- Evaluation ---
    print("Evaluating on val and test sets...")
    test_logits, test_labels = collect_logits_and_labels(trainer, test_dataset)

    results = {}
    for split_name, logits, labels in [("val", val_logits, val_labels), ("test", test_logits, test_labels)]:
        scaled_logits = logits / optimal_T
        probs = torch.softmax(scaled_logits, dim=-1)[:, 1].numpy()
        preds = (probs >= 0.5).astype(int)
        labels_np = labels.numpy()

        auc = roc_auc_score(labels_np, probs)
        f1_h = f1_score(labels_np, preds, pos_label=0)
        f1_s = f1_score(labels_np, preds, pos_label=1)
        ece, bin_data = compute_ece(probs, labels_np, n_bins=15)

        results[split_name] = {
            "auc": auc,
            "ece": ece,
            "f1_human": f1_h,
            "f1_synthetic": f1_s,
            "calibration_bins": bin_data,
        }
        print(f"  {split_name}: AUC={auc:.4f}, ECE={ece:.4f}, F1_human={f1_h:.4f}, F1_synthetic={f1_s:.4f}")

    calibration_output = {
        "temperature": optimal_T,
        "val": results["val"],
        "test": results["test"],
    }
    cal_path = os.path.join(args.output_dir, "calibration_results.json")
    with open(cal_path, "w") as f:
        json.dump(calibration_output, f, indent=2)
    print(f"Calibration results saved to {cal_path}")

    # --- Save predictions ---
    pred_path = os.path.join(args.output_dir, "predictions.jsonl")
    if os.path.exists(pred_path):
        os.remove(pred_path)
    save_predictions(val_logits, val_labels, optimal_T, pred_path, "val")
    save_predictions(test_logits, test_labels, optimal_T, pred_path, "test")
    print(f"Predictions saved to {pred_path}")

    # --- Save model + temperature ---
    model_save_dir = os.path.join(args.output_dir, "final_model")
    trainer.save_model(model_save_dir)
    tokenizer.save_pretrained(model_save_dir)
    torch.save({"temperature": optimal_T}, os.path.join(model_save_dir, "temperature.pt"))
    print(f"Model and temperature saved to {model_save_dir}")


if __name__ == "__main__":
    main()
