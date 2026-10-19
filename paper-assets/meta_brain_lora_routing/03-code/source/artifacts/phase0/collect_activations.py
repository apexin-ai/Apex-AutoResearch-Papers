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
from libero_integration import (
    load_pi0_for_collection,
    obs_to_model_input,
    run_episode,
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


# load_pi0_model, rollout_episode, _obs_to_model_input replaced by
# load_pi0_for_collection, run_episode, obs_to_model_input from libero_integration


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


def _set_seed(seed: int) -> None:
    import random
    import numpy as np
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def collect(args: argparse.Namespace) -> None:
    _set_seed(args.seed)
    device = args.device
    output_dir = Path(args.output_dir)

    log.info("Seed=%d, loading model from %s", args.seed, args.checkpoint)
    policy, model = load_pi0_for_collection(args.checkpoint, device)

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
                result = run_episode(
                    policy, collector,
                    perturbation_type=None if is_nominal else ptype,
                    device=device,
                    task_suite=args.task_suite,
                    seed=args.seed + ep_idx,
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
        "--task_suite", type=str, default="libero_spatial",
        choices=["libero_spatial", "libero_object", "libero_goal", "libero_10", "libero_90"],
        help="LIBERO-Plus suite (libero_90 has no perturbation variants)",
    )
    p.add_argument(
        "--device", type=str, default="cuda:0",
        help="Device for model inference",
    )
    p.add_argument(
        "--seed", type=int, default=42,
        help="Global random seed for reproducibility",
    )
    return p.parse_args()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    args = parse_args()
    collect(args)
