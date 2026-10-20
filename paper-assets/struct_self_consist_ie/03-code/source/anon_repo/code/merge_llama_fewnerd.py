"""Merge LLaMA 3.1-8B base with FewNERD LoRA adapter."""
import argparse
import os
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base_model", default="/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct")
    p.add_argument("--adapter_path", default="/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora")
    p.add_argument("--output_path", default="/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-merged")
    args = p.parse_args()

    if os.path.exists(os.path.join(args.output_path, "config.json")):
        print(f"Merged model already exists at {args.output_path}, skipping")
        return

    print(f"Loading base model from {args.base_model}...")
    base = AutoModelForCausalLM.from_pretrained(
        args.base_model, torch_dtype=torch.bfloat16, device_map="cpu"
    )
    print(f"Loading LoRA adapter from {args.adapter_path}...")
    model = PeftModel.from_pretrained(base, args.adapter_path)
    print("Merging and unloading...")
    model = model.merge_and_unload()

    os.makedirs(args.output_path, exist_ok=True)
    print(f"Saving merged model to {args.output_path}...")
    model.save_pretrained(args.output_path)
    tokenizer = AutoTokenizer.from_pretrained(args.base_model)
    tokenizer.save_pretrained(args.output_path)
    print("Merge complete.")


if __name__ == "__main__":
    main()
