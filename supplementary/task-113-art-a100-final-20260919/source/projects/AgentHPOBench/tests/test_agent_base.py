from __future__ import annotations

import unittest

from agenthpobench.core.agent_base import Agent, AgentDecision, DecisionContext


class DummyAgent(Agent):
    def decide(self, context: DecisionContext) -> AgentDecision:
        return AgentDecision(
            new_config=context.current_config,
            reasoning="keep",
            confidence=1.0,
            metadata={},
        )


class AgentBaseTests(unittest.TestCase):
    def test_validate_decision_accepts_values_in_search_space(self) -> None:
        agent = DummyAgent("dummy", "dummy")
        valid, error = agent.validate_decision(
            {"learning_rate": 0.01, "batch_size": 64},
            {
                "learning_rate": {"min": 0.001, "max": 0.1},
                "batch_size": [32, 64, 128],
            },
        )

        self.assertTrue(valid)
        self.assertIsNone(error)

    def test_validate_decision_rejects_unknown_or_out_of_range_values(self) -> None:
        agent = DummyAgent("dummy", "dummy")

        self.assertFalse(
            agent.validate_decision({"unknown": 1}, {"batch_size": [32]})[0]
        )
        self.assertFalse(
            agent.validate_decision(
                {"learning_rate": 1.0},
                {"learning_rate": {"min": 0.001, "max": 0.1}},
            )[0]
        )
