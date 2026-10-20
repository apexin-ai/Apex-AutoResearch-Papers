#!/usr/bin/env python3
"""exp_deberta_filtering_comparison: DeBERTa vs 15D Filtering downstream comparison.

Four strategies using PREDICTED depth (not true depth):
  no_filter          all docs, weight=1
  obd_binary         remove docs with OBD predicted depth >= K*_OBD (3)
  deberta_binary     remove docs with DeBERTa predicted depth >= K*_DeBERTa (4)
  deberta_graduated  all docs, weighted by DeBERTa predicted depth

LoRA rank=16, alpha=32. Eval: MMLU + HellaSwag + ARC-Challenge.

Usage:
    python scripts/exp_deberta_filtering_comparison.py --strategy no_filter --device cuda:1
    python scripts/exp_deberta_filtering_comparison.py --strategy deberta_graduated --device cuda:2
"""

import argparse
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
DATA_DIR = PROJECT_ROOT / "data" / "exp_024_arxiv"
PRED_PATH = (
    PROJECT_ROOT / "results" / "exp_deberta_filtering_comparison" / "predictions.npz"
)

OBD_KSTAR = 3
DEB_KSTAR = 4
MAX_DEPTH = 5

GRADUATED_WEIGHTS = {0: 1.0, 1: 0.8, 2: 0.5, 3: 0.25, 4: 0.1, 5: 0.1}

LORA_RANK = 16
LORA_ALPHA = 32
LORA_TARGET_MODULES = ["q_proj", "v_proj"]
LORA_DROPOUT = 0.05

TRAIN_LR = 2e-4
TRAIN_BATCH_SIZE = 4
GRADIENT_ACCUMULATION = 4
TRAIN_EPOCHS = 1
MAX_LENGTH = 256


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def set_seed(seed):
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_all_texts():
    texts = []
    for d in range(MAX_DEPTH + 1):
        with open(DATA_DIR / f"depth_{d}.jsonl") as f:
            for line in f:
                texts.append(json.loads(line)["text"])
    return texts


# ---------------------------------------------------------------------------
# Phase 1: Data Preparation
# ---------------------------------------------------------------------------


def prepare_data(strategy, texts, predictions, seed=42):
    deberta_preds = predictions["deberta_preds"]
    obd_preds = predictions["obd_preds"]
    rng = np.random.RandomState(seed)

    if strategy == "no_filter":
        indices = list(range(len(texts)))
        weights = [1.0] * len(texts)

    elif strategy == "obd_binary":
        indices = [i for i in range(len(texts)) if obd_preds[i] < OBD_KSTAR]
        weights = [1.0] * len(indices)

    elif strategy == "deberta_binary":
        indices = [i for i in range(len(texts)) if deberta_preds[i] < DEB_KSTAR]
        weights = [1.0] * len(indices)

    elif strategy == "deberta_graduated":
        indices = list(range(len(texts)))
        weights = [GRADUATED_WEIGHTS.get(int(deberta_preds[i]), 0.1) for i in indices]

    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    sel_texts = [texts[i] for i in indices]
    perm = rng.permutation(len(sel_texts)).tolist()
    sel_texts = [sel_texts[i] for i in perm]
    sel_weights = [weights[i] for i in perm]

    log.info(
        f"Data: strategy={strategy}, n={len(sel_texts)}, "
        f"mean_weight={np.mean(sel_weights):.4f}"
    )
    return sel_texts, sel_weights


# ---------------------------------------------------------------------------
# Phase 2: LoRA Continued Pretraining
# ---------------------------------------------------------------------------


def continued_pretrain_lora(texts, weights, output_dir, device, seed):
    from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
    from peft import LoraConfig, get_peft_model, TaskType
    from torch.utils.data import Dataset

    set_seed(seed)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id

    class WeightedTextDataset(Dataset):
        def __init__(self, texts, weights, tokenizer, max_length):
            self.items = []
            self.weights = []
            for text, w in zip(texts, weights):
                enc = tokenizer(
                    text,
                    truncation=True,
                    max_length=max_length,
                    padding="max_length",
                    return_tensors="pt",
                )
                self.items.append({k: v.squeeze(0) for k, v in enc.items()})
                self.weights.append(w)

        def __len__(self):
            return len(self.items)

        def __getitem__(self, idx):
            item = {k: v.clone() for k, v in self.items[idx].items()}
            item["labels"] = item["input_ids"].clone()
            item["labels"][item["attention_mask"] == 0] = -100
            item["weight"] = torch.tensor(self.weights[idx], dtype=torch.float32)
            return item

    class WeightedTrainer(Trainer):
        def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
            weights_t = inputs.pop("weight", None)
            has_nontrivial = weights_t is not None and not torch.all(
                weights_t == 1.0
            )

            if has_nontrivial:
                labels = inputs.pop("labels")
                outputs = model(**inputs)
                logits = outputs.logits
                shift_logits = logits[..., :-1, :].contiguous()
                shift_labels = labels[..., 1:].contiguous()
                loss_fct = torch.nn.CrossEntropyLoss(
                    ignore_index=-100, reduction="none"
                )
                flat_loss = loss_fct(
                    shift_logits.view(-1, shift_logits.size(-1)),
                    shift_labels.view(-1),
                ).view(shift_logits.size(0), -1)
                mask = (shift_labels != -100).float()
                per_sample = (flat_loss * mask).sum(-1) / mask.sum(-1).clamp(min=1)
                w = weights_t.to(per_sample.device)
                loss = (per_sample * w).sum() / w.sum()
            else:
                outputs = model(**inputs)
                loss = outputs.loss

            return (loss, outputs) if return_outputs else loss

    log.info(f"Tokenizing {len(texts)} texts...")
    dataset = WeightedTextDataset(texts, weights, tokenizer, MAX_LENGTH)

    log.info("Loading Qwen2.5-1.5B...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.float16
    ).to(device)

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=LORA_RANK,
        lora_alpha=LORA_ALPHA,
        target_modules=LORA_TARGET_MODULES,
        lora_dropout=LORA_DROPOUT,
        bias="none",
    )
    model = get_peft_model(model, lora_config)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    log.info(
        f"LoRA: {trainable:,} trainable / {total:,} total "
        f"({trainable / total * 100:.2f}%)"
    )

    training_args = TrainingArguments(
        output_dir=str(output_dir),
        num_train_epochs=TRAIN_EPOCHS,
        per_device_train_batch_size=TRAIN_BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION,
        learning_rate=TRAIN_LR,
        warmup_ratio=0.05,
        weight_decay=0.01,
        logging_steps=50,
        save_strategy="no",
        fp16=True,
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

    log.info(
        f"Training: {TRAIN_EPOCHS} epoch, batch={TRAIN_BATCH_SIZE}x{GRADIENT_ACCUMULATION}, "
        f"lr={TRAIN_LR}, device={device}"
    )
    trainer.train()

    merged_dir = output_dir / "merged"
    log.info("Merging LoRA weights...")
    merged_model = model.merge_and_unload()
    merged_model.save_pretrained(merged_dir)
    tokenizer.save_pretrained(merged_dir)
    log.info(f"Merged model saved to {merged_dir}")

    del model, merged_model, trainer, dataset
    torch.cuda.empty_cache()
    gc.collect()

    return merged_dir


# ---------------------------------------------------------------------------
# Phase 3: Evaluation
# ---------------------------------------------------------------------------


def evaluate_model(model_path, device, results_path):
    import lm_eval
    from lm_eval.models.huggingface import HFLM

    log.info(f"Evaluating {model_path} on {device}...")

    lm = HFLM(
        pretrained=str(model_path),
        device=str(device),
        batch_size=8,
        dtype="float16",
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            results = lm_eval.simple_evaluate(
                model=lm,
                tasks=["mmlu", "hellaswag", "arc_challenge"],
                batch_size=8,
                device=str(device),
            )
            break
        except (RuntimeError, ConnectionError, OSError) as e:
            if attempt < max_retries - 1:
                wait = 30 * (attempt + 1)
                log.warning(
                    f"Eval attempt {attempt+1} failed: {e}. Retrying in {wait}s..."
                )
                time.sleep(wait)
            else:
                raise

    scores = {}
    if "mmlu" in results["results"]:
        scores["mmlu"] = results["results"]["mmlu"].get(
            "acc,none", results["results"]["mmlu"].get("acc", 0)
        )
    if "hellaswag" in results["results"]:
        scores["hellaswag"] = results["results"]["hellaswag"].get(
            "acc_norm,none", results["results"]["hellaswag"].get("acc_norm", 0)
        )
    if "arc_challenge" in results["results"]:
        scores["arc_challenge"] = results["results"]["arc_challenge"].get(
            "acc_norm,none", results["results"]["arc_challenge"].get("acc_norm", 0)
        )

    results_path = Path(results_path)
    results_path.parent.mkdir(parents=True, exist_ok=True)
    with open(results_path, "w") as f:
        json.dump(
            {"scores": scores, "full": {k: v for k, v in results["results"].items()}},
            f,
            indent=2,
            default=str,
        )

    log.info(
        f"MMLU={scores.get('mmlu', 'N/A'):.4f}, "
        f"HellaSwag={scores.get('hellaswag', 'N/A'):.4f}, "
        f"ARC-C={scores.get('arc_challenge', 'N/A'):.4f}"
    )

    del lm
    torch.cuda.empty_cache()
    gc.collect()

    return scores


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="DeBERTa vs 15D Filtering Comparison"
    )
    parser.add_argument(
        "--strategy",
        required=True,
        choices=["no_filter", "obd_binary", "deberta_binary", "deberta_graduated"],
    )
    parser.add_argument("--device", default="cuda:1")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--skip_eval", action="store_true")
    args = parser.parse_args()

    results_base = PROJECT_ROOT / "results" / "exp_deberta_filtering_comparison"
    output_dir = results_base / args.strategy
    eval_path = output_dir / "eval_results.json"

    if eval_path.exists():
        log.info(f"Already completed: {eval_path}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    log_path = (
        PROJECT_ROOT
        / "logs"
        / "exp_deberta_filtering_comparison"
        / f"{args.strategy}.log"
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(log_path)
    fh.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
    )
    logging.getLogger().addHandler(fh)

    log.info("=" * 60)
    log.info(f"exp_deberta_filtering_comparison: {args.strategy}")
    log.info(f"Device: {args.device}, Seed: {args.seed}")
    log.info(f"LoRA: rank={LORA_RANK}, alpha={LORA_ALPHA}")
    log.info(f"OBD K*={OBD_KSTAR}, DeBERTa K*={DEB_KSTAR}")
    log.info(f"Graduated weights: {GRADUATED_WEIGHTS}")
    log.info("=" * 60)

    predictions = np.load(PRED_PATH)
    texts = load_all_texts()

    n_total = len(texts)
    deberta_preds = predictions["deberta_preds"]
    obd_preds = predictions["obd_preds"]
    true_depths = predictions["true_depths"]
    log.info(
        f"Loaded {n_total} texts, {len(deberta_preds)} predictions"
    )
    log.info(
        f"DeBERTa pred dist: {np.bincount(deberta_preds, minlength=6).tolist()}"
    )
    log.info(
        f"OBD pred dist: {np.bincount(obd_preds, minlength=6).tolist()}"
    )

    sel_texts, sel_weights = prepare_data(
        args.strategy, texts, predictions, seed=args.seed
    )

    device = torch.device(args.device)
    train_dir = output_dir / "train"
    model_dir = continued_pretrain_lora(
        sel_texts, sel_weights, train_dir, device, args.seed
    )

    if not args.skip_eval:
        scores = evaluate_model(model_dir, device, eval_path)
    else:
        log.info("Skipping eval (--skip_eval)")
        scores = {}
        with open(eval_path, "w") as f:
            json.dump({"scores": scores}, f)

    import shutil

    if model_dir.exists():
        shutil.rmtree(model_dir, ignore_errors=True)
        if train_dir.exists():
            shutil.rmtree(train_dir, ignore_errors=True)
        log.info("Cleaned up training artifacts")

    log.info(f"Done: {args.strategy} scores={scores}")


if __name__ == "__main__":
    main()
