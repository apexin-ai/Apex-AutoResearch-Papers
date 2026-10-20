"""Post-softmax attention weight rescaling (split-softmax).

Li et al. (2024), "System-Level Natural Language Feedback", arXiv:2402.10962.
Rescales post-softmax attention weights to amplify system prompt attention.

k=1.0 is identity (no effect). k->0 is maximum amplification.
Training-free, inference-time only.

Requires attn_implementation="eager".
"""

import torch
import torch.nn as nn


def _find_hf_model(model):
    if hasattr(model, "model") and hasattr(model.model, "layers"):
        return model
    try:
        inner = model.base_model.model
        if hasattr(inner, "model") and hasattr(inner.model, "layers"):
            return inner
    except AttributeError:
        pass
    raise ValueError("Cannot find HF model with .model.layers")


def _get_model_module(model_type):
    if model_type == "qwen2":
        import transformers.models.qwen2.modeling_qwen2 as mod
        return mod
    elif model_type == "llama":
        import transformers.models.llama.modeling_llama as mod
        return mod
    raise ValueError(
        f"SplitSoftmax: unsupported model type '{model_type}'. "
        "Supported: qwen2, llama."
    )


def get_system_prompt_token_len(tokenizer, messages):
    sys_content = None
    for msg in messages:
        if msg["role"] == "system":
            sys_content = msg["content"]
            break
    if sys_content is None:
        return 0
    sys_messages = [{"role": "system", "content": sys_content}]
    sys_text = tokenizer.apply_chat_template(
        sys_messages, tokenize=False, add_generation_prompt=False,
    )
    return len(tokenizer(sys_text, return_tensors="pt").input_ids.squeeze(0))


class SplitSoftmax:

    def __init__(self, model, k=0.5):
        self.model = model
        self.k = k
        self._system_prompt_len = 0
        self._original_eager_fn = None
        self._model_module = None
        self._active = False

    def activate(self, system_prompt_len):
        if self._active:
            self.deactivate()
        self._system_prompt_len = system_prompt_len

        hf_model = _find_hf_model(self.model)
        mod = _get_model_module(hf_model.config.model_type)
        self._model_module = mod
        self._original_eager_fn = mod.eager_attention_forward

        steering = self
        repeat_kv_fn = mod.repeat_kv

        def split_softmax_eager_forward(
            module, query, key, value, attention_mask, scaling, dropout=0.0, **kwargs
        ):
            key_states = repeat_kv_fn(key, module.num_key_value_groups)
            value_states = repeat_kv_fn(value, module.num_key_value_groups)

            attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling
            if attention_mask is not None:
                attn_weights = attn_weights + attention_mask

            attn_weights = nn.functional.softmax(
                attn_weights, dim=-1, dtype=torch.float32
            ).to(query.dtype)

            sp_len = steering._system_prompt_len
            k = steering.k
            if sp_len > 0 and k != 1.0:
                pi = attn_weights[:, :, :, :sp_len].sum(dim=-1, keepdim=True)
                pi_f32 = pi.float().clamp(min=1e-8, max=1 - 1e-6)
                sp_scale = ((pi_f32 ** k) / pi_f32).to(attn_weights.dtype)
                conv_scale = ((1 - pi_f32 ** k) / (1 - pi_f32)).to(attn_weights.dtype)
                attn_weights = attn_weights.clone()
                attn_weights[:, :, :, :sp_len] *= sp_scale
                attn_weights[:, :, :, sp_len:] *= conv_scale

            attn_weights = nn.functional.dropout(
                attn_weights, p=dropout, training=module.training
            )
            attn_output = torch.matmul(attn_weights, value_states)
            attn_output = attn_output.transpose(1, 2).contiguous()
            return attn_output, attn_weights

        mod.eager_attention_forward = split_softmax_eager_forward
        self._active = True

    def deactivate(self):
        if not self._active:
            return
        self._model_module.eager_attention_forward = self._original_eager_fn
        self._original_eager_fn = None
        self._model_module = None
        self._active = False

    def update_system_prompt_len(self, sp_len):
        self._system_prompt_len = sp_len

    def __del__(self):
        if self._active:
            self.deactivate()
