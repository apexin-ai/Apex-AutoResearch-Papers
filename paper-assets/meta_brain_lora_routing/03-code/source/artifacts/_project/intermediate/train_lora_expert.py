"""
Phase 1 LoRA Expert Training for Meta-Brain Perturbation-Adaptive Routing.

Trains perturbation-specific LoRA adapters on frozen pi0 base model using
flow-matching action prediction loss. Each adapter specializes in one
perturbation type (visual/spatial/physical) or all types (universal).

Input:
    - pi0_base checkpoint: /root/autodl-tmp/checkpoints/pi0_base/model.safetensors
    - LIBERO-Plus rollout data (or synthetic for --dry_run)
Output:
    - PEFT LoRA adapter in /root/meta_brain_lora_routing/checkpoints/lora_{type}_r16/

Usage:
    # Dry-run (validate model loading, LoRA injection, forward/backward)
    python phase1/train_lora_expert.py --perturbation_type visual --gpu_id 0 --dry_run

    # Full training (4 GPUs in parallel, one adapter per GPU)
    python phase1/train_lora_expert.py --perturbation_type visual   --gpu_id 0 &
    python phase1/train_lora_expert.py --perturbation_type spatial  --gpu_id 1 &
    python phase1/train_lora_expert.py --perturbation_type physical --gpu_id 2 &
    python phase1/train_lora_expert.py --perturbation_type universal --gpu_id 3 &

Dependencies: torch, peft, safetensors, wandb, openpi (PI0Pytorch model)
"""

import sys

sys.path.insert(0, "/root/openpi/src")

import argparse
import logging
import math
import os
import time
from pathlib import Path

import safetensors.torch
import torch
import wandb
from peft import LoraConfig, get_peft_model

import openpi.models.pi0_config as pi0_config
import openpi.models_pytorch.pi0_pytorch as pi0_pytorch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import VisualAugmentation, create_dataloader

log = logging.getLogger(__name__)

# LoRA targets: PaliGemma attention Q/K/V/O on all 18 layers.
# Regex must fullmatch against module paths from model.named_modules().
# Excludes action expert (gemma_expert) -- Phase 0 showed it doesn't encode
# perturbation differences.
PALIGEMMA_ATTN_REGEX = (
    r"paligemma_with_expert\.paligemma\.model\.language_model\."
    r"layers\.\d+\.self_attn\.(q|k|v|o)_proj"
)

PERTURBATION_TYPES = ["visual", "spatial", "physical", "universal"]

DEFAULT_CHECKPOINT = "/root/autodl-tmp/checkpoints/pi0_base"
DEFAULT_OUTPUT_DIR = "/root/meta_brain_lora_routing/checkpoints"


def parse_args():
    p = argparse.ArgumentParser(
        description="Train perturbation-specific LoRA adapter on frozen pi0"
    )
    p.add_argument(
        "--perturbation_type",
        required=True,
        choices=PERTURBATION_TYPES,
    )
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument(
        "--dry_run",
        action="store_true",
        help="Run 2 steps with synthetic data to validate code path",
    )

    g = p.add_argument_group("model")
    g.add_argument("--checkpoint", default=DEFAULT_CHECKPOINT)
    g.add_argument("--output_dir", default=DEFAULT_OUTPUT_DIR)

    g = p.add_argument_group("lora")
    g.add_argument("--lora_rank", type=int, default=16)
    g.add_argument("--lora_alpha", type=int, default=32)
    g.add_argument("--lora_dropout", type=float, default=0.05)

    g = p.add_argument_group("training")
    g.add_argument("--lr", type=float, default=2e-4)
    g.add_argument("--batch_size", type=int, default=2)
    g.add_argument("--num_train_steps", type=int, default=30000)
    g.add_argument("--warmup_steps", type=int, default=100)
    g.add_argument("--log_interval", type=int, default=50)
    g.add_argument("--save_interval", type=int, default=1000)
    g.add_argument("--eval_interval", type=int, default=500)
    g.add_argument("--grad_clip_norm", type=float, default=1.0)
    g.add_argument("--weight_decay", type=float, default=0.01)
    g.add_argument(
        "--patience",
        type=int,
        default=3,
        help="Early stop after N eval checkpoints without improvement",
    )

    g = p.add_argument_group("wandb")
    g.add_argument("--wandb_project", default="meta_brain_lora_routing")
    g.add_argument("--no_wandb", action="store_true")

    g = p.add_argument_group("data")
    g.add_argument(
        "--data_dir", default="/root/meta_brain_lora_routing/rollouts"
    )
    g.add_argument("--seed", type=int, default=42)

    return p.parse_args()


def setup_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
    )
    handler.flush = lambda: handler.stream.flush()
    logging.root.addHandler(handler)
    logging.root.setLevel(logging.INFO)


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------


def load_pi0_model(checkpoint_path, device):
    """Load PI0Pytorch model and weights from safetensors checkpoint."""
    log.info("Creating PI0 model (gemma_2b + gemma_300m)...")
    config = pi0_config.Pi0Config(
        dtype="bfloat16",
        action_dim=32,
        action_horizon=50,
    )
    model = pi0_pytorch.PI0Pytorch(config)

    model_path = os.path.join(checkpoint_path, "model.safetensors")
    log.info(f"Loading weights from {model_path}...")
    safetensors.torch.load_model(model, model_path)
    model = model.to(device)
    log.info("PI0 model loaded")
    return model


def apply_lora(model, rank, alpha, dropout):
    """Freeze base model and inject PEFT LoRA into PaliGemma attention."""
    for param in model.parameters():
        param.requires_grad = False

    lora_config = LoraConfig(
        r=rank,
        lora_alpha=alpha,
        target_modules=PALIGEMMA_ATTN_REGEX,
        lora_dropout=dropout,
        bias="none",
    )
    model = get_peft_model(model, lora_config)

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    log.info(
        f"LoRA injected: {trainable:,} trainable / {total:,} total "
        f"({100 * trainable / total:.2f}%)"
    )
    model.print_trainable_parameters()
    return model


# ---------------------------------------------------------------------------
# LR schedule
# ---------------------------------------------------------------------------


def cosine_lr(step, warmup_steps, peak_lr, total_steps):
    """Linear warmup then cosine decay to 5% of peak."""
    if step < warmup_steps:
        return peak_lr * (step + 1) / (warmup_steps + 1)
    end_lr = peak_lr * 0.05
    progress = min(1.0, (step - warmup_steps) / max(1, total_steps - warmup_steps))
    return end_lr + (peak_lr - end_lr) * 0.5 * (1 + math.cos(math.pi * progress))


# ---------------------------------------------------------------------------
# Device transfer
# ---------------------------------------------------------------------------


def obs_to_device(observation, device):
    """Move observation fields to device."""
    observation.images = {k: v.to(device) for k, v in observation.images.items()}
    observation.image_masks = {k: v.to(device) for k, v in observation.image_masks.items()}
    observation.state = observation.state.to(device)
    observation.tokenized_prompt = observation.tokenized_prompt.to(device)
    observation.tokenized_prompt_mask = observation.tokenized_prompt_mask.to(device)
    return observation


# ---------------------------------------------------------------------------
# Main training loop
# ---------------------------------------------------------------------------


def train(args):
    device = torch.device(f"cuda:{args.gpu_id}")
    torch.cuda.set_device(device)
    torch.manual_seed(args.seed)

    run_name = f"lora_{args.perturbation_type}_r{args.lora_rank}"
    save_dir = Path(args.output_dir) / run_name
    save_dir.mkdir(parents=True, exist_ok=True)

    # W&B
    if args.dry_run or args.no_wandb:
        wandb.init(mode="disabled")
    else:
        wandb.init(project=args.wandb_project, name=run_name, config=vars(args))

    # Load model + LoRA
    model = load_pi0_model(args.checkpoint, device)
    model = apply_lora(model, args.lora_rank, args.lora_alpha, args.lora_dropout)

    # Visual augmentation for LoRA-V
    visual_aug = (
        VisualAugmentation(severity=0.5)
        if args.perturbation_type == "visual"
        else None
    )

    # Optimizer on LoRA params only
    trainable_params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(
        trainable_params,
        lr=args.lr,
        betas=(0.9, 0.95),
        eps=1e-8,
        weight_decay=args.weight_decay,
    )

    # Data
    num_steps = 2 if args.dry_run else args.num_train_steps
    train_loader = create_dataloader(
        perturbation_type=args.perturbation_type,
        batch_size=args.batch_size,
        dry_run=args.dry_run,
        data_dir=args.data_dir,
        seed=args.seed,
    )

    # Training
    model.train()
    global_step = 0
    losses_accum = []
    t0 = time.time()

    log.info(f"=== Training {run_name} ===")
    log.info(f"  device={device}, perturbation={args.perturbation_type}")
    log.info(f"  lora_rank={args.lora_rank}, alpha={args.lora_alpha}")
    log.info(f"  lr={args.lr}, batch_size={args.batch_size}, steps={num_steps}")

    while global_step < num_steps:
        for observation, actions in train_loader:
            if global_step >= num_steps:
                break

            observation = obs_to_device(observation, device)
            actions = actions.to(torch.float32).to(device)

            if visual_aug is not None:
                observation.images = visual_aug(observation.images)

            # LR schedule
            lr = cosine_lr(global_step, args.warmup_steps, args.lr, num_steps)
            for pg in optimizer.param_groups:
                pg["lr"] = lr

            # Forward: flow-matching action prediction loss
            losses = model(observation, actions)
            if isinstance(losses, (list, tuple)):
                losses = torch.stack(losses)
            loss = losses.mean()

            # Backward
            loss.backward()
            grad_norm = torch.nn.utils.clip_grad_norm_(
                trainable_params, max_norm=args.grad_clip_norm
            )
            optimizer.step()
            optimizer.zero_grad(set_to_none=True)

            losses_accum.append(loss.item())

            # Log
            if (
                global_step % args.log_interval == 0
                or global_step == num_steps - 1
            ):
                avg_loss = sum(losses_accum) / len(losses_accum)
                elapsed = time.time() - t0
                log.info(
                    f"step={global_step} loss={avg_loss:.4f} lr={lr:.2e} "
                    f"grad_norm={float(grad_norm):.2f} "
                    f"elapsed={elapsed:.1f}s"
                )
                wandb.log(
                    {
                        "train/loss": avg_loss,
                        "train/lr": lr,
                        "train/grad_norm": float(grad_norm),
                    },
                    step=global_step,
                )
                losses_accum = []
                t0 = time.time()

            # Save checkpoint
            if (
                not args.dry_run
                and global_step > 0
                and global_step % args.save_interval == 0
            ):
                ckpt_path = save_dir / f"step_{global_step}"
                model.save_pretrained(str(ckpt_path))
                log.info(f"Checkpoint saved: {ckpt_path}")

            global_step += 1

    # Save final
    if not args.dry_run:
        final_path = save_dir / "final"
        model.save_pretrained(str(final_path))
        log.info(f"Final adapter saved: {final_path}")

    if args.dry_run:
        log.info("=== DRY RUN PASSED ===")
        log.info(
            f"  Model loaded, LoRA injected, {global_step} step(s) completed"
        )

    wandb.finish()


def main():
    setup_logging()
    args = parse_args()
    if args.dry_run:
        log.info("=== DRY RUN MODE ===")
    train(args)


if __name__ == "__main__":
    main()
