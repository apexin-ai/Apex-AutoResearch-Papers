"""
OpenAI-compatible API agent implementation for AgentHPOBench.
Supports OpenAI, DeepSeek, OpenRouter, and other OpenAI-compatible endpoints.
"""

import os
import time
from typing import Dict, Any, Optional
from openai import OpenAI
import json

from agenthpobench.core.agent_base import Agent, DecisionContext, AgentDecision, InvalidDecisionError


class OpenAICompatibleAgent(Agent):
    """Agent using OpenAI-compatible API for DeepSeek, OpenAI, OpenRouter, etc."""

    def __init__(
        self,
        model: str,
        api_key: [REDACTED] = None,
        base_url: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
        **kwargs
    ):
        """
        Initialize OpenAI-compatible agent.

        Args:
            model: Model name (e.g., "deepseek-chat", "gpt-4", "nex-agi/deepseek-v3.1-nex-1")
            api_key: [REDACTED] key (defaults to OPENAI_API_KEY env var)
            base_url: Base URL for API (defaults to OPENAI_BASE_URL env var or OpenAI official)
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
        """
        super().__init__(
            name="OpenAICompat",
            model_name=model,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

        # Get API key
        api_key = [REDACTED] or os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable must be set")

        # Get base URL (default to OpenAI official if not provided)
        base_url = base_url or os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")

        # Initialize client
        try:
            self.client = OpenAI(api_key=[REDACTED], base_url=base_url)
        except ImportError:
            print("Warning: openai package not installed. Run: pip install openai")
            self.client = None
        except Exception as e:
            print(f"Warning: Failed to initialize OpenAI client: {e}")
            self.client = None

    def decide(self, context: DecisionContext) -> AgentDecision:
        """Make a decision using OpenAI-compatible API."""

        if self.client is None:
            return self._fallback_decision(context)

        # Build prompt
        prompt = self._build_prompt(context)

        start_time = time.time()

        try:
            # Call API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )

            elapsed_time = time.time() - start_time

            # Estimate cost
            if hasattr(response, 'usage') and response.usage:
                prompt_tokens = response.usage.prompt_tokens
                completion_tokens = response.usage.completion_tokens
                cost = self._estimate_cost(prompt_tokens, completion_tokens)
                self.total_cost += cost
            else:
                # Rough estimate if usage not available
                cost = 0.0

            # Parse response
            response_text = response.choices[0].message.content
            decision = self._parse_response(response_text, context)

            return decision

        except Exception as e:
            print(f"OpenAI API error: {e}")
            return self._fallback_decision(context)

    def _build_prompt(self, context: DecisionContext) -> str:
        """Build the prompt for the agent."""

        prompt = f"""You are an expert machine learning researcher helping to optimize hyperparameters for model training.

## Task
Optimize hyperparameters to maximize the performance metric within the remaining budget.

## Current Training Progress
- Current Epoch: {context.epoch}
- Budget Remaining: {context.budget_remaining} epochs (out of {context.total_budget} total)
- Decision Number: {context.decision_number + 1}

## Recent Training Logs
```
{context.training_log}
```

## Current Hyperparameters
```
{self._format_config(context.current_config)}
```

## Hyperparameter Search Space
You can adjust these hyperparameters within the specified ranges:
{self._format_search_space(context.search_space)}

## Your Task
Based on the training progress, decide whether to adjust the hyperparameters. Consider:

1. **Learning Rate**: If loss is plateauing or unstable, consider adjusting
2. **Batch Size**: Larger batches may need higher learning rates
3. **Optimizer**: Different optimizers work better for different tasks
4. **Regularization**: If overfitting (train acc >> val acc), increase regularization

**IMPORTANT**:
- If training is progressing well, you may keep current values
- Be conservative - small adjustments are better than drastic changes
- Consider the remaining budget - if budget is low, consider larger changes
- Return ONLY valid hyperparameter values from the search space

## Response Format
Return your response in this exact format:

```
REASONING: [Your explanation of what's happening in training and why you're making these changes]

NEW_CONFIG:
{{
    "learning_rate": 0.05,
    "batch_size": 128,
    "optimizer": "sgd",
    ...
}}

CONFIDENCE: 0.8
```

Make your decision now:
"""
        return prompt

    def _parse_response(self, response: str, context: DecisionContext) -> AgentDecision:
        """Parse the agent's response."""

        try:
            # Extract reasoning
            reasoning_start = response.find("REASONING:")
            if reasoning_start == -1:
                raise ValueError("Missing REASONING: section")

            reasoning_end = response.find("NEW_CONFIG:")
            if reasoning_end == -1:
                raise ValueError("Missing NEW_CONFIG: section")

            reasoning = response[reasoning_start + 11:reasoning_end].strip()

            # Extract config
            config_start = response.find("{")
            if config_start == -1:
                raise ValueError("Missing JSON config")
            config_end = response.rfind("}") + 1
            if config_end == 0:
                raise ValueError("Invalid JSON config")

            config_str = response[config_start:config_end]

            new_config = json.loads(config_str)

            # Extract confidence
            confidence = 0.8
            confidence_start = response.find("CONFIDENCE:")
            if confidence_start != -1:
                confidence_str = response[confidence_start + 11:].strip().split()[0]
                confidence = float(confidence_str)

            # Validate
            is_valid, error_msg = self.validate_decision(new_config, context.search_space)
            if not is_valid:
                raise InvalidDecisionError(f"Invalid config: {error_msg}")

            return AgentDecision(
                new_config=new_config,
                reasoning=reasoning,
                confidence=confidence,
                metadata={"raw_response": response, "model": self.model},
            )

        except Exception as e:
            print(f"Failed to parse OpenAI response: {e}")
            raise InvalidDecisionError(f"Failed to parse response: {e}")

    def _fallback_decision(self, context: DecisionContext) -> AgentDecision:
        """Fallback rule-based decision if API fails."""
        metrics_history = context.metrics_history

        if len(metrics_history) >= 2:
            recent_acc = metrics_history[-1][1].get("accuracy", 0.0)
            prev_acc = metrics_history[-2][1].get("accuracy", 0.0)

            if recent_acc <= prev_acc:
                # Performance plateaued, reduce LR
                current_lr = context.current_config.get("learning_rate", 0.001)
                new_lr = current_lr * 0.5

                new_config = context.current_config.copy()
                new_config["learning_rate"] = new_lr

                return AgentDecision(
                    new_config=new_config,
                    reasoning=f"Fallback: Performance plateaued (acc: {recent_acc:.4f}), reducing learning rate",
                    confidence=0.6,
                    metadata={"fallback": True},
                )

        # Keep current config
        return AgentDecision(
            new_config=context.current_config.copy(),
            reasoning="Fallback: Keeping current configuration",
            confidence=0.5,
            metadata={"fallback": True},
        )

    def _format_config(self, config: Dict[str, Any]) -> str:
        """Format config for display."""
        return "\n".join([f"  {k}: {v}" for k, v in config.items()])

    def _format_search_space(self, search_space: Dict[str, Any]) -> str:
        """Format search space for display."""
        lines = []
        for param, range_def in search_space.items():
            if isinstance(range_def, list):
                lines.append(f"- {param}: {range_def}")
            elif isinstance(range_def, dict):
                if "min" in range_def and "max" in range_def:
                    scale = range_def.get("scale", "linear")
                    lines.append(f"- {param}: [{range_def['min']}, {range_def['max']}] ({scale} scale)")
                else:
                    lines.append(f"- {param}: {range_def}")

        return "\n".join(lines)

    def _estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Estimate API cost in USD (OpenAI pricing)."""
        # OpenAI pricing (as of 2024, per 1M tokens)
        # Update with actual pricing for your model
        input_cost_per_1m = 0.0  # Unknown, assume 0 for local/OpenRouter
        output_cost_per_1m = 0.0

        return (input_tokens * input_cost_per_1m / 1e6) + (output_tokens * output_cost_per_1m / 1e6)


# GPTAgent alias for compatibility
GPTAgent = OpenAICompatibleAgent
# ClaudeAgent is already defined in this file, keep it separate
