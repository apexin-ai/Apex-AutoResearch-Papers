"""Mistral-7B-v0.3 8K long-context PPL eval: BF16 / uniform-4bit / constrained MCKP.

Inputs:
  - mistral_hires_bf16_2bitonly_profiles.json  (hires bf16 2-bit-only profiling)
  - mistral_profiling_results.json             (standard 2/4/8-bit profiles)
Outputs:
  - artifacts/mistral7b_8k_eval_results.json

Key params:
  - seq_len=8192 (8K context window)
  - budget=0.25 (25% memory budget for quantization)
  - max_2bit=2 (at most 2 heads assigned to 2-bit)
  - Profiles merged: hires 2-bit deltas + standard 4-bit/8-bit deltas

Architecture: Mistral-7B-v0.3 — 32 layers, 8 KV heads/layer, GQA 4:1
"""
import argparse
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity


def main():
    parser = argparse.ArgumentParser(description="Mistral-7B-v0.3 8K context PPL eval")
    parser.add_argument("--gpu", type=int, default=0, help="GPU device index (default: 0)")
    args = parser.parse_args()

    device = f"cuda:{args.gpu}"
    model_name = "/root/autodl-tmp/models/Mistral-7B-v0.3"
    hires_2bit_path = "mistral_hires_bf16_2bitonly_profiles.json"
    standard_path = "mistral_profiling_results.json"
    output_path = "artifacts/mistral7b_8k_eval_results.json"
    budget = 0.25
    max_2bit = 2
    seq_len = 8192
    t0 = time.time()

    config = AutoConfig.from_pretrained(model_name)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads
    print(f"Mistral-7B-v0.3: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")
    print(f"8K context eval (stride={seq_len}), device={device}")

    # Load hires bf16 2-bit deltas
    print(f"\nLoading hires 2-bit profiles from {hires_2bit_path}...")
    with open(hires_2bit_path) as f:
        hires_data = json.load(f)
    print(f"Hires: {len(hires_data)} layers, {len(hires_data['0'])} heads/layer")

    # Load standard profiling (has 2, 4, 8 bit deltas)
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
    print(f"Total distortion: {mckp_result['total_distortion']:.6f}")

    # Uniform 4-bit allocation
    uniform_result = uniform_quantization_baseline(profiles, bits=4)

    # Load model
    print(f"\nLoading model in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(device) / 1e9
    print(f"Model loaded. GPU mem: {mem_gb:.1f}GB")

    # BF16 baseline @ 8K
    print(f"\nEvaluating bf16 baseline on WikiText-2 (stride={seq_len})...")
    baseline_ppl = evaluate_perplexity(model, tokenizer, device, stride=seq_len)
    print(f"BF16 8K PPL: {baseline_ppl:.4f}")

    # MCKP @ 8K
    print(f"\nEvaluating constrained MCKP on WikiText-2 (stride={seq_len})...")
    orig_fwds = patch_attention(model, mckp_result["allocation"])
    mckp_ppl = evaluate_perplexity(model, tokenizer, device, stride=seq_len)
    restore_attention(model, orig_fwds)
    print(f"MCKP 8K PPL: {mckp_ppl:.4f}")

    # Uniform 4-bit @ 8K
    print(f"\nEvaluating uniform 4-bit on WikiText-2 (stride={seq_len})...")
    orig_fwds = patch_attention(model, uniform_result["allocation"])
    uniform_ppl = evaluate_perplexity(model, tokenizer, device, stride=seq_len)
    restore_attention(model, orig_fwds)
    print(f"Uniform 4-bit 8K PPL: {uniform_ppl:.4f}")

    delta = uniform_ppl - mckp_ppl
    pct_improvement = delta / (uniform_ppl - baseline_ppl) * 100 if uniform_ppl != baseline_ppl else 0

    # Concentration analysis
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
        "model": "mistralai/Mistral-7B-v0.3",
        "model_name": "Mistral-7B-v0.3",
        "experiment": "8K_context_eval",
        "seq_len": seq_len,
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
        "results_8k": {
            "baseline_ppl": round(baseline_ppl, 4),
            "mckp_ppl": round(mckp_ppl, 4),
            "uniform4bit_ppl": round(uniform_ppl, 4),
            "mckp_improvement_over_uniform": round(delta, 4),
            "mckp_improvement_pct": round(pct_improvement, 2),
        },
        "bit_distribution": bit_counts,
        "heads_2bit": heads_2bit,
        "heads_8bit": heads_8bit,
        "mckp_total_distortion": mckp_result["total_distortion"],
        "mckp_actual_memory_ratio": mckp_result["actual_memory_ratio"],
        "analysis": {
            "top5_concentration": round(top5_concentration, 4),
        },
        "timing": {"total_seconds": round(total_time, 1)},
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 60}")
    print(f"RESULTS — Mistral-7B-v0.3 8K Context Eval")
    print(f"{'=' * 60}")
    print(f"{'Method':<30} {'8K PPL':>10}")
    print("-" * 42)
    print(f"{'Baseline (bf16)':<30} {baseline_ppl:>10.4f}")
    print(f"{'Constrained MCKP (k=2)':<30} {mckp_ppl:>10.4f}")
    print(f"{'Uniform 4-bit':<30} {uniform_ppl:>10.4f}")
    print(f"\nMCKP improvement over uniform: {delta:+.4f} ({pct_improvement:+.1f}%)")
    print(f"Top-5% concentration: {top5_concentration:.4f}")
    print(f"2-bit heads: {heads_2bit}")
    print(f"8-bit heads: {heads_8bit}")
    print(f"Total time: {total_time / 60:.1f}min")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
