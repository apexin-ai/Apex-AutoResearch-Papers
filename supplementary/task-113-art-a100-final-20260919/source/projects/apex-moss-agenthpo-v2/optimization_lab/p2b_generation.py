from __future__ import annotations

import json
from dataclasses import dataclass

from optimization_lab.feedback import FeedbackCard
from optimization_lab.generation import _sanitize_private_paths
from optimization_lab.p2b_policy import P2bPolicyVersion, ScoreTrend
from optimization_lab.profiling import ProfileSummary


@dataclass(frozen=True)
class P2bGenerationRequest:
    task_id: str
    lane_id: str
    candidate_id: str
    task_card: str
    reference_source: str
    policy: P2bPolicyVersion
    base_candidate_source: str
    memory_sources: tuple[tuple[str, str], ...]
    feedback_history: tuple[FeedbackCard, ...]
    current_trend: ScoreTrend | None
    profile_history: tuple[ProfileSummary, ...]

    def to_prompt(self) -> str:
        feedback = [
            {
                "candidate_id": card.candidate_id,
                "compiled": card.compiled,
                "correct": card.correct,
                "candidate_runtime_ms": card.candidate_runtime_ms,
                "reference_runtime_ms": card.reference_runtime_ms,
                "speedup": card.speedup_vs_eager,
                "error_summary": _sanitize_private_paths(card.error_summary)[:800],
            }
            for card in self.feedback_history
        ]
        profiles = [item.to_public_dict() for item in self.profile_history]
        memory = "\n\n".join(
            f"### {candidate_id}\n```python\n{source[:14_000]}\n```"
            for candidate_id, source in self.memory_sources
        ) or "（本轮策略没有选择额外历史代码。）"
        trend = self.current_trend.to_dict() if self.current_trend else {
            "status": "first P2b candidate; compare against frozen starting score"
        }
        return f"""You are executing one frozen task-specific KernelBench Harness.
Follow its selected skills, tools, memory views, workflow, and mutation scope.
Output exactly one complete Python code block defining ModelNew. No second code block.

candidate_id: {self.candidate_id}
task_id: {self.task_id}
lane_id: {self.lane_id}

## Structured Harness
{self.policy.policy.to_harness_text()}

## Task card
{self.task_card}

## Fixed PyTorch reference semantics
```text
{self.reference_source}
```

## Policy-selected base candidate ({self.policy.policy.base_candidate_id})
```python
{self.base_candidate_source}
```

## Policy-selected memory views
{memory}

## Current score trend
{json.dumps(trend, ensure_ascii=False, indent=2)}

## This lane's scored feedback
{json.dumps(feedback, ensure_ascii=False, indent=2)}

## Public profiler evidence
{json.dumps(profiles, ensure_ascii=False, indent=2)}

The official scorer, task, GPU, precision, and correctness gate are immutable.
Do not read or infer private evaluator logs or other live P2b lanes.
"""
