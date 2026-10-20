"""Controlled training pipeline with PI-based collapse-aware data mixing.

Trains a language model across multiple generations. G0 trains on real data
(via train.py). G1+ uses a PI controller to dynamically adjust the
real/synthetic data mixing ratio w_t based on spectral effective rank
measured at each checkpoint boundary.

Input:
  - Real data: WikiText (via data_utils.prepare_real_data)
  - Synthetic data: generated from previous generation's model
Output:
  - Trained models at <output_dir>/G{i}/final_model/
  - control_log.jsonl with per-segment controller state and metrics

Dependencies: controller.py, metrics.py, data_utils.py, config.py, train.py, generate.py

Usage:
    python controlled_pipeline.py \
      --output_dir /root/autodl-tmp/output_controlled/ \
      --num_generations 3 \
      --tokens_per_generation 20000000 \
      --Kp 0.01 --Ki 0.005 \
      --r_target 680 \
      --w_init 0.5
"""

import argparse
import json
import logging
import os
import sys
import time

import torch
from torch.utils.data import Dataset as TorchDataset, DataLoader
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    get_linear_schedule_with_warmup,
)

from config import PilotConfig
from controller import CollapseAwareController, ControllerConfig
from data_utils import (
    PackedDataset,
    prepare_real_data,
    prepare_synthetic_data,
    make_dataloader,
)
from metrics import compute_spectral_effective_rank, compute_perplexity

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("controlled_pipeline")


# ---------------------------------------------------------------------------
# Online data mixing
# ---------------------------------------------------------------------------

class MixedDataset(TorchDataset):
    """Online real/synthetic mixing with dynamically adjustable ratio.

    Each sample is independently drawn from real_dataset with probability w,
    or from synthetic_dataset with probability (1 - w). Call set_ratio()
    between training segments to update w without rebuilding the dataloader.
    """

    def __init__(
        self,
        real_dataset: PackedDataset,
        synthetic_dataset: PackedDataset,
        w: float = 0.5,
    ):
        self.real = real_dataset
        self.synthetic = synthetic_dataset
        self.w = w

    def set_ratio(self, w: float):
        self.w = w

    def __len__(self):
        return max(len(self.real), len(self.synthetic))

    def __getitem__(self, idx):
        if torch.rand(1).item() < self.w:
            return self.real[idx % len(self.real)]
        return self.synthetic[idx % len(self.synthetic)]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _infinite_loader(loader: DataLoader):
    """Yield batches indefinitely by cycling through the loader."""
    while True:
        yield from loader


def _save_checkpoint(model, tokenizer, path: str):
    os.makedirs(path, exist_ok=True)
    model.save_pretrained(path)
    tokenizer.save_pretrained(path)


def _append_jsonl(path: str, entry: dict):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(entry, default=str) + "\n")


# ---------------------------------------------------------------------------
# Controlled generation (manual training loop + PI control)
# ---------------------------------------------------------------------------

def run_controlled_generation(
    gen_idx: int,
    real_dataset: PackedDataset,
    synthetic_dataset: PackedDataset,
    holdout_dataset: PackedDataset,
    config: PilotConfig,
    ctrl_config: ControllerConfig,
    model_name_or_path: str,
    device: str,
) -> str:
    """Train one generation with PI-controlled real/synthetic mixing.

    Training is split into segments of config.save_steps optimizer steps.
    After each segment: save checkpoint -> measure spectral effective rank
    -> PI controller step -> update mixing ratio for next segment.

    Uses a manual training loop (not HF Trainer) to allow pausing between
    segments for metric computation and ratio updates.

    Returns path to the final model directory.
    """
    gen_dir = config.gen_dir(gen_idx)
    training_dir = os.path.join(gen_dir, "training")
    final_dir = os.path.join(gen_dir, "final_model")
    log_path = os.path.join(config.output_dir, "control_log.jsonl")

    num_segments = config.max_steps // config.save_steps
    steps_per_seg = config.save_steps

    logger.info("=== Generation %d: %d segments x %d steps (total %d) ===",
                gen_idx, num_segments, steps_per_seg, config.max_steps)

    # --- Model ---
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name_or_path,
        torch_dtype=torch.bfloat16,
        attn_implementation="sdpa",
    ).to(device)

    if config.gradient_checkpointing:
        model.gradient_checkpointing_enable(
            gradient_checkpointing_kwargs={"use_reentrant": False}
        )

    # --- Optimizer & scheduler (mirrors train.py's Trainer setup) ---
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=config.learning_rate,
        weight_decay=config.weight_decay,
    )
    warmup_steps = int(config.max_steps * config.warmup_ratio)
    scheduler = get_linear_schedule_with_warmup(
        optimizer,
        num_warmup_steps=warmup_steps,
        num_training_steps=config.max_steps,
    )

    # --- Data ---
    mixed_ds = MixedDataset(real_dataset, synthetic_dataset, w=ctrl_config.w_init)
    loader = DataLoader(
        mixed_ds,
        batch_size=config.per_device_batch_size,
        shuffle=True,
        num_workers=2,
        pin_memory=True,
    )
    data_iter = _infinite_loader(loader)

    holdout_loader = make_dataloader(holdout_dataset, batch_size=config.ppl_batch_size)
    spectral_loader = make_dataloader(holdout_dataset, batch_size=config.spectral_batch_size)

    # Measure initial rank before constructing controller — auto-set r_target
    # if not explicitly provided (avoids the r_target=50 vs eff_rank~680 clamp bug)
    model.eval()
    init_rank = compute_spectral_effective_rank(
        model, spectral_loader,
        num_samples=config.spectral_num_samples, device=device,
    )["spectral_effective_rank"]

    if ctrl_config.r_target <= 0:
        ctrl_config.r_target = init_rank
        logger.info("  r_target auto-set from initial eff_rank: %.1f", init_rank)

    controller = CollapseAwareController(ctrl_config)
    controller.step(init_rank)
    logger.info("  Initial eff_rank=%.1f, r_target=%.1f", init_rank, ctrl_config.r_target)

    w_t = ctrl_config.w_init
    global_step = 0

    for seg in range(num_segments):
        mixed_ds.set_ratio(w_t)

        logger.info("--- Seg %d/%d | w=%.4f | steps %d->%d ---",
                    seg, num_segments - 1, w_t,
                    global_step, global_step + steps_per_seg)

        # --- Train one segment ---
        model.train()
        t0 = time.time()
        seg_loss = 0.0

        for step_in_seg in range(steps_per_seg):
            optimizer.zero_grad()
            accum_loss = 0.0

            for _ in range(config.gradient_accumulation_steps):
                batch = next(data_iter)
                input_ids = batch["input_ids"].to(device)
                attention_mask = batch["attention_mask"].to(device)
                labels = batch["labels"].to(device)

                with torch.amp.autocast("cuda", dtype=torch.bfloat16):
                    loss = model(
                        input_ids=input_ids,
                        attention_mask=attention_mask,
                        labels=labels,
                    ).loss / config.gradient_accumulation_steps

                loss.backward()
                accum_loss += loss.item()

            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()
            seg_loss += accum_loss

            cur_step = global_step + step_in_seg + 1
            if cur_step % 50 == 0:
                logger.info("  step %d | loss %.4f | lr %.2e",
                            cur_step, accum_loss, scheduler.get_last_lr()[0])

        global_step += steps_per_seg
        avg_loss = seg_loss / steps_per_seg

        # --- Checkpoint ---
        ckpt_path = os.path.join(training_dir, f"checkpoint-{global_step}")
        _save_checkpoint(model, tokenizer, ckpt_path)

        # --- Measure spectral rank & perplexity ---
        model.eval()
        eff_rank = compute_spectral_effective_rank(
            model, spectral_loader,
            num_samples=config.spectral_num_samples, device=device,
        )["spectral_effective_rank"]

        ppl = compute_perplexity(
            model, holdout_loader,
            num_samples=config.ppl_num_samples, device=device,
        )["perplexity"]

        # --- PI controller step ---
        w_t = controller.step(eff_rank)
        state = controller.get_state()

        entry = {
            "generation": gen_idx,
            "segment": seg,
            "step": global_step,
            "eff_rank": round(eff_rank, 2),
            "w_t": round(w_t, 4),
            "ppl": round(ppl, 2),
            "proportional": round(state["proportional_term"], 6),
            "integral": round(state["integral_term"], 6),
        }
        _append_jsonl(log_path, entry)

        logger.info("  rank=%.1f | w_t=%.4f | ppl=%.2f (%.0fs)",
                    eff_rank, w_t, ppl, time.time() - t0)

    # --- Save final model ---
    _save_checkpoint(model, tokenizer, final_dir)
    logger.info("Final model -> %s", final_dir)

    del model
    torch.cuda.empty_cache()
    return final_dir


# ---------------------------------------------------------------------------
# Multi-generation orchestrator
# ---------------------------------------------------------------------------

def run_controlled_pipeline(config: PilotConfig, ctrl_config: ControllerConfig):
    """Multi-generation pipeline: G0 on real data, G1+ with PI-controlled mixing."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    os.makedirs(config.output_dir, exist_ok=True)

    logger.info("=" * 60)
    logger.info("CONTROLLED PIPELINE")
    logger.info("  Model: %s | Gens: %d | Tokens/gen: %dM",
                config.model_name, config.num_generations,
                config.tokens_per_generation // 1_000_000)
    logger.info("  PI: Kp=%.4f Ki=%.4f r_target=%.1f w=[%.2f, %.2f, %.2f]",
                ctrl_config.Kp, ctrl_config.Ki, ctrl_config.r_target,
                ctrl_config.w_min, ctrl_config.w_init, ctrl_config.w_max)
    logger.info("=" * 60)

    tokenizer = AutoTokenizer.from_pretrained(config.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    real_train, holdout = prepare_real_data(config, tokenizer)
    prev_model_dir: str | None = None

    for g in range(config.num_generations):
        logger.info("=" * 60)
        logger.info("GENERATION %d / %d", g, config.num_generations - 1)
        logger.info("=" * 60)

        if g == 0:
            # G0: standard training on real data only (no mixing needed)
            from train import train_generation
            final_dir, _ = train_generation(
                gen_idx=g,
                train_dataset=real_train,
                config=config,
            )
        else:
            synth_path = config.synthetic_data_path(g - 1)
            synthetic = prepare_synthetic_data(synth_path, config, tokenizer)

            final_dir = run_controlled_generation(
                gen_idx=g,
                real_dataset=real_train,
                synthetic_dataset=synthetic,
                holdout_dataset=holdout,
                config=config,
                ctrl_config=ctrl_config,
                model_name_or_path=prev_model_dir or config.model_name,
                device=device,
            )

        # Generate synthetic data for next generation
        if g < config.num_generations - 1:
            logger.info("Generating synthetic data from G%d ...", g)
            from generate import generate_synthetic_data
            gen_model = AutoModelForCausalLM.from_pretrained(
                final_dir, torch_dtype=torch.bfloat16
            ).to(device)
            gen_tok = AutoTokenizer.from_pretrained(config.model_name)
            if gen_tok.pad_token is None:
                gen_tok.pad_token = gen_tok.eos_token

            generate_synthetic_data(
                model=gen_model,
                tokenizer=gen_tok,
                num_tokens=config.tokens_per_generation,
                config=config,
                output_dir=config.synthetic_data_path(g),
            )
            del gen_model
            torch.cuda.empty_cache()

        prev_model_dir = final_dir

    logger.info("CONTROLLED PIPELINE COMPLETE")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="PI-controlled collapse-aware training pipeline"
    )
    # PilotConfig overrides
    p.add_argument("--output_dir", type=str, default="./output_controlled")
    p.add_argument("--num_generations", type=int, default=3)
    p.add_argument("--tokens_per_generation", type=int, default=20_000_000)
    p.add_argument("--checkpoint_interval_tokens", type=int, default=10_000_000)
    p.add_argument("--model_name", type=str, default="EleutherAI/pythia-1b")
    p.add_argument("--per_device_batch_size", type=int, default=8)
    p.add_argument("--gradient_accumulation_steps", type=int, default=4)
    p.add_argument("--learning_rate", type=float, default=2e-6)
    p.add_argument("--no_wandb", action="store_true")
    p.add_argument("--seed", type=int, default=42)
    # ControllerConfig
    p.add_argument("--Kp", type=float, default=0.01)
    p.add_argument("--Ki", type=float, default=0.005)
    p.add_argument("--r_target", type=float, default=0,
                   help="PI target rank. 0 = auto from initial eff_rank measurement")
    p.add_argument("--w_init", type=float, default=0.5)
    p.add_argument("--w_min", type=float, default=0.1)
    p.add_argument("--w_max", type=float, default=0.9)
    return p.parse_args()


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
        use_wandb=not args.no_wandb,
        seed=args.seed,
    )

    ctrl_config = ControllerConfig(
        Kp=args.Kp,
        Ki=args.Ki,
        r_target=args.r_target,
        w_init=args.w_init,
        w_min=args.w_min,
        w_max=args.w_max,
    )

    run_controlled_pipeline(config, ctrl_config)


if __name__ == "__main__":
    main()
