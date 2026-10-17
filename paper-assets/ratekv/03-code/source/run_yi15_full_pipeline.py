"""Yi-1.5-9B Full Pipeline: profiling + MCKP + k ablation.
GQA 8:1 (4 KV heads/layer, 48 layers, 192 total heads).
Llama-compatible architecture — uses standard profiler and eval code.
Tests whether high GQA ratio → high heterogeneity generalizes beyond Qwen.
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import argparse
import json
import math
import time
import torch
from transformers import AutoConfig
from full_bitwidth_profiler import FullBitwidthProfiler
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--calibration_data", type=str, default="calibration_data.json")
    parser.add_argument("--output", type=str, default="yi15_full_results.json")
    parser.add_argument("--budget", type=float, default=0.25)
    parser.add_argument("--initial_k", type=int, default=8)
    parser.add_argument("--gpu", type=str, default="cuda:1")
    args = parser.parse_args()

    device = args.gpu
    t0 = time.time()

    # Validate architecture
    config = AutoConfig.from_pretrained(args.model)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads

    print(f"Yi-1.5-9B: {num_layers} layers, {num_kv_heads} KV heads/layer, "
          f"GQA {gqa_ratio}:1, {total_kv_heads} total KV heads")
    assert num_kv_heads == 4, f"Expected 4 KV heads, got {num_kv_heads}"
    assert num_layers == 48, f"Expected 48 layers, got {num_layers}"

    # ========== Phase 1: Profiling ==========
    print("\n" + "=" * 60)
    print("PHASE 1: Profiling (192 heads × 3 bitwidths)")
    print("=" * 60)

    profile_start = time.time()
    profiler = FullBitwidthProfiler(
        model_path=args.model,
        calibration_data=args.calibration_data,
        device=device,
        num_samples=16,
        seq_len=512,
    )
    baseline_cal_ppl = profiler.compute_baseline_ppl()
    profiles_raw = profiler.profile_all(bit_widths=(2, 4, 8))
    profile_time = time.time() - profile_start

    with open("yi15_profiling_results.json", "w") as f:
        json.dump(profiles_raw, f, indent=2)
    print(f"Phase 1 done in {profile_time / 60:.1f}min")

    _print_sensitivity(profiles_raw)

    profiles = enforce_monotonicity(profiles_raw)

    # ========== Phase 2: MCKP + Uniform + BF16 eval ==========
    print("\n" + "=" * 60)
    print(f"PHASE 2: MCKP (k={args.initial_k}) + Uniform + BF16 eval")
    print("=" * 60)

    phase2_start = time.time()
    model = profiler.model
    tokenizer = profiler.tokenizer

    print("Evaluating bf16 baseline on WikiText-2...")
    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)
    print(f"BF16 WikiText-2 PPL: {baseline_wt2:.4f}")

    # MCKP allocation
    mckp_result = solve_mckp_constrained(
        profiles, args.budget, mode="quant_only",
        max_2bit=args.initial_k, l0_exclude_2bit=True)

    bit_counts = {}
    for key, (atype, param) in mckp_result["allocation"].items():
        b = int(param) if atype == "quant" else 16
        bit_counts[b] = bit_counts.get(b, 0) + 1
    print(f"MCKP bit distribution: {bit_counts}")

    orig_fwds = patch_attention(model, mckp_result["allocation"])
    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"MCKP PPL: {mckp_wt2:.4f}")

    # Uniform 4-bit
    uniform_result = uniform_quantization_baseline(profiles, bits=4)
    orig_fwds = patch_attention(model, uniform_result["allocation"])
    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"Uniform 4-bit PPL: {uniform_wt2:.4f}")

    delta_phase2 = uniform_wt2 - mckp_wt2
    print(f"MCKP improvement over uniform: {delta_phase2:+.4f}")
    phase2_time = time.time() - phase2_start

    # ========== Phase 3: K Ablation ==========
    print("\n" + "=" * 60)
    print("PHASE 3: K Ablation Sweep")
    print("=" * 60)

    ablation_start = time.time()
    k_values = [2, 4, 6, 8, 10, 12, 14, 16]
    k_results = []

    for k in k_values:
        print(f"\n--- k={k} ---")
        result_k = solve_mckp_constrained(
            profiles, args.budget, mode="quant_only",
            max_2bit=k, l0_exclude_2bit=True)

        orig_fwds = patch_attention(model, result_k["allocation"])
        ppl_k = evaluate_perplexity(model, tokenizer, device)
        restore_attention(model, orig_fwds)

        n_2bit = sum(1 for _, (a, p) in result_k["allocation"].items()
                     if a == "quant" and int(p) == 2)
        k_entry = {
            "max_2bit": k,
            "ppl": round(ppl_k, 4),
            "n_2bit_actual": n_2bit,
            "total_distortion": result_k["total_distortion"],
            "actual_memory_ratio": result_k["actual_memory_ratio"],
        }
        k_results.append(k_entry)
        print(f"k={k}: PPL={ppl_k:.4f}, n_2bit={n_2bit}")

    with open("yi15_k_ablation_results.json", "w") as f:
        json.dump(k_results, f, indent=2)

    best_k = min(k_results, key=lambda x: x["ppl"])
    print(f"\nBest k={best_k['max_2bit']} with PPL={best_k['ppl']:.4f}")
    ablation_time = time.time() - ablation_start

    # ========== Phase 4: Analysis ==========
    print("\n" + "=" * 60)
    print("PHASE 4: Heterogeneity Analysis")
    print("=" * 60)

    all_deltas_2bit = []
    layer_deltas = {}
    for l_str in sorted(profiles.keys(), key=int):
        l = int(l_str)
        layer_deltas[l] = []
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            all_deltas_2bit.append((l, int(h_str), d2))
            layer_deltas[l].append(d2)

    # Top-5% concentration
    sorted_by_d2 = sorted(all_deltas_2bit, key=lambda x: -x[2])
    n_top5 = max(1, int(len(sorted_by_d2) * 0.05))
    total_sum = sum(x[2] for x in all_deltas_2bit)
    top5_sum = sum(x[2] for x in sorted_by_d2[:n_top5])
    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0

    # Layer 0 dominance
    l0_deltas = layer_deltas.get(0, [0])
    l0_mean = sum(l0_deltas) / max(len(l0_deltas), 1)
    other_means = []
    for l in range(1, num_layers):
        if l in layer_deltas and layer_deltas[l]:
            other_means.append(sum(layer_deltas[l]) / len(layer_deltas[l]))
    other_avg = sum(other_means) / len(other_means) if other_means else 0
    l0_ratio = l0_mean / other_avg if other_avg > 0 else float("inf")

    # General stats
    d_tensor = torch.tensor([x[2] for x in all_deltas_2bit])
    n_positive = int((d_tensor > 1e-6).sum().item())
    cv = d_tensor.std().item() / d_tensor.mean().item() if d_tensor.mean().item() > 0 else 0

    print(f"Top-5% concentration: {top5_concentration:.4f} ({n_top5} heads)")
    print(f"Layer 0 mean delta(2bit): {l0_mean:.6f}")
    print(f"Other layers mean delta(2bit): {other_avg:.6f}")
    print(f"L0 dominance ratio: {l0_ratio:.2f}x")
    print(f"Heads with positive delta: {n_positive}/{len(all_deltas_2bit)}")
    print(f"CV of delta(2bit): {cv:.4f}")

    print("\nTop-5 most sensitive heads:")
    for name_l, name_h, d2 in sorted_by_d2[:5]:
        d4 = profiles[str(name_l)][str(name_h)]["quantization"].get("4", 0.0)
        d8 = profiles[str(name_l)][str(name_h)]["quantization"].get("8", 0.0)
        print(f"  L{name_l}H{name_h}: 2bit={d2:+.4f}, 4bit={d4:+.4f}, 8bit={d8:+.4f}")

    mckp_dist = mckp_result["total_distortion"]
    print(f"\nMCKP total distortion: {mckp_dist:.6f}")

    # ========== Phase 5: Save Results ==========
    total_time = time.time() - t0

    results = {
        "model": args.model,
        "model_name": "Yi-1.5-9B",
        "model_type": config.model_type,
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "head_dim": config.hidden_size // num_q_heads,
            "hidden_size": config.hidden_size,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
        },
        "verdict": "PASS" if delta_phase2 >= 0.5 else "MARGINAL" if delta_phase2 >= 0.1 else "FAIL",
        "baseline_calibration_ppl": baseline_cal_ppl,
        "baseline_wikitext2_ppl": baseline_wt2,
        "mckp_wikitext2_ppl": mckp_wt2,
        "uniform4bit_wikitext2_ppl": uniform_wt2,
        "mckp_improvement_over_uniform": delta_phase2,
        "initial_k": args.initial_k,
        "bit_distribution": bit_counts,
        "mckp_actual_memory_ratio": mckp_result["actual_memory_ratio"],
        "k_ablation": k_results,
        "best_k": best_k,
        "analysis": {
            "top5_concentration": round(top5_concentration, 4),
            "top5_n_heads": n_top5,
            "layer0_mean_delta_2bit": round(l0_mean, 6),
            "other_layers_mean_delta_2bit": round(other_avg, 6),
            "layer0_dominance_ratio": round(l0_ratio, 2),
            "delta_2bit_mean": round(d_tensor.mean().item(), 6),
            "delta_2bit_std": round(d_tensor.std().item(), 6),
            "delta_2bit_cv": round(cv, 4),
            "heads_with_positive_delta": n_positive,
        },
        "timing": {
            "profile_seconds": round(profile_time, 1),
            "phase2_seconds": round(phase2_time, 1),
            "ablation_seconds": round(ablation_time, 1),
            "total_seconds": round(total_time, 1),
        },
        "config": {
            "budget": args.budget,
            "initial_k": args.initial_k,
            "k_values": k_values,
            "calibration_data": args.calibration_data,
        },
    }

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 60}")
    print("RESULTS — Yi-1.5-9B")
    print(f"{'=' * 60}")
    print(f"\n{'Method':<30} {'PPL':>10} {'Delta vs uniform':>18}")
    print("-" * 60)
    print(f"{'Baseline (bf16)':<30} {baseline_wt2:>10.4f} {'---':>18}")
    print(f"{'Non-uniform MCKP':<30} {mckp_wt2:>10.4f} {delta_phase2:>+18.4f}")
    print(f"{'Uniform 4-bit':<30} {uniform_wt2:>10.4f} {'---':>18}")
    print(f"\nTop-5% concentration: {top5_concentration:.4f}")
    print(f"L0 dominance: {l0_ratio:.2f}x")
    print(f"Best k: {best_k['max_2bit']} (PPL={best_k['ppl']:.4f})")
    print(f"Verdict: {results['verdict']}")
    print(f"Total time: {total_time / 3600:.1f}h")
    print(f"\nSaved to {args.output}")


def _print_sensitivity(profiles):
    all_2bit = []
    for l_str in sorted(profiles.keys(), key=int):
        for h_str in sorted(profiles[l_str].keys(), key=int):
            delta_2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            delta_4 = profiles[l_str][h_str]["quantization"].get("4", 0.0)
            delta_8 = profiles[l_str][h_str]["quantization"].get("8", 0.0)
            all_2bit.append((f"L{l_str}H{h_str}", delta_2, delta_4, delta_8))

    deltas = [x[1] for x in all_2bit]
    print(f"\n2-bit delta stats: min={min(deltas):.4f}, max={max(deltas):.4f}, "
          f"mean={sum(deltas) / len(deltas):.4f}, "
          f"std={torch.tensor(deltas).std().item():.4f}")

    by_2bit = sorted(all_2bit, key=lambda x: -x[1])
    print("\nTop-5 most sensitive heads (2-bit):")
    for name, d2, d4, d8 in by_2bit[:5]:
        print(f"  {name}: 2bit={d2:+.4f}, 4bit={d4:+.4f}, 8bit={d8:+.4f}")
    print("\nBottom-5 least sensitive heads (2-bit):")
    for name, d2, d4, d8 in by_2bit[-5:]:
        print(f"  {name}: 2bit={d2:+.4f}, 4bit={d4:+.4f}, 8bit={d8:+.4f}")


if __name__ == "__main__":
    main()
