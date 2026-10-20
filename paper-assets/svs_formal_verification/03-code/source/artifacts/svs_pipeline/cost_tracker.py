"""API cost tracker — 记录所有 LLM API 调用的 token 使用量和费用估算。"""

import logging
from dataclasses import dataclass, field
from threading import Lock

logger = logging.getLogger(__name__)

DEFAULT_PRICING = {
    "deepseek-chat": {"input": 0.14, "output": 0.28},
    "deepseek-reasoner": {"input": 0.55, "output": 2.19},
    "deepseek/deepseek-v3.2": {"input": 0.27, "output": 1.10},
    "deepseek/deepseek-v4-pro": {"input": 0.80, "output": 3.20},
}

# Local vLLM: no per-token API cost, tracked as GPU-hours instead.
# RTX 5090 ~$1.50/h/card. TP=2 = $3.00/h total.
LOCAL_GPU_COST_PER_HOUR = 3.0


@dataclass
class CostTracker:
    """Thread-safe API cost tracker."""

    pricing: dict = field(default_factory=lambda: dict(DEFAULT_PRICING))
    _records: list = field(default_factory=list, repr=False)
    _lock: Lock = field(default_factory=Lock, repr=False)
    _total_input_tokens: int = 0
    _total_output_tokens: int = 0

    def record(self, model: str, prompt_tokens: int, completion_tokens: int, module: str = ""):
        with self._lock:
            self._total_input_tokens += prompt_tokens
            self._total_output_tokens += completion_tokens
            self._records.append({
                "model": model,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens,
                "module": module,
            })
        logger.debug("API call [%s/%s]: %d+%d tokens", module, model, prompt_tokens, completion_tokens)

    def summary(self) -> dict:
        with self._lock:
            by_module: dict = {}
            by_model: dict = {}
            for r in self._records:
                mod = r["module"] or "unknown"
                if mod not in by_module:
                    by_module[mod] = {"calls": 0, "input_tokens": 0, "output_tokens": 0}
                by_module[mod]["calls"] += 1
                by_module[mod]["input_tokens"] += r["prompt_tokens"]
                by_module[mod]["output_tokens"] += r["completion_tokens"]

                mdl = r["model"]
                if mdl not in by_model:
                    by_model[mdl] = {"calls": 0, "input_tokens": 0, "output_tokens": 0}
                by_model[mdl]["calls"] += 1
                by_model[mdl]["input_tokens"] += r["prompt_tokens"]
                by_model[mdl]["output_tokens"] += r["completion_tokens"]

            total_cost = 0.0
            model_costs: dict = {}
            for mdl, counts in by_model.items():
                prices = self.pricing.get(mdl, {"input": 0.0, "output": 0.0})
                cost = (counts["input_tokens"] / 1_000_000 * prices["input"]
                        + counts["output_tokens"] / 1_000_000 * prices["output"])
                model_costs[mdl] = round(cost, 6)
                total_cost += cost

            return {
                "total_calls": len(self._records),
                "total_input_tokens": self._total_input_tokens,
                "total_output_tokens": self._total_output_tokens,
                "total_tokens": self._total_input_tokens + self._total_output_tokens,
                "estimated_cost_usd": round(total_cost, 6),
                "by_module": by_module,
                "by_model": {
                    mdl: {**counts, "estimated_cost_usd": model_costs.get(mdl, 0)}
                    for mdl, counts in by_model.items()
                },
            }


_global_tracker = CostTracker()


def get_tracker() -> CostTracker:
    return _global_tracker


def reset_tracker():
    global _global_tracker
    _global_tracker = CostTracker()
