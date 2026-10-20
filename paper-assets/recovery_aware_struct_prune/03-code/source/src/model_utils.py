import logging
import os

import torch
import torch.nn as nn
from transformers import AutoConfig, AutoModelForCausalLM

logger = logging.getLogger(__name__)


def _load_state_dict(model_path):
    safetensor_files = sorted(
        f for f in os.listdir(model_path) if f.endswith(".safetensors")
    )
    if safetensor_files:
        from safetensors.torch import load_file
        state_dict = {}
        for f in safetensor_files:
            state_dict.update(load_file(os.path.join(model_path, f)))
        return state_dict
    return torch.load(
        os.path.join(model_path, "pytorch_model.bin"),
        map_location="cpu", weights_only=True,
    )


def load_pruned_model(model_path, device_map="auto", torch_dtype=torch.bfloat16):
    """Load a pruned model that may have non-uniform MLP/attention dimensions per layer."""
    config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
    per_layer_sizes = getattr(config, "per_layer_intermediate_size", None)
    per_layer_heads = getattr(config, "per_layer_num_attention_heads", None) or getattr(config, "per_layer_num_heads", None)
    per_layer_kv_heads = getattr(config, "per_layer_num_key_value_heads", None) or getattr(config, "per_layer_num_kv_heads", None)

    if per_layer_sizes is None and per_layer_heads is None:
        return AutoModelForCausalLM.from_pretrained(
            model_path, torch_dtype=torch_dtype, device_map=device_map,
            trust_remote_code=True,
        )

    hidden_size = config.hidden_size

    if per_layer_sizes is not None:
        max_size = max(per_layer_sizes)
        config.intermediate_size = max_size
        logger.info(
            "Non-uniform MLP detected: intermediate_size range [%d, %d]",
            min(per_layer_sizes), max_size,
        )

    if per_layer_heads is not None:
        config.num_attention_heads = max(per_layer_heads)
        config.num_key_value_heads = max(per_layer_kv_heads)
        logger.info(
            "Non-uniform attention detected: heads range [%d, %d], kv_heads range [%d, %d]",
            min(per_layer_heads), max(per_layer_heads),
            min(per_layer_kv_heads), max(per_layer_kv_heads),
        )

    head_dim = getattr(config, "head_dim", hidden_size // config.num_attention_heads)

    prev_dtype = torch.get_default_dtype()
    torch.set_default_dtype(torch_dtype)
    try:
        model = AutoModelForCausalLM.from_config(config)
        num_layers = len(model.model.layers)

        for layer_idx in range(num_layers):
            layer = model.model.layers[layer_idx]

            if per_layer_sizes is not None:
                size = per_layer_sizes[layer_idx]
                if size != config.intermediate_size:
                    mlp = layer.mlp
                    mlp.gate_proj = nn.Linear(hidden_size, size, bias=False)
                    mlp.up_proj = nn.Linear(hidden_size, size, bias=False)
                    mlp.down_proj = nn.Linear(size, hidden_size, bias=False)

            if per_layer_heads is not None:
                nh = per_layer_heads[layer_idx]
                nkv = per_layer_kv_heads[layer_idx]
                if nh != config.num_attention_heads or nkv != config.num_key_value_heads:
                    attn = layer.self_attn
                    q_out = nh * head_dim
                    kv_out = nkv * head_dim
                    attn.q_proj = nn.Linear(hidden_size, q_out, bias=getattr(attn.q_proj, 'bias', None) is not None)
                    attn.k_proj = nn.Linear(hidden_size, kv_out, bias=getattr(attn.k_proj, 'bias', None) is not None)
                    attn.v_proj = nn.Linear(hidden_size, kv_out, bias=getattr(attn.v_proj, 'bias', None) is not None)
                    attn.o_proj = nn.Linear(q_out, hidden_size, bias=getattr(attn.o_proj, 'bias', None) is not None)
                    attn.num_heads = nh
                    attn.num_key_value_heads = nkv
                    attn.num_key_value_groups = max(1, nh // max(1, nkv))
                    attn.head_dim = head_dim
    finally:
        torch.set_default_dtype(prev_dtype)

    state_dict = _load_state_dict(model_path)
    model.load_state_dict(state_dict, strict=True)
    del state_dict

    if device_map == "auto":
        model = model.cuda()
    elif device_map is not None and str(device_map) != "cpu":
        model = model.to(device_map)

    model.eval()
    return model
