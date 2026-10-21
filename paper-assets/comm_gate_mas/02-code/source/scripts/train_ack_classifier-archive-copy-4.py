"""Train binary ack classifier (ack vs non-ack).

Two models:
  (a) TF-IDF + Logistic Regression (CPU, fast)
  (b) Fine-tuned DistilBERT (GPU recommended)

Usage:
    python scripts/train_ack_classifier.py --model tfidf
    python scripts/train_ack_classifier.py --model distilbert --dry-run
    python scripts/train_ack_classifier.py --model distilbert

Input:  data/classifier/train.jsonl, data/classifier/val.jsonl
Output: artifacts/classifier/tfidf_lr.pkl  OR  artifacts/classifier/distilbert_ack/
"""
import argparse
import json
import logging
import os
import pickle
import sys
from typing import Dict, List, Optional, Tuple

import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data", "classifier")
ARTIFACT_DIR = os.path.join(PROJECT_ROOT, "artifacts", "classifier")


def load_jsonl(path: str) -> List[dict]:
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def load_data(
    dry_run: bool = False,
) -> Tuple[List[str], List[int], List[str], List[int]]:
    train_recs = load_jsonl(os.path.join(DATA_DIR, "train.jsonl"))
    val_recs = load_jsonl(os.path.join(DATA_DIR, "val.jsonl"))

    if dry_run:
        train_recs = train_recs[:10]
        val_recs = val_recs[:10]

    train_texts = [r["text"] for r in train_recs]
    train_labels = [r["label"] for r in train_recs]
    val_texts = [r["text"] for r in val_recs]
    val_labels = [r["label"] for r in val_recs]

    log.info(
        "Loaded: train=%d (ack=%d), val=%d (ack=%d)",
        len(train_texts), sum(train_labels),
        len(val_texts), sum(val_labels),
    )
    return train_texts, train_labels, val_texts, val_labels


# ---------------------------------------------------------------------------
# (a) TF-IDF + Logistic Regression
# ---------------------------------------------------------------------------

def train_tfidf(
    train_texts: List[str],
    train_labels: List[int],
    val_texts: List[str],
    val_labels: List[int],
    dry_run: bool = False,
) -> None:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import classification_report, f1_score
    from sklearn.model_selection import cross_val_score
    from sklearn.pipeline import Pipeline

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            analyzer="char_wb",
            ngram_range=(2, 5),
            max_features=50000,
            sublinear_tf=True,
        )),
        ("lr", LogisticRegression(
            class_weight="balanced",
            max_iter=1000,
            C=1.0,
            solver="lbfgs",
        )),
    ])

    pipeline_word = Pipeline([
        ("tfidf", TfidfVectorizer(
            analyzer="word",
            ngram_range=(1, 2),
            max_features=30000,
            sublinear_tf=True,
        )),
        ("lr", LogisticRegression(
            class_weight="balanced",
            max_iter=1000,
            C=1.0,
            solver="lbfgs",
        )),
    ])

    from sklearn.feature_extraction.text import TfidfVectorizer as TV
    from sklearn.pipeline import FeatureUnion

    combined_pipeline = Pipeline([
        ("features", FeatureUnion([
            ("char", TfidfVectorizer(
                analyzer="char_wb",
                ngram_range=(2, 5),
                max_features=50000,
                sublinear_tf=True,
            )),
            ("word", TfidfVectorizer(
                analyzer="word",
                ngram_range=(1, 2),
                max_features=30000,
                sublinear_tf=True,
            )),
        ])),
        ("lr", LogisticRegression(
            class_weight="balanced",
            max_iter=1000,
            C=1.0,
            solver="lbfgs",
        )),
    ])

    if not dry_run:
        log.info("Running 5-fold CV on train set...")
        cv_scores = cross_val_score(
            combined_pipeline, train_texts, train_labels,
            cv=5, scoring="f1_macro", n_jobs=-1,
        )
        log.info("CV F1-macro: %.4f (+/- %.4f)", cv_scores.mean(), cv_scores.std())

    log.info("Fitting combined TF-IDF + LR on full train set...")
    combined_pipeline.fit(train_texts, train_labels)

    val_preds = combined_pipeline.predict(val_texts)
    log.info("Validation results:")
    print(classification_report(
        val_labels, val_preds,
        target_names=["non_ack", "ack"],
        digits=4,
    ))

    out_path = os.path.join(ARTIFACT_DIR, "tfidf_lr.pkl")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "wb") as f:
        pickle.dump(combined_pipeline, f)
    log.info("Saved model to %s", out_path)


# ---------------------------------------------------------------------------
# (b) DistilBERT fine-tuning
# ---------------------------------------------------------------------------

def train_distilbert(
    train_texts: List[str],
    train_labels: List[int],
    val_texts: List[str],
    val_labels: List[int],
    dry_run: bool = False,
) -> None:
    import torch
    from transformers import (
        AutoModelForSequenceClassification,
        AutoTokenizer,
        Trainer,
        TrainingArguments,
    )
    from datasets import Dataset

    model_name = "distilbert-base-uncased"
    out_dir = os.path.join(ARTIFACT_DIR, "distilbert_ack")
    os.makedirs(out_dir, exist_ok=True)

    log.info("Loading tokenizer and model: %s", model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        model_name, num_labels=2
    )

    def tokenize_fn(examples):
        return tokenizer(
            examples["text"],
            padding="max_length",
            truncation=True,
            max_length=256,
        )

    train_ds = Dataset.from_dict({"text": train_texts, "label": train_labels})
    val_ds = Dataset.from_dict({"text": val_texts, "label": val_labels})

    train_ds = train_ds.map(tokenize_fn, batched=True, remove_columns=["text"])
    val_ds = val_ds.map(tokenize_fn, batched=True, remove_columns=["text"])

    train_ds.set_format("torch")
    val_ds.set_format("torch")

    n_ack = sum(train_labels)
    n_total = len(train_labels)
    pos_weight = (n_total - n_ack) / max(n_ack, 1)

    class WeightedTrainer(Trainer):
        def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
            labels = inputs.pop("labels")
            outputs = model(**inputs)
            logits = outputs.logits
            weight = torch.tensor(
                [1.0, pos_weight], device=logits.device, dtype=logits.dtype
            )
            loss = torch.nn.functional.cross_entropy(logits, labels, weight=weight)
            return (loss, outputs) if return_outputs else loss

    num_epochs = 1 if dry_run else 3
    eval_steps = 5 if dry_run else 100

    training_args = TrainingArguments(
        output_dir=out_dir,
        num_train_epochs=num_epochs,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=32,
        learning_rate=2e-5,
        warmup_ratio=0.1,
        weight_decay=0.01,
        eval_strategy="steps",
        eval_steps=eval_steps,
        save_strategy="steps",
        save_steps=eval_steps,
        load_best_model_at_end=True,
        metric_for_best_model="f1_macro",
        greater_is_better=True,
        logging_steps=10 if not dry_run else 2,
        save_total_limit=2,
        fp16=torch.cuda.is_available(),
        dataloader_num_workers=0,
        report_to="none",
        max_steps=10 if dry_run else -1,
    )

    def compute_metrics(eval_pred):
        from sklearn.metrics import f1_score, accuracy_score
        logits, labels = eval_pred
        preds = np.argmax(logits, axis=-1)
        return {
            "accuracy": accuracy_score(labels, preds),
            "f1_macro": f1_score(labels, preds, average="macro"),
            "f1_ack": f1_score(labels, preds, pos_label=1),
            "f1_non_ack": f1_score(labels, preds, pos_label=0),
        }

    trainer = WeightedTrainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        compute_metrics=compute_metrics,
    )

    log.info("Starting training (epochs=%d, dry_run=%s)...", num_epochs, dry_run)
    trainer.train()

    val_results = trainer.evaluate()
    log.info("Validation results: %s", json.dumps(val_results, indent=2))

    trainer.save_model(out_dir)
    tokenizer.save_pretrained(out_dir)
    log.info("Saved model to %s", out_dir)


def main():
    parser = argparse.ArgumentParser(description="Train binary ack classifier.")
    parser.add_argument(
        "--model", choices=["tfidf", "distilbert"], required=True,
        help="Model type: tfidf (CPU) or distilbert (GPU recommended)."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Run on 10 samples to verify pipeline works."
    )
    args = parser.parse_args()

    train_texts, train_labels, val_texts, val_labels = load_data(
        dry_run=args.dry_run
    )

    if args.model == "tfidf":
        train_tfidf(train_texts, train_labels, val_texts, val_labels,
                     dry_run=args.dry_run)
    elif args.model == "distilbert":
        train_distilbert(train_texts, train_labels, val_texts, val_labels,
                         dry_run=args.dry_run)


if __name__ == "__main__":
    main()
