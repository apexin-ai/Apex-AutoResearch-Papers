"""Inference-time attention steering via pre-softmax bias injection.

Patches self_attn.forward on transformer layers to add scalar bias beta
to goal-token columns of the 4D attention mask, boosting pre-softmax
QK^T logits toward goal positions.

Requires eager attention (attn_implementation="eager") so the mask is
applied as additive bias in the explicit QK^T + mask + softmax path.
"""

import torch


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


class AttentionSteering:

    def __init__(self, model, beta, goal_positions, layer_range=None):
        self.model = model
        self.beta = beta
        self.goal_positions = list(goal_positions) if goal_positions else []
        self.layer_range = layer_range
        self._original_forwards = {}
        self._active = False

    def activate(self):
        if self._active:
            return
        hf_model = _find_hf_model(self.model)
        layers = hf_model.model.layers
        for i, layer in enumerate(layers):
            if self.layer_range is not None:
                if not (self.layer_range[0] <= i < self.layer_range[1]):
                    continue
            attn = layer.self_attn
            self._original_forwards[i] = attn.forward
            attn.forward = self._make_patched_forward(i)
        self._active = True

    def _make_patched_forward(self, layer_idx):
        original_forward = self._original_forwards[layer_idx]
        steering = self

        def patched_forward(*args, **kwargs):
            mask = kwargs.get("attention_mask", None)
            if mask is not None and steering.goal_positions and steering.beta != 0:
                kv_len = mask.shape[-1]
                valid = [p for p in steering.goal_positions if p < kv_len]
                if valid:
                    idx = torch.tensor(valid, device=mask.device, dtype=torch.long)
                    mask = mask.clone()
                    mask[:, :, :, idx] = mask[:, :, :, idx] + steering.beta
                    kwargs["attention_mask"] = mask
            return original_forward(*args, **kwargs)

        return patched_forward

    def deactivate(self):
        if not self._active:
            return
        hf_model = _find_hf_model(self.model)
        layers = hf_model.model.layers
        for i, original in self._original_forwards.items():
            layers[i].self_attn.forward = original
        self._original_forwards.clear()
        self._active = False

    def update_goal_positions(self, positions):
        self.goal_positions = list(positions) if positions else []

    def __del__(self):
        if self._active:
            self.deactivate()
