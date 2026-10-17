"""Mistral-7B-v0.3: re-evaluate uniform 4-bit PPL only (fix for bits=0.25 bug).
Reads existing results, reruns uniform 4-bit eval, updates the JSON.
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
from solver import uniform_quantization_baseline, enforce_monotonicity


def main():
    device = "cuda:0"
    model_name = "/root/autodl-tmp/models/Mistral-7B-v0.3"
    hires_2bit_path = "mistral_hires_bf16_2bitonly_profiles.json"
    standard_path = "mistral_profiling_results.json"
    output_path = "artifacts/mistral_hires_constrained_results.json"
    t0 = time.time()

    # Load and merge profiles (same as original)
    with open(hires_2bit_path) as f:
        hires_data = json.load(f)
    with open(standard_path) as f:
        std_raw = json.load(f)
    std_data = std_raw["profiles"] if "profiles" in std_raw else std_raw

    merged = {}
    for l_str in sorted(hires_data.keys(), key=int):
        merged[l_str] = {}
        for h_str in sorted(hires_data[l_str].keys(), key=int):
            d2_hires = hires_data[l_str][h_str]["quantization"]["2"]
            d4_std = std_data[l_str][h_str]["quantization"]["4"]
            d8_std = std_data[l_str][h_str]["quantization"]["8"]
            merged[l_str][h_str] = {"quantization": {"2": d2_hires, "4": d4_std, "8": d8_std}}

    profiles = enforce_monotonicity(merged)

    # Load model
    print(f"Loading Mistral-7B-v0.3 in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()
    print(f"Model loaded. GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")

    # Uniform 4-bit eval (THE FIX: bits=4, not budget=0.25)
    print("\nEvaluating uniform 4-bit on WikiText-2...")
    uniform_result = uniform_quantization_baseline(profiles, bits=4)
    orig_fwds = patch_attention(model, uniform_result["allocation"])
    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"Uniform 4-bit PPL: {uniform_wt2:.4f}")

    # Update existing results JSON
    with open(output_path) as f:
        results = json.load(f)

    old_uniform = results["uniform4bit_wikitext2_ppl"]
    baseline = results["baseline_wikitext2_ppl"]
    mckp_ppl = results["mckp_wikitext2_ppl"]

    results["uniform4bit_wikitext2_ppl"] = round(uniform_wt2, 4)
    delta = uniform_wt2 - mckp_ppl
    pct = delta / (uniform_wt2 - baseline) * 100 if uniform_wt2 != baseline else 0
    results["mckp_improvement_over_uniform"] = round(delta, 4)
    results["mckp_improvement_pct"] = round(pct, 2)
    results["verdict"] = "PASS" if delta >= 0.5 else "MARGINAL" if delta >= 0.1 else "FAIL"
    results["uniform_fix_note"] = f"Re-evaluated: old={old_uniform} (bug: bits=0.25), new={round(uniform_wt2, 4)}"

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    total_time = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f"UNIFORM 4-BIT FIX RESULTS")
    print(f"{'=' * 60}")
    print(f"Old uniform PPL (buggy): {old_uniform}")
    print(f"New uniform PPL (fixed): {uniform_wt2:.4f}")
    print(f"Baseline PPL: {baseline}")
    print(f"MCKP PPL: {mckp_ppl}")
    print(f"MCKP improvement over uniform: {delta:+.4f} ({pct:+.1f}%)")
    print(f"Verdict: {results['verdict']}")
    print(f"Time: {total_time / 60:.1f}min")
    print(f"Updated {output_path}")


if __name__ == "__main__":
    main()
