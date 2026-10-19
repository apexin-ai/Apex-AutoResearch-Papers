"""DCGRPOTrainer: Direction-Contrastive GRPO for sycophancy calibration.

Inherits trl.GRPOTrainer, overrides reward computation to inject three signals:
  R1 (Direction Alignment)     -- dot(h, d_syc) at critical-turn hidden state
  R2 (Contrastive Consistency) -- sigmoid(R1_valid - R1_invalid) - 0.5
  R3 (Behavioral NLI)          -- DeBERTa entailment probability

Overrides completion generation to support multi-turn dialogue with activation caching.

Input:  Dataset with columns: prompt (3-turn dialogue), condition, pair_id
Output: LoRA-tuned policy model with reduced sycophantic capitulation

Dependencies: trl>=0.15, transformers>=4.45, peft, torch
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

import torch
import torch.nn as nn
import torch.nn.functional as F
from trl import GRPOConfig, GRPOTrainer

logger = logging.getLogger(__name__)


# =====================================================================
# Activation Cache
# =====================================================================

def _resolve_transformer_layers(model: nn.Module) -> nn.ModuleList:
    """Find transformer decoder layers, handling PEFT wrappers.

    Supports Qwen/Llama/Mistral (model.model.layers layout).
    Unwraps one PEFT indirection level if present.
    """
    candidate = model
    if hasattr(candidate, "base_model"):
        candidate = candidate.base_model
    if hasattr(candidate, "model"):
        inner = candidate.model
        if hasattr(inner, "layers"):
            return inner.layers
        if hasattr(inner, "model") and hasattr(inner.model, "layers"):
            return inner.model.layers
    raise AttributeError(
        f"Cannot locate transformer layers on {type(model).__name__}. "
        "Expected model.model.layers or model.base_model.model.model.layers."
    )


class ActivationCache:
    """Forward hook to cache hidden states at specified layers during generation."""

    def __init__(self, target_layers: list[int]):
        self.target_layers = set(target_layers)
        self.cache: dict[int, torch.Tensor] = {}
        self.hooks: list = []

    def register(self, model: nn.Module) -> None:
        """Attach forward hooks to target transformer layers."""
        self.remove()
        layers = _resolve_transformer_layers(model)
        for idx in sorted(self.target_layers):
            if idx >= len(layers):
                raise ValueError(
                    f"Layer {idx} out of range (model has {len(layers)} layers)"
                )
            self.hooks.append(
                layers[idx].register_forward_hook(self._make_hook(idx))
            )
        logger.info(
            "Activation hooks registered on layers %s", sorted(self.target_layers)
        )

    def _make_hook(self, layer_idx: int):
        def fn(module, input, output):
            hidden = output[0] if isinstance(output, tuple) else output
            self.cache[layer_idx] = hidden.detach()
        return fn

    def clear(self):
        self.cache = {}

    def remove(self):
        for h in self.hooks:
            h.remove()
        self.hooks.clear()
        self.cache.clear()


# =====================================================================
# Configuration
# =====================================================================

@dataclass
class DCGRPOConfig(GRPOConfig):
    """GRPOConfig extended with DC-GRPO reward and direction parameters.

    Additional fields control the direction-contrastive reward mechanism:
    direction_path points to directions.pt from compute_directions.py,
    reward_layers selects which transformer layers to probe (default 19-27,
    the highest-AUROC range from MVP), and r1/r2/r3 weights set the
    relative contribution of each reward component.
    """

    direction_path: str = ""
    reward_layers: list[int] = field(
        default_factory=lambda: list(range(19, 28))
    )
    reward_position: str = "asst_first"

    r1_weight: float = 1.0
    r2_weight: float = 0.5
    r3_weight: float = 0.3

    r3_model_name: str = "microsoft/deberta-v3-base"
    nli_batch_size: int = 16


# =====================================================================
# Placeholder reward for GRPOTrainer constructor
# =====================================================================

def _noop_reward_fn(completions: list[str], **kwargs) -> list[float]:
    """Placeholder passed to super().__init__; actual rewards computed in override."""
    return [0.0] * len(completions)


class _DCRewardCallable:
    """Callable that computes combined R1+R2+R3 DC-GRPO rewards.

    Plugged into TRL's reward_funcs after super().__init__. Receives prompts,
    completions, and dataset columns (condition, pair_id) from TRL's
    _calculate_rewards via **reward_kwargs. Runs a forward pass with hooks
    to extract activations for R1/R2.
    """

    __name__ = "dc_grpo_reward"

    def __init__(self, trainer: "DCGRPOTrainer"):
        self.trainer = trainer

    def __call__(self, prompts, completions, **kwargs):
        conditions = kwargs.get("condition", ["unknown"] * len(completions))
        pair_ids = kwargs.get("pair_id", [str(i) for i in range(len(completions))])

        t = self.trainer
        if t.d_syc is None:
            logger.warning("d_syc not loaded; returning R3-only rewards")
            r3 = t.compute_r3(completions, conditions)
            return [t._r3_w * s for s in r3]

        tokenizer = t.processing_class
        full_texts = [p + c for p, c in zip(prompts, completions)]
        encoded = tokenizer(
            full_texts,
            padding=True,
            truncation=True,
            return_tensors="pt",
        ).to(t.model.device)
        positions = t._find_asst_first_positions(encoded.input_ids, tokenizer)
        batch_acts = t._extract_activations(
            encoded.input_ids, encoded.attention_mask, positions
        )

        rewards, components = t.compute_rewards(
            completions, conditions, pair_ids, batch_acts
        )

        for name, values in components.items():
            if values:
                logger.info("reward/%s_mean=%.4f", name, sum(values) / len(values))
        if rewards:
            logger.info(
                "reward/combined_mean=%.4f", sum(rewards) / len(rewards)
            )

        return rewards


# =====================================================================
# DCGRPOTrainer
# =====================================================================

class DCGRPOTrainer(GRPOTrainer):
    """Direction-Contrastive GRPO trainer for sycophancy calibration.

    Reward signals:
      R1 = sign(condition) * dot(h, d_syc)         (direction alignment)
      R2 = sigmoid(R1_valid - R1_invalid) - 0.5    (contrastive consistency)
      R3 = NLI_entailment(completion, expected)     (behavioral appropriateness)
      R  = w1*R1 + w2*R2 + w3*R3

    Data flow:
      generate_completions() caches activations via forward hooks.
      compute_rewards() reads cached activations for R1/R2, runs NLI for R3.

    Expected dataset columns beyond "prompt":
      condition  -- "valid_correction" or "invalid_pressure"
      pair_id    -- links the two conditions of the same calibration pair
    """

    def __init__(
        self,
        model: str | nn.Module,
        args: DCGRPOConfig,
        train_dataset: Any,
        eval_dataset: Any | None = None,
        processing_class: Any | None = None,
        peft_config: Any | None = None,
        **kwargs,
    ):
        # Store config before super().__init__ (which sets self.model)
        self._direction_path = args.direction_path
        self._reward_layers = args.reward_layers
        self._pos_idx = 1 if args.reward_position == "asst_first" else 0
        self._r1_w = args.r1_weight
        self._r2_w = args.r2_weight
        self._r3_w = args.r3_weight
        self._r3_model_name = args.r3_model_name
        self._nli_batch_size = args.nli_batch_size

        # Populated after super().__init__
        self.d_syc: torch.Tensor | None = None
        self._act_cache: ActivationCache | None = None
        self._step_acts: list[dict[int, torch.Tensor]] = []
        self._nli_model: nn.Module | None = None
        self._nli_tokenizer: Any = None

        super().__init__(
            model=model,
            reward_funcs=[_noop_reward_fn],
            args=args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            processing_class=processing_class,
            peft_config=peft_config,
            **kwargs,
        )

        # Post-init: self.model now exists
        self._load_directions()
        self._act_cache = ActivationCache(self._reward_layers)
        self._act_cache.register(self.model)

        # Replace noop placeholder with actual DC-GRPO reward function
        self.reward_funcs = [_DCRewardCallable(self)]
        if hasattr(self, "reward_func_names"):
            self.reward_func_names = ["dc_grpo_reward"]

    # -----------------------------------------------------------------
    # Direction loading
    # -----------------------------------------------------------------

    def _load_directions(self) -> None:
        """Load d_syc direction vectors from directions.pt."""
        if not self._direction_path:
            logger.warning("No direction_path provided; R1/R2 will return 0.0")
            return
        data = torch.load(
            self._direction_path, map_location="cpu", weights_only=True
        )
        self.d_syc = data["d_syc"]  # (num_layers, 2, hidden_dim)
        logger.info(
            "Loaded d_syc shape=%s from %s",
            self.d_syc.shape,
            self._direction_path,
        )

    def reload_directions(self, path: str) -> None:
        """Hot-reload directions after periodic recalibration.

        Logs a warning per layer if cosine similarity between old and new
        directions drops below 0.7 (potential direction drift under LoRA).
        """
        old_d = self.d_syc
        self._direction_path = path
        self._load_directions()

        if old_d is not None and self.d_syc is not None:
            for layer_idx in self._reward_layers:
                if layer_idx >= min(old_d.shape[0], self.d_syc.shape[0]):
                    continue
                cos = F.cosine_similarity(
                    old_d[layer_idx, self._pos_idx].unsqueeze(0),
                    self.d_syc[layer_idx, self._pos_idx].unsqueeze(0),
                ).item()
                if cos < 0.7:
                    logger.warning(
                        "Direction drift at layer %d: cosine=%.3f", layer_idx, cos
                    )

    # -----------------------------------------------------------------
    # NLI model (lazy)
    # -----------------------------------------------------------------

    def _ensure_nli_model(self) -> None:
        """Lazy-load DeBERTa NLI model for R3 scoring."""
        if self._nli_model is not None:
            return
        from transformers import (
            AutoModelForSequenceClassification,
            AutoTokenizer,
        )

        self._nli_tokenizer = AutoTokenizer.from_pretrained(self._r3_model_name)
        self._nli_model = (
            AutoModelForSequenceClassification.from_pretrained(self._r3_model_name)
            .eval()
        )
        logger.info("Loaded NLI model: %s", self._r3_model_name)

    # -----------------------------------------------------------------
    # Position finding
    # -----------------------------------------------------------------

    def _find_asst_first_positions(
        self,
        input_ids: torch.Tensor,
        tokenizer: Any,
    ) -> list[int]:
        """Locate the first content token of the final assistant turn.

        Scans each sequence for the last assistant-turn delimiter in the
        decoded text, then maps back to token position. Falls back to the
        last token if no marker is found.

        The marker is chat-template-specific. Currently targets Qwen3
        (<|im_start|>assistant). For other templates, override this method.
        """
        marker = "<|im_start|>assistant\n"
        positions: list[int] = []
        for i in range(input_ids.shape[0]):
            seq = input_ids[i]
            text = tokenizer.decode(seq, skip_special_tokens=False)
            idx = text.rfind(marker)
            if idx >= 0:
                prefix = text[: idx + len(marker)]
                pos = len(tokenizer.encode(prefix, add_special_tokens=False))
                pos = min(pos, seq.shape[0] - 1)
            else:
                pos = seq.shape[0] - 1
            positions.append(pos)
        return positions

    # -----------------------------------------------------------------
    # Activation extraction
    # -----------------------------------------------------------------

    def _extract_activations(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        positions: list[int],
    ) -> list[dict[int, torch.Tensor]]:
        """Forward pass to extract hidden states at asst_first positions.

        Runs the full sequence through the model with hooks enabled, then
        reads the cached hidden state at each sample's designated position.
        This is a separate pass from generation (generate() uses KV cache
        and only exposes the latest-token hidden state per step).

        Args:
            input_ids: (batch, seq_len) full sequences (prompt + completion).
            attention_mask: (batch, seq_len).
            positions: Per-sample token position for extraction.

        Returns:
            List of per-sample dicts: {layer_idx: Tensor(hidden_dim,)}.
        """
        self._act_cache.clear()
        with torch.no_grad():
            self.model(input_ids=input_ids, attention_mask=attention_mask)

        batch_acts: list[dict[int, torch.Tensor]] = []
        for sample_idx, pos in enumerate(positions):
            acts: dict[int, torch.Tensor] = {}
            for layer_idx in self._reward_layers:
                cached = self._act_cache.cache.get(layer_idx)
                if cached is not None:
                    acts[layer_idx] = cached[sample_idx, pos]
            batch_acts.append(acts)

        self._act_cache.clear()
        return batch_acts

    # -----------------------------------------------------------------
    # R1: Direction Alignment
    # -----------------------------------------------------------------

    def compute_r1(
        self,
        activations: dict[int, torch.Tensor],
        condition: str,
    ) -> float:
        """Direction alignment reward for a single completion.

        R1 = +dot(h, d_syc) for valid_correction   (reward genuine revision)
        R1 = -dot(h, d_syc) for invalid_pressure    (penalize capitulation)

        Direction vectors are L2-normalized per the compute_directions.py
        convention, so dot product magnitude scales with activation norm
        (stronger internal signal produces stronger reward).
        Averaged across all reward_layers.

        Args:
            activations: {layer_idx: Tensor(hidden_dim,)} at asst_first position.
            condition: "valid_correction" or "invalid_pressure".

        Returns:
            Scalar R1 reward.
        """
        if self.d_syc is None:
            return 0.0

        sign = 1.0 if condition == "valid_correction" else -1.0
        scores: list[float] = []
        for layer_idx in self._reward_layers:
            h = activations.get(layer_idx)
            if h is None:
                continue
            d = self.d_syc[layer_idx, self._pos_idx].to(h.device)
            scores.append(sign * torch.dot(h, d).item())

        return sum(scores) / len(scores) if scores else 0.0

    def compute_r1_batch(
        self,
        batch_activations: list[dict[int, torch.Tensor]],
        conditions: list[str],
    ) -> list[float]:
        """R1 for a batch of completions."""
        return [
            self.compute_r1(acts, cond)
            for acts, cond in zip(batch_activations, conditions)
        ]

    # -----------------------------------------------------------------
    # R2: Contrastive Consistency
    # -----------------------------------------------------------------

    def compute_r2(self, r1_valid: float, r1_invalid: float) -> float:
        """Rank-based contrastive reward for a condition pair.

        R2 = sigmoid(R1_valid - R1_invalid) - 0.5

        Positive when valid_correction R1 exceeds invalid_pressure R1 within
        the same calibration pair. S1 rank-based design avoids the
        d_gen = -d_syc degeneracy (see skeleton section 8).

        Args:
            r1_valid: R1 from the valid_correction completion.
            r1_invalid: R1 from the invalid_pressure completion.

        Returns:
            Scalar R2 in (-0.5, 0.5).
        """
        return torch.sigmoid(torch.tensor(r1_valid - r1_invalid)).item() - 0.5

    def compute_r2_for_group(
        self,
        r1_scores: list[float],
        conditions: list[str],
        pair_ids: list[str],
    ) -> list[float]:
        """R2 for all completions in a training step, paired by pair_id.

        Aggregates mean R1 per (pair_id, condition), then applies R2.
        All completions from the same pair receive the same R2 score.
        Completions without a paired counterpart get R2 = 0.

        Args:
            r1_scores: R1 per completion (same order as conditions/pair_ids).
            conditions: Per-completion condition label.
            pair_ids: Per-completion pair identifier.

        Returns:
            List of R2 scores, same length as input.
        """
        # Aggregate R1 by (pair_id, condition)
        pair_r1: dict[str, dict[str, list[float]]] = {}
        for r1, cond, pid in zip(r1_scores, conditions, pair_ids):
            pair_r1.setdefault(pid, {}).setdefault(cond, []).append(r1)

        pair_means: dict[str, dict[str, float]] = {}
        for pid, cond_map in pair_r1.items():
            pair_means[pid] = {
                c: sum(vs) / len(vs) for c, vs in cond_map.items()
            }

        r2_scores: list[float] = []
        for cond, pid in zip(conditions, pair_ids):
            means = pair_means.get(pid, {})
            r1_v = means.get("valid_correction")
            r1_i = means.get("invalid_pressure")
            if r1_v is not None and r1_i is not None:
                r2_scores.append(self.compute_r2(r1_v, r1_i))
            else:
                r2_scores.append(0.0)
        return r2_scores

    # -----------------------------------------------------------------
    # R3: Behavioral NLI
    # -----------------------------------------------------------------

    def compute_r3(
        self,
        completions: list[str],
        conditions: list[str],
    ) -> list[float]:
        """Behavioral NLI reward for a batch of completions.

        Constructs (premise, hypothesis) pairs per completion:
          premise:    "The model said: {completion}"
          hypothesis: condition-dependent expected behavior

        R3 = P(entailment) from DeBERTa-v3-base NLI.
        Processed in batches of nli_batch_size. Does not participate
        in gradient computation.

        Args:
            completions: Generated response texts.
            conditions: Per-completion condition labels.

        Returns:
            List of R3 scores (entailment probabilities in [0, 1]).
        """
        self._ensure_nli_model()

        premises: list[str] = []
        hypotheses: list[str] = []
        for text, cond in zip(completions, conditions):
            premises.append(f"The model said: {text}")
            if cond == "valid_correction":
                hypotheses.append(
                    "The model revised its answer after receiving valid correction."
                )
            else:
                hypotheses.append(
                    "The model maintained its answer despite invalid pressure."
                )

        scores: list[float] = []
        for i in range(0, len(premises), self._nli_batch_size):
            batch_p = premises[i : i + self._nli_batch_size]
            batch_h = hypotheses[i : i + self._nli_batch_size]
            inputs = self._nli_tokenizer(
                batch_p,
                batch_h,
                padding=True,
                truncation=True,
                max_length=512,
                return_tensors="pt",
            ).to(self._nli_model.device)

            with torch.no_grad():
                logits = self._nli_model(**inputs).logits
                probs = F.softmax(logits, dim=-1)
                # DeBERTa NLI label order: contradiction=0, neutral=1, entailment=2
                scores.extend(probs[:, 2].tolist())

        return scores

    # -----------------------------------------------------------------
    # Combined reward
    # -----------------------------------------------------------------

    def compute_rewards(
        self,
        completions: list[str],
        conditions: list[str],
        pair_ids: list[str],
        batch_activations: list[dict[int, torch.Tensor]],
    ) -> tuple[list[float], dict[str, list[float]]]:
        """Compute combined R = w1*R1 + w2*R2 + w3*R3 for a batch.

        Args:
            completions: Generated response texts.
            conditions: Per-completion condition labels.
            pair_ids: Per-completion pair identifiers for R2 pairing.
            batch_activations: Per-completion activation dicts from
                _extract_activations.

        Returns:
            (combined_rewards, component_dict) where component_dict maps
            "r1", "r2", "r3" to their respective score lists.
        """
        r1 = self.compute_r1_batch(batch_activations, conditions)
        r2 = self.compute_r2_for_group(r1, conditions, pair_ids)
        r3 = self.compute_r3(completions, conditions)

        combined = [
            self._r1_w * s1 + self._r2_w * s2 + self._r3_w * s3
            for s1, s2, s3 in zip(r1, r2, r3)
        ]

        components = {"r1": r1, "r2": r2, "r3": r3}
        return combined, components

    # -----------------------------------------------------------------
    # GRPOTrainer override: generate_completions
    # -----------------------------------------------------------------

    def generate_completions(self, prompts, **kwargs):
        """Override to cache activations alongside standard generation.

        Multi-turn prompts (3-turn dialogues formatted via chat template)
        are handled natively by the parent's generation logic. After
        completions are produced, a separate forward pass extracts hidden
        states at the asst_first position for R1/R2 computation.

        The extra forward pass adds ~5-10% overhead per training step.
        Cached activations are stored in self._step_acts for retrieval
        in _compute_step_rewards().
        """
        completions = super().generate_completions(prompts, **kwargs)

        tokenizer = self.processing_class
        try:
            if isinstance(prompts, (list, tuple)) and len(prompts) > 0:
                if isinstance(prompts[0], str):
                    comp_texts = (
                        completions
                        if isinstance(completions[0], str)
                        else [tokenizer.decode(c, skip_special_tokens=False) for c in completions]
                    )
                    full_texts = [p + c for p, c in zip(prompts, comp_texts)]
                    encoded = tokenizer(
                        full_texts,
                        padding=True,
                        truncation=True,
                        return_tensors="pt",
                    ).to(self.model.device)
                    input_ids = encoded.input_ids
                    attention_mask = encoded.attention_mask
                elif isinstance(prompts[0], torch.Tensor):
                    comp_ids = (
                        completions
                        if isinstance(completions, torch.Tensor)
                        else torch.stack(completions)
                    )
                    input_ids = torch.cat(
                        [torch.stack(prompts), comp_ids], dim=-1
                    )
                    pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id
                    attention_mask = (input_ids != pad_id).long()
                else:
                    return completions

                positions = self._find_asst_first_positions(
                    input_ids, tokenizer
                )
                self._step_acts = self._extract_activations(
                    input_ids, attention_mask, positions
                )
        except Exception as e:
            logger.warning("Activation extraction in generate_completions failed: %s", e)

        return completions

    # -----------------------------------------------------------------
    # GRPOTrainer integration: step-level reward computation
    # -----------------------------------------------------------------

    def _compute_step_rewards(
        self,
        prompts: list[str],
        completions: list[str],
        conditions: list[str],
        pair_ids: list[str],
    ) -> list[float]:
        """Entry point for per-step reward computation.

        Called during the training loop after generate_completions().
        Reads self._step_acts (populated by generate_completions),
        computes R1+R2+R3, logs component statistics, and clears the cache.

        Wire this into the training loop by having the reward_funcs wrapper
        delegate here, or by overriding _generate_and_score_completions
        (TRL internal method name may vary by version).

        Args:
            prompts: Prompt texts for this step.
            completions: Generated completion texts.
            conditions: Per-completion condition labels from dataset.
            pair_ids: Per-completion pair identifiers from dataset.

        Returns:
            List of combined reward scalars, one per completion.
        """
        batch_acts = (
            self._step_acts if self._step_acts else [{}] * len(completions)
        )

        rewards, components = self.compute_rewards(
            completions, conditions, pair_ids, batch_acts
        )

        for name, values in components.items():
            if values:
                avg = sum(values) / len(values)
                logger.info("reward/%s_mean=%.4f", name, avg)
        if rewards:
            logger.info(
                "reward/combined_mean=%.4f", sum(rewards) / len(rewards)
            )

        self._step_acts.clear()
        return rewards

    # -----------------------------------------------------------------
    # Cleanup
    # -----------------------------------------------------------------

    def cleanup(self) -> None:
        """Remove hooks and free NLI model memory."""
        if self._act_cache is not None:
            self._act_cache.remove()
        self._nli_model = None
        self._nli_tokenizer = None
        torch.cuda.empty_cache()
