"""Tests for RoPE utility functions."""

import sys
from pathlib import Path
from types import SimpleNamespace

import torch
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from compresslink.rope_utils import (
    rotate_half,
    apply_rope_query_only,
    apply_rope_key_only,
    remove_rope,
    get_rope_embeddings,
)


def test_rotate_half_twice_negates():
    x = torch.randn(2, 4, 8, 64)
    assert torch.allclose(rotate_half(rotate_half(x)), -x)


def test_remove_rope_inverts_apply():
    x = torch.randn(1, 4, 16, 128)
    # Proper rotation: cos^2 + sin^2 = 1
    angles = torch.randn(1, 1, 16, 64)
    cos = torch.cos(angles).repeat(1, 1, 1, 2)
    sin = torch.sin(angles).repeat(1, 1, 1, 2)

    k_rope = apply_rope_key_only(x, cos, sin)
    k_nope = remove_rope(k_rope, cos, sin)
    assert torch.allclose(x, k_nope, atol=1e-5)


def test_query_only_matches_standard():
    """Q-only RoPE gives same result as standard RoPE's Q component."""
    q = torch.randn(1, 4, 16, 128)
    cos = torch.randn(1, 1, 16, 128)
    sin = torch.randn(1, 1, 16, 128)

    q_rope = apply_rope_query_only(q, cos, sin)
    q_standard = (q * cos) + (rotate_half(q) * sin)
    assert torch.allclose(q_rope, q_standard)


def test_get_rope_embeddings_shape():
    config = SimpleNamespace(
        hidden_size=4096, num_attention_heads=32, rope_theta=500000.0
    )
    positions = torch.arange(128)
    cos, sin = get_rope_embeddings(config, positions, torch.device("cpu"))
    # head_dim = 4096/32 = 128
    assert cos.shape == (1, 1, 128, 128)
    assert sin.shape == (1, 1, 128, 128)


def test_get_rope_embeddings_batch():
    config = SimpleNamespace(
        hidden_size=256, num_attention_heads=4, rope_theta=10000.0
    )
    positions = torch.arange(32).unsqueeze(0).expand(2, -1)  # [2, 32]
    cos, sin = get_rope_embeddings(config, positions, torch.device("cpu"))
    assert cos.shape == (2, 1, 32, 64)
    # Batch entries should be identical for same positions
    assert torch.allclose(cos[0], cos[1])


def test_nope_attention_equivalence():
    """Q_rope @ apply_rope(K_nope).T == Q_rope @ K_rope.T when K_nope is original."""
    B, H, T, D = 1, 4, 32, 64
    q = torch.randn(B, H, T, D)
    k = torch.randn(B, H, T, D)

    angles = torch.randn(1, 1, T, D // 2)
    cos = torch.cos(angles).repeat(1, 1, 1, 2)
    sin = torch.sin(angles).repeat(1, 1, 1, 2)

    q_rope = apply_rope_query_only(q, cos, sin)
    k_rope = apply_rope_key_only(k, cos, sin)

    attn_standard = q_rope @ k_rope.transpose(-2, -1)

    # NoPE path: store k as NoPE, apply rope at attention time
    k_rope_from_nope = apply_rope_key_only(k, cos, sin)
    attn_nope = q_rope @ k_rope_from_nope.transpose(-2, -1)

    assert torch.allclose(attn_standard, attn_nope, atol=1e-5)
