"""
Baseline: Vanilla π0 fine-tune on SafeLIBERO MVP scenarios.
No SDF, no collision awareness — serves as Phase B baseline.

Usage:
    # Single GPU
    python scripts/train_baseline.py --scene spatial_bowl --seed 0 --gpu 0

    # Multi-GPU
    torchrun --standalone --nnodes=1 --nproc_per_node=4 \
        scripts/train_baseline.py --scene spatial_bowl --seed 0

    # Dry run (2 steps, no wandb)
    python scripts/train_baseline.py --scene spatial_bowl --dry_run
"""

import argparse
import os
import sys
import logging

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "openpi", "src"))

import openpi.models.pi0_config as pi0_config
import openpi.training.config as _config
import openpi.training.weight_loaders as weight_loaders


SCENE_CONFIG = {
    "spatial_bowl": {
        "description": "SafeLIBERO Spatial: bowl between plate and ramekin (Level II)",
        "data_subdir": "safelibero_spatial",
    },
    "object_pudding": {
        "description": "SafeLIBERO Object: chocolate pudding to basket (Level I)",
        "data_subdir": "safelibero_object",
    },
}

CHECKPOINT_BASE = "./checkpoints"
DATA_BASE = "./data"
WEIGHTS_BASE = "./weights"


def parse_args():
    parser = argparse.ArgumentParser(description="Baseline π0 LoRA fine-tune")
    parser.add_argument("--scene", type=str, required=True, choices=list(SCENE_CONFIG.keys()))
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--gpu", type=int, default=0, help="GPU id (single-GPU mode)")
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--num_train_steps", type=int, default=30000)
    parser.add_argument("--lr", type=float, default=2.5e-5)
    parser.add_argument("--save_interval", type=int, default=2000)
    parser.add_argument("--log_interval", type=int, default=100)
    parser.add_argument("--exp_name", type=str, default=None)
    parser.add_argument("--dry_run", action="store_true", help="Quick 2-step test without wandb")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--data_dir", type=str, default=None, help="Override data directory")
    parser.add_argument("--weight_path", type=str, default=None, help="Override base weight path")
    return parser.parse_args()


def build_config(args) -> _config.TrainConfig:
    scene_cfg = SCENE_CONFIG[args.scene]
    data_dir = args.data_dir or os.path.join(DATA_BASE, scene_cfg["data_subdir"])
    weight_path = args.weight_path or os.path.join(WEIGHTS_BASE, "pi0_base", "params")
    exp_name = args.exp_name or f"baseline_{args.scene}_seed{args.seed}"
    ckpt_dir = os.path.join(CHECKPOINT_BASE, f"baseline_{args.scene}_{args.seed}")

    num_steps = 2 if args.dry_run else args.num_train_steps

    model_config = pi0_config.Pi0Config(
        paligemma_variant="gemma_2b_lora",
        action_expert_variant="gemma_300m_lora",
        action_dim=7,
        action_horizon=50,
    )

    from openpi.training.optimizer import CosineDecaySchedule

    config = _config.TrainConfig(
        name=f"baseline_{args.scene}",
        project_name="colliforce-vla",
        exp_name=exp_name,
        model=model_config,
        data=_config.LeRobotLiberoDataConfig(
            repo_id=data_dir,
            base_config=_config.DataConfig(prompt_from_task=True),
            extra_delta_transform=True,
        ),
        weight_loader=weight_loaders.CheckpointWeightLoader(weight_path),
        freeze_filter=model_config.get_freeze_filter(),
        ema_decay=None,
        lr_schedule=CosineDecaySchedule(
            warmup_steps=min(1000, num_steps // 3),
            peak_lr=args.lr,
            decay_steps=num_steps,
            decay_lr=args.lr / 10,
        ),
        num_train_steps=num_steps,
        batch_size=args.batch_size,
        save_interval=args.save_interval if not args.dry_run else num_steps,
        log_interval=args.log_interval if not args.dry_run else 1,
        checkpoint_base_dir=CHECKPOINT_BASE,
        seed=args.seed,
        wandb_enabled=not args.dry_run,
        overwrite=args.dry_run,
        resume=args.resume,
    )

    return config


def main():
    args = parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    if not int(os.environ.get("WORLD_SIZE", "1")) > 1:
        os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    scene_cfg = SCENE_CONFIG[args.scene]
    logging.info("Scene: %s", scene_cfg["description"])
    logging.info("Seed: %d, Dry run: %s", args.seed, args.dry_run)

    data_dir = args.data_dir or os.path.join(DATA_BASE, scene_cfg["data_subdir"])
    weight_path = args.weight_path or os.path.join(WEIGHTS_BASE, "pi0_base", "params")

    if not os.path.exists(data_dir):
        logging.error("Data directory not found: %s", data_dir)
        logging.error("Run the data pipeline first (Worker 2)")
        sys.exit(1)

    if not os.path.exists(weight_path):
        logging.error("Base weights not found: %s", weight_path)
        logging.error("Download pi0_base checkpoint first (Worker 1)")
        sys.exit(1)

    config = build_config(args)
    logging.info("Checkpoint dir: %s", config.checkpoint_dir)
    logging.info("Training steps: %d, Batch size: %d, LR: %.2e",
                 config.num_train_steps, config.batch_size, args.lr)

    from scripts.train_pytorch import train_loop
    train_loop(config)


if __name__ == "__main__":
    main()
