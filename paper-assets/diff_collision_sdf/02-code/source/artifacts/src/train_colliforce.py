"""
ColliForce-VLA training script — extends openpi's train_pytorch.py.

Training pipeline:
  Phase 1: Freeze VLA backbone, train SDF decoder only (warmup)
  Phase 2: End-to-end — SDF decoder + gradient refiner + LoRA on action expert

Loss components:
  - flow_loss: original openpi flow matching MSE on velocity
  - sdf_loss: L1 clamped SDF + Eikonal regularization
  - gradient_alignment_loss: encourage SDF-gradient refinement to reduce collision

Dependencies: torch, openpi (for base model + training infra)
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

import torch
import torch.nn as nn

from .sdf_decoder import SDFDecoder, SDFDecoderConfig, compute_sdf_loss
from .sdf_gradient_refiner import (
    SDFGradientRefiner,
    GradientRefinerConfig,
    compute_gradient_alignment_loss,
)
from .sdf_data import SDFDataConfig, SDFDataset, SDFBatchCollator

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass
class ColliForceConfig:
    """Hyperparameters for ColliForce-VLA training."""

    # --- Paths ---
    openpi_checkpoint: str = ""
    sdf_data_dir: str = ""
    output_dir: str = ""

    # --- Loss weights ---
    sdf_loss_weight: float = 0.1
    eikonal_weight: float = 0.01
    gradient_alignment_weight: float = 0.05

    # --- SDF decoder ---
    sdf_feature_dim: int = 1024
    sdf_hidden_dim: int = 256
    sdf_clamp_delta: float = 0.05
    sdf_aggregation: str = "mean"

    # --- Gradient refiner ---
    refinement_alpha: float = 0.1
    collision_margin: float = 0.02
    collision_softplus_beta: float = 10.0
    use_learned_projection: bool = True

    # --- Data ---
    n_query_points: int = 4096
    near_surface_threshold: float = 0.01
    near_surface_weight: float = 5.0

    # --- Training phases ---
    phase1_epochs: int = 5
    phase2_epochs: int = 50
    warmup_steps: int = 500
    learning_rate: float = 1e-4
    sdf_decoder_lr: float = 3e-4
    weight_decay: float = 0.01
    batch_size: int = 16
    grad_clip_norm: float = 1.0

    # --- LoRA (Phase 2) ---
    lora_rank: int = 32
    lora_alpha: float = 64.0
    lora_target_modules: list[str] = field(
        default_factory=lambda: ["q_proj", "v_proj", "o_proj"]
    )

    # --- Logging ---
    log_every: int = 50
    eval_every: int = 500
    save_every: int = 1000
    wandb_project: str = "colliforce-vla"
    wandb_run_name: str = ""


# ---------------------------------------------------------------------------
# Model wrapper
# ---------------------------------------------------------------------------

class ColliForceVLA(nn.Module):
    """
    Wraps the openpi π0 model with SDF decoder and gradient refiner.

    Architecture:
      openpi backbone (frozen or LoRA) → suffix_out [B, action_horizon, 1024]
        ├→ SDF decoder (auxiliary) → SDF predictions for supervision
        └→ Gradient refiner → refined suffix_out → action_out_proj → actions
    """

    def __init__(self, config: ColliForceConfig):
        super().__init__()
        self.config = config

        # TODO: Load openpi model from checkpoint
        # self.backbone = load_openpi_model(config.openpi_checkpoint)
        self.backbone = None  # placeholder

        # SDF decoder
        sdf_config = SDFDecoderConfig(
            feature_dim=config.sdf_feature_dim,
            hidden_dim=config.sdf_hidden_dim,
            clamp_delta=config.sdf_clamp_delta,
            aggregation=config.sdf_aggregation,
        )
        self.sdf_decoder = SDFDecoder(sdf_config)

        # Gradient refiner — shares the SDF decoder
        refiner_config = GradientRefinerConfig(
            feature_dim=config.sdf_feature_dim,
            collision_margin=config.collision_margin,
            refinement_alpha=config.refinement_alpha,
            use_learned_projection=config.use_learned_projection,
            collision_softplus_beta=config.collision_softplus_beta,
        )
        self.gradient_refiner = SDFGradientRefiner(
            config=refiner_config,
            sdf_decoder=self.sdf_decoder,
        )

    def forward_phase1(
        self,
        batch: dict,
        sdf_batch: dict[str, torch.Tensor],
    ) -> dict[str, torch.Tensor]:
        """
        Phase 1: SDF decoder warmup. Backbone frozen, no gradient refiner.

        Args:
            batch: openpi training batch (images, language, actions, etc.)
            sdf_batch: {query_points: [B, N, 3], sdf_gt: [B, N], sample_weights: [B, N]}

        Returns:
            losses dict
        """
        # TODO: Run backbone forward to get suffix_out
        # suffix_out = self.backbone.forward_to_suffix(batch)  # [B, action_horizon, 1024]
        # For now, we expect suffix_out to be extracted via a hook or explicit API
        suffix_out = batch["suffix_out"]  # placeholder interface

        # SDF prediction
        query_xyz = sdf_batch["query_points"]
        sdf_pred, sdf_grad = self.sdf_decoder(suffix_out, query_xyz, return_gradients=True)

        sdf_losses = compute_sdf_loss(
            sdf_pred=sdf_pred,
            sdf_gt=sdf_batch["sdf_gt"],
            sdf_gradients=sdf_grad,
            clamp_delta=self.config.sdf_clamp_delta,
            eikonal_weight=self.config.eikonal_weight,
            sample_weights=sdf_batch.get("sample_weights"),
        )

        return {
            "loss": sdf_losses["sdf_total"],
            **{f"sdf/{k}": v for k, v in sdf_losses.items()},
        }

    def forward_phase2(
        self,
        batch: dict,
        sdf_batch: dict[str, torch.Tensor],
    ) -> dict[str, torch.Tensor]:
        """
        Phase 2: End-to-end training with gradient refinement.

        Args:
            batch: openpi training batch
            sdf_batch: SDF ground truth data

        Returns:
            losses dict
        """
        # TODO: Run backbone forward to get suffix_out and flow matching target
        # suffix_out, flow_target = self.backbone.forward_to_suffix(batch, return_flow_target=True)
        suffix_out = batch["suffix_out"]
        flow_target = batch.get("flow_target")

        # --- Gradient refinement ---
        refined_features, refiner_info = self.gradient_refiner(suffix_out)

        # --- Flow matching loss on refined features ---
        # TODO: Pass refined_features through action_out_proj
        # predicted_velocity = self.backbone.action_out_proj(refined_features)
        # flow_loss = F.mse_loss(predicted_velocity, flow_target)
        flow_loss = batch.get("flow_loss", torch.tensor(0.0))  # placeholder

        # --- SDF auxiliary loss ---
        query_xyz = sdf_batch["query_points"]
        sdf_pred, sdf_grad = self.sdf_decoder(suffix_out, query_xyz, return_gradients=True)

        sdf_losses = compute_sdf_loss(
            sdf_pred=sdf_pred,
            sdf_gt=sdf_batch["sdf_gt"],
            sdf_gradients=sdf_grad,
            clamp_delta=self.config.sdf_clamp_delta,
            eikonal_weight=self.config.eikonal_weight,
            sample_weights=sdf_batch.get("sample_weights"),
        )

        # --- Gradient alignment loss ---
        align_loss = compute_gradient_alignment_loss(
            action_features=suffix_out,
            refined_features=refined_features,
            sdf_decoder=self.sdf_decoder,
            ee_positions=refiner_info["ee_positions"],
            collision_margin=self.config.collision_margin,
        )

        # --- Total loss ---
        total_loss = (
            flow_loss
            + self.config.sdf_loss_weight * sdf_losses["sdf_total"]
            + self.config.gradient_alignment_weight * align_loss
        )

        return {
            "loss": total_loss,
            "flow_loss": flow_loss.detach() if isinstance(flow_loss, torch.Tensor) else flow_loss,
            "gradient_alignment_loss": align_loss.detach(),
            "collision_cost": refiner_info["collision_cost"],
            "cost_grad_norm": refiner_info["cost_grad_norm"],
            "correction_norm": refiner_info["correction_norm"],
            **{f"sdf/{k}": v.detach() for k, v in sdf_losses.items()},
        }


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------

def setup_phase1(model: ColliForceVLA) -> list[dict]:
    """Freeze backbone, return optimizer param groups for Phase 1."""
    # TODO: Freeze backbone parameters
    # for p in model.backbone.parameters():
    #     p.requires_grad = False

    param_groups = [
        {
            "params": list(model.sdf_decoder.parameters()),
            "lr": model.config.sdf_decoder_lr,
            "name": "sdf_decoder",
        },
    ]
    return param_groups


def setup_phase2(model: ColliForceVLA) -> list[dict]:
    """
    Apply LoRA to action expert, unfreeze gradient refiner.
    Return optimizer param groups for Phase 2.
    """
    config = model.config

    # TODO: Apply LoRA to backbone action expert
    # from peft import LoraConfig, get_peft_model
    # lora_config = LoraConfig(
    #     r=config.lora_rank,
    #     lora_alpha=config.lora_alpha,
    #     target_modules=config.lora_target_modules,
    #     lora_dropout=0.0,
    #     bias="none",
    # )
    # model.backbone = apply_lora_to_action_expert(model.backbone, lora_config)

    param_groups = [
        {
            "params": list(model.sdf_decoder.parameters()),
            "lr": config.sdf_decoder_lr,
            "name": "sdf_decoder",
        },
        {
            "params": list(model.gradient_refiner.ee_extractor.parameters()),
            "lr": config.learning_rate,
            "name": "ee_extractor",
        },
        {
            "params": (
                list(model.gradient_refiner.gradient_correction.parameters())
                if model.gradient_refiner.gradient_correction is not None
                else []
            ),
            "lr": config.learning_rate,
            "name": "gradient_correction",
        },
        # TODO: Add LoRA params
        # {
        #     "params": [p for p in model.backbone.parameters() if p.requires_grad],
        #     "lr": config.learning_rate * 0.1,
        #     "name": "backbone_lora",
        # },
    ]
    return [g for g in param_groups if g["params"]]


def train(config: ColliForceConfig) -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # --- Model ---
    model = ColliForceVLA(config).to(device)
    logger.info(
        "ColliForceVLA initialized — SDF decoder params: %d, refiner params: %d",
        sum(p.numel() for p in model.sdf_decoder.parameters()),
        sum(p.numel() for p in model.gradient_refiner.parameters())
        - sum(p.numel() for p in model.sdf_decoder.parameters()),
    )

    # --- SDF data ---
    sdf_data_config = SDFDataConfig(
        data_dir=config.sdf_data_dir,
        n_query_points=config.n_query_points,
        clamp_delta=config.sdf_clamp_delta,
        near_surface_threshold=config.near_surface_threshold,
        near_surface_weight=config.near_surface_weight,
    )
    sdf_dataset = SDFDataset(sdf_data_config)
    sdf_collator = SDFBatchCollator(sdf_dataset)

    # TODO: Create openpi data loader
    # train_loader = create_openpi_dataloader(config)

    # ======================================================================
    # Phase 1: SDF decoder warmup
    # ======================================================================
    logger.info("=== Phase 1: SDF decoder warmup (%d epochs) ===", config.phase1_epochs)
    param_groups = setup_phase1(model)
    optimizer = torch.optim.AdamW(
        param_groups, lr=config.sdf_decoder_lr, weight_decay=config.weight_decay
    )

    global_step = 0
    for epoch in range(config.phase1_epochs):
        model.train()
        # TODO: Iterate over actual openpi data loader
        # for batch_idx, batch in enumerate(train_loader):
        #     sdf_batch = sdf_collator.collate_for_batch(batch["scene_ids"])
        #     if sdf_batch is None:
        #         continue
        #     sdf_batch = {k: v.to(device) for k, v in sdf_batch.items()}
        #     batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
        #
        #     losses = model.forward_phase1(batch, sdf_batch)
        #     optimizer.zero_grad()
        #     losses["loss"].backward()
        #     torch.nn.utils.clip_grad_norm_(model.sdf_decoder.parameters(), config.grad_clip_norm)
        #     optimizer.step()
        #
        #     if global_step % config.log_every == 0:
        #         log_losses(losses, global_step, prefix="phase1")
        #     global_step += 1
        pass

    # ======================================================================
    # Phase 2: End-to-end with gradient refinement + LoRA
    # ======================================================================
    logger.info("=== Phase 2: End-to-end training (%d epochs) ===", config.phase2_epochs)
    param_groups = setup_phase2(model)
    optimizer = torch.optim.AdamW(
        param_groups, lr=config.learning_rate, weight_decay=config.weight_decay
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=config.phase2_epochs,
    )

    for epoch in range(config.phase2_epochs):
        model.train()
        # TODO: Iterate over actual openpi data loader
        # for batch_idx, batch in enumerate(train_loader):
        #     sdf_batch = sdf_collator.collate_for_batch(batch["scene_ids"])
        #     if sdf_batch is None:
        #         continue
        #     sdf_batch = {k: v.to(device) for k, v in sdf_batch.items()}
        #     batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
        #
        #     losses = model.forward_phase2(batch, sdf_batch)
        #     optimizer.zero_grad()
        #     losses["loss"].backward()
        #     torch.nn.utils.clip_grad_norm_(
        #         [p for p in model.parameters() if p.requires_grad],
        #         config.grad_clip_norm,
        #     )
        #     optimizer.step()
        #
        #     if global_step % config.log_every == 0:
        #         log_losses(losses, global_step, prefix="phase2")
        #     if global_step % config.save_every == 0:
        #         save_checkpoint(model, optimizer, global_step, config.output_dir)
        #     global_step += 1
        pass

        scheduler.step()

    logger.info("Training complete. Total steps: %d", global_step)


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def log_losses(losses: dict[str, torch.Tensor], step: int, prefix: str = "") -> None:
    """Log losses to console and wandb."""
    msg = f"[{prefix}] step={step}"
    for k, v in losses.items():
        val = v.item() if isinstance(v, torch.Tensor) else v
        msg += f" {k}={val:.4f}"
    logger.info(msg)
    # TODO: wandb.log({f"{prefix}/{k}": v.item() for k, v in losses.items()}, step=step)


def save_checkpoint(
    model: ColliForceVLA,
    optimizer: torch.optim.Optimizer,
    step: int,
    output_dir: str,
) -> None:
    path = Path(output_dir) / f"checkpoint_{step:06d}.pt"
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "step": step,
            "sdf_decoder": model.sdf_decoder.state_dict(),
            "gradient_refiner_ee": model.gradient_refiner.ee_extractor.state_dict(),
            "gradient_refiner_correction": (
                model.gradient_refiner.gradient_correction.state_dict()
                if model.gradient_refiner.gradient_correction is not None
                else None
            ),
            # TODO: Save LoRA weights
            # "backbone_lora": get_lora_state_dict(model.backbone),
            "optimizer": optimizer.state_dict(),
        },
        path,
    )
    logger.info("Saved checkpoint to %s", path)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # TODO: Replace with tyro CLI parsing to match openpi style
    # import tyro
    # config = tyro.cli(ColliForceConfig)
    config = ColliForceConfig(
        openpi_checkpoint="checkpoints/pi0_libero",
        sdf_data_dir="data/sdf_libero",
        output_dir="checkpoints/colliforce_v1",
    )
    train(config)
