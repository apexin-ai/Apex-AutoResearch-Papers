# PACS Profiling — full MVP pipeline (v4: importance-based masking).
#
# End-to-end:
#   1. Load causal LM + MATH-500 (stratified 50 problems)
#   2. Generate reasoning traces, segment into phases (quantile-based)
#   3. Per problem: dense forward with output_attentions to get CE losses
#      + head importance (Frobenius norm) + KV importance (cumulative attention)
#   4. For each sparsity level (10%, 20%):
#      - Build importance-based masks (prune least important heads/KV positions)
#      - Compute per-phase perplexity under 4 conditions (dense/attn/kv/both)
#      - Compute per-phase Interaction Index
#   5. Bootstrap 95% CI per (phase, level)
#   6. Pass/fail judgment (CI overlap + sign reversal, OR logic)
#   7. Output structured JSON
#
# Usage:
#   python -m pacs.profiling.run_profiling \
#     --model_path <HF model ID or path> \
#     --data_path <MATH-500 JSON> \
#     --output_dir ./profiling_output

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import torch

from ..utils.data_utils import stratified_sample_math500
from ..utils.metrics import compute_perplexity, ppl_from_cached_losses
from .interaction_index import InteractionIndexCalculator, _HeadMaskHook, bootstrap_interaction_index
from .phase_segmentation import PhaseSegmenter
from .alt_segmentation import segment_by_quantile, to_phase_annotation

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("run_profiling")

DEFAULT_SPARSITY_LEVELS = [0.1, 0.2, 0.3]
N_BOOTSTRAP = 1000
MIN_SEGMENTS_WARN = 20
SEED = 42


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


def load_data(data_path: str) -> List[Dict[str, Any]]:
    logger.info("Loading data from %s", data_path)
    with open(data_path) as f:
        data = json.load(f)
    if isinstance(data, dict) and "data" in data:
        data = data["data"]
    logger.info("Loaded %d problems", len(data))
    return data


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
    """Check pass criteria across phases.

    Args:
        ii_results: {phase_name: {level_str: {"mean", "ci_low", "ci_high"}}}.

    Returns:
        Dict with ci_overlap_test, sign_reversal_test, overall verdict.
    """
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
            # NaN guard: skip pairs with non-finite CI bounds
            if not (np.isfinite(c1[0]) and np.isfinite(c1[1]) and np.isfinite(c2[0]) and np.isfinite(c2[1])):
                continue
            # CI non-overlap
            if c1[1] < c2[0] or c2[1] < c1[0]:
                ci_pass = True
                ci_detail = f"{p1} vs {p2} CI non-overlapping at {level_str}"
            # Sign reversal: one strictly positive, other strictly negative
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
    device = "cuda" if torch.cuda.is_available() else "cpu"
    torch.manual_seed(SEED)
    sparsity_levels = args.sparsity_levels
    use_importance = (args.masking_method == "importance")
    model, tokenizer = load_model_and_tokenizer(args.model_path, device=device)

    raw_data = load_data(args.data_path)
    data = stratified_sample_math500(raw_data, seed=SEED)
    logger.info("Stratified sample: %d problems", len(data))

    segmenter = PhaseSegmenter(
        bandwidth=args.kde_bandwidth,
        min_phase_length=args.min_phase_length,
    )
    ii_calc = InteractionIndexCalculator(model, tokenizer, device=device)

    os.makedirs(args.output_dir, exist_ok=True)
    warnings_list: List[str] = []

    # Accumulators: {phase_name: {level_str: [ii_values]}}
    ii_per_phase_level: Dict[str, Dict[str, List[float]]] = defaultdict(
        lambda: defaultdict(list)
    )
    # Accumulators: {phase_name: {level_str: {condition: [ppl_values]}}}
    ppl_per_phase_level: Dict[str, Dict[str, Dict[str, List[float]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )
    # Phase token counts
    phase_token_counts: Dict[str, List[int]] = defaultdict(list)
    phase_segment_counts: Dict[str, int] = defaultdict(int)

    # P1 diagnostics accumulators
    all_problem_diagnostics: List[Dict[str, Any]] = []
    all_sparsity_values: List[float] = []

    # Locate attention layers once for hook registration (C1/C3 fix)
    attn_layers = _HeadMaskHook._find_attention_layers(model)
    if not attn_layers:
        raise RuntimeError("Could not find attention layers in model")
    last_attn_layer = attn_layers[-1]

    for idx, item in enumerate(data):
        problem_text = item.get("problem", item.get("question", ""))
        problem_id = item.get("id", str(idx))
        logger.info("[%d/%d] Processing problem %s", idx + 1, len(data), problem_id)

        prompt = (
            f"Solve the following math problem step by step.\n\n"
            f"Problem: {problem_text}\n\nSolution:"
        )
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        prompt_len = inputs["input_ids"].shape[1]

        # --- C1/C3 fix: hook-based per-step sparsity, no output_attentions accumulation ---
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

        if len(step_sparsities) == 0:
            logger.warning("No generation steps for problem %s, skipping.", problem_id)
            warnings_list.append(f"No generation steps for {problem_id}")
            continue

        # Phase segmentation on the generation trace (quantile-based)
        gen_sparsity = np.array(step_sparsities)
        quant_seg = segment_by_quantile(gen_sparsity, n_groups=3)
        annotation = to_phase_annotation(
            quant_seg.assignments,
            quant_seg.group_names,
            gen_sparsity,
            offset=0,
            min_phase_length=args.min_phase_length,
        )

        # P1: collect per-problem sparsity diagnostics
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

        # Offset phase indices to full_ids coordinates (prompt + generation)
        for phase in annotation.phases:
            phase.start += prompt_len
            phase.end += prompt_len

        # --- Dense forward: importance-based extracts head/KV importance; random skips it ---
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

        # --- C2 fix: generate masks once per level, reuse across phases ---
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
    # Aggregate: mean perplexity per (phase, level, condition)
    # ------------------------------------------------------------------
    perplexity_out: Dict[str, Dict[str, Dict[str, float]]] = {}
    for pname in sorted(ppl_per_phase_level.keys()):
        perplexity_out[pname] = {}
        for level_str in sorted(ppl_per_phase_level[pname].keys()):
            cond_means: Dict[str, float] = {}
            for cond in ["dense", "attn", "kv", "both"]:
                vals = ppl_per_phase_level[pname][level_str][cond]
                valid = [v for v in vals if not (isinstance(v, float) and v != v)]
                cond_means[cond] = round(float(np.mean(valid)), 4) if valid else float("nan")
            perplexity_out[pname][level_str] = cond_means

    # ------------------------------------------------------------------
    # Bootstrap CI per (phase, level)
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
                    "mean": round(mean, 6),
                    "ci_low": round(ci_low, 6),
                    "ci_high": round(ci_high, 6),
                }

    # ------------------------------------------------------------------
    # Pass / fail
    # ------------------------------------------------------------------
    pass_fail = evaluate_pass_fail(ii_out)

    # ------------------------------------------------------------------
    # Assemble output
    # ------------------------------------------------------------------
    # P1: build sparsity histogram
    diagnostics_section: Dict[str, Any] = {
        "per_problem_sparsity": all_problem_diagnostics,
    }
    if all_sparsity_values:
        counts, bin_edges = np.histogram(all_sparsity_values, bins=50)
        diagnostics_section["global_sparsity_histogram"] = {
            "bins": bin_edges.tolist(),
            "counts": counts.tolist(),
        }

    output = {
        "config": {
            "model": args.model_path,
            "sparsity_levels": sparsity_levels,
            "masking_method": args.masking_method,
            "head_importance_metric": "attention_frobenius_norm" if use_importance else "none",
            "kv_importance_metric": "cumulative_attention_received" if use_importance else "none",
            "segmentation_method": "quantile",
            "n_bootstrap": N_BOOTSTRAP,
            "n_problems": len(data),
            "seed": SEED,
        },
        "phase_stats": phase_stats,
        "perplexity": perplexity_out,
        "interaction_index": ii_out,
        "pass_fail": pass_fail,
        "warnings": warnings_list,
        "diagnostics": diagnostics_section,
    }

    out_path = os.path.join(args.output_dir, "profiling_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Results saved to %s", out_path)

    # Print summary
    print(f"\n{'='*60}")
    print(f"PACS Profiling Complete — {len(data)} problems")
    print(f"{'='*60}")
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
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="PACS Phase Profiling — interaction index analysis"
    )
    parser.add_argument(
        "--model_path", type=str, required=True,
        help="Path or HF model ID for the causal LM",
    )
    parser.add_argument(
        "--data_path", type=str, required=True,
        help="Path to MATH-500 JSON",
    )
    parser.add_argument(
        "--output_dir", type=str, default="./profiling_output",
        help="Directory for output JSON (default: ./profiling_output)",
    )
    parser.add_argument(
        "--max_new_tokens", type=int, default=2048,
        help="Max tokens to generate per problem (default: 2048)",
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
        help="Masking method: importance (prune least important) or random (default: importance)",
    )
    args = parser.parse_args()
    if args.sparsity_levels is not None:
        args.sparsity_levels = [float(x) for x in args.sparsity_levels.split(",")]
    else:
        args.sparsity_levels = list(DEFAULT_SPARSITY_LEVELS)
    return args


if __name__ == "__main__":
    run_profiling(parse_args())
