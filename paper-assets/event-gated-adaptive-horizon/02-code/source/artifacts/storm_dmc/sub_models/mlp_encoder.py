"""
MLP encoder and decoder for proprioceptive observations.

Replaces STORM's CNN EncoderBN/DecoderBN for use with low-dimensional
vector observations (e.g., 24-dim Walker Walk proprioceptive state).
"""
import torch
import torch.nn as nn
from einops import rearrange


class MLPEncoder(nn.Module):
    """
    Maps proprioceptive vector obs to an embedding compatible with STORM's DistHead.

    Input:  (B, L, obs_dim)   e.g. (B, L, 24)
    Output: (B, L, output_dim) e.g. (B, L, 256)
    """

    def __init__(self, obs_dim, hidden_dim=256, output_dim=256):
        super().__init__()
        self.output_dim = output_dim
        self.backbone = nn.Sequential(
            nn.Linear(obs_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(inplace=True),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(inplace=True),
            nn.Linear(hidden_dim, output_dim),
            nn.LayerNorm(output_dim),
        )

    def forward(self, x):
        # x: (B, L, obs_dim)
        return self.backbone(x)


class MLPDecoder(nn.Module):
    """
    Reconstructs proprioceptive vector obs from stochastic latent.

    Input:  (B, L, stoch_dim)  e.g. (B, L, 1024)
    Output: (B, L, obs_dim)    e.g. (B, L, 24)
    """

    def __init__(self, stoch_dim, obs_dim, hidden_dim=256):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Linear(stoch_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(inplace=True),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(inplace=True),
            nn.Linear(hidden_dim, obs_dim),
        )

    def forward(self, x):
        # x: (B, L, stoch_dim)
        return self.backbone(x)
