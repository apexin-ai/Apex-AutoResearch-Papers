"""Evaluate learned classifiers vs rule-based heuristic baselines.

Compares: TF-IDF+LR, DistilBERT, Qwen heuristic, Llama heuristic
on the held-out test set.

Usage:
    python scripts/eval_classifier_vs_heuristic.py
    python scripts/eval_classifier_vs_heuristic.py --models tfidf
    python scripts/eval_classifier_vs_heuristic.py --models tfidf distilbert
    python scripts/eval_classifier_vs_heuristic.py --per-backbone

Input:  data/classifier/test.jsonl + trained models
Output: printed classification reports + confusion matrices
"""
import argparse
import json
import logging
import os
import pickle
import re
import sys
from collections import defaultdict
from typing import Callable, Dict, List, Optional, Tuple

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


# ---------------------------------------------------------------------------
# Heuristic baselines
# ---------------------------------------------------------------------------

def heuristic_qwen(text: str, prev_text: str = "") -> int:
    """Qwen heuristic: char_length < 30 → ack. Paper F1 = 0.845."""
    return 1 if len(text.strip()) < 30 else 0


ACK_KEYWORDS = [
    "i'm glad", "you've broken", "your step-by-step",
    "your rephrased", "i appreciate the", "you've provided",
    "your solution is correct", "the answer is indeed",
]
NONACK_KEYWORDS = [
    "here's another", "i have another", "let's break down",
    "let me solve", "i have a new", "i need help",
    "can you help", "solve this", "please solve",
]
LEN_THRESHOLD = 300
OVERLAP_THRESHOLD = 0.3


def _four_gram_overlap(cur_text: str, prev_text: str) -> float:
    cw = cur_text.lower().split()
    pw = prev_text.lower().split()
    if len(cw) < 4 or len(pw) < 4:
        return 0.0
    c4 = set(tuple(cw[i:i + 4]) for i in range(len(cw) - 3))
    p4 = set(tuple(pw[i:i + 4]) for i in range(len(pw) - 3))
    return len(c4 & p4) / len(c4) if c4 else 0.0


def heuristic_llama(text: str, prev_text: str = "") -> int:
    """Llama heuristic: keyword + 4-gram repetition + char < 300. Paper F1 = 0.805."""
    tl = text.lower()
    if any(kw in tl for kw in NONACK_KEYWORDS):
        return 0
    if "however" in tl[:300]:
        return 0
    if any(kw in tl[:300] for kw in ACK_KEYWORDS):
        return 1
    if len(text.strip()) < LEN_THRESHOLD:
        return 1
    if prev_text and _four_gram_overlap(text, prev_text) > OVERLAP_THRESHOLD:
        return 1
    return 0


def heuristic_combined(text: str, prev_text: str = "", backbone: str = "") -> int:
    """Route to backbone-specific heuristic."""
    if backbone == "qwen":
        return heuristic_qwen(text, prev_text)
    return heuristic_llama(text, prev_text)


# ---------------------------------------------------------------------------
# Model loaders
# ---------------------------------------------------------------------------

def load_tfidf_model():
    path = os.path.join(ARTIFACT_DIR, "tfidf_lr.pkl")
    if not os.path.exists(path):
        log.warning("TF-IDF model not found at %s", path)
        return None
    with open(path, "rb") as f:
        return pickle.load(f)


def load_distilbert_model():
    model_dir = os.path.join(ARTIFACT_DIR, "distilbert_ack")
    if not os.path.exists(model_dir):
        log.warning("DistilBERT model not found at %s", model_dir)
        return None
    try:
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        import torch
    except ImportError:
        log.warning("transformers/torch not available, skipping distilbert")
        return None

    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    model.eval()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    return (model, tokenizer, device)


def predict_tfidf(pipeline, texts: List[str]) -> List[int]:
    return pipeline.predict(texts).tolist()


def predict_distilbert(
    model_tuple, texts: List[str], batch_size: int = 32
) -> List[int]:
    import torch
    model, tokenizer, device = model_tuple
    preds = []
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        inputs = tokenizer(
            batch_texts, padding=True, truncation=True,
            max_length=256, return_tensors="pt"
        ).to(device)
        with torch.no_grad():
            logits = model(**inputs).logits
        batch_preds = torch.argmax(logits, dim=-1).cpu().tolist()
        preds.extend(batch_preds)
    return preds


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def eval_predictions(
    y_true: List[int],
    y_pred: List[int],
    name: str,
) -> Dict[str, float]:
    from sklearn.metrics import (
        accuracy_score, classification_report, confusion_matrix, f1_score,
        precision_score, recall_score,
    )

    acc = accuracy_score(y_true, y_pred)
    f1_mac = f1_score(y_true, y_pred, average="macro")
    f1_ack = f1_score(y_true, y_pred, pos_label=1)
    f1_non = f1_score(y_true, y_pred, pos_label=0)
    prec_ack = precision_score(y_true, y_pred, pos_label=1, zero_division=0)
    rec_ack = recall_score(y_true, y_pred, pos_label=1, zero_division=0)

    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")
    print(classification_report(
        y_true, y_pred,
        target_names=["non_ack", "ack"],
        digits=4,
    ))
    cm = confusion_matrix(y_true, y_pred)
    print("Confusion matrix:")
    print(f"                Pred non_ack  Pred ack")
    print(f"  True non_ack  {cm[0][0]:>10}  {cm[0][1]:>8}")
    print(f"  True ack      {cm[1][0]:>10}  {cm[1][1]:>8}")

    return {
        "accuracy": round(acc, 4),
        "f1_macro": round(f1_mac, 4),
        "f1_ack": round(f1_ack, 4),
        "f1_non_ack": round(f1_non, 4),
        "precision_ack": round(prec_ack, 4),
        "recall_ack": round(rec_ack, 4),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate ack classifiers vs heuristic baselines."
    )
    parser.add_argument(
        "--models", nargs="*", default=None,
        choices=["tfidf", "distilbert"],
        help="Which learned models to evaluate (default: all available)."
    )
    parser.add_argument(
        "--per-backbone", action="store_true",
        help="Also report per-backbone breakdown."
    )
    parser.add_argument(
        "--output", default=None,
        help="Save results JSON to this path."
    )
    args = parser.parse_args()

    test_path = os.path.join(DATA_DIR, "test.jsonl")
    test_recs = load_jsonl(test_path)
    log.info("Loaded %d test records", len(test_recs))

    texts = [r["text"] for r in test_recs]
    prev_texts = [r.get("prev_text", "") for r in test_recs]
    labels = [r["label"] for r in test_recs]
    backbones = [r["backbone"] for r in test_recs]

    results = {}

    # --- Heuristic baselines ---
    heur_qwen_preds = [heuristic_qwen(t, p) for t, p in zip(texts, prev_texts)]
    results["heuristic_qwen"] = eval_predictions(labels, heur_qwen_preds, "Heuristic: Qwen (char < 30)")

    heur_llama_preds = [heuristic_llama(t, p) for t, p in zip(texts, prev_texts)]
    results["heuristic_llama"] = eval_predictions(labels, heur_llama_preds, "Heuristic: Llama (keyword + 4-gram + len)")

    heur_comb_preds = [
        heuristic_combined(t, p, b)
        for t, p, b in zip(texts, prev_texts, backbones)
    ]
    results["heuristic_combined"] = eval_predictions(labels, heur_comb_preds, "Heuristic: Combined (backbone-specific)")

    # --- Learned models ---
    model_list = args.models
    if model_list is None:
        model_list = ["tfidf", "distilbert"]

    if "tfidf" in model_list:
        tfidf = load_tfidf_model()
        if tfidf is not None:
            tfidf_preds = predict_tfidf(tfidf, texts)
            results["tfidf_lr"] = eval_predictions(labels, tfidf_preds, "TF-IDF + Logistic Regression")

    if "distilbert" in model_list:
        db = load_distilbert_model()
        if db is not None:
            db_preds = predict_distilbert(db, texts)
            results["distilbert"] = eval_predictions(labels, db_preds, "DistilBERT (fine-tuned)")

    # --- Summary table ---
    print(f"\n{'='*60}")
    print("  Summary")
    print(f"{'='*60}")
    print(f"{'Method':<35} {'Acc':>6} {'F1-mac':>7} {'F1-ack':>7} {'P-ack':>6} {'R-ack':>6}")
    print("-" * 70)
    for name, metrics in results.items():
        print(
            f"{name:<35} "
            f"{metrics['accuracy']:>6.4f} "
            f"{metrics['f1_macro']:>7.4f} "
            f"{metrics['f1_ack']:>7.4f} "
            f"{metrics['precision_ack']:>6.4f} "
            f"{metrics['recall_ack']:>6.4f}"
        )

    # --- Per-backbone breakdown ---
    if args.per_backbone:
        print(f"\n{'='*60}")
        print("  Per-backbone breakdown")
        print(f"{'='*60}")
        for bb in sorted(set(backbones)):
            idx = [i for i, b in enumerate(backbones) if b == bb]
            bb_labels = [labels[i] for i in idx]
            bb_texts = [texts[i] for i in idx]
            bb_prev = [prev_texts[i] for i in idx]

            print(f"\n--- {bb} (n={len(idx)}, ack={sum(bb_labels)}) ---")
            for method_name in results:
                if method_name == "heuristic_qwen":
                    preds = [heuristic_qwen(t, p) for t, p in zip(bb_texts, bb_prev)]
                elif method_name == "heuristic_llama":
                    preds = [heuristic_llama(t, p) for t, p in zip(bb_texts, bb_prev)]
                elif method_name == "heuristic_combined":
                    preds = [heuristic_combined(t, p, bb) for t, p in zip(bb_texts, bb_prev)]
                elif method_name == "tfidf_lr" and "tfidf" in model_list:
                    tfidf = load_tfidf_model()
                    if tfidf is None:
                        continue
                    preds = predict_tfidf(tfidf, bb_texts)
                elif method_name == "distilbert" and "distilbert" in model_list:
                    db = load_distilbert_model()
                    if db is None:
                        continue
                    preds = predict_distilbert(db, bb_texts)
                else:
                    continue

                from sklearn.metrics import f1_score, accuracy_score
                f1 = f1_score(bb_labels, preds, average="macro")
                acc = accuracy_score(bb_labels, preds)
                f1_ack = f1_score(bb_labels, preds, pos_label=1)
                print(f"  {method_name:<30} acc={acc:.4f} F1-mac={f1:.4f} F1-ack={f1_ack:.4f}")

    # --- Save results ---
    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        log.info("Results saved to %s", args.output)


if __name__ == "__main__":
    main()
