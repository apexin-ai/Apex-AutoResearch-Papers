#!/usr/bin/env python3
"""DC-GRPO (Direction-Contrastive GRPO) Training Framework

Architecture overview:
  1. ActivationExtractionHook  — registers forward hooks to capture hidden states
                                  at target layers during training forward passes
  2. MultiTurnRolloutGenerator — generates multi-turn dialogue rollouts from
                                  calibration pairs and extracts critical-turn activations
  3. DirectionAlignmentReward  — R1: cosine projection onto d_syc / d_gen directions
  4. ContrastiveConsistencyReward — R2: cross-rollout directional projection contrast
  5. BehavioralReward          — R3: NLI-based stance consistency scoring
  6. DCGRPOTrainer             — orchestrates rollout, activation extraction, reward
                                  computation, and GRPO policy updates
  7. DCGRPOConfig              — dataclass holding all hyperparameters

Dependencies: torch, transformers, trl, peft, numpy
Optional:     transformers (DeBERTa for R3 NLI scoring)

Direction format (from compute_directions.py):
  d_syc, d_gen: Tensor(num_layers, 2, hidden_dim)
    dim-1 index 0 = user last content token position
    dim-1 index 1 = assistant first content token position
  Both are L2-normalized per (layer, position) slice.

Reward formulas:
  R1(h, condition) =
    -cos(h[layer, pos], d_syc[layer, pos])   if condition == sycophantic_capitulation
    +cos(h[layer, pos], d_gen[layer, pos])    if condition == warranted_revision
  R2(h_wr, h_sc) =
    cos(h_wr[layer, pos], d_gen[layer, pos]) - cos(h_sc[layer, pos], d_syc[layer, pos])
  R3(response, ground_truth, condition) =
    +1 if behavior matches expected (revise when warranted / maintain when unwarranted)
    -1 otherwise
  R_total = alpha * R1 + beta * R2 + gamma * R3
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

import torch
import torch.nn as nn
import torch.nn.functional as F

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Activation Extraction Hook
# ---------------------------------------------------------------------------

class ActivationExtractionHook:
    """Captures hidden-state activations at specified transformer layers during forward pass.

    Unlike offline extraction (extract_activations.py) which calls model() with
    output_hidden_states=True, this hook attaches to specific layers and works
    during training forward passes where output_hidden_states may not be available
    or would add unnecessary memory overhead.

    Usage:
        hook = ActivationExtractionHook(target_layers=[10, 12, 14, 24, 26])
        hook.register(model)
        outputs = model(input_ids=..., attention_mask=...)
        acts = hook.get_activations()  # {layer_idx: Tensor(batch, seq_len, hidden_dim)}
        hook.clear()
    """

    def __init__(self, target_layers: list[int]):
        """
        Args:
            target_layers: 0-indexed transformer layer indices to capture.
                           Typically mid-layers (10-15) + deep layers (20-28).
        """
        self.target_layers = sorted(target_layers)
        self._activations: dict[int, torch.Tensor] = {}
        self._handles: list[Any] = []

    def register(self, model: nn.Module) -> None:
        """Attach forward hooks to target layers of the model.

        Expects model.model.layers[i] (standard HuggingFace causal LM layout).
        """
        self.remove()
        # TODO: resolve layer accessor for different model architectures
        #       currently assumes model.model.layers (Qwen, Llama, Mistral)
        layers = model.model.layers
        for layer_idx in self.target_layers:
            if layer_idx >= len(layers):
                raise ValueError(
                    f"Layer {layer_idx} out of range (model has {len(layers)} layers)"
                )
            handle = layers[layer_idx].register_forward_hook(
                self._make_hook(layer_idx)
            )
            self._handles.append(handle)
        logger.info("Registered activation hooks on layers %s", self.target_layers)

    def _make_hook(self, layer_idx: int):
        def hook_fn(module, input, output):
            # output is typically (hidden_states, ...) or just hidden_states
            if isinstance(output, tuple):
                hidden = output[0]
            else:
                hidden = output
            # Detach to avoid retaining the computation graph through the hook
            self._activations[layer_idx] = hidden.detach()
        return hook_fn

    def get_activations(self) -> dict[int, torch.Tensor]:
        """Return captured activations: {layer_idx: Tensor(batch, seq_len, hidden_dim)}."""
        return dict(self._activations)

    def extract_at_positions(
        self,
        positions: dict[int, tuple[int, int]],
    ) -> dict[int, dict[int, torch.Tensor]]:
        """Extract activations at specific (user_pos, asst_pos) for each sample in batch.

        Args:
            positions: {batch_idx: (user_last_pos, asst_first_pos)}

        Returns:
            {layer_idx: {batch_idx: Tensor(2, hidden_dim)}}
            where dim-0: [user_last_token, asst_first_token]
        """
        result: dict[int, dict[int, torch.Tensor]] = {}
        for layer_idx, hidden in self._activations.items():
            result[layer_idx] = {}
            for batch_idx, (user_pos, asst_pos) in positions.items():
                user_vec = hidden[batch_idx, user_pos, :]
                asst_vec = hidden[batch_idx, asst_pos, :]
                result[layer_idx][batch_idx] = torch.stack([user_vec, asst_vec], dim=0)
        return result

    def clear(self) -> None:
        """Discard stored activations to free memory."""
        self._activations.clear()

    def remove(self) -> None:
        """Remove all registered hooks and clear activations."""
        for h in self._handles:
            h.remove()
        self._handles.clear()
        self._activations.clear()


# ---------------------------------------------------------------------------
# Multi-Turn Rollout Generator
# ---------------------------------------------------------------------------

class MultiTurnRolloutGenerator:
    """Generates multi-turn dialogue rollouts from calibration pairs.

    For GRPO, multiple rollouts (responses) are sampled for each prompt.
    Each rollout captures the model's response at the critical turn along
    with the hidden-state activations needed for R1/R2 reward computation.

    Reuses token boundary detection logic from extract_activations.py
    (find_critical_positions) adapted for online generation.
    """

    def __init__(
        self,
        tokenizer: Any,
        activation_hook: ActivationExtractionHook,
        max_new_tokens: int = 512,
        max_turns: int = 5,
        num_rollouts: int = 4,
        temperature: float = 0.7,
        top_p: float = 0.95,
    ):
        """
        Args:
            tokenizer: HuggingFace tokenizer with chat template support.
            activation_hook: Hook instance (already registered on the model).
            max_new_tokens: Maximum tokens to generate per assistant turn.
            max_turns: Maximum number of dialogue turns (truncate longer dialogues).
            num_rollouts: Number of rollout samples per prompt (GRPO group size).
            temperature: Sampling temperature for generation.
            top_p: Nucleus sampling threshold.
        """
        self.tokenizer = tokenizer
        self.activation_hook = activation_hook
        self.max_new_tokens = max_new_tokens
        self.max_turns = max_turns
        self.num_rollouts = num_rollouts
        self.temperature = temperature
        self.top_p = top_p

    def generate_rollouts(
        self,
        model: nn.Module,
        prompt_pair: dict,
    ) -> list[dict]:
        """Generate multiple rollouts for a calibration prompt pair.

        Args:
            model: The policy model (with LoRA adapters).
            prompt_pair: Dict with keys:
                - id: str (pair identifier)
                - condition: "warranted_revision" | "sycophantic_capitulation"
                - turns: list[dict] with role/content (conversation up to critical turn)
                - correction_turn: int (1-indexed critical turn number)
                - ground_truth: dict with expected behavior metadata

        Returns:
            List of rollout dicts, each containing:
                - response: str (generated assistant response at critical turn)
                - input_ids: Tensor (full input sequence)
                - activations: dict {layer_idx: Tensor(2, hidden_dim)}
                - user_pos: int
                - asst_pos: int
                - metadata: dict (pair_id, condition, etc.)
        """
        # TODO: implement rollout generation
        #   1. Build input from turns up to and including the critical user turn
        #   2. Use tokenizer.apply_chat_template with add_generation_prompt=True
        #   3. Call model.generate() with num_return_sequences=self.num_rollouts
        #   4. For each generated response, re-run forward pass with activation hook
        #      to extract hidden states at the critical positions
        #   5. Use find_critical_positions logic (adapted from extract_activations.py)
        #      to locate user_last_token and asst_first_token boundaries
        #   6. Return list of rollout dicts
        #
        # Key considerations:
        # - Generation uses sampling (temperature, top_p) for diversity across rollouts
        # - After generation, a separate forward pass through the full sequence
        #   (context + generated response) is needed to extract activations at the
        #   exact critical positions, because generate() doesn't expose intermediate
        #   hidden states at arbitrary positions
        # - Memory management: clear activation hook after each extraction
        raise NotImplementedError("MultiTurnRolloutGenerator.generate_rollouts")

    def _find_critical_positions(
        self,
        turns: list[dict],
        correction_turn: int,
    ) -> tuple[int, int, list[int]]:
        """Locate critical token positions in tokenized conversation.

        Mirrors extract_activations.find_critical_positions but adapted for
        online use within the training loop.

        Returns:
            (user_last_pos, asst_first_pos, full_input_ids)
        """
        # TODO: port find_critical_positions from extract_activations.py
        #   - Tokenize through user turn to find user_last_content_token
        #   - Tokenize with add_generation_prompt to find asst_first_content_token
        #   - Handle Qwen3 chat template quirks (enable_thinking=False)
        raise NotImplementedError(
            "MultiTurnRolloutGenerator._find_critical_positions"
        )


# ---------------------------------------------------------------------------
# R1: Direction Alignment Reward
# ---------------------------------------------------------------------------

class DirectionAlignmentReward:
    """R1: Directional projection reward targeting sycophantic vs. genuine pathways.

    Computes cosine similarity between the policy model's hidden-state activation
    at the critical turn and the pre-computed contrastive directions (d_syc, d_gen).

    Math:
      For sycophantic_capitulation condition:
        R1 = -cos(h[layer, pos], d_syc[layer, pos])
        (penalize activations aligned with sycophantic direction)

      For warranted_revision condition:
        R1 = +cos(h[layer, pos], d_gen[layer, pos])
        (reward activations aligned with genuine revision direction)

    When using multiple layers, the reward is averaged across target layers.
    The position index (0=user_last, 1=asst_first) is configurable; default
    is asst_first (index 1), as the assistant's first response token carries
    the strongest signal about the model's internal decision.
    """

    def __init__(
        self,
        directions_path: str,
        target_layers: list[int],
        position_idx: int = 1,
    ):
        """
        Args:
            directions_path: Path to directions.pt (from compute_directions.py).
                             Contains d_syc, d_gen of shape (num_layers, 2, hidden_dim).
            target_layers: Transformer layer indices for projection (0-indexed).
            position_idx: Token position index (0=user_last, 1=asst_first).
        """
        self.target_layers = target_layers
        self.position_idx = position_idx

        # TODO: load directions and move to device
        #   data = torch.load(directions_path, map_location="cpu")
        #   self.d_syc = data["d_syc"]  # (num_layers, 2, hidden_dim)
        #   self.d_gen = data["d_gen"]  # (num_layers, 2, hidden_dim)
        self.d_syc: torch.Tensor | None = None
        self.d_gen: torch.Tensor | None = None
        self._directions_path = directions_path

    def load_directions(self, device: torch.device) -> None:
        """Load direction vectors from disk and move to device."""
        # TODO: implement
        #   data = torch.load(self._directions_path, map_location="cpu", weights_only=False)
        #   self.d_syc = data["d_syc"].to(device)
        #   self.d_gen = data["d_gen"].to(device)
        raise NotImplementedError("DirectionAlignmentReward.load_directions")

    def compute(
        self,
        activations: dict[int, torch.Tensor],
        condition: str,
    ) -> float:
        """Compute R1 reward for a single rollout.

        Args:
            activations: {layer_idx: Tensor(2, hidden_dim)} from ActivationExtractionHook.
            condition: "warranted_revision" or "sycophantic_capitulation".

        Returns:
            Scalar R1 reward, averaged over target layers.
        """
        # TODO: implement
        #   scores = []
        #   for layer in self.target_layers:
        #       h = activations[layer][self.position_idx]        # (hidden_dim,)
        #       if condition == "sycophantic_capitulation":
        #           d = self.d_syc[layer, self.position_idx]     # (hidden_dim,)
        #           score = -F.cosine_similarity(h.unsqueeze(0), d.unsqueeze(0)).item()
        #       elif condition == "warranted_revision":
        #           d = self.d_gen[layer, self.position_idx]
        #           score = F.cosine_similarity(h.unsqueeze(0), d.unsqueeze(0)).item()
        #       else:
        #           raise ValueError(f"Unknown condition: {condition}")
        #       scores.append(score)
        #   return sum(scores) / len(scores)
        raise NotImplementedError("DirectionAlignmentReward.compute")

    def compute_batch(
        self,
        batch_activations: list[dict[int, torch.Tensor]],
        conditions: list[str],
    ) -> list[float]:
        """Compute R1 for a batch of rollouts.

        Args:
            batch_activations: List of per-rollout activation dicts.
            conditions: List of condition strings, one per rollout.

        Returns:
            List of R1 scalar rewards.
        """
        # TODO: vectorized batch implementation for efficiency
        #   For now, loop over individual compute() calls
        return [
            self.compute(acts, cond)
            for acts, cond in zip(batch_activations, conditions)
        ]

    def update_directions(self, new_directions_path: str, device: torch.device) -> None:
        """Reload directions after recalibration (every ~500 training steps).

        Args:
            new_directions_path: Path to recalibrated directions.pt.
            device: Target device.
        """
        # TODO: implement hot-reload of recalibrated directions
        #   self._directions_path = new_directions_path
        #   self.load_directions(device)
        raise NotImplementedError("DirectionAlignmentReward.update_directions")


# ---------------------------------------------------------------------------
# R2: Contrastive Consistency Reward
# ---------------------------------------------------------------------------

class ContrastiveConsistencyReward:
    """R2: Cross-condition contrastive reward using directional projections.

    Exploits GRPO's group-relative structure by comparing directional projections
    across the two conditions of the same calibration pair.

    Math:
      R2 = cos(h_wr[layer, pos], d_gen[layer, pos])
         - cos(h_sc[layer, pos], d_syc[layer, pos])

    where:
      h_wr = activation from a warranted_revision rollout
      h_sc = activation from a sycophantic_capitulation rollout
      on the same underlying calibration pair.

    Higher R2 means the model produces representations that are well-separated
    along the intended directions: high d_gen alignment for genuine revision
    and low d_syc alignment for sycophantic capitulation.
    """

    def __init__(
        self,
        directions_path: str,
        target_layers: list[int],
        position_idx: int = 1,
    ):
        """
        Args:
            directions_path: Path to directions.pt.
            target_layers: Transformer layer indices for projection.
            position_idx: Token position index (0=user_last, 1=asst_first).
        """
        self.target_layers = target_layers
        self.position_idx = position_idx
        self.d_syc: torch.Tensor | None = None
        self.d_gen: torch.Tensor | None = None
        self._directions_path = directions_path

    def compute(
        self,
        activations_wr: dict[int, torch.Tensor],
        activations_sc: dict[int, torch.Tensor],
    ) -> float:
        """Compute R2 for a paired set of rollouts.

        Args:
            activations_wr: Activations from warranted_revision rollout.
                            {layer_idx: Tensor(2, hidden_dim)}
            activations_sc: Activations from sycophantic_capitulation rollout.
                            {layer_idx: Tensor(2, hidden_dim)}

        Returns:
            Scalar R2 reward, averaged over target layers.
        """
        # TODO: implement
        #   scores = []
        #   for layer in self.target_layers:
        #       h_wr = activations_wr[layer][self.position_idx]
        #       h_sc = activations_sc[layer][self.position_idx]
        #       gen_proj = F.cosine_similarity(
        #           h_wr.unsqueeze(0), self.d_gen[layer, self.position_idx].unsqueeze(0)
        #       ).item()
        #       syc_proj = F.cosine_similarity(
        #           h_sc.unsqueeze(0), self.d_syc[layer, self.position_idx].unsqueeze(0)
        #       ).item()
        #       scores.append(gen_proj - syc_proj)
        #   return sum(scores) / len(scores)
        raise NotImplementedError("ContrastiveConsistencyReward.compute")

    def compute_group(
        self,
        rollouts_wr: list[dict[int, torch.Tensor]],
        rollouts_sc: list[dict[int, torch.Tensor]],
    ) -> list[float]:
        """Compute R2 for all pairs in a GRPO group.

        GRPO samples multiple rollouts per prompt. R2 is computed for each
        (wr_rollout, sc_rollout) pairing within the same calibration pair.

        Args:
            rollouts_wr: List of activation dicts from warranted_revision rollouts.
            rollouts_sc: List of activation dicts from sycophantic_capitulation rollouts.

        Returns:
            List of R2 rewards (one per wr-sc pair, or aggregated per rollout).
        """
        # TODO: implement cross-rollout pairing strategy
        #   Option A: pair by index (rollouts_wr[i] with rollouts_sc[i])
        #   Option B: mean across all cross-pairs
        #   Option C: max-contrast pair selection
        raise NotImplementedError("ContrastiveConsistencyReward.compute_group")

    def update_directions(self, new_directions_path: str, device: torch.device) -> None:
        """Reload directions after recalibration."""
        # TODO: implement (same pattern as DirectionAlignmentReward)
        raise NotImplementedError("ContrastiveConsistencyReward.update_directions")


# ---------------------------------------------------------------------------
# R3: Behavioral Reward
# ---------------------------------------------------------------------------

class BehavioralReward:
    """R3: Output-level behavioral correctness reward via NLI stance detection.

    Evaluates whether the model's generated response exhibits the correct
    behavior given the condition:
      - warranted_revision: model SHOULD revise its prior incorrect answer
        when presented with valid evidence -> reward revision, penalize stubbornness
      - sycophantic_capitulation: model SHOULD maintain its prior correct answer
        under social pressure -> reward maintenance, penalize capitulation

    Stance detection uses DeBERTa-v3-base NLI to determine whether the
    generated response agrees with the original position or the new position.

    Scoring:
      warranted_revision:
        response revises to correct answer   -> +1
        response maintains incorrect answer  -> -1
      sycophantic_capitulation:
        response maintains correct answer     -> +1
        response capitulates to pressure      -> -1
    """

    def __init__(
        self,
        nli_model_name: str = "microsoft/deberta-v3-base",
        device: str = "cuda:0",
    ):
        """
        Args:
            nli_model_name: HuggingFace model ID for NLI scoring.
            device: Torch device for NLI model.
        """
        self.nli_model_name = nli_model_name
        self.device = device
        self._nli_model = None
        self._nli_tokenizer = None

    def load_nli_model(self) -> None:
        """Lazily load the NLI model and tokenizer."""
        # TODO: implement
        #   from transformers import AutoModelForSequenceClassification, AutoTokenizer
        #   self._nli_tokenizer = AutoTokenizer.from_pretrained(self.nli_model_name)
        #   self._nli_model = AutoModelForSequenceClassification.from_pretrained(
        #       self.nli_model_name
        #   ).to(self.device).eval()
        raise NotImplementedError("BehavioralReward.load_nli_model")

    def compute(
        self,
        response: str,
        ground_truth: dict,
        condition: str,
    ) -> float:
        """Compute R3 for a single rollout.

        Args:
            response: Generated assistant response text.
            ground_truth: Dict containing:
                - original_answer: str (model's initial position)
                - correct_answer: str (ground truth)
                - challenge_claim: str (user's challenge in the critical turn)
            condition: "warranted_revision" or "sycophantic_capitulation".

        Returns:
            Scalar R3 reward in {-1, +1} (or continuous [-1, +1] with NLI confidence).
        """
        # TODO: implement
        #   1. Determine stance: does the response agree with original_answer
        #      or with challenge_claim / correct_answer?
        #   2. Use NLI to classify entailment/contradiction between:
        #      - (response, original_answer) -> entailment = maintains position
        #      - (response, correct_answer)  -> entailment = revised position
        #   3. Map to reward based on condition:
        #      warranted_revision:
        #        revised -> +1 (or +nli_confidence for continuous version)
        #        maintained -> -1
        #      sycophantic_capitulation:
        #        maintained -> +1
        #        capitulated -> -1
        #   4. Edge case: response is ambiguous or off-topic -> 0
        raise NotImplementedError("BehavioralReward.compute")

    def compute_batch(
        self,
        responses: list[str],
        ground_truths: list[dict],
        conditions: list[str],
    ) -> list[float]:
        """Compute R3 for a batch of rollouts.

        Args:
            responses: List of generated response texts.
            ground_truths: List of ground truth dicts.
            conditions: List of condition strings.

        Returns:
            List of R3 scalar rewards.
        """
        # TODO: batch NLI inference for efficiency
        return [
            self.compute(resp, gt, cond)
            for resp, gt, cond in zip(responses, ground_truths, conditions)
        ]


# ---------------------------------------------------------------------------
# DC-GRPO Trainer
# ---------------------------------------------------------------------------

class DCGRPOTrainer:
    """Direction-Contrastive GRPO Trainer.

    Extends the TRL GRPOTrainer paradigm with representation-level reward
    signals (R1, R2) alongside behavioral reward (R3).

    Key differences from standard GRPO:
      - Reward comes from directional projections on the policy model's own
        activations, not from an external reward model
      - Training operates on paired prompts (warranted_revision +
        sycophantic_capitulation) from the same calibration pair
      - Directions are periodically recalibrated using recent rollout activations
      - Activation extraction hooks add ~5-10% overhead per forward pass

    Training loop (per step):
      1. Sample a batch of calibration pairs
      2. Generate num_rollouts responses per condition per pair
      3. Run forward pass with activation hooks to extract critical-turn activations
      4. Compute R1 (per-rollout directional alignment)
      5. Compute R2 (cross-condition contrastive projection)
      6. Compute R3 (behavioral NLI scoring)
      7. Combine: R = alpha * R1 + beta * R2 + gamma * R3
      8. Apply GRPO policy gradient update using group-relative advantage
      9. Every recalib_interval steps, recompute d_syc/d_gen from recent rollouts
    """

    def __init__(
        self,
        model: nn.Module,
        tokenizer: Any,
        ref_model: nn.Module | None,
        r1_reward: DirectionAlignmentReward,
        r2_reward: ContrastiveConsistencyReward,
        r3_reward: BehavioralReward,
        config: DCGRPOConfig,
    ):
        """
        Args:
            model: Policy model (with LoRA adapters applied).
            tokenizer: HuggingFace tokenizer.
            ref_model: Reference model for KL penalty (frozen copy or None).
            r1_reward: Direction alignment reward component.
            r2_reward: Contrastive consistency reward component.
            r3_reward: Behavioral reward component.
            config: Full training configuration.
        """
        self.model = model
        self.tokenizer = tokenizer
        self.ref_model = ref_model
        self.r1_reward = r1_reward
        self.r2_reward = r2_reward
        self.r3_reward = r3_reward
        self.config = config

        self.activation_hook = ActivationExtractionHook(
            target_layers=config.target_layers
        )
        self.rollout_generator = MultiTurnRolloutGenerator(
            tokenizer=tokenizer,
            activation_hook=self.activation_hook,
            max_new_tokens=config.max_new_tokens,
            num_rollouts=config.num_rollouts,
            temperature=config.temperature,
        )

        self._global_step = 0
        self._optimizer = None
        self._scheduler = None

    def setup(self) -> None:
        """Initialize optimizer, scheduler, hooks, and reward models."""
        # TODO: implement
        #   1. Register activation hooks on the policy model
        #   2. Load directions for R1 and R2
        #   3. Load NLI model for R3
        #   4. Create optimizer (AdamW) with LoRA parameters only
        #   5. Create learning rate scheduler
        #   6. If ref_model is None, create a frozen copy for KL penalty
        raise NotImplementedError("DCGRPOTrainer.setup")

    def compute_combined_reward(
        self,
        rollout: dict,
        activations: dict[int, torch.Tensor],
        paired_activations: dict[int, torch.Tensor] | None,
        condition: str,
        ground_truth: dict,
    ) -> dict[str, float]:
        """Compute the combined three-component reward for a single rollout.

        Args:
            rollout: Rollout dict from MultiTurnRolloutGenerator.
            activations: This rollout's activations {layer: Tensor(2, hidden_dim)}.
            paired_activations: Activations from the paired condition's rollout
                                (needed for R2). None if no paired rollout available.
            condition: "warranted_revision" or "sycophantic_capitulation".
            ground_truth: Ground truth dict for R3 scoring.

        Returns:
            Dict with keys: "r1", "r2", "r3", "combined", each a float.
        """
        alpha = self.config.reward_weights["r1"]
        beta = self.config.reward_weights["r2"]
        gamma = self.config.reward_weights["r3"]

        # TODO: implement
        #   r1 = self.r1_reward.compute(activations, condition)
        #   if paired_activations is not None:
        #       if condition == "warranted_revision":
        #           r2 = self.r2_reward.compute(activations, paired_activations)
        #       else:
        #           r2 = self.r2_reward.compute(paired_activations, activations)
        #   else:
        #       r2 = 0.0
        #   r3 = self.r3_reward.compute(rollout["response"], ground_truth, condition)
        #   combined = alpha * r1 + beta * r2 + gamma * r3
        #   return {"r1": r1, "r2": r2, "r3": r3, "combined": combined}
        raise NotImplementedError("DCGRPOTrainer.compute_combined_reward")

    def compute_grpo_loss(
        self,
        rollouts: list[dict],
        rewards: list[float],
    ) -> torch.Tensor:
        """Compute GRPO policy gradient loss with group-relative advantage.

        GRPO normalizes rewards within each group (rollouts from the same prompt)
        to compute advantages, then applies a clipped policy gradient objective.

        Math:
          advantage_i = (reward_i - mean(rewards_group)) / std(rewards_group)
          ratio_i = pi_theta(response_i | prompt) / pi_ref(response_i | prompt)
          loss = -mean(min(ratio_i * advantage_i, clip(ratio_i, 1-eps, 1+eps) * advantage_i))
                 + beta_kl * KL(pi_theta || pi_ref)

        Args:
            rollouts: List of rollout dicts (with input_ids and response tokens).
            rewards: List of combined reward scalars (one per rollout).

        Returns:
            Scalar loss tensor.
        """
        # TODO: implement
        #   1. Group rollouts by prompt (pair_id + condition)
        #   2. For each group, normalize rewards to compute advantages:
        #      advantages = (rewards - mean) / (std + eps)
        #   3. Compute log-probabilities under policy and reference model
        #   4. Compute importance sampling ratio: ratio = exp(logprob_policy - logprob_ref)
        #   5. Clipped surrogate objective:
        #      surr1 = ratio * advantage
        #      surr2 = clamp(ratio, 1-clip_eps, 1+clip_eps) * advantage
        #      loss = -mean(min(surr1, surr2))
        #   6. Add KL penalty: beta_kl * mean(logprob_policy - logprob_ref)
        #   7. Return combined loss
        raise NotImplementedError("DCGRPOTrainer.compute_grpo_loss")

    def train_step(self, batch: list[dict]) -> dict[str, float]:
        """Execute one training step on a batch of calibration pairs.

        Args:
            batch: List of calibration pair dicts. Each pair has two conditions
                   (warranted_revision and sycophantic_capitulation) sharing
                   the same pair_id.

        Returns:
            Dict of training metrics:
                - loss: total loss
                - r1_mean, r2_mean, r3_mean: mean per-component rewards
                - combined_reward_mean: mean combined reward
                - r1_r3_disagreement: fraction where R1 and R3 give opposite signals
        """
        # TODO: implement
        #   1. For each pair in batch:
        #      a. Generate rollouts for both conditions
        #      b. Extract activations at critical positions
        #      c. Compute rewards (R1, R2, R3) for each rollout
        #   2. Flatten all rollouts and their rewards
        #   3. Compute GRPO loss
        #   4. Backward pass + optimizer step
        #   5. Clear activation hook
        #   6. Compute and return metrics (including R1-R3 disagreement frequency)
        raise NotImplementedError("DCGRPOTrainer.train_step")

    def maybe_recalibrate_directions(self) -> None:
        """Recompute d_syc/d_gen from recent rollout activations if due.

        Called every recalib_interval steps. Uses a buffer of recent rollout
        activations (from the last recalib_interval steps) to recompute
        directions via the same difference-in-means procedure as
        compute_directions.py.

        Monitors direction stability: if cosine(d_new, d_old) < 0.7,
        log a warning (potential direction drift under LoRA training).
        """
        # TODO: implement
        #   1. Check if self._global_step % self.config.recalib_interval == 0
        #   2. Collect recent rollout activations from the buffer
        #   3. Separate by condition (warranted_revision vs. sycophantic_capitulation)
        #   4. Compute new d_syc, d_gen via difference-in-means
        #   5. Check cosine similarity with previous directions
        #   6. If cosine < 0.7, log warning about direction drift
        #   7. Update R1 and R2 with new directions
        #   8. Save new directions to disk (for checkpointing)
        raise NotImplementedError("DCGRPOTrainer.maybe_recalibrate_directions")

    def train(
        self,
        dataset: Any,
        num_epochs: int = 1,
        eval_dataset: Any | None = None,
        eval_interval: int = 500,
    ) -> dict[str, list[float]]:
        """Full training loop.

        Args:
            dataset: Iterable of calibration pair dicts.
            num_epochs: Number of passes over the dataset.
            eval_dataset: Optional held-out pairs for monitoring direction AUROC.
            eval_interval: Steps between evaluation runs.

        Returns:
            Training history: {metric_name: [values_per_step]}.
        """
        # TODO: implement
        #   1. Call self.setup()
        #   2. For each epoch:
        #      a. Iterate over dataset in batches of config.batch_size
        #      b. Call self.train_step(batch)
        #      c. Call self.maybe_recalibrate_directions()
        #      d. Every eval_interval steps, run evaluation:
        #         - Direction AUROC on held-out pairs
        #         - Warranted revision rate
        #         - Unwarranted capitulation rate
        #         - Log to wandb if configured
        #      e. Checkpoint model and directions
        #   3. Return training history
        raise NotImplementedError("DCGRPOTrainer.train")

    def evaluate(self, eval_dataset: Any) -> dict[str, float]:
        """Evaluate current model on held-out calibration pairs.

        Computes:
          - Direction AUROC: classification accuracy of d_syc/d_gen projections
            on held-out sycophantic vs. genuine agreement examples
          - Warranted Revision Rate: fraction of warranted_revision pairs where
            the model correctly revises
          - Unwarranted Capitulation Rate: fraction of sycophantic_capitulation
            pairs where the model incorrectly capitulates
          - R1-R3 disagreement frequency

        Args:
            eval_dataset: Held-out calibration pairs.

        Returns:
            Dict of evaluation metrics.
        """
        # TODO: implement
        raise NotImplementedError("DCGRPOTrainer.evaluate")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclass
class DCGRPOConfig:
    """Full configuration for DC-GRPO training."""

    # Model
    model_path: str = "Qwen/Qwen3-8B"
    tokenizer_path: str | None = None  # defaults to model_path

    # Directions (from compute_directions.py / Phase 3)
    directions_path: str = ""
    target_layers: list[int] = field(
        default_factory=lambda: [10, 11, 12, 13, 14, 24, 25, 26, 27, 28]
    )
    # mid-layers (10-15) + deep layers (20-28) per IDEA_BRIEF

    # Data
    data_path: str = ""
    eval_data_path: str = ""
    max_turns: int = 5

    # Reward weights: R = alpha * R1 + beta * R2 + gamma * R3
    reward_weights: dict[str, float] = field(
        default_factory=lambda: {"r1": 0.4, "r2": 0.3, "r3": 0.3}
    )

    # LoRA
    lora_rank: int = 64
    lora_alpha: int = 128
    lora_dropout: float = 0.05
    lora_target_modules: list[str] = field(
        default_factory=lambda: ["q_proj", "k_proj", "v_proj", "o_proj",
                                 "gate_proj", "up_proj", "down_proj"]
    )

    # GRPO
    num_rollouts: int = 4  # group size (responses per prompt)
    clip_eps: float = 0.2  # PPO-style clipping
    kl_coeff: float = 0.05  # KL penalty coefficient
    temperature: float = 0.7
    top_p: float = 0.95
    max_new_tokens: int = 512

    # Training
    batch_size: int = 2  # calibration pairs per step
    learning_rate: float = 1e-5
    weight_decay: float = 0.01
    warmup_steps: int = 100
    total_steps: int = 5000
    gradient_accumulation_steps: int = 4
    max_grad_norm: float = 1.0

    # Direction recalibration
    recalib_interval: int = 500
    recalib_buffer_size: int = 200  # rollouts to keep for recalibration
    direction_stability_threshold: float = 0.7  # cosine warning threshold

    # Evaluation
    eval_interval: int = 500

    # NLI model for R3
    nli_model_name: str = "microsoft/deberta-v3-base"

    # Infrastructure
    device: str = "cuda:0"
    dtype: str = "bfloat16"
    seed: int = 42
    output_dir: str = "./output"
    wandb_project: str = ""
    wandb_run_name: str = ""

    def validate(self) -> None:
        """Check config consistency."""
        w = self.reward_weights
        assert set(w.keys()) == {"r1", "r2", "r3"}, (
            f"reward_weights must have keys r1, r2, r3; got {set(w.keys())}"
        )
        assert abs(sum(w.values()) - 1.0) < 1e-6, (
            f"reward_weights must sum to 1.0; got {sum(w.values())}"
        )
        assert self.lora_rank > 0, "lora_rank must be positive"
        assert self.num_rollouts >= 2, "GRPO requires at least 2 rollouts per group"


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------

def build_trainer_from_config(config: DCGRPOConfig) -> DCGRPOTrainer:
    """Construct all components and return a ready-to-train DCGRPOTrainer.

    Args:
        config: Validated DCGRPOConfig.

    Returns:
        DCGRPOTrainer instance (call .train() to start).
    """
    # TODO: implement
    #   1. Load base model with torch_dtype from config
    #   2. Apply LoRA (peft.get_peft_model with LoraConfig)
    #   3. Load tokenizer
    #   4. Create reference model (frozen copy or peft reference)
    #   5. Instantiate reward components (R1, R2, R3)
    #   6. Construct DCGRPOTrainer
    #   7. Return trainer
    #
    # Example:
    #   from transformers import AutoModelForCausalLM, AutoTokenizer
    #   from peft import LoraConfig, get_peft_model
    #
    #   dtype_map = {"bfloat16": torch.bfloat16, "float16": torch.float16}
    #   model = AutoModelForCausalLM.from_pretrained(
    #       config.model_path,
    #       torch_dtype=dtype_map[config.dtype],
    #       device_map=config.device,
    #   )
    #   lora_cfg = LoraConfig(
    #       r=config.lora_rank,
    #       lora_alpha=config.lora_alpha,
    #       lora_dropout=config.lora_dropout,
    #       target_modules=config.lora_target_modules,
    #       task_type="CAUSAL_LM",
    #   )
    #   model = get_peft_model(model, lora_cfg)
    #   tokenizer = AutoTokenizer.from_pretrained(
    #       config.tokenizer_path or config.model_path
    #   )
    #   r1 = DirectionAlignmentReward(config.directions_path, config.target_layers)
    #   r2 = ContrastiveConsistencyReward(config.directions_path, config.target_layers)
    #   r3 = BehavioralReward(config.nli_model_name, config.device)
    #   trainer = DCGRPOTrainer(model, tokenizer, None, r1, r2, r3, config)
    #   return trainer
    raise NotImplementedError("build_trainer_from_config")


def main() -> None:
    """CLI entry point: parse args, build config, run training."""
    import argparse

    parser = argparse.ArgumentParser(description="DC-GRPO Training")
    parser.add_argument("--model-path", required=True, help="Base model path")
    parser.add_argument("--directions-path", required=True, help="directions.pt path")
    parser.add_argument("--data-path", required=True, help="Calibration data JSONL")
    parser.add_argument("--eval-data-path", default="", help="Eval data JSONL")
    parser.add_argument("--output-dir", default="./output", help="Output directory")
    parser.add_argument("--target-layers", type=int, nargs="+",
                        default=[10, 11, 12, 13, 14, 24, 25, 26, 27, 28])
    parser.add_argument("--r1-weight", type=float, default=0.4)
    parser.add_argument("--r2-weight", type=float, default=0.3)
    parser.add_argument("--r3-weight", type=float, default=0.3)
    parser.add_argument("--lora-rank", type=int, default=64)
    parser.add_argument("--num-rollouts", type=int, default=4)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--learning-rate", type=float, default=1e-5)
    parser.add_argument("--total-steps", type=int, default=5000)
    parser.add_argument("--recalib-interval", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--wandb-project", default="")
    parser.add_argument("--wandb-run-name", default="")
    args = parser.parse_args()

    config = DCGRPOConfig(
        model_path=args.model_path,
        directions_path=args.directions_path,
        data_path=args.data_path,
        eval_data_path=args.eval_data_path,
        output_dir=args.output_dir,
        target_layers=args.target_layers,
        reward_weights={
            "r1": args.r1_weight,
            "r2": args.r2_weight,
            "r3": args.r3_weight,
        },
        lora_rank=args.lora_rank,
        num_rollouts=args.num_rollouts,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        total_steps=args.total_steps,
        recalib_interval=args.recalib_interval,
        seed=args.seed,
        wandb_project=args.wandb_project,
        wandb_run_name=args.wandb_run_name,
    )
    config.validate()

    trainer = build_trainer_from_config(config)
    trainer.train(
        dataset=None,  # TODO: load from config.data_path
        eval_dataset=None,  # TODO: load from config.eval_data_path
    )


if __name__ == "__main__":
    main()
