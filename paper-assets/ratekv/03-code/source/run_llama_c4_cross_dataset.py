"""Llama-3.1-8B C4 Cross-Dataset Evaluation.

Profile with C4 calibration data, solve constrained MCKP (k=2),
evaluate on WT2 and C4, compare with WT2-calibrated allocation.

Input:
  - C4 calibration data: c4_calibration_real.json (allenai/c4 en validation, concatenated)
  - WT2 hires profiles: llama_ppl_profiles_hires.json (64x2048)
  - Model: Llama-3.1-8B (32 layers, 8 KV heads, 256 total heads, GQA 4:1)

Output:
  - llama_c4_cross_dataset_results.json (full results)
  - llama_c4_cross_dataset.log (execution log)
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import json
import math
import sys
import time
import torch
import torch.nn.functional as F

from full_bitwidth_profiler import FullBitwidthProfiler
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity

MODEL = "/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B/"
DEVICE = "cuda:0"
C4_CALIBRATION = "c4_calibration_real.json"
WT2_PROFILES_FILE = "llama_ppl_profiles_hires.json"
BUDGET = 0.25
MAX_2BIT = 2  # Llama natural 2-bit count

LOG_FILE = "llama_c4_cross_dataset.log"
RESULTS_FILE = "llama_c4_cross_dataset_results.json"


class Tee:
    """Duplicate stdout to a log file."""
    def __init__(self, path):
        self.file = open(path, "w")
        self.stdout = sys.stdout
    def write(self, data):
        self.stdout.write(data)
        self.file.write(data)
    def flush(self):
        self.stdout.flush()
        self.file.flush()


def compute_agreement(alloc_a, alloc_b):
    """Compute per-head allocation agreement rate between two allocations."""
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


def evaluate_ppl_on_c4(model, tokenizer, device, data_path, seq_len=512, num_samples=16):
    """Evaluate perplexity on C4 calibration data (batch forward pass)."""
    with open(data_path) as f:
        samples = json.load(f)

    all_ids = []
    for s in samples:
        tokens = tokenizer.encode(s["text"], add_special_tokens=False)
        if len(tokens) >= seq_len:
            all_ids.append(tokens[:seq_len])
        if len(all_ids) >= num_samples:
            break

    if not all_ids:
        raise RuntimeError(f"No C4 seqs with >= {seq_len} tokens")

    input_ids = torch.tensor(all_ids, dtype=torch.long, device=device)
    print(f"  C4 eval: {input_ids.shape[0]} seqs x {input_ids.shape[1]} tokens")

    with torch.no_grad():
        outputs = model(
            input_ids, use_cache=False,
            cache_position=torch.arange(seq_len, device=device)
        )
    shift_logits = outputs.logits[:, :-1].contiguous()
    shift_labels = input_ids[:, 1:].contiguous()
    loss = F.cross_entropy(
        shift_logits.view(-1, shift_logits.shape[-1]),
        shift_labels.view(-1),
        reduction="sum"
    )
    total_tokens = shift_labels.numel()
    return math.exp(loss.item() / total_tokens)


def main():
    sys.stdout = Tee(LOG_FILE)
    t_start = time.time()

    # === Phase 1: C4 Profiling ===
    print("=" * 60)
    print("[Phase 1] Profiling with C4 calibration data (16x512)...")
    print("=" * 60)
    t0 = time.time()

    profiler = FullBitwidthProfiler(
        model_path=MODEL,
        calibration_data=C4_CALIBRATION,
        device=DEVICE,
        num_samples=16,
        seq_len=512
    )
    c4_baseline_cal_ppl = profiler.compute_baseline_ppl()
    c4_raw_profiles = profiler.profile_all(bit_widths=(2, 4, 8))
    profile_time = time.time() - t0
    print(f"\nC4 profiling done in {profile_time:.1f}s")

    with open("llama_c4_profiling_results.json", "w") as f:
        json.dump({
            "model": MODEL,
            "calibration_source": "c4",
            "baseline_calibration_ppl": c4_baseline_cal_ppl,
            "num_samples": 16,
            "seq_len": 512,
            "profile_time_seconds": profile_time,
            "profiles": c4_raw_profiles,
        }, f, indent=2)
    print("Saved llama_c4_profiling_results.json")

    # === Phase 2: Solve MCKP with C4 profiles ===
    print(f"\n{'=' * 60}")
    print(f"[Phase 2] Solving constrained MCKP (budget={BUDGET}, max_2bit={MAX_2BIT})...")
    print("=" * 60)

    c4_profiles = enforce_monotonicity(c4_raw_profiles)
    c4_mckp = solve_mckp_constrained(
        c4_profiles, BUDGET, mode="quant_only",
        max_2bit=MAX_2BIT, l0_exclude_2bit=True
    )
    c4_uniform = uniform_quantization_baseline(c4_profiles, bits=4)

    print(f"C4 MCKP bit distribution: {c4_mckp['bit_distribution']}")
    print(f"C4 MCKP memory ratio: {c4_mckp['actual_memory_ratio']:.4f}")
    print(f"C4 MCKP n_2bit: {c4_mckp['n_2bit']}")

    # === Phase 3: Load WT2-calibrated profiles, re-solve with same constraints ===
    print(f"\n{'=' * 60}")
    print("[Phase 3] Loading WT2 hires profiles, solving MCKP with max_2bit=2...")
    print("=" * 60)

    with open(WT2_PROFILES_FILE) as f:
        wt2_data = json.load(f)
    wt2_raw_profiles = wt2_data["profiles"]
    wt2_profiles = enforce_monotonicity(wt2_raw_profiles)
    wt2_mckp = solve_mckp_constrained(
        wt2_profiles, BUDGET, mode="quant_only",
        max_2bit=MAX_2BIT, l0_exclude_2bit=True
    )

    print(f"WT2 MCKP bit distribution: {wt2_mckp['bit_distribution']}")
    print(f"WT2 MCKP memory ratio: {wt2_mckp['actual_memory_ratio']:.4f}")
    print(f"WT2 MCKP n_2bit: {wt2_mckp['n_2bit']}")

    # === Phase 4: Allocation agreement ===
    print(f"\n{'=' * 60}")
    print("[Phase 4] Allocation agreement analysis...")
    print("=" * 60)

    n_heads = 256
    agreement_rate, disagree_details = compute_agreement(
        wt2_mckp["allocation"], c4_mckp["allocation"]
    )
    n_agree = int(round(agreement_rate * n_heads))

    print(f"Agreement rate: {agreement_rate:.1%} ({n_agree}/{n_heads} heads)")
    print(f"Disagreements: {len(disagree_details)}")
    if disagree_details:
        print("\nDisagreement details:")
        for k, v in sorted(disagree_details.items()):
            print(f"  {k}: WT2={v['wt2']}, C4={v['c4']}")

    # === Phase 5: WikiText-2 PPL Eval ===
    print(f"\n{'=' * 60}")
    print("[Phase 5] WikiText-2 PPL evaluation...")
    print("=" * 60)

    model = profiler.model
    tokenizer = profiler.tokenizer
    t1 = time.time()

    print("\n  [5a] BF16 baseline...")
    bf16_wt2_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    print(f"  >>> BF16 WT2 PPL = {bf16_wt2_ppl:.4f}")

    print("\n  [5b] C4-calibrated MCKP...")
    orig = patch_attention(model, c4_mckp["allocation"])
    c4cal_wt2_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f"  >>> C4-cal MCKP WT2 PPL = {c4cal_wt2_ppl:.4f}")

    print("\n  [5c] WT2-calibrated MCKP...")
    orig = patch_attention(model, wt2_mckp["allocation"])
    wt2cal_wt2_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f"  >>> WT2-cal MCKP WT2 PPL = {wt2cal_wt2_ppl:.4f}")

    print("\n  [5d] Uniform 4-bit...")
    orig = patch_attention(model, c4_uniform["allocation"])
    uniform_wt2_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f"  >>> Uniform 4-bit WT2 PPL = {uniform_wt2_ppl:.4f}")

    wt2_eval_time = time.time() - t1

    # === Phase 6: C4 PPL Eval (cross-domain) ===
    print(f"\n{'=' * 60}")
    print("[Phase 6] C4 PPL evaluation (cross-domain)...")
    print("=" * 60)
    t2 = time.time()

    print("\n  [6a] BF16 baseline on C4...")
    bf16_c4_ppl = evaluate_ppl_on_c4(model, tokenizer, DEVICE, C4_CALIBRATION)
    print(f"  >>> BF16 C4 PPL = {bf16_c4_ppl:.4f}")

    print("\n  [6b] WT2-calibrated MCKP on C4...")
    orig = patch_attention(model, wt2_mckp["allocation"])
    wt2cal_c4_ppl = evaluate_ppl_on_c4(model, tokenizer, DEVICE, C4_CALIBRATION)
    restore_attention(model, orig)
    print(f"  >>> WT2-cal MCKP C4 PPL = {wt2cal_c4_ppl:.4f}")

    print("\n  [6c] C4-calibrated MCKP on C4...")
    orig = patch_attention(model, c4_mckp["allocation"])
    c4cal_c4_ppl = evaluate_ppl_on_c4(model, tokenizer, DEVICE, C4_CALIBRATION)
    restore_attention(model, orig)
    print(f"  >>> C4-cal MCKP C4 PPL = {c4cal_c4_ppl:.4f}")

    print("\n  [6d] Uniform 4-bit on C4...")
    orig = patch_attention(model, c4_uniform["allocation"])
    uniform_c4_ppl = evaluate_ppl_on_c4(model, tokenizer, DEVICE, C4_CALIBRATION)
    restore_attention(model, orig)
    print(f"  >>> Uniform 4-bit C4 PPL = {uniform_c4_ppl:.4f}")

    c4_eval_time = time.time() - t2
    total_time = time.time() - t_start

    # === Summary ===
    print(f"\n{'=' * 70}")
    print("CROSS-DATASET RESULTS — Llama-3.1-8B (budget=0.25, k=2)")
    print("=" * 70)
    print(f"\n{'Eval \\ Calibration':<30} {'WT2-cal':>12} {'C4-cal':>12} {'Uniform4':>12} {'BF16':>12}")
    print("-" * 78)
    print(f"{'WT2 test PPL':<30} {wt2cal_wt2_ppl:>12.4f} {c4cal_wt2_ppl:>12.4f} {uniform_wt2_ppl:>12.4f} {bf16_wt2_ppl:>12.4f}")
    print(f"{'C4 eval PPL':<30} {wt2cal_c4_ppl:>12.4f} {c4cal_c4_ppl:>12.4f} {uniform_c4_ppl:>12.4f} {bf16_c4_ppl:>12.4f}")
    print(f"\n{'Bit distribution (WT2-cal):':<30} {wt2_mckp['bit_distribution']}")
    print(f"{'Bit distribution (C4-cal):':<30} {c4_mckp['bit_distribution']}")
    print(f"\nAllocation agreement: {agreement_rate:.1%} ({n_agree}/{n_heads} heads)")
    print(f"WT2-cal delta over uniform (WT2): {uniform_wt2_ppl - wt2cal_wt2_ppl:+.4f}")
    print(f"C4-cal delta over uniform (WT2):  {uniform_wt2_ppl - c4cal_wt2_ppl:+.4f}")
    print(f"\nTiming: profile={profile_time:.1f}s, wt2_eval={wt2_eval_time:.1f}s, c4_eval={c4_eval_time:.1f}s, total={total_time:.1f}s")

    # === Save results ===
    results = {
        "experiment": "llama_c4_cross_dataset_eval",
        "model": MODEL,
        "model_name": "Llama-3.1-8B",
        "budget": BUDGET,
        "max_2bit": MAX_2BIT,
        "n_heads": n_heads,
        "c4_profiling": {
            "calibration_data": C4_CALIBRATION,
            "baseline_calibration_ppl": c4_baseline_cal_ppl,
            "num_samples": 16,
            "seq_len": 512,
            "profile_time_seconds": profile_time,
        },
        "c4_mckp": {
            "bit_distribution": c4_mckp["bit_distribution"],
            "memory_ratio": c4_mckp["actual_memory_ratio"],
            "total_distortion": c4_mckp["total_distortion"],
            "n_2bit": c4_mckp["n_2bit"],
            "allocation": c4_mckp["allocation"],
        },
        "wt2_mckp": {
            "bit_distribution": wt2_mckp["bit_distribution"],
            "memory_ratio": wt2_mckp["actual_memory_ratio"],
            "total_distortion": wt2_mckp["total_distortion"],
            "n_2bit": wt2_mckp["n_2bit"],
            "allocation": wt2_mckp["allocation"],
            "source_profiles": WT2_PROFILES_FILE,
        },
        "agreement": {
            "rate": agreement_rate,
            "n_agree": n_agree,
            "n_disagree": len(disagree_details),
            "disagree_details": disagree_details,
        },
        "ppl_results": {
            "bf16_wt2": bf16_wt2_ppl,
            "bf16_c4": bf16_c4_ppl,
            "wt2cal_wt2": wt2cal_wt2_ppl,
            "wt2cal_c4": wt2cal_c4_ppl,
            "c4cal_wt2": c4cal_wt2_ppl,
            "c4cal_c4": c4cal_c4_ppl,
            "uniform_wt2": uniform_wt2_ppl,
            "uniform_c4": uniform_c4_ppl,
        },
        "timing": {
            "profile_seconds": profile_time,
            "wt2_eval_seconds": wt2_eval_time,
            "c4_eval_seconds": c4_eval_time,
            "total_seconds": total_time,
        },
        "c4_profiles": c4_raw_profiles,
    }

    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved {RESULTS_FILE}")


if __name__ == "__main__":
    main()
