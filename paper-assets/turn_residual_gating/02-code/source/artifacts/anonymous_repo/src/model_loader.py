import os

import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForCausalLM

from threadgate import TurnEmbedding, GateNetwork, UniformGateNetwork
from turn_utils import build_turn_features
from config import MODEL_NAME


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


def _find_layers(model):
    return _find_hf_model(model).model.layers


def load_gates(checkpoint_dir, gate_type, hidden_dim, num_layers):
    if gate_type == "threadgate":
        turn_embedding = TurnEmbedding()
        gates = nn.ModuleList([
            GateNetwork(hidden_dim, turn_embedding, init_bias=5.0)
            for _ in range(num_layers)
        ])
    else:
        turn_embedding = None
        gates = nn.ModuleList([
            UniformGateNetwork(hidden_dim, init_bias=5.0)
            for _ in range(num_layers)
        ])

    gate_path = os.path.join(checkpoint_dir, "gate_params.pt")
    if not os.path.exists(gate_path):
        raise FileNotFoundError(f"Gate parameters not found: {gate_path}")
    gate_state = torch.load(gate_path, map_location="cpu", weights_only=True)
    gates.load_state_dict(gate_state["gates"])
    if gate_type == "threadgate" and "turn_embedding" in gate_state:
        turn_embedding.load_state_dict(gate_state["turn_embedding"])

    return gates, turn_embedding


class TurnFeaturesTracker:

    def __init__(self, num_layers):
        self.num_layers = num_layers
        self.full_td = None
        self.full_ti = None
        self._pos = 0

    def prepare(self, input_ids, tokenizer, max_new_tokens, device):
        ids = input_ids.squeeze(0) if input_ids.dim() > 1 else input_ids
        tf = build_turn_features(ids, tokenizer)

        last_td = tf["turn_distance"][-1].item()
        last_ti = tf["turn_index"][-1].item()
        extra_td = torch.arange(
            last_td + 1, last_td + 1 + max_new_tokens, dtype=torch.long
        )
        extra_ti = torch.full((max_new_tokens,), last_ti, dtype=torch.long)

        self.full_td = torch.cat([tf["turn_distance"], extra_td]).to(device)
        self.full_ti = torch.cat([tf["turn_index"], extra_ti]).to(device)
        self._pos = 0

    def get_features(self, seq_len, layer_idx):
        pos = self._pos
        if seq_len > 1:
            features = {
                "turn_distance": self.full_td[:seq_len],
                "turn_index": self.full_ti[:seq_len],
            }
            if layer_idx == self.num_layers - 1:
                self._pos = seq_len
        else:
            features = {
                "turn_distance": self.full_td[pos:pos + 1],
                "turn_index": self.full_ti[pos:pos + 1],
            }
            if layer_idx == self.num_layers - 1:
                self._pos = pos + 1
        return features


class GateContext:

    def __init__(self, hooks, gate_type, tracker=None, turn_features_ref=None,
                 gate_values=None):
        self.hooks = hooks
        self.gate_type = gate_type
        self.tracker = tracker
        self.turn_features_ref = turn_features_ref
        self.gate_values = gate_values or {}

    def prepare_generation(self, input_ids, tokenizer, max_new_tokens, device):
        if self.tracker is not None:
            self.tracker.prepare(input_ids, tokenizer, max_new_tokens, device)

    def set_turn_features(self, turn_features):
        if self.turn_features_ref is not None:
            self.turn_features_ref[0] = turn_features

    def cleanup(self):
        for h in self.hooks:
            h.remove()
        self.hooks = []


def _register_eval_hooks(model, gates, gate_type, turn_embedding=None):
    layers = _find_layers(model)
    hooks = []
    turn_features_ref = [None]
    gate_values = {}

    for i, layer in enumerate(layers):
        device = next(layer.parameters()).device
        gates[i].to(device=device, dtype=torch.bfloat16)
    if gate_type == "threadgate" and turn_embedding is not None:
        device0 = next(layers[0].parameters()).device
        turn_embedding.to(device=device0, dtype=torch.bfloat16)

    if gate_type == "threadgate":
        def make_hook(layer_idx):
            def hook(module, input, output):
                tf = turn_features_ref[0]
                if tf is None:
                    return output
                layer_input = input[0]
                layer_output = output[0] if isinstance(output, tuple) else output
                g = gates[layer_idx](layer_input, tf)
                f_x = layer_output - layer_input
                gated = layer_input + g * f_x
                gate_values[layer_idx] = g.detach()
                if isinstance(output, tuple):
                    return (gated,) + output[1:]
                return gated
            return hook
    else:
        def make_hook(layer_idx):
            def hook(module, input, output):
                layer_input = input[0]
                layer_output = output[0] if isinstance(output, tuple) else output
                g = gates[layer_idx](layer_input)
                f_x = layer_output - layer_input
                gated = layer_input + g * f_x
                gate_values[layer_idx] = g.detach()
                if isinstance(output, tuple):
                    return (gated,) + output[1:]
                return gated
            return hook

    for i, layer in enumerate(layers):
        hooks.append(layer.register_forward_hook(make_hook(i)))

    return hooks, turn_features_ref, gate_values


def _register_generation_hooks(model, gates, gate_type, turn_embedding=None):
    layers = _find_layers(model)
    num_layers = len(layers)
    hooks = []
    gate_values = {}

    for i, layer in enumerate(layers):
        device = next(layer.parameters()).device
        gates[i].to(device=device, dtype=torch.bfloat16)
    if gate_type == "threadgate" and turn_embedding is not None:
        device0 = next(layers[0].parameters()).device
        turn_embedding.to(device=device0, dtype=torch.bfloat16)

    if gate_type == "threadgate":
        tracker = TurnFeaturesTracker(num_layers)

        def make_hook(layer_idx):
            def hook(module, input, output):
                if tracker.full_td is None:
                    return output
                layer_input = input[0]
                layer_output = output[0] if isinstance(output, tuple) else output
                tf = tracker.get_features(layer_input.shape[1], layer_idx)
                g = gates[layer_idx](layer_input, tf)
                f_x = layer_output - layer_input
                gated = layer_input + g * f_x
                gate_values[layer_idx] = g.detach()
                if isinstance(output, tuple):
                    return (gated,) + output[1:]
                return gated
            return hook
    else:
        tracker = None

        def make_hook(layer_idx):
            def hook(module, input, output):
                layer_input = input[0]
                layer_output = output[0] if isinstance(output, tuple) else output
                g = gates[layer_idx](layer_input)
                f_x = layer_output - layer_input
                gated = layer_input + g * f_x
                gate_values[layer_idx] = g.detach()
                if isinstance(output, tuple):
                    return (gated,) + output[1:]
                return gated
            return hook

    for i, layer in enumerate(layers):
        hooks.append(layer.register_forward_hook(make_hook(i)))

    return hooks, tracker, gate_values


def load_model_with_gates(checkpoint_dir, gate_type, model_name=None,
                          device_map="auto"):
    if model_name is None:
        model_name = MODEL_NAME

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, device_map=device_map,
    )

    lora_path = os.path.join(checkpoint_dir, "lora")
    if os.path.isdir(lora_path):
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, lora_path)
    model.eval()

    if gate_type == "baseline":
        return model, tokenizer, GateContext([], "baseline")

    hf_model = _find_hf_model(model)
    hidden_dim = hf_model.config.hidden_size
    num_layers = hf_model.config.num_hidden_layers

    gates, turn_embedding = load_gates(
        checkpoint_dir, gate_type, hidden_dim, num_layers,
    )
    hooks, tracker, gate_values = _register_generation_hooks(
        model, gates, gate_type, turn_embedding,
    )

    return model, tokenizer, GateContext(
        hooks, gate_type, tracker=tracker, gate_values=gate_values,
    )
