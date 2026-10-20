"""Compare spectral effective rank on holdout vs model-generated text.

Tests whether eff_rank computed on generated text drops earlier than
eff_rank on holdout, since generation diversity collapses before the
model's ability to encode held-out inputs degrades.

Usage:
    python analyze_generated_eff_rank.py \
        --checkpoint-dir /root/autodl-tmp/output_v7/ \
        --model-name EleutherAI/pythia-1b \
        --output-dir /root/autodl-tmp/output_v7/pivot_analysis/

Input:
    Checkpoint directory with G0/G1/G2 subdirs, each containing
    training/checkpoint-*/  and/or final_model/ directories.

Output:
    - generated_vs_holdout_eff_rank.json: per-checkpoint comparison
    - Printed summary table
"""

import argparse
import json
import math
import os
import sys
from pathlib import Path

import torch
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


def find_checkpoints(base_dir: str) -> list[dict]:
    """Find all checkpoints across generations, sorted by (gen, step)."""
    base = Path(base_dir)
    checkpoints = []
    for gen_dir in sorted(base.glob("G*")):
        gen_idx = int(gen_dir.name[1:])
        for ckpt in sorted(gen_dir.glob("training/checkpoint-*")):
            step = int(ckpt.name.split("-")[-1])
            checkpoints.append({"gen": gen_idx, "step": step, "path": str(ckpt)})
        final = gen_dir / "final_model"
        if final.exists():
            checkpoints.append({"gen": gen_idx, "step": 999999, "path": str(final), "is_final": True})
    return checkpoints


def compute_eff_rank_from_hidden(hidden_list: list[torch.Tensor], max_samples: int) -> float:
    """SVD-based effective rank from collected hidden states."""
    E = torch.cat(hidden_list, dim=0)[:max_samples]
    sigma = torch.linalg.svdvals(E)
    sigma_pos = sigma[sigma > 0]
    p = sigma_pos / sigma_pos.sum()
    entropy = -(p * p.log()).sum().item()
    return math.exp(entropy)


def compute_holdout_eff_rank(
    model, tokenizer, holdout_texts: list[str],
    num_samples: int, device: str, max_length: int = 2048,
) -> float:
    """Effective rank on holdout text (standard approach)."""
    model.eval()
    hidden_list = []
    collected = 0
    batch_size = 8

    for i in range(0, len(holdout_texts), batch_size):
        if collected >= num_samples:
            break
        batch_texts = holdout_texts[i:i + batch_size]
        enc = tokenizer(batch_texts, return_tensors="pt", padding=True,
                        truncation=True, max_length=max_length).to(device)
        with torch.no_grad():
            out = model(**enc, output_hidden_states=True)
        h = out.hidden_states[-1].float()
        mask = enc["attention_mask"].unsqueeze(-1).float()
        pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)
        hidden_list.append(pooled.cpu())
        collected += pooled.shape[0]

    return compute_eff_rank_from_hidden(hidden_list, num_samples)


def compute_generated_eff_rank(
    model, tokenizer,
    num_samples: int, max_length: int, device: str,
) -> float:
    """Effective rank on model's own generated text."""
    model.eval()
    hidden_list = []
    collected = 0
    gen_batch = 16

    while collected < num_samples:
        n = min(gen_batch, num_samples - collected)
        input_ids = tokenizer.bos_token_id if tokenizer.bos_token_id is not None else tokenizer.eos_token_id
        inputs = torch.full((n, 1), input_ids, dtype=torch.long, device=device)

        with torch.no_grad():
            gen_ids = model.generate(
                inputs, max_new_tokens=max_length, do_sample=True,
                temperature=1.0, top_p=0.95, pad_token_id=tokenizer.pad_token_id,
            )
            enc = tokenizer.pad(
                {"input_ids": [ids for ids in gen_ids]},
                return_tensors="pt", padding=True,
            ).to(device)
            out = model(**enc, output_hidden_states=True)

        h = out.hidden_states[-1].float()
        mask = enc["attention_mask"].unsqueeze(-1).float()
        pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)
        hidden_list.append(pooled.cpu())
        collected += pooled.shape[0]

    return compute_eff_rank_from_hidden(hidden_list, num_samples)


def main():
    parser = argparse.ArgumentParser(description="Compare holdout vs generated eff_rank")
    parser.add_argument("--checkpoint-dir", required=True)
    parser.add_argument("--model-name", default="EleutherAI/pythia-1b")
    parser.add_argument("--num-samples", type=int, default=1000)
    parser.add_argument("--max-length", type=int, default=2048)
    parser.add_argument("--max-lengths", default=None,
                        help="Comma-separated lengths for ablation (e.g. 512,1024,2048). "
                             "Overrides --max-length when set.")
    parser.add_argument("--only-final", action="store_true",
                        help="Only evaluate final_model checkpoints (skip training checkpoints)")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--holdout-texts", default=None,
                        help="Path to holdout text file (one doc per line). "
                             "If omitted, uses wikitext-103 validation split.")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    os.makedirs(args.output_dir, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    if args.holdout_texts:
        with open(args.holdout_texts) as f:
            holdout_texts = [line.strip() for line in f if line.strip()]
    else:
        from datasets import load_dataset
        ds = load_dataset("wikitext", "wikitext-103-raw-v1", split="validation")
        holdout_texts = [t for t in ds["text"] if len(t.strip()) > 100][:5000]

    checkpoints = find_checkpoints(args.checkpoint_dir)
    if args.only_final:
        checkpoints = [c for c in checkpoints if c.get("is_final")]
    if not checkpoints:
        print("ERROR: No checkpoints found", file=sys.stderr)
        sys.exit(1)

    max_lengths = (
        [int(x) for x in args.max_lengths.split(",")]
        if args.max_lengths else [args.max_length]
    )

    results = []
    for ckpt in tqdm(checkpoints, desc="checkpoints"):
        print(f"\n=== G{ckpt['gen']} step={ckpt['step']} ===")
        model = AutoModelForCausalLM.from_pretrained(
            ckpt["path"], torch_dtype=torch.bfloat16,
        ).to(device)

        holdout_rank = compute_holdout_eff_rank(
            model, tokenizer, holdout_texts, args.num_samples, device,
            max_length=max(max_lengths))

        for max_len in max_lengths:
            generated_rank = compute_generated_eff_rank(
                model, tokenizer, args.num_samples, max_len, device)

            entry = {
                "generation": ckpt["gen"],
                "step": ckpt["step"],
                "checkpoint": ckpt["path"],
                "max_length": max_len,
                "holdout_eff_rank": round(holdout_rank, 2),
                "generated_eff_rank": round(generated_rank, 2),
                "delta": round(holdout_rank - generated_rank, 2),
            }
            results.append(entry)
            print(f"  len={max_len}: holdout={holdout_rank:.1f}  "
                  f"generated={generated_rank:.1f}  "
                  f"delta={holdout_rank - generated_rank:.1f}")

        del model
        torch.cuda.empty_cache()

    print(f"\n{'Gen':<5} {'Step':<8} {'MaxLen':<8} {'Holdout':<10} "
          f"{'Generated':<10} {'Delta':<8}")
    print("-" * 53)
    for r in results:
        print(f"G{r['generation']:<4} {r['step']:<8} {r['max_length']:<8} "
              f"{r['holdout_eff_rank']:<10.1f} "
              f"{r['generated_eff_rank']:<10.1f} {r['delta']:<8.1f}")

    out_path = os.path.join(args.output_dir, "generated_vs_holdout_eff_rank.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
