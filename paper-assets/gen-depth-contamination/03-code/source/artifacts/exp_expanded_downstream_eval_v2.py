#!/usr/bin/env python3
"""Expanded downstream evaluation for K*-guided filtering strategies.

Retrains LoRA models on Qwen2.5-1.5B with 3 filtering strategies
(no_filter, binary_ours, graduated), then evaluates on 5 benchmarks:
PIQA, TruthfulQA-MC2, WinoGrande, ARC-Challenge, GSM8K.

Usage:
    python scripts/exp_expanded_downstream_eval.py --device cuda:0 --num_seeds 3
    python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 2 --num_seeds 1 --strategy no_filter --skip_base
"""

import argparse
import gc
import json
import logging
import os
import shutil
import sys
import time
from pathlib import Path

import numpy as np
import torch
from scipy import stats

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

PROJECT_ROOT = Path("/root/autodl-tmp/gen-depth-contamination")
MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B"
DATA_DIR = PROJECT_ROOT / "data_exp020_pythia_greedy"

KSTAR = 2
GRADUATED_ALPHA = 0.9
MAX_DEPTH = 5
STRATEGIES = ["no_filter", "binary_ours", "graduated"]

LORA_RANK = 8
LORA_ALPHA = 16
LORA_TARGET_MODULES = ["q_proj", "v_proj"]
LORA_DROPOUT = 0.05

TRAIN_LR = 2e-4
TRAIN_BATCH_SIZE = 4
GRADIENT_ACCUMULATION = 4
TRAIN_EPOCHS = 1
MAX_LENGTH = 256

BENCHMARKS = [
    ("piqa", 0),
    ("truthfulqa_mc2", 0),
    ("winogrande", 5),
    ("arc_challenge", 25),
    ("gsm8k", 8),
]


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def set_seed(seed):
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def prepare_data(strategy, seed):
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
    elif strategy == "graduated":
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
            weights_val = inputs.pop("weight", None)
            outputs = model(**inputs)
            loss = outputs.loss
            if weights_val is not None and weights_val.numel() > 0:
                loss = loss * weights_val.mean()
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


def evaluate_model(model_path, device, results_path,
                   benchmarks_override=None, existing_scores=None, existing_full=None):
    import lm_eval
    from lm_eval.models.huggingface import HFLM

    benchmarks = benchmarks_override if benchmarks_override is not None else BENCHMARKS
    log.info(f"Evaluating {model_path} on {len(benchmarks)} benchmarks: {[b for b,_ in benchmarks]}")

    lm = HFLM(
        pretrained=str(model_path),
        device=device,
        dtype="float16",
        batch_size="auto:4",
        max_length=2048,
        trust_remote_code=True,
    )

    all_scores = dict(existing_scores) if existing_scores else {}
    all_full = dict(existing_full) if existing_full else {}

    for task_name, n_fewshot in benchmarks:
        log.info(f"  Running {task_name} ({n_fewshot}-shot)...")
        t0 = time.time()

        success = False
        for attempt in range(3):
            try:
                results = lm_eval.simple_evaluate(
                    model=lm,
                    tasks=[task_name],
                    num_fewshot=n_fewshot,
                )
                success = True
                break
            except Exception as e:
                if attempt < 2:
                    wait = 30 * (attempt + 1)
                    log.warning(f"  Attempt {attempt+1} failed: {e}. Retrying in {wait}s...")
                    time.sleep(wait)
                else:
                    log.error(f"  Failed {task_name} after 3 attempts: {e}")

        if not success:
            all_scores[task_name] = None
            continue

        task_results = results.get("results", {}).get(task_name, {})

        if task_name == "gsm8k":
            score = task_results.get("exact_match,strict-match",
                     task_results.get("exact_match,get-answer",
                      task_results.get("acc,none", 0)))
        elif task_name == "arc_challenge":
            score = task_results.get("acc_norm,none",
                     task_results.get("acc,none", 0))
        elif task_name == "truthfulqa_mc2":
            score = task_results.get("acc,none", 0)
        elif task_name in ("piqa", "winogrande"):
            score = task_results.get("acc,none", 0)
        else:
            score = task_results.get("acc,none", 0)

        all_scores[task_name] = float(score) if score is not None else None
        all_full[task_name] = {k: v for k, v in task_results.items()}
        elapsed = time.time() - t0
        log.info(f"  {task_name}: {score:.4f} ({elapsed:.0f}s)")

    results_path.parent.mkdir(parents=True, exist_ok=True)
    with open(results_path, "w") as f:
        json.dump({
            "scores": all_scores,
            "full": all_full,
            "benchmarks": [[b, n] for b, n in BENCHMARKS],
        }, f, indent=2, default=str)

    del lm
    torch.cuda.empty_cache()
    gc.collect()

    return all_scores


def run_statistical_analysis(results_dir, num_seeds, seed_start):
    log.info("Running statistical analysis...")

    strategy_scores = {s: {} for s in STRATEGIES}

    for strategy in STRATEGIES:
        for seed in range(seed_start, seed_start + num_seeds):
            eval_path = results_dir / f"{strategy}_seed{seed}_eval.json"
            if eval_path.exists():
                with open(eval_path) as f:
                    data = json.load(f)
                strategy_scores[strategy][seed] = data["scores"]

    all_benchmarks = set()
    for scores_by_seed in strategy_scores.values():
        for scores in scores_by_seed.values():
            all_benchmarks.update(k for k, v in scores.items() if v is not None)

    analysis = {"strategies": {}, "comparisons": []}

    for strategy in STRATEGIES:
        strat_data = {}
        for bench in sorted(all_benchmarks):
            vals = [strategy_scores[strategy][s][bench]
                    for s in strategy_scores[strategy]
                    if bench in strategy_scores[strategy][s]
                    and strategy_scores[strategy][s][bench] is not None]
            if vals:
                strat_data[bench] = {
                    "mean": float(np.mean(vals)),
                    "std": float(np.std(vals)),
                    "values": vals,
                }
        analysis["strategies"][strategy] = strat_data

    comparisons = []
    for bench in sorted(all_benchmarks):
        for s1, s2 in [("binary_ours", "no_filter"), ("binary_ours", "graduated"),
                       ("graduated", "no_filter")]:
            v1 = analysis["strategies"].get(s1, {}).get(bench, {}).get("values", [])
            v2 = analysis["strategies"].get(s2, {}).get(bench, {}).get("values", [])
            if len(v1) >= 2 and len(v2) >= 2:
                t_stat, p_val = stats.ttest_ind(v1, v2)
                diff = np.mean(v1) - np.mean(v2)
                pooled_std = np.sqrt((np.var(v1) + np.var(v2)) / 2)
                cohens_d = diff / pooled_std if pooled_std > 0 else 0.0
                comparisons.append({
                    "benchmark": bench,
                    "comparison": f"{s1}_vs_{s2}",
                    "mean_diff": float(diff),
                    "t_stat": float(t_stat),
                    "p_value": float(p_val),
                    "cohens_d": float(cohens_d),
                })

    if comparisons:
        p_values = [c["p_value"] for c in comparisons]
        sorted_indices = np.argsort(p_values)
        m = len(p_values)
        for rank, idx in enumerate(sorted_indices):
            adjusted_alpha = 0.05 / (m - rank)
            comparisons[idx]["holm_significant"] = p_values[idx] < adjusted_alpha

    analysis["comparisons"] = comparisons

    out_path = results_dir / "statistical_analysis.json"
    with open(out_path, "w") as f:
        json.dump(analysis, f, indent=2)
    log.info(f"Statistical analysis saved to {out_path}")
    return analysis


def main():
    parser = argparse.ArgumentParser(
        description="Expanded downstream eval for K*-guided filtering")
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--num_seeds", type=int, default=3)
    parser.add_argument("--seed_start", type=int, default=0)
    parser.add_argument("--skip_base", action="store_true")
    parser.add_argument("--strategy", type=str, default="all",
                        choices=["no_filter", "binary_ours", "graduated", "all"])
    parser.add_argument("--skip_train", action="store_true",
                        help="Skip training, load from existing merged model dir")
    args = parser.parse_args()

    results_dir = PROJECT_ROOT / "results" / "exp_expanded_downstream_eval"
    results_dir.mkdir(parents=True, exist_ok=True)

    log_path = PROJECT_ROOT / "logs" / "exp_expanded_downstream_eval.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(log_path)
    fh.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S"))
    logging.getLogger().addHandler(fh)

    log.info("=" * 60)
    log.info("Expanded Downstream Evaluation")
    log.info(f"Model: {MODEL_PATH}")
    log.info(f"Data: {DATA_DIR}")
    log.info(f"Strategy filter: {args.strategy}")
    log.info(f"Seeds: {args.seed_start}-{args.seed_start + args.num_seeds - 1}")
    log.info(f"Benchmarks: {[b[0] for b in BENCHMARKS]}")
    log.info(f"LoRA: rank={LORA_RANK}, alpha={LORA_ALPHA}, target={LORA_TARGET_MODULES}")
    log.info(f"skip_train={args.skip_train}")
    log.info("=" * 60)

    if not args.skip_base:
        base_eval_path = results_dir / "base_model_eval.json"
        if base_eval_path.exists():
            log.info("Base model eval exists, skipping")
        else:
            log.info("Evaluating base model...")
            base_scores = evaluate_model(MODEL_PATH, args.device, base_eval_path)
            log.info(f"Base model scores: {base_scores}")

    for seed in range(args.seed_start, args.seed_start + args.num_seeds):
        for strategy in STRATEGIES:
            if args.strategy != "all" and strategy != args.strategy:
                continue

            run_name = f"{strategy}_seed{seed}"
            eval_path = results_dir / f"{run_name}_eval.json"

            benchmarks_to_run = BENCHMARKS
            existing_scores = {}
            existing_full = {}

            if eval_path.exists():
                with open(eval_path) as f:
                    existing_data = json.load(f)
                existing_scores = existing_data.get("scores", {})
                existing_full = existing_data.get("full", {})
                null_benchmarks = [(b, n) for b, n in BENCHMARKS
                                   if existing_scores.get(b) is None]
                if not null_benchmarks:
                    log.info(f"[{run_name}] All benchmarks complete, skipping")
                    continue
                benchmarks_to_run = null_benchmarks
                log.info(f"[{run_name}] Patching null benchmarks: {[b for b,_ in null_benchmarks]}")

            log.info(f"\n{'='*60}\n  {run_name}\n{'='*60}")

            train_dir = results_dir / f"{run_name}_train"
            merged_dir = train_dir / "merged"

            if args.skip_train and merged_dir.exists():
                log.info(f"[{run_name}] skip_train: using existing model at {merged_dir}")
                model_dir = merged_dir
            else:
                if args.skip_train:
                    log.warning(f"[{run_name}] --skip_train but no model at {merged_dir}, training from scratch")
                texts, weights = prepare_data(strategy, seed)
                model_dir = train_lora(texts, weights, train_dir, args.device, seed)

            scores = evaluate_model(model_dir, args.device, eval_path,
                                    benchmarks_override=benchmarks_to_run,
                                    existing_scores=existing_scores,
                                    existing_full=existing_full)
            log.info(f"[{run_name}] Scores: {scores}")

            if train_dir.exists():
                shutil.rmtree(train_dir, ignore_errors=True)
                log.info(f"Cleaned up {train_dir}")

    log.info("\n" + "=" * 60 + "\n  STATISTICAL ANALYSIS\n" + "=" * 60)
    analysis = run_statistical_analysis(
        results_dir, args.num_seeds, args.seed_start)

    log.info("\n=== SUMMARY ===")

    base_eval_path = results_dir / "base_model_eval.json"
    if base_eval_path.exists():
        with open(base_eval_path) as f:
            base_scores = json.load(f)["scores"]
        log.info("  base_model: " + ", ".join(
            f"{k}={v:.4f}" for k, v in base_scores.items() if v is not None))

    for strategy in STRATEGIES:
        strat = analysis["strategies"].get(strategy, {})
        if strat:
            parts = []
            for bench in sorted(strat.keys()):
                m = strat[bench]["mean"]
                s = strat[bench]["std"]
                parts.append(f"{bench}={m:.4f}+/-{s:.4f}")
            log.info(f"  {strategy}: {', '.join(parts)}")

    for comp in analysis.get("comparisons", []):
        sig = "***" if comp.get("holm_significant") else "n.s."
        log.info(f"  {comp['benchmark']}: {comp['comparison']}: "
                 f"d={comp['cohens_d']:.3f}, p={comp['p_value']:.4f} {sig}")

    summary = {"base_model": {}, "strategies": analysis["strategies"],
               "comparisons": analysis["comparisons"]}
    if base_eval_path.exists():
        with open(base_eval_path) as f:
            summary["base_model"] = json.load(f)["scores"]
    with open(results_dir / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    log.info("\nDone!")


if __name__ == "__main__":
    main()
