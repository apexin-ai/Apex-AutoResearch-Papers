"""
K=1 Multi-Scale Conformal Refinement Module (MSCRM).

Single-sample correction: no candidate selection, direct action refinement.
Uses multi-scale VLM features from transformer layers [3, 7, 11, 15] with
action-conditioned attention fusion.

Architecture:
  1. Multi-scale feature extraction via hooks on VLM text_model layers
  2. Shared bottleneck projection: 960D -> 192D per layer
  3. Layer-specific FiLM modulation
  4. Action-conditioned attention: base_action queries layer features
  5. Correction MLP with GELU + LayerNorm -> delta -> eps-clipped

Input: base_action (30D) + multi_scale_obs (4x960D or fallback 1x960D)
Output: refined_action (30D) = base_action + clipped_delta
Params: ~323K
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from contextlib import contextmanager

EXTRACT_LAYERS = [3, 7, 11, 15]


class MultiScaleFeatureExtractor:
    """Extract intermediate hidden states from SmolVLA VLM text_model via forward hooks.

    During SmolVLAWrapper.encode_prefix, the VLM text model processes prefix tokens
    through 16 LlamaDecoderLayers. This extractor captures hidden states at specified
    layer boundaries without modifying existing code.

    Hooks:
      - Layer N (N < 15): hook on layers[N+1].input_layernorm INPUT -> layer N output
      - Layer 15: hook on text_model.norm OUTPUT -> post-norm final representation
    """

    def __init__(self, text_model, layer_indices=None):
        self.text_model = text_model
        self.layer_indices = layer_indices or EXTRACT_LAYERS
        self.captured = {}
        self._hooks = []

    def _make_input_hook(self, layer_idx):
        def hook_fn(module, inp, out):
            self.captured[layer_idx] = inp[0].detach()
        return hook_fn

    def _make_output_hook(self, layer_idx):
        def hook_fn(module, inp, out):
            self.captured[layer_idx] = out.detach()
        return hook_fn

    def register(self):
        self.remove()
        num_layers = len(self.text_model.layers)
        for idx in self.layer_indices:
            if idx < num_layers - 1:
                hook = self.text_model.layers[idx + 1].input_layernorm.register_forward_hook(
                    self._make_input_hook(idx)
                )
            else:
                hook = self.text_model.norm.register_forward_hook(
                    self._make_output_hook(idx)
                )
            self._hooks.append(hook)

    def remove(self):
        for h in self._hooks:
            h.remove()
        self._hooks = []
        self.captured = {}

    def get_features(self, pad_mask):
        """Mean-pool captured hidden states using pad_mask -> list of (B, 960)."""
        features = []
        mask = pad_mask.unsqueeze(-1).float()
        for idx in self.layer_indices:
            h = self.captured[idx].float()
            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)
            features.append(pooled)
        return features

    @contextmanager
    def capture(self):
        self.register()
        self.captured = {}
        try:
            yield self
        finally:
            self.remove()


class MultiScaleCRM(nn.Module):
    """K=1 CRM with multi-scale VLM feature fusion and action-conditioned attention."""

    def __init__(self, action_dim=30, obs_dim=960,
                 hidden_dim=256, bottleneck_dim=192,
                 num_scale_layers=4,
                 max_correction_norm=1.42):
        super().__init__()
        self.action_dim = action_dim
        self.obs_dim = obs_dim
        self.bottleneck_dim = bottleneck_dim
        self.num_scale_layers = num_scale_layers
        self.max_correction_norm = max_correction_norm

        # Shared bottleneck for all VLM layer features
        self.layer_proj = nn.Linear(obs_dim, bottleneck_dim)

        # Layer-specific FiLM (Feature-wise Linear Modulation)
        self.film_scale = nn.Parameter(torch.ones(num_scale_layers, bottleneck_dim))
        self.film_shift = nn.Parameter(torch.zeros(num_scale_layers, bottleneck_dim))

        # Action query for attention over multi-scale features
        self.action_query_proj = nn.Linear(action_dim, bottleneck_dim)

        # Correction MLP
        mlp_input_dim = action_dim + bottleneck_dim
        self.mlp = nn.Sequential(
            nn.Linear(mlp_input_dim, hidden_dim),
            nn.GELU(),
            nn.LayerNorm(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, action_dim),
        )

        # Per-layer normalization buffers
        self.register_buffer("action_mean", torch.zeros(action_dim))
        self.register_buffer("action_std", torch.ones(action_dim))
        self.register_buffer("obs_mean", torch.zeros(num_scale_layers, obs_dim))
        self.register_buffer("obs_std", torch.ones(num_scale_layers, obs_dim))

        # Residual init: last layer near zero
        nn.init.zeros_(self.mlp[-1].weight)
        nn.init.zeros_(self.mlp[-1].bias)

    def forward(self, base_action, multi_scale_obs):
        """
        Args:
            base_action: (B, action_dim)
            multi_scale_obs: list of (B, obs_dim) from VLM layers,
                             or single (B, obs_dim) tensor for fallback
        Returns:
            refined_action: (B, action_dim)
        """
        action_norm = (base_action - self.action_mean) / (self.action_std + 1e-8)

        # Fallback: single obs feature -> skip attention
        if isinstance(multi_scale_obs, torch.Tensor) and multi_scale_obs.dim() == 2:
            feat_norm = (multi_scale_obs - self.obs_mean[-1]) / (self.obs_std[-1] + 1e-8)
            fused = self.layer_proj(feat_norm)
            if self.num_scale_layers > 0:
                fused = fused * self.film_scale[-1] + self.film_shift[-1]
        else:
            projected = []
            for i, feat in enumerate(multi_scale_obs):
                idx = min(i, self.num_scale_layers - 1)
                feat_norm = (feat - self.obs_mean[idx]) / (self.obs_std[idx] + 1e-8)
                p = self.layer_proj(feat_norm)
                p = p * self.film_scale[idx] + self.film_shift[idx]
                projected.append(p)

            features = torch.stack(projected, dim=1)
            query = self.action_query_proj(action_norm).unsqueeze(1)
            attn_logits = (query * features).sum(-1) / (self.bottleneck_dim ** 0.5)
            attn_weights = F.softmax(attn_logits, dim=-1)
            fused = (attn_weights.unsqueeze(-1) * features).sum(1)

        x = torch.cat([action_norm, fused], dim=-1)
        delta = self.mlp(x)

        # Epsilon-bound norm clipping
        delta_norm = delta.norm(dim=-1, keepdim=True)
        delta = delta * torch.clamp(self.max_correction_norm / (delta_norm + 1e-8), max=1.0)

        return base_action + delta

    def set_normalization_stats(self, action_mean, action_std, obs_mean, obs_std):
        """Set input normalization buffers.

        Args:
            action_mean: (action_dim,)
            action_std: (action_dim,)
            obs_mean: (num_scale_layers, obs_dim) or (obs_dim,)
            obs_std: (num_scale_layers, obs_dim) or (obs_dim,)
        """
        self.action_mean.copy_(action_mean)
        self.action_std.copy_(action_std)
        if obs_mean.dim() == 1:
            self.obs_mean[:] = obs_mean.unsqueeze(0)
            self.obs_std[:] = obs_std.unsqueeze(0)
        else:
            self.obs_mean.copy_(obs_mean)
            self.obs_std.copy_(obs_std)

    def count_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)


class CRMMultiLoss(nn.Module):
    """Combined loss for K=1 CRM training.

    Components:
      - L2 residual: MSE(refined, expert)
      - Direction-aware: 1 - cosine_similarity(delta_pred, delta_true)
      - Triplet improvement: max(0, margin + d(refined,expert) - d(vla,expert))
      - Correction magnitude: ||delta||^2 regularization
    """

    def __init__(self, lambda_dir=0.1, lambda_tri=0.05, lambda_mag=0.01,
                 triplet_margin=0.01, dir_threshold=0.01):
        super().__init__()
        self.lambda_dir = lambda_dir
        self.lambda_tri = lambda_tri
        self.lambda_mag = lambda_mag
        self.triplet_margin = triplet_margin
        self.dir_threshold = dir_threshold

    def forward(self, refined, expert, base_action):
        """Returns (total_loss, loss_dict)."""
        l2_loss = F.mse_loss(refined, expert)

        delta_pred = refined - base_action
        delta_true = expert - base_action

        # Direction loss (only on samples with meaningful correction)
        delta_true_norm = delta_true.norm(dim=-1)
        valid = delta_true_norm > self.dir_threshold
        if valid.any():
            dir_loss = (1 - F.cosine_similarity(
                delta_pred[valid], delta_true[valid], dim=-1
            )).mean()
        else:
            dir_loss = torch.tensor(0.0, device=refined.device)

        # Triplet improvement loss
        d_refined = (refined - expert).norm(dim=-1)
        d_vla = (base_action - expert).norm(dim=-1)
        tri_loss = F.relu(self.triplet_margin + d_refined - d_vla).mean()

        # Magnitude regularization
        mag_loss = delta_pred.pow(2).mean()

        total = (l2_loss
                 + self.lambda_dir * dir_loss
                 + self.lambda_tri * tri_loss
                 + self.lambda_mag * mag_loss)

        return total, {
            "l2": l2_loss.item(),
            "dir": dir_loss.item(),
            "tri": tri_loss.item(),
            "mag": mag_loss.item(),
            "total": total.item(),
        }


if __name__ == "__main__":
    print("=" * 60)
    print("MultiScaleCRM (K=1) verification")
    print("=" * 60)

    model = MultiScaleCRM()
    n_params = model.count_parameters()
    print(f"\nTotal parameters: {n_params:,}")
    print(f"  layer_proj:        {sum(p.numel() for p in model.layer_proj.parameters()):,}")
    print(f"  FiLM:              {model.film_scale.numel() + model.film_shift.numel():,}")
    print(f"  action_query_proj: {sum(p.numel() for p in model.action_query_proj.parameters()):,}")
    print(f"  MLP:               {sum(p.numel() for p in model.mlp.parameters()):,}")

    B = 4

    # Multi-scale forward
    action = torch.randn(B, 30)
    obs_list = [torch.randn(B, 960) for _ in range(4)]
    out = model(action, obs_list)
    print(f"\nMulti-scale forward: action {action.shape} -> output {out.shape}")
    assert out.shape == (B, 30), f"Shape mismatch: {out.shape}"

    # Single-scale fallback
    obs_single = torch.randn(B, 960)
    out2 = model(action, obs_single)
    print(f"Fallback forward:    action {action.shape}, obs {obs_single.shape} -> output {out2.shape}")
    assert out2.shape == (B, 30), f"Shape mismatch: {out2.shape}"

    # Correction norm clipping
    model.max_correction_norm = 0.1
    out3 = model(action, obs_list)
    delta_norms = (out3 - action).norm(dim=-1)
    print(f"\nCorrection norms (eps={model.max_correction_norm}): "
          f"max={delta_norms.max().item():.4f}")
    assert (delta_norms <= model.max_correction_norm + 1e-5).all(), "Norm clipping failed"

    # Loss computation
    loss_fn = CRMMultiLoss()
    expert = action + torch.randn(B, 30) * 0.1
    total_loss, loss_dict = loss_fn(out3, expert, action)
    print(f"\nLoss components:")
    for k, v in loss_dict.items():
        print(f"  {k}: {v:.6f}")

    # Gradient flow
    model.max_correction_norm = 1.42
    model.zero_grad()
    out4 = model(action, obs_list)
    loss, _ = loss_fn(out4, expert, action)
    loss.backward()
    grad_norms = {name: p.grad.norm().item()
                  for name, p in model.named_parameters()
                  if p.grad is not None}
    print(f"\nGradient norms (all modules):")
    for name, gn in sorted(grad_norms.items()):
        print(f"  {name}: {gn:.6f}")

    print(f"\n{'=' * 60}")
    print("All checks passed!")
    print(f"{'=' * 60}")
