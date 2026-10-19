"""
Model setup for TBAB multi-turn training.

Handles:
- Loading Mistral-7B-Instruct-v0.1 with bf16
- Registering bridge tokens (expanding embedding + lm_head)
- Applying LoRA with optional trainable_token_indices for bridge tokens
- Freezing base embeddings so only bridge token rows are trainable

Dependencies: transformers, peft, torch
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model


BRIDGE_TOKEN_PREFIX = "<bridge_{i}>"


def load_tokenizer(model_name_or_path: str, cache_dir: str = None) -> AutoTokenizer:
    tokenizer = AutoTokenizer.from_pretrained(
        model_name_or_path,
        cache_dir=cache_dir,
        trust_remote_code=True,
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    return tokenizer


def add_bridge_tokens(tokenizer: AutoTokenizer, num_bridge: int) -> list:
    """Add bridge tokens to tokenizer vocabulary.

    Returns list of bridge token IDs in order [bridge_0, bridge_1, ..., bridge_{K-1}].
    """
    bridge_tokens = [f"<bridge_{i}>" for i in range(num_bridge)]
    tokenizer.add_tokens(bridge_tokens, special_tokens=True)
    bridge_token_ids = [tokenizer.convert_tokens_to_ids(t) for t in bridge_tokens]
    return bridge_token_ids


def load_model(
    model_name_or_path: str,
    tokenizer: AutoTokenizer,
    bridge_token_ids: list = None,
    cache_dir: str = None,
) -> AutoModelForCausalLM:
    """Load model, resize embeddings for bridge tokens, init bridge embeddings."""
    model = AutoModelForCausalLM.from_pretrained(
        model_name_or_path,
        cache_dir=cache_dir,
        dtype=torch.bfloat16,
        attn_implementation="sdpa",
        trust_remote_code=True,
    )

    if bridge_token_ids:
        original_vocab_size = model.get_input_embeddings().weight.shape[0]
        model.resize_token_embeddings(len(tokenizer))

        with torch.no_grad():
            embed_weight = model.get_input_embeddings().weight
            vocab_mean = embed_weight[:original_vocab_size].mean(dim=0)
            for tid in bridge_token_ids:
                embed_weight[tid] = vocab_mean + torch.randn_like(vocab_mean) * 0.01

            lm_head_weight = model.lm_head.weight
            head_mean = lm_head_weight[:original_vocab_size].mean(dim=0)
            for tid in bridge_token_ids:
                lm_head_weight[tid] = head_mean + torch.randn_like(head_mean) * 0.01

    model.config.use_cache = False
    return model


def apply_lora(
    model: AutoModelForCausalLM,
    lora_r: int = 32,
    lora_alpha: int = 64,
    lora_dropout: float = 0.05,
    use_bridge_tokens: bool = False,
    bridge_token_ids: list = None,
) -> AutoModelForCausalLM:
    """Apply LoRA. If bridge tokens are used, mark their embedding indices as trainable."""
    lora_config = LoraConfig(
        r=lora_r,
        lora_alpha=lora_alpha,
        target_modules="all-linear",
        lora_dropout=lora_dropout,
        task_type="CAUSAL_LM",
    )

    model = get_peft_model(model, lora_config)

    if use_bridge_tokens and bridge_token_ids:
        _make_bridge_embeddings_trainable(model, bridge_token_ids)

    return model


def _make_bridge_embeddings_trainable(model, bridge_token_ids: list):
    """Freeze all embedding rows except bridge tokens.

    After LoRA wrapping, the base model embeddings are frozen by default.
    We selectively enable gradients for bridge token rows by using a
    forward hook that zeroes out gradients for non-bridge rows.
    """
    base_model = model.get_base_model()
    embed = base_model.get_input_embeddings()
    embed.weight.requires_grad = True

    lm_head = base_model.lm_head
    lm_head.weight.requires_grad = True

    bridge_set = set(bridge_token_ids)
    vocab_size = embed.weight.shape[0]

    grad_mask = torch.zeros(vocab_size, 1, device=embed.weight.device, dtype=embed.weight.dtype)
    for tid in bridge_set:
        grad_mask[tid] = 1.0

    def _zero_non_bridge_grad_embed(grad):
        return grad * grad_mask.to(grad.device, grad.dtype)

    def _zero_non_bridge_grad_head(grad):
        return grad * grad_mask.to(grad.device, grad.dtype)

    embed.weight.register_hook(_zero_non_bridge_grad_embed)
    lm_head.weight.register_hook(_zero_non_bridge_grad_head)


def setup_model_and_tokenizer(config: dict):
    """High-level setup: load tokenizer, add bridge tokens, load model, apply LoRA.

    Args:
        config: dict with keys from YAML config file

    Returns:
        (model, tokenizer, bridge_token_ids)
        bridge_token_ids is empty list if use_bridge_tokens=False
    """
    model_path = config["model_name_or_path"]
    cache_dir = config.get("cache_dir", None)
    use_bridge = config.get("use_bridge_tokens", False)
    num_bridge = config.get("num_bridge_tokens", 4)

    tokenizer = load_tokenizer(model_path, cache_dir=cache_dir)

    bridge_token_ids = []
    if use_bridge:
        bridge_token_ids = add_bridge_tokens(tokenizer, num_bridge)

    model = load_model(model_path, tokenizer, bridge_token_ids if use_bridge else None, cache_dir=cache_dir)

    model = apply_lora(
        model,
        lora_r=config.get("lora_r", 32),
        lora_alpha=config.get("lora_alpha", 64),
        lora_dropout=config.get("lora_dropout", 0.05),
        use_bridge_tokens=use_bridge,
        bridge_token_ids=bridge_token_ids if use_bridge else None,
    )

    return model, tokenizer, bridge_token_ids
