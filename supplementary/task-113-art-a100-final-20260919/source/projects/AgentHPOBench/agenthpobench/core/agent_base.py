"""
Base agent interface for AgentHPOBench framework.

All agents must implement the Agent interface to participate in
automatic repository reproduction tasks.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class DecisionContext:
    """Context provided to agent for decision making."""

    training_log: str  # Recent training logs (last N epochs)
    current_config: Dict[str, Any]  # Current hyperparameter configuration
    metrics_history: list  # Historical metrics [(epoch, metrics_dict), ...]
    budget_remaining: int  # Remaining epochs
    total_budget: int  # Total initial budget
    search_space: Dict[str, Any]  # Valid hyperparameter ranges
    epoch: int  # Current epoch number
    decision_number: int  # Which decision this is (0-indexed)
    metric_direction: Optional[str] = None  # higher/lower objective direction


@dataclass
class AgentDecision:
    """Decision made by an agent."""

    new_config: Dict[str, Any]  # New hyperparameter configuration
    reasoning: str  # Explanation for the decision
    confidence: float  # Confidence score [0, 1]
    metadata: Dict[str, Any]  # Additional metadata


class Agent(ABC):
    """
    Abstract base class for all agents in AgentHPOBench.

    Agents analyze training logs and make hyperparameter adjustments
    to optimize the declared target metric within a computational budget.
    """

    def __init__(self, name: str, model_name: str, **kwargs):
        """
        Initialize the agent.

        Args:
            name: Human-readable name for this agent
            model_name: Model identifier (e.g., "gpt-4", "llama-3-70b")
            **kwargs: Additional agent-specific parameters
        """
        self.name = name
        self.model_name = model_name
        self.config = kwargs

        # Statistics
        self.total_decisions = 0
        self.invalid_decisions = 0
        self.total_cost = 0.0  # API cost or compute time

    @abstractmethod
    def decide(self, context: DecisionContext) -> AgentDecision:
        """
        Make a hyperparameter adjustment decision based on training context.

        Args:
            context: DecisionContext containing training logs, current config,
                    metrics history, budget, and search space

        Returns:
            AgentDecision containing new hyperparameters, reasoning, and confidence

        Raises:
            InvalidDecisionError: If decision violates search space constraints
        """
        pass

    def validate_decision(
        self, decision: Dict[str, Any], search_space: Dict[str, Any]
    ) -> tuple[bool, Optional[str]]:
        """
        Validate that a decision is within the search space.

        Args:
            decision: Proposed hyperparameter configuration
            search_space: Valid hyperparameter ranges

        Returns:
            (is_valid, error_message)
        """
        for param, value in decision.items():
            if param not in search_space:
                return False, f"Unknown parameter: {param}"

            valid_range = search_space[param]

            # Check if parameter is in valid range
            if isinstance(valid_range, list):
                if value not in valid_range:
                    return False, f"{param}={value} not in valid range {valid_range}"
            elif isinstance(valid_range, dict):
                if "min" in valid_range and value < valid_range["min"]:
                    return False, f"{param}={value} below minimum {valid_range['min']}"
                if "max" in valid_range and value > valid_range["max"]:
                    return False, f"{param}={value} above maximum {valid_range['max']}"

        return True, None

    def get_stats(self) -> Dict[str, Any]:
        """Return agent statistics."""
        return {
            "name": self.name,
            "model_name": self.model_name,
            "total_decisions": self.total_decisions,
            "invalid_decisions": self.invalid_decisions,
            "valid_decision_rate": (
                (self.total_decisions - self.invalid_decisions) / self.total_decisions
                if self.total_decisions > 0
                else 1.0
            ),
            "total_cost": self.total_cost,
        }

    def reset_stats(self):
        """Reset agent statistics."""
        self.total_decisions = 0
        self.invalid_decisions = 0
        self.total_cost = 0.0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', model='{self.model_name}')"


class InvalidDecisionError(Exception):
    """Raised when an agent makes an invalid decision."""

    pass
