"""
TaxEI Injection Base Module
===========================
Defines the InjectionOperator ABC, ErrorInjectMemory (extends verl-agent SimpleMemory),
and ErrorInjectEnvManager (extends AlfWorldEnvironmentManager).

Key design decision: verl-agent has NO explicit plan state. "Planning" errors (P1/P2)
are injected by tampering with the action-observation history so the agent faces
state inconsistencies — it must recognize and recover from corrupted history.

Dependencies:
    - verl-agent at /root/autodl-tmp/verl-agent/
      (agent_system.memory.memory.SimpleMemory)
      (agent_system.environments.env_manager.AlfWorldEnvironmentManager)
"""
from __future__ import annotations

import copy
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

# verl-agent on the training server
VERL_AGENT_PATH = "/root/autodl-tmp/verl-agent"
if VERL_AGENT_PATH not in sys.path:
    sys.path.insert(0, VERL_AGENT_PATH)

from agent_system.memory.memory import SimpleMemory
from agent_system.environments.env_manager import AlfWorldEnvironmentManager


# ---------------------------------------------------------------------------
# Injection log entry
# ---------------------------------------------------------------------------
@dataclass
class InjectionRecord:
    env_idx: int
    step_idx: int
    operator_name: str
    before: Any
    after: Any


# ---------------------------------------------------------------------------
# InjectionOperator ABC
# ---------------------------------------------------------------------------
class InjectionOperator(ABC):
    """Base class for all error-injection operators."""

    name: str = "base"
    category: str = "base"  # "planning" | "context"

    @abstractmethod
    def inject(
        self,
        trajectory: List[Dict[str, Any]],
        env_idx: int,
        step_idx: int,
        config: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        """Apply injection to a single trajectory (list of step dicts).

        Returns a *new* list — must not mutate the input.
        """
        ...

    @abstractmethod
    def validate(
        self,
        original: List[Dict[str, Any]],
        modified: List[Dict[str, Any]],
    ) -> bool:
        """Check post-injection trajectory is still structurally legal."""
        ...

    def describe(self) -> str:
        return f"[{self.category}] {self.name}"


# ---------------------------------------------------------------------------
# ErrorInjectMemory
# ---------------------------------------------------------------------------
class ErrorInjectMemory(SimpleMemory):
    """Memory that applies injection operators before returning history.

    Wraps SimpleMemory.fetch() — after the parent builds the history
    string, each active injector is applied to the underlying _data
    before formatting.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.injectors: List[InjectionOperator] = []
        self.inject_config: Dict[str, Any] = {}
        self._injection_log: List[InjectionRecord] = []

    def register(self, operator: InjectionOperator) -> None:
        self.injectors.append(operator)

    def reset(self, batch_size: int) -> None:
        super().reset(batch_size)
        self._injection_log = []

    def fetch(
        self,
        history_length: int,
        obs_key: str = "text_obs",
        action_key: str = "action",
    ) -> Tuple[List[str], List[int]]:
        """Fetch history with injections applied.

        For each env, copies the raw history, runs every active injector,
        then delegates to the parent formatter.
        """
        # Snapshot original data, apply injections on a copy
        original_data = [list(env_hist) for env_hist in self._data]
        injected_data = [copy.deepcopy(env_hist) for env_hist in self._data]

        for env_idx in range(self.batch_size):
            traj = injected_data[env_idx]
            if not traj:
                continue
            for op in self.injectors:
                op_conf = self.inject_config.get(op.name, {})
                if not op_conf.get("enabled", True):
                    continue
                step_idx = len(traj) - 1
                before = copy.deepcopy(traj)
                traj = op.inject(traj, env_idx, step_idx, op_conf)
                if op.validate(before, traj):
                    self._injection_log.append(
                        InjectionRecord(
                            env_idx=env_idx,
                            step_idx=step_idx,
                            operator_name=op.name,
                            before=before,
                            after=copy.deepcopy(traj),
                        )
                    )
            injected_data[env_idx] = traj

        # Temporarily swap data, call parent fetch, then restore
        self._data = injected_data
        result = super().fetch(history_length, obs_key, action_key)
        self._data = original_data
        return result

    def get_injection_log(self) -> List[InjectionRecord]:
        return list(self._injection_log)


# ---------------------------------------------------------------------------
# ErrorInjectEnvManager
# ---------------------------------------------------------------------------
class ErrorInjectEnvManager(AlfWorldEnvironmentManager):
    """EnvManager that uses ErrorInjectMemory and supports obs-level injection.

    - Observation masking (C4) is applied in step().
    - Context truncation (C1) is applied via ErrorInjectMemory.fetch()
      (called internally by build_text_obs through the memory).
    """

    def __init__(self, envs, projection_f, config):
        super().__init__(envs, projection_f, config)
        self.memory = ErrorInjectMemory()
        self._obs_injectors: List[InjectionOperator] = []
        self._obs_inject_config: Dict[str, Any] = {}

    def register_memory_injector(self, operator: InjectionOperator) -> None:
        self.memory.register(operator)

    def register_obs_injector(self, operator: InjectionOperator) -> None:
        self._obs_injectors.append(operator)

    def set_inject_config(self, config: Dict[str, Any]) -> None:
        self.memory.inject_config = config
        self._obs_inject_config = config

    def step(self, text_actions: List[str]):
        result = super().step(text_actions)
        obs_dict, rewards, dones, infos = result

        # Apply observation-level injectors (e.g. C4)
        for op in self._obs_injectors:
            op_conf = self._obs_inject_config.get(op.name, {})
            if not op_conf.get("enabled", True):
                continue
            text_obs_list = obs_dict["text"]
            for env_idx in range(len(text_obs_list)):
                original = [{"text_obs": text_obs_list[env_idx]}]
                modified = op.inject(original, env_idx, 0, op_conf)
                obs_dict["text"][env_idx] = modified[0]["text_obs"]

        return obs_dict, rewards, dones, infos
