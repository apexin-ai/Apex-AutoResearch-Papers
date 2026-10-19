"""
Phase 1 LoRA Expert Training — Main Script.

Trains per-perturbation-type LoRA adapters on pi0's PaliGemma backbone
using the OpenPI PyTorch framework. LoRA is injected into ALL 18
PaliGemma attention layers (Q/K/V/O projections). Action Expert layers
are frozen and untouched.

Input:
    --perturbation_type {visual,spatial,physical,universal}
    --dry_run  (pipeline validation: 1 epoch, synthetic data, 2 batches)
    pi0 base checkpoint at /root/autodl-tmp/checkpoints/pi0_base/

Output:
    LoRA adapter checkpoint at checkpoints/phase1/{perturbation_type}/
    W&B logs (project=meta_brain_lora_routing, group=phase1_lora)

Dependencies:
    openpi (installed editable), peft, torch, safetensors, wandb
"""

import argparse
import json
import logging
import math
import os
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("phase1")

# ---------------------------------------------------------------------------
# Imports: OpenPI + PEFT (deferred so we can give clear error messages)
# ---------------------------------------------------------------------------

def _ensure_openpi():
    """Add OpenPI to sys.path and stub out lerobot if missing."""
    openpi_src = "/root/openpi/src"
    if openpi_src not in sys.path:
        sys.path.insert(0, openpi_src)
    openpi_root = "/root/openpi"
    if openpi_root not in sys.path:
        sys.path.insert(0, openpi_root)

    # Stub lerobot (training-only dep) to avoid import errors during model load
    import types
    for mod in [
        "lerobot", "lerobot.common", "lerobot.common.datasets",
        "lerobot.common.datasets.lerobot_dataset",
    ]:
        if mod not in sys.modules:
            sys.modules[mod] = types.ModuleType(mod)

_ensure_openpi()

# Phase 1 configs
sys.path.insert(0, str(Path(__file__).parent))
from configs import (
    PI0_WEIGHTS,
    PALIGEMMA_NUM_LAYERS,
    LoRAConfig,
    TrainConfig,
    apply_dry_run_overrides,
)


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_pi0_model(device: str) -> torch.nn.Module:
    """Load PI0Pytorch from safetensors checkpoint."""
    import safetensors.torch
    from openpi.models.pi0_config import Pi0Config
    from openpi.models_pytorch.pi0_pytorch import PI0Pytorch

    config = Pi0Config(dtype="bfloat16")
    log.info("Creating PI0Pytorch model...")
    model = PI0Pytorch(config)

    log.info("Loading weights from %s", PI0_WEIGHTS)
    safetensors.torch.load_model(model, PI0_WEIGHTS)

    model = model.to(device)
    log.info("Model loaded on %s", device)
    return model


# ---------------------------------------------------------------------------
# PaliGemma attention layer discovery
# ---------------------------------------------------------------------------

def discover_paligemma_attn_modules(model: torch.nn.Module) -> list[str]:
    """Scan model.named_modules() to find PaliGemma LM Q/K/V/O projections.

    Targets ONLY the language_model layers, NOT the vision tower or action expert.
    Full path pattern: paligemma_with_expert.paligemma.model.language_model.layers.{i}.self_attn.{q,k,v,o}_proj

    Returns full module-path strings for diagnostic purposes.
    """
    target_suffixes = {"q_proj", "k_proj", "v_proj", "o_proj"}
    paligemma_lm_modules = []

    for name, _ in model.named_modules():
        # Specifically match PaliGemma language model layers only
        if "model.language_model.layers" in name and "self_attn" in name:
            suffix = name.rsplit(".", 1)[-1]
            if suffix in target_suffixes:
                paligemma_lm_modules.append(name)

    expected = PALIGEMMA_NUM_LAYERS * len(target_suffixes)  # 72
    if len(paligemma_lm_modules) != expected:
        log.warning(
            "Expected %d PaliGemma LM attn modules, found %d. Listing all:",
            expected, len(paligemma_lm_modules),
        )
        for m in paligemma_lm_modules:
            log.warning("  %s", m)

    log.info(
        "Discovered %d PaliGemma LM attention modules (expected %d)",
        len(paligemma_lm_modules), expected,
    )
    return paligemma_lm_modules


# Regex matching PaliGemma language model attention projections only.
# Excludes vision tower (vision_model.encoder.layers) and action expert (gemma_expert).
PALIGEMMA_LM_ATTN_REGEX = (
    r"paligemma_with_expert\.paligemma\.model\.language_model"
    r"\.layers\.\d+\.self_attn\.(q|k|v|o)_proj"
)


# ---------------------------------------------------------------------------
# LoRA injection via PEFT
# ---------------------------------------------------------------------------

def inject_lora(model: torch.nn.Module, lora_cfg: LoRAConfig) -> torch.nn.Module:
    """Apply PEFT LoRA to PaliGemma LM attention layers only."""
    from peft import LoraConfig, get_peft_model

    # Diagnostic: verify expected modules exist
    target_modules = discover_paligemma_attn_modules(model)
    if not target_modules:
        raise RuntimeError("No PaliGemma LM attention modules found — check model structure")

    # Use regex to precisely target only PaliGemma LM layers
    peft_config = LoraConfig(
        r=lora_cfg.rank,
        lora_alpha=lora_cfg.alpha,
        lora_dropout=lora_cfg.dropout,
        bias=lora_cfg.bias,
        target_modules=PALIGEMMA_LM_ATTN_REGEX,
    )

    model = get_peft_model(model, peft_config)

    # Report parameter counts
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    log.info(
        "LoRA injected: trainable=%s (%.2f%%) / total=%s",
        f"{trainable:,}", 100.0 * trainable / total, f"{total:,}",
    )

    return model


# ---------------------------------------------------------------------------
# Synthetic data for dry-run
# ---------------------------------------------------------------------------

class SyntheticPI0Dataset(Dataset):
    """Generates random (observation, actions) pairs matching PI0 input format."""

    def __init__(self, num_samples: int = 100, action_dim: int = 32,
                 action_horizon: int = 50, max_token_len: int = 48):
        self.num_samples = num_samples
        self.action_dim = action_dim
        self.action_horizon = action_horizon
        self.max_token_len = max_token_len

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        rng = np.random.RandomState(idx)
        # Images: uint8 [H, W, 3]
        base_img = rng.randint(0, 256, (224, 224, 3), dtype=np.uint8)
        wrist_img = rng.randint(0, 256, (224, 224, 3), dtype=np.uint8)
        zero_img = np.zeros((224, 224, 3), dtype=np.uint8)

        # State
        state = rng.randn(self.action_dim).astype(np.float32)
        # Actions
        actions = rng.randn(self.action_horizon, self.action_dim).astype(np.float32)
        # Tokenized prompt (random token IDs)
        tokens = rng.randint(0, 256000, (self.max_token_len,)).astype(np.int32)
        token_mask = np.ones(self.max_token_len, dtype=bool)

        return {
            "image": {
                "base_0_rgb": base_img,
                "left_wrist_0_rgb": wrist_img,
                "right_wrist_0_rgb": zero_img,
            },
            "image_mask": {
                "base_0_rgb": True,
                "left_wrist_0_rgb": True,
                "right_wrist_0_rgb": False,
            },
            "state": state,
            "tokenized_prompt": tokens,
            "tokenized_prompt_mask": token_mask,
            "actions": actions,
        }


def collate_pi0(batch: list[dict]) -> tuple:
    """Collate synthetic samples into (Observation, actions) for PI0Pytorch."""
    from openpi.models.model import Observation

    images = {}
    image_masks = {}
    for key in ["base_0_rgb", "left_wrist_0_rgb", "right_wrist_0_rgb"]:
        imgs = np.stack([s["image"][key] for s in batch])
        # Convert uint8 [B,H,W,C] -> float32 [-1,1] [B,C,H,W]
        # Vision model expects channels-first; preprocessing preserves input format
        imgs = imgs.astype(np.float32) / 255.0 * 2.0 - 1.0
        imgs = np.transpose(imgs, (0, 3, 1, 2))  # HWC -> CHW
        images[key] = torch.from_numpy(imgs)
        masks = np.array([s["image_mask"][key] for s in batch])
        image_masks[key] = torch.from_numpy(masks)

    state = torch.from_numpy(np.stack([s["state"] for s in batch]))
    tokens = torch.from_numpy(np.stack([s["tokenized_prompt"] for s in batch]))
    token_mask = torch.from_numpy(np.stack([s["tokenized_prompt_mask"] for s in batch]))
    actions = torch.from_numpy(np.stack([s["actions"] for s in batch]))

    obs = Observation(
        images=images,
        image_masks=image_masks,
        state=state,
        tokenized_prompt=tokens,
        tokenized_prompt_mask=token_mask,
    )
    return obs, actions


def create_synthetic_loaders(cfg: TrainConfig):
    """Create train/val data loaders with synthetic data for dry-run."""
    n_train = 10 if cfg.dry_run else 100
    n_val = 4 if cfg.dry_run else 20

    train_ds = SyntheticPI0Dataset(num_samples=n_train)
    val_ds = SyntheticPI0Dataset(num_samples=n_val)

    train_loader = DataLoader(
        train_ds, batch_size=cfg.batch_size, shuffle=True,
        collate_fn=collate_pi0, drop_last=True,
    )
    val_loader = DataLoader(
        val_ds, batch_size=cfg.batch_size, shuffle=False,
        collate_fn=collate_pi0, drop_last=False,
    )
    return train_loader, val_loader


# ---------------------------------------------------------------------------
# LIBERO data loading (via OpenPI pipeline)
# ---------------------------------------------------------------------------

def create_libero_loaders(cfg: TrainConfig, augmentation_fn=None):
    """Create train/val data loaders using OpenPI's LIBERO data pipeline.

    augmentation_fn: optional callable(batch) -> batch for online augmentation.
                     Placeholder for visual perturbation augmentations.
    """
    from openpi.training import config as openpi_config
    from openpi.training import data_loader as openpi_data

    train_config = openpi_config.get_config(cfg.openpi_config_name)

    # Override batch size
    train_config = dataclasses.replace(train_config, batch_size=cfg.batch_size)

    loader = openpi_data.create_data_loader(
        train_config, framework="pytorch", shuffle=True
    )

    class WrappedLoader:
        """Wraps OpenPI data loader with optional augmentation + epoch semantics."""

        def __init__(self, base_loader, augmentation_fn=None, max_batches=None):
            self._base = base_loader
            self._augmentation_fn = augmentation_fn
            self._max_batches = max_batches

        def __iter__(self):
            count = 0
            for obs, actions in self._base:
                if self._max_batches and count >= self._max_batches:
                    break
                if self._augmentation_fn:
                    obs, actions = self._augmentation_fn(obs, actions)
                yield obs, actions
                count += 1

    # For now, use the same loader for train and val (split is TODO)
    # In practice, val should use a held-out set of episodes
    import dataclasses as dc
    train_loader = WrappedLoader(loader, augmentation_fn=augmentation_fn)
    val_loader = WrappedLoader(loader, max_batches=10)

    return train_loader, val_loader


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------

def move_observation_to_device(obs, device):
    """Move Observation fields to target device."""
    from openpi.models.model import Observation

    images = {k: v.to(device) for k, v in obs.images.items()}
    image_masks = {k: v.to(device) for k, v in obs.image_masks.items()}

    return Observation(
        images=images,
        image_masks=image_masks,
        state=obs.state.to(device),
        tokenized_prompt=obs.tokenized_prompt.to(device) if obs.tokenized_prompt is not None else None,
        tokenized_prompt_mask=obs.tokenized_prompt_mask.to(device) if obs.tokenized_prompt_mask is not None else None,
        token_ar_mask=obs.token_ar_mask.to(device) if obs.token_ar_mask is not None else None,
        token_loss_mask=obs.token_loss_mask.to(device) if obs.token_loss_mask is not None else None,
    )


def train_one_epoch(model, loader, optimizer, scheduler, device, cfg, epoch, global_step):
    """Run one training epoch. Returns (avg_loss, global_step)."""
    model.train()
    losses = []
    epoch_start = time.time()

    max_batches = 5 if cfg.dry_run else None

    for batch_idx, (obs, actions) in enumerate(loader):
        if max_batches and batch_idx >= max_batches:
            break

        obs = move_observation_to_device(obs, device)
        actions = actions.to(device)

        optimizer.zero_grad(set_to_none=True)

        # PI0Pytorch.forward returns per-element MSE loss
        loss_per_elem = model(obs, actions)
        loss = loss_per_elem.mean()

        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), cfg.grad_clip_norm)
        optimizer.step()

        if scheduler is not None:
            scheduler.step()

        losses.append(loss.item())
        global_step += 1

        if global_step % cfg.log_interval == 0:
            log.info(
                "epoch=%d step=%d batch=%d loss=%.6f lr=%.2e",
                epoch, global_step, batch_idx, loss.item(),
                optimizer.param_groups[0]["lr"],
            )

            if cfg.wandb_enabled:
                import wandb
                wandb.log({
                    "train/loss": loss.item(),
                    "train/lr": optimizer.param_groups[0]["lr"],
                    "train/epoch": epoch,
                }, step=global_step)

    elapsed = time.time() - epoch_start
    avg_loss = sum(losses) / len(losses) if losses else float("inf")
    log.info(
        "Epoch %d done: avg_loss=%.6f n_batches=%d time=%.1fs",
        epoch, avg_loss, len(losses), elapsed,
    )
    return avg_loss, global_step


@torch.no_grad()
def validate(model, loader, device, cfg):
    """Run validation. Returns average MSE loss."""
    model.eval()
    losses = []
    max_batches = 2 if cfg.dry_run else None

    for batch_idx, (obs, actions) in enumerate(loader):
        if max_batches and batch_idx >= max_batches:
            break

        obs = move_observation_to_device(obs, device)
        actions = actions.to(device)

        loss_per_elem = model(obs, actions)
        losses.append(loss_per_elem.mean().item())

    avg_loss = sum(losses) / len(losses) if losses else float("inf")
    log.info("Validation: avg_mse=%.6f (n_batches=%d)", avg_loss, len(losses))
    return avg_loss


# ---------------------------------------------------------------------------
# Checkpoint management
# ---------------------------------------------------------------------------

def save_checkpoint(model, optimizer, epoch, global_step, val_loss, cfg):
    """Save LoRA adapter checkpoint + training metadata."""
    ckpt_dir = Path(cfg.checkpoint_dir) / f"epoch_{epoch}"
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    # Save only LoRA adapter weights (via PEFT)
    model.save_pretrained(str(ckpt_dir))

    # Save optimizer and metadata
    meta = {
        "epoch": epoch,
        "global_step": global_step,
        "val_loss": val_loss,
        "perturbation_type": cfg.perturbation_type,
        "lora_rank": cfg.lora.rank,
        "lora_alpha": cfg.lora.alpha,
        "lr": cfg.lr,
        "seed": cfg.seed,
    }
    torch.save(optimizer.state_dict(), ckpt_dir / "optimizer.pt")
    with open(ckpt_dir / "metadata.json", "w") as f:
        json.dump(meta, f, indent=2)

    log.info("Checkpoint saved: %s (val_loss=%.6f)", ckpt_dir, val_loss)
    return str(ckpt_dir)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description="Phase 1: Train LoRA expert for pi0")
    parser.add_argument("--perturbation_type", type=str, default="visual",
                        choices=["visual", "spatial", "physical", "universal"])
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--checkpoint_dir", type=str, default="")
    parser.add_argument("--no_wandb", action="store_true")
    # LoRA overrides
    parser.add_argument("--lora_rank", type=int, default=16)
    parser.add_argument("--lora_alpha", type=int, default=32)
    return parser.parse_args()


def main():
    args = parse_args()

    # Build config
    lora_cfg = LoRAConfig(rank=args.lora_rank, alpha=args.lora_alpha)
    cfg = TrainConfig(
        perturbation_type=args.perturbation_type,
        gpu=args.gpu,
        epochs=args.epochs,
        batch_size=args.batch_size,
        lr=args.lr,
        seed=args.seed,
        dry_run=args.dry_run,
        checkpoint_dir=args.checkpoint_dir,
        lora=lora_cfg,
    )
    cfg.wandb_enabled = not args.no_wandb

    if cfg.dry_run:
        cfg = apply_dry_run_overrides(cfg)
        cfg.wandb_enabled = False
        log.info("=== DRY-RUN MODE ===")

    # Seed
    torch.manual_seed(cfg.seed)
    np.random.seed(cfg.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(cfg.seed)

    device = torch.device(cfg.device_str)
    log.info("Device: %s", device)

    # -----------------------------------------------------------------------
    # 1. Load model
    # -----------------------------------------------------------------------
    model = load_pi0_model(cfg.device_str)

    # -----------------------------------------------------------------------
    # 2. Inject LoRA
    # -----------------------------------------------------------------------
    model = inject_lora(model, cfg.lora)

    # Print LoRA target modules for verification
    if hasattr(model, "peft_config"):
        targets = model.peft_config["default"].target_modules
        if isinstance(targets, str):
            log.info("LoRA target_modules regex: %s", targets)
        else:
            log.info("LoRA target_modules (%d modules):", len(targets))
            for t in sorted(targets)[:8]:
                log.info("  %s", t)
            if len(targets) > 8:
                log.info("  ... (%d more)", len(targets) - 8)

    # -----------------------------------------------------------------------
    # 3. Create data loaders
    # -----------------------------------------------------------------------
    if cfg.dry_run:
        train_loader, val_loader = create_synthetic_loaders(cfg)
        log.info("Using synthetic data for dry-run")
    else:
        # Augmentation hook placeholder for visual perturbation type
        augmentation_fn = None
        if cfg.perturbation_type == "visual":
            # TODO: augmentation_fn = create_visual_augmentation_fn()
            log.info("Visual augmentation hook: placeholder (no augmentation applied)")

        train_loader, val_loader = create_libero_loaders(cfg, augmentation_fn)
        log.info("Using LIBERO data pipeline (config=%s)", cfg.openpi_config_name)

    # -----------------------------------------------------------------------
    # 4. Optimizer + scheduler
    # -----------------------------------------------------------------------
    trainable_params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(
        trainable_params,
        lr=cfg.lr,
        weight_decay=cfg.weight_decay,
        betas=(0.9, 0.95),
        eps=1e-8,
    )

    # Linear warmup + cosine decay
    total_steps = cfg.epochs * (len(train_loader) if hasattr(train_loader, "__len__") else 100)
    if cfg.dry_run:
        total_steps = cfg.epochs * 5

    def lr_lambda(step):
        if step < cfg.warmup_steps:
            return (step + 1) / (cfg.warmup_steps + 1)
        progress = (step - cfg.warmup_steps) / max(1, total_steps - cfg.warmup_steps)
        return 0.5 * (1.0 + math.cos(math.pi * progress))

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

    # -----------------------------------------------------------------------
    # 5. W&B
    # -----------------------------------------------------------------------
    if cfg.wandb_enabled:
        import wandb
        wandb.init(
            project=cfg.wandb_project,
            group=cfg.wandb_group,
            name=cfg.wandb_name,
            config={
                "perturbation_type": cfg.perturbation_type,
                "lora_rank": cfg.lora.rank,
                "lora_alpha": cfg.lora.alpha,
                "lr": cfg.lr,
                "epochs": cfg.epochs,
                "batch_size": cfg.batch_size,
                "seed": cfg.seed,
            },
        )

    # -----------------------------------------------------------------------
    # 6. Training loop
    # -----------------------------------------------------------------------
    global_step = 0
    best_val_loss = float("inf")
    patience_counter = 0
    checkpoint_dir = Path(cfg.checkpoint_dir)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    log.info("Starting training: epochs=%d, lr=%.1e, batch_size=%d",
             cfg.epochs, cfg.lr, cfg.batch_size)

    for epoch in range(cfg.epochs):
        # Train
        train_loss, global_step = train_one_epoch(
            model, train_loader, optimizer, scheduler, device, cfg, epoch, global_step,
        )

        # Validate
        val_loss = validate(model, val_loader, device, cfg)

        if cfg.wandb_enabled:
            import wandb
            wandb.log({
                "val/mse": val_loss,
                "val/epoch": epoch,
                "train/epoch_loss": train_loss,
            }, step=global_step)

        # Checkpoint
        save_checkpoint(model, optimizer, epoch, global_step, val_loss, cfg)

        # Early stopping check
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            # Save best model
            best_dir = checkpoint_dir / "best"
            best_dir.mkdir(parents=True, exist_ok=True)
            model.save_pretrained(str(best_dir))
            log.info("New best val_loss=%.6f — saved to %s", val_loss, best_dir)
        else:
            patience_counter += 1
            log.info(
                "Val loss did not improve (%.6f >= %.6f), patience=%d/%d",
                val_loss, best_val_loss, patience_counter, cfg.patience,
            )
            if patience_counter >= cfg.patience:
                log.info("Early stopping triggered at epoch %d", epoch)
                break

    # -----------------------------------------------------------------------
    # 7. Final summary
    # -----------------------------------------------------------------------
    log.info("=" * 60)
    log.info("Training complete.")
    log.info("  Perturbation type: %s", cfg.perturbation_type)
    log.info("  Best val MSE: %.6f", best_val_loss)
    log.info("  Total steps: %d", global_step)
    log.info("  Checkpoints: %s", cfg.checkpoint_dir)
    log.info("=" * 60)

    if cfg.wandb_enabled:
        import wandb
        wandb.finish()


if __name__ == "__main__":
    main()
