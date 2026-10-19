"""B-IAVR reward computation and Lagrangian dual update."""

from dataclasses import dataclass, field
from typing import List


def biavr_reward(
    verify_t: bool,
    action_changed_t: bool,
    lambda_cost: float,
    alpha: float = 1.0,
) -> float:
    """Compute per-step B-IAVR reward.

    r_step(t) = -lambda * 1[verify_t] + alpha * 1[verify_t AND action_changed_t]

    Args:
        verify_t: Whether the agent chose to verify at step t.
        action_changed_t: Whether self-guidance changed the action (a_pre != a_post).
        lambda_cost: Current Lagrangian multiplier (verification cost).
        alpha: Reward bonus for informative verification.
    """
    if not verify_t:
        return 0.0
    r = -lambda_cost
    if action_changed_t:
        r += alpha
    return r


def lagrangian_update(
    lambda_t: float,
    mean_verify_rate: float,
    beta: float = 0.3,
    eta: float = 0.01,
) -> float:
    """Lagrangian dual variable update.

    lambda_{t+1} = max(0, lambda_t + eta * (mean_verify_rate - beta))

    Args:
        lambda_t: Current lambda value.
        mean_verify_rate: Average verification rate across the batch.
        beta: Target verification rate.
        eta: Learning rate for dual update.
    """
    return max(0.0, lambda_t + eta * (mean_verify_rate - beta))


@dataclass
class BIAVRTracker:
    """Tracks B-IAVR statistics across a training run."""

    lambda_cost: float = 0.1
    alpha: float = 1.0
    beta: float = 0.3
    eta: float = 0.01

    _verify_decisions: List[bool] = field(default_factory=list)
    _action_changed: List[bool] = field(default_factory=list)
    _step_rewards: List[float] = field(default_factory=list)

    def record_step(self, verify: bool, action_changed: bool) -> float:
        """Record a step and return its B-IAVR reward."""
        r = biavr_reward(verify, action_changed, self.lambda_cost, self.alpha)
        self._verify_decisions.append(verify)
        self._action_changed.append(action_changed)
        self._step_rewards.append(r)
        return r

    @property
    def verify_rate(self) -> float:
        if not self._verify_decisions:
            return 0.0
        return sum(self._verify_decisions) / len(self._verify_decisions)

    @property
    def informativeness_rate(self) -> float:
        verified = [(v, c) for v, c in zip(self._verify_decisions, self._action_changed) if v]
        if not verified:
            return 0.0
        return sum(c for _, c in verified) / len(verified)

    @property
    def total_step_reward(self) -> float:
        return sum(self._step_rewards)

    def update_lambda(self) -> float:
        """Update lambda based on current verify rate and reset counters."""
        self.lambda_cost = lagrangian_update(
            self.lambda_cost, self.verify_rate, self.beta, self.eta
        )
        self._verify_decisions.clear()
        self._action_changed.clear()
        self._step_rewards.clear()
        return self.lambda_cost

    def get_metrics(self) -> dict:
        return {
            "biavr/lambda": self.lambda_cost,
            "biavr/verify_rate": self.verify_rate,
            "biavr/informativeness_rate": self.informativeness_rate,
            "biavr/total_step_reward": self.total_step_reward,
            "biavr/n_steps": len(self._verify_decisions),
        }
