from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping


@dataclass(frozen=True)
class WorkflowDefinition:
    workflow_id: str
    steps: tuple[str, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.workflow_id, str) or not self.workflow_id.strip():
            raise TypeError("workflow_id must be a non-empty string")
        if not self.steps or any(not isinstance(step, str) or not step.strip() for step in self.steps):
            raise TypeError("workflow steps must contain non-empty strings")
        object.__setattr__(self, "steps", tuple(self.steps))

    def public_payload(self) -> dict[str, object]:
        return {"id": self.workflow_id, "steps": list(self.steps)}


class WorkflowRegistry:
    """Fixed, non-executable workflow catalog selectable by a Task Harness."""

    def __init__(self, definitions: Mapping[str, WorkflowDefinition]) -> None:
        self._definitions: dict[str, WorkflowDefinition] = {}
        for workflow_id, definition in definitions.items():
            if workflow_id != definition.workflow_id:
                raise ValueError("workflow registry key differs from definition id")
            if workflow_id in self._definitions:
                raise ValueError("workflow ids must be unique")
            self._definitions[workflow_id] = definition

    @classmethod
    def standard(cls) -> "WorkflowRegistry":
        definitions = (
            WorkflowDefinition(
                "diagnose_generate_verify",
                (
                    "Diagnose the current failure using only public task evidence.",
                    "Generate one complete candidate that addresses the diagnosis.",
                    "Verify the public output contract before emitting.",
                ),
            ),
            WorkflowDefinition(
                "compare_repair_verify",
                (
                    "Compare the current approach with the strongest public prior attempt.",
                    "Repair the smallest high-impact weakness.",
                    "Verify the public output contract before emitting.",
                ),
            ),
            WorkflowDefinition(
                "explore_measure_refine",
                (
                    "Explore one materially different public strategy.",
                    "Use an allowed public tool when measurement is useful.",
                    "Refine one complete candidate and verify its output contract.",
                ),
            ),
        )
        return cls({item.workflow_id: item for item in definitions})

    def require(self, workflow_id: str) -> WorkflowDefinition:
        try:
            return self._definitions[workflow_id]
        except KeyError as exc:
            raise KeyError(f"unknown workflow: {workflow_id}") from exc

    def public_catalog(self, allowed: Iterable[str]) -> list[dict[str, object]]:
        names = tuple(allowed)
        if len(set(names)) != len(names):
            raise ValueError("allowed workflows must not contain duplicates")
        return [self.require(name).public_payload() for name in names]


__all__ = ["WorkflowDefinition", "WorkflowRegistry"]
