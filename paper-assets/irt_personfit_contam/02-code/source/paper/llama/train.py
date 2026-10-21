"""
train.py — QLoRA SFT training on Llama-3.1-8B-Instruct.

Usage: python train.py --condition clean --gpu 0
"""

import argparse
import json
import os

import torch
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import SFTConfig, SFTTrainer

BASE_DIR = "/path/to/project/llama"
MODEL_DIR = "/path/to/models"

SEED_MAP = {
    "contam_5": 42,
    "clean": 42,
    "contam_15": 42,
    "contam_25": 42,
    "contam_50": 42,
}


def find_model_path():
    patterns = [
        os.path.join(MODEL_DIR, "LLM-Research", "Meta-Llama-3___1-8B-Instruct"),
        os.path.join(MODEL_DIR, "LLM-Research", "Meta-Llama-3.1-8B-Instruct"),
        os.path.join(MODEL_DIR, "Llama-3.1-8B-Instruct"),
        os.path.join(MODEL_DIR, "Meta-Llama-3.1-8B-Instruct"),
    ]
    for p in patterns:
        if os.path.isdir(p):
            snapshot_dir = os.path.join(p, "snapshots")
            if os.path.isdir(snapshot_dir):
                snapshots = os.listdir(snapshot_dir)
                if snapshots:
                    return os.path.join(snapshot_dir, snapshots[0])
            if os.path.isfile(os.path.join(p, "config.json")):
                return p
    for root, dirs, files in os.walk(MODEL_DIR):
        if "config.json" in files and "Llama" in root and "8B" in root:
            return root
    raise FileNotFoundError(f"Cannot find Llama-3.1-8B-Instruct in {MODEL_DIR}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--condition", required=True, choices=list(SEED_MAP.keys()))
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--max_steps", type=int, default=-1)
    args = parser.parse_args()

    seed = SEED_MAP[args.condition]
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    model_path = find_model_path()
    print(f"Model path: {model_path}")
    print(f"Condition: {args.condition}, Seed: {seed}, GPU: {args.gpu}")

    data_path = os.path.join(BASE_DIR, "data", args.condition, "train.jsonl")
    with open(data_path) as f:
        records = [json.loads(line) for line in f]
    dataset = Dataset.from_list(records)
    print(f"Training samples: {len(dataset)}")

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        quantization_config=bnb_config,
        device_map={"": 0},
        trust_remote_code=True,
    )
    model = prepare_model_for_kbit_training(model)

    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    output_dir = os.path.join(BASE_DIR, "checkpoints", args.condition)

    use_bf16 = torch.cuda.is_bf16_supported()
    training_args = SFTConfig(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        warmup_ratio=0.1,
        bf16=use_bf16,
        fp16=not use_bf16,
        logging_steps=10,
        save_strategy="epoch",
        seed=seed,
        report_to="none",
        run_name=f"ctrl-contam-llama-{args.condition}",
        max_steps=args.max_steps,
        dataloader_num_workers=2,
        remove_unused_columns=False,
        max_length=512,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
    )

    trainer.train()
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"Model saved to {output_dir}")


if __name__ == "__main__":
    main()
