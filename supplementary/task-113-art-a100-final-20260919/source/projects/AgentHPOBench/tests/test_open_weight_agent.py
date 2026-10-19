import os
import unittest
from unittest import mock

from agenthpobench.agents.open_source.qwen_agent import QwenAgent
from agenthpobench.agents.open_weight import LocalTransformersAgent
from agenthpobench.core.agent_base import DecisionContext


class LocalTransformersAgentTest(unittest.TestCase):
    def setUp(self):
        self.agent = object.__new__(LocalTransformersAgent)
        self.agent.use_chat_template = False
        self.agent.tokenizer = object()

    def test_legacy_qwen_import_is_an_alias(self):
        self.assertIs(QwenAgent, LocalTransformersAgent)

    def test_unicode_punctuation_is_normalized(self):
        parsed = self.agent._loads_config_block(
            "{\u201clearning_rate\u201d\uff1a 0.001\uff0c \u201coptimizer\u201d\uff1a \u201cadamw\u201d}"
        )
        self.assertEqual(
            parsed,
            {"learning_rate": 0.001, "optimizer": "adamw"},
        )

    def test_force_prefix_without_chat_template(self):
        with mock.patch.dict(os.environ, {"AUTOREP_FORCE_CONFIG_PREFIX": "1"}):
            rendered = self.agent._render_prompt("Choose a configuration.")

        self.assertEqual(rendered, "Choose a configuration.\nNEW_CONFIG: {")
        self.assertEqual(self.agent._response_prefix, "NEW_CONFIG: {")

    @staticmethod
    def _context(
        *,
        training_log: str,
        metric_direction: str | None = None,
    ) -> DecisionContext:
        return DecisionContext(
            training_log=training_log,
            current_config={"learning_rate": 0.001},
            metrics_history=[],
            budget_remaining=5,
            total_budget=5,
            search_space={"learning_rate": [0.001, 0.01]},
            epoch=0,
            decision_number=0,
            metric_direction=metric_direction,
        )

    def test_prompt_minimizes_lower_is_better_metric(self):
        prompt = self.agent._build_prompt(
            self._context(
                training_log="Metric: validation loss, lower is better.",
                metric_direction="lower_is_better",
            )
        )

        self.assertIn(
            "Optimize hyperparameters to minimize the target metric",
            prompt,
        )
        self.assertIn("Metric Direction: lower is better", prompt)
        self.assertNotIn(
            "Optimize hyperparameters to maximize the target metric",
            prompt,
        )

    def test_prompt_maximizes_higher_is_better_metric(self):
        prompt = self.agent._build_prompt(
            self._context(
                training_log="Metric: validation accuracy, higher is better.",
                metric_direction="higher_is_better",
            )
        )

        self.assertIn(
            "Optimize hyperparameters to maximize the target metric",
            prompt,
        )
        self.assertIn("Metric Direction: higher is better", prompt)

    def test_prompt_uses_task_log_direction_for_legacy_callers(self):
        prompt = self.agent._build_prompt(
            self._context(
                training_log="Metric: test RMSE, lower is better.",
            )
        )

        self.assertIn(
            "Optimize hyperparameters to minimize the target metric",
            prompt,
        )

    def test_prompt_rejects_missing_metric_direction(self):
        with self.assertRaisesRegex(ValueError, "Metric direction is required"):
            self.agent._build_prompt(
                self._context(training_log="No objective direction was provided.")
            )


if __name__ == "__main__":
    unittest.main()
