"""
GLM (Zhipu AI) agent implementation for AgentHPOBench.

Supports both GLM-4 and other models via Zhipu AI API.
"""

import os
import time
from typing import Dict, Any

from agenthpobench.core.agent_base import Agent, DecisionContext, AgentDecision, InvalidDecisionError


class GLMAgent(Agent):
    """Agent using GLM API via Zhipu AI."""

    def __init__(
        self,
        model: str = "glm-4-flash",
        temperature: float = 0.7,
        max_tokens: int = 2000,
        api_key: [REDACTED] | None = None,
        **kwargs
    ):
        """
        Initialize GLM agent.

        Args:
            model: Model to use (e.g., "glm-4-flash", "glm-4-plus", "glm-4-air")
                   Available models:
                   - glm-4-flash: Fast, cost-effective (best for testing)
                   - glm-4-plus: Most capable
                   - glm-4-air: Balanced performance
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens in response
            api_key: [REDACTED] AI API key (defaults to ZHIPUAI_API_KEY env var)
        """
        super().__init__(
            name="GLM",
            model_name=model,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

        # Initialize client
        api_key = [REDACTED] or os.environ.get("ZHIPUAI_API_KEY")
        if not api_key:
            raise ValueError("ZHIPUAI_API_KEY environment variable must be set")

        self.api_key = [REDACTED]
        try:
            from zhipuai import ZhipuAI
            self.client = ZhipuAI(api_key=[REDACTED]
        except ImportError:
            print("Warning: zhipuai package not installed. Run: pip install zhipuai")
            self.client = None
        except Exception as e:
            print(f"Warning: Failed to initialize GLM client: {e}")
            self.client = None

    def decide(self, context: DecisionContext) -> AgentDecision:
        """Make a decision using GLM API."""

        if self.client is None:
            # Fallback: return a simple rule-based decision
            return self._fallback_decision(context)

        # Build prompt
        prompt = self._build_prompt(context)

        start_time = time.time()
        timeout_seconds = 60  # 1 minute timeout

        try:
            # Call API with timeout using threads
            import threading

            response_container = {}
            error_container = {}

            def api_call():
                try:
                    response_container['result'] = self.client.chat.completions.create(
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
                except Exception as e:
                    error_container['error'] = e

            # Start API call in a separate thread
            api_thread = threading.Thread(target=api_call)
            api_thread.daemon = True
            api_thread.start()
            api_thread.join(timeout=timeout_seconds)

            if api_thread.is_alive():
                print(f"GLM API timeout after {timeout_seconds}s")
                return self._fallback_decision(context)

            if 'error' in error_container:
                raise error_container['error']

            response = response_container['result']
            elapsed_time = time.time() - start_time

            # Estimate cost
            prompt_tokens = response.usage.prompt_tokens
            completion_tokens = response.usage.completion_tokens
            cost = self._estimate_cost(prompt_tokens, completion_tokens)
            self.total_cost += cost

            # Parse response
            response_text = response.choices[0].message.content
            decision = self._parse_response(response_text, context)

            return decision

        except Exception as e:
            print(f"GLM API error: {e}")
            return self._fallback_decision(context)

    def _fallback_decision(self, context: DecisionContext) -> AgentDecision:
        """Fallback rule-based decision if API fails."""
        # Simple heuristic: reduce learning rate if validation acc is not improving
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

    def _build_prompt(self, context: DecisionContext) -> str:
        """Build the prompt for the agent."""

        prompt = f"""你是一个机器学习研究专家，负责优化模型训练的超参数。

## 任务
在剩余预算内优化超参数以最大化性能指标。

## 当前进度
- 当前轮次: {context.epoch}
- 剩余预算: {context.budget_remaining} 轮 (总共 {context.total_budget} 轮)
- 决策编号: {context.decision_number + 1}

## 最近训练日志
```
{context.training_log}
```

## 当前超参数
```
{self._format_config(context.current_config)}
```

## 超参数搜索空间
你可以调整这些超参数在指定范围内：
{self._format_search_space(context.search_space)}

## 你的任务
基于训练进度，决定是否调整超参数。考虑因素：

1. **学习率**: 如果 loss 平坦或不稳定，考虑调整
2. **批次大小**: 更大的批次可能需要更高的学习率
3. **优化器**: 不同优化器适合不同任务
4. **正则化**: 如果过拟合（训练准确率 >> 验证准确率），增加正则化

**重要提示**：
- 如果训练进展良好，可以保持当前值
- 要保守 - 小调整比大改动好
- 考虑剩余预算 - 如果预算少，可以考虑更大的变化
- 只返回搜索空间内的有效超参数值

## 回复格式
请按以下格式返回：

```
推理: [你的解释，说明训练状况和为什么做这些调整]

新配置:
{{
    "learning_rate": 0.05,
    "batch_size": 128,
    "optimizer": "sgd",
    ...
}}

置信度: 0.8
```

请现在做出决策：
"""
        return prompt

    def _parse_response(self, response: str, context: DecisionContext) -> AgentDecision:
        """Parse the agent's response."""

        try:
            # Extract reasoning (handle Chinese key)
            reasoning_start = response.find("推理:")
            if reasoning_start == -1:
                reasoning_start = response.find("REASONING:")

            reasoning_end = response.find("新配置:")
            if reasoning_end == -1:
                reasoning_end = response.find("NEW_CONFIG:")

            reasoning = response[reasoning_start + 3:reasoning_end].strip()

            # Extract config
            config_start = response.find("{")
            config_end = response.rfind("}") + 1
            config_str = response[config_start:config_end]

            import json

            new_config = json.loads(config_str)

            # Extract confidence
            confidence_start = response.find("置信度:")
            if confidence_start == -1:
                confidence_start = response.find("CONFIDENCE:")

            confidence_str = response[confidence_start + 4:].strip()
            confidence = float(confidence_str)

            # Validate
            is_valid, error_msg = self.validate_decision(new_config, context.search_space)
            if not is_valid:
                raise InvalidDecisionError(f"Invalid config: {error_msg}")

            return AgentDecision(
                new_config=new_config,
                reasoning=reasoning,
                confidence=confidence,
                metadata={"raw_response": response},
            )

        except Exception as e:
            raise InvalidDecisionError(f"Failed to parse response: {e}")

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
        """Estimate API cost in CNY (GLM pricing)."""
        # GLM-4 pricing (as of 2024, in CNY)
        # Source: https://open.bigmodel.cn/pricing
        pricing = {
            "glm-4-flash": {"input": 0.0001, "output": 0.0001},  # 0.1元/1M tokens
            "glm-4-plus": {"input": 0.01, "output": 0.01},  # 10元/1M tokens
            "glm-4-air": {"input": 0.001, "output": 0.001},  # 1元/1M tokens
            "glm-3-turbo": {"input": 0.0005, "output": 0.0005},  # 0.5元/1M tokens
        }

        if self.model not in pricing:
            # Default to flash pricing
            rates = pricing["glm-4-flash"]
        else:
            rates = pricing[self.model]

        # Convert from yuan/1M to yuan/token
        input_cost = input_tokens * rates["input"] / 1e6
        output_cost = output_tokens * rates["output"] / 1e6

        return input_cost + output_cost
