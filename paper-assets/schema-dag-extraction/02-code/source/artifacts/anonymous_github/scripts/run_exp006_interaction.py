#!/usr/bin/env python3
"""Exp-006: 2×2 Factorial — Count × Confusability Interaction on NER.

Tests whether count × BCS effects are additive or multiplicative.
4 conditions (low/high count × low/high BCS), 10 batches each.
Hypothesis: if multiplicative, high_count + high_BCS degradation exceeds
the sum of the two main effects.

Input:
  - Few-NERD test data (parquet in data/parquet/)
  - Qwen3-32B-FP8 model
  - Pre-computed cosine similarity matrix (sim_matrix.pt)
Output (all in artifacts/exp006/):
  - batch_config.json — 4-cell batch definitions with BCS scores
  - predictions.json — raw model extraction outputs
  - eval_results.json — per-batch text_match F1/P/R metrics
  - interaction_analysis.json — cell means, main effects, interaction term
Dependencies: src/ modules (run_extraction, evaluate, compute_bcs, few_nerd_utils), vllm, torch
"""

import argparse
import json
import logging
import math
import os
import random
import sys
import time
from pathlib import Path

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def build_factorial_batches(sim_matrix, type_names, type_to_idx,
                            low_count, high_count, batches_per_cell,
                            pool_size, seed):
    """Build 2×2 factorial batch config by selecting BCS extremes from random pools.

    For each count level, generates a large random pool of type batches,
    sorts by BCS, and picks the lowest and highest N as the two BCS conditions.

    Args:
        sim_matrix: N×N cosine similarity tensor.
        type_names: list of type name strings (active types only).
        type_to_idx: dict mapping type name to sim_matrix row/col index.
        low_count: number of types for the low-count condition.
        high_count: number of types for the high-count condition.
        batches_per_cell: how many batches per factorial cell.
        pool_size: random batches to sample per count level before selecting extremes.
        seed: random seed.

    Returns:
        batch_config dict with keys "low_count"/"high_count", each containing
        "low_bcs" and "high_bcs" lists of {"types": [...], "bcs": float}.
    """
    from compute_bcs import compute_bcs

    batch_config = {}

    for count, count_label in [(low_count, "low_count"), (high_count, "high_count")]:
        rng = random.Random(seed + count)
        pool = []
        seen = set()
        max_attempts = pool_size * 20

        for _ in range(max_attempts):
            if len(pool) >= pool_size:
                break
            chosen = tuple(sorted(rng.sample(type_names, count)))
            if chosen in seen:
                continue
            seen.add(chosen)
            bcs = compute_bcs(list(chosen), sim_matrix, type_to_idx)
            pool.append({"types": list(chosen), "bcs": bcs})

        pool.sort(key=lambda x: x["bcs"])

        low_bcs_batches = pool[:batches_per_cell]
        high_bcs_batches = pool[-batches_per_cell:]

        logger.info("  %s (count=%d): pool=%d, low_bcs=[%.4f, %.4f], high_bcs=[%.4f, %.4f]",
                     count_label, count, len(pool),
                     low_bcs_batches[0]["bcs"], low_bcs_batches[-1]["bcs"],
                     high_bcs_batches[0]["bcs"], high_bcs_batches[-1]["bcs"])

        batch_config[count_label] = {
            "low_bcs": low_bcs_batches,
            "high_bcs": high_bcs_batches,
        }

    return batch_config


def compute_interaction_analysis(eval_results):
    """Compute 2×2 factorial analysis from evaluation results.

    Groups batch results into 4 cells, computes cell means for text_match F1,
    derives main effects and interaction term, and runs a contrast significance test.

    Args:
        eval_results: dict from evaluate_all(), mapping batch_id -> metrics.

    Returns:
        dict with cell_means, main_effects, interaction (with optional t-test).
    """
    cells = {
        "low_count/low_bcs": [],
        "low_count/high_bcs": [],
        "high_count/low_bcs": [],
        "high_count/high_bcs": [],
    }

    for bid, metrics in eval_results.items():
        parts = bid.split("/")
        if len(parts) >= 2:
            cell_key = f"{parts[0]}/{parts[1]}"
            if cell_key in cells:
                cells[cell_key].append(metrics)

    cell_means = {}
    for key, batch_metrics in cells.items():
        if not batch_metrics:
            logger.warning("No results for cell %s", key)
            continue
        f1s = [m["text_match"]["f1"] for m in batch_metrics]
        precs = [m["text_match"]["precision"] for m in batch_metrics]
        recs = [m["text_match"]["recall"] for m in batch_metrics]
        bcs_vals = [m["bcs"] for m in batch_metrics]
        mean_f1 = sum(f1s) / len(f1s)
        std_f1 = (sum((x - mean_f1) ** 2 for x in f1s) / len(f1s)) ** 0.5
        cell_means[key] = {
            "mean_f1": mean_f1,
            "std_f1": std_f1,
            "se_f1": std_f1 / len(f1s) ** 0.5 if len(f1s) > 1 else 0.0,
            "mean_precision": sum(precs) / len(precs),
            "mean_recall": sum(recs) / len(recs),
            "mean_bcs": sum(bcs_vals) / len(bcs_vals),
            "n_batches": len(f1s),
            "f1_values": f1s,
        }

    def get_f1(key):
        return cell_means.get(key, {}).get("mean_f1", 0.0)

    def get_se(key):
        return cell_means.get(key, {}).get("se_f1", 0.0)

    ll = get_f1("low_count/low_bcs")
    lh = get_f1("low_count/high_bcs")
    hl = get_f1("high_count/low_bcs")
    hh = get_f1("high_count/high_bcs")

    # Main effects (marginal means difference)
    count_effect = (hl + hh) / 2 - (ll + lh) / 2
    bcs_effect = (lh + hh) / 2 - (ll + hl) / 2

    # Interaction: does BCS effect differ between count levels?
    bcs_effect_at_low_count = lh - ll
    bcs_effect_at_high_count = hh - hl
    interaction = bcs_effect_at_high_count - bcs_effect_at_low_count

    # Interaction < 0 means BCS hurts MORE at high count (super-additive / multiplicative)
    if interaction < -0.005:
        interpretation = "Super-additive (multiplicative): BCS effect amplified at high count"
    elif interaction > 0.005:
        interpretation = "Sub-additive: BCS effect attenuated at high count"
    else:
        interpretation = "Approximately additive: BCS and count effects are independent"

    analysis = {
        "cell_means": cell_means,
        "cell_f1_summary": {
            "low_count_low_bcs": ll,
            "low_count_high_bcs": lh,
            "high_count_low_bcs": hl,
            "high_count_high_bcs": hh,
        },
        "main_effects": {
            "count_effect": count_effect,
            "bcs_effect": bcs_effect,
            "count_effect_interpretation": "high_count marginal mean - low_count marginal mean",
            "bcs_effect_interpretation": "high_bcs marginal mean - low_bcs marginal mean",
        },
        "interaction": {
            "bcs_effect_at_low_count": bcs_effect_at_low_count,
            "bcs_effect_at_high_count": bcs_effect_at_high_count,
            "interaction_term": interaction,
            "formula": "(HH - HL) - (LH - LL)",
            "interpretation": interpretation,
        },
    }

    # Contrast significance test via SE propagation
    se_ll = get_se("low_count/low_bcs")
    se_lh = get_se("low_count/high_bcs")
    se_hl = get_se("high_count/low_bcs")
    se_hh = get_se("high_count/high_bcs")
    se_interaction = (se_ll**2 + se_lh**2 + se_hl**2 + se_hh**2) ** 0.5

    if se_interaction > 0:
        z_stat = interaction / se_interaction
        # Two-tailed p-value approximation (normal)
        p_value = 2 * (1 - _norm_cdf(abs(z_stat)))
        analysis["interaction"]["z_test"] = {
            "z_statistic": z_stat,
            "se_interaction": se_interaction,
            "p_value": p_value,
            "significant_005": p_value < 0.05,
        }

    return analysis


def _norm_cdf(x):
    """Standard normal CDF approximation (no scipy dependency)."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def main():
    parser = argparse.ArgumentParser(
        description="Exp-006: Count × Confusability 2×2 factorial interaction design"
    )
    parser.add_argument("--model_path", default="~/.cache/huggingface/qwen3-32b-fp8/",
                        help="Path to Qwen3-32B-FP8 model")
    parser.add_argument("--types_file", default="configs/few_nerd_types.json",
                        help="Type definitions JSON")
    parser.add_argument("--sim_matrix_path", default="artifacts/sim_matrix.pt",
                        help="Pre-computed similarity matrix")
    parser.add_argument("--output_dir", default="artifacts/exp006",
                        help="Output directory")
    parser.add_argument("--max_samples", type=int, default=1000,
                        help="Max test samples from Few-NERD")
    parser.add_argument("--max_model_len", type=int, default=4096,
                        help="vLLM max model length")
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.95,
                        help="vLLM GPU memory utilization")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--low_count", type=int, default=6,
                        help="Number of types in low-count condition")
    parser.add_argument("--high_count", type=int, default=22,
                        help="Number of types in high-count condition")
    parser.add_argument("--batches_per_cell", type=int, default=10,
                        help="Number of random batches per factorial cell")
    parser.add_argument("--pool_size", type=int, default=500,
                        help="Random pool size for selecting BCS extremes")
    parser.add_argument("--dry_run", action="store_true",
                        help="Build and validate batches only, skip model extraction")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    random.seed(args.seed)

    sys.path.insert(0, str(PROJECT_ROOT / "src"))

    # Suppress CUDA init during imports (vLLM must init CUDA itself)
    orig_cuda = os.environ.get("CUDA_VISIBLE_DEVICES")
    os.environ["CUDA_VISIBLE_DEVICES"] = ""

    import torch
    from few_nerd_utils import load_few_nerd, load_type_definitions, get_all_types
    from compute_bcs import compute_bcs
    from evaluate import evaluate_all

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Step 1: Load data ---
    logger.info("Loading Few-NERD test data (max_samples=%s)...", args.max_samples)
    samples = load_few_nerd(split="test", max_samples=args.max_samples)
    type_definitions = load_type_definitions(args.types_file)
    active_types = sorted(get_all_types(samples))
    logger.info("Loaded %d samples, %d active entity types", len(samples), len(active_types))

    # --- Step 2: Load similarity matrix ---
    logger.info("Loading similarity matrix from %s", args.sim_matrix_path)
    sim_data = torch.load(args.sim_matrix_path, map_location="cpu", weights_only=True)
    sim_matrix = sim_data["sim_matrix"]
    type_to_idx = sim_data["type_to_idx"]

    # Filter to types present in both test data and sim matrix
    active_type_names = sorted(t for t in active_types if t in type_to_idx)
    logger.info("Active types in sim matrix: %d / %d", len(active_type_names), len(active_types))

    if args.high_count > len(active_type_names):
        logger.warning("high_count=%d exceeds active types=%d, clamping",
                        args.high_count, len(active_type_names))
        args.high_count = len(active_type_names)

    # --- Step 3: Build factorial batches ---
    logger.info("Building 2×2 factorial batches (pool_size=%d)...", args.pool_size)
    batch_config = build_factorial_batches(
        sim_matrix=sim_matrix,
        type_names=active_type_names,
        type_to_idx=type_to_idx,
        low_count=args.low_count,
        high_count=args.high_count,
        batches_per_cell=args.batches_per_cell,
        pool_size=args.pool_size,
        seed=args.seed,
    )

    batch_config_path = output_dir / "batch_config.json"
    with open(batch_config_path, "w") as f:
        json.dump(batch_config, f, indent=2)
    logger.info("Saved batch config to %s", batch_config_path)

    # Print batch summary
    total_batches = 0
    for count_key, strategies in batch_config.items():
        for strat_key, batches in strategies.items():
            n = len(batches)
            total_batches += n
            bcs_vals = [b["bcs"] for b in batches]
            logger.info("  %s/%s: %d batches, BCS=[%.4f, %.4f], mean=%.4f",
                         count_key, strat_key, n, min(bcs_vals), max(bcs_vals),
                         sum(bcs_vals) / len(bcs_vals))
    logger.info("Total: %d batches × %d samples = %d extractions",
                total_batches, len(samples), total_batches * len(samples))

    if args.dry_run:
        logger.info("DRY RUN complete — batch config saved, skipping extraction.")
        return

    # --- Step 4: Run extraction ---
    if orig_cuda is not None:
        os.environ["CUDA_VISIBLE_DEVICES"] = orig_cuda
    elif "CUDA_VISIBLE_DEVICES" in os.environ:
        del os.environ["CUDA_VISIBLE_DEVICES"]

    from run_extraction import run_extraction
    # Flatten 2x2 nested batch_config into per-batch entries:
    # run_extraction expects strategies["low_bcs"]["types"] as a single dict,
    # but build_factorial_batches returns a list of batches per cell.
    flat_batch_config = {}
    for count_key, strategies in batch_config.items():
        for strat_key, batches in strategies.items():
            for i, batch in enumerate(batches):
                entry_key = f"{count_key}/{strat_key}/batch_{i}"
                flat_batch_config[entry_key] = {
                    strat_key: {"types": batch["types"], "bcs": batch["bcs"]}
                }
    logger.info("Flattened batch_config: %d entries for run_extraction", len(flat_batch_config))


    logger.info("Starting vLLM extraction with %s ...", args.model_path)
    t0 = time.time()
    results = run_extraction(
        model_path=args.model_path,
        samples=samples,
        batch_config=flat_batch_config,
        type_definitions=type_definitions,
        max_model_len=args.max_model_len,
        prompt_version="v2",
        task="ner",
        gpu_memory_utilization=args.gpu_memory_utilization,
    )
    extraction_time = time.time() - t0
    logger.info("Extraction done in %.1fs, %d result entries", extraction_time, len(results))

    predictions_path = output_dir / "predictions.json"
    with open(predictions_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info("Saved predictions to %s", predictions_path)

    # --- Step 5: Evaluate ---
    logger.info("Evaluating (text_match mode)...")
    eval_results = evaluate_all(results, samples, eval_mode="text_match")

    eval_path = output_dir / "eval_results.json"
    with open(eval_path, "w") as f:
        json.dump(eval_results, f, indent=2)
    logger.info("Saved eval results to %s", eval_path)

    # --- Step 6: Interaction analysis ---
    logger.info("Computing interaction analysis...")
    analysis = compute_interaction_analysis(eval_results)

    analysis_path = output_dir / "interaction_analysis.json"
    with open(analysis_path, "w") as f:
        json.dump(analysis, f, indent=2, default=str)
    logger.info("Saved interaction analysis to %s", analysis_path)

    # --- Summary ---
    logger.info("=" * 70)
    logger.info("EXP-006 RESULTS: Count × BCS 2×2 Interaction")
    logger.info("=" * 70)
    for cell_key in ["low_count/low_bcs", "low_count/high_bcs",
                     "high_count/low_bcs", "high_count/high_bcs"]:
        stats = analysis["cell_means"].get(cell_key, {})
        if stats:
            logger.info("  %-25s F1=%.4f ± %.4f  P=%.4f  R=%.4f  BCS=%.4f  (n=%d)",
                         cell_key,
                         stats["mean_f1"], stats["std_f1"],
                         stats["mean_precision"], stats["mean_recall"],
                         stats["mean_bcs"], stats["n_batches"])
    logger.info("-" * 70)
    logger.info("  Count main effect:     %+.4f (high_count - low_count)",
                analysis["main_effects"]["count_effect"])
    logger.info("  BCS main effect:       %+.4f (high_bcs - low_bcs)",
                analysis["main_effects"]["bcs_effect"])
    logger.info("  Interaction term:      %+.4f  %s",
                analysis["interaction"]["interaction_term"],
                analysis["interaction"]["formula"])
    logger.info("  → %s", analysis["interaction"]["interpretation"])
    if "z_test" in analysis.get("interaction", {}):
        z = analysis["interaction"]["z_test"]
        logger.info("  z-test: z=%.3f, SE=%.4f, p=%.4f %s",
                     z["z_statistic"], z["se_interaction"], z["p_value"],
                     "**" if z["significant_005"] else "n.s.")
    logger.info("=" * 70)
    logger.info("Extraction time: %.1fs", extraction_time)
    logger.info("All results in: %s", output_dir)


if __name__ == "__main__":
    main()
