"""用 LoRA 微调后的模型无条件生成下一代文本。seed_id 与输入数据一一对应。"""

import argparse
import json
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel


def parse_args():
    p = argparse.ArgumentParser(description="Generate next-depth text with LoRA model")
    p.add_argument("--adapter_dir", required=True, help="LoRA adapter path")
    p.add_argument("--input_data", required=True, help="Previous depth data (for seed_id list)")
    p.add_argument("--output_path", required=True, help="Output jsonl path")
    p.add_argument("--model_name", default="Qwen/Qwen2.5-1.5B", help="Base model name")
    p.add_argument("--model_cache", default="/root/autodl-tmp/.hf_cache", help="Model cache dir")
    p.add_argument("--target_depth", type=int, required=True, help="Target depth (1, 2, 3)")
    p.add_argument("--num_samples", type=int, default=5000, help="Number of samples to generate")
    p.add_argument("--max_new_tokens", type=int, default=512)
    p.add_argument("--temperature", type=float, default=1.0)
    p.add_argument("--top_p", type=float, default=0.95)
    p.add_argument("--top_k", type=int, default=50)
    p.add_argument("--decoding_strategy", default="nucleus",
                   choices=["nucleus", "topk", "temp_only"],
                   help="Decoding strategy: nucleus (top_p), topk (top_k), temp_only")
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


def load_seed_ids(input_data, num_samples):
    seed_ids = []
    with open(input_data, "r", encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            seed_ids.append(rec["seed_id"])
    if len(seed_ids) < num_samples:
        repeats = (num_samples // len(seed_ids)) + 1
        seed_ids = (seed_ids * repeats)[:num_samples]
    else:
        seed_ids = seed_ids[:num_samples]
    return seed_ids


def main():
    args = parse_args()

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    device = torch.device("cuda:0")
    torch.manual_seed(args.seed)

    print(f"Loading base model: {args.model_name}")
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

    print(f"Loading LoRA adapter: {args.adapter_dir}")
    model = PeftModel.from_pretrained(model, args.adapter_dir)
    model = model.to(device)
    model.eval()

    seed_ids = load_seed_ids(args.input_data, args.num_samples)
    total = len(seed_ids)
    print(f"Generating {total} samples at depth {args.target_depth}")

    bos_token_id = tokenizer.bos_token_id
    if bos_token_id is None:
        bos_token_id = tokenizer.eos_token_id

    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)

    generated = 0
    with open(args.output_path, "w", encoding="utf-8") as fout:
        for batch_start in range(0, total, args.batch_size):
            batch_end = min(batch_start + args.batch_size, total)
            batch_seed_ids = seed_ids[batch_start:batch_end]
            cur_batch_size = len(batch_seed_ids)

            input_ids = torch.tensor([[bos_token_id]] * cur_batch_size, device=device)
            attention_mask = torch.ones_like(input_ids)

            gen_kwargs = {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "max_new_tokens": args.max_new_tokens,
                "do_sample": True,
                "pad_token_id": tokenizer.pad_token_id,
            }
            if args.decoding_strategy == "nucleus":
                gen_kwargs["top_p"] = args.top_p
                gen_kwargs["temperature"] = args.temperature
            elif args.decoding_strategy == "topk":
                gen_kwargs["top_k"] = args.top_k
                gen_kwargs["temperature"] = args.temperature
            elif args.decoding_strategy == "temp_only":
                gen_kwargs["temperature"] = args.temperature

            with torch.no_grad():
                outputs = model.generate(**gen_kwargs)

            for i, output in enumerate(outputs):
                text = tokenizer.decode(output[1:], skip_special_tokens=True)
                token_count = len(output) - 1
                record = {
                    "text": text,
                    "depth": args.target_depth,
                    "seed_id": batch_seed_ids[i],
                    "token_count": token_count,
                }
                fout.write(json.dumps(record, ensure_ascii=False) + "\n")

            generated += cur_batch_size
            if generated % (args.batch_size * 10) == 0 or generated == total:
                print(f"  Generated {generated}/{total}")

    print(f"Done. {total} samples saved to {args.output_path}")


if __name__ == "__main__":
    main()
