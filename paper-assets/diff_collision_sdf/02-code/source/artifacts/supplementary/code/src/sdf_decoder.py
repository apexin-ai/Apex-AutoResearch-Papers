"""
SDF MLP Decoder for ColliForce-VLA.

Takes action expert intermediate features and 3D query points,
predicts signed distance field values and spatial gradients.

Input:
  - action_features: [B, action_horizon, 1024] from suffix_out before action_out_proj
  - query_xyz: [B, N, 3] query points in workspace coordinates

Output:
  - sdf_values: [B, N] predicted signed distance
  - sdf_gradients: [B, N, 3] spatial gradients ∇_xyz SDF

Dependencies: torch
"""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F
from dataclasses import dataclass


@dataclass
class SDFDecoderConfig:
    feature_dim: int = 1024
    hidden_dim: int = 256
    n_layers: int = 4
    skip_layer: int = 2  # 0-indexed: inject skip at this layer's input
    softplus_beta: float = 5.0
    clamp_delta: float = 0.05
    aggregation: str = "mean"  # "mean" or "cross_attention"
    cross_attn_heads: int = 4


class SDFDecoder(nn.Module):
    """
    4-layer MLP with skip connection. Predicts SDF from action features + xyz.

    Architecture (validated in KG-3):
      layer0: Linear(feature_dim + 3, hidden) + Softplus
      layer1: Linear(hidden, hidden) + Softplus
      layer2: Linear(hidden + 3, hidden) + Softplus   ← skip: re-inject xyz
      layer3: Linear(hidden, 1)
    """

    def __init__(self, config: SDFDecoderConfig | None = None):
        super().__init__()
        if config is None:
            config = SDFDecoderConfig()
        self.config = config

        c = config
        self.layers = nn.ModuleList()
        # Layer 0: concat(feature, xyz) → hidden
        self.layers.append(nn.Linear(c.feature_dim + 3, c.hidden_dim))
        # Layer 1: hidden → hidden
        self.layers.append(nn.Linear(c.hidden_dim, c.hidden_dim))
        # Layer 2 (skip): hidden + 3 → hidden
        self.layers.append(nn.Linear(c.hidden_dim + 3, c.hidden_dim))
        # Layer 3: hidden → 1
        self.layers.append(nn.Linear(c.hidden_dim, 1))

        self.activation = nn.Softplus(beta=c.softplus_beta)

        if c.aggregation == "cross_attention":
            self.cross_attn = nn.MultiheadAttention(
                embed_dim=c.feature_dim,
                num_heads=c.cross_attn_heads,
                batch_first=True,
            )
            self.xyz_proj = nn.Linear(3, c.feature_dim)
        else:
            self.cross_attn = None
            self.xyz_proj = None

        self._init_weights()

    def _init_weights(self) -> None:
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
                if m.bias is not None:
                    nn.init.zeros_(m.bias)

    def aggregate_features(
        self,
        action_features: torch.Tensor,
        query_xyz: torch.Tensor,
    ) -> torch.Tensor:
        """
        Aggregate action_horizon features into per-query-point conditioning.

        Args:
            action_features: [B, action_horizon, feature_dim]
            query_xyz: [B, N, 3]

        Returns:
            [B, N, feature_dim] conditioning vector per query point.
        """
        if self.config.aggregation == "mean":
            # Mean pool over action_horizon → [B, feature_dim]
            pooled = action_features.mean(dim=1)
            # Broadcast to N query points → [B, N, feature_dim]
            return pooled.unsqueeze(1).expand(-1, query_xyz.shape[1], -1)

        elif self.config.aggregation == "cross_attention":
            assert self.cross_attn is not None
            # Query: xyz projected to feature_dim, Key/Value: action features
            query = self.xyz_proj(query_xyz)  # [B, N, feature_dim]
            attn_out, _ = self.cross_attn(
                query=query,
                key=action_features,
                value=action_features,
            )  # [B, N, feature_dim]
            return attn_out

        raise ValueError(f"Unknown aggregation: {self.config.aggregation}")

    def forward_sdf(
        self,
        features: torch.Tensor,
        xyz: torch.Tensor,
    ) -> torch.Tensor:
        """
        Raw SDF prediction for given per-point features and xyz.

        Args:
            features: [B, N, feature_dim]
            xyz: [B, N, 3]

        Returns:
            sdf: [B, N]
        """
        # Layer 0
        x = torch.cat([features, xyz], dim=-1)  # [B, N, feature_dim + 3]
        x = self.activation(self.layers[0](x))

        # Layer 1
        x = self.activation(self.layers[1](x))

        # Layer 2 with skip connection (re-inject xyz)
        x = torch.cat([x, xyz], dim=-1)  # [B, N, hidden + 3]
        x = self.activation(self.layers[2](x))

        # Layer 3 (output)
        sdf = self.layers[3](x).squeeze(-1)  # [B, N]
        return sdf

    def forward(
        self,
        action_features: torch.Tensor,
        query_xyz: torch.Tensor,
        return_gradients: bool = True,
    ) -> tuple[torch.Tensor, torch.Tensor | None]:
        """
        Args:
            action_features: [B, action_horizon, 1024]
            query_xyz: [B, N, 3] — requires_grad will be enabled internally for gradient computation
            return_gradients: if True, compute ∇_xyz SDF via autograd

        Returns:
            sdf_values: [B, N]
            sdf_gradients: [B, N, 3] or None
        """
        # Aggregate action features per query point
        cond = self.aggregate_features(action_features, query_xyz)  # [B, N, feature_dim]

        if return_gradients:
            xyz = query_xyz.detach().requires_grad_(True)
        else:
            xyz = query_xyz

        sdf = self.forward_sdf(cond, xyz)  # [B, N]

        if return_gradients:
            grad_outputs = torch.ones_like(sdf)
            (sdf_grad,) = torch.autograd.grad(
                outputs=sdf,
                inputs=xyz,
                grad_outputs=grad_outputs,
                create_graph=self.training,
                retain_graph=True,
            )  # [B, N, 3]
            return sdf, sdf_grad

        return sdf, None


def compute_sdf_loss(
    sdf_pred: torch.Tensor,
    sdf_gt: torch.Tensor,
    sdf_gradients: torch.Tensor | None,
    clamp_delta: float = 0.05,
    eikonal_weight: float = 0.01,
    sample_weights: torch.Tensor | None = None,
) -> dict[str, torch.Tensor]:
    """
    Args:
        sdf_pred: [B, N]
        sdf_gt: [B, N]
        sdf_gradients: [B, N, 3] or None
        clamp_delta: clamping range for SDF values
        eikonal_weight: weight for eikonal regularization
        sample_weights: [B, N] per-point importance weights

    Returns:
        dict with 'sdf_l1', 'eikonal', 'sdf_total' losses
    """
    # L1 clamped SDF loss
    pred_clamped = sdf_pred.clamp(-clamp_delta, clamp_delta)
    gt_clamped = sdf_gt.clamp(-clamp_delta, clamp_delta)
    l1 = (pred_clamped - gt_clamped).abs()

    if sample_weights is not None:
        l1 = l1 * sample_weights
    sdf_l1 = l1.mean()

    losses = {"sdf_l1": sdf_l1}

    # Eikonal regularization: (||∇_xyz SDF|| - 1)²
    if sdf_gradients is not None:
        grad_norm = sdf_gradients.norm(dim=-1)  # [B, N]
        eikonal = ((grad_norm - 1.0) ** 2).mean()
        losses["eikonal"] = eikonal
        losses["sdf_total"] = sdf_l1 + eikonal_weight * eikonal
    else:
        losses["sdf_total"] = sdf_l1

    return losses
