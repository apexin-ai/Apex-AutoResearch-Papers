"""NoPE KV storage + Q-only RoPE attention (MEPIC core).

Monkey-patches LlamaAttention.forward() to:
1. Apply RoPE only to queries
2. Store keys in NoPE (no positional encoding) format in cache
3. Apply RoPE to all cached keys dynamically during attention computation
4. Force eager attention (Flash Attention does not support dynamic RoPE)
"""

import math
import types
import torch
import torch.nn.functional as F
from typing import Optional, Tuple, Dict

from .rope_utils import apply_rope_query_only, apply_rope_key_only, get_rope_embeddings

_PATCHED_MODELS: Dict[int, Dict] = {}


def _repeat_kv(hidden_states: torch.Tensor, n_rep: int) -> torch.Tensor:
    if n_rep == 1:
        return hidden_states
    batch, num_kv_heads, slen, head_dim = hidden_states.shape
    hidden_states = hidden_states[:, :, None, :, :].expand(
        batch, num_kv_heads, n_rep, slen, head_dim
    )
    return hidden_states.reshape(batch, num_kv_heads * n_rep, slen, head_dim)


def _nope_forward(
    self,
    hidden_states: torch.Tensor,
    attention_mask: Optional[torch.Tensor] = None,
    position_ids: Optional[torch.LongTensor] = None,
    past_key_value=None,  # also accept past_key_values
    output_attentions: bool = False,
    use_cache: bool = False,
    cache_position: Optional[torch.LongTensor] = None,
    position_embeddings: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
    **kwargs,
) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
    # Handle both past_key_value and past_key_values parameter names
    if past_key_value is None:
        past_key_value = kwargs.pop('past_key_values', None)
    bsz, q_len, _ = hidden_states.size()

    query_states = self.q_proj(hidden_states)
    key_states = self.k_proj(hidden_states)
    value_states = self.v_proj(hidden_states)

    num_heads = self.config.num_attention_heads
    num_kv_heads = self.config.num_key_value_heads
    head_dim = self.head_dim
    num_kv_groups = num_heads // num_kv_heads

    query_states = query_states.view(bsz, q_len, num_heads, head_dim).transpose(1, 2)
    key_states = key_states.view(bsz, q_len, num_kv_heads, head_dim).transpose(1, 2)
    value_states = value_states.view(bsz, q_len, num_kv_heads, head_dim).transpose(1, 2)

    # --- RoPE: Q-only ---
    if position_embeddings is not None:
        cos, sin = position_embeddings
    elif hasattr(self, "rotary_emb"):
        cos, sin = self.rotary_emb(value_states, position_ids)
    else:
        cos, sin = get_rope_embeddings(
            self._nope_config, position_ids.squeeze(0), hidden_states.device
        )
    cos = cos.to(query_states.dtype)
    sin = sin.to(query_states.dtype)
    query_states = apply_rope_query_only(query_states, cos, sin)
    # key_states remains NoPE

    # --- Update KV cache with NoPE keys ---
    if past_key_value is not None:
        cache_kwargs = {}
        if cache_position is not None:
            cache_kwargs["cache_position"] = cache_position
        key_states, value_states = past_key_value.update(
            key_states, value_states, self.layer_idx, cache_kwargs
        )

    # --- Dynamic RoPE on ALL cached keys ---
    kv_seq_len = key_states.shape[2]
    all_positions = torch.arange(kv_seq_len, device=key_states.device).unsqueeze(0)

    if hasattr(self, "rotary_emb"):
        cos_full, sin_full = self.rotary_emb(key_states, all_positions)
    else:
        cos_full, sin_full = get_rope_embeddings(
            self._nope_config, all_positions.squeeze(0), key_states.device
        )
    cos_full = cos_full.to(key_states.dtype)
    sin_full = sin_full.to(key_states.dtype)
    key_states_rope = apply_rope_key_only(key_states, cos_full, sin_full)

    # --- GQA expansion ---
    key_states_rope = _repeat_kv(key_states_rope, num_kv_groups)
    value_states_expanded = _repeat_kv(value_states, num_kv_groups)

    # --- Eager attention ---
    attn_weights = torch.matmul(
        query_states, key_states_rope.transpose(2, 3)
    ) / math.sqrt(head_dim)

    if attention_mask is not None:
        causal_mask = attention_mask
        if causal_mask.dim() == 4 and causal_mask.shape[-1] > kv_seq_len:
            causal_mask = causal_mask[:, :, :, :kv_seq_len]
        attn_weights = attn_weights + causal_mask

    attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32).to(
        query_states.dtype
    )
    attn_output = torch.matmul(attn_weights, value_states_expanded)

    attn_output = attn_output.transpose(1, 2).contiguous().reshape(bsz, q_len, -1)
    attn_output = self.o_proj(attn_output)

    if not output_attentions:
        attn_weights = None

    return attn_output, attn_weights


def patch_model_for_nope(model):
    """Patch all attention layers to use NoPE KV storage with Q-only RoPE.

    Must be called before any forward pass. Use unpatch_model() to restore.
    """
    model_id = id(model)
    if model_id in _PATCHED_MODELS:
        return

    originals = {}
    config = model.config

    if hasattr(model, "model") and hasattr(model.model, "layers"):
        layers = model.model.layers
    elif hasattr(model, "layers"):
        layers = model.layers
    else:
        raise ValueError(
            "Unsupported model architecture: expected .model.layers or .layers"
        )

    for i, layer in enumerate(layers):
        attn = layer.self_attn
        originals[i] = attn.forward
        attn._nope_config = config
        attn.forward = types.MethodType(_nope_forward, attn)

    if hasattr(config, "_attn_implementation"):
        originals["_attn_implementation"] = config._attn_implementation
        config._attn_implementation = "eager"

    _PATCHED_MODELS[model_id] = originals


def unpatch_model(model):
    """Restore original attention forward methods."""
    model_id = id(model)
    if model_id not in _PATCHED_MODELS:
        return

    originals = _PATCHED_MODELS[model_id]

    if hasattr(model, "model") and hasattr(model.model, "layers"):
        layers = model.model.layers
    elif hasattr(model, "layers"):
        layers = model.layers
    else:
        return

    for i, layer in enumerate(layers):
        if i in originals:
            layer.self_attn.forward = originals[i]
            if hasattr(layer.self_attn, "_nope_config"):
                delattr(layer.self_attn, "_nope_config")

    if "_attn_implementation" in originals:
        model.config._attn_implementation = originals["_attn_implementation"]

    del _PATCHED_MODELS[model_id]
