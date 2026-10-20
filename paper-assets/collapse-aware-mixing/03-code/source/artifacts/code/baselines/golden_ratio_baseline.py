"""Fixed-ratio real/synthetic mixing baseline for model collapse experiments.

Trains iteratively over multiple generations. G0 uses 100% real data;
G1+ mixes real and synthetic data at a fixed ratio (--real_ratio).

Input:  CLI args (--model_name, --num_generations, --real_ratio, etc.)
Output: <output_dir>/golden_ratio_summary.json with per-generation metrics
Deps:   config, data_utils, generate, metrics, train
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

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from config import PilotConfig
from data_utils import (
    PackedDataset,
    prepare_real_data,
    prepare_synthetic_data,
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
logger = logging.getLogger("golden_ratio")


def mix_datasets(
    real_dataset: PackedDataset,
    synth_dataset: PackedDataset,
    real_ratio: float,
    total_seqs: int,
    rng: np.random.Generator | None = None,
) -> PackedDataset:
    """Sample from real and synthetic datasets at a fixed ratio, shuffle, return combined."""
    if rng is None:
        rng = np.random.default_rng()

    n_real = int(total_seqs * real_ratio)
    n_synth = total_seqs - n_real

    real_idx = rng.choice(
        len(real_dataset), min(n_real, len(real_dataset)),
        replace=n_real > len(real_dataset),
    )
    synth_idx = rng.choice(
        len(synth_dataset), min(n_synth, len(synth_dataset)),
        replace=n_synth > len(synth_dataset),
    )

    mixed = ([real_dataset.input_ids[i] for i in real_idx]
             + [synth_dataset.input_ids[i] for i in synth_idx])
    rng.shuffle(mixed)
    return PackedDataset(mixed)


def evaluate_checkpoints(
    checkpoint_paths: list[str],
    gen_idx: int,
    holdout_dataset,
    prev_gen_token_ids: list[int] | None,
    config: PilotConfig,
    device: str,
) -> list[dict]:
    tokenizer = AutoTokenizer.from_pretrained(config.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    vocab_size = tokenizer.vocab_size
    holdout_loader = make_dataloader(holdout_dataset, batch_size=config.ppl_batch_size)
    all_metrics = []

    for ci, ckpt_path in enumerate(checkpoint_paths):
        logger.info("--- Eval ckpt %d/%d: %s ---", ci + 1, len(checkpoint_paths), ckpt_path)
        t0 = time.time()
        model = AutoModelForCausalLM.from_pretrained(ckpt_path, torch_dtype="auto").to(device)
        model.eval()

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
            model=model, holdout_loader=holdout_loader,
            gen_token_ids=gen_ids, prev_gen_token_ids=prev_gen_token_ids,
            vocab_size=vocab_size, config=config, device=device,
        )
        m["generation"] = gen_idx
        m["checkpoint"] = ckpt_path
        m["checkpoint_index"] = ci
        step_str = os.path.basename(ckpt_path).split("-")[-1]
        m["global_step"] = int(step_str) if step_str.isdigit() else ci
        m["tokens_seen"] = m["global_step"] * config.tokens_per_step
        m["eval_time_sec"] = time.time() - t0
        all_metrics.append(m)

        logger.info(
            "  rank=%.1f  ppl=%.2f  ent_var=%.4f  cov=%.4f  (%.0fs)",
            m["spectral_effective_rank"], m["perplexity"],
            m["token_entropy_var"], m["vocab_coverage"], m["eval_time_sec"],
        )
        del model
        torch.cuda.empty_cache()

    return all_metrics


def save_metrics(metrics: list[dict], path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        for m in metrics:
            f.write(json.dumps(m, default=str) + "\n")


def run_golden_ratio(config: PilotConfig, real_ratio: float) -> list[dict]:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    rng = np.random.default_rng(config.seed)
    os.makedirs(config.output_dir, exist_ok=True)

    logger.info("=" * 60)
    logger.info("GOLDEN RATIO BASELINE  real_ratio=%.2f", real_ratio)
    logger.info("  Model: %s | Gens: %d | Tokens/gen: %dM",
                config.model_name, config.num_generations,
                config.tokens_per_generation // 1_000_000)
    logger.info("=" * 60)

    tokenizer = AutoTokenizer.from_pretrained(config.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    train_dataset, holdout_dataset = prepare_real_data(config, tokenizer)
    total_seqs = config.tokens_per_generation // config.max_seq_length

    all_results: list[dict] = []
    prev_gen_token_ids: list[int] | None = None
    prev_model_dir: str | None = None
    g0_baseline: dict | None = None

    for g in range(config.num_generations):
        logger.info("=" * 60)
        logger.info("GENERATION %d / %d", g, config.num_generations - 1)
        logger.info("=" * 60)

        # --- Build training data ---
        if g == 0:
            gen_train = train_dataset
        else:
            synth_path = config.synthetic_data_path(g - 1)
            synth_dataset = prepare_synthetic_data(synth_path, config, tokenizer)
            gen_train = mix_datasets(train_dataset, synth_dataset, real_ratio, total_seqs, rng)
            logger.info("Mixed %d seqs (%.0f%% real + %.0f%% synth)",
                        len(gen_train), real_ratio * 100, (1 - real_ratio) * 100)

        # --- Train ---
        final_model_dir, ckpt_paths = train_generation(g, gen_train, config, prev_model_dir)
        if final_model_dir not in ckpt_paths:
            ckpt_paths.append(final_model_dir)

        # --- Evaluate ---
        gen_metrics = evaluate_checkpoints(
            ckpt_paths, g, holdout_dataset, prev_gen_token_ids, config, device,
        )
        save_metrics(gen_metrics, config.metrics_path(g))
        all_results.extend(gen_metrics)

        if g == 0 and gen_metrics:
            ranks = np.array([m["spectral_effective_rank"] for m in gen_metrics])
            ppls = np.array([m["perplexity"] for m in gen_metrics])
            g0_baseline = {
                "spectral_rank_mean": float(ranks.mean()),
                "spectral_rank_std": float(ranks.std()),
                "ppl_final": float(ppls[-1]),
                "num_checkpoints": len(gen_metrics),
            }

        # --- Generate synthetic data for next gen ---
        if g < config.num_generations - 1:
            logger.info("Generating synthetic data from G%d ...", g)
            model = AutoModelForCausalLM.from_pretrained(
                final_model_dir, torch_dtype="auto",
            ).to(device)
            gen_tok = AutoTokenizer.from_pretrained(config.model_name)
            if gen_tok.pad_token is None:
                gen_tok.pad_token = gen_tok.eos_token

            generate_synthetic_data(
                model, gen_tok, config.tokens_per_generation,
                config, config.synthetic_data_path(g),
            )
            synth_ds = prepare_synthetic_data(config.synthetic_data_path(g), config, gen_tok)
            prev_gen_token_ids = extract_token_ids(synth_ds, max_tokens=10_000_000)
            del model
            torch.cuda.empty_cache()

        prev_model_dir = final_model_dir

    # --- Summary ---
    summary: dict = {
        "experiment": "golden_ratio_baseline",
        "real_ratio": real_ratio,
        "config": {k: v for k, v in config.__dict__.items() if not k.startswith("_")},
        "num_checkpoints_evaluated": len(all_results),
        "g0_baseline": g0_baseline,
        "generations": {},
    }
    for g in range(config.num_generations):
        gm = [m for m in all_results if m["generation"] == g]
        if gm:
            gs: dict = {
                "final_spectral_rank": gm[-1]["spectral_effective_rank"],
                "final_ppl": gm[-1]["perplexity"],
                "spectral_rank_trajectory": [m["spectral_effective_rank"] for m in gm],
                "ppl_trajectory": [m["perplexity"] for m in gm],
            }
            if "kl_unigram" in gm[-1]:
                gs["final_kl_unigram"] = gm[-1]["kl_unigram"]
            summary["generations"][f"G{g}"] = gs

    summary_path = os.path.join(config.output_dir, "golden_ratio_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    logger.info("Summary -> %s", summary_path)

    return all_results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="Fixed-ratio mixing baseline for model collapse")
    p.add_argument("--model_name", type=str, default="EleutherAI/pythia-1b")
    p.add_argument("--num_generations", type=int, default=3)
    p.add_argument("--real_ratio", type=float, default=0.618,
                   help="Fraction of real data in the training mix (default: 1/phi ≈ 0.618)")
    p.add_argument("--output_dir", type=str, default="./output_golden_ratio")
    p.add_argument("--tokens_per_generation", type=int, default=500_000_000)
    p.add_argument("--max_seq_length", type=int, default=2048)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--no_wandb", action="store_true")
    return p.parse_args()


def main():
    args = parse_args()
    config = PilotConfig(
        model_name=args.model_name,
        num_generations=args.num_generations,
        output_dir=args.output_dir,
        tokens_per_generation=args.tokens_per_generation,
        max_seq_length=args.max_seq_length,
        seed=args.seed,
        use_wandb=not args.no_wandb,
        wandb_run_prefix="golden_ratio",
    )
    run_golden_ratio(config, args.real_ratio)


if __name__ == "__main__":
    main()
