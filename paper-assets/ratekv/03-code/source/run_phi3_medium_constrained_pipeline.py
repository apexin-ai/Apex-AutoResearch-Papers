"""Phi-3-medium-14B constrained MCKP + WikiText-2 eval pipeline.

Architecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.
Profiling source: artifacts/phi3_medium_profiles_hires.json (2-bit only).
4-bit/8-bit deltas synthesized from 2-bit via fixed ratios.
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import argparse
import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
from solver import (solve_mckp_constrained, solve_mckp,
                    solve_greedy_ratequant, uniform_quantization_baseline)

MODEL_PATH = "/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct"
PROFILE_PATH = "artifacts/phi3_medium_profiles_hires.json"
OUTPUT_PATH = "artifacts/phi3_medium_constrained_results.json"
BUDGET = 0.25
MAX_2BIT = 8
RATIO_4BIT = 0.25
RATIO_8BIT = 0.05


def synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads):
    """Synthesize 4-bit and 8-bit deltas from 2-bit-only profiling data."""
    profiles = {}
    for li in range(num_layers):
        l_str = str(li)
        layer_data = raw_profiles[l_str]
        profiles[l_str] = {}
        for hi in range(num_kv_heads):
            h_str = str(hi)
            d2 = layer_data[h_str]["quantization"]["2"]
            profiles[l_str][h_str] = {
                "quantization": {
                    "2": d2,
                    "4": d2 * RATIO_4BIT,
                    "8": d2 * RATIO_8BIT,
                }
            }
    return profiles


def main():
    parser = argparse.ArgumentParser(description="Phi-3-medium-14B constrained MCKP pipeline")
    parser.add_argument("--gpu", type=str, default="cuda:1")
    args = parser.parse_args()

    device = args.gpu
    t0 = time.time()

    config = AutoConfig.from_pretrained(MODEL_PATH, trust_remote_code=False)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads
    print(f"Phi-3-medium-14B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")

    # Load 2-bit-only profiles and synthesize multi-bit
    print(f"\nLoading profiles from {PROFILE_PATH}...")
    with open(PROFILE_PATH) as f:
        raw = json.load(f)
    raw_profiles = raw["profiles"] if "profiles" in raw else raw
    profiles = synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads)
    print(f"Synthesized multi-bit profiles: {num_layers} layers x {num_kv_heads} heads")

    # Concentration analysis
    all_deltas_2bit = []
    for l_str in sorted(profiles.keys(), key=int):
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"]["2"]
            all_deltas_2bit.append(d2)
    sorted_d2 = sorted(all_deltas_2bit, reverse=True)
    n_top5 = max(1, int(len(sorted_d2) * 0.05))
    total_sum = sum(all_deltas_2bit)
    top5_sum = sum(sorted_d2[:n_top5])
    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0
    print(f"Top-5% concentration: {top5_concentration:.4f} (Spread pattern)")

    # --- Solve allocations ---
    print(f"\n--- Solving allocations (budget={BUDGET}, max_2bit={MAX_2BIT}) ---")

    constrained = solve_mckp_constrained(
        profiles, BUDGET, mode="quant_only",
        max_2bit=MAX_2BIT, l0_exclude_2bit=True)

    unconstrained = solve_mckp(profiles, BUDGET, mode="quant_only")

    greedy = solve_greedy_ratequant(profiles, budget=BUDGET, mode="quant_only")

    uniform = uniform_quantization_baseline(profiles, bits=4)

    for name, sol in [("Constrained MCKP", constrained),
                      ("Unconstrained MCKP", unconstrained),
                      ("Greedy", greedy),
                      ("Uniform-4bit", uniform)]:
        bits_dist = {}
        for k, v in sol["allocation"].items():
            b = int(v[1])
            bits_dist[b] = bits_dist.get(b, 0) + 1
        print(f"  {name}: mem={sol['actual_memory_ratio']:.4f}, "
              f"dist={sol['total_distortion']:.6f}, bits={bits_dist}")

    # --- Load model ---
    print(f"\nLoading model in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=False)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16,
        attn_implementation="eager", trust_remote_code=False
    )
    model = model.to(device)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(device) / 1e9
    print(f"Model loaded. GPU mem: {mem_gb:.1f}GB")

    # --- Eval: BF16 baseline ---
    print("\n[1/5] BF16 baseline PPL...")
    ppl_bf16 = evaluate_perplexity(model, tokenizer, device)
    print(f"  BF16 PPL = {ppl_bf16:.4f}")

    # --- Eval: Uniform 4-bit ---
    print("\n[2/5] Uniform 4-bit PPL...")
    orig_fwds = patch_attention(model, uniform["allocation"])
    ppl_uniform = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"  Uniform-4bit PPL = {ppl_uniform:.4f}")

    # --- Eval: Constrained MCKP ---
    print("\n[3/5] Constrained MCKP PPL...")
    orig_fwds = patch_attention(model, constrained["allocation"])
    ppl_constrained = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"  Constrained PPL = {ppl_constrained:.4f}")

    # --- Eval: Unconstrained MCKP ---
    print("\n[4/5] Unconstrained MCKP PPL...")
    orig_fwds = patch_attention(model, unconstrained["allocation"])
    ppl_unconstrained = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"  Unconstrained PPL = {ppl_unconstrained:.4f}")

    # --- Eval: Greedy ---
    print("\n[5/5] Greedy PPL...")
    orig_fwds = patch_attention(model, greedy["allocation"])
    ppl_greedy = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"  Greedy PPL = {ppl_greedy:.4f}")

    # --- Save results ---
    elapsed = time.time() - t0

    results = {
        "model": MODEL_PATH,
        "model_name": "Phi-3-medium-14B",
        "precision": "bfloat16",
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "head_dim": config.hidden_size // num_q_heads,
            "hidden_size": config.hidden_size,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
        },
        "profiling_source": PROFILE_PATH,
        "synthesis": {"ratio_4bit": RATIO_4BIT, "ratio_8bit": RATIO_8BIT},
        "constraint": {"budget": BUDGET, "max_2bit": MAX_2BIT, "l0_exclude_2bit": True},
        "analysis": {"top5_concentration": round(top5_concentration, 4)},
        "ppl_bf16": round(ppl_bf16, 4),
        "ppl_uniform_4bit": round(ppl_uniform, 4),
        "ppl_constrained_mckp": round(ppl_constrained, 4),
        "ppl_unconstrained_mckp": round(ppl_unconstrained, 4),
        "ppl_greedy": round(ppl_greedy, 4),
        "delta_uniform": round(ppl_uniform - ppl_bf16, 4),
        "delta_constrained": round(ppl_constrained - ppl_bf16, 4),
        "delta_unconstrained": round(ppl_unconstrained - ppl_bf16, 4),
        "delta_greedy": round(ppl_greedy - ppl_bf16, 4),
        "constrained_vs_uniform": round(ppl_uniform - ppl_constrained, 4),
        "constrained_bit_distribution": constrained.get("bit_distribution", {}),
        "unconstrained_bit_distribution": unconstrained.get("bit_distribution", {}),
        "greedy_bit_distribution": greedy.get("bit_distribution", {}),
        "constrained_allocation": {k: list(v) for k, v in constrained["allocation"].items()},
        "elapsed_seconds": round(elapsed, 1),
    }

    os.makedirs("artifacts", exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")

    # --- Summary ---
    print(f"\n{'='*65}")
    print("RESULTS — Phi-3-medium-14B Constrained MCKP Pipeline")
    print(f"{'='*65}")
    print(f"{'Method':<28} {'PPL':>10} {'Delta':>10} {'vs Uniform':>12}")
    print("-" * 65)
    print(f"{'Baseline (bf16)':<28} {ppl_bf16:>10.4f} {'---':>10} {'---':>12}")
    print(f"{'Constrained MCKP (k=8)':<28} {ppl_constrained:>10.4f} {ppl_constrained-ppl_bf16:>+10.4f} {ppl_uniform-ppl_constrained:>+12.4f}")
    print(f"{'Unconstrained MCKP':<28} {ppl_unconstrained:>10.4f} {ppl_unconstrained-ppl_bf16:>+10.4f} {ppl_uniform-ppl_unconstrained:>+12.4f}")
    print(f"{'Greedy':<28} {ppl_greedy:>10.4f} {ppl_greedy-ppl_bf16:>+10.4f} {ppl_uniform-ppl_greedy:>+12.4f}")
    print(f"{'Uniform 4-bit':<28} {ppl_uniform:>10.4f} {ppl_uniform-ppl_bf16:>+10.4f} {'---':>12}")
    print(f"\nTop-5% concentration: {top5_concentration:.4f}")
    print(f"Total time: {elapsed/60:.1f}min")


if __name__ == "__main__":
    main()
