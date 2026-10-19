"""Backward-compatible imports for the former Qwen-specific module."""

from agenthpobench.agents.open_weight import LocalTransformersAgent

QwenAgent = LocalTransformersAgent

__all__ = ["LocalTransformersAgent", "QwenAgent"]
