"""Re-run G2 evaluation without retraining.

Loads G2 checkpoints, prepares holdout data and G1 synthetic data,
computes all metrics, and writes metrics.jsonl. Use this after a
crash during eval to recover without repeating the training phase.

Usage:
    python rerun_g2_eval.py \
        --output-dir /root/autodl-tmp/output_v7/ \
        --tokens-per-gen 20000000 \
        --checkpoint-interval 5000000

Input:
    - G2 checkpoints in output_dir/G2/training/checkpoint-*
    - G2 final_model in output_dir/G2/final_model
    - G1 synthetic data in output_dir/G1/synth_data/
    - Holdout data cache in output_dir/real_data_cache/

Output:
    - output_dir/G2/metrics/metrics.jsonl (one JSON line per checkpoint)
"""

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from config import PilotConfig
from data_utils import (
    prepare_real_data,
    prepare_synthetic_data,
    extract_token_ids,
    make_dataloader,
)
from generate import generate_sample_tokens
from metrics import compute_checkpoint_metrics

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("rerun_g2_eval")


def find_g2_checkpoints(output_dir: str) -> list[str]:
    g2_dir = Path(output_dir) / "G2"
    ckpts = []
    training_dir = g2_dir / "training"
    if training_dir.exists():
        for ckpt in sorted(training_dir.glob("checkpoint-*")):
            ckpts.append(str(ckpt))
    final = g2_dir / "final_model"
    if final.exists() and str(final) not in ckpts:
        ckpts.append(str(final))
    return ckpts


def main():
    parser = argparse.ArgumentParser(description="Re-run G2 eval only (no retraining)")
    parser.add_argument("--output-dir", required=True,
                        help="v7 output directory (contains G0/G1/G2)")
    parser.add_argument("--model-name", default="EleutherAI/pythia-1b")
    parser.add_argument("--tokens-per-gen", type=int, default=20_000_000)
    parser.add_argument("--checkpoint-interval", type=int, default=5_000_000)
    parser.add_argument("--max-seq-length", type=int, default=2048)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--grad-accum", type=int, default=4)
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"

    config = PilotConfig(
        model_name=args.model_name,
        output_dir=args.output_dir,
        tokens_per_generation=args.tokens_per_gen,
        checkpoint_interval_tokens=args.checkpoint_interval,
        max_seq_length=args.max_seq_length,
        per_device_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
    )

    # Find G2 checkpoints
    ckpt_paths = find_g2_checkpoints(args.output_dir)
    if not ckpt_paths:
        print("ERROR: No G2 checkpoints found", file=sys.stderr)
        sys.exit(1)
    logger.info("Found %d G2 checkpoints: %s", len(ckpt_paths),
                [os.path.basename(p) for p in ckpt_paths])

    # Prepare tokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    vocab_size = tokenizer.vocab_size

    # Prepare holdout data
    logger.info("Preparing holdout data ...")
    _, holdout_dataset = prepare_real_data(config, tokenizer)
    holdout_loader = make_dataloader(holdout_dataset, batch_size=config.ppl_batch_size)

    # Load G1 synthetic data for KL comparison
    g1_synth_path = config.synthetic_data_path(1)
    g1_synth_alt = os.path.join(args.output_dir, "G1", "synth_data")
    prev_gen_token_ids = None
    for synth_path in [g1_synth_path, g1_synth_alt]:
        if os.path.exists(synth_path):
            logger.info("Loading G1 synthetic data from %s for KL ...", synth_path)
            synth_ds = prepare_synthetic_data(synth_path, config, tokenizer)
            prev_gen_token_ids = extract_token_ids(synth_ds, max_tokens=10_000_000)
            logger.info("G1 synth tokens: %d", len(prev_gen_token_ids))
            break
    if prev_gen_token_ids is None:
        logger.warning("G1 synth data not found at %s or %s, skipping KL",
                        g1_synth_path, g1_synth_alt)

    # Evaluate each checkpoint
    metrics_path = os.path.join(args.output_dir, "G2", "metrics.jsonl")
    os.makedirs(os.path.dirname(metrics_path), exist_ok=True)

    all_metrics = []
    for ci, ckpt_path in enumerate(ckpt_paths):
        logger.info("--- Evaluating checkpoint %d/%d: %s ---",
                     ci + 1, len(ckpt_paths), ckpt_path)
        t0 = time.time()

        model = AutoModelForCausalLM.from_pretrained(
            ckpt_path, torch_dtype=torch.bfloat16).to(device)
        model.eval()

        # Generate tokens for n-gram/coverage metrics
        logger.info("Generating %dK tokens for corpus metrics ...",
                     config.metrics_gen_tokens // 1000)
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
        m["generation"] = 2
        m["checkpoint"] = ckpt_path
        m["checkpoint_index"] = ci

        step_str = os.path.basename(ckpt_path).split("-")[-1]
        m["global_step"] = int(step_str) if step_str.isdigit() else config.max_steps
        m["tokens_seen"] = m["global_step"] * config.tokens_per_step
        m["eval_time_sec"] = time.time() - t0

        all_metrics.append(m)
        logger.info(
            "  eff_rank=%.1f  ppl=%.2f  entropy_var=%.4f  unigram_H=%.3f  "
            "coverage=%.4f  (%.0fs)",
            m["spectral_effective_rank"], m["perplexity"],
            m["token_entropy_var"], m["unigram_entropy"],
            m["vocab_coverage"], m["eval_time_sec"],
        )

        del model
        torch.cuda.empty_cache()

    # Write metrics
    with open(metrics_path, "w") as f:
        for m in all_metrics:
            f.write(json.dumps(m, default=str) + "\n")
    logger.info("Metrics written to %s", metrics_path)

    # Print summary
    print(f"\n{'Step':<8} {'eff_rank':<10} {'ppl':<8} {'unigram_H':<10} "
          f"{'coverage':<10} {'KL':<10}")
    print("-" * 60)
    for m in all_metrics:
        kl = m.get("kl_unigram", None)
        kl_s = f"{kl:.4f}" if kl is not None else "—"
        print(f"{m['global_step']:<8} {m['spectral_effective_rank']:<10.1f} "
              f"{m['perplexity']:<8.2f} {m['unigram_entropy']:<10.3f} "
              f"{m['vocab_coverage']:<10.4f} {kl_s:<10}")

    print(f"\nG2 eval complete. {len(all_metrics)} checkpoints evaluated.")


if __name__ == "__main__":
    main()
