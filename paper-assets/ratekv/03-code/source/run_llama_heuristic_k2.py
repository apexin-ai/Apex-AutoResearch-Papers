"""D041: Llama-3.1-8B heuristic baselines with k=2 (matching MCKP max_2bit=2).

Budget matching: k=2 with all-L0@8-bit gives budget=0.2568 != 0.25.
Adjustment: 1 L0 head (0,0) @8-bit, 7 L0 heads @4-bit -> exact budget=0.25.
Derivation: 8*1 + 2*2 + 4*253 = 1024, budget = 1024/4096 = 0.25.
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
MODEL_PATH = "/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B/"
NUM_LAYERS = 32
NUM_KV_HEADS = 8
N_TOTAL = NUM_LAYERS * NUM_KV_HEADS  # 256
K = 2
N_8BIT_L0 = 1  # budget-matched: only head (0,0) at 8-bit

SEEDS = [0, 1, 2, 3, 4]
MCKP_PPL_REF = 8.4498


def compute_budget(alloc):
    total_bits = sum(bits for _, bits in alloc.values())
    return total_bits / (N_TOTAL * 16)


def build_l0_random_allocation(seed):
    rng = random.Random(seed)
    non_l0_heads = [(l, h) for l in range(1, NUM_LAYERS) for h in range(NUM_KV_HEADS)]
    chosen_2bit = set(rng.sample(non_l0_heads, K))

    alloc = {}
    for l in range(NUM_LAYERS):
        for h in range(NUM_KV_HEADS):
            if l == 0 and h < N_8BIT_L0:
                alloc[f"{l},{h}"] = ["quant", 8]
            elif (l, h) in chosen_2bit:
                alloc[f"{l},{h}"] = ["quant", 2]
            else:
                alloc[f"{l},{h}"] = ["quant", 4]
    return alloc, chosen_2bit


def build_naive_positional_allocation():
    twobit_set = set()
    remaining = K
    for l in range(NUM_LAYERS - 1, 0, -1):
        if remaining <= 0:
            break
        assign = min(NUM_KV_HEADS, remaining)
        for h in range(assign):
            twobit_set.add((l, h))
        remaining -= assign

    alloc = {}
    for l in range(NUM_LAYERS):
        for h in range(NUM_KV_HEADS):
            if l == 0 and h < N_8BIT_L0:
                alloc[f"{l},{h}"] = ["quant", 8]
            elif (l, h) in twobit_set:
                alloc[f"{l},{h}"] = ["quant", 2]
            else:
                alloc[f"{l},{h}"] = ["quant", 4]
    return alloc, twobit_set


def eval_allocation(model, tokenizer, alloc, label):
    print(f"\nEval: {label}...")
    orig = patch_attention(model, alloc)
    ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f">>> {label} PPL: {ppl:.4f}")
    return ppl


def main():
    t_start = time.time()

    test_alloc, _ = build_l0_random_allocation(0)
    budget = compute_budget(test_alloc)
    print(f"Budget verification: {budget:.6f} (target 0.25)")
    assert abs(budget - 0.25) < 1e-9, f"Budget mismatch: {budget}"

    print(f"Loading {MODEL_PATH}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(DEVICE)
    model.eval()

    results = {
        "k": K,
        "n_8bit_l0": N_8BIT_L0,
        "budget": 0.25,
        "n_total_heads": N_TOTAL,
    }

    print("\nEval: baseline (bf16, no quant)...")
    baseline_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    print(f">>> Baseline PPL: {baseline_ppl:.4f}")
    results["baseline_bf16_ppl"] = baseline_ppl

    uniform_alloc = {f"{l},{h}": ["quant", 4]
                     for l in range(NUM_LAYERS) for h in range(NUM_KV_HEADS)}
    uniform_ppl = eval_allocation(model, tokenizer, uniform_alloc, "Uniform 4-bit")
    results["uniform_4bit_ppl"] = uniform_ppl

    l0_random = {}
    for seed in SEEDS:
        alloc, chosen = build_l0_random_allocation(seed)
        ppl = eval_allocation(model, tokenizer, alloc, f"L0-random seed={seed}")
        l0_random[f"seed_{seed}"] = ppl
        print(f"  2-bit heads: {sorted(chosen)}")

    vals = [l0_random[f"seed_{s}"] for s in SEEDS]
    l0_mean = sum(vals) / len(vals)
    l0_std = math.sqrt(sum((v - l0_mean) ** 2 for v in vals) / len(vals))
    l0_median = sorted(vals)[len(vals) // 2]
    l0_random["mean"] = l0_mean
    l0_random["std"] = l0_std
    l0_random["median"] = l0_median
    results["l0_random"] = l0_random

    naive_alloc, naive_2bit = build_naive_positional_allocation()
    naive_ppl = eval_allocation(model, tokenizer, naive_alloc,
                                "Naive positional (deepest 2 heads @2-bit)")
    results["naive_heuristic_ppl"] = naive_ppl
    results["naive_2bit_heads"] = [list(x) for x in sorted(naive_2bit)]

    results["mckp_ppl_ref"] = MCKP_PPL_REF

    del model
    torch.cuda.empty_cache()

    print(f"\n{'=' * 60}")
    print(f"Llama-3.1-8B k=2 Heuristic Results (budget=0.25)")
    print(f"{'=' * 60}")
    print(f"  Baseline bf16:     {baseline_ppl:.4f}")
    print(f"  Uniform 4-bit:     {uniform_ppl:.4f}")
    print(f"  MCKP (k=2):        {MCKP_PPL_REF:.4f}")
    print(f"  L0-random mean:    {l0_mean:.4f} +/- {l0_std:.4f}")
    print(f"  L0-random median:  {l0_median:.4f}")
    print(f"  Naive positional:  {naive_ppl:.4f}")
    gap = l0_mean - MCKP_PPL_REF
    print(f"  MCKP vs L0-random: {gap:.4f}")
    print(f"  MCKP vs Naive:     {naive_ppl - MCKP_PPL_REF:.4f}")
    if abs(gap) < 0.1:
        print(f"  *** WARNING: L0-random gap < 0.1 PPL — MCKP advantage may be small at k=2 ***")

    t_total = time.time() - t_start
    output = {
        "experiment": "d041_llama_heuristic_k2",
        "description": "Llama-3.1-8B heuristic baselines with k=2 at budget=0.25",
        "note": "Budget matched: 1 L0 head (0,0) @8-bit, 7 L0 heads @4-bit",
        "model": "Llama-3.1-8B",
        "results": results,
        "total_time_seconds": t_total,
        "device": DEVICE,
        "eval_dtype": "bfloat16",
        "seeds": SEEDS,
    }
    out_path = "/root/ratekv/d041_llama_heuristic_k2_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")
    print(f"Total time: {t_total:.1f}s ({t_total/60:.1f}min)")


if __name__ == "__main__":
    main()
