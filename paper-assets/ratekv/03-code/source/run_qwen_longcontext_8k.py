"""Qwen2.5-7B 8K long-context PPL eval: BF16 / uniform-4bit / constrained MCKP(k=8).

Input:  hires_profiles.json (2/4/8-bit distortion profiles)
Output: artifacts/qwen_longcontext_8k_results.json
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import argparse
import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity


def main():
    parser = argparse.ArgumentParser(description="Qwen2.5-7B 8K long-context eval")
    parser.add_argument("--gpu", type=str, default="cuda:0")
    args = parser.parse_args()

    device = args.gpu
    model_name = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B"
    profiles_path = "hires_profiles.json"
    output_path = "artifacts/qwen_longcontext_8k_results.json"
    budget = 0.25
    max_2bit = 8
    seq_len = 8192
    t0 = time.time()

    config = AutoConfig.from_pretrained(model_name)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads
    print(f"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")
    print(f"8K long-context eval (stride={seq_len})")

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
    print(f"\nEvaluating constrained MCKP (k={max_2bit}) on WikiText-2 (stride={seq_len})...")
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
        "model": "Qwen/Qwen2.5-7B",
        "model_name": "Qwen2.5-7B",
        "experiment": "8K_longcontext_eval",
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
        "profiling_source": f"{profiles_path} (reused from 2K profiling)",
        "constraint": {"max_2bit": max_2bit, "budget": budget, "l0_exclude_2bit": True},
        "results_8k": {
            "baseline_ppl": round(baseline_ppl, 4),
            "mckp_ppl": round(mckp_ppl, 4),
            "uniform4bit_ppl": round(uniform_ppl, 4),
            "mckp_improvement_over_uniform": round(delta, 4),
            "mckp_improvement_pct": round(pct_improvement, 2),
        },
        "results_2k_reference": {
            "baseline_ppl": 9.8106,
            "mckp_ppl": 10.8909,
            "uniform4bit_ppl": 15.4484,
            "mckp_improvement_over_uniform": 4.5575,
            "mckp_improvement_pct": 80.84,
        },
        "bit_distribution": bit_counts,
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
    print("RESULTS — Qwen2.5-7B 8K Long-Context Eval")
    print(f"{'=' * 60}")
    print(f"{'Method':<30} {'8K PPL':>10} {'2K PPL':>10}")
    print("-" * 60)
    print(f"{'Baseline (bf16)':<30} {baseline_ppl:>10.4f} {'9.8106':>10}")
    print(f"{'Constrained MCKP (k=8)':<30} {mckp_ppl:>10.4f} {'10.8909':>10}")
    print(f"{'Uniform 4-bit':<30} {uniform_ppl:>10.4f} {'15.4484':>10}")
    print(f"\nMCKP improvement over uniform: {delta:+.4f} ({pct_improvement:+.1f}%)")
    print(f"Top-5% concentration: {top5_concentration:.4f}")
    print(f"Total time: {total_time / 60:.1f}min")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
