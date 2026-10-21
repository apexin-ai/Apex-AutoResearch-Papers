import warnings
from contextlib import contextmanager

import torch
import torch.nn.functional as F
import numpy as np


class GARMeasurer:
    def __init__(self, model, measure_only=True):
        self.model = model
        self.measure_only = measure_only
        self._hooks = []
        self._attention_weights = {}
        self._active = False

        self._attn_layers = []
        for i, layer in enumerate(model.model.layers):
            self._attn_layers.append((i, layer.self_attn))
        self.num_layers = len(self._attn_layers)

        attn_impl = getattr(model.config, "_attn_implementation", None)
        if attn_impl and attn_impl != "eager":
            warnings.warn(
                f"attn_implementation={attn_impl!r} does not return attention weights. "
                f"Load model with attn_implementation='eager' for GAR measurement.",
                stacklevel=2,
            )

    def _make_hook(self, layer_idx):
        def hook_fn(module, input, output):
            if isinstance(output, tuple) and len(output) > 1 and output[1] is not None:
                attn_w = output[1]
                if self.measure_only:
                    attn_w = attn_w.detach().float()
                else:
                    attn_w = attn_w.float()
                self._attention_weights[layer_idx] = attn_w
        return hook_fn

    @contextmanager
    def measure(self):
        """Caller must pass output_attentions=True to model.forward() inside this context."""
        self._attention_weights = {}
        self._hooks = []
        self._active = True

        try:
            for layer_idx, attn_module in self._attn_layers:
                h = attn_module.register_forward_hook(self._make_hook(layer_idx))
                self._hooks.append(h)
            yield self
        finally:
            for h in self._hooks:
                h.remove()
            self._hooks = []
            self._active = False

    def compute_gar(self, goal_positions, query_positions):
        if not self._attention_weights:
            raise RuntimeError("No attention data collected. Run model forward inside measure() context with output_attentions=True.")

        if not goal_positions or not query_positions:
            return {
                "gar_per_query": [],
                "gar_per_layer": np.zeros((self.num_layers, 0)),
                "gar_per_head": np.zeros((self.num_layers, 0, 0)),
                "mean_gar": 0.0,
            }

        goal_idx = torch.tensor(goal_positions, dtype=torch.long)
        query_idx = torch.tensor(query_positions, dtype=torch.long)
        num_queries = len(query_positions)

        sorted_layers = sorted(self._attention_weights.keys())
        num_layers = len(sorted_layers)

        first_weights = self._attention_weights[sorted_layers[0]]
        num_heads = first_weights.shape[1]

        gar_per_head = np.zeros((num_layers, num_heads, num_queries))

        for li, layer_idx in enumerate(sorted_layers):
            attn_w = self._attention_weights[layer_idx]
            w = attn_w[0]

            goal_attn = w[:, query_idx, :][:, :, goal_idx]
            gar_values = goal_attn.sum(dim=-1)

            gar_per_head[li] = gar_values.detach().cpu().numpy()

            if self.measure_only:
                self._attention_weights[layer_idx] = None

        gar_per_layer = gar_per_head.mean(axis=1)
        gar_per_query = gar_per_layer.mean(axis=0).tolist()
        mean_gar = float(np.mean(gar_per_query)) if gar_per_query else 0.0

        return {
            "gar_per_query": gar_per_query,
            "gar_per_layer": gar_per_layer,
            "gar_per_head": gar_per_head,
            "mean_gar": mean_gar,
        }

    def compute_gar_differentiable(self, goal_positions, query_positions):
        if not self._attention_weights:
            raise RuntimeError("No attention data collected.")

        if self.measure_only:
            raise RuntimeError("measure_only=True, cannot compute differentiable GAR. Set measure_only=False.")

        if not goal_positions or not query_positions:
            return torch.tensor(0.0, requires_grad=True)

        goal_idx = torch.tensor(goal_positions, dtype=torch.long)
        query_idx = torch.tensor(query_positions, dtype=torch.long)

        sorted_layers = sorted(k for k, v in self._attention_weights.items() if v is not None)
        all_gar = []

        for layer_idx in sorted_layers:
            attn_w = self._attention_weights[layer_idx]
            w = attn_w[0]
            goal_attn = w[:, query_idx, :][:, :, goal_idx]
            gar_layer = goal_attn.sum(dim=-1).mean()
            all_gar.append(gar_layer)

        return torch.stack(all_gar).mean()


def compute_gar_loss(gar_per_turn, epsilon=0.02, mode="pairwise", target=0.3):
    if len(gar_per_turn) < 2:
        if isinstance(gar_per_turn[0], torch.Tensor):
            return torch.tensor(0.0, device=gar_per_turn[0].device, requires_grad=True)
        return torch.tensor(0.0, requires_grad=True)

    if mode == "pairwise":
        loss = torch.tensor(0.0)
        if isinstance(gar_per_turn[0], torch.Tensor):
            loss = torch.tensor(0.0, device=gar_per_turn[0].device)

        for i in range(1, len(gar_per_turn)):
            prev = gar_per_turn[i - 1]
            curr = gar_per_turn[i]
            if not isinstance(prev, torch.Tensor):
                prev = torch.tensor(prev, dtype=torch.float32)
            if not isinstance(curr, torch.Tensor):
                curr = torch.tensor(curr, dtype=torch.float32)
            drop = prev - curr - epsilon
            loss = loss + F.relu(drop)

        return loss

    elif mode == "cumulative":
        first = gar_per_turn[0]
        if not isinstance(first, torch.Tensor):
            first = torch.tensor(first, dtype=torch.float32)
        loss = torch.tensor(0.0, device=first.device)

        for i in range(1, len(gar_per_turn)):
            curr = gar_per_turn[i]
            if not isinstance(curr, torch.Tensor):
                curr = torch.tensor(curr, dtype=torch.float32)
            drop = first - curr - epsilon
            loss = loss + F.relu(drop)

        return loss

    elif mode == "maximize":
        all_gar = []
        for g in gar_per_turn:
            if not isinstance(g, torch.Tensor):
                g = torch.tensor(g, dtype=torch.float32)
            all_gar.append(g)
        return -torch.stack(all_gar).mean()

    elif mode == "hinge_target":
        all_gar = []
        for g in gar_per_turn:
            if not isinstance(g, torch.Tensor):
                g = torch.tensor(g, dtype=torch.float32)
            all_gar.append(g)
        mean_gar = torch.stack(all_gar).mean()
        return F.relu(target - mean_gar)

    elif mode == "smooth_saturation":
        all_gar = []
        for g in gar_per_turn:
            if not isinstance(g, torch.Tensor):
                g = torch.tensor(g, dtype=torch.float32)
            all_gar.append(g)
        mean_gar = torch.stack(all_gar).mean()
        return -target * torch.tanh(mean_gar / target)

    elif mode == "mse_target":
        # Bidirectional MSE loss: penalizes GAR both above and below target
        all_gar = []
        for g in gar_per_turn:
            if not isinstance(g, torch.Tensor):
                g = torch.tensor(g, dtype=torch.float32)
            all_gar.append(g)
        mean_gar = torch.stack(all_gar).mean()
        return (mean_gar - target) ** 2

    else:
        raise ValueError(f"Unknown mode: {mode}")
