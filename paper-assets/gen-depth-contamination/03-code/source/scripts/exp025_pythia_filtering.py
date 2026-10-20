#!/usr/bin/env python3
"""exp-025: Pythia-1.4B filtering validation experiment.

Replicates exp-006 (Qwen-1.5B) K*-aware filtering on Pythia-1.4B to verify
cross-model consistency. Three strategies: no_filter, binary_ours (K*=2),
graduated_a09 (weight=0.9^depth).

Usage:
    python scripts/exp025_pythia_filtering.py --strategy binary_ours --seed 42 --device cuda:0
    python scripts/exp025_pythia_filtering.py --strategy no_filter --seed 42 --dry_run
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
PYTHIA_PATH = "/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79"
DATA_DIR = PROJECT_ROOT / "data_exp020_pythia_greedy"

KSTAR = 2
GRADUATED_ALPHA = 0.9
MAX_DEPTH = 5

LORA_RANK = 8
LORA_ALPHA = 16
LORA_TARGET_MODULES = ["query_key_value"]
LORA_DROPOUT = 0.05

TRAIN_LR = 2e-4
TRAIN_BATCH_SIZE = 4
GRADIENT_ACCUMULATION = 4
TRAIN_EPOCHS = 1
MAX_LENGTH = 256


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


# ---------------------------------------------------------------------------
# Phase 1: Data Preparation
# ---------------------------------------------------------------------------

def prepare_data(strategy, seed):
    """Load depth chain data with filtering strategy applied."""
    rng = np.random.RandomState(seed)

    all_texts = []
    all_weights = []

    if strategy == "no_filter":
        for d in range(MAX_DEPTH + 1):
            records = load_jsonl(DATA_DIR / f"depth_{d}.jsonl")
            all_texts.extend(r["text"] for r in records)
            all_weights.extend([1.0] * len(records))

    elif strategy == "binary_ours":
        for d in range(KSTAR + 1):
            records = load_jsonl(DATA_DIR / f"depth_{d}.jsonl")
            all_texts.extend(r["text"] for r in records)
            all_weights.extend([1.0] * len(records))

    elif strategy == "graduated_a09":
        for d in range(MAX_DEPTH + 1):
            records = load_jsonl(DATA_DIR / f"depth_{d}.jsonl")
            w = GRADUATED_ALPHA ** d
            all_texts.extend(r["text"] for r in records)
            all_weights.extend([w] * len(records))

    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    indices = list(range(len(all_texts)))
    rng.shuffle(indices)
    all_texts = [all_texts[i] for i in indices]
    all_weights = [all_weights[i] for i in indices]

    log.info(f"Data: strategy={strategy}, n={len(all_texts)}, "
             f"mean_weight={np.mean(all_weights):.4f}")
    return all_texts, all_weights


# ---------------------------------------------------------------------------
# Phase 2: LoRA Continued Pretraining
# ---------------------------------------------------------------------------

def continued_pretrain_lora(texts, weights, output_dir, device, seed):
    from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
    from peft import LoraConfig, get_peft_model, TaskType
    from torch.utils.data import Dataset

    set_seed(seed)

    tokenizer = AutoTokenizer.from_pretrained(PYTHIA_PATH)
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
            weights = inputs.pop("weight", None)
            outputs = model(**inputs)
            loss = outputs.loss
            if weights is not None and weights.numel() > 0:
                loss = loss * weights.mean()
            return (loss, outputs) if return_outputs else loss

    log.info(f"Tokenizing {len(texts)} texts...")
    dataset = WeightedTextDataset(texts, weights, tokenizer, MAX_LENGTH)

    log.info("Loading Pythia-1.4B...")
    model = AutoModelForCausalLM.from_pretrained(
        PYTHIA_PATH, torch_dtype=torch.float16
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
    log.info(f"LoRA: {trainable:,} trainable / {total:,} total "
             f"({trainable/total*100:.2f}%)")

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

    log.info(f"Training: {len(dataset)} samples, bs={TRAIN_BATCH_SIZE}x{GRADIENT_ACCUMULATION}, "
             f"lr={TRAIN_LR}, device={device}")
    trainer.train()

    merged_dir = output_dir / "merged"
    log.info("Merging LoRA weights into base model...")
    merged_model = model.merge_and_unload()
    merged_model.save_pretrained(merged_dir)
    tokenizer.save_pretrained(merged_dir)
    log.info(f"Merged model saved to {merged_dir}")

    del model, merged_model, trainer, dataset
    torch.cuda.empty_cache()
    gc.collect()

    return merged_dir


# ---------------------------------------------------------------------------
# Phase 3: Evaluation (lm-eval-harness)
# ---------------------------------------------------------------------------

def evaluate_model(model_path, device, results_path):
    import lm_eval
    from lm_eval.models.huggingface import HFLM

    log.info(f"Evaluating {model_path}...")

    lm = HFLM(
        pretrained=str(model_path),
        device=device,
        dtype="float16",
        batch_size="auto:4",
        max_length=2048,
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            results = lm_eval.simple_evaluate(
                model=lm,
                tasks=["mmlu", "hellaswag"],
                num_fewshot=5,
            )
            break
        except (RuntimeError, ConnectionError, OSError) as e:
            if attempt < max_retries - 1:
                wait = 30 * (attempt + 1)
                log.warning(f"Eval attempt {attempt+1} failed: {e}. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise

    scores = {}
    if "mmlu" in results["results"]:
        scores["mmlu"] = results["results"]["mmlu"].get(
            "acc,none", results["results"]["mmlu"].get("acc", 0))
    if "hellaswag" in results["results"]:
        scores["hellaswag"] = results["results"]["hellaswag"].get(
            "acc_norm,none", results["results"]["hellaswag"].get("acc_norm", 0))

    results_path.parent.mkdir(parents=True, exist_ok=True)
    with open(results_path, "w") as f:
        json.dump(
            {"scores": scores,
             "full": {k: v for k, v in results["results"].items()}},
            f, indent=2, default=str)

    log.info(f"MMLU={scores.get('mmlu', 'N/A'):.4f}, "
             f"HellaSwag={scores.get('hellaswag', 'N/A'):.4f}")

    del lm
    torch.cuda.empty_cache()
    gc.collect()

    return scores


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="exp-025: Pythia-1.4B filtering validation")
    parser.add_argument("--strategy", type=str, required=True,
                        choices=["no_filter", "binary_ours", "graduated_a09"])
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--skip_eval", action="store_true")
    args = parser.parse_args()

    results_base = PROJECT_ROOT / "results" / "exp_025_pythia_filtering"
    output_dir = results_base / f"{args.strategy}_seed{args.seed}"
    eval_path = output_dir / "eval_results.json"

    if eval_path.exists():
        log.info(f"Already completed: {eval_path}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    # File logging
    log_path = PROJECT_ROOT / "logs" / "exp025" / f"{args.strategy}_seed{args.seed}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(log_path)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S"))
    logging.getLogger().addHandler(fh)

    log.info("=" * 60)
    log.info(f"exp-025: Pythia-1.4B filtering validation")
    log.info(f"Strategy: {args.strategy}, Seed: {args.seed}, Device: {args.device}")
    log.info(f"Model: {PYTHIA_PATH}")
    log.info(f"Data: {DATA_DIR}")
    log.info(f"LoRA: rank={LORA_RANK}, alpha={LORA_ALPHA}, target={LORA_TARGET_MODULES}")
    log.info(f"K*={KSTAR}, graduated_alpha={GRADUATED_ALPHA}")
    log.info("=" * 60)

    texts, weights = prepare_data(args.strategy, args.seed)

    if args.dry_run:
        log.info(f"DRY RUN complete: {len(texts)} texts, "
                 f"mean_weight={np.mean(weights):.4f}")
        return

    train_dir = output_dir / "train"
    model_dir = continued_pretrain_lora(texts, weights, train_dir, args.device, args.seed)

    if not args.skip_eval:
        scores = evaluate_model(model_dir, args.device, eval_path)
    else:
        log.info("Skipping eval (--skip_eval)")
        scores = {"mmlu": 0, "hellaswag": 0}
        with open(eval_path, "w") as f:
            json.dump({"scores": scores}, f)

    import shutil
    if model_dir.exists():
        shutil.rmtree(model_dir, ignore_errors=True)
        if train_dir.exists():
            shutil.rmtree(train_dir, ignore_errors=True)
        log.info(f"Cleaned up training artifacts")

    log.info(f"Done: {args.strategy} seed={args.seed} "
             f"MMLU={scores.get('mmlu', 'N/A')} "
             f"HellaSwag={scores.get('hellaswag', 'N/A')}")


if __name__ == "__main__":
    main()
