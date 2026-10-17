# Qwen2.5-7B bf16 consistency re-eval
# Purpose: Re-evaluate baseline and uniform 4-bit PPL under bf16 dtype
# to resolve fp16/bf16 inconsistency flagged by reviewer.
# Prior fp16 numbers: baseline=9.81, uniform_4bit=15.45
# Expected bf16 baseline: ~8.82 (from exp_e_hires_profile)

import json
import os
import sys
import time

os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

sys.path.insert(0, "/root/ratekv")

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity

MODEL = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B"
DEVICE = "cuda:0"
STRIDE = 512
OUTPUT_FILE = "/root/ratekv/bf16_reeval_results.json"

FP16_BASELINE = 9.81
FP16_UNIFORM_4BIT = 15.45

def main():
    print(f"=== Qwen2.5-7B bf16 Re-Eval ===")
    print(f"Device: {DEVICE}, Stride: {STRIDE}")
    print(f"Model: {MODEL}")
    t0 = time.time()

    print("\nLoading model in bf16...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL,
        torch_dtype=torch.bfloat16,
        attn_implementation="eager",
        device_map=DEVICE,
        trust_remote_code=True,
    )
    model.eval()

    param_dtype = next(model.parameters()).dtype
    print(f"Model dtype: {param_dtype}")
    assert param_dtype == torch.bfloat16, f"Expected bfloat16, got {param_dtype}"

    # --- Task 1: Baseline bf16 PPL (no quantization) ---
    print("\n=== [1/2] Baseline bf16 PPL (no quantization) ===")
    t1 = time.time()
    baseline_ppl = evaluate_perplexity(model, tokenizer, DEVICE, stride=STRIDE)
    t1_elapsed = time.time() - t1
    print(f">>> baseline_ppl_bf16 = {baseline_ppl:.4f}  (took {t1_elapsed:.1f}s)")
    print(f"    fp16 was: {FP16_BASELINE}, delta = {abs(baseline_ppl - FP16_BASELINE):.4f}")

    # --- Task 2: Uniform 4-bit bf16 PPL ---
    # Qwen2.5-7B: 28 layers × 4 KV heads = 112 heads, all set to 4-bit
    uniform_alloc = {}
    for layer in range(28):
        for head in range(4):
            uniform_alloc[f"{layer},{head}"] = ("quant", 4)

    print(f"\n=== [2/2] Uniform 4-bit bf16 PPL (all {len(uniform_alloc)} heads @ 4-bit) ===")
    t2 = time.time()
    orig = patch_attention(model, uniform_alloc)
    uniform_ppl = evaluate_perplexity(model, tokenizer, DEVICE, stride=STRIDE)
    restore_attention(model, orig)
    t2_elapsed = time.time() - t2
    print(f">>> uniform_4bit_ppl_bf16 = {uniform_ppl:.4f}  (took {t2_elapsed:.1f}s)")
    print(f"    fp16 was: {FP16_UNIFORM_4BIT}, delta = {abs(uniform_ppl - FP16_UNIFORM_4BIT):.4f}")

    total_elapsed = time.time() - t0

    # --- Summary ---
    results = {
        "experiment": "qwen_bf16_reeval",
        "model": "Qwen2.5-7B",
        "dtype": "bfloat16",
        "stride": STRIDE,
        "device": DEVICE,
        "baseline_ppl_bf16": round(baseline_ppl, 4),
        "baseline_ppl_fp16": FP16_BASELINE,
        "baseline_delta": round(abs(baseline_ppl - FP16_BASELINE), 4),
        "uniform_4bit_ppl_bf16": round(uniform_ppl, 4),
        "uniform_4bit_ppl_fp16": FP16_UNIFORM_4BIT,
        "uniform_4bit_delta": round(abs(uniform_ppl - FP16_UNIFORM_4BIT), 4),
        "num_heads_quantized": len(uniform_alloc),
        "budget": 0.25,
        "elapsed_seconds": round(total_elapsed, 1),
    }

    print(f"\n{'='*50}")
    print(f"RESULTS SUMMARY")
    print(f"{'='*50}")
    print(f"{'Metric':<30} {'bf16':>10} {'fp16':>10} {'delta':>10}")
    print(f"{'-'*60}")
    print(f"{'Baseline PPL':<30} {baseline_ppl:>10.4f} {FP16_BASELINE:>10.4f} {abs(baseline_ppl - FP16_BASELINE):>10.4f}")
    print(f"{'Uniform 4-bit PPL':<30} {uniform_ppl:>10.4f} {FP16_UNIFORM_4BIT:>10.4f} {abs(uniform_ppl - FP16_UNIFORM_4BIT):>10.4f}")
    print(f"{'='*50}")
    print(f"Total time: {total_elapsed:.1f}s")

    threshold = 0.3
    need_rerun = any(d > threshold for d in [results["baseline_delta"], results["uniform_4bit_delta"]])
    results["compounding_sweep_rerun_needed"] = need_rerun
    print(f"\nCompounding sweep bf16 rerun needed (threshold={threshold}): {need_rerun}")

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
