"""exp006 Continued Pretraining — LoRA CPT of Qwen2.5-1.5B on filtered depth chain data.

Input:  Qwen/Qwen2.5-1.5B-Instruct (base), data/ (features + text), strategy config
Output: LoRA adapter checkpoint in --output-dir/final_adapter/

Dependencies: torch, transformers, peft, lightgbm, numpy, pandas
"""

import argparse
import json
import os
import sys

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
    set_seed,
)
from peft import LoraConfig, get_peft_model, TaskType

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exp006_filtering_strategies import STRATEGIES, FEATURE_COLS, load_data


class TextDataset(Dataset):
    def __init__(self, texts, tokenizer, max_length=512):
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        enc = self.tokenizer(
            self.texts[idx],
            truncation=True,
            max_length=self.max_length,
            padding=False,
            return_attention_mask=False,
        )
        return {"input_ids": enc["input_ids"]}


def make_weighted_trainer(weights_array):
    """Return a Trainer subclass that uses weighted sampling when weights are non-uniform."""
    uniform = np.allclose(weights_array, 1.0)

    class WeightedTrainer(Trainer):
        def get_train_dataloader(self):
            if uniform:
                return super().get_train_dataloader()
            sampler = WeightedRandomSampler(
                weights=weights_array.tolist(),
                num_samples=len(weights_array),
                replacement=True,
            )
            return DataLoader(
                self.train_dataset,
                batch_size=self.args.per_device_train_batch_size,
                sampler=sampler,
                collate_fn=self.data_collator,
                num_workers=self.args.dataloader_num_workers,
                pin_memory=self.args.dataloader_pin_memory,
            )

    return WeightedTrainer


def main():
    parser = argparse.ArgumentParser(description="exp006 continued pretraining")
    parser.add_argument("--model-name", type=str, default="Qwen/Qwen2.5-1.5B-Instruct")
    parser.add_argument("--data-dir", type=str, default="data/")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--strategy", type=str, required=True,
                        choices=list(STRATEGIES.keys()))
    parser.add_argument("--alpha", type=float, default=0.5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--warmup-ratio", type=float, default=0.1)
    parser.add_argument("--lora-rank", type=int, default=8)
    parser.add_argument("--lora-alpha", type=int, default=16)
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")
    args = parser.parse_args()

    set_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    # --- Load & filter ---
    print(f"Loading data from {args.data_dir}")
    df, texts, _ = load_data(args.data_dir)
    features = df[FEATURE_COLS].values
    depths = df["depth"].values

    kwargs = {}
    if args.strategy == "graduated":
        kwargs["alpha"] = args.alpha
    if args.strategy in ("binary-drayson", "dsir"):
        kwargs["seed"] = args.seed
    strategy = STRATEGIES[args.strategy](**kwargs)

    print(f"Fitting strategy: {args.strategy}")
    strategy.fit(features, depths, texts)
    weights = strategy.get_weights(features, texts)

    # Remove zero-weight samples
    nonzero = weights > 1e-8
    filtered_texts = [t for t, nz in zip(texts, nonzero) if nz]
    filtered_weights = weights[nonzero]
    print(f"Samples after filtering: {len(filtered_texts)}/{len(texts)} "
          f"({len(filtered_texts)/len(texts)*100:.1f}%)")

    # Save filter config
    config = {
        "strategy": args.strategy,
        "alpha": args.alpha if args.strategy == "graduated" else None,
        "seed": args.seed,
        "n_total": len(texts),
        "n_filtered": len(filtered_texts),
        "weight_mean": float(filtered_weights.mean()),
        "weight_std": float(filtered_weights.std()),
    }
    with open(os.path.join(args.output_dir, "filter_config.json"), "w") as f:
        json.dump(config, f, indent=2)

    # --- Model ---
    print(f"Loading {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name, cache_dir=args.cache_dir, trust_remote_code=True,
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name, cache_dir=args.cache_dir,
        torch_dtype=torch.bfloat16, trust_remote_code=True,
    )

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # --- Dataset ---
    dataset = TextDataset(filtered_texts, tokenizer, args.max_length)
    collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    # --- Train ---
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.lr,
        warmup_ratio=args.warmup_ratio,
        bf16=True,
        logging_steps=50,
        save_strategy="epoch",
        save_total_limit=1,
        seed=args.seed,
        report_to="none",
        dataloader_num_workers=2,
        dataloader_pin_memory=True,
        remove_unused_columns=False,
    )

    TrainerCls = make_weighted_trainer(filtered_weights)
    trainer = TrainerCls(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=collator,
    )

    print("Training...")
    train_result = trainer.train()
    print(f"Train loss: {train_result.training_loss:.4f}")

    # Save adapter
    adapter_dir = os.path.join(args.output_dir, "final_adapter")
    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)
    print(f"Adapter saved to {adapter_dir}")

    # Save train metrics
    metrics = {
        "train_loss": train_result.training_loss,
        "train_runtime": train_result.metrics.get("train_runtime", 0),
        "train_samples_per_second": train_result.metrics.get("train_samples_per_second", 0),
    }
    with open(os.path.join(args.output_dir, "train_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    del model, trainer
    torch.cuda.empty_cache()
    print("Done.")


if __name__ == "__main__":
    main()
