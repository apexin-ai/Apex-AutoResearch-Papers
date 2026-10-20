"""
TaxEI Context Injection Operators: C1 (Context Truncation), C4 (Observation Masking)
====================================================================================
C1: Truncates early history, keeping only recent N steps (N < normal history_length).
    Implemented at the memory level — reduces effective history_length before fetch.

C4: Replaces an observation with empty or generic text.
    Implemented at the env-manager level — modifies text_obs after step().
"""
from __future__ import annotations

import copy
import math
import random
from typing import Any, Dict, List

from .base import InjectionOperator


class C1_ContextTruncation(InjectionOperator):
    """Truncate trajectory history to simulate lost context.

    Removes early steps so the agent only sees the most recent portion
    of its history, losing earlier context that may be needed for planning.
    """

    name = "C1_context_truncation"
    category = "context"

    def inject(
        self,
        trajectory: List[Dict[str, Any]],
        env_idx: int,
        step_idx: int,
        config: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        traj = copy.deepcopy(trajectory)
        if len(traj) <= 1:
            return traj

        ratio = config.get("truncation_ratio", 0.5)
        ratio = max(0.3, min(0.7, ratio))
        keep_count = max(1, math.ceil(len(traj) * ratio))
        return traj[-keep_count:]

    def validate(
        self,
        original: List[Dict[str, Any]],
        modified: List[Dict[str, Any]],
    ) -> bool:
        return len(modified) >= 1


GENERIC_OBS = "You see nothing special."


class C4_ObservationMasking(InjectionOperator):
    """Mask observations with empty or generic text.

    Applied per-step with a configurable probability. The agent must
    act with degraded perception — partial observability injection.
    """

    name = "C4_observation_masking"
    category = "context"

    def inject(
        self,
        trajectory: List[Dict[str, Any]],
        env_idx: int,
        step_idx: int,
        config: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        traj = copy.deepcopy(trajectory)
        if len(traj) <= 1:
            return traj
        mask_type = config.get("mask_type", "generic")
        max_masks = config.get("max_masks", 2)

        # Skip step 0 (initial observation is critical for task understanding)
        eligible = list(range(1, len(traj)))
        num_masks = min(max_masks, len(eligible))
        chosen = random.sample(eligible, num_masks)

        replacement = "" if mask_type == "empty" else GENERIC_OBS
        for idx in chosen:
            traj[idx]["text_obs"] = replacement

        return traj

    def validate(
        self,
        original: List[Dict[str, Any]],
        modified: List[Dict[str, Any]],
    ) -> bool:
        return all(isinstance(s.get("text_obs", ""), str) for s in modified)
