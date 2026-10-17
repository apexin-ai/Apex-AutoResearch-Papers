"""K ablation sweep: vary max_2bit cardinality constraint in constrained MCKP.
Input: hires PPL profiles JSON, model checkpoint
Output: per-k PPL + bit distribution, saved to JSON
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import argparse
import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from solver import solve_mckp_constrained, enforce_monotonicity
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity


def run_k_ablation(model_path, profiles_path, k_values, budget, device, output_path):
    with open(profiles_path) as f:
        data = json.load(f)
    profiles = data["profiles"]
    model_name = data.get("model_name", os.path.basename(model_path))

    enforced = enforce_monotonicity(profiles)

    n_heads = sum(len(heads) for heads in profiles.values())
    print(f"Model: {model_name}, {n_heads} KV heads, budget={budget}")
    print(f"K values: {k_values}")
    print(f"Profiles: {profiles_path}")

    print("\nLoading model...")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()

    results = []
    for k in k_values:
        print(f"\n{'='*60}")
        print(f"max_2bit = {k}")
        print(f"{'='*60}")

        t0 = time.time()
        sol = solve_mckp_constrained(
            enforced, budget, mode="quant_only",
            max_2bit=k, l0_exclude_2bit=True
        )
        t_solve = time.time() - t0

        bit_dist = sol["bit_distribution"]
        mem_ratio = sol["actual_memory_ratio"]
        print(f"Bit dist: {bit_dist}, mem_ratio: {mem_ratio:.4f}, solve: {t_solve:.2f}s")

        orig = patch_attention(model, sol["allocation"])
        ppl = evaluate_perplexity(model, tokenizer, device)
        restore_attention(model, orig)

        print(f">>> PPL = {ppl:.4f}")

        results.append({
            "max_2bit": k,
            "ppl": round(ppl, 4),
            "n_2bit": bit_dist.get(2, 0),
            "n_4bit": bit_dist.get(4, 0),
            "n_8bit": bit_dist.get(8, 0),
            "n_16bit": bit_dist.get(16, 0),
            "mem_ratio": round(mem_ratio, 4),
            "total_distortion": round(sol["total_distortion"], 6),
            "allocation": sol["allocation"],
        })

    output = {
        "model": model_path,
        "model_name": model_name,
        "budget": budget,
        "n_heads": n_heads,
        "profiles_file": profiles_path,
        "k_values": k_values,
        "results": results,
    }
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*60}")
    print(f"{model_name} k ablation (budget={budget}, hires profiling):")
    print(f"{'='*60}")
    print(f"{'k':>5} {'PPL':>10} {'2bit':>6} {'4bit':>6} {'8bit':>6} {'16bit':>6} {'mem':>8}")
    print("-" * 55)
    for r in results:
        print(f"{r['max_2bit']:>5} {r['ppl']:>10.4f} {r['n_2bit']:>6} {r['n_4bit']:>6} "
              f"{r['n_8bit']:>6} {r['n_16bit']:>6} {r['mem_ratio']:>8.4f}")

    best = min(results, key=lambda r: r["ppl"])
    print(f"\nBest k: {best['max_2bit']} (PPL={best['ppl']:.4f})")
    print(f"Saved: {output_path}")
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--profiles", type=str, required=True)
    parser.add_argument("--gpu", type=str, default="cuda:0")
    parser.add_argument("--k_values", type=str, default="4,8,12,16,18")
    parser.add_argument("--budget", type=float, default=0.25)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    k_values = [int(x) for x in args.k_values.split(",")]
    run_k_ablation(args.model, args.profiles, k_values, args.budget, args.gpu, args.output)


if __name__ == "__main__":
    main()
