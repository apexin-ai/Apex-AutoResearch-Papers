from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from optimization_lab.adapters.base import EvaluationResult, EvaluationStatus
from optimization_lab.task_spec import TaskSpec


@dataclass(frozen=True)
class FeedbackCard:
    task_id: str
    candidate_id: str
    outcome: str
    valid_run: bool
    stage_reached: str
    compiled: bool
    correct: bool
    speedup_vs_eager: float | None
    candidate_runtime_ms: float | None
    reference_runtime_ms: float | None
    error_summary: str
    next_action: str
    gpu_seconds: float
    hardware: str

    @classmethod
    def from_result(
        cls,
        task: TaskSpec,
        candidate_id: str,
        result: EvaluationResult,
    ) -> "FeedbackCard":
        if result.status is EvaluationStatus.ENVIRONMENT_INVALID:
            stage = "environment"
            next_action = "暂停候选判断，先修复 GPU 或评分环境后原样重跑。"
        elif result.status in {
            EvaluationStatus.COMPILE_FAILED,
            EvaluationStatus.POLICY_REJECTED,
        }:
            stage = "compile"
            detail = result.error_summary or "编译或静态合同未通过"
            next_action = f"先修复编译问题：{detail}"
        elif result.status is EvaluationStatus.TIMEOUT:
            stage = "runtime"
            next_action = "保留历史最佳版本，缩小改动并检查超时原因。"
        elif not result.correct:
            stage = "correctness"
            next_action = "禁止测速；先根据误差摘要恢复数值正确性。"
        else:
            stage = "performance"
            next_action = "与历史最佳比较；进步则保留，否则回滚并更换思路。"
        return cls(
            task_id=task.task_id,
            candidate_id=candidate_id,
            outcome=result.status.value,
            valid_run=result.status is not EvaluationStatus.ENVIRONMENT_INVALID,
            stage_reached=stage,
            compiled=result.compiled,
            correct=result.correct,
            speedup_vs_eager=result.speedup_vs_eager,
            candidate_runtime_ms=result.candidate_runtime_ms,
            reference_runtime_ms=result.reference_runtime_ms,
            error_summary=result.error_summary,
            next_action=next_action,
            gpu_seconds=result.gpu_seconds,
            hardware=result.hardware,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
