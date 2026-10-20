"""Pre-merge base + SFT + RSFT for GRPO training."""
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

BASE = "./outputs"
SFT = "./outputs"
RSFT = "./outputs"
OUT = "./outputs"

print("Loading base model...")
model = AutoModelForCausalLM.from_pretrained(BASE, torch_dtype=torch.bfloat16, device_map="cpu")

print("Merging SFT adapter...")
model = PeftModel.from_pretrained(model, SFT)
model = model.merge_and_unload()

print("Merging RSFT adapter...")
model = PeftModel.from_pretrained(model, RSFT)
model = model.merge_and_unload()

print("Saving merged model...")
model.save_pretrained(OUT)

print("Saving tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(SFT)
tokenizer.save_pretrained(OUT)

print(f"Merge complete -> {OUT}")
