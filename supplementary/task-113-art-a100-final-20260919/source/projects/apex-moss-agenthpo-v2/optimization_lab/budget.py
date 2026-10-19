from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


class BudgetExceeded(RuntimeError):
    pass


@dataclass
class ExperimentBudget:
    max_gpu_seconds: float
    max_model_calls: int
    max_api_cost_usd: float | None = None
    max_gpu_cost_usd: float | None = None
    gpu_seconds_used: float = 0.0
    model_calls_used: int = 0
    api_cost_usd_used: float = 0.0
    gpu_cost_usd_used: float = 0.0

    def reserve(
        self,
        *,
        gpu_seconds: float = 0.0,
        model_calls: int = 0,
        api_cost_usd: float = 0.0,
        gpu_cost_usd: float = 0.0,
    ) -> None:
        if min(gpu_seconds, model_calls, api_cost_usd, gpu_cost_usd) < 0:
            raise ValueError("budget reservations cannot be negative")
        if self.gpu_seconds_used + gpu_seconds > self.max_gpu_seconds:
            raise BudgetExceeded("GPU hard cap would be exceeded")
        if self.model_calls_used + model_calls > self.max_model_calls:
            raise BudgetExceeded("model-call hard cap would be exceeded")
        if (
            self.max_api_cost_usd is not None
            and self.api_cost_usd_used + api_cost_usd > self.max_api_cost_usd
        ):
            raise BudgetExceeded("API cost hard cap would be exceeded")
        if (
            self.max_gpu_cost_usd is not None
            and self.gpu_cost_usd_used + gpu_cost_usd > self.max_gpu_cost_usd
        ):
            raise BudgetExceeded("GPU cost hard cap would be exceeded")
        self.gpu_seconds_used += gpu_seconds
        self.model_calls_used += model_calls
        self.api_cost_usd_used += api_cost_usd
        self.gpu_cost_usd_used += gpu_cost_usd

    def settle_gpu(self, *, reserved_seconds: float, actual_seconds: float) -> None:
        if reserved_seconds < 0 or actual_seconds < 0:
            raise ValueError("GPU accounting cannot be negative")
        adjusted = self.gpu_seconds_used - reserved_seconds + actual_seconds
        if adjusted > self.max_gpu_seconds:
            raise BudgetExceeded("actual GPU usage crossed the hard cap")
        self.gpu_seconds_used = max(0.0, adjusted)

    def settle_api(self, *, reserved_cost_usd: float, actual_cost_usd: float) -> None:
        if reserved_cost_usd < 0 or actual_cost_usd < 0:
            raise ValueError("API accounting cannot be negative")
        adjusted = self.api_cost_usd_used - reserved_cost_usd + actual_cost_usd
        if self.max_api_cost_usd is not None and adjusted > self.max_api_cost_usd:
            raise BudgetExceeded("actual API cost crossed the hard cap")
        self.api_cost_usd_used = max(0.0, adjusted)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
