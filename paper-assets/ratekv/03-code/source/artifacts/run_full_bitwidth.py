"""PPL-guided Quant-only MCKP with full bit-width action space {2,4,8,16}.
End-to-end: profile → solve → evaluate → verdict.
"""

import argparse
import json
import math
import time
import torch
from full_bitwidth_profiler import FullBitwidthProfiler
from solver import solve_mckp, uniform_quantization_baseline
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity


def print_sensitivity_analysis(profiles):
    all_2bit = []
    for l_str in sorted(profiles.keys(), key=int):
        for h_str in sorted(profiles[l_str].keys(), key=int):
            delta_2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            delta_4 = profiles[l_str][h_str]["quantization"].get("4", 0.0)
            delta_8 = profiles[l_str][h_str]["quantization"].get("8", 0.0)
            all_2bit.append((f"L{l_str}H{h_str}", delta_2, delta_4, delta_8))

    deltas = [x[1] for x in all_2bit]
    print(f"\n2-bit delta stats: min={min(deltas):.4f}, max={max(deltas):.4f}, "
          f"mean={sum(deltas)/len(deltas):.4f}, "
          f"std={torch.tensor(deltas).std().item():.4f}")

    by_2bit = sorted(all_2bit, key=lambda x: -x[1])
    print("\nTop-5 most sensitive heads (2-bit):")
    for name, d2, d4, d8 in by_2bit[:5]:
        print(f"  {name}: 2bit={d2:+.4f}, 4bit={d4:+.4f}, 8bit={d8:+.4f}")

    print("\nBottom-5 least sensitive heads (2-bit):")
    for name, d2, d4, d8 in by_2bit[-5:]:
        print(f"  {name}: 2bit={d2:+.4f}, 4bit={d4:+.4f}, 8bit={d8:+.4f}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--calibration_data", type=str, default="calibration_data.json")
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--budget", type=float, default=0.25)
    parser.add_argument("--output", type=str, default="full_bitwidth_results.json")
    parser.add_argument("--num_calibration_samples", type=int, default=16)
    parser.add_argument("--calibration_seq_len", type=int, default=512)
    args = parser.parse_args()

    print("=" * 60)
    print("PPL-guided Quant-only MCKP — Full Bit-width Action Space")
    print("=" * 60)
    print(f"Model: {args.model}")
    print(f"Budget: {args.budget} (={int(args.budget*16)}-bit equivalent)")
    print(f"Device: {args.device}")

    # === Phase 1: Profile ===
    print(f"\n{'='*60}")
    print("[Phase 1] Profiling per-head PPL sensitivity...")
    print(f"{'='*60}")
    t0 = time.time()

    profiler = FullBitwidthProfiler(
        model_path=args.model,
        calibration_data=args.calibration_data,
        device=args.device,
        num_samples=args.num_calibration_samples,
        seq_len=args.calibration_seq_len
    )
    baseline_cal_ppl = profiler.compute_baseline_ppl()
    profiles = profiler.profile_all(bit_widths=(2, 4, 8))

    profile_time = time.time() - t0
    print(f"\nProfiling done in {profile_time:.1f}s")
    print_sensitivity_analysis(profiles)

    # === Phase 2: Solve MCKP ===
    print(f"\n{'='*60}")
    print("[Phase 2] Solving MCKP...")
    print(f"{'='*60}")

    mckp_result = solve_mckp(profiles, args.budget, mode="quant_only")
    uniform_result = uniform_quantization_baseline(profiles, bits=4)

    bit_counts = {"2bit": 0, "4bit": 0, "8bit": 0, "16bit": 0}
    for key, (atype, param) in mckp_result["allocation"].items():
        if atype == "full":
            bit_counts["16bit"] += 1
        else:
            bit_counts[f"{int(param)}bit"] += 1

    print(f"MCKP allocation: {bit_counts}")
    print(f"Actual memory ratio: {mckp_result['actual_memory_ratio']:.4f} "
          f"(target: {args.budget:.4f})")
    print(f"MCKP total distortion (sum of PPL deltas): {mckp_result['total_distortion']:.4f}")
    print(f"Uniform 4-bit total distortion: {uniform_result['total_distortion']:.4f}")

    # Print a few example allocations
    print("\nSample allocations (Layer 0):")
    for key, (atype, param) in sorted(mckp_result["allocation"].items()):
        l = int(key.split(",")[0])
        if l == 0:
            print(f"  {key}: {atype} {param}")

    # === Phase 3: WikiText-2 PPL Eval ===
    print(f"\n{'='*60}")
    print("[Phase 3] WikiText-2 PPL evaluation...")
    print(f"{'='*60}")
    t1 = time.time()

    model = profiler.model
    tokenizer = profiler.tokenizer
    device = args.device

    print("\n  Evaluating baseline (no compression)...")
    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)
    print(f"  >>> Baseline WikiText-2 PPL: {baseline_wt2:.4f}")

    print("\n  Evaluating non-uniform MCKP...")
    orig_fwds = patch_attention(model, mckp_result["allocation"])
    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"  >>> Non-uniform MCKP WikiText-2 PPL: {mckp_wt2:.4f}")

    print("\n  Evaluating uniform 4-bit...")
    orig_fwds = patch_attention(model, uniform_result["allocation"])
    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"  >>> Uniform 4-bit WikiText-2 PPL: {uniform_wt2:.4f}")

    eval_time = time.time() - t1

    # === Phase 4: Results ===
    delta = uniform_wt2 - mckp_wt2
    passed = delta >= 0.5
    verdict = "PASS" if passed else "FAIL"

    print(f"\n{'='*60}")
    print("RESULTS")
    print(f"{'='*60}")
    print(f"\n{'Method':<30} {'PPL':>10} {'Delta vs uniform':>18}")
    print("-" * 60)
    print(f"{'Baseline':<30} {baseline_wt2:>10.4f} {'—':>18}")
    print(f"{'Non-uniform MCKP':<30} {mckp_wt2:>10.4f} {delta:>+18.4f}")
    print(f"{'Uniform 4-bit':<30} {uniform_wt2:>10.4f} {'—':>18}")
    print(f"\nMCKP bit distribution: {bit_counts}")
    print(f"Budget target: {args.budget:.4f}, Actual: {mckp_result['actual_memory_ratio']:.4f}")
    print(f"Profile time: {profile_time:.1f}s, Eval time: {eval_time:.1f}s")

    print(f"\n{'='*60}")
    print(f"VERDICT: {verdict}")
    print(f"Non-uniform improvement over uniform: {delta:+.4f} (threshold: >=0.5)")
    print(f"{'='*60}")

    # Save results
    results = {
        "verdict": verdict,
        "baseline_calibration_ppl": baseline_cal_ppl,
        "baseline_wikitext2_ppl": baseline_wt2,
        "mckp_wikitext2_ppl": mckp_wt2,
        "uniform4bit_wikitext2_ppl": uniform_wt2,
        "mckp_improvement_over_uniform": delta,
        "bit_distribution": bit_counts,
        "mckp_actual_memory_ratio": mckp_result["actual_memory_ratio"],
        "mckp_total_distortion": mckp_result["total_distortion"],
        "mckp_allocation": mckp_result["allocation"],
        "profiles": profiles,
        "config": {
            "model": args.model,
            "budget": args.budget,
            "num_calibration_samples": args.num_calibration_samples,
            "calibration_seq_len": args.calibration_seq_len,
            "profile_time_seconds": profile_time,
            "eval_time_seconds": eval_time
        }
    }

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nFull results saved to {args.output}")


if __name__ == "__main__":
    main()
