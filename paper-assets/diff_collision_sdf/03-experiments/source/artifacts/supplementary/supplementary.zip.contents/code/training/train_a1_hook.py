"""
A1: π0 + SDF auxiliary task training via openpi train_loop hooks.
Hooks into openpi's train_pytorch.py train_loop — reuses weight loading, normalization,
optimizer, and data pipeline. Adds SDF decoder + EE extractor as auxiliary heads.

Two-phase training:
  Phase 1 (0 → warmup_phase_steps): Freeze entire backbone + LoRA. Train only aux heads (~658K).
  Phase 2 (warmup_phase_steps → end): Unfreeze LoRA (~26M). Backbone base params stay frozen.

Loss = action_loss + λ_sdf × sdf_loss + λ_ee × ee_fk_loss

Dependencies:
  - openpi train_pytorch.py (TrainHooks, train_loop)
  - colliforce/sdf_decoder.py (SDFDecoder, compute_sdf_loss)
  - colliforce/ee_extractor.py (EEPositionExtractor)
  - SDF GT npz (query_points + sdf_values)

Usage:
    CUDA_VISIBLE_DEVICES=3 python scripts/train_a1_hook.py --scene spatial_bowl --dry_run
    CUDA_VISIBLE_DEVICES=3 python scripts/train_a1_hook.py --scene spatial_bowl --seed 0
"""
import argparse
import logging
import os
import sys

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "openpi"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "openpi", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

os.environ["HF_LEROBOT_HOME"] = "./data"

import openpi.models.pi0_config as pi0_config
import openpi.training.config as _config
from openpi.training.optimizer import CosineDecaySchedule
from colliforce.sdf_decoder import SDFDecoder, compute_sdf_loss
from colliforce.ee_extractor import EEPositionExtractor
from scripts.train_pytorch import TrainHooks, train_loop


SCENE_CONFIG = {
    "spatial_bowl": {
        "description": "SafeLIBERO Spatial: bowl between plate and ramekin",
        "data_subdir": "safelibero_spatial",
        "sdf_gt": "./data/sdf_gt_spatial_bowl.npz",
    },
}

CHECKPOINT_BASE = "./checkpoints"
DATA_BASE = "./data"
WEIGHTS_BASE = "./weights"


# ---------------------------------------------------------------------------
# Manual LoRA — PEFT is not installed; PyTorch π0 has no native LoRA.
# Wraps nn.Linear, adds lora_A/lora_B params. Base weight stays frozen.
# ---------------------------------------------------------------------------

class LoRALinear(nn.Module):
    """Drop-in replacement for nn.Linear that adds low-rank adapters.
    Base weight is frozen; only lora_A and lora_B are trainable.
    """

    def __init__(self, base: nn.Linear, rank: int = 16, alpha: float = 16.0):
        super().__init__()
        self.base = base
        for p in self.base.parameters():
            p.requires_grad = False
        in_f, out_f = base.in_features, base.out_features
        device = base.weight.device
        self.lora_A = nn.Parameter(torch.randn(in_f, rank, device=device) * 0.01)
        self.lora_B = nn.Parameter(torch.zeros(rank, out_f, device=device))
        self.scaling = alpha / rank

    @property
    def weight(self):
        return self.base.weight

    @property
    def bias(self):
        return self.base.bias

    @property
    def in_features(self):
        return self.base.in_features

    @property
    def out_features(self):
        return self.base.out_features

    def forward(self, x):
        base_out = self.base(x)
        # LoRA path in float32 for numerical stability, cast back
        lora_out = (x.float() @ self.lora_A @ self.lora_B) * self.scaling
        return base_out + lora_out.to(base_out.dtype)


def _replace_linear(parent: nn.Module, attr_name: str, rank: int, alpha: float):
    old = getattr(parent, attr_name)
    assert isinstance(old, nn.Linear), f"{attr_name} is {type(old)}, expected nn.Linear"
    setattr(parent, attr_name, LoRALinear(old, rank=rank, alpha=alpha))


TARGET_MODULES = ("q_proj", "k_proj", "v_proj", "o_proj",
                  "gate_proj", "up_proj", "down_proj")


def inject_lora(model: nn.Module, rank: int = 16, alpha: float = 16.0):
    """Inject LoRA into all attention + MLP projections of paligemma and action expert.

    Returns list of all LoRA parameters (for optimizer / grad clipping).
    Estimated param count with rank=16: ~26.5M.
    """
    lora_params = []

    # Paligemma language model layers
    pali_layers = model.paligemma_with_expert.paligemma.language_model.layers
    for layer in pali_layers:
        for name in TARGET_MODULES:
            parent = layer.self_attn if name in ("q_proj", "k_proj", "v_proj", "o_proj") else layer.mlp
            _replace_linear(parent, name, rank, alpha)
            lora_mod = getattr(parent, name)
            lora_params.extend([lora_mod.lora_A, lora_mod.lora_B])

    # Action expert layers
    expert_layers = model.paligemma_with_expert.gemma_expert.model.layers
    for layer in expert_layers:
        for name in TARGET_MODULES:
            parent = layer.self_attn if name in ("q_proj", "k_proj", "v_proj", "o_proj") else layer.mlp
            _replace_linear(parent, name, rank, alpha)
            lora_mod = getattr(parent, name)
            lora_params.extend([lora_mod.lora_A, lora_mod.lora_B])

    return lora_params


# ---------------------------------------------------------------------------
# SDF data loading
# ---------------------------------------------------------------------------

def load_sdf_gt(path: str, device: torch.device):
    data = np.load(path)
    query_points = torch.tensor(data["query_points"], dtype=torch.float32, device=device)
    sdf_values = torch.tensor(data["sdf_values"], dtype=torch.float32, device=device)
    return query_points, sdf_values


def sample_sdf_batch(query_points, sdf_values, batch_size, n_query):
    """Random-sample n_query points, broadcast to [B, n_query, 3] / [B, n_query]."""
    indices = torch.randint(0, len(query_points), (n_query,), device=query_points.device)
    pts = query_points[indices].unsqueeze(0).expand(batch_size, -1, -1)
    sdf = sdf_values[indices].unsqueeze(0).expand(batch_size, -1)
    return pts, sdf


# ---------------------------------------------------------------------------
# Suffix-out capture hook
# ---------------------------------------------------------------------------

class SuffixOutCapture:
    """Forward hook on action_out_proj to capture its input (= suffix_out)."""

    def __init__(self):
        self.features = None

    def __call__(self, module, input, output):
        # input is a tuple; input[0] = suffix_out [B, action_horizon, 1024]
        self.features = input[0]


# ---------------------------------------------------------------------------
# A1 SDF Aux Hooks
# ---------------------------------------------------------------------------

class SdfAuxHooks(TrainHooks):
    def __init__(self, args):
        self.args = args
        self.phase = 1
        self.warmup_phase_steps = args.warmup_phase_steps
        self.lambda_sdf = args.lambda_sdf
        self.lambda_ee = args.lambda_ee
        self.n_query_points = args.n_query_points

        # feature_dim = gemma_300m width = 1024
        self.sdf_decoder = SDFDecoder(feature_dim=1024, hidden_dim=256)
        self.ee_extractor = EEPositionExtractor(feature_dim=1024, hidden_dim=256)

        self.suffix_capture = SuffixOutCapture()
        self.hook_handle = None
        self.lora_params = []
        self.sdf_query = None
        self.sdf_values = None
        self.device = None

    # -- TrainHooks interface --

    def on_model_created(self, model, device):
        self.device = device

        # 1. Move aux modules to device
        self.sdf_decoder.to(device)
        self.ee_extractor.to(device)

        # 2. Register forward hook to capture suffix_out
        _m = model.module if hasattr(model, "module") else model
        self.hook_handle = _m.action_out_proj.register_forward_hook(self.suffix_capture)

        # 3. Freeze ALL backbone params (Phase 1)
        for param in model.parameters():
            param.requires_grad = False

        # 4. Inject LoRA into backbone (adds ~26M params, initially frozen)
        self.lora_params = inject_lora(_m, rank=16, alpha=16.0)
        for p in self.lora_params:
            p.requires_grad = False

        # 5. Load SDF ground truth
        scene_cfg = SCENE_CONFIG[self.args.scene]
        self.sdf_query, self.sdf_values = load_sdf_gt(scene_cfg["sdf_gt"], device)

        # 6. Log param counts
        aux_params = sum(p.numel() for p in self.sdf_decoder.parameters()) + \
                     sum(p.numel() for p in self.ee_extractor.parameters())
        lora_total = sum(p.numel() for p in self.lora_params)
        backbone_total = sum(p.numel() for p in model.parameters())
        trainable_now = sum(p.numel() for p in self.sdf_decoder.parameters() if p.requires_grad) + \
                        sum(p.numel() for p in self.ee_extractor.parameters() if p.requires_grad)
        logging.info("=== A1 SDF Aux Hooks ===")
        logging.info("  Backbone params: %.2fM", backbone_total / 1e6)
        logging.info("  LoRA params (injected, frozen for Phase 1): %.2fM", lora_total / 1e6)
        logging.info("  Aux params (SDF decoder + EE extractor): %.2fM", aux_params / 1e6)
        logging.info("  Phase 1 trainable: %.2fM (aux only)", trainable_now / 1e6)
        logging.info("  Phase 2 trainable: %.2fM (LoRA + aux)", (lora_total + aux_params) / 1e6)

    def extra_params(self):
        # Only aux module params — LoRA params are already in model.parameters()
        # after inject_lora replaces nn.Linear with LoRALinear submodules
        return (list(self.sdf_decoder.parameters()) +
                list(self.ee_extractor.parameters()))

    def on_step_start(self, global_step, model):
        if global_step >= self.warmup_phase_steps and self.phase == 1:
            self.phase = 2
            # Unfreeze LoRA params — optimizer already tracks them
            unfrozen = 0
            for p in self.lora_params:
                p.requires_grad = True
                unfrozen += p.numel()
            logging.info("=== Phase 2 activated at step %d ===", global_step)
            logging.info("  Unfroze LoRA params: %.2fM", unfrozen / 1e6)
            # Verify: count all trainable params now
            _m = model.module if hasattr(model, "module") else model
            total_trainable = sum(p.numel() for p in _m.parameters() if p.requires_grad)
            total_trainable += sum(p.numel() for p in self.sdf_decoder.parameters() if p.requires_grad)
            total_trainable += sum(p.numel() for p in self.ee_extractor.parameters() if p.requires_grad)
            logging.info("  Total trainable now: %.2fM", total_trainable / 1e6)

    def on_loss_computed(self, action_loss, model, observation, global_step):
        features = self.suffix_capture.features
        if features is None:
            logging.warning("suffix_out not captured at step %d", global_step)
            return action_loss, {}

        # Mean-pool over action_horizon: [B, action_horizon, 1024] → [B, 1024]
        pooled = features.mean(dim=1).float()

        B = pooled.shape[0]

        # --- EE position prediction ---
        ee_gt = observation.state[:, :3].float()
        ee_pred = self.ee_extractor(pooled)
        ee_loss = F.mse_loss(ee_pred, ee_gt)

        # --- SDF prediction ---
        query_pts, gt_sdf = sample_sdf_batch(
            self.sdf_query, self.sdf_values, B, self.n_query_points
        )
        pred_sdf, grad_sdf = self.sdf_decoder(
            pooled, query_pts, return_gradients=True
        )
        sdf_losses = compute_sdf_loss(
            pred_sdf, gt_sdf, grad_sdf,
            clamp_delta=self.args.sdf_clamp,
            eikonal_weight=self.args.eikonal_weight,
        )

        total = action_loss + self.lambda_sdf * sdf_losses["sdf_total"] + self.lambda_ee * ee_loss

        aux_info = {
            "action_loss": action_loss.item() if hasattr(action_loss, "item") else float(action_loss),
            "sdf_l1": sdf_losses["sdf_l1"].item(),
            "sdf_total": sdf_losses["sdf_total"].item(),
            "ee_loss": ee_loss.item(),
            "phase": float(self.phase),
        }
        if "eikonal" in sdf_losses:
            aux_info["eikonal"] = sdf_losses["eikonal"].item()

        return total, aux_info

    def on_save_checkpoint(self, step_dir, global_step):
        torch.save(self.sdf_decoder.state_dict(), os.path.join(step_dir, "sdf_decoder.pt"))
        torch.save(self.ee_extractor.state_dict(), os.path.join(step_dir, "ee_extractor.pt"))
        # Save LoRA state separately (base model checkpoint has LoRA in its state_dict,
        # but this explicit save helps with resume debugging)
        lora_state = {f"lora_param_{i}": p.data for i, p in enumerate(self.lora_params)}
        torch.save(lora_state, os.path.join(step_dir, "lora_params.pt"))
        torch.save({"phase": self.phase, "global_step": global_step},
                    os.path.join(step_dir, "aux_metadata.pt"))
        logging.info("Saved aux modules + LoRA at step %d", global_step)

    def on_cleanup(self):
        if self.hook_handle is not None:
            self.hook_handle.remove()


# ---------------------------------------------------------------------------
# Config builder
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="A1: π0 + SDF auxiliary task via hooks")
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
    p.add_argument("--lambda_sdf", type=float, default=0.1)
    p.add_argument("--lambda_ee", type=float, default=0.01)
    p.add_argument("--n_query_points", type=int, default=64)
    p.add_argument("--sdf_clamp", type=float, default=0.05)
    p.add_argument("--eikonal_weight", type=float, default=0.1)
    p.add_argument("--warmup_phase_steps", type=int, default=5000)
    return p.parse_args()


def build_config(args) -> _config.TrainConfig:
    scene_cfg = SCENE_CONFIG[args.scene]
    num_steps = 2 if args.dry_run else args.num_train_steps
    exp_name = args.exp_name or f"a1_sdf_{args.scene}_seed{args.seed}"

    # Use base variants (no _lora suffix) — we inject LoRA manually
    model_config = pi0_config.Pi0Config(
        paligemma_variant="gemma_2b",
        action_expert_variant="gemma_300m",
    )

    config = _config.TrainConfig(
        name=f"a1_sdf_{args.scene}",
        project_name="colliforce-vla",
        exp_name=exp_name,
        model=model_config,
        data=_config.LeRobotLiberoDataConfig(
            repo_id=scene_cfg["data_subdir"],
            base_config=_config.DataConfig(prompt_from_task=True),
            extra_delta_transform=False,
        ),
        pytorch_weight_path=os.path.join(WEIGHTS_BASE, "pi0_base"),
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

    scene_cfg = SCENE_CONFIG[args.scene]
    logging.info("A1 SDF Aux (hooks) | Scene: %s | Seed: %d | Dry run: %s",
                 args.scene, args.seed, args.dry_run)
    logging.info("Phase 1 warmup: %d steps, λ_sdf=%.3f, λ_ee=%.3f",
                 args.warmup_phase_steps, args.lambda_sdf, args.lambda_ee)

    data_dir = os.path.join(DATA_BASE, scene_cfg["data_subdir"])
    weight_path = os.path.join(WEIGHTS_BASE, "pi0_base")
    sdf_gt_path = scene_cfg["sdf_gt"]

    for path, desc in [(data_dir, "Training data"), (weight_path, "Base weights"),
                        (sdf_gt_path, "SDF GT")]:
        if not os.path.exists(path):
            logging.error("%s not found: %s", desc, path)
            sys.exit(1)

    config = build_config(args)
    hooks = SdfAuxHooks(args)
    logging.info("Checkpoint dir: %s", config.checkpoint_dir)
    train_loop(config, hooks=hooks)


if __name__ == "__main__":
    main()
