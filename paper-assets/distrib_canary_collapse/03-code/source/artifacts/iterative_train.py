"""Iterative self-consuming training pipeline for model collapse study.

Each generation:
  1. Generate synthetic text from current model using held-out prompts
  2. Mix synthetic data with real data according to --synthetic_ratio
  3. Fine-tune the model on the mixed dataset
  4. Save checkpoint and compute all canary + downstream metrics

Synthetic mixing modes:
  - Default: each generation uses only current-gen synthetic data + real data
  - --accumulate: pool all historical synthetic data (gen 1..N) + real data

Usage:
    python iterative_train.py \
        --model_name EleutherAI/pythia-410m \
        --data_dir data/wikitext103 \
        --output_dir results/mvp/rep_42 \
        --num_generations 10 \
        --steps_per_gen 10000 \
        --synthetic_ratio 0.75 \
        --accumulate \
        --seed 42
"""

import argparse
import json
import os
import random

import numpy as np
import torch
from datasets import Dataset, concatenate_datasets, load_from_disk
from torch.utils.data import DataLoader
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
    set_seed,
)

from metrics import compute_all_metrics


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model_name", type=str, default="EleutherAI/pythia-410m")
    p.add_argument("--data_dir", type=str, default="data/wikitext103",
                   help="Output of prepare_data.py")
    p.add_argument("--dataset", type=str, default="wikitext-103-v1",
                   help="Dataset identifier (for logging only; actual data from data_dir)")
    p.add_argument("--synthetic_ratio", type=float, default=1.0,
                   help="Fraction of training data that is synthetic (0-1)")
    p.add_argument("--num_generations", type=int, default=10)
    p.add_argument("--steps_per_gen", type=int, default=5000)
    p.add_argument("--output_dir", type=str, default="results/mvp/rep_42")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--max_length", type=int, default=512)
    p.add_argument("--lr", type=float, default=5e-5)
    p.add_argument("--gen_max_new_tokens", type=int, default=256,
                   help="Max new tokens per generation sample")
    p.add_argument("--gen_batch_size", type=int, default=16)
    p.add_argument("--top_p", type=float, default=0.95,
                   help="Nucleus sampling p for synthetic generation")
    p.add_argument("--accumulate", action="store_true",
                   help="Pool all historical synthetic data instead of only the latest generation")
    return p.parse_args()


def generate_synthetic_data(model, tokenizer, prompts_dataset, args):
    """Generate synthetic text from `model` using held-out prompts."""
    model.eval()
    device = next(model.parameters()).device
    generated_texts = []

    original_padding_side = tokenizer.padding_side
    tokenizer.padding_side = 'left'

    try:
        prompt_texts = prompts_dataset["text"]
        for i in range(0, len(prompt_texts), args.gen_batch_size):
            batch_prompts = prompt_texts[i:i + args.gen_batch_size]
            enc = tokenizer(batch_prompts, return_tensors="pt", truncation=True,
                            max_length=args.max_length // 2, padding=True)
            input_ids = enc["input_ids"].to(device)
            attention_mask = enc["attention_mask"].to(device)

            with torch.no_grad():
                outputs = model.generate(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    max_new_tokens=args.gen_max_new_tokens,
                    do_sample=True,
                    top_p=args.top_p,
                    temperature=1.0,
                    pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
                )
            for seq in outputs:
                text = tokenizer.decode(seq, skip_special_tokens=True)
                generated_texts.append(text)
    finally:
        tokenizer.padding_side = original_padding_side

    return Dataset.from_dict({"text": generated_texts})


def mix_datasets(real_dataset, synthetic_dataset, synthetic_ratio, seed):
    """Mix real and synthetic data according to synthetic_ratio.

    Bidirectional subsampling to hit the target ratio:
    - Low α (enough synthetic): keep all real, subsample synthetic
    - High α (synthetic scarce): keep all synthetic, subsample real
    """
    if synthetic_ratio >= 1.0:
        return synthetic_dataset
    if synthetic_ratio <= 0.0:
        return real_dataset

    needed_syn = int(len(real_dataset) * synthetic_ratio / (1 - synthetic_ratio))
    if needed_syn <= len(synthetic_dataset):
        syn_subset = synthetic_dataset.shuffle(seed=seed).select(range(needed_syn))
        real_subset = real_dataset
    else:
        needed_real = int(len(synthetic_dataset) * (1 - synthetic_ratio) / synthetic_ratio)
        needed_real = min(needed_real, len(real_dataset))
        real_subset = real_dataset.shuffle(seed=seed).select(range(needed_real))
        syn_subset = synthetic_dataset

    actual_ratio = len(syn_subset) / (len(syn_subset) + len(real_subset))
    print(f"  Mix: {len(syn_subset)} syn + {len(real_subset)} real = {actual_ratio:.4f}")
    return concatenate_datasets([real_subset, syn_subset]).shuffle(seed=seed)


def tokenize_dataset(dataset, tokenizer, max_length):
    """Tokenize and chunk text for causal LM training."""
    def tokenize_fn(examples):
        return tokenizer(examples["text"], truncation=True,
                         max_length=max_length, padding="max_length")

    tokenized = dataset.map(tokenize_fn, batched=True,
                            remove_columns=["text"],
                            num_proc=1)
    tokenized.set_format("torch")
    return tokenized


def train_one_generation(model, tokenizer, train_dataset, args, gen_idx):
    """Fine-tune model for one generation."""
    tokenized = tokenize_dataset(train_dataset, tokenizer, args.max_length)

    training_args = TrainingArguments(
        output_dir=os.path.join(args.output_dir, f"gen_{gen_idx}", "trainer"),
        max_steps=args.steps_per_gen,
        per_device_train_batch_size=args.batch_size,
        learning_rate=args.lr,
        warmup_steps=min(500, args.steps_per_gen // 10),
        weight_decay=0.01,
        logging_steps=100,
        save_strategy="no",
        seed=args.seed + gen_idx,
        fp16=torch.cuda.is_available(),
        dataloader_drop_last=True,
        report_to="none",
    )

    collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized,
        data_collator=collator,
    )
    trainer.train()
    return model


def main():
    args = parse_args()
    set_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    with open(os.path.join(args.output_dir, "config.json"), "w") as f:
        json.dump(vars(args), f, indent=2)

    print(f"Loading model: {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(args.model_name)
    if torch.cuda.is_available():
        model = model.cuda()

    print(f"Loading data from {args.data_dir}")
    train_dataset = load_from_disk(os.path.join(args.data_dir, "train"))
    eval_dataset = load_from_disk(os.path.join(args.data_dir, "eval"))
    prompts_dataset = load_from_disk(os.path.join(args.data_dir, "prompts"))

    all_metrics = []
    synthetic_pool = []  # for --accumulate mode

    # --- Generation 0: baseline metrics (no training yet) ---
    print("=" * 60)
    print("Generation 0 (baseline)")
    print("=" * 60)

    gen0_synthetic = generate_synthetic_data(model, tokenizer, prompts_dataset, args)
    gen0_dir = os.path.join(args.output_dir, "gen_0")
    os.makedirs(gen0_dir, exist_ok=True)
    gen0_synthetic.save_to_disk(os.path.join(gen0_dir, "synthetic_data"))

    metrics = compute_all_metrics(model, tokenizer, eval_dataset, gen0_synthetic)
    metrics["generation"] = 0
    all_metrics.append(metrics)

    with open(os.path.join(gen0_dir, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Gen 0 metrics: ppl={metrics['perplexity']:.2f}, "
          f"entropy={metrics['token_entropy']:.4f}, "
          f"eff_rank={metrics['effective_rank']:.1f}")

    # --- Generations 1..N ---
    for gen in range(1, args.num_generations + 1):
        print("=" * 60)
        print(f"Generation {gen}/{args.num_generations}")
        print("=" * 60)

        gen_dir = os.path.join(args.output_dir, f"gen_{gen}")
        os.makedirs(gen_dir, exist_ok=True)

        # Step 1: generate synthetic data with current model
        print("  Generating synthetic data …")
        synthetic_data = generate_synthetic_data(
            model, tokenizer, prompts_dataset, args)
        synthetic_data.save_to_disk(os.path.join(gen_dir, "synthetic_data"))

        # Step 2: mix real + synthetic
        if args.accumulate:
            synthetic_pool.append(synthetic_data)
            effective_synthetic = concatenate_datasets(synthetic_pool)
        else:
            effective_synthetic = synthetic_data
        mixed = mix_datasets(train_dataset, effective_synthetic,
                             args.synthetic_ratio, args.seed + gen)
        print(f"  Mixed dataset: {len(mixed)} samples "
              f"(synthetic={len(effective_synthetic)}, "
              f"synthetic_ratio={args.synthetic_ratio}, "
              f"accumulate={args.accumulate})")

        # Step 3: fine-tune
        print("  Training …")
        model = train_one_generation(model, tokenizer, mixed, args, gen)

        # Step 4: save checkpoint
        ckpt_path = os.path.join(gen_dir, "checkpoint")
        model.save_pretrained(ckpt_path)
        tokenizer.save_pretrained(ckpt_path)
        print(f"  Checkpoint saved: {ckpt_path}")

        # Step 5: compute metrics
        print("  Computing metrics …")
        metrics = compute_all_metrics(model, tokenizer, eval_dataset,
                                      synthetic_data)
        metrics["generation"] = gen
        all_metrics.append(metrics)

        with open(os.path.join(gen_dir, "metrics.json"), "w") as f:
            json.dump(metrics, f, indent=2)
        print(f"  ppl={metrics['perplexity']:.2f}, "
              f"entropy={metrics['token_entropy']:.4f}, "
              f"eff_rank={metrics['effective_rank']:.1f}, "
              f"mauve={metrics.get('mauve', float('nan')):.4f}")

    # Save consolidated metrics
    metrics_path = os.path.join(args.output_dir, "all_metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(all_metrics, f, indent=2)
    print(f"\nAll metrics saved to {metrics_path}")

    sentinel_path = os.path.join(args.output_dir, "EXIT_CODE")
    with open(sentinel_path, "w") as f:
        f.write("0\n")
    print(f"Sentinel written: {sentinel_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        try:
            _args = parse_args()
            os.makedirs(_args.output_dir, exist_ok=True)
            with open(os.path.join(_args.output_dir, "EXIT_CODE"), "w") as f:
                f.write(f"1\n{e}\n")
        except Exception:
            pass
        raise
