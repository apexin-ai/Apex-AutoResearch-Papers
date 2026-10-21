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
import re
from collections import deque
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
    Unwraps PEFT indirection and handles transformers>=5.x where
    model.base_model returns the inner model directly.
    """
    candidate = model
    # PEFT wrapping: model.base_model.model.model.layers
    if hasattr(candidate, "base_model"):
        candidate = candidate.base_model
    if hasattr(candidate, "layers"):
        return candidate.layers
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
        default_factory=lambda: list(range(19, 36))
    )
    reward_position: str = "asst_first"

    r1_weight: float = 1.0
    r2_weight: float = 0.5
    r3_weight: float = 0.3

    r3_model_name: str = "cross-encoder/nli-deberta-v3-base"
    nli_batch_size: int = 16

    r1_scale_factor: float = 1.0

    recalibration_interval: int = 0
    calibration_data_path: str = ""


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
        self._r1_ema: dict[str, dict[str, float]] = {}
        self._ema_alpha: float = 0.3

    def __call__(self, prompts, completions, **kwargs):
        conditions = kwargs.get("condition", ["unknown"] * len(completions))
        pair_ids = kwargs.get("pair_id", [str(i) for i in range(len(completions))])

        t = self.trainer
        if t.d_syc is None:
            logger.warning("d_syc not loaded; returning R3-only rewards")
            r3 = t.compute_r3(completions, conditions)
            return [t._r3_w * s for s in r3]

        tokenizer = t.processing_class
        t._prompt_lengths = [
            len(tokenizer.encode(p, add_special_tokens=False))
            for p in prompts
        ]
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
            completions, conditions, pair_ids, batch_acts,
            self._r1_ema, self._ema_alpha,
        )

        t._reward_step += 1
        step = t._reward_step

        if (t._recalibration_interval > 0
                and step > 0
                and step % t._recalibration_interval == 0):
            t.recalibrate_direction(step)

        if step <= 10:
            import statistics
            for name, values in components.items():
                if values:
                    mu = sum(values) / len(values)
                    sd = statistics.stdev(values) if len(values) > 1 else 0.0
                    logger.info(
                        "[step %d] reward/%s  mean=%.4f  std=%.4f  min=%.4f  max=%.4f",
                        step, name, mu, sd, min(values), max(values),
                    )
            if rewards:
                mu = sum(rewards) / len(rewards)
                sd = statistics.stdev(rewards) if len(rewards) > 1 else 0.0
                logger.info(
                    "[step %d] reward/combined  mean=%.4f  std=%.4f",
                    step, mu, sd,
                )
        else:
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
        self._r1_scale_factor = args.r1_scale_factor
        self._recalibration_interval = args.recalibration_interval
        self._calibration_data_path = args.calibration_data_path

        # Populated after super().__init__
        self.d_syc: torch.Tensor | None = None
        self._act_cache: ActivationCache | None = None
        self._step_acts: list[dict[int, torch.Tensor]] | None = []
        self._nli_model: nn.Module | None = None
        self._nli_tokenizer: Any = None
        self._extraction_failures: int = 0
        self._prompt_lengths: list[int] = []
        self._reward_step: int = 0

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
    # Direction recalibration
    # -----------------------------------------------------------------

    def recalibrate_direction(self, step: int) -> dict:
        """Recalibrate d_syc using current model's activations on calibration data.

        Extracts hidden states from the current (LoRA-adapted) model on the
        original calibration pairs, recomputes d_syc = mean(invalid) - mean(valid),
        and replaces self.d_syc in place. Logs cosine similarity with the previous
        direction and separation AUROC.
        """
        import json

        if not self._calibration_data_path:
            logger.warning("[RECALIB step %d] No calibration_data_path, skipping", step)
            return {}

        logger.info("[RECALIB step %d] Starting direction recalibration...", step)
        old_d_syc = self.d_syc.clone() if self.d_syc is not None else None

        records = []
        with open(self._calibration_data_path) as f:
            for line in f:
                records.append(json.loads(line))
        logger.info("[RECALIB step %d] Loaded %d calibration records", step, len(records))

        tokenizer = self.processing_class
        prompts = []
        conditions = []
        for rec in records:
            msgs = [{"role": t["role"], "content": t["content"]} for t in rec["turns"]]
            try:
                prompt = tokenizer.apply_chat_template(
                    msgs, tokenize=False, add_generation_prompt=True,
                    enable_thinking=False,
                )
            except TypeError:
                prompt = tokenizer.apply_chat_template(
                    msgs, tokenize=False, add_generation_prompt=True,
                )
            prompts.append(prompt)
            conditions.append(rec["condition"])

        unwrapped = (
            self.accelerator.unwrap_model(self.model)
            if hasattr(self, "accelerator") else self.model
        )
        was_training = unwrapped.training
        unwrapped.eval()

        valid_acts: dict[int, list[torch.Tensor]] = {l: [] for l in self._reward_layers}
        invalid_acts: dict[int, list[torch.Tensor]] = {l: [] for l in self._reward_layers}

        batch_size = 4
        for i in range(0, len(prompts), batch_size):
            batch_prompts = prompts[i : i + batch_size]
            batch_conds = conditions[i : i + batch_size]

            self._prompt_lengths = [
                len(tokenizer.encode(p, add_special_tokens=False))
                for p in batch_prompts
            ]
            encoded = tokenizer(
                batch_prompts, padding=True, truncation=True,
                max_length=512, return_tensors="pt",
            ).to(next(unwrapped.parameters()).device)
            positions = self._find_asst_first_positions(encoded.input_ids, tokenizer)

            self._act_cache.clear()
            with torch.no_grad():
                unwrapped(
                    input_ids=encoded.input_ids,
                    attention_mask=encoded.attention_mask,
                )

            for sample_idx, (pos, cond) in enumerate(zip(positions, batch_conds)):
                target = valid_acts if cond == "valid_correction" else invalid_acts
                for layer_idx in self._reward_layers:
                    cached = self._act_cache.cache.get(layer_idx)
                    if cached is not None and sample_idx < cached.shape[0]:
                        target[layer_idx].append(
                            cached[sample_idx, pos].float().cpu()
                        )
            self._act_cache.clear()

        new_d_syc = self.d_syc.clone()
        cosine_sims = []
        direction_norms = []

        for layer_idx in self._reward_layers:
            if not valid_acts[layer_idx] or not invalid_acts[layer_idx]:
                continue
            mean_valid = torch.stack(valid_acts[layer_idx]).mean(dim=0)
            mean_invalid = torch.stack(invalid_acts[layer_idx]).mean(dim=0)
            direction = mean_invalid - mean_valid
            norm = direction.norm().item()
            direction_norms.append(norm)
            if norm > 0:
                direction = direction / direction.norm()

            if old_d_syc is not None:
                cos = F.cosine_similarity(
                    old_d_syc[layer_idx, self._pos_idx].float().unsqueeze(0),
                    direction.unsqueeze(0),
                ).item()
                cosine_sims.append(cos)

            new_d_syc[layer_idx, self._pos_idx] = direction

        auroc = self._recalib_auroc(valid_acts, invalid_acts, new_d_syc)
        mean_cos = sum(cosine_sims) / len(cosine_sims) if cosine_sims else 0.0
        mean_norm = sum(direction_norms) / len(direction_norms) if direction_norms else 0.0

        if mean_cos < 0.3:
            logger.warning(
                "[RECALIB step %d] Direction drastically changed! "
                "mean_cosine=%.4f — updating anyway to let training adapt",
                step, mean_cos,
            )

        self.d_syc = new_d_syc

        if was_training:
            unwrapped.train()

        logger.info(
            "[RECALIB step %d] cosine_sim=%.4f, auroc=%.4f, direction_norm=%.4f",
            step, mean_cos, auroc, mean_norm,
        )
        return {"cosine_sim": mean_cos, "auroc": auroc, "step": step}

    def _recalib_auroc(
        self,
        valid_acts: dict[int, list[torch.Tensor]],
        invalid_acts: dict[int, list[torch.Tensor]],
        d_syc: torch.Tensor,
    ) -> float:
        """AUROC of separating valid vs invalid using mean dot product across layers."""
        scores: list[float] = []
        labels: list[int] = []
        mean_d = torch.stack(
            [d_syc[l, self._pos_idx].float() for l in self._reward_layers]
        ).mean(0)
        n_valid = len(valid_acts[self._reward_layers[0]])
        n_invalid = len(invalid_acts[self._reward_layers[0]])

        for i in range(n_valid):
            vecs = [valid_acts[l][i] for l in self._reward_layers if i < len(valid_acts[l])]
            if vecs:
                mean_h = torch.stack(vecs).mean(0)
                scores.append(torch.dot(mean_h, mean_d).item())
                labels.append(0)
        for i in range(n_invalid):
            vecs = [invalid_acts[l][i] for l in self._reward_layers if i < len(invalid_acts[l])]
            if vecs:
                mean_h = torch.stack(vecs).mean(0)
                scores.append(torch.dot(mean_h, mean_d).item())
                labels.append(1)

        if not scores or sum(labels) == 0 or sum(labels) == len(labels):
            return 0.0
        paired = sorted(zip(scores, labels), reverse=True)
        tp, auc_sum = 0, 0.0
        p_total = sum(labels)
        n_total = len(labels) - p_total
        for _, label in paired:
            if label == 1:
                tp += 1
            else:
                auc_sum += tp
        return auc_sum / (p_total * n_total) if (p_total * n_total) > 0 else 0.0

    # -----------------------------------------------------------------
    # NLI model (lazy)
    # -----------------------------------------------------------------

    def _ensure_nli_model(self) -> None:
        """Lazy-load DeBERTa NLI model for R3 scoring."""
        if self._nli_model is not None:
            return
        from transformers import AutoModelForSequenceClassification

        try:
            from transformers import DebertaV2Tokenizer
            self._nli_tokenizer = DebertaV2Tokenizer.from_pretrained(
                self._r3_model_name
            )
        except Exception:
            from transformers import AutoTokenizer
            self._nli_tokenizer = AutoTokenizer.from_pretrained(
                self._r3_model_name
            )

        self._nli_model = (
            AutoModelForSequenceClassification.from_pretrained(self._r3_model_name)
            .eval()
        )
        id2label = getattr(self._nli_model.config, "id2label", {})
        self._entailment_idx = 2
        for idx, label in id2label.items():
            if "entail" in str(label).lower():
                self._entailment_idx = int(idx)
                break
        logger.info(
            "Loaded NLI model: %s (entailment_idx=%d)",
            self._r3_model_name, self._entailment_idx,
        )

    # -----------------------------------------------------------------
    # Position finding
    # -----------------------------------------------------------------

    def _find_asst_first_positions(
        self,
        input_ids: torch.Tensor,
        tokenizer: Any,
    ) -> list[int]:
        """Locate asst_first position using tokenize-based method.

        Matches extract_activations_v2.py: asst_first = len(prompt_tokens) - 1,
        the last prompt token whose hidden state predicts the first generated
        content token. Uses self._prompt_lengths when available (set by
        generate_completions or _DCRewardCallable before calling this method).
        Falls back to scanning for the <|im_start|> assistant marker.
        """
        positions: list[int] = []
        for i in range(input_ids.shape[0]):
            seq_len = input_ids.shape[1]
            if self._prompt_lengths and i < len(self._prompt_lengths):
                pos = self._prompt_lengths[i] - 1
            else:
                im_start_id = tokenizer.convert_tokens_to_ids("<|im_start|>")
                ids_list = input_ids[i].tolist()
                pos = seq_len - 1
                for j in range(len(ids_list) - 1, -1, -1):
                    if ids_list[j] == im_start_id:
                        candidate = j + 2
                        if candidate < seq_len:
                            pos = candidate
                        break
            positions.append(min(pos, seq_len - 1))
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
            d = self.d_syc[layer_idx, self._pos_idx].to(h)
            h_norm = torch.norm(h).item() + 1e-8
            cos_sim = torch.dot(h, d).item() / h_norm
            scores.append(sign * cos_sim)

        if not scores:
            return 0.0
        return self._r1_scale_factor * sum(scores) / len(scores)

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
        r1_ema: dict[str, dict[str, float]] | None = None,
        ema_alpha: float = 0.3,
    ) -> list[float]:
        """R2 for all completions, using cross-step EMA for pairing.

        GRPO batch_size=1 means each step only sees one condition per pair.
        An exponential moving average of R1 per (pair_id, condition) enables
        cross-step pairing. R2 activates after both conditions have been seen.

        Args:
            r1_scores: R1 per completion (same order as conditions/pair_ids).
            conditions: Per-completion condition label.
            pair_ids: Per-completion pair identifier.
            r1_ema: Cross-step R1 EMA dict, updated in place.
            ema_alpha: Weight for new values (0.3 = 30% new, 70% history).

        Returns:
            List of R2 scores, same length as input.
        """
        if r1_ema is not None:
            for r1, cond, pid in zip(r1_scores, conditions, pair_ids):
                ema = r1_ema.setdefault(pid, {})
                if cond in ema:
                    ema[cond] = ema_alpha * r1 + (1 - ema_alpha) * ema[cond]
                else:
                    ema[cond] = r1

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
            elif r1_ema is not None and pid in r1_ema:
                ema = r1_ema[pid]
                ema_v = ema.get("valid_correction")
                ema_i = ema.get("invalid_pressure")
                if ema_v is not None and ema_i is not None:
                    r2_scores.append(self.compute_r2(ema_v, ema_i))
                else:
                    r2_scores.append(0.0)
            else:
                r2_scores.append(0.0)
        return r2_scores

    # -----------------------------------------------------------------
    # R3: Behavioral NLI
    # -----------------------------------------------------------------

    @staticmethod
    def _extract_last_response(text: str) -> str:
        """Extract last assistant response from completion, strip special tokens."""
        clean = re.sub(
            r"<\|im_start\|>|<\|im_end\|>|<think>|</think>|<\|endoftext\|>",
            "",
            text,
        )
        parts = clean.split("assistant")
        response = parts[-1].strip() if len(parts) > 1 else clean.strip()
        if len(response) > 1000:
            response = response[:1000]
        return response if response else text[:500]

    def compute_r3(
        self,
        completions: list[str],
        conditions: list[str],
    ) -> list[float]:
        """Factual NLI reward using inverted scoring for invalid_pressure.

        Both conditions use the same hypothesis ("response changes/corrects
        the answer"). For valid_correction, high entailment = high R3 (model
        correctly revised). For invalid_pressure, the score is inverted:
        low entailment = model held firm = high R3.

        Args:
            completions: Generated response texts.
            conditions: Per-completion condition labels.

        Returns:
            List of R3 scores in [0, 1].
        """
        self._ensure_nli_model()

        hypothesis = "The response changes or corrects the previous answer."
        premises: list[str] = []
        invert: list[bool] = []
        for text, cond in zip(completions, conditions):
            premises.append(self._extract_last_response(text))
            invert.append(cond == "invalid_pressure")

        raw_scores: list[float] = []
        for i in range(0, len(premises), self._nli_batch_size):
            batch_p = premises[i : i + self._nli_batch_size]
            batch_h = [hypothesis] * len(batch_p)
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
                raw_scores.extend(probs[:, self._entailment_idx].tolist())

        return [1.0 - s if inv else s for s, inv in zip(raw_scores, invert)]

    # -----------------------------------------------------------------
    # Combined reward
    # -----------------------------------------------------------------

    def compute_rewards(
        self,
        completions: list[str],
        conditions: list[str],
        pair_ids: list[str],
        batch_activations: list[dict[int, torch.Tensor]],
        r1_ema: dict[str, dict[str, float]] | None = None,
        ema_alpha: float = 0.3,
    ) -> tuple[list[float], dict[str, list[float]]]:
        """Compute combined R = w1*R1 + w2*R2 + w3*R3 for a batch.

        Args:
            completions: Generated response texts.
            conditions: Per-completion condition labels.
            pair_ids: Per-completion pair identifiers for R2 pairing.
            batch_activations: Per-completion activation dicts from
                _extract_activations.
            r1_ema: Cross-step R1 EMA for R2 pairing.
            ema_alpha: EMA decay weight.

        Returns:
            (combined_rewards, component_dict) where component_dict maps
            "r1", "r2", "r3" to their respective score lists.
        """
        r1 = self.compute_r1_batch(batch_activations, conditions)
        r2 = self.compute_r2_for_group(r1, conditions, pair_ids, r1_ema, ema_alpha)
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
        tokenizer = self.processing_class
        if isinstance(prompts, (list, tuple)) and len(prompts) > 0:
            if isinstance(prompts[0], str):
                self._prompt_lengths = [
                    len(tokenizer.encode(p, add_special_tokens=False))
                    for p in prompts
                ]
            elif isinstance(prompts[0], torch.Tensor):
                pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id
                self._prompt_lengths = [
                    (p != pad_id).sum().item() for p in prompts
                ]

        completions = super().generate_completions(prompts, **kwargs)

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
                self._extraction_failures = 0
        except Exception as e:
            self._step_acts = None
            self._extraction_failures += 1
            logger.warning(
                "Activation extraction failed (attempt %d): %s",
                self._extraction_failures,
                e,
            )
            if self._extraction_failures >= 10:
                raise RuntimeError(
                    "Activation extraction failed 10 consecutive times, aborting training"
                ) from e

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
        if self._step_acts is None:
            logger.warning(
                "step_acts is None (extraction failed); returning zero rewards"
            )
            return [0.0] * len(completions)

        batch_acts = self._step_acts if self._step_acts else [{}] * len(completions)

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
