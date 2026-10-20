#!/usr/bin/env python3
# GSM8K Profiling — PACS compound sparsity cross-dataset validation (v2).
#
# Parameters (must match MATH-500 main experiment):
#   - n=50, seed=42, min_phase_length=10
#   - Data: gsm8k_test.json (full GSM8K test set, random 50 samples)
#   - save_generations: always enabled when flag is set
#
# Additions over v1:
#   - --gpu flag for explicit GPU assignment
#   - --save_generations: saves generation text + ground truth
#   - Dense accuracy: extracts #### answers, compares with ground truth
#   - Phase segmentation sanity check: n_phases distribution, phase sizes

from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import random
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_SCRIPT_DIR)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

import numpy as np
import torch

from pacs.utils.metrics import compute_perplexity, ppl_from_cached_losses
from pacs.profiling.interaction_index import (
    InteractionIndexCalculator,
    _HeadMaskHook,
    bootstrap_interaction_index,
)
from pacs.profiling.phase_segmentation import PhaseSegmenter
from pacs.profiling.alt_segmentation import segment_by_quantile, to_phase_annotation

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("run_profiling_gsm8k")

DEFAULT_SPARSITY_LEVELS = [0.1, 0.2, 0.3]
N_BOOTSTRAP = 1000
MIN_SEGMENTS_WARN = 20
SEED = 42
GSM8K_N_SAMPLE = 50


# ---------------------------------------------------------------------------
# Model / data loading
# ---------------------------------------------------------------------------

def load_model_and_tokenizer(model_path: str, device: str = "cuda"):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    logger.info("Loading tokenizer from %s", model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    logger.info("Loading model from %s", model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map=device,
        trust_remote_code=True,
        attn_implementation="eager",
    )
    model.eval()
    return model, tokenizer


DEFAULT_GSM8K_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "gsm8k_test.json")


def load_gsm8k_data(
    data_path: str = DEFAULT_GSM8K_PATH,
    n_sample: int = GSM8K_N_SAMPLE,
    seed: int = SEED,
) -> List[Dict[str, Any]]:
    """Load GSM8K test split from local JSON and random-sample n problems."""
    logger.info("Loading GSM8K from %s", data_path)
    with open(data_path) as f:
        raw = json.load(f)
    logger.info("GSM8K test split: %d problems total", len(raw))

    rng = random.Random(seed)
    indices = rng.sample(range(len(raw)), min(n_sample, len(raw)))
    indices.sort()

    data = []
    for i in indices:
        item = raw[i]
        answer_text = item["answer"]
        final_answer = ""
        if "####" in answer_text:
            final_answer = answer_text.split("####")[-1].strip()
        data.append({
            "id": f"gsm8k_test/{i}",
            "problem": item["question"],
            "solution": answer_text,
            "answer": final_answer,
            "dataset": "gsm8k",
            "original_index": i,
        })

    logger.info("Sampled %d GSM8K problems (seed=%d)", len(data), seed)
    return data


def extract_gsm8k_answer(text: str) -> Optional[str]:
    """Extract the final numerical answer from GSM8K generation (#### NUMBER format)."""
    match = re.findall(r"####\s*([+-]?[\d,]+\.?\d*)", text)
    if match:
        return match[-1].replace(",", "")
    match = re.findall(r"\\boxed\{([+-]?[\d,]+\.?\d*)\}", text)
    if match:
        return match[-1].replace(",", "")
    match = re.findall(r"(?:answer|result)\s*(?:is|=)\s*\$?\s*([+-]?[\d,]+\.?\d*)", text, re.IGNORECASE)
    if match:
        return match[-1].replace(",", "")
    return None


def normalize_number(s: str) -> Optional[float]:
    """Normalize a number string for comparison."""
    if s is None:
        return None
    s = s.strip().replace(",", "").replace("$", "").replace("%", "")
    try:
        return float(s)
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Phase-conditioned perplexity
# ---------------------------------------------------------------------------

def compute_conditioned_perplexities(
    ii_calc: InteractionIndexCalculator,
    input_ids: torch.Tensor,
    phase_token_indices: List[int],
    attn_head_mask: torch.Tensor,
    kv_mask: torch.Tensor,
    dense_ce_losses: torch.Tensor,
    seq_len: int,
) -> Dict[str, float]:
    """Run 3 sparse forward passes; dense ppl from cached CE losses."""
    ppl_dense = ppl_from_cached_losses(dense_ce_losses, phase_token_indices, seq_len)

    ppl_attn = ii_calc.forward_with_sparse_config(
        input_ids, attn_head_mask=attn_head_mask,
        phase_token_indices=phase_token_indices,
    )
    ppl_kv = ii_calc.forward_with_sparse_config(
        input_ids, kv_mask=kv_mask,
        phase_token_indices=phase_token_indices,
    )
    ppl_both = ii_calc.forward_with_sparse_config(
        input_ids, attn_head_mask=attn_head_mask, kv_mask=kv_mask,
        phase_token_indices=phase_token_indices,
    )

    return {"dense": ppl_dense, "attn": ppl_attn, "kv": ppl_kv, "both": ppl_both}


# ---------------------------------------------------------------------------
# Pass/fail judgment (OR logic)
# ---------------------------------------------------------------------------

def evaluate_pass_fail(
    ii_results: Dict[str, Dict[str, Dict[str, float]]],
) -> Dict[str, Any]:
    phase_names = list(ii_results.keys())
    ci_pass = False
    ci_detail = ""
    sign_pass = False
    sign_detail = ""

    all_levels = set()
    for pdata in ii_results.values():
        all_levels.update(pdata.keys())

    for level_str in sorted(all_levels):
        phase_cis = {}
        for pname in phase_names:
            entry = ii_results.get(pname, {}).get(level_str)
            if entry is None:
                continue
            phase_cis[pname] = (entry["ci_low"], entry["ci_high"], entry["mean"])

        for (p1, c1), (p2, c2) in combinations(phase_cis.items(), 2):
            if not (np.isfinite(c1[0]) and np.isfinite(c1[1]) and np.isfinite(c2[0]) and np.isfinite(c2[1])):
                continue
            if c1[1] < c2[0] or c2[1] < c1[0]:
                ci_pass = True
                ci_detail = f"{p1} vs {p2} CI non-overlapping at {level_str}"
            sign1 = "pos" if c1[0] > 0 else ("neg" if c1[1] < 0 else "zero")
            sign2 = "pos" if c2[0] > 0 else ("neg" if c2[1] < 0 else "zero")
            if {sign1, sign2} == {"pos", "neg"}:
                sign_pass = True
                sign_detail = f"{p1} II{'>' if sign1 == 'pos' else '<'}0, {p2} II{'>' if sign2 == 'pos' else '<'}0 at {level_str}"

    overall = "PASS" if (ci_pass or sign_pass) else "FAIL"
    return {
        "ci_overlap_test": {"pass": ci_pass, "details": ci_detail},
        "sign_reversal_test": {"pass": sign_pass, "details": sign_detail},
        "overall": overall,
    }


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

@torch.no_grad()
def run_profiling(args: argparse.Namespace) -> None:
    # Device selection
    if args.gpu is not None:
        device = f"cuda:{args.gpu}"
    else:
        device = args.device

    torch.manual_seed(SEED)
    sparsity_levels = args.sparsity_levels
    use_importance = (args.masking_method == "importance")
    model, tokenizer = load_model_and_tokenizer(args.model_path, device=device)

    data = load_gsm8k_data(data_path=args.data_path, n_sample=GSM8K_N_SAMPLE, seed=SEED)
    if args.max_problems is not None and args.max_problems < len(data):
        data = data[: args.max_problems]
        logger.info("Truncated to %d problems (--max_problems)", len(data))
    logger.info("Processing %d GSM8K problems", len(data))

    segmenter = PhaseSegmenter(
        bandwidth=args.kde_bandwidth,
        min_phase_length=args.min_phase_length,
    )
    ii_calc = InteractionIndexCalculator(model, tokenizer, device=device)

    os.makedirs(args.output_dir, exist_ok=True)
    warnings_list: List[str] = []

    # Accumulators
    ii_per_phase_level: Dict[str, Dict[str, List[float]]] = defaultdict(
        lambda: defaultdict(list)
    )
    ppl_per_phase_level: Dict[str, Dict[str, Dict[str, List[float]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )
    phase_token_counts: Dict[str, List[int]] = defaultdict(list)
    phase_segment_counts: Dict[str, int] = defaultdict(int)

    all_problem_diagnostics: List[Dict[str, Any]] = []
    all_sparsity_values: List[float] = []

    per_problem_ii_acc: Dict[str, Dict[int, Dict[str, Any]]] = defaultdict(dict)

    # Generation + accuracy tracking
    generation_records: List[Dict[str, Any]] = []
    dense_accuracy_records: List[Dict[str, Any]] = []

    # Locate attention layers once
    attn_layers = _HeadMaskHook._find_attention_layers(model)
    if not attn_layers:
        raise RuntimeError("Could not find attention layers in model")
    last_attn_layer = attn_layers[-1]

    for idx, item in enumerate(data):
        problem_text = item.get("problem", item.get("question", ""))
        problem_id = item.get("id", str(idx))
        ground_truth = item.get("answer", "")
        logger.info("[%d/%d] Processing problem %s", idx + 1, len(data), problem_id)

        prompt = (
            f"Solve the following math problem step by step.\n\n"
            f"Problem: {problem_text}\n\nSolution:"
        )
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        prompt_len = inputs["input_ids"].shape[1]

        # --- Hook-based per-step sparsity ---
        step_sparsities: List[float] = []

        def _enable_attn_pre_hook(module, args, kwargs):
            kwargs = dict(kwargs)
            kwargs["output_attentions"] = True
            return args, kwargs

        def _capture_sparsity_hook(module, input, output):
            if isinstance(output, tuple) and len(output) > 1 and output[1] is not None:
                attn_w = output[1]
                if attn_w.shape[-2] == 1:
                    step_sparsities.append(
                        segmenter.compute_step_sparsity(attn_w[0])
                    )
                return (output[0],) + (None,) + output[2:]

        pre_h = last_attn_layer.register_forward_pre_hook(
            _enable_attn_pre_hook, with_kwargs=True
        )
        post_h = last_attn_layer.register_forward_hook(_capture_sparsity_hook)

        try:
            outputs = model.generate(
                **inputs,
                max_new_tokens=args.max_new_tokens,
                do_sample=False,
            )
        finally:
            pre_h.remove()
            post_h.remove()

        full_ids = outputs.sequences if hasattr(outputs, "sequences") else outputs
        if full_ids.dim() == 1:
            full_ids = full_ids.unsqueeze(0)

        # Capture generation text
        gen_ids = full_ids[0, prompt_len:]
        gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)

        # Dense accuracy: extract answer from generation, compare with ground truth
        model_answer = extract_gsm8k_answer(gen_text)
        gt_num = normalize_number(ground_truth)
        model_num = normalize_number(model_answer) if model_answer else None
        correct = 1 if (gt_num is not None and model_num is not None and abs(gt_num - model_num) < 1e-6) else 0

        dense_accuracy_records.append({
            "problem_id": problem_id,
            "ground_truth": ground_truth,
            "model_answer": model_answer if model_answer else "",
            "correct": correct,
        })

        if args.save_generations:
            generation_records.append({
                "id": problem_id,
                "generation": gen_text,
                "ground_truth": item.get("solution", ""),
                "ground_truth_answer": ground_truth,
                "model_answer": model_answer if model_answer else "",
                "correct": correct,
            })

        logger.info(
            "  Dense accuracy: GT=%s, Model=%s, Correct=%d",
            ground_truth, model_answer, correct,
        )

        if len(step_sparsities) == 0:
            logger.warning("No generation steps for problem %s, skipping.", problem_id)
            warnings_list.append(f"No generation steps for {problem_id}")
            continue

        # Phase segmentation
        gen_sparsity = np.array(step_sparsities)
        quant_seg = segment_by_quantile(gen_sparsity, n_groups=3)
        annotation = to_phase_annotation(
            quant_seg.assignments,
            quant_seg.group_names,
            gen_sparsity,
            offset=0,
            min_phase_length=args.min_phase_length,
        )

        problem_diagnostics = {
            "problem_id": problem_id,
            "sparsity_values": [float(s) for s in step_sparsities],
            "n_tokens": len(step_sparsities),
            "sparsity_mean": float(np.mean(gen_sparsity)),
            "sparsity_std": float(np.std(gen_sparsity)),
            "sparsity_min": float(np.min(gen_sparsity)),
            "sparsity_max": float(np.max(gen_sparsity)),
            "n_phases_detected": len(annotation.phases),
            "phase_sizes": [p.end - p.start for p in annotation.phases],
            "phase_names": [p.name for p in annotation.phases],
            "segmentation_method": "quantile",
            "quantile_boundaries": quant_seg.boundaries.tolist(),
            "quantile_group_stats": quant_seg.group_stats,
        }
        all_problem_diagnostics.append(problem_diagnostics)
        all_sparsity_values.extend(problem_diagnostics["sparsity_values"])

        # Offset phase indices to full_ids coordinates
        for phase in annotation.phases:
            phase.start += prompt_len
            phase.end += prompt_len

        if use_importance:
            dense_ce_losses, head_importance, kv_importance = (
                ii_calc.compute_dense_forward_with_importance(full_ids)
            )
        else:
            dense_ce_losses = ii_calc.compute_dense_ce_losses(full_ids)
            head_importance = None
            kv_importance = None
        full_seq_len = full_ids.shape[1]

        for phase in annotation.phases:
            phase_token_counts[phase.name].append(len(phase.token_indices))
            phase_segment_counts[phase.name] += 1

        num_layers, num_heads = ii_calc._get_model_dims()

        for level in sparsity_levels:
            level_str = str(level)
            attn_head_mask = InteractionIndexCalculator._select_heads_to_mask(
                num_layers, num_heads, level,
                importance=head_importance,
            )
            kv_mask = InteractionIndexCalculator._select_kv_to_evict(
                full_seq_len, level,
                importance=kv_importance,
            )

            if idx not in per_problem_ii_acc[level_str]:
                per_problem_ii_acc[level_str][idx] = {
                    "problem_idx": idx,
                    "problem_id": problem_id,
                }

            phase_ii_vals_for_problem: Dict[str, List[float]] = defaultdict(list)
            phase_seg_for_problem: Dict[str, int] = defaultdict(int)

            for phase in annotation.phases:
                ppls = compute_conditioned_perplexities(
                    ii_calc, full_ids, phase.token_indices,
                    attn_head_mask, kv_mask,
                    dense_ce_losses, full_seq_len,
                )
                for cond, val in ppls.items():
                    ppl_per_phase_level[phase.name][level_str][cond].append(val)

                ppl_d = ppls["dense"]
                if ppl_d > 0:
                    r_attn = ppls["attn"] / ppl_d
                    r_kv = ppls["kv"] / ppl_d
                    r_both = ppls["both"] / ppl_d
                    ii_val = r_both - r_attn - r_kv + 1
                else:
                    ii_val = float("nan")
                ii_per_phase_level[phase.name][level_str].append(ii_val)

                phase_key = phase.name.replace("_sparsity", "")
                if not np.isnan(ii_val):
                    phase_ii_vals_for_problem[phase_key].append(ii_val)
                phase_seg_for_problem[phase_key] += 1

            rec = per_problem_ii_acc[level_str][idx]
            for pk in ["high", "mid", "low"]:
                vals = phase_ii_vals_for_problem.get(pk, [])
                rec[f"ii_{pk}"] = float(np.mean(vals)) if vals else None
                rec[f"n_segments_{pk}"] = phase_seg_for_problem.get(pk, 0)

        logger.info(
            "  -> %d phases, boundaries at %s",
            len(annotation.phases), annotation.boundaries,
        )

    # ------------------------------------------------------------------
    # Aggregate: per-phase stats
    # ------------------------------------------------------------------
    phase_stats: Dict[str, Any] = {}
    for pname in sorted(phase_token_counts.keys()):
        n_tokens = sum(phase_token_counts[pname])
        n_segments = phase_segment_counts[pname]
        phase_stats[pname] = {"n_tokens": n_tokens, "n_segments": n_segments}
        if n_segments < MIN_SEGMENTS_WARN:
            msg = f"Phase '{pname}' has only {n_segments} segments (< {MIN_SEGMENTS_WARN})"
            warnings_list.append(msg)
            logger.warning(msg)

    # ------------------------------------------------------------------
    # Aggregate: bootstrap CI for II and mean perplexity
    # ------------------------------------------------------------------
    ii_out: Dict[str, Dict[str, Dict[str, float]]] = {}
    for pname in sorted(ii_per_phase_level.keys()):
        ii_out[pname] = {}
        for level_str in sorted(ii_per_phase_level[pname].keys()):
            samples = [v for v in ii_per_phase_level[pname][level_str] if not np.isnan(v)]
            if len(samples) < 2:
                ii_out[pname][level_str] = {
                    "mean": float(np.mean(samples)) if samples else float("nan"),
                    "ci_low": float("nan"),
                    "ci_high": float("nan"),
                }
                warnings_list.append(
                    f"Phase '{pname}' at {level_str}: only {len(samples)} valid II samples, CI unavailable"
                )
            else:
                mean, ci_low, ci_high = bootstrap_interaction_index(
                    samples, n_resamples=N_BOOTSTRAP, seed=SEED,
                )
                ii_out[pname][level_str] = {
                    "mean": mean, "ci_low": ci_low, "ci_high": ci_high,
                }

    perplexity_out: Dict[str, Dict[str, Dict[str, float]]] = {}
    for pname in sorted(ppl_per_phase_level.keys()):
        perplexity_out[pname] = {}
        for level_str in sorted(ppl_per_phase_level[pname].keys()):
            cond_ppls = ppl_per_phase_level[pname][level_str]
            perplexity_out[pname][level_str] = {
                cond: round(float(np.mean(vals)), 4)
                for cond, vals in cond_ppls.items()
            }

    # ------------------------------------------------------------------
    # Pass/fail
    # ------------------------------------------------------------------
    pass_fail = evaluate_pass_fail(ii_out)

    # ------------------------------------------------------------------
    # per_problem_ii (extract_table2.py compatible)
    # ------------------------------------------------------------------
    per_problem_ii_out: Dict[str, List[Dict]] = {}
    for level_str in sorted(per_problem_ii_acc.keys()):
        records = per_problem_ii_acc[level_str]
        per_problem_ii_out[level_str] = [records[k] for k in sorted(records.keys())]

    # ------------------------------------------------------------------
    # Diagnostics
    # ------------------------------------------------------------------
    diagnostics_section: Dict[str, Any] = {
        "per_problem_sparsity": all_problem_diagnostics,
    }
    if all_sparsity_values:
        counts, bin_edges = np.histogram(all_sparsity_values, bins=50)
        diagnostics_section["global_sparsity_histogram"] = {
            "bins": bin_edges.tolist(),
            "counts": counts.tolist(),
        }

    # ------------------------------------------------------------------
    # Dense accuracy summary
    # ------------------------------------------------------------------
    n_correct = sum(r["correct"] for r in dense_accuracy_records)
    n_total = len(dense_accuracy_records)
    dense_accuracy_summary = {
        "n_correct": n_correct,
        "n_total": n_total,
        "accuracy": round(n_correct / n_total, 4) if n_total > 0 else 0.0,
    }
    logger.info(
        "Dense accuracy: %d/%d = %.2f%%",
        n_correct, n_total, dense_accuracy_summary["accuracy"] * 100,
    )

    # ------------------------------------------------------------------
    # Phase segmentation sanity check
    # ------------------------------------------------------------------
    n_phases_list = [d["n_phases_detected"] for d in all_problem_diagnostics]
    all_phase_sizes = []
    for d in all_problem_diagnostics:
        all_phase_sizes.extend(d["phase_sizes"])

    sanity_check = {
        "n_problems_processed": len(all_problem_diagnostics),
        "n_phases_detected": {
            "values": n_phases_list,
            "mean": round(float(np.mean(n_phases_list)), 2) if n_phases_list else 0,
            "median": round(float(np.median(n_phases_list)), 2) if n_phases_list else 0,
            "min": int(min(n_phases_list)) if n_phases_list else 0,
            "max": int(max(n_phases_list)) if n_phases_list else 0,
            "std": round(float(np.std(n_phases_list)), 2) if n_phases_list else 0,
        },
        "phase_sizes": {
            "values": all_phase_sizes,
            "mean": round(float(np.mean(all_phase_sizes)), 2) if all_phase_sizes else 0,
            "median": round(float(np.median(all_phase_sizes)), 2) if all_phase_sizes else 0,
            "min": int(min(all_phase_sizes)) if all_phase_sizes else 0,
            "max": int(max(all_phase_sizes)) if all_phase_sizes else 0,
        },
        "segmentation_degradation": {},
    }

    # Check for degradation: problems with only 1-2 phases
    n_few_phases = sum(1 for n in n_phases_list if n <= 2)
    pct_few = round(n_few_phases / len(n_phases_list) * 100, 1) if n_phases_list else 0
    sanity_check["segmentation_degradation"] = {
        "n_problems_leq_2_phases": n_few_phases,
        "pct_problems_leq_2_phases": pct_few,
        "is_degraded": pct_few > 50,
        "note": "DEGRADED: >50% problems have <=2 phases" if pct_few > 50
                else "OK: segmentation appears stable",
    }

    # Histogram of n_phases
    if n_phases_list:
        phase_counts = defaultdict(int)
        for n in n_phases_list:
            phase_counts[n] += 1
        sanity_check["n_phases_histogram"] = dict(sorted(phase_counts.items()))

    # Save sanity check
    sanity_path = os.path.join(args.output_dir, "phase_sanity_check.json")
    with open(sanity_path, "w") as f:
        json.dump(sanity_check, f, indent=2)
    logger.info("Phase sanity check saved to %s", sanity_path)

    # Save dense accuracy CSV
    acc_csv_path = os.path.join(args.output_dir, "dense_accuracy.csv")
    with open(acc_csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["problem_id", "ground_truth", "model_answer", "correct"])
        writer.writeheader()
        writer.writerows(dense_accuracy_records)
    logger.info("Dense accuracy CSV saved to %s", acc_csv_path)

    # ------------------------------------------------------------------
    # Assemble output
    # ------------------------------------------------------------------
    output = {
        "config": {
            "model": args.model_path,
            "data_path": args.data_path,
            "sparsity_levels": sparsity_levels,
            "masking_method": args.masking_method,
            "head_importance_metric": "attention_frobenius_norm" if use_importance else "none",
            "kv_importance_metric": "cumulative_attention_received" if use_importance else "none",
            "segmentation_method": "quantile",
            "min_phase_length": args.min_phase_length,
            "n_bootstrap": N_BOOTSTRAP,
            "n_problems": len(data),
            "seed": SEED,
        },
        "phase_stats": phase_stats,
        "perplexity": perplexity_out,
        "interaction_index": ii_out,
        "pass_fail": pass_fail,
        "per_problem_ii": per_problem_ii_out,
        "dense_accuracy": dense_accuracy_summary,
        "phase_sanity_check": sanity_check,
        "warnings": warnings_list,
        "diagnostics": diagnostics_section,
    }

    out_path = os.path.join(args.output_dir, "profiling_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Results saved to %s", out_path)

    # Save generations
    if args.save_generations and generation_records:
        gen_path = os.path.join(args.output_dir, "generations.json")
        with open(gen_path, "w") as f:
            json.dump(generation_records, f, indent=2, ensure_ascii=False)
        logger.info("Saved %d generations to %s", len(generation_records), gen_path)

    # ------------------------------------------------------------------
    # Print summary
    # ------------------------------------------------------------------
    print(f"\n{'='*60}")
    print(f"PACS GSM8K Profiling Complete — {len(data)} problems")
    print(f"{'='*60}")
    print(f"  Dense accuracy: {n_correct}/{n_total} = {dense_accuracy_summary['accuracy']*100:.1f}%")
    print()
    for pname, stats in phase_stats.items():
        print(f"  {pname}: {stats['n_tokens']} tokens, {stats['n_segments']} segments")
    print()
    for pname in sorted(ii_out.keys()):
        for level_str in sorted(ii_out[pname].keys()):
            e = ii_out[pname][level_str]
            print(
                f"  II[{pname}, {level_str}]: "
                f"mean={e['mean']:+.4f}  95%CI=[{e['ci_low']:+.4f}, {e['ci_high']:+.4f}]"
            )
    print(f"\nVerdict: {pass_fail['overall']}")
    if pass_fail["ci_overlap_test"]["pass"]:
        print(f"  CI overlap test: {pass_fail['ci_overlap_test']['details']}")
    if pass_fail["sign_reversal_test"]["pass"]:
        print(f"  Sign reversal:   {pass_fail['sign_reversal_test']['details']}")
    print()
    sc = sanity_check["segmentation_degradation"]
    print(f"  Phase sanity: {sc['n_problems_leq_2_phases']}/{len(n_phases_list)} problems with <=2 phases ({sc['pct_problems_leq_2_phases']}%)")
    print(f"  Status: {sc['note']}")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="PACS Phase Profiling — GSM8K cross-dataset validation"
    )
    parser.add_argument(
        "--model_path", type=str, required=True,
        help="Path or HF model ID for the causal LM",
    )
    parser.add_argument(
        "--data_path", type=str, default=DEFAULT_GSM8K_PATH,
        help=f"Path to GSM8K JSON (default: {DEFAULT_GSM8K_PATH})",
    )
    parser.add_argument(
        "--output_dir", type=str, default="./gsm8k_profiling/output",
        help="Directory for output JSON",
    )
    parser.add_argument(
        "--device", type=str, default=None,
        help="Device: cuda / cpu / cuda:0 (default: auto-detect)",
    )
    parser.add_argument(
        "--max_new_tokens", type=int, default=2048,
        help="Max tokens to generate per problem (default: 2048)",
    )
    parser.add_argument(
        "--max_problems", type=int, default=None,
        help="Limit number of problems (default: all 50)",
    )
    parser.add_argument(
        "--kde_bandwidth", type=str, default="scott",
        help="KDE bandwidth: scott / silverman / float (default: scott)",
    )
    parser.add_argument(
        "--min_phase_length", type=int, default=10,
        help="Min tokens per phase segment (default: 10)",
    )
    parser.add_argument(
        "--sparsity_levels", type=str, default=None,
        help="Comma-separated sparsity levels (default: 0.1,0.2,0.3)",
    )
    parser.add_argument(
        "--masking_method", type=str, default="importance",
        choices=["importance", "random"],
        help="Masking method: importance or random (default: importance)",
    )
    parser.add_argument(
        "--save_generations", action="store_true",
        help="Save generated texts for accuracy evaluation",
    )
    parser.add_argument(
        "--gpu", type=int, default=None,
        help="GPU device index, e.g. 0 for cuda:0 (default: auto)",
    )
    args = parser.parse_args()
    if args.device is None:
        args.device = "cuda" if torch.cuda.is_available() else "cpu"
    if args.sparsity_levels is not None:
        args.sparsity_levels = [float(x) for x in args.sparsity_levels.split(",")]
    else:
        args.sparsity_levels = list(DEFAULT_SPARSITY_LEVELS)
    return args


if __name__ == "__main__":
    run_profiling(parse_args())
