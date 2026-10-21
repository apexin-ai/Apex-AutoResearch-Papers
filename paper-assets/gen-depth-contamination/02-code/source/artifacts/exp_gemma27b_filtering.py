#!/usr/bin/env python3
"""Gemma-2-27B filtering effectiveness evaluation.

Tests OBD binary filtering on Gemma-2-27B generated text (harder to detect
than Qwen-1.5B, cross-scorer AUC=0.887). Three strategies:
  - no_filter: 50% contaminated corpus, no filtering
  - binary_ours: train LightGBM on 15D OBD features, filter predicted contaminated
  - graduated_a09: weight docs by 0.9^depth (oracle depth)

Downstream: Qwen2.5-1.5B + LoRA rank=4, eval on MMLU + HellaSwag.

Usage:
    python scripts/exp_gemma27b_filtering.py --strategy no_filter --seed 42 --device cuda:3
    python scripts/exp_gemma27b_filtering.py --strategy binary_ours --seed 42 --device cuda:3
    python scripts/exp_gemma27b_filtering.py --strategy graduated_a09 --seed 42 --device cuda:3
"""

import argparse
import csv
import gc
import json
import logging
import os
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
os.environ.setdefault("HF_DATASETS_OFFLINE", "1")
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
import sys
import time
from pathlib import Path

import numpy as np
import torch

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path("/root/autodl-tmp/gen-depth-contamination")
MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B"
DATA_DIR = PROJECT_ROOT / "data" / "exp_gemma27b_c4"
FEATURES_CSV = PROJECT_ROOT / "data" / "exp_gemma27b_c4_qwen_scorer" / "features.csv"

TOTAL_DOCS = 5000
CONTAMINATION_RATE = 50  # percent
MAX_DEPTH = 5
GRADUATED_ALPHA = 0.9

LORA_RANK = 4
LORA_ALPHA = 8
LORA_TARGET_MODULES = ["q_proj", "v_proj"]
LORA_DROPOUT = 0.05

TRAIN_LR = 2e-4
TRAIN_BATCH_SIZE = 4
GRADIENT_ACCUMULATION = 4
TRAIN_EPOCHS = 1
MAX_LENGTH = 256

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def set_seed(seed):
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_features():
    rows_by_key = {}
    with open(FEATURES_CSV) as f:
        for row in csv.DictReader(f):
            key = (int(row["depth"]), int(row["doc_id"]))
            feat = []
            for c in FEAT_COLS:
                try:
                    feat.append(float(row[c]))
                except (ValueError, KeyError):
                    feat.append(np.nan)
            rows_by_key[key] = np.array(feat)
    return rows_by_key


def train_obd_classifier(features_by_key):
    """Train LightGBM binary classifier: depth 0 vs depth 1+.
    Returns OOF predictions dict: (depth, doc_id) -> predicted_label."""
    import lightgbm as lgb
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import accuracy_score, roc_auc_score

    keys = sorted(features_by_key.keys())
    X = np.array([features_by_key[k] for k in keys])
    y = np.array([0 if k[0] == 0 else 1 for k in keys])

    nan_mask = np.isnan(X)
    if nan_mask.any():
        from sklearn.impute import SimpleImputer
        imp = SimpleImputer(strategy="median")
        X = imp.fit_transform(X)

    oof_preds = np.zeros(len(y))
    oof_probs = np.zeros(len(y))
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    for fold, (tri, tei) in enumerate(skf.split(X, y)):
        clf = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.05,
            num_leaves=31, verbose=-1, n_jobs=-1,
        )
        clf.fit(X[tri], y[tri])
        probs = clf.predict_proba(X[tei])[:, 1]
        oof_probs[tei] = probs
        oof_preds[tei] = (probs >= 0.5).astype(int)

    acc = accuracy_score(y, oof_preds)
    auc = roc_auc_score(y, oof_probs)
    log.info(f"OBD classifier OOF: acc={acc:.4f}, AUC={auc:.4f}")

    pred_dict = {}
    prob_dict = {}
    for i, k in enumerate(keys):
        pred_dict[k] = int(oof_preds[i])
        prob_dict[k] = float(oof_probs[i])

    return pred_dict, prob_dict, {"acc": acc, "auc": auc}


# ---------------------------------------------------------------------------
# Data preparation
# ---------------------------------------------------------------------------

def prepare_corpus(seed):
    """Create 50% contaminated mixed corpus."""
    rng = np.random.RandomState(seed)

    n_synthetic = int(TOTAL_DOCS * CONTAMINATION_RATE / 100)
    n_human = TOTAL_DOCS - n_synthetic

    human_pool = load_jsonl(DATA_DIR / "depth_0.jsonl")
    ai_pool = []
    for d in range(1, MAX_DEPTH + 1):
        recs = load_jsonl(DATA_DIR / f"depth_{d}.jsonl")
        for r in recs:
            r["depth"] = d
        ai_pool.extend(recs)

    corpus = []

    h_idx = rng.choice(len(human_pool), min(n_human, len(human_pool)), replace=False)
    for i in h_idx:
        r = human_pool[i]
        corpus.append({
            "text": r["text"], "doc_id": r["doc_id"],
            "depth": 0, "source": "human",
        })

    a_idx = rng.choice(len(ai_pool), min(n_synthetic, len(ai_pool)), replace=False)
    for i in a_idx:
        r = ai_pool[i]
        corpus.append({
            "text": r["text"], "doc_id": r["doc_id"],
            "depth": r["depth"], "source": "synthetic",
        })

    rng.shuffle(corpus)
    log.info(f"Corpus: {len(corpus)} docs, "
             f"{sum(1 for c in corpus if c['source']=='human')} human, "
             f"{sum(1 for c in corpus if c['source']=='synthetic')} synthetic")
    return corpus


def apply_strategy(corpus, strategy, obd_preds=None, obd_probs=None):
    """Apply filtering strategy. Returns (texts, weights, n_kept, n_removed)."""
    if strategy == "no_filter":
        texts = [r["text"] for r in corpus]
        weights = [1.0] * len(texts)
        return texts, weights, len(texts), 0

    elif strategy == "binary_ours":
        kept_texts = []
        n_removed = 0
        for r in corpus:
            key = (r["depth"], r["doc_id"])
            pred = obd_preds.get(key, 0)
            if pred == 0:
                kept_texts.append(r["text"])
            else:
                n_removed += 1
        log.info(f"Binary OBD filter: {len(corpus)} -> {len(kept_texts)} "
                 f"(removed {n_removed})")
        return kept_texts, [1.0] * len(kept_texts), len(kept_texts), n_removed

    elif strategy == "graduated_a09":
        texts = [r["text"] for r in corpus]
        weights = [GRADUATED_ALPHA ** r["depth"] for r in corpus]
        log.info(f"Graduated a={GRADUATED_ALPHA}: mean_weight={np.mean(weights):.4f}")
        return texts, weights, len(texts), 0

    raise ValueError(f"Unknown strategy: {strategy}")


# ---------------------------------------------------------------------------
# LoRA Training
# ---------------------------------------------------------------------------

def train_lora(texts, weights, output_dir, device, seed):
    from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
    from peft import LoraConfig, get_peft_model, TaskType
    from torch.utils.data import Dataset

    set_seed(seed)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id

    class WeightedTextDataset(Dataset):
        def __init__(self, texts, weights, tokenizer, max_length):
            self.encodings = []
            self.weights = []
            for text, w in zip(texts, weights):
                enc = tokenizer(text, truncation=True, max_length=max_length,
                                padding="max_length", return_tensors="pt")
                self.encodings.append({k: v.squeeze(0) for k, v in enc.items()})
                self.weights.append(w)

        def __len__(self):
            return len(self.encodings)

        def __getitem__(self, idx):
            item = {k: v.clone() for k, v in self.encodings[idx].items()}
            item["labels"] = item["input_ids"].clone()
            item["labels"][item["attention_mask"] == 0] = -100
            item["weight"] = torch.tensor(self.weights[idx], dtype=torch.float32)
            return item

    class WeightedTrainer(Trainer):
        def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
            w = inputs.pop("weight", None)
            outputs = model(**inputs)
            loss = outputs.loss
            if w is not None and w.numel() > 0:
                loss = loss * w.mean()
            return (loss, outputs) if return_outputs else loss

    log.info(f"Tokenizing {len(texts)} texts...")
    dataset = WeightedTextDataset(texts, weights, tokenizer, MAX_LENGTH)

    log.info("Loading Qwen2.5-1.5B...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, trust_remote_code=True,
    ).to(device)

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=LORA_RANK,
        lora_alpha=LORA_ALPHA,
        target_modules=LORA_TARGET_MODULES,
        lora_dropout=LORA_DROPOUT,
    )
    model = get_peft_model(model, lora_config)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    log.info(f"LoRA r={LORA_RANK}: {trainable:,} trainable / {total:,} total "
             f"({trainable/total*100:.2f}%)")

    training_args = TrainingArguments(
        output_dir=str(output_dir),
        num_train_epochs=TRAIN_EPOCHS,
        per_device_train_batch_size=TRAIN_BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION,
        learning_rate=TRAIN_LR,
        warmup_ratio=0.05,
        weight_decay=0.01,
        logging_steps=20,
        save_strategy="no",
        bf16=True,
        dataloader_pin_memory=False,
        seed=seed,
        report_to="none",
        remove_unused_columns=False,
    )

    trainer = WeightedTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    log.info(f"Training: {len(dataset)} samples, bs={TRAIN_BATCH_SIZE}x"
             f"{GRADIENT_ACCUMULATION}, lr={TRAIN_LR}, device={device}")
    trainer.train()

    merged_dir = output_dir / "merged"
    log.info("Merging LoRA weights...")
    merged = model.merge_and_unload()
    merged.save_pretrained(str(merged_dir))
    tokenizer.save_pretrained(str(merged_dir))
    log.info(f"Merged model saved to {merged_dir}")

    del model, merged, trainer, dataset
    torch.cuda.empty_cache()
    gc.collect()

    return merged_dir


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate_model(model_path, device, results_path):
    if results_path.exists():
        with open(results_path) as f:
            data = json.load(f)
        if data.get("scores", {}).get("mmlu") is not None:
            log.info(f"Eval results exist: {results_path}")
            return data["scores"]

    import lm_eval
    from lm_eval.models.huggingface import HFLM

    log.info(f"Loading model for eval: {model_path}")
    lm = HFLM(
        pretrained=str(model_path),
        device=device,
        batch_size=8,
        dtype="bfloat16",
        trust_remote_code=True,
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            results = lm_eval.simple_evaluate(
                model=lm,
                tasks=["mmlu", "hellaswag"],
                num_fewshot=None,
                task_manager=None,
            )
            break
        except (RuntimeError, ConnectionError, OSError) as e:
            if attempt < max_retries - 1:
                wait = 30 * (attempt + 1)
                log.warning(f"Eval attempt {attempt+1} failed: {e}. Retry in {wait}s...")
                time.sleep(wait)
            else:
                raise

    scores = {}
    res = results["results"]

    if "mmlu" in res:
        scores["mmlu"] = res["mmlu"].get("acc,none", res["mmlu"].get("acc", 0))
    if "hellaswag" in res:
        scores["hellaswag"] = res["hellaswag"].get(
            "acc_norm,none", res["hellaswag"].get("acc_norm", 0))

    results_path.parent.mkdir(parents=True, exist_ok=True)
    with open(results_path, "w") as f:
        json.dump({"scores": scores, "full": {k: v for k, v in res.items()}},
                  f, indent=2, default=str)

    log.info(f"MMLU={scores.get('mmlu', 'N/A')}, "
             f"HellaSwag={scores.get('hellaswag', 'N/A')}")

    del lm
    torch.cuda.empty_cache()
    gc.collect()

    return scores


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Gemma-27B filtering effectiveness evaluation")
    parser.add_argument("--strategy", type=str, required=True,
                        choices=["no_filter", "binary_ours", "graduated_a09"])
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--device", type=str, default="cuda:3")
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--skip_eval", action="store_true")
    args = parser.parse_args()

    results_base = PROJECT_ROOT / "results" / "exp_gemma27b_filtering"
    output_dir = results_base / f"{args.strategy}_seed{args.seed}"
    eval_path = output_dir / "eval_results.json"

    if eval_path.exists():
        with open(eval_path) as f:
            data = json.load(f)
        if data.get("scores", {}).get("mmlu") is not None:
            log.info(f"Already completed: {eval_path}")
            return

    output_dir.mkdir(parents=True, exist_ok=True)

    log_dir = PROJECT_ROOT / "logs" / "exp_gemma27b_filtering"
    log_dir.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(
        log_dir / f"{args.strategy}_seed{args.seed}.log")
    fh.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S"))
    logging.getLogger().addHandler(fh)

    log.info("=" * 60)
    log.info("Gemma-27B filtering effectiveness evaluation")
    log.info(f"Strategy: {args.strategy}, Seed: {args.seed}, Device: {args.device}")
    log.info(f"Model: {MODEL_PATH}")
    log.info(f"Data: {DATA_DIR}")
    log.info(f"Features: {FEATURES_CSV}")
    log.info(f"LoRA: rank={LORA_RANK}, alpha={LORA_ALPHA}")
    log.info(f"Contamination rate: {CONTAMINATION_RATE}%")
    log.info("=" * 60)

    # Train OBD classifier if needed
    obd_preds, obd_probs, obd_stats = None, None, None
    if args.strategy == "binary_ours":
        log.info("Training OBD binary classifier...")
        features_by_key = load_features()
        obd_preds, obd_probs, obd_stats = train_obd_classifier(features_by_key)
        obd_path = output_dir / "obd_classifier_stats.json"
        with open(obd_path, "w") as f:
            json.dump(obd_stats, f, indent=2)

    # Prepare corpus
    corpus = prepare_corpus(args.seed)

    # Apply strategy
    texts, weights, n_kept, n_removed = apply_strategy(
        corpus, args.strategy, obd_preds, obd_probs)

    # Log filtering stats
    if args.strategy == "binary_ours":
        true_human = sum(1 for r in corpus if r["source"] == "human")
        true_synth = sum(1 for r in corpus if r["source"] == "synthetic")
        pred_clean = sum(1 for r in corpus
                         if obd_preds.get((r["depth"], r["doc_id"]), 0) == 0)
        tp = sum(1 for r in corpus if r["source"] == "synthetic"
                 and obd_preds.get((r["depth"], r["doc_id"]), 0) == 1)
        fp = sum(1 for r in corpus if r["source"] == "human"
                 and obd_preds.get((r["depth"], r["doc_id"]), 0) == 1)
        fn = sum(1 for r in corpus if r["source"] == "synthetic"
                 and obd_preds.get((r["depth"], r["doc_id"]), 0) == 0)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        log.info(f"Filtering stats: TP={tp}, FP={fp}, FN={fn}, "
                 f"precision={precision:.4f}, recall={recall:.4f}")

    strategy_meta = {
        "strategy": args.strategy,
        "seed": args.seed,
        "n_corpus": len(corpus),
        "n_kept": n_kept,
        "n_removed": n_removed,
        "mean_weight": float(np.mean(weights)),
    }
    with open(output_dir / "strategy_meta.json", "w") as f:
        json.dump(strategy_meta, f, indent=2)

    if args.dry_run:
        log.info(f"DRY RUN: {len(texts)} texts, mean_weight={np.mean(weights):.4f}")
        return

    # Train
    train_dir = output_dir / "train"
    model_dir = train_lora(texts, weights, train_dir, args.device, args.seed)

    # Eval
    if not args.skip_eval:
        scores = evaluate_model(model_dir, args.device, eval_path)
    else:
        log.info("Skipping eval (--skip_eval)")
        scores = {"mmlu": None, "hellaswag": None}
        with open(eval_path, "w") as f:
            json.dump({"scores": scores}, f)

    # Cleanup training artifacts
    import shutil
    if train_dir.exists():
        shutil.rmtree(train_dir, ignore_errors=True)
        log.info("Cleaned up training artifacts")

    log.info(f"Done: {args.strategy} seed={args.seed} "
             f"MMLU={scores.get('mmlu', 'N/A')} "
             f"HellaSwag={scores.get('hellaswag', 'N/A')}")


if __name__ == "__main__":
    main()
