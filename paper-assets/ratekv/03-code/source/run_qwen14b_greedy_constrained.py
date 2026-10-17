"""Qwen2.5-14B Greedy Constrained ablation for Table 1 Greedy column.
Input: qwen14b_hires_bf16_2bitonly_profiles.json (per-head 2-bit distortion deltas)
Output: artifacts/qwen14b_greedy_constrained_results.json (greedy PPL + bit distribution)
Params: budget=0.25, max_2bit=8, bit_options={2,4,8,16}
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
from solver import enforce_monotonicity

RATIO_4BIT = 0.25
RATIO_8BIT = 0.05


def solve_greedy_constrained(profiles, budget, max_2bit=8, bit_options=None):
    """Greedy downgrade with cardinality constraint on 2-bit assignments.

    Starting from all heads at max bit-width (16), iteratively downgrades the
    head with the smallest marginal distortion increase per bit saved, subject
    to at most max_2bit heads being assigned 2-bit precision.
    """
    if bit_options is None:
        bit_options = [2, 4, 8, 16]
    bit_options = sorted(bit_options)

    heads = []
    for l_str in sorted(profiles.keys(), key=lambda x: int(x)):
        for h_str in sorted(profiles[l_str].keys(), key=lambda x: int(x)):
            l, h = int(l_str), int(h_str)
            qdata = profiles[l_str][h_str].get("quantization", {})
            distortion_map = {16: 0.0}
            for b in bit_options:
                if b == 16:
                    continue
                for key in [str(b), str(float(b))]:
                    if key in qdata:
                        distortion_map[b] = qdata[key]
                        break
            heads.append((l, h, distortion_map))

    n_heads = len(heads)
    max_bits = max(bit_options)
    allocation = [max_bits] * n_heads
    target_mem = budget * n_heads * max_bits

    count_2bit = 0
    steps = 0

    while sum(allocation) > target_mem + 1e-9:
        best_head = None
        best_gain = float('inf')

        for i in range(n_heads):
            cur_bits = allocation[i]
            lower = [b for b in bit_options if b < cur_bits]
            if not lower:
                continue
            next_lower = max(lower)

            if next_lower == 2 and count_2bit >= max_2bit:
                lower = [b for b in lower if b > 2]
                if not lower:
                    continue
                next_lower = max(lower)

            cur_dist = heads[i][2].get(cur_bits, 0.0)
            nxt_dist = heads[i][2].get(next_lower, None)
            if nxt_dist is None:
                continue

            bits_saved = cur_bits - next_lower
            dist_inc = nxt_dist - cur_dist
            marginal = dist_inc / bits_saved

            if marginal < best_gain:
                best_gain = marginal
                best_head = i
                best_next = next_lower

        if best_head is None:
            print(f"  Early termination at step {steps}: no valid downgrade")
            break

        allocation[best_head] = best_next
        if best_next == 2:
            count_2bit += 1
        steps += 1

    alloc_dict = {}
    total_dist = 0.0
    bit_dist = {}
    for i, (l, h, dmap) in enumerate(heads):
        b = allocation[i]
        alloc_dict[f"{l},{h}"] = ["quant" if b < 16 else "full", b]
        total_dist += dmap.get(b, 0.0)
        bit_dist[b] = bit_dist.get(b, 0) + 1

    actual_ratio = sum(allocation) / (n_heads * max_bits)

    return {
        "allocation": alloc_dict,
        "total_distortion": total_dist,
        "actual_memory_ratio": actual_ratio,
        "bit_distribution": bit_dist,
        "n_2bit": bit_dist.get(2, 0),
        "steps": steps,
        "early_stop": sum(allocation) > target_mem + 1e-9,
    }


def main():
    device = "cuda:0"
    model_name = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-14B"
    profiles_path = "qwen14b_hires_bf16_2bitonly_profiles.json"
    output_path = "artifacts/qwen14b_greedy_constrained_results.json"
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

    print(f"\n=== Greedy + Cardinality Constraint (max_2bit={max_2bit}) ===")
    print(f"Budget: {budget}, Bit options: [2, 4, 8, 16]")
    t_solve = time.time()
    sol = solve_greedy_constrained(profiles, budget, max_2bit=max_2bit)
    t_solve = time.time() - t_solve

    print(f"Solve time: {t_solve:.2f}s")
    print(f"Bit distribution: {sol['bit_distribution']}")
    print(f"Memory ratio: {sol['actual_memory_ratio']:.4f}")
    print(f"Total distortion: {sol['total_distortion']:.6f}")
    print(f"Steps: {sol['steps']}, Early stop: {sol['early_stop']}")

    if sol['early_stop']:
        print(f"WARNING: budget not met! actual={sol['actual_memory_ratio']:.4f} > target={budget}")

    print(f"\nLoading model in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(device) / 1e9
    print(f"Model loaded. GPU mem: {mem_gb:.1f}GB")

    print("\nEvaluating bf16 baseline on WikiText-2...")
    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)
    print(f"BF16 WikiText-2 PPL: {baseline_wt2:.4f}")

    print("\nEvaluating greedy constrained on WikiText-2...")
    orig_fwds = patch_attention(model, sol["allocation"])
    greedy_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"Greedy constrained PPL: {greedy_wt2:.4f}")

    total_time = time.time() - t0

    ref_mckp = 7.2206
    ref_uniform = 7.2020
    delta_vs_mckp = greedy_wt2 - ref_mckp
    delta_vs_uniform = greedy_wt2 - ref_uniform

    results = {
        "model": model_name,
        "model_name": "Qwen2.5-14B",
        "experiment": "greedy_constrained",
        "method": f"greedy_constrained_max2bit_{max_2bit}",
        "budget": budget,
        "max_2bit": max_2bit,
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
        },
        "profiling": {
            "source": profiles_path,
            "type": "hires_bf16_2bitonly",
            "synthesized_ratios": {"4bit": RATIO_4BIT, "8bit": RATIO_8BIT},
        },
        "solver": {
            "solve_time_seconds": round(t_solve, 2),
            "steps": sol["steps"],
            "early_stop": sol["early_stop"],
            "total_distortion": round(sol["total_distortion"], 6),
            "memory_ratio": round(sol["actual_memory_ratio"], 4),
        },
        "results": {
            "baseline_wikitext2_ppl": round(baseline_wt2, 4),
            "greedy_constrained_wikitext2_ppl": round(greedy_wt2, 4),
        },
        "comparison": {
            "ref_uniform4bit_ppl": ref_uniform,
            "ref_constrained_mckp_ppl": ref_mckp,
            "delta_vs_mckp": round(delta_vs_mckp, 4),
            "delta_vs_uniform": round(delta_vs_uniform, 4),
        },
        "bit_distribution": {str(k): v for k, v in sol["bit_distribution"].items()},
        "allocation": sol["allocation"],
        "timing": {"total_seconds": round(total_time, 1)},
    }

    os.makedirs("artifacts", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 70}")
    print("RESULTS - Qwen2.5-14B Greedy Constrained (Table 1)")
    print(f"{'=' * 70}")
    print(f"\n{'Method':<35} {'PPL':>10} {'Delta vs MCKP':>15}")
    print("-" * 62)
    print(f"{'Baseline (bf16)':<35} {baseline_wt2:>10.4f} {'---':>15}")
    print(f"{'Uniform 4-bit (ref)':<35} {ref_uniform:>10.4f} {'---':>15}")
    print(f"{'Constrained MCKP (ref)':<35} {ref_mckp:>10.4f} {'(reference)':>15}")
    print(f"{'Greedy constrained (k={max_2bit})':<35} {greedy_wt2:>10.4f} {delta_vs_mckp:>+15.4f}")
    print(f"\nBit distribution: {sol['bit_distribution']}")
    print(f"Total time: {total_time / 60:.1f}min")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
