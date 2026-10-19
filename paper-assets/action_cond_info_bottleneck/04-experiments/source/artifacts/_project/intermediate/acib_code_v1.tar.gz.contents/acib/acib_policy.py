# ACIBPolicy: wraps SmolVLAPolicy with action-conditioned information bottleneck.
# Inserts ACIBScorer between PixelShuffle output and VLM transformer layers.
# During training, adds IB + consistency losses on top of flow matching loss.
#
# Key dependency: lerobot.policies.smolvla.SmolVLAPolicy
# NOTE: The exact hook point in SmolVLA's forward() needs source code confirmation.
# This implementation assumes visual tokens are accessible as an intermediate tensor
# after the connector (PixelShuffle + Linear Proj) and before VLM layers.
# [NEEDS_SOURCE_VERIFICATION] — Worker should read modeling_smolvla.py and patch
# _get_visual_tokens() and _inject_scored_tokens() methods accordingly.

import torch
import torch.nn as nn
from typing import Any

from acib.config import ACIBConfig
from acib.scorer import ACIBScorer
from acib.losses import ACIBLoss


class ACIBPolicy(nn.Module):
    """SmolVLA policy augmented with Action-Conditioned Information Bottleneck.

    Wraps a pretrained SmolVLAPolicy. During forward():
    1. Extracts visual tokens after PixelShuffle + Linear Proj (64 tokens, 960-dim)
    2. Extracts conditioning signal (language embedding or robot state)
    3. Runs ACIBScorer to get per-token relevance weights
    4. Applies weights to visual tokens before VLM processing
    5. Computes original task loss + ACIB losses

    Args:
        base_policy: pretrained SmolVLAPolicy instance.
        acib_config: ACIBConfig with scorer and loss settings.
    """

    def __init__(self, base_policy: nn.Module, acib_config: ACIBConfig):
        super().__init__()
        self.base_policy = base_policy
        self.acib_config = acib_config

        self.scorer = ACIBScorer(acib_config)
        self.acib_loss_fn = ACIBLoss(acib_config)
        self.acib_enabled = True

        self._setup_freeze(acib_config)
        self._install_hooks()

    def _setup_freeze(self, config: ACIBConfig) -> None:
        """Freeze parameters according to config."""
        if config.freeze_vlm:
            for name, param in self.base_policy.named_parameters():
                # Freeze VLM backbone (vision encoder + language model)
                # Keep action expert and state_proj trainable by default
                if "action" not in name.lower() and "state_proj" not in name.lower():
                    param.requires_grad = False

        if config.train_scorer_only:
            for param in self.base_policy.parameters():
                param.requires_grad = False

        # Scorer is always trainable
        for param in self.scorer.parameters():
            param.requires_grad = True

    def _install_hooks(self) -> None:
        """Install forward hooks to intercept visual tokens.

        [NEEDS_SOURCE_VERIFICATION]
        The hook target depends on SmolVLA's internal module structure.
        Expected target: the Linear Proj layer after PixelShuffle (connector).
        After reading modeling_smolvla.py, update the hook registration below.
        """
        self._visual_tokens_cache: torch.Tensor | None = None
        self._condition_cache: torch.Tensor | None = None
        self._hook_handles: list = []

        # Attempt to find the connector module
        # Common names: model.connector, model.vlm.connector, model.multi_modal_projector
        connector = self._find_module(
            ["connector", "multi_modal_projector", "vision_proj"]
        )
        if connector is not None:
            handle = connector.register_forward_hook(self._capture_visual_tokens_hook)
            self._hook_handles.append(handle)

    def _find_module(self, candidate_names: list[str]) -> nn.Module | None:
        """Search for a named submodule in the base policy."""
        for name, module in self.base_policy.named_modules():
            for candidate in candidate_names:
                if candidate in name.lower():
                    return module
        return None

    def _capture_visual_tokens_hook(
        self, module: nn.Module, input: Any, output: torch.Tensor
    ) -> torch.Tensor:
        """Forward hook: capture and reweight visual tokens.

        Intercepts connector output, applies ACIB scoring, returns modified tokens.
        """
        if not self.acib_enabled:
            return output

        # output shape: (B, N, D) where N=64, D=960
        visual_tokens = output
        self._visual_tokens_cache = visual_tokens.detach()

        if self._condition_cache is None:
            # Fallback: use mean-pooled visual tokens as self-conditioning
            # [NEEDS_SOURCE_VERIFICATION] Replace with proper language/state conditioning
            condition = visual_tokens.mean(dim=1)
        else:
            condition = self._condition_cache

        weights, logits = self.scorer(visual_tokens, condition)
        self._last_scores_logits = logits
        self._last_weights = weights

        return self.scorer.apply_weights(visual_tokens, weights)

    def forward(self, batch: dict[str, torch.Tensor]) -> tuple[torch.Tensor, dict]:
        """Forward pass with ACIB scoring.

        Args:
            batch: LeRobot-style batch dict with observation tensors and actions.

        Returns:
            total_loss: combined task + ACIB losses.
            loss_dict: breakdown of individual loss terms.
        """
        self._condition_cache = self._extract_condition(batch)

        # Run base policy forward (hook intercepts visual tokens)
        task_loss, base_outputs = self.base_policy.forward(batch)

        if not self.acib_enabled or not hasattr(self, "_last_scores_logits"):
            return task_loss, {"total": task_loss, "task": task_loss}

        scores_clean = self._last_scores_logits

        # If batch contains perturbed observations, score those too
        scores_perturbed = None
        if "observation.images.perturbed" in batch:
            scores_perturbed = self._score_perturbed(batch)

        loss_dict = self.acib_loss_fn(task_loss, scores_clean, scores_perturbed)
        return loss_dict["total"], loss_dict

    def _extract_condition(self, batch: dict[str, torch.Tensor]) -> torch.Tensor | None:
        """Extract conditioning signal from batch.

        [NEEDS_SOURCE_VERIFICATION]
        The exact method depends on how SmolVLA exposes language embeddings.
        Options:
          - "language": pool language token hidden states from VLM
          - "state": use robot state after state_proj
          - "both": concatenate both

        Current implementation: returns None (hook falls back to self-conditioning).
        Worker should implement proper extraction after reading source.
        """
        if self.acib_config.condition_source == "state":
            if "observation.state" in batch:
                state = batch["observation.state"]
                # state_proj in SmolVLA maps state to 960-dim
                # [NEEDS_SOURCE_VERIFICATION] Access base_policy.state_proj
                state_proj = self._find_module(["state_proj"])
                if state_proj is not None:
                    with torch.no_grad():
                        return state_proj(state).squeeze(1)
        return None

    def _score_perturbed(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        """Run scorer on perturbed visual tokens for consistency loss.

        [NEEDS_SOURCE_VERIFICATION]
        Requires extracting visual tokens from perturbed images through the
        vision encoder + PixelShuffle pipeline without full forward pass.
        """
        # Placeholder: run perturbed images through vision encoder + connector
        # and score them. Implementation depends on SmolVLA internals.
        raise NotImplementedError(
            "Perturbed scoring requires source code verification. "
            "Worker should implement after reading modeling_smolvla.py."
        )

    def select_action(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        """Inference: select action using base policy with ACIB-scored visual tokens."""
        self._condition_cache = self._extract_condition(batch)
        with torch.inference_mode():
            return self.base_policy.select_action(batch)

    def toggle_acib(self, enabled: bool) -> None:
        """Enable/disable ACIB scoring (for A/B eval comparison)."""
        self.acib_enabled = enabled

    def get_scorer_stats(self) -> dict[str, float]:
        """Return scorer weight statistics for logging."""
        if not hasattr(self, "_last_weights"):
            return {}
        w = self._last_weights
        return {
            "scorer/mean": w.mean().item(),
            "scorer/std": w.std().item(),
            "scorer/min": w.min().item(),
            "scorer/max": w.max().item(),
            "scorer/sparsity": (w < 0.5).float().mean().item(),
        }

    @classmethod
    def from_pretrained(cls, model_id: str, acib_config: ACIBConfig | None = None):
        """Load pretrained SmolVLA and wrap with ACIB.

        Args:
            model_id: HuggingFace model ID (e.g. 'lerobot/smolvla_base').
            acib_config: ACIB configuration. Uses defaults if None.
        """
        from lerobot.policies.smolvla import SmolVLAPolicy

        base_policy = SmolVLAPolicy.from_pretrained(model_id)
        if acib_config is None:
            acib_config = ACIBConfig()
        return cls(base_policy, acib_config)
