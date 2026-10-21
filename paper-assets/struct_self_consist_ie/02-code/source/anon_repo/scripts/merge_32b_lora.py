"""Merge QLoRA adapter into base model for inference."""
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import sys

adapter_path = sys.argv[1]
output_path = sys.argv[2]

config = PeftConfig.from_pretrained(adapter_path)
base_model = AutoModelForCausalLM.from_pretrained(
    config.base_model_name_or_path,
    torch_dtype=torch.bfloat16,
    device_map="cpu",
)
model = PeftModel.from_pretrained(base_model, adapter_path)
merged = model.merge_and_unload()
merged.save_pretrained(output_path)

tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
tokenizer.save_pretrained(output_path)
print(f"Merged model saved to {output_path}")
