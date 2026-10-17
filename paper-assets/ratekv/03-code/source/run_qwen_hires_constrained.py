"""Qwen2.5-7B Constrained MCKP + WikiText-2 Eval using D048 float32 hires profiling data."""
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
    model_name = "Qwen/Qwen2.5-7B"
    profiles_path = "hires_profiles.json"
    output_path = "qwen_hires_constrained_results.json"
    budget = 0.25
    max_2bit = 8
    t0 = time.time()

    config = AutoConfig.from_pretrained(model_name)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads
    print(f"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")

    # Load D048 float32 hires profiling data
    print(f"\nLoading profiles from {profiles_path}...")
    with open(profiles_path) as f:
        raw = json.load(f)
    profiles_raw = raw["profiles"] if "profiles" in raw else raw
    print(f"Loaded: {len(profiles_raw)} layers, {len(profiles_raw['0'])} heads/layer")

    profiles = enforce_monotonicity(profiles_raw)

    # Constrained MCKP
    print(f"\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...")
    mckp_result = solve_mckp_constrained(
        profiles, budget, mode="quant_only",
        max_2bit=max_2bit, l0_exclude_2bit=True)

    bit_counts = {}
    for key, (atype, param) in mckp_result["allocation"].items():
        b = int(param) if atype == "quant" else 16
        bit_counts[b] = bit_counts.get(b, 0) + 1
    print(f"Bit distribution: {bit_counts}")
    print(f"Total distortion: {mckp_result['total_distortion']:.6f}")
    print(f"Memory ratio: {mckp_result['actual_memory_ratio']:.4f}")

    # Load model for eval
    print(f"\nLoading model in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(device) / 1e9
    print(f"Model loaded. GPU mem: {mem_gb:.1f}GB")

    # BF16 baseline WikiText-2
    print("\nEvaluating bf16 baseline on WikiText-2...")
    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)
    print(f"BF16 WikiText-2 PPL: {baseline_wt2:.4f}")

    # MCKP eval
    print("\nEvaluating constrained MCKP allocation on WikiText-2...")
    orig_fwds = patch_attention(model, mckp_result["allocation"])
    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"MCKP PPL: {mckp_wt2:.4f}")

    # Uniform 4-bit eval
    print("\nEvaluating uniform 4-bit on WikiText-2...")
    uniform_result = uniform_quantization_baseline(profiles, bits=4)
    orig_fwds = patch_attention(model, uniform_result["allocation"])
    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"Uniform 4-bit PPL: {uniform_wt2:.4f}")

    delta = uniform_wt2 - mckp_wt2
    pct_improvement = delta / (uniform_wt2 - baseline_wt2) * 100 if uniform_wt2 != baseline_wt2 else 0
    print(f"\nMCKP improvement over uniform: {delta:+.4f} ({pct_improvement:+.1f}%)")

    # Concentration analysis
    all_deltas_2bit = []
    for l_str in sorted(profiles.keys(), key=int):
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            all_deltas_2bit.append(d2)

    sorted_d2 = sorted(all_deltas_2bit, reverse=True)
    n_top5 = max(1, int(len(sorted_d2) * 0.05))
    total_sum = sum(all_deltas_2bit)
    top5_sum = sum(sorted_d2[:n_top5])
    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0

    total_time = time.time() - t0

    results = {
        "model": model_name,
        "model_name": "Qwen2.5-7B",
        "precision": "float32_hires_profiling",
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "head_dim": config.hidden_size // num_q_heads,
            "hidden_size": config.hidden_size,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
        },
        "profiling_source": "qwen_float32_profiles.json (D048 float32 hires)",
        "constraint": {"max_2bit": max_2bit, "budget": budget, "l0_exclude_2bit": True},
        "baseline_wikitext2_ppl": round(baseline_wt2, 4),
        "mckp_wikitext2_ppl": round(mckp_wt2, 4),
        "uniform4bit_wikitext2_ppl": round(uniform_wt2, 4),
        "mckp_improvement_over_uniform": round(delta, 4),
        "mckp_improvement_pct": round(pct_improvement, 2),
        "bit_distribution": bit_counts,
        "mckp_total_distortion": mckp_result["total_distortion"],
        "mckp_actual_memory_ratio": mckp_result["actual_memory_ratio"],
        "allocation": {k: list(v) for k, v in mckp_result["allocation"].items()},
        "analysis": {
            "top5_concentration": round(top5_concentration, 4),
        },
        "timing": {"total_seconds": round(total_time, 1)},
    }

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 60}")
    print("RESULTS — Qwen2.5-7B (float32 hires constrained MCKP)")
    print(f"{'=' * 60}")
    print(f"{'Method':<30} {'PPL':>10} {'Delta vs uniform':>18}")
    print("-" * 60)
    print(f"{'Baseline (bf16)':<30} {baseline_wt2:>10.4f} {'---':>18}")
    print(f"{'Constrained MCKP (k=8)':<30} {mckp_wt2:>10.4f} {delta:>+18.4f}")
    print(f"{'Uniform 4-bit':<30} {uniform_wt2:>10.4f} {'---':>18}")
    print(f"\nTop-5% concentration: {top5_concentration:.4f}")
    print(f"Bit distribution: {bit_counts}")
    print(f"Total time: {total_time / 60:.1f}min")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
