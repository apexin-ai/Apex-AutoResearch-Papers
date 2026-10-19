"""
A1-Pi0.5: Pi0.5 + SDF auxiliary task training via openpi train_loop hooks.

Forked from train_a1_sdf_aux.py (Pi0 version). Key differences:
  - Model: Pi0Config(pi05=True, action_horizon=10, discrete_state_input=False)
  - Weights: pi05_libero checkpoint (not pi0_base)
  - lambda_sdf default: 0.005 (reduced from 0.1 to avoid action collapse)
  - action_horizon: 10 tokens (Pi0=50), affects mean pooling granularity for SDFDecoder

Architecture: Pi0.5 shares PI0Pytorch class (pi05=True flag). Action Expert is identical
(gemma_300m, width=1024), so action_out_proj hook, SDFDecoder, EEExtractor, and LoRA
injection work without modification.

Dependencies:
  - openpi (sys.path: ../openpi/src)
  - colliforce.sdf_decoder, colliforce.ee_extractor, colliforce.lora_utils
  - scripts.train_pytorch (TrainHooks, train_loop)

Input: SafeLIBERO scene data + SDF ground truth
Output: Checkpoint with LoRA params + sdf_decoder.pt + ee_extractor.pt

Usage:
    python scripts/train_a1_sdf_aux_pi05.py --scene spatial_bowl --dry_run
    python scripts/train_a1_sdf_aux_pi05.py --scene spatial_bowl --seed 0 --gpu 0
"""
import argparse
import logging
import os
import sys

import numpy as np
import torch
import torch.nn.functional as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "openpi"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "openpi", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

os.environ["HF_LEROBOT_HOME"] = "./data"

import openpi.models.pi0_config as pi0_config
import openpi.training.config as _config
from openpi.training.optimizer import CosineDecaySchedule
from openpi.training.config import AssetsConfig

from colliforce.sdf_decoder import SDFDecoder, compute_sdf_loss
from colliforce.ee_extractor import EEPositionExtractor
from colliforce.lora_utils import inject_lora_pi0
from scripts.train_pytorch import TrainHooks, train_loop


SCENE_CONFIG = {
    "spatial_bowl": {
        "description": "SafeLIBERO Spatial: bowl between plate and ramekin",
        "data_subdir": "safelibero_spatial",
        "sdf_gt": "./data/sdf_gt_spatial_bowl.npz",
        "assets_dir": "./assets/baseline_spatial_bowl",
    },
    "object_pudding": {
        "description": "SafeLIBERO Object: pick chocolate pudding into basket",
        "data_subdir": "safelibero_object",
        "sdf_gt": "./data/sdf_gt_object_chocolate.npz",
        "assets_dir": "./assets/baseline_object_pudding",
    },
}

CHECKPOINT_BASE = "./checkpoints"
DATA_BASE = "./data"
WEIGHTS_BASE = "./weights"


def parse_args():
    p = argparse.ArgumentParser(description="A1-Pi0.5: Pi0.5 + SDF auxiliary task via hooks")
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
    p.add_argument("--lambda_sdf", type=float, default=0.005,
                   help="SDF loss weight (default 0.005, reduced from Pi0's 0.1 to avoid action collapse)")
    p.add_argument("--lambda_sdf_phase2", type=float, default=None,
                   help="SDF loss weight for Phase 2 (step >= phase1_steps). If None, uses --lambda_sdf throughout.")
    p.add_argument("--lambda_ee", type=float, default=0.01)
    p.add_argument("--n_query_points", type=int, default=64)
    p.add_argument("--sdf_clamp", type=float, default=0.05)
    p.add_argument("--eikonal_weight", type=float, default=0.1)
    p.add_argument("--warmup_phase_steps", type=int, default=5000)
    return p.parse_args()


class SuffixOutHook:
    """Captures input to action_out_proj (= suffix_out after slicing)."""
    def __init__(self):
        self.features = None

    def __call__(self, module, input, output):
        self.features = input[0]  # [B, action_horizon, 1024]


def load_sdf_gt(path, device):
    data = np.load(path)
    query_points = torch.tensor(data["query_points"], dtype=torch.float32, device=device)
    sdf_values = torch.tensor(data["sdf_values"], dtype=torch.float32, device=device)
    return query_points, sdf_values


def sample_sdf_batch(query_points, sdf_values, batch_size, n_query):
    indices = torch.randint(0, len(query_points), (n_query,), device=query_points.device)
    pts = query_points[indices].unsqueeze(0).expand(batch_size, -1, -1)
    sdf = sdf_values[indices].unsqueeze(0).expand(batch_size, -1)
    return pts, sdf


class SdfAuxHooks(TrainHooks):
    def __init__(self, args):
        self.args = args
        self.phase = 1
        self.warmup_phase_steps = args.warmup_phase_steps
        self.lambda_sdf = args.lambda_sdf
        self.lambda_sdf_phase2 = args.lambda_sdf_phase2 if args.lambda_sdf_phase2 is not None else args.lambda_sdf
        self.lambda_ee = args.lambda_ee
        self.n_query_points = args.n_query_points

        self.sdf_decoder = SDFDecoder(feature_dim=1024, hidden_dim=256)
        self.ee_extractor = EEPositionExtractor(feature_dim=1024, hidden_dim=256)

        self.suffix_hook = SuffixOutHook()
        self.hook_handle = None
        self.sdf_query = None
        self.sdf_values = None

    def on_model_created(self, model, device):
        _m = model.module if hasattr(model, "module") else model
        self.hook_handle = _m.action_out_proj.register_forward_hook(self.suffix_hook)

        self.sdf_decoder = self.sdf_decoder.to(device)
        self.ee_extractor = self.ee_extractor.to(device)

        scene_cfg = SCENE_CONFIG[self.args.scene]
        self.sdf_query, self.sdf_values = load_sdf_gt(scene_cfg["sdf_gt"], device)
        logging.info("SDF GT loaded: %d points", len(self.sdf_query))

        # Freeze ALL backbone params
        for p in _m.parameters():
            p.requires_grad = False

        # Inject LoRA (initially frozen for Phase 1)
        self.lora_params, self._pali_lora_params, self._expert_lora_params = inject_lora_pi0(
            _m, pali_rank=16, pali_alpha=16.0, expert_rank=32, expert_alpha=32.0)
        for p in self.lora_params:
            p.requires_grad = False

        # Unfreeze aux modules
        for p in self.sdf_decoder.parameters():
            p.requires_grad = True
        for p in self.ee_extractor.parameters():
            p.requires_grad = True

        n_backbone = sum(p.numel() for p in _m.parameters())
        n_lora = sum(p.numel() for p in self.lora_params)
        n_sdf = sum(p.numel() for p in self.sdf_decoder.parameters())
        n_ee = sum(p.numel() for p in self.ee_extractor.parameters())
        logging.info("=== A1-Pi0.5 SDF Aux Hooks ===")
        logging.info("  Backbone params (incl. LoRA weights): %.2fM", n_backbone / 1e6)
        logging.info("  LoRA PaliGemma (rank=16): %.2fM",
                     sum(p.numel() for p in self._pali_lora_params) / 1e6)
        logging.info("  LoRA Action Expert (rank=32): %.2fM",
                     sum(p.numel() for p in self._expert_lora_params) / 1e6)
        logging.info("  LoRA total (frozen for Phase 1): %.2fM", n_lora / 1e6)
        logging.info("  Phase 1: SDF decoder (%d) + EE extractor (%d) trainable",
                     n_sdf, n_ee)
        logging.info("  Phase 2: + LoRA (%.2fM) will be unfrozen", n_lora / 1e6)

    def extra_params(self):
        return list(self.sdf_decoder.parameters()) + list(self.ee_extractor.parameters())

    def on_step_start(self, global_step, model):
        if global_step == self.warmup_phase_steps and self.phase == 1:
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
            n_total_trainable = n_unfrozen
            for p in self.sdf_decoder.parameters():
                n_total_trainable += p.numel()
            for p in self.ee_extractor.parameters():
                n_total_trainable += p.numel()
            logging.info(
                "Phase 2: unfroze %d LoRA params at step %d (total trainable: %d, LoRA grad warmup: %d steps)",
                n_unfrozen, global_step, n_total_trainable, self._lora_warmup_steps,
            )
            if self.lambda_sdf != self.lambda_sdf_phase2:
                logging.info(
                    "[Phase 2] Switching lambda_sdf: %.4f -> %.4f",
                    self.lambda_sdf, self.lambda_sdf_phase2,
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
            aux_trainable = sum(p.numel() for p in self.sdf_decoder.parameters() if p.requires_grad) + \
                           sum(p.numel() for p in self.ee_extractor.parameters() if p.requires_grad)
            print(f"[Step {global_step}] Trainable params: {sum(trainable.values()) + aux_trainable:,}")
            print(f"[Step {global_step}] LoRA params: {sum(v for n, v in trainable.items() if 'lora' in n):,}")

    def on_loss_computed(self, action_loss, model, observation, global_step):
        features = self.suffix_hook.features
        if features is None:
            return action_loss, {}

        pooled = features.mean(dim=1)  # [B, 1024]
        if self.phase == 1:
            pooled = pooled.detach()

        B = pooled.shape[0]
        query_pts, gt_sdf = sample_sdf_batch(
            self.sdf_query, self.sdf_values, B, self.n_query_points
        )
        pred_sdf, grad_sdf = self.sdf_decoder(pooled, query_pts, return_gradients=True)
        sdf_losses = compute_sdf_loss(
            pred_sdf, gt_sdf, grad_sdf,
            clamp_delta=self.args.sdf_clamp,
            eikonal_weight=self.args.eikonal_weight,
        )

        ee_gt = observation.state[:, :3].float()
        ee_pred = self.ee_extractor(pooled)
        ee_loss = F.mse_loss(ee_pred, ee_gt)

        _lsdf = self.lambda_sdf if self.phase == 1 else self.lambda_sdf_phase2
        total = action_loss + _lsdf * sdf_losses["sdf_total"] + self.lambda_ee * ee_loss

        aux_info = {
            "action_loss": action_loss.item(),
            "sdf_l1": sdf_losses["sdf_l1"].item(),
            "sdf_total": sdf_losses["sdf_total"].item(),
            "ee_loss": ee_loss.item(),
            "phase": float(self.phase),
            "lambda_sdf_effective": _lsdf,
        }
        if "eikonal" in sdf_losses:
            aux_info["eikonal"] = sdf_losses["eikonal"].item()

        return total, aux_info

    def on_save_checkpoint(self, step_dir, global_step):
        torch.save(self.sdf_decoder.state_dict(), os.path.join(step_dir, "sdf_decoder.pt"))
        torch.save(self.ee_extractor.state_dict(), os.path.join(step_dir, "ee_extractor.pt"))
        torch.save({"phase": self.phase, "global_step": global_step},
                    os.path.join(step_dir, "aux_metadata.pt"))
        logging.info("Saved aux modules at step %d", global_step)

    def on_cleanup(self):
        if self.hook_handle is not None:
            self.hook_handle.remove()
        for h in getattr(self, '_lora_grad_hooks', []):
            h.remove()


def build_config(args):
    scene_cfg = SCENE_CONFIG[args.scene]
    num_steps = 2 if args.dry_run else args.num_train_steps
    exp_name = args.exp_name or f"a1_sdf_pi05_{args.scene}_seed{args.seed}"

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
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    if not int(os.environ.get("WORLD_SIZE", "1")) > 1:
        os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    logging.info("A1-Pi0.5 SDF Aux (hooks) | Scene: %s | Seed: %d | Dry run: %s",
                 args.scene, args.seed, args.dry_run)
    logging.info("Phase 1 warmup: %d steps, lambda_sdf=%.4f, lambda_ee=%.3f",
                 args.warmup_phase_steps, args.lambda_sdf, args.lambda_ee)
    if args.lambda_sdf_phase2 is not None:
        logging.info("Phase 2 lambda_sdf override: %.4f", args.lambda_sdf_phase2)

    config = build_config(args)
    hooks = SdfAuxHooks(args)
    train_loop(config, hooks=hooks)


if __name__ == "__main__":
    main()
