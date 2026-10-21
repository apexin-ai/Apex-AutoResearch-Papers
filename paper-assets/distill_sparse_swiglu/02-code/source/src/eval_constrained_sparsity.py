"""Constrained-allocation eval: cap sparsity in a designated layer range.

Tests the causal hypothesis that late-layer starvation (L22-L28 receiving
~50% sparsity under global allocation) drives knowledge-task degradation.

Condition A (protect_late): cap L[cap_start..cap_end] sparsity <= cap. Excess
pruning budget is redistributed to remaining layers via a re-computed global
threshold so overall model sparsity matches sparsity_target.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from evaluate import _print_mask_stats
from benchmark_eval import (
    LM_EVAL_DEFAULTS,
    load_model_and_tokenizer,
    get_calibration_ids,
    setup_predictor,
    apply_static_masks,
    restore_forwards,
    run_wikitext2_ppl,
    run_c4_ppl,
    run_lm_eval_tasks,
    extract_key_metrics,
)

BASE_DIR = "/root/distill_sparse_swiglu"
DEFAULT_MODEL = "/root/autodl-tmp/models/llama-3.1-8b"


def compute_predictor_layer_scores(wrapper, input_ids, calib_batch_size=4):
    """Per-neuron mean sigmoid(predictor logit) across calibration tokens.

    Mirrors evaluate.teal_global_masks scoring, factored out so we can apply a
    custom allocation policy on top.
    """
    accum = {}
    n_batches = 0
    for start in range(0, input_ids.size(0), calib_batch_size):
        batch = input_ids[start:start + calib_batch_size]
        wrapper.forward_dense(batch, capture_intermediates=True)
        layer_inputs = wrapper.get_layer_inputs()
        with torch.no_grad():
            for li in range(len(wrapper.predictors)):
                if li not in layer_inputs:
                    continue
                pred = wrapper.predictors[li]
                pred_device = next(pred.parameters()).device
                logits = pred(layer_inputs[li].to(pred_device))
                scores = torch.sigmoid(logits).mean(dim=(0, 1))
                accum[li] = scores if li not in accum else accum[li] + scores
        n_batches += 1
    return {li: accum[li] / n_batches for li in sorted(accum)}


def _normalize_scores(layer_scores):
    """Per-layer mean normalization (matches evaluate._global_topk_masks)."""
    out = {}
    for li, s in layer_scores.items():
        s_f = s.float()
        mu = s_f.mean()
        out[li] = s_f / mu if mu > 1e-12 else s_f
    return out


def constrained_global_masks(layer_scores, sparsity_target, capped_layers, cap):
    """Global top-k with a per-layer sparsity cap on a designated layer set.

    Algorithm (threshold-level, not direct sparsity manipulation):
      1. Run vanilla global top-k → initial per-layer sparsity.
      2. For each layer in capped_layers whose initial sparsity > cap:
         replace its mask with per-layer top-k at sparsity = cap.
      3. Re-run global top-k on the remaining (uncapped) layers with the residual
         zero budget so the overall sparsity stays at sparsity_target.
    """
    normalized = _normalize_scores(layer_scores)
    n_per_layer = next(iter(normalized.values())).shape[0]
    n_total = sum(s.numel() for s in normalized.values())
    target_zeros = int(round(sparsity_target * n_total))

    all_s = torch.cat([normalized[li] for li in sorted(normalized)])
    num_keep_initial = n_total - target_zeros
    if num_keep_initial <= 0 or num_keep_initial >= n_total:
        raise ValueError(f"Degenerate sparsity_target={sparsity_target}")
    thr_init = torch.topk(all_s, num_keep_initial).values[-1]
    initial_sparsity = {
        li: 1.0 - (normalized[li] >= thr_init).float().mean().item()
        for li in normalized
    }

    capped_set = {int(li) for li in capped_layers}
    fixed = set()
    masks = {}
    zeros_fixed = 0
    for li in capped_set:
        if li not in normalized:
            continue
        if initial_sparsity[li] > cap + 1e-9:
            s = normalized[li]
            num_keep_l = int(round(n_per_layer * (1.0 - cap)))
            thr_l = torch.topk(s, num_keep_l).values[-1]
            masks[li] = (s >= thr_l).to(torch.bfloat16)
            zeros_fixed += int((masks[li] == 0).sum().item())
            fixed.add(li)

    remaining = [li for li in sorted(normalized) if li not in fixed]
    rem_scores = torch.cat([normalized[li] for li in remaining])
    n_rem = rem_scores.numel()
    target_zeros_rem = target_zeros - zeros_fixed

    if target_zeros_rem <= 0:
        for li in remaining:
            masks[li] = torch.ones_like(normalized[li], dtype=torch.bfloat16)
    elif target_zeros_rem >= n_rem:
        for li in remaining:
            masks[li] = torch.zeros_like(normalized[li], dtype=torch.bfloat16)
    else:
        num_keep_rem = n_rem - target_zeros_rem
        thr_rem = torch.topk(rem_scores, num_keep_rem).values[-1]
        for li in remaining:
            masks[li] = (normalized[li] >= thr_rem).to(torch.bfloat16)

    info = {
        "initial_sparsity": initial_sparsity,
        "fixed_layers": sorted(fixed),
        "zeros_fixed": int(zeros_fixed),
        "target_zeros": int(target_zeros),
    }
    return masks, info


def parse_args():
    p = argparse.ArgumentParser(
        description="Constrained per-layer sparsity allocation eval"
    )
    p.add_argument("--model_name_or_path", type=str, default=DEFAULT_MODEL)
    p.add_argument("--checkpoint", type=str, required=True,
                   help="Path to predictor .pt checkpoint")
    p.add_argument("--constraint_type", type=str, default="protect_late",
                   choices=["protect_late"],
                   help="Which constraint to apply. protect_late caps L22-L28 sparsity")
    p.add_argument("--cap_start", type=int, default=22,
                   help="First layer index in capped range (inclusive)")
    p.add_argument("--cap_end", type=int, default=28,
                   help="Last layer index in capped range (inclusive)")
    p.add_argument("--cap", type=float, default=0.30,
                   help="Max per-layer sparsity for capped range")
    p.add_argument("--sparsity_target", type=float, default=0.30,
                   help="Overall model sparsity target")
    p.add_argument("--tasks", type=str, default="wikitext2,arc_challenge,mmlu,gsm8k",
                   help="Comma-separated task list")
    p.add_argument("--seq_len", type=int, default=2048)
    p.add_argument("--calibration_samples", type=int, default=32)
    p.add_argument("--calibration_data", type=str, default="wikitext2",
                   choices=["wikitext2", "c4"])
    p.add_argument("--batch_size", type=int, default=8)
    p.add_argument("--bottleneck_size", type=int, default=128)
    p.add_argument("--max_eval_samples", type=int, default=None)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--exp_id", type=str, default=None,
                   help="Output subdir under results/benchmark/. "
                        "Defaults to constraint_<type>_kl<sp>_s42.")
    return p.parse_args()


def main():
    args = parse_args()
    device = torch.device(f"cuda:{args.gpu}")

    tasks = [t.strip() for t in args.tasks.split(",")]
    lm_eval_tasks = [t for t in tasks if t in LM_EVAL_DEFAULTS]
    do_wikitext2 = "wikitext2" in tasks
    do_c4 = "c4" in tasks
    unknown = [t for t in tasks
               if t not in ("wikitext2", "c4") and t not in LM_EVAL_DEFAULTS]
    if unknown:
        print(f"Warning: unknown tasks ignored: {unknown}")

    exp_id = args.exp_id or (
        f"constraint_{args.constraint_type}_kl{int(args.sparsity_target * 100)}_s42"
    )
    out_dir = Path(BASE_DIR) / "results" / "benchmark" / exp_id
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading model: {args.model_name_or_path}")
    model, tokenizer = load_model_and_tokenizer(
        args.model_name_or_path, device, multi_gpu=False
    )

    ckpt_path = args.checkpoint
    if not os.path.isabs(ckpt_path):
        ckpt_path = os.path.join(BASE_DIR, ckpt_path)
    print(f"Loading predictor: {ckpt_path}")
    wrapper = setup_predictor(model, ckpt_path, args.bottleneck_size, device)

    print(f"Loading calibration data ({args.calibration_data}, "
          f"{args.calibration_samples} samples) ...")
    calib_ids = get_calibration_ids(
        tokenizer, args.seq_len, args.calibration_samples, device,
        dataset=args.calibration_data,
    )

    print("Computing predictor layer importance scores ...")
    layer_scores = compute_predictor_layer_scores(wrapper, calib_ids)

    capped_layers = list(range(args.cap_start, args.cap_end + 1))
    print(f"Constraint: {args.constraint_type}, capped_layers={capped_layers}, "
          f"cap={args.cap}, sparsity_target={args.sparsity_target}")
    masks, info = constrained_global_masks(
        layer_scores, args.sparsity_target, capped_layers, args.cap
    )

    print("\nInitial (uncapped) per-layer sparsity under global top-k:")
    for li in sorted(info["initial_sparsity"]):
        marker = "  <-- capped" if li in info["fixed_layers"] else ""
        print(f"  Layer {li:2d}: {info['initial_sparsity'][li]:.3f}{marker}")
    print(f"  Capped layers (sparsity > {args.cap}): {info['fixed_layers']}")
    print(f"  Zeros fixed by cap: {info['zeros_fixed']} "
          f"/ target_zeros={info['target_zeros']}")

    final_sp = _print_mask_stats(f"constrained-{args.constraint_type}", masks)

    # Switch wrapper from per-token to static masks for benchmark eval
    wrapper.sparse_mode = False
    saved_forwards = apply_static_masks(model, masks, device)

    results = {
        "exp_id": exp_id,
        "config": {k: v for k, v in vars(args).items()},
        "mode": {
            "mode": f"constrained_{args.constraint_type}",
            "checkpoint": ckpt_path,
            "sparsity_target": args.sparsity_target,
            "cap_range": [args.cap_start, args.cap_end],
            "cap": args.cap,
        },
        "mask_info": {
            "actual_model_sparsity": float(final_sp),
            "per_layer_sparsity": {
                int(li): float(1.0 - masks[li].mean().item())
                for li in sorted(masks)
            },
            "initial_per_layer_sparsity": {
                int(li): float(v) for li, v in info["initial_sparsity"].items()
            },
            "fixed_layers": info["fixed_layers"],
        },
        "metrics": {},
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    if do_wikitext2:
        print("\n--- WikiText-2 PPL ---")
        t0 = time.time()
        ppl = run_wikitext2_ppl(
            model, tokenizer, args.seq_len, device, args.max_eval_samples
        )
        elapsed = time.time() - t0
        print(f"  PPL = {ppl:.4f}  ({elapsed:.1f}s)")
        results["metrics"]["wikitext2_ppl"] = round(ppl, 4)

    if do_c4:
        print("\n--- C4 PPL ---")
        t0 = time.time()
        ppl = run_c4_ppl(
            model, tokenizer, args.seq_len, device, args.max_eval_samples
        )
        elapsed = time.time() - t0
        print(f"  PPL = {ppl:.4f}  ({elapsed:.1f}s)")
        results["metrics"]["c4_ppl"] = round(ppl, 4)

    if lm_eval_tasks:
        print(f"\n--- lm-eval: {lm_eval_tasks} ---")
        t0 = time.time()
        raw = run_lm_eval_tasks(
            model, tokenizer, lm_eval_tasks, args.batch_size, device
        )
        elapsed = time.time() - t0
        summary = extract_key_metrics(raw)
        results["metrics"]["lm_eval"] = summary
        results["metrics"]["lm_eval_raw"] = raw
        print(f"  Completed in {elapsed:.1f}s")
        for task_name, m in summary.items():
            line = ", ".join(
                f"{k}={v:.4f}" if isinstance(v, float) else f"{k}={v}"
                for k, v in m.items() if not k.endswith("_stderr")
            )
            print(f"  {task_name}: {line}")

    if saved_forwards:
        restore_forwards(model, saved_forwards)

    out_path = out_dir / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
