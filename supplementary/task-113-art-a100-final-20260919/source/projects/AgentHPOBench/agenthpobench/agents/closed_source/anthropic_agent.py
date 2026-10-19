"""
Anthropic SDK agent for AgentHPOBench.
Supports custom base_url for routing through a local proxy (gpu_http_proxy).
"""

import os
import time
import json
from typing import Dict, Any, Optional

from agenthpobench.core.agent_base import Agent, DecisionContext, AgentDecision, InvalidDecisionError


class AnthropicAgent(Agent):
    """Agent using Anthropic SDK, with optional base_url for proxy support."""

    def __init__(
        self,
        model: str = "claude-sonnet-4-6",
        api_key: [REDACTED] = None,
        base_url: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1500,
        **kwargs,
    ):
        super().__init__(
            name="AnthropicAgent",
            model_name=model,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs,
        )
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

        api_key = [REDACTED] or os.environ.get("ANTHROPIC_API_KEY", "dummy")

        try:
            from anthropic import Anthropic
            kwargs_client: Dict[str, Any] = {"api_key": [REDACTED]}
            if base_url:
                kwargs_client["base_url"] = base_url
            self.client = Anthropic(**kwargs_client)
        except ImportError:
            print("Warning: anthropic package not installed.")
            self.client = None

    def decide(self, context: DecisionContext) -> AgentDecision:
        if self.client is None:
            return self._fallback_decision(context)

        prompt = self._build_prompt(context)
        max_retries = 5
        retry_delay = 10.0
        for attempt in range(1, max_retries + 1):
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    temperature=self.temperature,
                    messages=[{"role": "user", "content": prompt}],
                )
                text = response.content[0].text
                return self._parse_response(text, context)
            except Exception as e:
                is_503 = "503" in str(e) or "overloaded" in str(e).lower()
                if is_503 and attempt < max_retries:
                    print(f"Anthropic API 503, retry {attempt}/{max_retries - 1} in {retry_delay}s...")
                    time.sleep(retry_delay)
                else:
                    print(f"Anthropic API error (attempt {attempt}): {e}")
                    return self._fallback_decision(context)

    def _build_prompt(self, context: DecisionContext) -> str:
        return f"""You are an expert ML researcher optimizing hyperparameters.

## Training Progress
- Epoch: {context.epoch} / {context.total_budget}
- Budget remaining: {context.budget_remaining} epochs
- Decision #: {context.decision_number + 1}

## Recent Training Logs
```
{context.training_log}
```

## Current Hyperparameters
```
{self._fmt_dict(context.current_config)}
```

## Search Space
{self._fmt_search_space(context.search_space)}

## Instructions
Analyze training and return updated hyperparameters.
- If training is progressing well, keep values.
- Be conservative; prefer small adjustments.
- All values must be within the search space.

## Response Format (exact)
REASONING: <your analysis>

NEW_CONFIG:
{{
    "learning_rate": <value>,
    "batch_size": <value>,
    "optimizer": "<value>",
    "weight_decay": <value>,
    "momentum": <value>
}}

CONFIDENCE: <0.0-1.0>
"""

    def _parse_response(self, response: str, context: DecisionContext) -> AgentDecision:
        try:
            r_start = response.find("REASONING:")
            nc_start = response.find("NEW_CONFIG:")
            if r_start == -1 or nc_start == -1:
                raise ValueError("Missing REASONING or NEW_CONFIG section")

            reasoning = response[r_start + 10:nc_start].strip()

            brace_start = response.find("{", nc_start)
            brace_end = response.rfind("}") + 1
            if brace_start == -1 or brace_end == 0:
                raise ValueError("Missing JSON in NEW_CONFIG")

            new_config = json.loads(response[brace_start:brace_end])

            confidence = 0.8
            conf_pos = response.find("CONFIDENCE:", nc_start)
            if conf_pos != -1:
                try:
                    confidence = float(response[conf_pos + 11:].strip().split()[0])
                except (ValueError, IndexError):
                    pass

            is_valid, error_msg = self.validate_decision(new_config, context.search_space)
            if not is_valid:
                raise InvalidDecisionError(f"Invalid config: {error_msg}")

            return AgentDecision(
                new_config=new_config,
                reasoning=reasoning,
                confidence=confidence,
                metadata={"model": self.model},
            )
        except Exception as e:
            print(f"Failed to parse response: {e}")
            raise InvalidDecisionError(str(e))

    def _fallback_decision(self, context: DecisionContext) -> AgentDecision:
        history = context.metrics_history
        new_config = context.current_config.copy()
        if len(history) >= 2:
            acc_now = history[-1][1].get("accuracy", 0.0)
            acc_prev = history[-2][1].get("accuracy", 0.0)
            if acc_now <= acc_prev:
                new_config["learning_rate"] = new_config.get("learning_rate", 0.01) * 0.5
                return AgentDecision(
                    new_config=new_config,
                    reasoning=f"Fallback: plateau detected, halving LR",
                    confidence=0.6,
                    metadata={"fallback": True},
                )
        return AgentDecision(
            new_config=new_config,
            reasoning="Fallback: keeping current config",
            confidence=0.5,
            metadata={"fallback": True},
        )

    def _fmt_dict(self, d: Dict[str, Any]) -> str:
        return "\n".join(f"  {k}: {v}" for k, v in d.items())

    def _fmt_search_space(self, search_space: Dict[str, Any]) -> str:
        lines = []
        for param, spec in search_space.items():
            if isinstance(spec, list):
                lines.append(f"- {param}: {spec}")
            elif isinstance(spec, dict) and "min" in spec:
                lines.append(f"- {param}: [{spec['min']}, {spec['max']}] ({spec.get('scale', 'linear')})")
            else:
                lines.append(f"- {param}: {spec}")
        return "\n".join(lines)
