"""Discrete-time PI controller for collapse-aware real/synthetic data mixing.

Adjusts the real data ratio w_t based on spectral effective rank signal,
increasing real data when rank drops (collapse risk) and decreasing it
when rank recovers.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ControllerConfig:
    Kp: float = 0.01
    Ki: float = 0.005
    r_target: float = 0.0
    w_init: float = 0.5
    w_min: float = 0.1
    w_max: float = 0.9


class CollapseAwareController:
    def __init__(self, config: ControllerConfig):
        self.config = config
        self._w: float = config.w_init
        self._r_prev: Optional[float] = None
        self._integral: float = 0.0
        self._proportional: float = 0.0
        self._r_history: List[float] = []
        self._w_history: List[float] = [config.w_init]
        self._step_count: int = 0

    def step(self, r_t: float) -> float:
        """Given current spectral rank, return updated real data ratio w_t."""
        cfg = self.config

        if self._r_prev is None:
            self._r_prev = r_t
            self._r_history.append(r_t)
            return self._w

        error = r_t - cfg.r_target
        delta_r = r_t - self._r_prev

        # rank drop (negative delta_r / negative error) → increase w
        self._proportional = -cfg.Kp * delta_r
        self._integral += -cfg.Ki * error

        self._w = self._w + self._proportional + (-cfg.Ki * error)

        self._w = max(cfg.w_min, min(cfg.w_max, self._w))

        self._r_prev = r_t
        self._r_history.append(r_t)
        self._w_history.append(self._w)
        self._step_count += 1

        return self._w

    def get_state(self) -> dict:
        """Return controller internals."""
        return {
            "w": self._w,
            "proportional_term": self._proportional,
            "integral_term": self._integral,
            "r_history": list(self._r_history),
            "w_history": list(self._w_history),
            "step_count": self._step_count,
        }

    def reset(self):
        """Reset controller state to initial."""
        self._w = self.config.w_init
        self._r_prev = None
        self._integral = 0.0
        self._proportional = 0.0
        self._r_history = []
        self._w_history = [self.config.w_init]
        self._step_count = 0
