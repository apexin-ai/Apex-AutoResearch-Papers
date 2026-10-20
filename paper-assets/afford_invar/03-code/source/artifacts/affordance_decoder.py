"""
AffordanceDecoder: Generates affordance heatmaps from VLA intermediate features.

Takes layer-18 LLM hidden states (image tokens + text embedding) and produces
a [B, 1, 128, 128] affordance heatmap via transposed convolution upsampling
with FiLM-style text conditioning.

Architecture:
    Input: [B, 256, 4096] image tokens from LLM layer 18
    → Linear projection: 4096 → 512
    → Reshape to [B, 512, 16, 16]
    → 3x TransposedConv blocks with FiLM text conditioning
    → Sigmoid → [B, 1, 128, 128]

Parameters: ~7.9M (target ~8M)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class AffordanceDecoder(nn.Module):

    def __init__(
        self,
        hidden_dim: int = 4096,
        num_image_tokens: int = 256,
        grid_size: int = 16,
        proj_dim: int = 512,
        channels: tuple = (256, 64),
        num_groups: tuple = (32, 16),
        output_size: int = 128,
    ):
        """
        Args:
            hidden_dim: LLM hidden dimension (4096 for Llama-2-7b)
            num_image_tokens: Number of image tokens in LLM sequence (256 for OpenVLA)
            grid_size: Spatial grid size (sqrt of num_image_tokens, 16 for 16x16)
            proj_dim: Channel dim after initial projection (512)
            channels: Channel dims for deconv blocks (256, 64)
            num_groups: GroupNorm groups for each block (32, 16)
            output_size: Output heatmap resolution (128)
        """
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_image_tokens = num_image_tokens
        self.grid_size = grid_size
        self.output_size = output_size
        assert num_image_tokens == grid_size * grid_size

        ch0 = proj_dim      # 512
        ch1 = channels[0]   # 256
        ch2 = channels[1]   # 64

        # Linear projection: 4096 → 512
        self.input_proj = nn.Linear(hidden_dim, ch0)

        # Block 1: 16×16 → 32×32
        self.deconv1 = nn.ConvTranspose2d(ch0, ch1, kernel_size=4, stride=2, padding=1)
        self.gn1 = nn.GroupNorm(num_groups[0], ch1)

        # Block 2: 32×32 → 64×64
        self.deconv2 = nn.ConvTranspose2d(ch1, ch2, kernel_size=4, stride=2, padding=1)
        self.gn2 = nn.GroupNorm(num_groups[1], ch2)

        # Block 3: 64×64 → 128×128
        self.deconv3 = nn.ConvTranspose2d(ch2, 1, kernel_size=4, stride=2, padding=1)

        self.act = nn.GELU()

        # FiLM text conditioning: scale features before each deconv block
        self.text_proj1 = nn.Linear(hidden_dim, ch0)
        self.text_proj2 = nn.Linear(hidden_dim, ch1)
        self.text_proj3 = nn.Linear(hidden_dim, ch2)

        self._init_weights()

    def _init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.ConvTranspose2d):
                nn.init.kaiming_normal_(m.weight, nonlinearity="linear")
                if m.bias is not None:
                    nn.init.zeros_(m.bias)
            elif isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight, nonlinearity="linear")
                if m.bias is not None:
                    nn.init.zeros_(m.bias)
        # FiLM projections: init near identity (output ≈ 1) so early training
        # doesn't destroy spatial features
        for proj in [self.text_proj1, self.text_proj2, self.text_proj3]:
            nn.init.zeros_(proj.weight)
            nn.init.ones_(proj.bias)

    def forward(
        self,
        image_features: torch.Tensor,
        text_embed: torch.Tensor,
    ) -> torch.Tensor:
        """
        Args:
            image_features: [B, num_image_tokens, hidden_dim] image tokens from LLM layer
            text_embed: [B, hidden_dim] mean-pooled text token features

        Returns:
            heatmap: [B, 1, output_size, output_size] affordance heatmap in [0, 1]
        """
        B = image_features.shape[0]

        # Project: [B, 256, 4096] → [B, 256, 512]
        x = self.input_proj(image_features)

        # Reshape to spatial grid: [B, 256, 512] → [B, 512, 16, 16]
        x = x.permute(0, 2, 1).reshape(B, -1, self.grid_size, self.grid_size)

        # Block 1: FiLM scale → deconv → GroupNorm → GELU → [B, 256, 32, 32]
        scale1 = self.text_proj1(text_embed).unsqueeze(-1).unsqueeze(-1)
        x = x * scale1
        x = self.act(self.gn1(self.deconv1(x)))

        # Block 2: FiLM scale → deconv → GroupNorm → GELU → [B, 64, 64, 64]
        scale2 = self.text_proj2(text_embed).unsqueeze(-1).unsqueeze(-1)
        x = x * scale2
        x = self.act(self.gn2(self.deconv2(x)))

        # Block 3: FiLM scale → deconv → sigmoid → [B, 1, 128, 128]
        scale3 = self.text_proj3(text_embed).unsqueeze(-1).unsqueeze(-1)
        x = x * scale3
        x = torch.sigmoid(self.deconv3(x))

        return x

    @staticmethod
    def extract_features(
        hidden_states: tuple,
        layer_idx: int = 18,
        num_patches: int = 256,
        num_text_tokens: int = None,
    ) -> tuple:
        """
        Extract image features and text embedding from LLM hidden states.

        In OpenVLA's multimodal sequence layout:
            [BOS(1)] [image_patches(num_patches)] [text_tokens...] [action_tokens...] [stop(1)]

        Args:
            hidden_states: Tuple from LLM with output_hidden_states=True.
                hidden_states[0] = embedding layer output
                hidden_states[i] = layer-i output (1-indexed)
            layer_idx: LLM layer index (1-indexed, default 18)
            num_patches: Number of image tokens (256 for OpenVLA)
            num_text_tokens: Number of text prompt tokens (excluding BOS).
                If None, uses all tokens after image patches for mean pooling.

        Returns:
            image_features: [B, num_patches, hidden_dim]
            text_embed: [B, hidden_dim]
        """
        h = hidden_states[layer_idx]  # [B, seq_len, hidden_dim]

        # Image tokens: positions 1 to num_patches (position 0 = BOS)
        image_features = h[:, 1 : 1 + num_patches, :]

        # Text tokens: start after image patches
        text_start = 1 + num_patches
        if num_text_tokens is not None:
            text_end = text_start + num_text_tokens
        else:
            text_end = h.shape[1]
        text_tokens = h[:, text_start:text_end, :]
        text_embed = text_tokens.mean(dim=1)

        return image_features, text_embed
