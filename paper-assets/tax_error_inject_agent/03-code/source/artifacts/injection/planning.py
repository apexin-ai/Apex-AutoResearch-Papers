"""
TaxEI Planning Injection Operators: P1 (Step-Order Swap), P2 (Sub-Goal Deletion)
================================================================================
verl-agent has NO explicit plan state. These operators tamper with the
action-observation *history* so the agent faces temporal/causal inconsistencies.

P1: Swaps two adjacent steps in history → agent sees out-of-order execution record.
P2: Deletes a critical step from history → agent sees a gap in its action record.

The agent must recognize the inconsistency and recover (re-plan, re-execute, etc.).
"""
from __future__ import annotations

import copy
import random
from typing import Any, Dict, List

from .base import InjectionOperator


class P1_StepOrderSwap(InjectionOperator):
    """Swap two adjacent steps in the trajectory history.

    The agent will observe a history where action order doesn't match
    the actual execution sequence, creating a temporal inconsistency.
    """

    name = "P1_step_order_swap"
    category = "planning"

    def inject(
        self,
        trajectory: List[Dict[str, Any]],
        env_idx: int,
        step_idx: int,
        config: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        traj = copy.deepcopy(trajectory)
        if len(traj) < 2:
            return traj

        swap_range = config.get("swap_range", 5)
        # Pick from the most recent `swap_range` steps
        window_start = max(0, len(traj) - swap_range)
        candidates = list(range(window_start, len(traj) - 1))
        if not candidates:
            return traj

        idx = random.choice(candidates)
        traj[idx], traj[idx + 1] = traj[idx + 1], traj[idx]
        return traj

    def validate(
        self,
        original: List[Dict[str, Any]],
        modified: List[Dict[str, Any]],
    ) -> bool:
        return len(original) == len(modified)


class P2_SubGoalDeletion(InjectionOperator):
    """Delete a step from the trajectory history, simulating a missed sub-goal.

    The agent will observe a history with a gap — an executed action is
    missing from the record, causing state inconsistency.
    """

    name = "P2_sub_goal_deletion"
    category = "planning"

    CRITICAL_ACTIONS = {"pick", "put", "heat", "cool", "clean", "use", "open", "close", "toggle"}

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

        strategy = config.get("deletion_strategy", "random")

        if strategy == "critical":
            critical_indices = [
                i for i, step in enumerate(traj)
                if self._is_critical(step.get("action", ""))
            ]
            if critical_indices:
                del_idx = random.choice(critical_indices)
            else:
                del_idx = random.randint(0, len(traj) - 1)
        else:
            del_idx = random.randint(0, len(traj) - 1)

        traj.pop(del_idx)
        return traj

    def validate(
        self,
        original: List[Dict[str, Any]],
        modified: List[Dict[str, Any]],
    ) -> bool:
        return len(modified) >= 1

    @staticmethod
    def _is_critical(action_text: str) -> bool:
        action_lower = action_text.lower()
        return any(kw in action_lower for kw in P2_SubGoalDeletion.CRITICAL_ACTIONS)
