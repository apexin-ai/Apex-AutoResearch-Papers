"""
Pi0.5 LoRA Baseline Training (No SDF/EE Auxiliary Loss)

Control experiment for A1 SDF auxiliary loss ablation.
Identical training schedule (Phase 1: LoRA frozen, Phase 2: LoRA unfrozen + warmup)
with only action loss, no SDF decoder or EE extractor.

Fork of: train_a1_sdf_aux_pi05.py
Removed: SDF decoder, EE extractor, lambda_sdf, lambda_ee
Purpose: Attribute CAR improvement to SDF signal vs LoRA fine-tuning alone

Usage:
  python scripts/train_pi05_lora_baseline.py --scene object_pudding --seed 0 --gpu 0
"""
import argparse
import logging
import os
import sys

import torch
import torch.nn as nn

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "openpi"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "openpi", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

os.environ["HF_LEROBOT_HOME"] = "./data"

import openpi.models.pi0_config as pi0_config
import openpi.training.config as _config
from openpi.training.optimizer import CosineDecaySchedule
from openpi.training.config import AssetsConfig

from colliforce.lora_utils import inject_lora_pi0
from scripts.train_pytorch import TrainHooks, train_loop


SCENE_CONFIG = {
    "spatial_bowl": {
        "description": "SafeLIBERO Spatial: bowl between plate and ramekin",
        "data_subdir": "safelibero_spatial",
        "assets_dir": "./assets/baseline_spatial_bowl",
    },
    "object_pudding": {
        "description": "SafeLIBERO Object: pick chocolate pudding into basket",
        "data_subdir": "safelibero_object",
        "assets_dir": "./assets/baseline_object_pudding",
    },
}

CHECKPOINT_BASE = "./checkpoints"
DATA_BASE = "./data"
WEIGHTS_BASE = "./weights"


def parse_args():
    p = argparse.ArgumentParser(description="Pi0.5 LoRA Baseline (no SDF/EE aux)")
    p.add_argument("--scene", type=str, required=True, choices=list(SCENE_CONFIG.keys()))
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--gpu", type=int, default=3)
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--num_train_steps", type=int, default=30000)
    p.add_argument("--lr", type=float, default=2.5e-5)
    p.add_argument("--save_interval", type=int, default=2000)
    p.add_argument("--log_interval", type=int, default=100)
    p.add_argument("--exp_name", type=str, default=None)
    p.add_argument("--dry_run", action="store_true")
    p.add_argument("--resume", action="store_true")
    p.add_argument("--warmup_phase_steps", type=int, default=5000)
    return p.parse_args()


class LoRABaselineHooks(TrainHooks):
    def __init__(self, args):
        self.args = args
        self.phase = 1
        self.warmup_phase_steps = args.warmup_phase_steps

    def on_model_created(self, model, device):
        _m = model.module if hasattr(model, "module") else model

        # Freeze ALL backbone params
        for p in _m.parameters():
            p.requires_grad = False

        # Inject LoRA (initially frozen for Phase 1)
        self.lora_params, self._pali_lora_params, self._expert_lora_params = inject_lora_pi0(
            _m, pali_rank=16, pali_alpha=16.0, expert_rank=32, expert_alpha=32.0)
        for p in self.lora_params:
            p.requires_grad = False

        n_backbone = sum(p.numel() for p in _m.parameters())
        n_lora = sum(p.numel() for p in self.lora_params)
        logging.info("=== Pi0.5 LoRA Baseline (No Aux) ===")
        logging.info("  Backbone params (incl. LoRA weights): %.2fM", n_backbone / 1e6)
        logging.info("  LoRA PaliGemma (rank=16): %.2fM",
                     sum(p.numel() for p in self._pali_lora_params) / 1e6)
        logging.info("  LoRA Action Expert (rank=32): %.2fM",
                     sum(p.numel() for p in self._expert_lora_params) / 1e6)
        logging.info("  LoRA total (frozen for Phase 1): %.2fM", n_lora / 1e6)
        logging.info("  Phase 1: dummy scalar keeps grad graph alive (LoRA frozen)")
        logging.info("  Phase 2: LoRA (%.2fM) will be unfrozen at step %d",
                     n_lora / 1e6, self.warmup_phase_steps)

        self._dummy = nn.Parameter(torch.zeros(1, device=device))

    def extra_params(self):
        if self.phase == 1:
            return [self._dummy]
        return []

    def on_step_start(self, global_step, model):
        if global_step >= self.warmup_phase_steps and self.phase == 1:
            self.phase = 2
            self._phase2_start = global_step
            self._lora_warmup_steps = 100
            self._lora_warmup_scale = 0.0
            self._lora_grad_hooks = []
            n_unfrozen = 0
            for p in self.lora_params:
                p.requires_grad = True
                n_unfrozen += p.numel()
                h = p.register_hook(lambda grad, s=self: grad * s._lora_warmup_scale)
                self._lora_grad_hooks.append(h)
            logging.info(
                "Phase 2: unfroze %d LoRA params at step %d (LoRA grad warmup: %d steps)",
                n_unfrozen, global_step, self._lora_warmup_steps,
            )

        if self.phase == 2 and hasattr(self, '_phase2_start'):
            steps_in = global_step - self._phase2_start
            if steps_in < self._lora_warmup_steps:
                self._lora_warmup_scale = (steps_in + 1) / self._lora_warmup_steps
            elif hasattr(self, '_lora_grad_hooks') and self._lora_grad_hooks:
                for h in self._lora_grad_hooks:
                    h.remove()
                self._lora_grad_hooks = []
                self._lora_warmup_scale = 1.0
                logging.info("LoRA gradient warmup complete at step %d", global_step)

        # Param verification for first 100 steps
        if global_step < 100 and global_step % 10 == 0:
            _m = model.module if hasattr(model, "module") else model
            trainable = {n: p.numel() for n, p in _m.named_parameters() if p.requires_grad}
            print(f"[Step {global_step}] Trainable params: {sum(trainable.values()):,}")
            print(f"[Step {global_step}] LoRA params: {sum(v for n, v in trainable.items() if 'lora' in n):,}")

    def on_loss_computed(self, action_loss, model, observation, global_step):
        if self.phase == 1:
            action_loss = action_loss + 0.0 * self._dummy
        aux_info = {
            "action_loss": action_loss.item(),
            "phase": float(self.phase),
        }
        return action_loss, aux_info

    def on_save_checkpoint(self, step_dir, global_step):
        torch.save({"phase": self.phase, "global_step": global_step},
                    os.path.join(step_dir, "baseline_metadata.pt"))
        logging.info("Saved baseline metadata at step %d", global_step)

    def on_cleanup(self):
        for h in getattr(self, '_lora_grad_hooks', []):
            h.remove()


def build_config(args):
    scene_cfg = SCENE_CONFIG[args.scene]
    num_steps = 2 if args.dry_run else args.num_train_steps
    exp_name = args.exp_name or f"pi05_lora_baseline_{args.scene}_seed{args.seed}"

    model_config = pi0_config.Pi0Config(
        pi05=True,
        action_horizon=10,
        discrete_state_input=False,
    )

    config = _config.TrainConfig(
        name=f"a1_sdf_pi05_{args.scene}",
        project_name="colliforce-vla",
        exp_name=exp_name,
        model=model_config,
        data=_config.LeRobotLiberoDataConfig(
            repo_id=scene_cfg["data_subdir"],
            base_config=_config.DataConfig(prompt_from_task=True),
            extra_delta_transform=False,
            assets=AssetsConfig(assets_dir=scene_cfg["assets_dir"]),
        ),
        pytorch_weight_path=os.path.join(WEIGHTS_BASE, "pi05_libero"),
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
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", force=True)

    if not int(os.environ.get("WORLD_SIZE", "1")) > 1:
        os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    logging.info("Pi0.5 LoRA Baseline | Scene: %s | Seed: %d | Dry run: %s",
                 args.scene, args.seed, args.dry_run)
    logging.info("Phase 1: %d steps (LoRA frozen, action-only forward), Phase 2: LoRA unfrozen",
                 args.warmup_phase_steps)

    config = build_config(args)
    hooks = LoRABaselineHooks(args)
    train_loop(config, hooks=hooks)


if __name__ == "__main__":
    main()
