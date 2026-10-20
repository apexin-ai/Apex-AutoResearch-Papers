#!/usr/bin/env python3
"""exp_contamination_rate_sweep: Test K*-guided filtering across contamination rates.

Trains Qwen2.5-1.5B with LoRA on mixed corpora at 10%/30%/50%/100% synthetic
contamination, under three filtering strategies: no_filter, binary, graduated.
Evaluates on MMLU, HellaSwag, ARC-Challenge.

Input:  depth_{0..5}.jsonl from data_exp020_pythia_greedy/
Output: LoRA adapter + eval results per (rate, strategy) combination

Usage:
    python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:1
    python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy binary --device cuda:2
    python scripts/exp_contamination_rate_sweep.py --rate 100 --strategy graduated --device cuda:3
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
DATA_DIR = PROJECT_ROOT / "data_exp020_pythia_greedy"

TOTAL_DOCS = 5000
MAX_DEPTH = 5
SEED = 42

LORA_RANK = 16
LORA_ALPHA = 32
LORA_TARGET_MODULES = ["q_proj", "v_proj"]
LORA_DROPOUT = 0.05

TRAIN_LR = 2e-4
TRAIN_BATCH_SIZE = 4
GRADIENT_ACCUMULATION = 4
TRAIN_EPOCHS = 1
MAX_LENGTH = 256

GRADUATED_WEIGHTS = {0: 1.0, 1: 0.5, 2: 0.25, 3: 0.1, 4: 0.1, 5: 0.1}


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(records, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def set_seed(seed):
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


# ---------------------------------------------------------------------------
# Phase 1: Create mixed corpus with fixed total size
# ---------------------------------------------------------------------------

def prepare_corpus(rate, data_out_dir):
    """Create a fixed-size corpus with specified contamination rate.

    rate: percentage of synthetic docs (10, 30, 50, 100)
    Returns list of dicts with text/depth/source fields.
    """
    out_path = data_out_dir / "corpus.jsonl"
    if out_path.exists():
        records = load_jsonl(out_path)
        log.info(f"Corpus exists ({len(records)} docs), reusing")
        return records

    rng = np.random.RandomState(SEED)

    n_synthetic = int(TOTAL_DOCS * rate / 100)
    n_human = TOTAL_DOCS - n_synthetic

    human_pool = load_jsonl(DATA_DIR / "depth_0.jsonl")
    ai_pool = []
    for d in range(1, MAX_DEPTH + 1):
        recs = load_jsonl(DATA_DIR / f"depth_{d}.jsonl")
        for r in recs:
            r["depth"] = d
        ai_pool.extend(recs)

    corpus = []

    if n_human > 0:
        h_idx = rng.choice(len(human_pool), min(n_human, len(human_pool)), replace=False)
        for i in h_idx:
            r = human_pool[i]
            corpus.append({"text": r["text"], "doc_id": r["doc_id"], "depth": 0, "source": "human"})

    if n_synthetic > 0:
        a_idx = rng.choice(len(ai_pool), min(n_synthetic, len(ai_pool)), replace=False)
        for i in a_idx:
            r = ai_pool[i]
            corpus.append({"text": r["text"], "doc_id": r.get("doc_id", -1),
                           "depth": r["depth"], "source": "ai"})

    rng.shuffle(corpus)

    data_out_dir.mkdir(parents=True, exist_ok=True)
    save_jsonl(corpus, out_path)

    depth_counts = {}
    for r in corpus:
        d = r["depth"]
        depth_counts[d] = depth_counts.get(d, 0) + 1
    log.info(f"Corpus: {len(corpus)} docs, rate={rate}%, depths={dict(sorted(depth_counts.items()))}")
    return corpus


# ---------------------------------------------------------------------------
# Phase 2: Apply filtering strategy
# ---------------------------------------------------------------------------

def apply_strategy(corpus, strategy):
    """Apply filtering strategy. Returns (records, weights)."""
    if strategy == "no_filter":
        return corpus, [1.0] * len(corpus)

    elif strategy == "binary":
        filtered = [r for r in corpus if r["depth"] == 0]
        log.info(f"Binary filter: {len(corpus)} -> {len(filtered)} docs (removed {len(corpus)-len(filtered)} synthetic)")
        return filtered, [1.0] * len(filtered)

    elif strategy == "graduated":
        weights = [GRADUATED_WEIGHTS.get(r["depth"], 0.1) for r in corpus]
        log.info(f"Graduated weights: mean={np.mean(weights):.3f}, "
                 f"by_depth={{ {', '.join(f'd{d}:{GRADUATED_WEIGHTS.get(d, 0.1)}' for d in range(MAX_DEPTH+1))} }}")
        return corpus, weights

    raise ValueError(f"Unknown strategy: {strategy}")


# ---------------------------------------------------------------------------
# Phase 3: LoRA training
# ---------------------------------------------------------------------------

def train_lora(records, weights, output_dir, device):
    """LoRA fine-tuning on filtered corpus."""
    from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
    from peft import LoraConfig, get_peft_model, TaskType
    from torch.utils.data import Dataset

    set_seed(SEED)

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
            weights = inputs.pop("weight", None)
            outputs = model(**inputs)
            loss = outputs.loss
            if weights is not None and weights.numel() > 0:
                loss = loss * weights.mean()
            return (loss, outputs) if return_outputs else loss

    texts = [r["text"] for r in records]
    dataset = WeightedTextDataset(texts, weights, tokenizer, MAX_LENGTH)
    log.info(f"Dataset: {len(dataset)} samples")

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, trust_remote_code=True,
    )

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=LORA_RANK,
        lora_alpha=LORA_ALPHA,
        target_modules=LORA_TARGET_MODULES,
        lora_dropout=LORA_DROPOUT,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    model = model.to(device)

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
        seed=SEED,
        report_to="none",
        remove_unused_columns=False,
    )

    trainer = WeightedTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
    )

    log.info(f"Starting LoRA training: {len(dataset)} samples, device={device}")
    trainer.train()

    adapter_dir = output_dir / "adapter"
    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)
    log.info(f"LoRA adapter saved to {adapter_dir}")

    del model, trainer
    torch.cuda.empty_cache()
    gc.collect()

    return adapter_dir


# ---------------------------------------------------------------------------
# Phase 4: Evaluation
# ---------------------------------------------------------------------------

def evaluate_model(adapter_dir, device, results_path):
    """Run lm-eval on MMLU, HellaSwag, ARC-Challenge."""
    for k in ["HF_DATASETS_OFFLINE", "HF_HUB_OFFLINE", "TRANSFORMERS_OFFLINE"]:
        os.environ.pop(k, None)

    import lm_eval
    from lm_eval.models.huggingface import HFLM

    log.info(f"Evaluating {adapter_dir}...")

    lm = HFLM(
        pretrained=MODEL_PATH,
        peft=str(adapter_dir),
        device=device,
        dtype="bfloat16",
        batch_size="auto:4",
        trust_remote_code=True,
        max_length=2048,
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            results = lm_eval.simple_evaluate(
                model=lm,
                tasks=["mmlu", "hellaswag", "arc_challenge"],
                num_fewshot=None,
                task_manager=None,
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
    res = results["results"]

    if "mmlu" in res:
        scores["mmlu"] = res["mmlu"].get("acc,none", res["mmlu"].get("acc", 0))
    if "hellaswag" in res:
        scores["hellaswag"] = res["hellaswag"].get("acc_norm,none", res["hellaswag"].get("acc_norm", 0))
    if "arc_challenge" in res:
        scores["arc_challenge"] = res["arc_challenge"].get("acc_norm,none", res["arc_challenge"].get("acc_norm", 0))

    results_path.parent.mkdir(parents=True, exist_ok=True)
    with open(results_path, "w") as f:
        json.dump({"scores": scores, "full": {k: v for k, v in res.items()}},
                  f, indent=2, default=str)

    log.info(f"Eval: MMLU={scores.get('mmlu', 'N/A')}, "
             f"HellaSwag={scores.get('hellaswag', 'N/A')}, "
             f"ARC-C={scores.get('arc_challenge', 'N/A')}")

    del lm
    torch.cuda.empty_cache()
    gc.collect()

    return scores


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Contamination rate sweep experiment")
    parser.add_argument("--rate", type=int, required=True, choices=[10, 30, 50, 100])
    parser.add_argument("--strategy", type=str, required=True,
                        choices=["no_filter", "binary", "graduated"])
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--skip_eval", action="store_true")
    parser.add_argument("--eval_only", action="store_true")
    args = parser.parse_args()

    exp_name = f"rate_{args.rate}/{args.strategy}"
    results_base = PROJECT_ROOT / "results" / "exp_contamination_rate_sweep"
    output_dir = results_base / exp_name
    eval_path = output_dir / "eval_results.json"
    adapter_dir = output_dir / "adapter"

    if eval_path.exists() and not args.eval_only:
        log.info(f"Already completed: {eval_path}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    log_dir = PROJECT_ROOT / "logs" / "exp_contamination_rate_sweep"
    log_dir.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(log_dir / f"rate{args.rate}_{args.strategy}.log")
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S"))
    logging.getLogger().addHandler(fh)

    log.info("=" * 60)
    log.info(f"exp_contamination_rate_sweep")
    log.info(f"Rate: {args.rate}%, Strategy: {args.strategy}, Device: {args.device}")
    log.info(f"Model: {MODEL_PATH}, LoRA: rank={LORA_RANK}, alpha={LORA_ALPHA}")
    log.info("=" * 60)

    # Prepare data
    data_dir = PROJECT_ROOT / "data" / "contamination_sweep" / f"rate_{args.rate}"
    corpus = prepare_corpus(args.rate, data_dir)
    records, weights = apply_strategy(corpus, args.strategy)

    if args.eval_only:
        if not adapter_dir.exists():
            log.error(f"Adapter not found: {adapter_dir}")
            return
        scores = evaluate_model(adapter_dir, args.device, eval_path)
        log.info(f"Done (eval_only): {scores}")
        return

    # Train
    trained_adapter = train_lora(records, weights, output_dir, args.device)

    # Eval
    if not args.skip_eval:
        scores = evaluate_model(trained_adapter, args.device, eval_path)
    else:
        log.info("Skipping eval (--skip_eval)")
        scores = {}

    log.info(f"Done: rate={args.rate}% strategy={args.strategy} scores={scores}")


if __name__ == "__main__":
    main()
