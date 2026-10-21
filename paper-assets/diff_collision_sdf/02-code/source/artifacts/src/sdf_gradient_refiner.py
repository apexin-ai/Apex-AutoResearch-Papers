"""
SDF Gradient-Guided Action Refinement — ColliForce-VLA primary novelty.

Single forward-pass refinement: uses SDF gradients w.r.t. action features
to push action representations away from collision regions.

Input:
  - action_features: [B, action_horizon, 1024] from action expert suffix_out
  - candidate_ee_positions: [B, action_horizon, 3] end-effector positions derived from actions

Output:
  - refined_action_features: [B, action_horizon, 1024]

Dependencies: torch, sdf_decoder.SDFDecoder
"""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F
from dataclasses import dataclass

from .sdf_decoder import SDFDecoder, SDFDecoderConfig


@dataclass
class GradientRefinerConfig:
    feature_dim: int = 1024
    collision_margin: float = 0.02
    refinement_alpha: float = 0.1
    # Learned projection from feature-space gradient to correction
    use_learned_projection: bool = True
    # If False, directly use raw gradient (scaled by alpha)
    detach_sdf_decoder: bool = False
    # Softplus temperature for collision cost (smoother than ReLU)
    collision_softplus_beta: float = 10.0


class EEPositionExtractor(nn.Module):
    """
    Extracts end-effector xyz positions from action tokens.

    In π0, actions are in a normalized space. This module learns a linear
    mapping from action features to 3D workspace coordinates.
    """

    def __init__(self, feature_dim: int = 1024):
        super().__init__()
        self.proj = nn.Linear(feature_dim, 3)

    def forward(self, action_features: torch.Tensor) -> torch.Tensor:
        """
        Args:
            action_features: [B, action_horizon, feature_dim]

        Returns:
            ee_positions: [B, action_horizon, 3]
        """
        return self.proj(action_features)


class GradientCorrection(nn.Module):
    """
    Learned linear projection: maps collision gradient in feature space
    to an action correction vector.
    """

    def __init__(self, feature_dim: int = 1024):
        super().__init__()
        self.proj = nn.Linear(feature_dim, feature_dim, bias=False)
        nn.init.zeros_(self.proj.weight)

    def forward(self, grad: torch.Tensor) -> torch.Tensor:
        """
        Args:
            grad: [B, action_horizon, feature_dim] — ∂collision_cost/∂action_features

        Returns:
            correction: [B, action_horizon, feature_dim]
        """
        return self.proj(grad)


class SDFGradientRefiner(nn.Module):
    """
    Core ColliForce-VLA mechanism: single-pass SDF-gradient-guided action refinement.

    Flow:
      1. Extract candidate EE positions from action features
      2. Query SDF decoder at EE positions → SDF values per timestep
      3. Compute collision_cost = Softplus(-SDF + margin)
      4. Backprop collision_cost → ∂cost/∂action_features
      5. Learned projection maps gradient to action correction
      6. refined = action_features - alpha * correction
    """

    def __init__(
        self,
        config: GradientRefinerConfig | None = None,
        sdf_decoder: SDFDecoder | None = None,
        sdf_config: SDFDecoderConfig | None = None,
    ):
        super().__init__()
        if config is None:
            config = GradientRefinerConfig()
        self.config = config

        # SDF decoder — shared with auxiliary SDF training
        if sdf_decoder is not None:
            self.sdf_decoder = sdf_decoder
        else:
            self.sdf_decoder = SDFDecoder(sdf_config or SDFDecoderConfig())

        self.ee_extractor = EEPositionExtractor(config.feature_dim)

        if config.use_learned_projection:
            self.gradient_correction = GradientCorrection(config.feature_dim)
        else:
            self.gradient_correction = None

        self.collision_softplus = nn.Softplus(beta=config.collision_softplus_beta)

    def compute_collision_cost(
        self,
        action_features: torch.Tensor,
        ee_positions: torch.Tensor,
    ) -> torch.Tensor:
        """
        Compute per-timestep collision cost from SDF values at EE positions.

        Args:
            action_features: [B, action_horizon, feature_dim]
            ee_positions: [B, action_horizon, 3]

        Returns:
            collision_cost: scalar, mean collision cost over batch and horizon
        """
        # Query SDF at each EE position — treat each timestep as a single query point
        # Reshape: [B, action_horizon, 3] → use action_horizon as N query points
        sdf_values, _ = self.sdf_decoder(
            action_features, ee_positions, return_gradients=False
        )  # [B, action_horizon]

        # Softplus(-SDF + margin): smooth penalty for being inside or near surface
        cost = self.collision_softplus(-sdf_values + self.config.collision_margin)
        return cost.mean()

    def forward(
        self,
        action_features: torch.Tensor,
        ee_positions: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        """
        Args:
            action_features: [B, action_horizon, 1024]
            ee_positions: [B, action_horizon, 3] or None (will be extracted if None)

        Returns:
            refined_features: [B, action_horizon, 1024]
            info: dict with intermediate values for logging/loss computation
        """
        if ee_positions is None:
            ee_positions = self.ee_extractor(action_features)

        info: dict[str, torch.Tensor] = {"ee_positions": ee_positions}

        # --- Compute collision cost gradient w.r.t. action_features ---
        # We need action_features to be a leaf for autograd.grad
        features_for_grad = action_features
        if not features_for_grad.requires_grad:
            features_for_grad = features_for_grad.detach().requires_grad_(True)

        collision_cost = self.compute_collision_cost(features_for_grad, ee_positions)
        info["collision_cost"] = collision_cost.detach()

        # Compute ∇_features collision_cost
        (cost_grad,) = torch.autograd.grad(
            outputs=collision_cost,
            inputs=features_for_grad,
            create_graph=self.training,  # need higher-order grads during training
            retain_graph=True,
        )  # [B, action_horizon, feature_dim]

        info["cost_grad_norm"] = cost_grad.detach().norm(dim=-1).mean()

        # --- Map gradient to correction ---
        if self.gradient_correction is not None:
            correction = self.gradient_correction(cost_grad)
        else:
            correction = cost_grad

        # Refine: move features in the negative gradient direction (reduce collision)
        refined = action_features - self.config.refinement_alpha * correction
        info["correction_norm"] = correction.detach().norm(dim=-1).mean()

        return refined, info


def compute_gradient_alignment_loss(
    action_features: torch.Tensor,
    refined_features: torch.Tensor,
    sdf_decoder: SDFDecoder,
    ee_positions: torch.Tensor,
    collision_margin: float = 0.02,
) -> torch.Tensor:
    """
    Encourage that refined features produce higher SDF values (less collision)
    at the EE positions compared to original features.

    Args:
        action_features: [B, action_horizon, feature_dim] — original
        refined_features: [B, action_horizon, feature_dim] — after refinement
        sdf_decoder: shared SDF decoder
        ee_positions: [B, action_horizon, 3]
        collision_margin: safety margin

    Returns:
        alignment_loss: scalar — penalizes cases where refinement doesn't reduce collision
    """
    with torch.no_grad():
        sdf_original, _ = sdf_decoder(
            action_features, ee_positions, return_gradients=False
        )

    sdf_refined, _ = sdf_decoder(
        refined_features, ee_positions, return_gradients=False
    )

    # We want sdf_refined > sdf_original (further from collision)
    # Loss = mean(ReLU(sdf_original - sdf_refined + margin))
    # Penalizes when refined SDF is not sufficiently better
    delta = sdf_original - sdf_refined + collision_margin
    loss = F.relu(delta).mean()
    return loss
