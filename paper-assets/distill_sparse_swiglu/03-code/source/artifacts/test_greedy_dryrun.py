"""Dry-run: verify TEAL greedy allocation on 3 calibration samples.

Usage:
    source /root/distill_sparse_swiglu/setup_env.sh
    cd /root/distill_sparse_swiglu
    CUDA_VISIBLE_DEVICES=0 python src/test_greedy_dryrun.py
"""

import sys
import os
import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from baselines import (
    teal_greedy_allocation_masks,
    wina_global_masks,
    wina_greedy_allocation_masks,
)


def main():
    model_path = "/root/autodl-tmp/models/llama-3.1-8b"
    device = torch.device("cuda:0")
    n_calib = 3
    seq_len = 512
    sparsity_target = 0.5

    print(f"Loading tokenizer from {model_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"Loading model ...")
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        device_map={"": device},
        attn_implementation="sdpa",
    )
    model.eval()

    print(f"Generating {n_calib} random calibration sequences (seq_len={seq_len}) ...")
    import random
    random.seed(42)
    vocab_size = tokenizer.vocab_size
    calib_ids = torch.tensor(
        [[random.randint(0, vocab_size - 1) for _ in range(seq_len)]
         for _ in range(n_calib)],
        dtype=torch.long, device=device,
    )

    # --- TEAL greedy allocation ---
    print(f"\n{'='*60}")
    print(f"TEAL greedy allocation (target={sparsity_target})")
    print(f"{'='*60}")
    t0 = time.time()
    greedy_masks = teal_greedy_allocation_masks(
        model, calib_ids, sparsity_target=sparsity_target,
        step_size=0.05, calib_batch_size=2, device=device,
    )
    dt = time.time() - t0
    print(f"\n  Time: {dt:.1f}s")

    print("\n  Verification:")
    n_layers = len(greedy_masks)
    sparsities = []
    for li in sorted(greedy_masks):
        sp = 1.0 - greedy_masks[li].mean().item()
        sparsities.append(sp)
    global_avg = sum(sparsities) / len(sparsities)
    max_sp = max(sparsities)
    min_sp = min(sparsities)
    print(f"    Layers: {n_layers}")
    print(f"    Global avg sparsity: {global_avg:.4f}")
    print(f"    Min layer sparsity:  {min_sp:.4f}")
    print(f"    Max layer sparsity:  {max_sp:.4f}")

    ok = True
    if max_sp >= 1.0:
        print("    FAIL: some layer at 100% sparsity!")
        ok = False
    if abs(global_avg - sparsity_target) > 0.05:
        print(f"    WARN: global avg {global_avg:.4f} deviates from target {sparsity_target}")
    if min_sp <= 0.0:
        n_zero = sum(1 for s in sparsities if s <= 0.0)
        print(f"    INFO: {n_zero} layers at 0% sparsity (kept dense)")

    if ok:
        print("    PASS: no layer at 100% sparsity")

    # --- WINA global ---
    print(f"\n{'='*60}")
    print(f"WINA global masks (target={sparsity_target})")
    print(f"{'='*60}")
    t0 = time.time()
    wina_masks = wina_global_masks(
        model, calib_ids, sparsity_target=sparsity_target,
        calib_batch_size=2,
    )
    dt = time.time() - t0
    print(f"  Time: {dt:.1f}s")
    for li in sorted(wina_masks):
        sp = 1.0 - wina_masks[li].mean().item()
        print(f"    Layer {li:2d}: {sp:.3f}")
    total_n = sum(m.numel() for m in wina_masks.values())
    total_z = sum((m == 0).sum().item() for m in wina_masks.values())
    print(f"    Model-level: {total_z / total_n:.3f}")

    # --- WINA greedy ---
    print(f"\n{'='*60}")
    print(f"WINA greedy allocation (target={sparsity_target})")
    print(f"{'='*60}")
    t0 = time.time()
    wina_g_masks = wina_greedy_allocation_masks(
        model, calib_ids, sparsity_target=sparsity_target,
        step_size=0.05, calib_batch_size=2, device=device,
    )
    dt = time.time() - t0
    print(f"  Time: {dt:.1f}s")
    for li in sorted(wina_g_masks):
        sp = 1.0 - wina_g_masks[li].mean().item()
        print(f"    Layer {li:2d}: {sp:.3f}")
    total_n = sum(m.numel() for m in wina_g_masks.values())
    total_z = sum((m == 0).sum().item() for m in wina_g_masks.values())
    print(f"    Model-level: {total_z / total_n:.3f}")

    print(f"\n{'='*60}")
    print("Dry-run complete.")


if __name__ == "__main__":
    main()
