"""End-to-end pilot pipeline: G0 -> gen -> G1 -> gen -> G2 with metrics at every checkpoint.

Usage:
    python pilot_pipeline.py [--output_dir ./output] [--num_generations 3] [--no_wandb]
"""

import argparse
import json
import logging
import os
import sys
import time

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from config import PilotConfig
from data_utils import (
    prepare_real_data,
    prepare_synthetic_data,
    mix_datasets,
    extract_token_ids,
    make_dataloader,
)
from generate import generate_synthetic_data, generate_sample_tokens
from metrics import compute_checkpoint_metrics
from train import train_generation

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("pilot")


def evaluate_checkpoints(
    checkpoint_paths: list[str],
    gen_idx: int,
    holdout_dataset,
    prev_gen_token_ids: list[int] | None,
    config: PilotConfig,
    device: str,
) -> list[dict]:
    """Load each checkpoint, compute all metrics, return list of metric dicts."""
    tokenizer = AutoTokenizer.from_pretrained(config.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    vocab_size = tokenizer.vocab_size

    holdout_loader = make_dataloader(holdout_dataset, batch_size=config.ppl_batch_size)
    all_metrics = []

    for ci, ckpt_path in enumerate(checkpoint_paths):
        logger.info("--- Evaluating checkpoint %d/%d: %s ---", ci + 1, len(checkpoint_paths), ckpt_path)
        t0 = time.time()

        model = AutoModelForCausalLM.from_pretrained(ckpt_path, torch_dtype=torch.bfloat16).to(device)
        model.eval()

        # generate a small sample for n-gram / coverage metrics
        logger.info("Generating %dK tokens for corpus metrics ...", config.metrics_gen_tokens // 1000)
        gen_ids = generate_sample_tokens(
            model, tokenizer,
            num_tokens=config.metrics_gen_tokens,
            batch_size=config.gen_batch_size,
            max_new_tokens=256,
            temperature=config.gen_temperature,
            top_p=config.gen_top_p,
            device=device,
        )

        m = compute_checkpoint_metrics(
            model=model,
            holdout_loader=holdout_loader,
            gen_token_ids=gen_ids,
            prev_gen_token_ids=prev_gen_token_ids,
            vocab_size=vocab_size,
            config=config,
            device=device,
        )
        m["generation"] = gen_idx
        m["checkpoint"] = ckpt_path
        m["checkpoint_index"] = ci

        step_str = os.path.basename(ckpt_path).split("-")[-1]
        m["global_step"] = int(step_str) if step_str.isdigit() else config.max_steps
        m["tokens_seen"] = m["global_step"] * config.tokens_per_step
        m["eval_time_sec"] = time.time() - t0

        all_metrics.append(m)
        logger.info(
            "  eff_rank=%.1f  ppl=%.2f  entropy_var=%.4f  unigram_H=%.3f  coverage=%.4f  (%.0fs)",
            m["spectral_effective_rank"], m["perplexity"],
            m["token_entropy_var"], m["unigram_entropy"],
            m["vocab_coverage"], m["eval_time_sec"],
        )

        del model
        torch.cuda.empty_cache()

    return all_metrics


def save_metrics(metrics: list[dict], path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        for m in metrics:
            f.write(json.dumps(m, default=str) + "\n")
    logger.info("Metrics appended to %s", path)


def run_pilot(config: PilotConfig):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    os.makedirs(config.output_dir, exist_ok=True)

    logger.info("=" * 60)
    logger.info("PILOT PIPELINE START")
    logger.info("  Model: %s", config.model_name)
    logger.info("  Generations: %d | Tokens/gen: %dM", config.num_generations, config.tokens_per_generation // 1_000_000)
    logger.info("  Checkpoint interval: %dM tokens (%d steps)", config.checkpoint_interval_tokens // 1_000_000, config.save_steps)
    logger.info("  Fixed ratio: %s", config.fixed_ratio if config.fixed_ratio is not None else "None (original behavior)")
    logger.info("  Device: %s", device)
    logger.info("=" * 60)

    # --- Prepare data ---
    tokenizer = AutoTokenizer.from_pretrained(config.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    logger.info("Preparing real data ...")
    train_dataset, holdout_dataset = prepare_real_data(config, tokenizer)

    all_results = []
    prev_gen_token_ids = None
    prev_model_dir = None  # G0: None → config.model_name; G1+: previous gen's final checkpoint
    g0_baseline = None  # populated after G0 evaluation

    for g in range(config.num_generations):
        logger.info("=" * 60)
        logger.info("GENERATION %d / %d", g, config.num_generations - 1)
        logger.info("=" * 60)

        # --- Determine training data ---
        if g == 0:
            # G0 always uses real data (no synthetic data exists yet)
            gen_train = train_dataset
        elif config.fixed_ratio is None:
            # Original behavior: G1+ uses pure synthetic
            synth_path = config.synthetic_data_path(g - 1)
            gen_train = prepare_synthetic_data(synth_path, config, tokenizer)
        elif config.fixed_ratio >= 1.0:
            # w=1: every generation trains on real data only
            gen_train = train_dataset
        elif config.fixed_ratio <= 0.0:
            # w=0: G1+ uses pure synthetic (same as original)
            synth_path = config.synthetic_data_path(g - 1)
            gen_train = prepare_synthetic_data(synth_path, config, tokenizer)
        else:
            # 0 < w < 1: mix real and synthetic by ratio
            synth_path = config.synthetic_data_path(g - 1)
            synth_dataset = prepare_synthetic_data(synth_path, config, tokenizer)
            gen_train = mix_datasets(train_dataset, synth_dataset, config.fixed_ratio, seed=config.seed + g)

        # --- Train (chain model from previous generation) ---
        final_model_dir, ckpt_paths = train_generation(
            gen_idx=g,
            train_dataset=gen_train,
            config=config,
            model_name_or_path=prev_model_dir,
        )

        # include final model as the last eval point
        if final_model_dir not in ckpt_paths:
            ckpt_paths.append(final_model_dir)

        # --- Evaluate all checkpoints ---
        gen_metrics = evaluate_checkpoints(
            checkpoint_paths=ckpt_paths,
            gen_idx=g,
            holdout_dataset=holdout_dataset,
            prev_gen_token_ids=prev_gen_token_ids,
            config=config,
            device=device,
        )
        save_metrics(gen_metrics, config.metrics_path(g))
        all_results.extend(gen_metrics)

        # --- G0 baseline statistics for leading-indicator threshold ---
        if g == 0 and gen_metrics:
            ranks = np.array([m["spectral_effective_rank"] for m in gen_metrics])
            ppls = np.array([m["perplexity"] for m in gen_metrics])
            g0_baseline = {
                "spectral_rank_mean": float(ranks.mean()),
                "spectral_rank_std": float(ranks.std()),
                "spectral_rank_min": float(ranks.min()),
                "spectral_rank_max": float(ranks.max()),
                "ppl_final": float(ppls[-1]),
                "ppl_mean": float(ppls.mean()),
                "ppl_std": float(ppls.std()),
                "num_checkpoints": len(gen_metrics),
            }
            logger.info("G0 BASELINE: rank=%.1f +/- %.2f (sigma for 1-sigma threshold)  ppl_final=%.2f",
                         g0_baseline["spectral_rank_mean"], g0_baseline["spectral_rank_std"],
                         g0_baseline["ppl_final"])

        # --- Generate synthetic data for next generation ---
        if g < config.num_generations - 1:
            logger.info("Generating synthetic data from G%d for next generation ...", g)
            model = AutoModelForCausalLM.from_pretrained(final_model_dir, torch_dtype=torch.bfloat16).to(device)
            gen_tok = AutoTokenizer.from_pretrained(config.model_name)
            if gen_tok.pad_token is None:
                gen_tok.pad_token = gen_tok.eos_token

            generate_synthetic_data(
                model=model,
                tokenizer=gen_tok,
                num_tokens=config.tokens_per_generation,
                config=config,
                output_dir=config.synthetic_data_path(g),
            )

            # save current gen token ids for KL computation in next gen
            synth_ds = prepare_synthetic_data(config.synthetic_data_path(g), config, gen_tok)
            prev_gen_token_ids = extract_token_ids(synth_ds, max_tokens=10_000_000)

            del model
            torch.cuda.empty_cache()

        # chain: next generation initialises from this generation's final model
        prev_model_dir = final_model_dir

    # --- Summary ---
    summary = {
        "config": {k: v for k, v in config.__dict__.items() if not k.startswith("_")},
        "num_checkpoints_evaluated": len(all_results),
        "g0_baseline": g0_baseline,
        "generations": {},
    }
    for g in range(config.num_generations):
        gm = [m for m in all_results if m["generation"] == g]
        if gm:
            gen_summary = {
                "final_spectral_rank": gm[-1]["spectral_effective_rank"],
                "final_ppl": gm[-1]["perplexity"],
                "spectral_rank_trajectory": [m["spectral_effective_rank"] for m in gm],
                "ppl_trajectory": [m["perplexity"] for m in gm],
            }
            if "kl_unigram" in gm[-1]:
                gen_summary["final_kl_unigram"] = gm[-1]["kl_unigram"]
                gen_summary["final_kl_bigram"] = gm[-1].get("kl_bigram")
                gen_summary["final_kl_ci_95"] = [gm[-1].get("kl_ci_lower_95"), gm[-1].get("kl_ci_upper_95")]
            summary["generations"][f"G{g}"] = gen_summary

    summary_path = config.summary_path()
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    logger.info("Summary written to %s", summary_path)

    # --- MVP GO / NO-GO check (quantitative criteria from ROADMAP) ---
    if g0_baseline and len(summary["generations"]) >= 2:
        sigma = g0_baseline["spectral_rank_std"]
        g0_rank_mean = g0_baseline["spectral_rank_mean"]
        g0_ppl = g0_baseline["ppl_final"]
        rank_threshold = g0_rank_mean - sigma  # drop >= 1 sigma

        # PPL significance: >= 2 pts absolute OR >= 5% relative
        ppl_abs_threshold = g0_ppl + 2.0
        ppl_rel_threshold = g0_ppl * 1.05

        # Scan all post-G0 checkpoints for the leading indicator pattern:
        # find first checkpoint where rank drops >= 1 sigma below G0 mean
        # and check whether PPL has NOT yet risen significantly at that point
        first_rank_drop_idx = None
        first_ppl_rise_idx = None

        post_g0 = [m for m in all_results if m["generation"] > 0]
        for i, m in enumerate(post_g0):
            if first_rank_drop_idx is None and m["spectral_effective_rank"] <= rank_threshold:
                first_rank_drop_idx = i
            if first_ppl_rise_idx is None and (m["perplexity"] >= ppl_abs_threshold or m["perplexity"] >= ppl_rel_threshold):
                first_ppl_rise_idx = i

        # KL check (on final generation boundary)
        last_gen_metrics = [m for m in all_results if m["generation"] == config.num_generations - 1]
        kl_value = last_gen_metrics[-1].get("kl_unigram", 0) if last_gen_metrics else 0
        kl_ci = (last_gen_metrics[-1].get("kl_ci_lower_95", 0), last_gen_metrics[-1].get("kl_ci_upper_95", 0)) if last_gen_metrics else (0, 0)

        spectral_leads = (first_rank_drop_idx is not None and
                          (first_ppl_rise_idx is None or first_rank_drop_idx < first_ppl_rise_idx))
        kl_above_threshold = kl_value > 0.1

        logger.info("=" * 60)
        logger.info("MVP GO / NO-GO CHECK")
        logger.info("  G0 baseline: rank=%.1f +/- %.2f (1-sigma threshold=%.1f)  ppl=%.2f",
                     g0_rank_mean, sigma, rank_threshold, g0_ppl)
        logger.info("  PPL significance: >= %.2f (abs +2) OR >= %.2f (rel +5%%)",
                     ppl_abs_threshold, ppl_rel_threshold)
        logger.info("  First rank drop (>= 1 sigma): %s",
                     f"checkpoint {first_rank_drop_idx}" if first_rank_drop_idx is not None else "NOT DETECTED")
        logger.info("  First PPL rise (significant): %s",
                     f"checkpoint {first_ppl_rise_idx}" if first_ppl_rise_idx is not None else "NOT DETECTED")
        logger.info("  Spectral leads PPL: %s", spectral_leads)
        logger.info("  KL divergence: %.4f  (95%% CI: [%.4f, %.4f])  threshold 0.1: %s",
                     kl_value, kl_ci[0], kl_ci[1], "PASS" if kl_above_threshold else "FAIL")

        if spectral_leads and kl_above_threshold:
            verdict = "GO — spectral rank is a leading indicator, KL confirms non-stationarity"
        elif first_rank_drop_idx is not None and first_ppl_rise_idx is not None and first_rank_drop_idx == first_ppl_rise_idx:
            verdict = "CONDITIONAL GO — spectral and PPL drop simultaneously, check granularity advantage"
        elif kl_value < 0.1 and (first_rank_drop_idx is not None or first_ppl_rise_idx is not None):
            verdict = "EXTEND — KL below threshold but collapse signals detected, add generation to accumulate KL"
        elif first_rank_drop_idx is None and first_ppl_rise_idx is not None:
            verdict = "KILL — PPL rose but spectral rank did not drop, indicator ineffective for autoregressive LM collapse"
        elif first_rank_drop_idx is None and first_ppl_rise_idx is None:
            verdict = "EXTEND — neither spectral rank nor PPL moved in 2 generations, add generation to trigger collapse"
        else:
            verdict = "INCONCLUSIVE — review trajectories manually"

        logger.info("  VERDICT: %s", verdict)
        logger.info("=" * 60)

        summary["mvp_check"] = {
            "g0_rank_mean": g0_rank_mean,
            "g0_rank_std": sigma,
            "rank_threshold_1sigma": rank_threshold,
            "ppl_threshold_abs": ppl_abs_threshold,
            "ppl_threshold_rel": ppl_rel_threshold,
            "first_rank_drop_checkpoint": first_rank_drop_idx,
            "first_ppl_rise_checkpoint": first_ppl_rise_idx,
            "spectral_leads": spectral_leads,
            "kl_unigram": kl_value,
            "kl_ci_95": list(kl_ci),
            "kl_above_0_1": kl_above_threshold,
            "verdict": verdict,
        }
        with open(summary_path, "w") as f:
            json.dump(summary, f, indent=2, default=str)

    return all_results


def parse_args():
    parser = argparse.ArgumentParser(description="Collapse-aware mixing pilot experiment")
    parser.add_argument("--output_dir", type=str, default="./output")
    parser.add_argument("--num_generations", type=int, default=3)
    parser.add_argument("--tokens_per_generation", type=int, default=90_000_000)
    parser.add_argument("--checkpoint_interval_tokens", type=int, default=10_000_000)
    parser.add_argument("--holdout_size", type=int, default=5_000)
    parser.add_argument("--model_name", type=str, default="EleutherAI/pythia-1b")
    parser.add_argument("--per_device_batch_size", type=int, default=8)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=4)
    parser.add_argument("--learning_rate", type=float, default=1e-5)
    parser.add_argument("--spectral_num_samples", type=int, default=50_000)
    parser.add_argument("--gen_temperature", type=float, default=1.0)
    parser.add_argument("--gen_top_p", type=float, default=0.95)
    parser.add_argument("--no_wandb", action="store_true")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--real_dataset", type=str, default="wikitext")
    parser.add_argument("--metrics_gen_tokens", type=int, default=500_000)
    parser.add_argument("--fixed-ratio", type=float, default=None,
        help="Fixed real/synthetic mixing ratio. None=original behavior (G0 real, G1+ pure synth). "
             "0.0=pure synthetic, 1.0=pure real, 0.5=50/50 mix")
    return parser.parse_args()


def main():
    args = parse_args()
    config = PilotConfig(
        output_dir=args.output_dir,
        num_generations=args.num_generations,
        tokens_per_generation=args.tokens_per_generation,
        checkpoint_interval_tokens=args.checkpoint_interval_tokens,
        model_name=args.model_name,
        per_device_batch_size=args.per_device_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        spectral_num_samples=args.spectral_num_samples,
        gen_temperature=args.gen_temperature,
        gen_top_p=args.gen_top_p,
        use_wandb=not args.no_wandb,
        seed=args.seed,
        real_dataset=args.real_dataset,
        metrics_gen_tokens=args.metrics_gen_tokens,
        holdout_size=args.holdout_size,
        fixed_ratio=args.fixed_ratio,
    )
    run_pilot(config)


if __name__ == "__main__":
    main()
