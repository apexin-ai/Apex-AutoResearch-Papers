"""Full comparative experiment: pure_synthetic vs fixed_mix vs pi_controller.

Trains a shared G0 baseline on real data, then runs each condition
independently for G1+ with different data mixing strategies:
  1. pure_synthetic — 100% synthetic data each generation
  2. fixed_mix     — fixed real:synthetic ratio (--fixed_ratio)
  3. pi_controller — PI controller dynamically adjusts ratio per checkpoint

Input:  CLI args (--model_name, --num_generations, --conditions, etc.)
Output:
  - <output_dir>/<condition>/summary.json   per-condition results
  - <output_dir>/comparison_summary.json    cross-condition key metrics
  - <output_dir>/comparison.csv             tabular comparison
Deps:   config, controller, data_utils, generate, metrics, train
"""

import argparse
import csv
import json
import logging
import os
import shutil
import sys
import time
from dataclasses import fields

import numpy as np
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

from config import PilotConfig
from controller import CollapseAwareController, ControllerConfig
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
logger = logging.getLogger("experiment")

CONDITION_NAMES = ["pure_synthetic", "fixed_mix", "pi_controller"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_config(base: PilotConfig, **overrides) -> PilotConfig:
    d = {f.name: getattr(base, f.name) for f in fields(base)}
    d.update(overrides)
    return PilotConfig(**d)


def mix_datasets(
    real_dataset: PackedDataset,
    synth_dataset: PackedDataset,
    real_ratio: float,
    total_seqs: int,
    rng: np.random.Generator | None = None,
) -> PackedDataset:
    """Sample from real and synthetic datasets at a given ratio, shuffle, return combined."""
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
    results: list[dict] = []

    for ci, ckpt in enumerate(checkpoint_paths):
        logger.info("--- Eval ckpt %d/%d: %s ---", ci + 1, len(checkpoint_paths), ckpt)
        t0 = time.time()
        model = AutoModelForCausalLM.from_pretrained(ckpt, torch_dtype="auto").to(device)
        model.eval()

        gen_ids = generate_sample_tokens(
            model, tokenizer, num_tokens=config.metrics_gen_tokens,
            batch_size=config.gen_batch_size, max_new_tokens=256,
            temperature=config.gen_temperature, top_p=config.gen_top_p, device=device,
        )
        m = compute_checkpoint_metrics(
            model=model, holdout_loader=holdout_loader,
            gen_token_ids=gen_ids, prev_gen_token_ids=prev_gen_token_ids,
            vocab_size=vocab_size, config=config, device=device,
        )
        m["generation"] = gen_idx
        m["checkpoint"] = ckpt
        m["checkpoint_index"] = ci
        step_str = os.path.basename(ckpt).split("-")[-1]
        m["global_step"] = int(step_str) if step_str.isdigit() else ci
        m["tokens_seen"] = m["global_step"] * config.tokens_per_step
        m["eval_time_sec"] = time.time() - t0
        results.append(m)

        logger.info("  rank=%.1f  ppl=%.2f  (%.0fs)",
                     m["spectral_effective_rank"], m["perplexity"], m["eval_time_sec"])
        del model
        torch.cuda.empty_cache()

    return results


def save_metrics(metrics: list[dict], path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        for m in metrics:
            f.write(json.dumps(m, default=str) + "\n")


# ---------------------------------------------------------------------------
# Condition: pure_synthetic
# ---------------------------------------------------------------------------

def run_pure_synthetic(
    config: PilotConfig,
    g0_final_dir: str,
    g0_synth_path: str,
    real_train: PackedDataset,
    holdout: PackedDataset,
    tokenizer: AutoTokenizer,
    device: str,
    g0_metrics: list[dict],
) -> list[dict]:
    """100% synthetic data each generation (pilot_pipeline behaviour for G1+)."""
    logger.info("==== CONDITION: pure_synthetic ====")
    all_results = list(g0_metrics)
    prev_model_dir = g0_final_dir

    synth_ds = prepare_synthetic_data(g0_synth_path, config, tokenizer)
    prev_gen_token_ids = extract_token_ids(synth_ds, max_tokens=10_000_000)

    for g in range(1, config.num_generations):
        logger.info("=== G%d (pure_synthetic) ===", g)

        synth_path = g0_synth_path if g == 1 else config.synthetic_data_path(g - 1)
        gen_train = prepare_synthetic_data(synth_path, config, tokenizer)

        final_dir, ckpt_paths = train_generation(g, gen_train, config, prev_model_dir)
        if final_dir not in ckpt_paths:
            ckpt_paths.append(final_dir)

        gen_metrics = evaluate_checkpoints(
            ckpt_paths, g, holdout, prev_gen_token_ids, config, device,
        )
        save_metrics(gen_metrics, config.metrics_path(g))
        all_results.extend(gen_metrics)

        if g < config.num_generations - 1:
            model = AutoModelForCausalLM.from_pretrained(final_dir, torch_dtype="auto").to(device)
            generate_synthetic_data(
                model, tokenizer, config.tokens_per_generation,
                config, config.synthetic_data_path(g),
            )
            sd = prepare_synthetic_data(config.synthetic_data_path(g), config, tokenizer)
            prev_gen_token_ids = extract_token_ids(sd, max_tokens=10_000_000)
            del model
            torch.cuda.empty_cache()

        prev_model_dir = final_dir

    return all_results


# ---------------------------------------------------------------------------
# Condition: fixed_mix
# ---------------------------------------------------------------------------

def run_fixed_mix(
    config: PilotConfig,
    g0_final_dir: str,
    g0_synth_path: str,
    real_train: PackedDataset,
    holdout: PackedDataset,
    tokenizer: AutoTokenizer,
    device: str,
    g0_metrics: list[dict],
    fixed_ratio: float,
) -> list[dict]:
    """Fixed real:synthetic ratio each generation."""
    logger.info("==== CONDITION: fixed_mix (ratio=%.2f) ====", fixed_ratio)
    rng = np.random.default_rng(config.seed)
    total_seqs = config.tokens_per_generation // config.max_seq_length
    all_results = list(g0_metrics)
    prev_model_dir = g0_final_dir

    synth_ds = prepare_synthetic_data(g0_synth_path, config, tokenizer)
    prev_gen_token_ids = extract_token_ids(synth_ds, max_tokens=10_000_000)

    for g in range(1, config.num_generations):
        logger.info("=== G%d (fixed_mix) ===", g)

        synth_path = g0_synth_path if g == 1 else config.synthetic_data_path(g - 1)
        synth_dataset = prepare_synthetic_data(synth_path, config, tokenizer)
        gen_train = mix_datasets(real_train, synth_dataset, fixed_ratio, total_seqs, rng)
        logger.info("Mixed %d seqs (%.0f%% real)", len(gen_train), fixed_ratio * 100)

        final_dir, ckpt_paths = train_generation(g, gen_train, config, prev_model_dir)
        if final_dir not in ckpt_paths:
            ckpt_paths.append(final_dir)

        gen_metrics = evaluate_checkpoints(
            ckpt_paths, g, holdout, prev_gen_token_ids, config, device,
        )
        save_metrics(gen_metrics, config.metrics_path(g))
        all_results.extend(gen_metrics)

        if g < config.num_generations - 1:
            model = AutoModelForCausalLM.from_pretrained(final_dir, torch_dtype="auto").to(device)
            generate_synthetic_data(
                model, tokenizer, config.tokens_per_generation,
                config, config.synthetic_data_path(g),
            )
            sd = prepare_synthetic_data(config.synthetic_data_path(g), config, tokenizer)
            prev_gen_token_ids = extract_token_ids(sd, max_tokens=10_000_000)
            del model
            torch.cuda.empty_cache()

        prev_model_dir = final_dir

    return all_results


# ---------------------------------------------------------------------------
# Condition: pi_controller  (segment-level dynamic mixing)
# ---------------------------------------------------------------------------

def train_generation_pi(
    gen_idx: int,
    real_dataset: PackedDataset,
    synth_dataset: PackedDataset,
    config: PilotConfig,
    controller: CollapseAwareController,
    holdout: PackedDataset,
    tokenizer,
    model_path: str,
    device: str,
    prev_gen_token_ids: list[int] | None = None,
) -> tuple[str, list[str], list[dict]]:
    """Train one generation with PI controller adjusting mix ratio at each checkpoint interval.

    Breaks training into segments of save_steps steps. After each segment
    the spectral effective rank is computed, the controller is updated,
    and the mixing ratio is adjusted for the next segment.
    Optimizer state (Adam m/v) is preserved across segments via resume_from_checkpoint.
    """
    training_dir = os.path.join(config.gen_dir(gen_idx), "training")
    final_dir = os.path.join(config.gen_dir(gen_idx), "final_model")
    num_segments = config.max_steps // config.save_steps
    total_seqs = config.tokens_per_generation // config.max_seq_length
    rng = np.random.default_rng(config.seed + gen_idx * 1000)

    vocab_size = tokenizer.vocab_size
    holdout_loader = make_dataloader(holdout, batch_size=config.ppl_batch_size)
    current_model_path = model_path or config.model_name
    resume_ckpt: str | None = None

    all_ckpt_paths: list[str] = []
    all_metrics: list[dict] = []

    for seg in range(num_segments):
        w_t = controller._w
        logger.info("  Segment %d/%d: w_t=%.3f", seg + 1, num_segments, w_t)

        mixed = mix_datasets(real_dataset, synth_dataset, w_t, total_seqs, rng)

        model = AutoModelForCausalLM.from_pretrained(current_model_path, torch_dtype="auto")
        if config.gradient_checkpointing:
            model.gradient_checkpointing_enable(
                gradient_checkpointing_kwargs={"use_reentrant": False},
            )

        seg_args = TrainingArguments(
            output_dir=training_dir,
            max_steps=config.save_steps * (seg + 1),
            per_device_train_batch_size=config.per_device_batch_size,
            gradient_accumulation_steps=config.gradient_accumulation_steps,
            learning_rate=config.learning_rate,
            warmup_ratio=0.0,
            weight_decay=config.weight_decay,
            bf16=config.bf16,
            logging_steps=50,
            save_steps=config.save_steps,
            save_total_limit=2,
            seed=config.seed,
            report_to="wandb" if config.use_wandb else "none",
            run_name=f"{config.wandb_run_prefix}_G{gen_idx}_seg{seg}",
            dataloader_num_workers=2,
            dataloader_pin_memory=True,
            remove_unused_columns=False,
        )

        trainer = Trainer(model=model, args=seg_args, train_dataset=mixed)
        trainer.train(resume_from_checkpoint=resume_ckpt)

        # Persist checkpoint with optimizer state for next segment
        global_step = (seg + 1) * config.save_steps
        ckpt_dir = os.path.join(training_dir, f"checkpoint-{global_step}")
        os.makedirs(ckpt_dir, exist_ok=True)
        trainer.save_model(ckpt_dir)
        trainer.save_state()
        tokenizer.save_pretrained(ckpt_dir)
        all_ckpt_paths.append(ckpt_dir)
        current_model_path = ckpt_dir
        resume_ckpt = ckpt_dir

        # Evaluate
        model = model.to(device)
        model.eval()

        gen_ids = generate_sample_tokens(
            model, tokenizer, num_tokens=config.metrics_gen_tokens,
            batch_size=config.gen_batch_size, max_new_tokens=256,
            temperature=config.gen_temperature, top_p=config.gen_top_p,
            device=device,
        )
        m = compute_checkpoint_metrics(
            model=model, holdout_loader=holdout_loader,
            gen_token_ids=gen_ids, prev_gen_token_ids=prev_gen_token_ids,
            vocab_size=vocab_size, config=config, device=device,
        )
        m.update({
            "generation": gen_idx,
            "checkpoint": ckpt_dir,
            "segment": seg,
            "global_step": global_step,
            "tokens_seen": global_step * config.tokens_per_step,
            "w_t": w_t,
        })
        all_metrics.append(m)

        # Controller update
        new_w = controller.step(m["spectral_effective_rank"])
        logger.info("    rank=%.1f  ppl=%.2f  w_t %.3f -> %.3f",
                     m["spectral_effective_rank"], m["perplexity"], w_t, new_w)

        del model, trainer
        torch.cuda.empty_cache()

    # Final model = copy of last checkpoint
    os.makedirs(final_dir, exist_ok=True)
    last_ckpt = all_ckpt_paths[-1]
    for fn in os.listdir(last_ckpt):
        shutil.copy2(os.path.join(last_ckpt, fn), final_dir)

    return final_dir, all_ckpt_paths, all_metrics


def run_pi_controller(
    config: PilotConfig,
    g0_final_dir: str,
    g0_synth_path: str,
    real_train: PackedDataset,
    holdout: PackedDataset,
    tokenizer,
    device: str,
    g0_metrics: list[dict],
    r_target: float | None = None,
    Kp: float = 0.01,
    Ki: float = 0.005,
) -> tuple[list[dict], dict]:
    """PI controller with dynamic mixing ratio adjusted per checkpoint.

    DEPRECATED: Use controlled_pipeline.py for P0 experiments. This function
    uses HF Trainer segments (offline mixing, per-segment LR restart).
    controlled_pipeline.py uses a manual training loop (online per-sample
    mixing, continuous optimizer state + linear LR decay).
    """
    logger.info("==== CONDITION: pi_controller ====")

    # r_target defaults to G0 final eff_rank to avoid the error=627 clamp bug
    if r_target is None and g0_metrics:
        r_target = g0_metrics[-1]["spectral_effective_rank"]
        logger.info("  r_target auto-set from G0 final: %.1f", r_target)
    elif r_target is None:
        raise ValueError("r_target cannot be auto-inferred: no G0 metrics available")

    ctrl_config = ControllerConfig(Kp=Kp, Ki=Ki, r_target=r_target)
    controller = CollapseAwareController(ctrl_config)
    all_results = list(g0_metrics)
    prev_model_dir = g0_final_dir

    synth_ds = prepare_synthetic_data(g0_synth_path, config, tokenizer)
    prev_gen_token_ids = extract_token_ids(synth_ds, max_tokens=10_000_000)

    # Seed controller with G0 final spectral rank
    if g0_metrics:
        controller.step(g0_metrics[-1]["spectral_effective_rank"])

    for g in range(1, config.num_generations):
        logger.info("=== G%d (pi_controller) ===", g)

        synth_path = g0_synth_path if g == 1 else config.synthetic_data_path(g - 1)
        synth_dataset = prepare_synthetic_data(synth_path, config, tokenizer)

        final_dir, ckpt_paths, gen_metrics = train_generation_pi(
            gen_idx=g, real_dataset=real_train, synth_dataset=synth_dataset,
            config=config, controller=controller, holdout=holdout,
            tokenizer=tokenizer, model_path=prev_model_dir, device=device,
            prev_gen_token_ids=prev_gen_token_ids,
        )
        save_metrics(gen_metrics, config.metrics_path(g))
        all_results.extend(gen_metrics)

        if g < config.num_generations - 1:
            model = AutoModelForCausalLM.from_pretrained(final_dir, torch_dtype="auto").to(device)
            generate_synthetic_data(
                model, tokenizer, config.tokens_per_generation,
                config, config.synthetic_data_path(g),
            )
            sd = prepare_synthetic_data(config.synthetic_data_path(g), config, tokenizer)
            prev_gen_token_ids = extract_token_ids(sd, max_tokens=10_000_000)
            del model
            torch.cuda.empty_cache()

        prev_model_dir = final_dir

    return all_results, controller.get_state()


# ---------------------------------------------------------------------------
# Summary / comparison
# ---------------------------------------------------------------------------

def build_condition_summary(
    condition_name: str,
    all_results: list[dict],
    config: PilotConfig,
    extra: dict | None = None,
) -> dict:
    summary: dict = {
        "condition": condition_name,
        "num_checkpoints_evaluated": len(all_results),
        "generations": {},
    }
    for g in range(config.num_generations):
        gm = [m for m in all_results if m["generation"] == g]
        if not gm:
            continue
        gs: dict = {
            "final_spectral_rank": gm[-1]["spectral_effective_rank"],
            "final_ppl": gm[-1]["perplexity"],
            "spectral_rank_trajectory": [m["spectral_effective_rank"] for m in gm],
            "ppl_trajectory": [m["perplexity"] for m in gm],
        }
        if "kl_unigram" in gm[-1]:
            gs["final_kl_unigram"] = gm[-1]["kl_unigram"]
        if "w_t" in gm[-1]:
            gs["w_t_trajectory"] = [m["w_t"] for m in gm]
        summary["generations"][f"G{g}"] = gs
    if extra:
        summary.update(extra)
    return summary


def generate_comparison(
    all_summaries: dict[str, dict],
    output_dir: str,
    config: PilotConfig,
):
    last_gen = f"G{config.num_generations - 1}"

    comparison: dict = {
        "config": {
            "model_name": config.model_name,
            "num_generations": config.num_generations,
            "tokens_per_generation": config.tokens_per_generation,
            "seed": config.seed,
        },
        "conditions": {},
    }
    csv_rows: list[dict] = []

    for cond_name, summary in all_summaries.items():
        fg = summary["generations"].get(last_gen, {})
        entry = {
            "final_spectral_rank": fg.get("final_spectral_rank"),
            "final_ppl": fg.get("final_ppl"),
            "final_kl_unigram": fg.get("final_kl_unigram"),
            "rank_trajectory": {
                gk: gv.get("spectral_rank_trajectory", [])
                for gk, gv in summary["generations"].items()
            },
            "ppl_trajectory": {
                gk: gv.get("ppl_trajectory", [])
                for gk, gv in summary["generations"].items()
            },
        }
        comparison["conditions"][cond_name] = entry
        csv_rows.append({
            "condition": cond_name,
            "final_spectral_rank": fg.get("final_spectral_rank"),
            "final_ppl": fg.get("final_ppl"),
            "final_kl_unigram": fg.get("final_kl_unigram"),
        })

    comp_path = os.path.join(output_dir, "comparison_summary.json")
    with open(comp_path, "w") as f:
        json.dump(comparison, f, indent=2, default=str)

    csv_path = os.path.join(output_dir, "comparison.csv")
    if csv_rows:
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=csv_rows[0].keys())
            writer.writeheader()
            writer.writerows(csv_rows)

    logger.info("Comparison -> %s, %s", comp_path, csv_path)


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def run_experiment(args):
    base_config = PilotConfig(
        model_name=args.model_name,
        num_generations=args.num_generations,
        output_dir=args.output_dir,
        seed=args.seed,
        use_wandb=not args.no_wandb,
    )
    device = "cuda" if torch.cuda.is_available() else "cpu"
    os.makedirs(args.output_dir, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(base_config.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # ---- Shared real data ----
    logger.info("Preparing shared real data ...")
    real_train, holdout = prepare_real_data(base_config, tokenizer)

    # ---- Shared G0 ----
    logger.info("=" * 60)
    logger.info("TRAINING SHARED G0")
    logger.info("=" * 60)
    g0_config = make_config(
        base_config,
        output_dir=os.path.join(args.output_dir, "shared_G0"),
        wandb_run_prefix="shared",
    )
    g0_final_dir, g0_ckpt_paths = train_generation(0, real_train, g0_config)
    if g0_final_dir not in g0_ckpt_paths:
        g0_ckpt_paths.append(g0_final_dir)

    g0_metrics = evaluate_checkpoints(
        g0_ckpt_paths, 0, holdout, None, g0_config, device,
    )

    # ---- Shared G0 synthetic data ----
    g0_synth_path = os.path.join(args.output_dir, "shared_G0_synth")
    if not os.path.exists(g0_synth_path):
        logger.info("Generating shared synthetic data from G0 ...")
        model = AutoModelForCausalLM.from_pretrained(
            g0_final_dir, torch_dtype="auto",
        ).to(device)
        generate_synthetic_data(
            model, tokenizer, base_config.tokens_per_generation,
            base_config, g0_synth_path,
        )
        del model
        torch.cuda.empty_cache()

    # ---- Run conditions ----
    conditions = args.conditions or CONDITION_NAMES
    all_summaries: dict[str, dict] = {}

    for cond in conditions:
        if cond not in CONDITION_NAMES:
            logger.warning("Unknown condition '%s', skipping", cond)
            continue

        cond_config = make_config(
            base_config,
            output_dir=os.path.join(args.output_dir, cond),
            wandb_run_prefix=cond,
        )

        if cond == "pure_synthetic":
            results = run_pure_synthetic(
                cond_config, g0_final_dir, g0_synth_path,
                real_train, holdout, tokenizer, device, g0_metrics,
            )
            summary = build_condition_summary(cond, results, cond_config)

        elif cond == "fixed_mix":
            results = run_fixed_mix(
                cond_config, g0_final_dir, g0_synth_path,
                real_train, holdout, tokenizer, device, g0_metrics,
                args.fixed_ratio,
            )
            summary = build_condition_summary(
                cond, results, cond_config,
                extra={"fixed_ratio": args.fixed_ratio},
            )

        elif cond == "pi_controller":
            results, ctrl_state = run_pi_controller(
                cond_config, g0_final_dir, g0_synth_path,
                real_train, holdout, tokenizer, device, g0_metrics,
                r_target=args.r_target, Kp=args.Kp, Ki=args.Ki,
            )
            summary = build_condition_summary(
                cond, results, cond_config,
                extra={"controller_state": ctrl_state},
            )

        # Save per-condition summary
        cond_summary_path = os.path.join(cond_config.output_dir, "summary.json")
        os.makedirs(cond_config.output_dir, exist_ok=True)
        with open(cond_summary_path, "w") as f:
            json.dump(summary, f, indent=2, default=str)
        logger.info("Condition '%s' summary -> %s", cond, cond_summary_path)

        all_summaries[cond] = summary

    # ---- Cross-condition comparison ----
    generate_comparison(all_summaries, args.output_dir, base_config)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="Comparative experiment: pure_synthetic vs fixed_mix vs pi_controller",
    )
    p.add_argument("--model_name", type=str, default="EleutherAI/pythia-1b")
    p.add_argument("--num_generations", type=int, default=3)
    p.add_argument("--output_dir", type=str, default="./output_experiment")
    p.add_argument("--fixed_ratio", type=float, default=0.618,
                   help="Real data ratio for fixed_mix condition (default: 1/phi ≈ 0.618)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--no_wandb", action="store_true")
    p.add_argument("--conditions", nargs="+", choices=CONDITION_NAMES, default=None,
                   help="Subset of conditions to run (default: all three)")
    p.add_argument("--r_target", type=float, default=None,
                   help="PI controller r_target. None = auto from G0 final eff_rank")
    p.add_argument("--Kp", type=float, default=0.01, help="PI proportional gain")
    p.add_argument("--Ki", type=float, default=0.005, help="PI integral gain")
    return p.parse_args()


def main():
    args = parse_args()
    run_experiment(args)


if __name__ == "__main__":
    main()
