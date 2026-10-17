"""plan_015 corrected: L0 heuristic baseline with exact budget=0.25.

Strategies:
1. L0-random: L0@8-bit, k random non-L0 heads@2-bit, rest@4-bit (5 seeds)
2. Naive positional: L0@8-bit, deepest k heads@2-bit, rest@4-bit
3. MCKP optimal: reference existing results
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import json
import math
import random
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity

DEVICE = "cuda:0"

MODELS = {
    "Qwen2.5-7B": {
        "path": "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B",
        "num_layers": 28,
        "num_kv_heads": 4,
        "k": 8,
        "mckp_ppl": 9.569,
    },
    "Llama-3.1-8B": {
        "path": "/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B/",
        "num_layers": 32,
        "num_kv_heads": 8,
        "k": 16,
        "mckp_ppl": 8.4498,
    },
    "Mistral-7B-v0.3": {
        "path": "/root/autodl-tmp/models/mistralai/Mistral-7B-v0___3/",
        "num_layers": 32,
        "num_kv_heads": 8,
        "k": 16,
        "mckp_ppl": 7.323,
    },
}

SEEDS = [0, 1, 2, 3, 4]


def compute_budget(alloc, n_total_heads):
    total_bits = sum(bits for _, bits in alloc.values())
    return total_bits / (n_total_heads * 16)


def build_l0_random_allocation(num_layers, num_kv_heads, k, seed):
    """L0@8-bit, k random non-L0 heads@2-bit, rest@4-bit."""
    rng = random.Random(seed)
    non_l0_heads = [(l, h) for l in range(1, num_layers) for h in range(num_kv_heads)]
    chosen_2bit = set(rng.sample(non_l0_heads, k))

    alloc = {}
    for l in range(num_layers):
        for h in range(num_kv_heads):
            if l == 0:
                alloc[f"{l},{h}"] = ["quant", 8]
            elif (l, h) in chosen_2bit:
                alloc[f"{l},{h}"] = ["quant", 2]
            else:
                alloc[f"{l},{h}"] = ["quant", 4]
    return alloc, chosen_2bit


def build_naive_heuristic_allocation(num_layers, num_kv_heads, k):
    """L0@8-bit, deepest k heads@2-bit, rest@4-bit."""
    alloc = {}
    twobit_set = set()
    remaining = k
    for l in range(num_layers - 1, 0, -1):
        if remaining <= 0:
            break
        assign = min(num_kv_heads, remaining)
        for h in range(assign):
            twobit_set.add((l, h))
        remaining -= assign

    for l in range(num_layers):
        for h in range(num_kv_heads):
            if l == 0:
                alloc[f"{l},{h}"] = ["quant", 8]
            elif (l, h) in twobit_set:
                alloc[f"{l},{h}"] = ["quant", 2]
            else:
                alloc[f"{l},{h}"] = ["quant", 4]
    return alloc


def eval_allocation(model, tokenizer, alloc, label):
    print(f"\nEval: {label}...")
    orig = patch_attention(model, alloc)
    ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f">>> {label} PPL: {ppl:.4f}")
    return ppl


def main():
    all_results = {}
    t_start = time.time()

    for model_name, cfg in MODELS.items():
        print(f"\n{'='*60}")
        print(f"Model: {model_name}")
        print(f"{'='*60}")

        n_layers = cfg["num_layers"]
        n_kv = cfg["num_kv_heads"]
        k = cfg["k"]
        n_total = n_layers * n_kv

        # Budget verification
        # L0: n_kv heads @8-bit, k heads @2-bit, rest @4-bit
        expected_bits = n_kv * 8 + k * 2 + (n_total - n_kv - k) * 4
        expected_budget = expected_bits / (n_total * 16)
        assert abs(expected_budget - 0.25) < 1e-9, \
            f"Budget mismatch for {model_name}: {expected_budget} != 0.25"
        print(f"Budget verified: {expected_bits}/{n_total*16} = {expected_budget:.4f}")

        print(f"Loading {cfg['path']}...")
        tokenizer = AutoTokenizer.from_pretrained(cfg["path"])
        model = AutoModelForCausalLM.from_pretrained(
            cfg["path"], torch_dtype=torch.bfloat16, attn_implementation="eager"
        )
        model = model.to(DEVICE)
        model.eval()

        # Baseline bf16
        print("\nEval: baseline (bf16, no quant)...")
        baseline_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
        print(f">>> Baseline PPL: {baseline_ppl:.4f}")

        # Uniform 4-bit
        uniform_alloc = {f"{l},{h}": ["quant", 4]
                         for l in range(n_layers) for h in range(n_kv)}
        uniform_ppl = eval_allocation(model, tokenizer, uniform_alloc, "Uniform 4-bit")

        # L0-random baseline (5 seeds)
        l0_random_results = {}
        for seed in SEEDS:
            alloc, chosen = build_l0_random_allocation(n_layers, n_kv, k, seed)
            budget = compute_budget(alloc, n_total)
            assert abs(budget - 0.25) < 1e-9, f"L0-random budget {budget} != 0.25"
            ppl = eval_allocation(
                model, tokenizer, alloc,
                f"L0-random seed={seed} (budget={budget:.4f})"
            )
            l0_random_results[f"seed_{seed}"] = ppl

        l0_vals = list(l0_random_results.values())
        l0_mean = sum(l0_vals) / len(l0_vals)
        l0_std = math.sqrt(sum((v - l0_mean)**2 for v in l0_vals) / len(l0_vals))
        l0_random_results["mean"] = l0_mean
        l0_random_results["std"] = l0_std

        # Naive positional heuristic
        naive_alloc = build_naive_heuristic_allocation(n_layers, n_kv, k)
        naive_budget = compute_budget(naive_alloc, n_total)
        assert abs(naive_budget - 0.25) < 1e-9, f"Naive budget {naive_budget} != 0.25"
        naive_ppl = eval_allocation(
            model, tokenizer, naive_alloc,
            f"Naive positional heuristic (budget={naive_budget:.4f})"
        )

        all_results[model_name] = {
            "budget": 0.25,
            "k": k,
            "n_total_heads": n_total,
            "baseline_bf16_ppl": baseline_ppl,
            "uniform_4bit_ppl": uniform_ppl,
            "mckp_ppl": cfg["mckp_ppl"],
            "l0_random": l0_random_results,
            "naive_heuristic_ppl": naive_ppl,
        }

        del model
        torch.cuda.empty_cache()

        print(f"\n--- {model_name} Summary ---")
        print(f"  Baseline bf16:     {baseline_ppl:.4f}")
        print(f"  Uniform 4-bit:     {uniform_ppl:.4f}")
        print(f"  MCKP optimal:      {cfg['mckp_ppl']:.4f}")
        print(f"  L0-random mean:    {l0_mean:.4f} ± {l0_std:.4f}")
        print(f"  Naive heuristic:   {naive_ppl:.4f}")

    t_total = time.time() - t_start

    output = {
        "experiment": "plan_015_l0_heuristic_corrected",
        "description": "L0 heuristic baselines at exact budget=0.25",
        "models": all_results,
        "total_time_seconds": t_total,
        "device": DEVICE,
        "eval_dtype": "bfloat16",
        "seeds": SEEDS,
    }
    out_path = "/root/ratekv/l0_heuristic_corrected_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved results to {out_path}")
    print(f"Total time: {t_total:.1f}s ({t_total/60:.1f}min)")

    print(f"\n{'='*70}")
    print("FINAL COMPARISON (budget=0.25)")
    print(f"{'='*70}")
    print(f"{'Model':<20} {'BF16':>8} {'Unif4':>8} {'MCKP':>8} {'L0rand':>10} {'Naive':>8}")
    print("-" * 66)
    for name, r in all_results.items():
        print(f"{name:<20} {r['baseline_bf16_ppl']:>8.3f} {r['uniform_4bit_ppl']:>8.3f} "
              f"{r['mckp_ppl']:>8.3f} {r['l0_random']['mean']:>7.3f}±{r['l0_random']['std']:.3f} "
              f"{r['naive_heuristic_ppl']:>8.3f}")


if __name__ == "__main__":
    main()
