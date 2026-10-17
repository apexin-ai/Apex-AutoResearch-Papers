"""Qwen2.5-14B Constrained Pipeline: uniform 4-bit vs constrained vs unconstrained MCKP.
Tests Spike prediction (conc=0.33, t1/t5=24.35): MCKP ≈ uniform.
Uses hires bf16 2bit-only profiling with synthesized 4-bit/8-bit deltas.
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
from solver import (solve_mckp_constrained, solve_mckp,
                    uniform_quantization_baseline, enforce_monotonicity)

RATIO_4BIT = 0.25
RATIO_8BIT = 0.05


def main():
    device = "cuda:0"
    model_name = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-14B"
    profiles_path = "qwen14b_hires_bf16_2bitonly_profiles.json"
    output_path = "artifacts/qwen14b_constrained_pipeline_results.json"
    budget = 0.25
    max_2bit = 8
    t0 = time.time()

    config = AutoConfig.from_pretrained(model_name)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads
    print(f"Qwen2.5-14B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")

    print(f"\nLoading profiles from {profiles_path}...")
    with open(profiles_path) as f:
        raw = json.load(f)
    profiles_raw = raw["profiles"] if "profiles" in raw else raw
    print(f"Loaded: {len(profiles_raw)} layers, {len(profiles_raw['0'])} heads/layer")

    print(f"Synthesizing 4-bit (ratio={RATIO_4BIT}) and 8-bit (ratio={RATIO_8BIT}) deltas...")
    for l_str in profiles_raw:
        for h_str in profiles_raw[l_str]:
            d2 = profiles_raw[l_str][h_str]["quantization"]["2"]
            profiles_raw[l_str][h_str]["quantization"]["4"] = d2 * RATIO_4BIT
            profiles_raw[l_str][h_str]["quantization"]["8"] = d2 * RATIO_8BIT

    profiles = enforce_monotonicity(profiles_raw)

    # Concentration analysis
    all_deltas_2bit = []
    for l_str in sorted(profiles.keys(), key=int):
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            all_deltas_2bit.append(d2)

    sorted_d2 = sorted(all_deltas_2bit, reverse=True)
    n_top1 = max(1, int(len(sorted_d2) * 0.01))
    n_top5 = max(1, int(len(sorted_d2) * 0.05))
    total_sum = sum(all_deltas_2bit)
    top1_sum = sum(sorted_d2[:n_top1])
    top5_sum = sum(sorted_d2[:n_top5])
    top1_conc = top1_sum / total_sum if total_sum > 0 else 0
    top5_conc = top5_sum / total_sum if total_sum > 0 else 0
    t1_t5 = top1_conc / top5_conc if top5_conc > 0 else 0
    print(f"Concentration: top1={top1_conc:.4f}, top5={top5_conc:.4f}, t1/t5={t1_t5:.2f}")

    # Constrained MCKP
    print(f"\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...")
    constrained = solve_mckp_constrained(
        profiles, budget, mode="quant_only",
        max_2bit=max_2bit, l0_exclude_2bit=True)

    c_bits = {}
    for key, (atype, param) in constrained["allocation"].items():
        b = int(param) if atype == "quant" else 16
        c_bits[b] = c_bits.get(b, 0) + 1
    print(f"Constrained bit distribution: {c_bits}")
    print(f"Constrained distortion: {constrained['total_distortion']:.6f}")

    # Unconstrained MCKP
    print(f"\nRunning unconstrained MCKP (budget={budget})...")
    unconstrained = solve_mckp(profiles, budget, mode="quant_only")

    u_bits = {}
    for key, (atype, param) in unconstrained["allocation"].items():
        b = int(param) if atype == "quant" else 16
        u_bits[b] = u_bits.get(b, 0) + 1
    print(f"Unconstrained bit distribution: {u_bits}")
    print(f"Unconstrained distortion: {unconstrained['total_distortion']:.6f}")

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

    # BF16 baseline
    print("\nEvaluating bf16 baseline on WikiText-2...")
    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)
    print(f"BF16 WikiText-2 PPL: {baseline_wt2:.4f}")

    # Uniform 4-bit eval
    print("\nEvaluating uniform 4-bit on WikiText-2...")
    uniform = uniform_quantization_baseline(profiles, bits=4)
    orig_fwds = patch_attention(model, uniform["allocation"])
    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"Uniform 4-bit PPL: {uniform_wt2:.4f}")

    # Constrained MCKP eval
    print(f"\nEvaluating constrained MCKP (k={max_2bit}) on WikiText-2...")
    orig_fwds = patch_attention(model, constrained["allocation"])
    constrained_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"Constrained MCKP PPL: {constrained_wt2:.4f}")

    # Unconstrained MCKP eval
    print("\nEvaluating unconstrained MCKP on WikiText-2...")
    orig_fwds = patch_attention(model, unconstrained["allocation"])
    unconstrained_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"Unconstrained MCKP PPL: {unconstrained_wt2:.4f}")

    delta_c = uniform_wt2 - constrained_wt2
    delta_u = uniform_wt2 - unconstrained_wt2
    pct_c = delta_c / (uniform_wt2 - baseline_wt2) * 100 if uniform_wt2 != baseline_wt2 else 0
    pct_u = delta_u / (uniform_wt2 - baseline_wt2) * 100 if uniform_wt2 != baseline_wt2 else 0

    total_time = time.time() - t0

    spike_threshold = 0.3
    spike_verified = abs(delta_u) < spike_threshold

    results = {
        "model": model_name,
        "model_name": "Qwen2.5-14B",
        "experiment": "constrained_pipeline",
        "hypothesis": "Spike prediction: MCKP ~ uniform (conc=0.33, t1/t5=24.35)",
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "head_dim": config.hidden_size // num_q_heads,
            "hidden_size": config.hidden_size,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
        },
        "profiling": {
            "source": profiles_path,
            "type": "hires_bf16_2bitonly",
            "synthesized_ratios": {"4bit": RATIO_4BIT, "8bit": RATIO_8BIT},
        },
        "concentration": {
            "top1_pct": round(top1_conc, 4),
            "top5_pct": round(top5_conc, 4),
            "t1_t5": round(t1_t5, 2),
        },
        "budget": budget,
        "constraint": {"max_2bit": max_2bit, "l0_exclude_2bit": True},
        "results": {
            "baseline_wikitext2_ppl": round(baseline_wt2, 4),
            "uniform4bit_wikitext2_ppl": round(uniform_wt2, 4),
            "constrained_mckp_wikitext2_ppl": round(constrained_wt2, 4),
            "unconstrained_mckp_wikitext2_ppl": round(unconstrained_wt2, 4),
        },
        "deltas": {
            "constrained_vs_uniform": round(delta_c, 4),
            "constrained_vs_uniform_pct": round(pct_c, 2),
            "unconstrained_vs_uniform": round(delta_u, 4),
            "unconstrained_vs_uniform_pct": round(pct_u, 2),
        },
        "bit_distributions": {
            "constrained": {str(k): v for k, v in c_bits.items()},
            "unconstrained": {str(k): v for k, v in u_bits.items()},
        },
        "spike_prediction": {
            "verified": spike_verified,
            "threshold": spike_threshold,
            "unconstrained_delta": round(delta_u, 4),
        },
        "timing": {"total_seconds": round(total_time, 1)},
    }

    os.makedirs("artifacts", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 70}")
    print("RESULTS - Qwen2.5-14B Constrained Pipeline")
    print(f"{'=' * 70}")
    print(f"\n{'Method':<35} {'PPL':>10} {'Delta vs uniform':>18}")
    print("-" * 65)
    print(f"{'Baseline (bf16)':<35} {baseline_wt2:>10.4f} {'---':>18}")
    print(f"{'Uniform 4-bit':<35} {uniform_wt2:>10.4f} {'(reference)':>18}")
    print(f"{'Constrained MCKP (k=' + str(max_2bit) + ')':<35} {constrained_wt2:>10.4f} {delta_c:>+18.4f}")
    print(f"{'Unconstrained MCKP':<35} {unconstrained_wt2:>10.4f} {delta_u:>+18.4f}")
    print(f"\nConcentration: top1={top1_conc:.4f}, top5={top5_conc:.4f}, t1/t5={t1_t5:.2f}")
    print(f"Spike prediction verified: {spike_verified} (|delta|={abs(delta_u):.4f} vs threshold={spike_threshold})")
    print(f"Bit distributions:")
    print(f"  Constrained:   {c_bits}")
    print(f"  Unconstrained: {u_bits}")
    print(f"Total time: {total_time / 60:.1f}min")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
