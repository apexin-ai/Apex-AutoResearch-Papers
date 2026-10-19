"""
Collect frozen π₀ activations from LIBERO-Plus rollouts.

Registers forward hooks on PaliGemma LLM layers and Action Expert layers,
runs episodes under each perturbation type (or nominal), and saves per-layer
activations with 4 pooling strategies in fp16.

Usage:
    # Collect camera perturbation episodes
    python collect_activations.py \
        --checkpoint /path/to/pi0_base \
        --output_dir ./activations \
        --perturbation_type camera_viewpoints \
        --num_episodes 50 \
        --device cuda:0

    # Collect all perturbation types
    python collect_activations.py \
        --checkpoint /path/to/pi0_base \
        --output_dir ./activations \
        --perturbation_type all \
        --num_episodes 50

    # Collect nominal (no perturbation) baseline
    python collect_activations.py \
        --checkpoint /path/to/pi0_base \
        --output_dir ./activations \
        --perturbation_type nominal \
        --num_episodes 100

Dependencies:
    torch, safetensors, openpi (for model loading), libero
"""

import argparse
import logging
import os
from pathlib import Path
from typing import Any

import torch
import torch.nn as nn

from configs import (
    CLASS_6_TO_3_MAPPING,
    EXPERT_LAYER_TEMPLATE,
    EXPERT_LAYERS,
    PALIGEMMA_LAYER_TEMPLATE,
    PALIGEMMA_LAYERS,
    PERTURBATION_TYPES_6CLASS,
    POOLING_STRATEGIES,
)

log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Pooling helpers
# ---------------------------------------------------------------------------

def pool_activation(hidden_states: torch.Tensor, strategy: str) -> torch.Tensor:
    """Pool a (batch, seq_len, hidden_dim) tensor into (batch, D).

    Strategies:
        mean       — mean over seq_len → (batch, hidden_dim)
        first      — first token       → (batch, hidden_dim)
        last       — last token        → (batch, hidden_dim)
        first_last — concat first+last → (batch, hidden_dim*2)
    """
    if strategy == "mean":
        return hidden_states.mean(dim=1)
    elif strategy == "first":
        return hidden_states[:, 0]
    elif strategy == "last":
        return hidden_states[:, -1]
    elif strategy == "first_last":
        return torch.cat([hidden_states[:, 0], hidden_states[:, -1]], dim=-1)
    raise ValueError(f"Unknown pooling strategy: {strategy}")


# ---------------------------------------------------------------------------
# Hook manager
# ---------------------------------------------------------------------------

class ActivationCollector:
    """Registers hooks on specified layers and stores pooled activations."""

    def __init__(self, model: nn.Module):
        self.model = model
        self._hooks: list[torch.utils.hooks.RemovableHook] = []
        self._raw: dict[str, torch.Tensor] = {}  # layer_name -> last hidden_states

    def register_hooks(self) -> None:
        for i in PALIGEMMA_LAYERS:
            name = f"paligemma_layer_{i}"
            module_path = PALIGEMMA_LAYER_TEMPLATE.format(i=i)
            module = _get_submodule(self.model, module_path)
            self._hooks.append(
                module.register_forward_hook(self._make_hook(name))
            )
            log.info("Hooked %s -> %s", name, module_path)

        for i in EXPERT_LAYERS:
            name = f"expert_layer_{i}"
            module_path = EXPERT_LAYER_TEMPLATE.format(i=i)
            module = _get_submodule(self.model, module_path)
            self._hooks.append(
                module.register_forward_hook(self._make_hook(name))
            )
            log.info("Hooked %s -> %s", name, module_path)

    def _make_hook(self, name: str):
        def hook_fn(_module, _input, output):
            # Gemma layers return (hidden_states, ...) or just hidden_states
            if isinstance(output, tuple):
                h = output[0]
            else:
                h = output
            self._raw[name] = h.detach()
        return hook_fn

    def get_pooled(self) -> dict[str, dict[str, torch.Tensor]]:
        """Return {layer_name: {pooling_strategy: tensor(fp16)}} from last forward."""
        result = {}
        for name, h in self._raw.items():
            result[name] = {}
            for strat in POOLING_STRATEGIES:
                pooled = pool_activation(h, strat)
                result[name][strat] = pooled.half().cpu()
        return result

    def clear(self) -> None:
        self._raw.clear()

    def remove_hooks(self) -> None:
        for h in self._hooks:
            h.remove()
        self._hooks.clear()


def _get_submodule(model: nn.Module, path: str) -> nn.Module:
    parts = path.split(".")
    m = model
    for p in parts:
        if p.isdigit():
            m = m[int(p)]
        else:
            m = getattr(m, p)
    return m


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_pi0_model(checkpoint_path: str, device: str) -> nn.Module:
    """Load frozen π₀ PyTorch model from checkpoint directory."""
    from safetensors.torch import load_model

    # Attempt openpi loader
    try:
        from openpi.models_pytorch.pi0_pytorch import PI0Pytorch
        from openpi.models_pytorch.model_config import get_model_config
    except ImportError:
        raise ImportError(
            "openpi package required. Install from the openpi repo or "
            "adjust the import path for your setup."
        )

    ckpt_path = Path(checkpoint_path)
    config = get_model_config("pi0_base")
    model = PI0Pytorch(config)

    # Load safetensors weights
    safetensors_files = list(ckpt_path.glob("*.safetensors"))
    if not safetensors_files:
        raise FileNotFoundError(f"No .safetensors files in {ckpt_path}")
    for sf in safetensors_files:
        load_model(model, str(sf), strict=False)
        log.info("Loaded weights from %s", sf.name)

    model = model.to(device)
    model.eval()
    for p in model.parameters():
        p.requires_grad_(False)
    log.info("Model loaded and frozen on %s", device)
    return model


# ---------------------------------------------------------------------------
# LIBERO-Plus episode rollout (stub — adapt to your LIBERO integration)
# ---------------------------------------------------------------------------

def rollout_episode(
    model: nn.Module,
    collector: ActivationCollector,
    perturbation_type: str | None,
    device: str,
    task_suite: str = "libero_90",
) -> dict[str, Any]:
    """Run one LIBERO-Plus episode and return collected activations.

    This is a reference implementation. Adapt the environment setup
    and action generation to your LIBERO / openpi integration.

    Args:
        perturbation_type: one of PERTURBATION_TYPES_6CLASS keys, or None for nominal.
    """
    # --- Environment setup (adapt to your LIBERO-Plus installation) ---
    try:
        import libero.libero.envs  # noqa: F401
        from libero.libero import get_libero_suite
    except ImportError:
        raise ImportError(
            "LIBERO package required. See https://github.com/Lifelong-Robot-Learning/LIBERO"
        )

    suite = get_libero_suite(task_suite)
    # Pick a random task from the suite
    import random
    task_idx = random.randint(0, len(suite) - 1)
    task = suite[task_idx]

    env_kwargs = {}
    if perturbation_type is not None:
        env_kwargs["perturbation_type"] = perturbation_type

    env = task.make_env(**env_kwargs)
    obs = env.reset()

    step_activations = []
    done = False
    step = 0
    max_steps = 400

    while not done and step < max_steps:
        collector.clear()
        # Build model input from observation (adapt to your observation format)
        model_input = _obs_to_model_input(obs, device)

        with torch.no_grad():
            action = model(model_input)

        pooled = collector.get_pooled()
        step_activations.append(pooled)

        obs, reward, done, info = env.step(action)
        step += 1

    env.close()

    # Average activations across timesteps
    avg_activations = _average_step_activations(step_activations)

    return {
        "activations": avg_activations,
        "task_name": task.name,
        "num_steps": step,
        "success": info.get("success", False),
    }


def _obs_to_model_input(obs: dict, device: str) -> dict:
    """Convert LIBERO observation dict to π₀ model input.

    This is environment-specific — adapt to your observation format
    (images, proprioception, language instruction).
    """
    inputs = {}
    for key, val in obs.items():
        if isinstance(val, torch.Tensor):
            inputs[key] = val.unsqueeze(0).to(device)
        else:
            import numpy as np
            if isinstance(val, np.ndarray):
                inputs[key] = torch.from_numpy(val).unsqueeze(0).to(device)
            else:
                inputs[key] = val
    return inputs


def _average_step_activations(
    step_activations: list[dict[str, dict[str, torch.Tensor]]],
) -> dict[str, dict[str, torch.Tensor]]:
    """Average activation tensors across timesteps."""
    if not step_activations:
        return {}

    layer_names = step_activations[0].keys()
    result = {}
    for layer in layer_names:
        result[layer] = {}
        for strat in POOLING_STRATEGIES:
            tensors = [sa[layer][strat] for sa in step_activations]
            result[layer][strat] = torch.stack(tensors).mean(dim=0)
    return result


# ---------------------------------------------------------------------------
# Data saving
# ---------------------------------------------------------------------------

def save_episodes(
    episodes: list[dict[str, Any]],
    perturbation_type: str,
    output_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{perturbation_type}.pt"

    # Support incremental collection: append to existing file
    if out_path.exists():
        existing = torch.load(out_path, weights_only=False)
        log.info("Appending %d episodes to existing %d in %s",
                 len(episodes), len(existing), out_path)
        episodes = existing + episodes

    torch.save(episodes, out_path)
    log.info("Saved %d episodes to %s", len(episodes), out_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def make_labels(perturbation_type: str) -> dict[str, int]:
    if perturbation_type == "nominal":
        return {"label_6class": -1, "label_3class": -1, "label_binary": 0}

    label_6 = PERTURBATION_TYPES_6CLASS[perturbation_type]
    label_3 = CLASS_6_TO_3_MAPPING[label_6]
    return {"label_6class": label_6, "label_3class": label_3, "label_binary": 1}


def collect(args: argparse.Namespace) -> None:
    device = args.device
    output_dir = Path(args.output_dir)

    log.info("Loading model from %s", args.checkpoint)
    model = load_pi0_model(args.checkpoint, device)

    collector = ActivationCollector(model)
    collector.register_hooks()

    perturbation_types: list[str]
    if args.perturbation_type == "all":
        perturbation_types = list(PERTURBATION_TYPES_6CLASS.keys())
    else:
        perturbation_types = [args.perturbation_type]

    for ptype in perturbation_types:
        is_nominal = ptype == "nominal"
        log.info("Collecting %d episodes for %s", args.num_episodes, ptype)

        episodes = []
        for ep_idx in range(args.num_episodes):
            log.info("  Episode %d/%d", ep_idx + 1, args.num_episodes)
            try:
                result = rollout_episode(
                    model, collector,
                    perturbation_type=None if is_nominal else ptype,
                    device=device,
                )
            except Exception:
                log.exception("Episode %d failed, skipping", ep_idx)
                continue

            labels = make_labels(ptype)
            episode_data = {
                "activations": result["activations"],
                **labels,
                "metadata": {
                    "perturbation_type": ptype,
                    "task_name": result["task_name"],
                    "num_steps": result["num_steps"],
                    "success": result["success"],
                    "episode_idx": ep_idx,
                },
            }
            episodes.append(episode_data)

        save_episodes(episodes, ptype, output_dir)

    collector.remove_hooks()
    log.info("Collection complete.")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Collect π₀ activations from LIBERO-Plus rollouts"
    )
    p.add_argument(
        "--checkpoint", type=str, required=True,
        help="Path to π₀ checkpoint directory (with .safetensors files)",
    )
    p.add_argument(
        "--output_dir", type=str, default="./activations",
        help="Directory to save activation .pt files",
    )
    valid_types = list(PERTURBATION_TYPES_6CLASS.keys()) + ["all", "nominal"]
    p.add_argument(
        "--perturbation_type", type=str, default="all",
        choices=valid_types,
        help="Perturbation type to collect, 'all' for all 6, or 'nominal'",
    )
    p.add_argument(
        "--num_episodes", type=int, default=50,
        help="Number of episodes per perturbation type",
    )
    p.add_argument(
        "--device", type=str, default="cuda:0",
        help="Device for model inference",
    )
    return p.parse_args()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    args = parse_args()
    collect(args)
