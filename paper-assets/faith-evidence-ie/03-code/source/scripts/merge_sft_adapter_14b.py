"""Merge 14B SFT adapter into base model for RSFT training.

ZeRO-3 parameter partitioning is incompatible with runtime adapter merge,
so we pre-merge and save the full model to disk.

Usage: python scripts/merge_sft_adapter_14b.py
"""
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

BASE_MODEL = "/path/to/Qwen3-14B"
SFT_ADAPTER = "./outputs/sft_14b"
OUTPUT_DIR = "/path/to/Qwen3-14B-sft-merged"

print(f"Loading base model: {BASE_MODEL}")
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL, torch_dtype=torch.bfloat16, device_map="cpu",
    trust_remote_code=True,
)

print(f"Loading and merging SFT adapter: {SFT_ADAPTER}")
model = PeftModel.from_pretrained(model, SFT_ADAPTER)
model = model.merge_and_unload()

print(f"Saving merged model to: {OUTPUT_DIR}")
model.save_pretrained(OUTPUT_DIR)

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
tokenizer.save_pretrained(OUTPUT_DIR)

print("Done.")
