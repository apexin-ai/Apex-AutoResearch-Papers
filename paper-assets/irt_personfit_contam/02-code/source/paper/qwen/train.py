"""
train.py — QLoRA SFT training on Qwen2.5-7B-Instruct / Llama-3.1-8B / Mistral-7B.

Usage: python train.py --condition clean_s1 --gpu 0 [--model qwen]
"""

import argparse
import glob
import json
import os

import torch
import os
assert torch.cuda.device_count() == 1, f"Expected 1 GPU but found {torch.cuda.device_count()}. Set CUDA_VISIBLE_DEVICES first!"
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,

)
from trl import SFTConfig, SFTTrainer

BASE_DIR = "/path/to/project/qwen"
HF_CACHE = "/path/to/hf_cache"

MODEL_PATHS = {
    "qwen": None,
    "llama": "/path/to/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/",
    "mistral": "/path/to/hf_cache/mistralai/Mistral-7B-Instruct-v0___3/",
}

SEED_MAP = {
    "clean_s1": 42,
    "clean_s2": 123,
    "contam_15": 42,
    "contam_25": 42,
    "contam_5": 42,
    "contam_5_s2": 123,
    "contam_15_s2": 123,
    "contam_15_s3": 456,
    "contam_25_s2": 123,
    "contam_25_s3": 456,
    "contam_50_s2": 123,
    "contam_50_s3": 456,
    "contam_5_s3": 456,
    "contam_50": 42,
    "clean_s3": 456,
    "clean_s4": 301,
    "clean_s5": 302,
    "clean_s6": 303,
    "clean_s7": 304,
    "clean_s8": 305,
    "clean_s9": 306,
    "clean_s10": 307,
}


def find_qwen_path():
    patterns = [
        os.path.join(HF_CACHE, "Qwen", "Qwen2.5-7B-Instruct"),
        os.path.join(HF_CACHE, "Qwen2___5-7B-Instruct"),
        os.path.join(HF_CACHE, "models--Qwen--Qwen2.5-7B-Instruct"),
        os.path.join(HF_CACHE, "Qwen", "Qwen2___5-7B-Instruct"),
        os.path.join(HF_CACHE, "qwen", "Qwen2___5-7B-Instruct"),
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
    for root, dirs, files in os.walk(HF_CACHE):
        if "config.json" in files and "Qwen2.5-7B-Instruct" in root:
            return root
    raise FileNotFoundError(f"Cannot find Qwen2.5-7B-Instruct in {HF_CACHE}")


def get_model_path(model_name):
    if model_name == "qwen":
        return find_qwen_path()
    path = MODEL_PATHS[model_name]
    if not os.path.isdir(path):
        raise FileNotFoundError(f"Model path not found: {path}")
    return path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--condition", required=True, choices=list(SEED_MAP.keys()))
    parser.add_argument("--model", default="qwen", choices=list(MODEL_PATHS.keys()))
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--max_steps", type=int, default=-1, help="Override for dry-run")
    args = parser.parse_args()

    seed = SEED_MAP[args.condition]
    # GPU assignment handled by framework via CUDA_VISIBLE_DEVICES

    model_path = get_model_path(args.model)
    print(f"Model path: {model_path}")
    print(f"Model: {args.model}, Condition: {args.condition}, Seed: {seed}, GPU: {args.gpu}")

    # Load training data
    data_path = os.path.join(BASE_DIR, "data", args.condition, "train.jsonl")
    with open(data_path) as f:
        records = [json.loads(line) for line in f]
    dataset = Dataset.from_list(records)
    print(f"Training samples: {len(dataset)}")

    # QLoRA config
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
    )

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        quantization_config=bnb_config,
        device_map={"": 0},
        trust_remote_code=True,
    )
    model = prepare_model_for_kbit_training(model)

    # LoRA config
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

    if args.model == "qwen":
        output_dir = os.path.join(BASE_DIR, "checkpoints", args.condition)
        run_name = f"ctrl-contam-{args.condition}"
    else:
        output_dir = os.path.join(BASE_DIR, "checkpoints", args.model, args.condition)
        run_name = f"ctrl-contam-{args.model}-{args.condition}"

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
        run_name=run_name,
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
