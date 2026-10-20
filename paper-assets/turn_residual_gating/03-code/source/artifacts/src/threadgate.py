import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer

from config import (
    MODEL_NAME,
    LORA_RANK,
    GATE_HIDDEN_DIM,
    MAX_TURN_DISTANCE,
    TURN_EMBED_DIM,
)


class TurnEmbedding(nn.Module):

    def __init__(self):
        super().__init__()
        half_dim = TURN_EMBED_DIM // 2
        num_buckets = MAX_TURN_DISTANCE + 1
        self.distance_embed = nn.Embedding(num_buckets, half_dim)
        self.index_embed = nn.Embedding(num_buckets, half_dim)

    def forward(self, turn_distance, turn_index):
        td = turn_distance.clamp(0, MAX_TURN_DISTANCE)
        ti = turn_index.clamp(0, MAX_TURN_DISTANCE)
        return torch.cat([self.distance_embed(td), self.index_embed(ti)], dim=-1)


class GateNetwork(nn.Module):

    def __init__(self, hidden_dim, turn_embedding, init_bias=5.0):
        super().__init__()
        self.down_proj = nn.Linear(hidden_dim, LORA_RANK, bias=False)
        self.turn_embedding = turn_embedding
        self.fc1 = nn.Linear(LORA_RANK + TURN_EMBED_DIM, GATE_HIDDEN_DIM)
        self.fc2 = nn.Linear(GATE_HIDDEN_DIM, 1)
        self.fc2.bias.data.fill_(init_bias)

    def forward(self, hidden_state, turn_features):
        down = self.down_proj(hidden_state)
        turn_emb = self.turn_embedding(
            turn_features["turn_distance"],
            turn_features["turn_index"],
        )
        while turn_emb.dim() < down.dim():
            turn_emb = turn_emb.unsqueeze(0)
        if turn_emb.shape[0] == 1 and down.shape[0] > 1:
            turn_emb = turn_emb.expand(down.shape[0], -1, -1)
        combined = torch.cat([down, turn_emb], dim=-1)
        return torch.sigmoid(self.fc2(torch.relu(self.fc1(combined))))


class UniformGateNetwork(nn.Module):

    def __init__(self, hidden_dim, init_bias=5.0):
        super().__init__()
        self.down_proj = nn.Linear(hidden_dim, LORA_RANK, bias=False)
        self.constant_vector = nn.Parameter(torch.zeros(TURN_EMBED_DIM))
        self.fc1 = nn.Linear(LORA_RANK + TURN_EMBED_DIM, GATE_HIDDEN_DIM)
        self.fc2 = nn.Linear(GATE_HIDDEN_DIM, 1)
        self.fc2.bias.data.fill_(init_bias)

    def forward(self, hidden_state):
        h = self.down_proj(hidden_state)
        c = self.constant_vector.unsqueeze(0).unsqueeze(0).expand(
            hidden_state.size(0), hidden_state.size(1), -1
        )
        combined = torch.cat([h, c], dim=-1)
        return torch.sigmoid(self.fc2(torch.relu(self.fc1(combined))))


class ThreadGatedModel(nn.Module):

    def __init__(self, model_name=MODEL_NAME, gate_type="threadgate", init_bias=2.0, device_map="auto"):
        super().__init__()
        self.gate_type = gate_type

        self.base_model = AutoModelForCausalLM.from_pretrained(
            model_name, torch_dtype=torch.bfloat16, device_map=device_map,
        )
        for param in self.base_model.parameters():
            param.requires_grad = False

        hidden_dim = self.base_model.config.hidden_size
        num_layers = self.base_model.config.num_hidden_layers
        self.num_layers = num_layers

        if gate_type == "none":
            self.gates = None
        elif gate_type == "threadgate":
            self.turn_embedding = TurnEmbedding()
            self.gates = nn.ModuleList([
                GateNetwork(hidden_dim, self.turn_embedding, init_bias)
                for _ in range(num_layers)
            ])
        else:
            self.gates = nn.ModuleList([
                UniformGateNetwork(hidden_dim, init_bias)
                for _ in range(num_layers)
            ])

        if self.gates is not None:
            for i, layer in enumerate(self.base_model.model.layers):
                device = next(layer.parameters()).device
                self.gates[i].to(device=device, dtype=torch.bfloat16)
            if gate_type == "threadgate":
                device = next(self.gates[0].parameters()).device
                self.turn_embedding.to(device=device, dtype=torch.bfloat16)

        self._gate_values = {}
        self._gate_values_with_grad = {}
        self._current_turn_features = None

        self._hooks = []
        if self.gate_type != "none":
            for i, layer in enumerate(self.base_model.model.layers):
                self._hooks.append(layer.register_forward_hook(self._make_hook(i)))

    def _make_hook(self, layer_idx):
        def hook(module, input, output):
            layer_input = input[0]

            if isinstance(output, tuple):
                layer_output = output[0]
            else:
                layer_output = output

            if self.gate_type == "threadgate":
                gate = self.gates[layer_idx](layer_input, self._current_turn_features)
            else:
                gate = self.gates[layer_idx](layer_input)

            f_x = layer_output - layer_input
            gated = layer_input + gate * f_x
            self._gate_values[layer_idx] = gate.detach()
            self._gate_values_with_grad[layer_idx] = gate

            if isinstance(output, tuple):
                return (gated,) + output[1:]
            return gated

        return hook

    def forward(self, input_ids, attention_mask=None, labels=None, turn_features=None, **kwargs):
        if self.gate_type == "threadgate" and turn_features is not None:
            device = next(self.gates[0].parameters()).device
            self._current_turn_features = {
                k: v.to(device) if isinstance(v, torch.Tensor) else v
                for k, v in turn_features.items()
            }
        else:
            self._current_turn_features = None

        outputs = self.base_model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels,
            **kwargs,
        )
        return outputs

    def get_gate_values(self, with_grad=False):
        if self.gate_type == "none":
            return {i: torch.tensor(1.0) for i in range(self.num_layers)}
        if with_grad:
            return dict(self._gate_values_with_grad)
        return dict(self._gate_values)

    def trainable_parameters(self):
        for name, param in self.named_parameters():
            if param.requires_grad:
                yield name, param

    def count_parameters(self):
        total = sum(p.numel() for p in self.parameters())
        trainable = sum(p.numel() for p in self.parameters() if p.requires_grad)
        ratio = trainable / total if total > 0 else 0.0
        return total, trainable, ratio


def create_model(gate_type="threadgate", init_bias=2.0, device_map="auto"):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = ThreadGatedModel(MODEL_NAME, gate_type, init_bias, device_map)
    return model, tokenizer
