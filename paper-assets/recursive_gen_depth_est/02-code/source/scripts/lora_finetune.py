"""LoRA 微调脚本，支持任意 depth 的数据输入。每代从 base model 重新微调。"""

import argparse
import json
import os
import torch
from torch.utils.data import Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)
from peft import LoraConfig, get_peft_model


class TextDataset(Dataset):
    def __init__(self, data_path, tokenizer, max_seq_len):
        self.examples = []
        with open(data_path, "r", encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                encoded = tokenizer(
                    rec["text"],
                    truncation=True,
                    max_length=max_seq_len,
                    padding=False,
                )
                self.examples.append(encoded)

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        return {k: torch.tensor(v) for k, v in self.examples[idx].items()}


def parse_args():
    p = argparse.ArgumentParser(description="LoRA fine-tune on depth-N data")
    p.add_argument("--input_data", required=True, help="Input jsonl path")
    p.add_argument("--output_dir", required=True, help="LoRA adapter save path")
    p.add_argument("--model_name", default="EleutherAI/pythia-1.4b", help="Base model name")
    p.add_argument("--model_cache", default="/root/autodl-tmp/models/pythia-1.4b", help="Model cache dir")
    p.add_argument("--target_modules", default="query_key_value", help="Comma-separated LoRA target module names")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--lr", type=float, default=2e-4)
    p.add_argument("--batch_size", type=int, default=8)
    p.add_argument("--gradient_accumulation", type=int, default=2)
    p.add_argument("--max_seq_len", type=int, default=512)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gpu", type=int, default=0)
    return p.parse_args()


def main():
    args = parse_args()

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    device = torch.device("cuda:0")

    print(f"Loading tokenizer and model: {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name,
        cache_dir=args.model_cache,
        trust_remote_code=True,
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        cache_dir=args.model_cache,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
    )

    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=[m.strip() for m in args.target_modules.split(",")],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    print(f"Loading dataset: {args.input_data}")
    dataset = TextDataset(args.input_data, tokenizer, args.max_seq_len)
    print(f"Dataset size: {len(dataset)}")

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation,
        learning_rate=args.lr,
        bf16=True,
        logging_steps=10,
        save_strategy="epoch",
        save_total_limit=1,
        seed=args.seed,
        report_to="none",
        remove_unused_columns=False,
        dataloader_pin_memory=True,
        dataloader_num_workers=4,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=data_collator,
    )

    print("Starting training...")
    result = trainer.train()
    print(f"Training complete. Final loss: {result.training_loss:.4f}")

    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    print(f"LoRA adapter saved to {args.output_dir}")


if __name__ == "__main__":
    main()
