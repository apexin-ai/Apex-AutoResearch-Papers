"""Mistral-7B-v0.3 Constrained MCKP + WikiText-2 eval using merged hires profiling data.
Merges hires bf16 2-bit deltas (64seq x 2048tok) with standard 4-bit/8-bit deltas.

Inputs:
  - mistral_hires_bf16_2bitonly_profiles.json  (hires bf16 2-bit-only profiling)
  - mistral_profiling_results.json             (standard 2/4/8-bit profiles)
Outputs:
  - artifacts/mistral_hires_constrained_results.json

Dependencies: transformers, torch, eval_ppl, solver
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity


def main():
    device = "cuda:0"
    model_name = "/root/autodl-tmp/models/Mistral-7B-v0.3"
    hires_2bit_path = "mistral_hires_bf16_2bitonly_profiles.json"
    standard_path = "mistral_profiling_results.json"
    output_path = "artifacts/mistral_hires_constrained_results.json"
    budget = 0.25
    max_2bit = 2
    t0 = time.time()

    config = AutoConfig.from_pretrained(model_name)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads
    print(f"Mistral-7B-v0.3: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")

    # Load hires bf16 2-bit deltas
    print(f"\nLoading hires 2-bit profiles from {hires_2bit_path}...")
    with open(hires_2bit_path) as f:
        hires_data = json.load(f)
    print(f"Hires: {len(hires_data)} layers, {len(hires_data['0'])} heads/layer")

    # Load standard profiling (has 2, 4, 8 bit deltas; uses 'profiles' wrapper)
    print(f"Loading standard profiles from {standard_path}...")
    with open(standard_path) as f:
        std_raw = json.load(f)
    std_data = std_raw["profiles"] if "profiles" in std_raw else std_raw
    print(f"Standard: {len(std_data)} layers, {len(std_data['0'])} heads/layer")

    # Merge: hires 2-bit + standard 4-bit and 8-bit
    print("\nMerging profiles (hires 2-bit + standard 4-bit/8-bit)...")
    merged = {}
    for l_str in sorted(hires_data.keys(), key=int):
        merged[l_str] = {}
        for h_str in sorted(hires_data[l_str].keys(), key=int):
            d2_hires = hires_data[l_str][h_str]["quantization"]["2"]
            d4_std = std_data[l_str][h_str]["quantization"]["4"]
            d8_std = std_data[l_str][h_str]["quantization"]["8"]
            merged[l_str][h_str] = {"quantization": {"2": d2_hires, "4": d4_std, "8": d8_std}}

    print(f"  L2H5 merged: 2bit={merged['2']['5']['quantization']['2']:.4f} (hires), "
          f"4bit={merged['2']['5']['quantization']['4']:.6f}, "
          f"8bit={merged['2']['5']['quantization']['8']:.6f} (standard)")
    print(f"  L2H5 standard 2bit was: {std_data['2']['5']['quantization']['2']:.4f}")

    profiles = enforce_monotonicity(merged)

    # Constrained MCKP
    print(f"\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...")
    mckp_result = solve_mckp_constrained(
        profiles, budget, mode="quant_only",
        max_2bit=max_2bit, l0_exclude_2bit=True)

    bit_counts = {}
    heads_2bit = []
    heads_8bit = []
    for key, (atype, param) in mckp_result["allocation"].items():
        b = int(param) if atype == "quant" else 16
        bit_counts[b] = bit_counts.get(b, 0) + 1
        if b == 2:
            heads_2bit.append(key)
        elif b == 8:
            heads_8bit.append(key)
    print(f"Bit distribution: {bit_counts}")
    print(f"2-bit heads: {heads_2bit}")
    print(f"8-bit heads: {heads_8bit}")
    print(f"Total distortion: {mckp_result['total_distortion']:.6f}")
    print(f"Memory ratio: {mckp_result['actual_memory_ratio']:.4f}")

    # Load model
    print(f"\nLoading model in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()

    # BF16 baseline WikiText-2
    print("\nEvaluating BF16 baseline on WikiText-2...")
    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)
    print(f"BF16 baseline PPL: {baseline_wt2:.4f}")

    # MCKP WikiText-2
    print("\nEvaluating constrained MCKP on WikiText-2...")
    orig_fwds = patch_attention(model, mckp_result["allocation"])
    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"MCKP (k={max_2bit}) PPL: {mckp_wt2:.4f}")

    # Uniform 4-bit WikiText-2
    print("\nEvaluating uniform 4-bit on WikiText-2...")
    uniform_result = uniform_quantization_baseline(profiles, bits=4)
    orig_fwds = patch_attention(model, uniform_result["allocation"])
    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"Uniform 4-bit PPL: {uniform_wt2:.4f}")

    delta = uniform_wt2 - mckp_wt2
    pct_improvement = delta / (uniform_wt2 - baseline_wt2) * 100 if uniform_wt2 != baseline_wt2 else 0
    print(f"\nMCKP improvement over uniform: {delta:+.4f} ({pct_improvement:+.1f}%)")

    # Concentration analysis (from hires 2-bit deltas)
    all_deltas_2bit = []
    for l_str in sorted(merged.keys(), key=int):
        for h_str in sorted(merged[l_str].keys(), key=int):
            d2 = merged[l_str][h_str]["quantization"]["2"]
            all_deltas_2bit.append(d2)

    sorted_d2 = sorted(all_deltas_2bit, reverse=True)
    n_top5 = max(1, int(len(sorted_d2) * 0.05))
    total_sum = sum(all_deltas_2bit)
    top5_sum = sum(sorted_d2[:n_top5])
    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0

    total_time = time.time() - t0

    results = {
        "model": model_name,
        "model_name": "Mistral-7B-v0.3",
        "precision": "merged_hires_bf16_2bit_plus_standard_4bit_8bit",
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "head_dim": config.hidden_size // num_q_heads,
            "hidden_size": config.hidden_size,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
        },
        "profiling_sources": {
            "2bit": f"{hires_2bit_path} (bf16, 64seq x 2048tok)",
            "4bit_8bit": f"{standard_path} (standard)",
        },
        "constraint": {"max_2bit": max_2bit, "budget": budget, "l0_exclude_2bit": True},
        "baseline_wikitext2_ppl": round(baseline_wt2, 4),
        "mckp_wikitext2_ppl": round(mckp_wt2, 4),
        "uniform4bit_wikitext2_ppl": round(uniform_wt2, 4),
        "mckp_improvement_over_uniform": round(delta, 4),
        "mckp_improvement_pct": round(pct_improvement, 2),
        "verdict": "PASS" if delta >= 0.5 else "MARGINAL" if delta >= 0.1 else "FAIL",
        "bit_distribution": bit_counts,
        "heads_2bit": heads_2bit,
        "heads_8bit": heads_8bit,
        "mckp_total_distortion": mckp_result["total_distortion"],
        "mckp_actual_memory_ratio": mckp_result["actual_memory_ratio"],
        "allocation": {k: list(v) for k, v in mckp_result["allocation"].items()},
        "analysis": {
            "top5_concentration_hires": round(top5_concentration, 4),
        },
        "timing": {"total_seconds": round(total_time, 1)},
    }

    os.makedirs("artifacts", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 60}")
    print("RESULTS — Mistral-7B-v0.3 (hires constrained MCKP)")
    print(f"{'=' * 60}")
    print(f"\n{'Method':<35} {'PPL':>10} {'Delta vs uniform':>18}")
    print("-" * 65)
    print(f"{'Baseline (bf16)':<35} {baseline_wt2:>10.4f} {'---':>18}")
    print(f"{'Hires MCKP (k=2)':<35} {mckp_wt2:>10.4f} {delta:>+18.4f}")
    print(f"{'Uniform 4-bit':<35} {uniform_wt2:>10.4f} {'---':>18}")
    print(f"\nConcentration: hires={top5_concentration:.4f}")
    print(f"Bit distribution: {bit_counts}")
    print(f"2-bit heads: {heads_2bit}")
    print(f"8-bit heads: {heads_8bit}")
    print(f"Verdict: {results['verdict']}")
    print(f"Total time: {total_time / 60:.1f}min")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
