#!/usr/bin/env python3
"""ACIB-S training: fine-tune SmolVLA with action-conditioned information bottleneck.

Loads pretrained SmolVLA, wraps with ACIBPolicy, trains on LIBERO data.
Freezes VLM backbone, trains Action Expert + ACIB Scorer.

Usage:
    MUJOCO_GL=egl python scripts/train_acib.py \
        --model_id lerobot/smolvla_base \
        --dataset_id lerobot/libero \
        --hidden_dim 64 \
        --alpha 1.0 \
        --beta 0.01 \
        --mode soft \
        --steps 20000 \
        --batch_size 64 \
        --lr 1e-4 \
        --gpu 0 \
        --output_dir outputs/acib_s_h64 \
        --seed 42 \
        --wandb_project acib

Requires: lerobot[smolvla], LIBERO installed.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import torch
import torch.nn as nn

# Add parent dir to path for acib imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from acib.config import ACIBConfig
from acib.acib_policy import ACIBPolicy


def parse_args():
    parser = argparse.ArgumentParser(description="ACIB-S training")

    # Model / data
    parser.add_argument("--model_id", type=str, default="lerobot/smolvla_base")
    parser.add_argument("--dataset_id", type=str, default="lerobot/libero")

    # ACIB config
    parser.add_argument("--hidden_dim", type=int, default=64, choices=[64, 128])
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--beta", type=float, default=0.01)
    parser.add_argument("--mode", type=str, default="soft", choices=["soft", "hard"])
    parser.add_argument("--top_k_ratio", type=float, default=0.8)
    parser.add_argument("--condition_source", type=str, default="language",
                        choices=["language", "state", "both"])

    # Training
    parser.add_argument("--steps", type=int, default=20000)
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--warmup_steps", type=int, default=1000)
    parser.add_argument("--grad_clip", type=float, default=1.0)
    parser.add_argument("--eval_freq", type=int, default=2000)
    parser.add_argument("--save_freq", type=int, default=5000)
    parser.add_argument("--dtype", type=str, default="bfloat16",
                        choices=["float32", "bfloat16", "float16"])

    # Infra
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="outputs/acib_s")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb_project", type=str, default="")
    parser.add_argument("--wandb_run_name", type=str, default="")

    return parser.parse_args()


def setup_wandb(args):
    if not args.wandb_project:
        return None
    try:
        import wandb
        run_name = args.wandb_run_name or f"acib-{args.mode}-h{args.hidden_dim}-a{args.alpha}-b{args.beta}-s{args.seed}"
        run = wandb.init(
            project=args.wandb_project,
            name=run_name,
            config=vars(args),
        )
        return run
    except ImportError:
        print("wandb not installed, skipping logging")
        return None


def build_acib_policy(args) -> ACIBPolicy:
    acib_config = ACIBConfig(
        hidden_dim=args.hidden_dim,
        alpha=args.alpha,
        beta=args.beta,
        mode=args.mode,
        top_k_ratio=args.top_k_ratio,
        condition_source=args.condition_source,
        freeze_vlm=True,
    )

    print(f"Loading base model: {args.model_id}")
    policy = ACIBPolicy.from_pretrained(args.model_id, acib_config)

    trainable = sum(p.numel() for p in policy.parameters() if p.requires_grad)
    total = sum(p.numel() for p in policy.parameters())
    print(f"Parameters: {total:,} total, {trainable:,} trainable ({trainable/total:.1%})")

    return policy


def build_dataloader(args):
    """Build LeRobot dataloader for LIBERO.

    [NEEDS_SOURCE_VERIFICATION] DataLoader API may vary by lerobot version.
    """
    from lerobot.datasets.lerobot_dataset import LeRobotDataset

    print(f"Loading dataset: {args.dataset_id}")
    dataset = LeRobotDataset(args.dataset_id)
    print(f"Dataset: {len(dataset)} frames")

    dataloader = torch.utils.data.DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=4,
        pin_memory=True,
        drop_last=True,
    )
    return dataloader


def train(args):
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    torch.manual_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    dtype_map = {
        "float32": torch.float32,
        "bfloat16": torch.bfloat16,
        "float16": torch.float16,
    }
    dtype = dtype_map[args.dtype]

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save config
    with open(output_dir / "config.json", "w") as f:
        json.dump(vars(args), f, indent=2)

    wandb_run = setup_wandb(args)

    policy = build_acib_policy(args).to(device)
    dataloader = build_dataloader(args)

    # Optimizer: only trainable params
    trainable_params = [p for p in policy.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(trainable_params, lr=args.lr, betas=(0.9, 0.95))

    # Cosine schedule with warmup
    def lr_lambda(step):
        if step < args.warmup_steps:
            return step / max(1, args.warmup_steps)
        progress = (step - args.warmup_steps) / max(1, args.steps - args.warmup_steps)
        return 0.5 * (1.0 + torch.cos(torch.tensor(progress * 3.14159)).item())

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

    print(f"\nStarting ACIB-{args.mode.upper()} training")
    print(f"  Hidden dim: {args.hidden_dim}")
    print(f"  Alpha (consistency): {args.alpha}")
    print(f"  Beta (IB): {args.beta}")
    print(f"  Steps: {args.steps}")
    print(f"  Batch size: {args.batch_size}")
    print(f"  Device: {device}, dtype: {args.dtype}")

    global_step = 0
    data_iter = iter(dataloader)
    t0 = time.time()

    while global_step < args.steps:
        try:
            batch = next(data_iter)
        except StopIteration:
            data_iter = iter(dataloader)
            batch = next(data_iter)

        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v
                 for k, v in batch.items()}

        with torch.autocast(device_type="cuda", dtype=dtype):
            total_loss, loss_dict = policy(batch)

        optimizer.zero_grad()
        total_loss.backward()
        if args.grad_clip > 0:
            nn.utils.clip_grad_norm_(trainable_params, args.grad_clip)
        optimizer.step()
        scheduler.step()

        global_step += 1

        # Logging
        if global_step % 100 == 0:
            elapsed = time.time() - t0
            steps_per_sec = global_step / elapsed
            scorer_stats = policy.get_scorer_stats()

            log_dict = {
                "train/total_loss": loss_dict["total"].item(),
                "train/task_loss": loss_dict["task"].item(),
                "train/consistency_loss": loss_dict.get("consistency", torch.tensor(0)).item(),
                "train/ib_loss": loss_dict.get("ib", torch.tensor(0)).item(),
                "train/lr": scheduler.get_last_lr()[0],
                "train/steps_per_sec": steps_per_sec,
                **{f"train/{k}": v for k, v in scorer_stats.items()},
            }

            print(f"Step {global_step}/{args.steps} | "
                  f"loss={loss_dict['total'].item():.4f} "
                  f"task={loss_dict['task'].item():.4f} "
                  f"ib={loss_dict.get('ib', torch.tensor(0)).item():.4f} | "
                  f"{steps_per_sec:.1f} steps/s")

            if wandb_run:
                import wandb
                wandb.log(log_dict, step=global_step)

        # Save checkpoint
        if global_step % args.save_freq == 0 or global_step == args.steps:
            ckpt_dir = output_dir / f"checkpoint-{global_step}"
            ckpt_dir.mkdir(exist_ok=True)
            torch.save({
                "step": global_step,
                "policy_state_dict": policy.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "config": vars(args),
            }, ckpt_dir / "checkpoint.pt")
            print(f"  Saved checkpoint to {ckpt_dir}")

    total_time = time.time() - t0
    print(f"\nTraining complete: {args.steps} steps in {total_time/3600:.1f}h")

    if wandb_run:
        wandb_run.finish()


if __name__ == "__main__":
    args = parse_args()
    train(args)
