"""
TaxEI Recovery Rate Evaluator
==============================
Evaluates a trained model's ability to recover from injected errors.

Metrics:
- Per-operator recovery rate: success rate under each injection type
- Overall recovery rate: aggregate across all operators
- Baseline success rate: performance without injection (regression check)
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from injection.base import InjectionOperator


@dataclass
class RecoveryResult:
    operator_name: str
    total_episodes: int
    recovered: int
    rate: float = 0.0

    def __post_init__(self):
        self.rate = self.recovered / self.total_episodes if self.total_episodes > 0 else 0.0


@dataclass
class EvalReport:
    per_operator: List[RecoveryResult] = field(default_factory=list)
    baseline_success_rate: float = 0.0
    overall_recovery_rate: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "baseline_success_rate": self.baseline_success_rate,
            "overall_recovery_rate": self.overall_recovery_rate,
            "per_operator": [
                {"operator": r.operator_name, "total": r.total_episodes,
                 "recovered": r.recovered, "rate": r.rate}
                for r in self.per_operator
            ],
        }


def evaluate_recovery(
    model_path: str,
    injection_operators: List[InjectionOperator],
    num_episodes: int = 100,
    output_path: Optional[str] = None,
) -> EvalReport:
    """Run recovery evaluation.

    For each injection operator:
      1. Reset ALFWorld env
      2. Inject the specified error
      3. Roll out the model
      4. Record success/failure

    Also runs baseline (no injection) episodes.
    """
    report = EvalReport()

    # TODO: load model from model_path
    # TODO: initialize ALFWorld env

    # --- Baseline (no injection) ---
    baseline_successes = 0
    for ep in range(num_episodes):
        # TODO: rollout without injection
        pass
    report.baseline_success_rate = baseline_successes / max(num_episodes, 1)

    # --- Per-operator evaluation ---
    total_recovered = 0
    total_tested = 0
    for op in injection_operators:
        recovered = 0
        for ep in range(num_episodes):
            # TODO: rollout with op injecting at a random step
            pass
        result = RecoveryResult(
            operator_name=op.name,
            total_episodes=num_episodes,
            recovered=recovered,
        )
        report.per_operator.append(result)
        total_recovered += recovered
        total_tested += num_episodes

    report.overall_recovery_rate = total_recovered / max(total_tested, 1)

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_text(
            json.dumps(report.to_dict(), indent=2, ensure_ascii=False)
        )

    return report
