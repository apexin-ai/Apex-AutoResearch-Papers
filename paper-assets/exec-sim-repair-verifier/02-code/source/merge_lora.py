#!/usr/bin/env python3
"""merge_lora.py — Merge LoRA adapter into base model for vLLM serving.

Usage:
  python merge_lora.py \
    --base /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
    --adapter /root/autodl-tmp/checkpoints_backup_cwm_8b/checkpoint-400/ \
    --output /root/autodl-tmp/merged_cwm_8b_ckpt400/
"""

import argparse
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", required=True, help="Base model path")
    p.add_argument("--adapter", required=True, help="LoRA adapter checkpoint path")
    p.add_argument("--output", required=True, help="Output directory for merged model")
    args = p.parse_args()

    print(f"Loading base model: {args.base}")
    model = AutoModelForCausalLM.from_pretrained(
        args.base, torch_dtype=torch.bfloat16, trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(args.base, trust_remote_code=True)

    print(f"Loading adapter: {args.adapter}")
    model = PeftModel.from_pretrained(model, args.adapter)

    print("Merging weights...")
    model = model.merge_and_unload()

    print(f"Saving to: {args.output}")
    model.save_pretrained(args.output)
    tokenizer.save_pretrained(args.output)
    print("Done.")


if __name__ == "__main__":
    main()
