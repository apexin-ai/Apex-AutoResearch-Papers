"""RoPE apply/remove/restore utilities for CompressLink NoPE pipeline."""

import torch
from torch import Tensor
from typing import Tuple


def rotate_half(x: Tensor) -> Tensor:
    x1 = x[..., : x.shape[-1] // 2]
    x2 = x[..., x.shape[-1] // 2 :]
    return torch.cat((-x2, x1), dim=-1)


def apply_rope_query_only(q: Tensor, cos: Tensor, sin: Tensor) -> Tensor:
    """Apply RoPE to query only. Same math as standard apply_rotary_pos_emb for Q."""
    return (q * cos) + (rotate_half(q) * sin)


def apply_rope_key_only(k_nope: Tensor, cos: Tensor, sin: Tensor) -> Tensor:
    """Apply RoPE to NoPE keys (forward rotation)."""
    return (k_nope * cos) + (rotate_half(k_nope) * sin)


def remove_rope(k_rope: Tensor, cos: Tensor, sin: Tensor) -> Tensor:
    """Remove RoPE from post-RoPE keys (inverse rotation)."""
    return (k_rope * cos) - (rotate_half(k_rope) * sin)


def get_rope_embeddings(
    config, positions: Tensor, device: torch.device
) -> Tuple[Tensor, Tensor]:
    """Compute cos/sin RoPE embeddings for given positions.

    Args:
        config: model config with hidden_size, num_attention_heads, rope_theta
        positions: [seq_len] or [batch, seq_len] position indices
        device: torch device

    Returns:
        cos, sin: broadcastable to [batch, 1, seq_len, head_dim]
    """
    head_dim = getattr(
        config, "head_dim", config.hidden_size // config.num_attention_heads
    )
    rope_theta = getattr(config, "rope_theta", 10000.0)

    inv_freq = 1.0 / (
        rope_theta
        ** (torch.arange(0, head_dim, 2, device=device, dtype=torch.float32) / head_dim)
    )

    if positions.dim() == 1:
        positions = positions.unsqueeze(0)

    freqs = torch.einsum("bi,j->bij", positions.float().to(device), inv_freq)
    emb = torch.cat((freqs, freqs), dim=-1)

    cos = emb.cos().unsqueeze(1)  # [batch, 1, seq_len, head_dim]
    sin = emb.sin().unsqueeze(1)

    return cos, sin
