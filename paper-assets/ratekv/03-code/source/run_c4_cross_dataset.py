"""C4 Cross-Dataset Evaluation (plan_007).
Profile with C4 calibration data, solve MCKP, eval PPL, compare with WikiText-2 results.
"""
import json
import time
import torch
from full_bitwidth_profiler import FullBitwidthProfiler
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity

MODEL = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B"
DEVICE = "cuda:0"
C4_CALIBRATION = "c4_calibration.json"
WT2_REF_FILE = "budget_sweep_results.json"
BUDGET = 0.25
MAX_2BIT = 8


def load_wt2_reference():
    with open(WT2_REF_FILE) as f:
        data = json.load(f)
    for r in data["results"]:
        if abs(r["budget"] - BUDGET) < 1e-6:
            return r
    raise ValueError(f"No budget={BUDGET} entry in {WT2_REF_FILE}")


def compute_agreement(alloc_a, alloc_b):
    keys = set(alloc_a.keys()) & set(alloc_b.keys())
    if not keys:
        return 0.0, {}
    agree = 0
    disagree_details = {}
    for k in sorted(keys):
        a_type, a_param = alloc_a[k]
        b_type, b_param = alloc_b[k]
        if a_type == b_type and a_param == b_param:
            agree += 1
        else:
            disagree_details[k] = {"wt2": [a_type, a_param], "c4": [b_type, b_param]}
    return agree / len(keys), disagree_details


def main():
    t_start = time.time()

    # === Phase 1: C4 Profiling ===
    print("=" * 60)
    print("[Phase 1] Profiling with C4 calibration data...")
    print("=" * 60)
    t0 = time.time()

    profiler = FullBitwidthProfiler(
        model_path=MODEL,
        calibration_data=C4_CALIBRATION,
        device=DEVICE,
        num_samples=16,
        seq_len=512
    )
    baseline_cal_ppl = profiler.compute_baseline_ppl()
    raw_profiles = profiler.profile_all(bit_widths=(2, 4, 8))
    profile_time = time.time() - t0
    print(f"\nC4 profiling done in {profile_time:.1f}s")

    # Save raw profiles
    profiling_output = {
        "calibration_source": "c4",
        "baseline_calibration_ppl": baseline_cal_ppl,
        "profile_time_seconds": profile_time,
        "profiles": raw_profiles,
    }
    with open("c4_profiling_results.json", "w") as f:
        json.dump(profiling_output, f, indent=2)
    print("Saved c4_profiling_results.json")

    # === Phase 2: Enforce monotonicity + Solve MCKP ===
    print(f"\n{'=' * 60}")
    print("[Phase 2] Solving constrained MCKP (budget=0.25, max_2bit=8)...")
    print("=" * 60)

    profiles = enforce_monotonicity(raw_profiles)
    mckp_sol = solve_mckp_constrained(
        profiles, BUDGET, mode="quant_only",
        max_2bit=MAX_2BIT, l0_exclude_2bit=True
    )
    uniform_sol = uniform_quantization_baseline(profiles, bits=4)

    print(f"MCKP bit distribution: {mckp_sol['bit_distribution']}")
    print(f"MCKP memory ratio: {mckp_sol['actual_memory_ratio']:.4f}")
    print(f"MCKP total distortion: {mckp_sol['total_distortion']:.6f}")

    # === Phase 3: WikiText-2 PPL Eval ===
    print(f"\n{'=' * 60}")
    print("[Phase 3] WikiText-2 PPL evaluation...")
    print("=" * 60)

    model = profiler.model
    tokenizer = profiler.tokenizer
    t1 = time.time()

    print("\n  Evaluating FP16 baseline...")
    fp16_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    print(f"  >>> FP16 PPL = {fp16_ppl:.4f}")

    print("\n  Evaluating C4-calibrated MCKP allocation...")
    orig = patch_attention(model, mckp_sol["allocation"])
    c4_mckp_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f"  >>> C4-MCKP PPL = {c4_mckp_ppl:.4f}")

    print("\n  Evaluating uniform 4-bit...")
    orig = patch_attention(model, uniform_sol["allocation"])
    uniform_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f"  >>> Uniform 4-bit PPL = {uniform_ppl:.4f}")

    eval_time = time.time() - t1

    # === Phase 4: Cross-dataset comparison ===
    print(f"\n{'=' * 60}")
    print("[Phase 4] Cross-dataset comparison...")
    print("=" * 60)

    wt2_ref = load_wt2_reference()
    wt2_mckp_ppl = wt2_ref["mckp_ppl"]
    wt2_uniform_ppl = wt2_ref["uniform_ppl"]
    wt2_alloc = wt2_ref["mckp_allocation"]
    wt2_bit_dist = wt2_ref["bit_distribution"]

    agreement_rate, disagree_details = compute_agreement(wt2_alloc, mckp_sol["allocation"])

    c4_delta = uniform_ppl - c4_mckp_ppl
    wt2_delta = wt2_uniform_ppl - wt2_mckp_ppl

    total_time = time.time() - t_start

    # === Print summary ===
    print(f"\n{'=' * 70}")
    print("CROSS-DATASET COMPARISON RESULTS")
    print("=" * 70)
    print(f"\n{'Metric':<40} {'WikiText-2 cal':>15} {'C4 cal':>15}")
    print("-" * 70)
    print(f"{'Calibration baseline PPL':<40} {'N/A':>15} {baseline_cal_ppl:>15.4f}")
    print(f"{'FP16 WikiText-2 PPL':<40} {fp16_ppl:>15.4f} {fp16_ppl:>15.4f}")
    print(f"{'MCKP WikiText-2 PPL':<40} {wt2_mckp_ppl:>15.4f} {c4_mckp_ppl:>15.4f}")
    print(f"{'Uniform 4-bit WikiText-2 PPL':<40} {wt2_uniform_ppl:>15.4f} {uniform_ppl:>15.4f}")
    print(f"{'Delta (uniform - MCKP)':<40} {wt2_delta:>+15.4f} {c4_delta:>+15.4f}")
    print(f"\n{'Bit distribution (WT2 cal):':<40} {wt2_bit_dist}")
    print(f"{'Bit distribution (C4 cal):':<40} {mckp_sol['bit_distribution']}")
    print(f"\nAllocation agreement rate: {agreement_rate:.1%} ({int(agreement_rate * 112)}/112 heads)")
    print(f"Number of disagreements: {len(disagree_details)}")

    if disagree_details:
        print("\nDisagreement details (first 20):")
        for i, (k, v) in enumerate(sorted(disagree_details.items())):
            if i >= 20:
                print(f"  ... and {len(disagree_details) - 20} more")
                break
            print(f"  {k}: WT2={v['wt2']}, C4={v['c4']}")

    print(f"\nProfile time: {profile_time:.1f}s, Eval time: {eval_time:.1f}s, Total: {total_time:.1f}s")

    # === Save results ===
    results = {
        "experiment": "c4_cross_dataset_eval",
        "calibration_source": "c4",
        "budget": BUDGET,
        "max_2bit": MAX_2BIT,
        "c4_calibration_baseline_ppl": baseline_cal_ppl,
        "fp16_wikitext2_ppl": fp16_ppl,
        "c4_mckp_wikitext2_ppl": c4_mckp_ppl,
        "uniform4bit_wikitext2_ppl": uniform_ppl,
        "c4_mckp_delta_over_uniform": c4_delta,
        "c4_mckp_bit_distribution": mckp_sol["bit_distribution"],
        "c4_mckp_memory_ratio": mckp_sol["actual_memory_ratio"],
        "c4_mckp_total_distortion": mckp_sol["total_distortion"],
        "c4_mckp_allocation": mckp_sol["allocation"],
        "wt2_reference": {
            "mckp_ppl": wt2_mckp_ppl,
            "uniform_ppl": wt2_uniform_ppl,
            "delta": wt2_delta,
            "bit_distribution": wt2_bit_dist,
        },
        "cross_dataset_comparison": {
            "allocation_agreement_rate": agreement_rate,
            "n_agree": int(agreement_rate * 112),
            "n_disagree": len(disagree_details),
            "disagree_details": disagree_details,
            "ppl_gap_mckp": c4_mckp_ppl - wt2_mckp_ppl,
            "delta_gap": c4_delta - wt2_delta,
        },
        "timing": {
            "profile_seconds": profile_time,
            "eval_seconds": eval_time,
            "total_seconds": total_time,
        },
        "c4_profiles": raw_profiles,
    }

    with open("c4_eval_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nSaved c4_eval_results.json")


if __name__ == "__main__":
    main()
