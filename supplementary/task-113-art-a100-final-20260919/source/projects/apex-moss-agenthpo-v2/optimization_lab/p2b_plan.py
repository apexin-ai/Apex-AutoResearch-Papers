from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from optimization_lab.campaign import ACTIVE_TASK_IDS


P2B_STRATEGIES = (
    "profile_exploit",
    "architecture_reset",
    "counterfactual",
    "recombinant_frontier",
)
P2B_STRUCTURAL_ROUNDS = (1, 3, 5, 6)


@dataclass(frozen=True)
class FrozenCandidate:
    task_id: str
    source_phase: str
    candidate_id: str
    source_path: str
    source_sha256: str
    speedup: float
    frozen_path: str = ""

    def __post_init__(self) -> None:
        if self.task_id not in ACTIVE_TASK_IDS:
            raise ValueError(f"unsupported P2b task: {self.task_id}")
        if self.source_phase not in {"p1", "p2"}:
            raise ValueError("frozen candidate must come from P1 or P2")
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", self.candidate_id):
            raise ValueError("frozen candidate id is unsafe")
        if not re.fullmatch(r"[0-9a-f]{64}", self.source_sha256):
            raise ValueError("frozen candidate hash is invalid")
        if self.speedup <= 0:
            raise ValueError("frozen candidate speedup must be positive")
        if self.frozen_path:
            path = PurePosixPath(self.frozen_path)
            if path.is_absolute() or ".." in path.parts:
                raise ValueError("frozen candidate path must be relative")


@dataclass(frozen=True)
class P2bLanePlan:
    lane_id: str
    task_id: str
    strategy: str
    history_scope: str
    starting_candidate_id: str
    starting_score: float
    allowed_frozen_candidate_ids: tuple[str, ...]
    mandatory_structural_rounds: tuple[int, ...] = P2B_STRUCTURAL_ROUNDS
    forced_restart_round: int = 6
    max_rounds: int = 8
    model_call_cap: int = 15
    gpu_seconds_cap: float = 3600.0

    def __post_init__(self) -> None:
        if self.task_id not in ACTIVE_TASK_IDS:
            raise ValueError("P2b lane task is not frozen")
        if self.strategy not in P2B_STRATEGIES:
            raise ValueError("P2b lane strategy is invalid")
        if self.lane_id != f"p2b:{self.task_id}:{self.strategy}":
            raise ValueError("P2b lane id does not match task and strategy")
        scope = PurePosixPath(self.history_scope)
        if scope.is_absolute() or not scope.parts or ".." in scope.parts:
            raise ValueError("P2b history scope is unsafe")
        if self.starting_score <= 0:
            raise ValueError("P2b starting score must be positive")
        if self.max_rounds != 8 or self.model_call_cap != 15:
            raise ValueError("P2b lane must preserve the frozen 8/15 limits")
        if self.gpu_seconds_cap != 3600.0:
            raise ValueError("P2b lane must preserve the frozen GPU cap")
        if self.forced_restart_round != 6:
            raise ValueError("P2b forced restart must remain at round six")
        if len(set(self.allowed_frozen_candidate_ids)) != len(
            self.allowed_frozen_candidate_ids
        ):
            raise ValueError("P2b allowed frozen candidates must be unique")
        if self.starting_candidate_id != "reference" and (
            self.starting_candidate_id not in self.allowed_frozen_candidate_ids
        ):
            raise ValueError("P2b starting candidate is not in the frozen inputs")


@dataclass(frozen=True)
class P2bPlan:
    artifact_root: str
    source_artifact_root: str
    executor_model: str
    frozen_candidates: tuple[FrozenCandidate, ...]
    lanes: tuple[P2bLanePlan, ...]
    global_model_call_cap: int = 120
    global_gpu_seconds_cap: float = 14_400.0
    api_dollar_cap_per_lane: float = 100.0
    gpu_dollar_cap_per_lane: float = 100.0
    schema_version: int = 1

    def __post_init__(self) -> None:
        if not self.executor_model.strip():
            raise ValueError("P2b executor model is required")
        if self.global_model_call_cap != 120:
            raise ValueError("P2b global model-call cap must remain 120")
        if self.global_gpu_seconds_cap != 14_400.0:
            raise ValueError("P2b global GPU cap must remain 14,400 seconds")
        if len(self.lanes) != len(ACTIVE_TASK_IDS) * len(P2B_STRATEGIES):
            raise ValueError("P2b requires exactly eight lanes")
        expected = {
            (task_id, strategy)
            for task_id in ACTIVE_TASK_IDS
            for strategy in P2B_STRATEGIES
        }
        actual = {(lane.task_id, lane.strategy) for lane in self.lanes}
        if actual != expected:
            raise ValueError("P2b lane matrix is incomplete or duplicated")
        if len({lane.history_scope for lane in self.lanes}) != len(self.lanes):
            raise ValueError("P2b lane histories must be isolated")
        for task_id in ACTIVE_TASK_IDS:
            task_inputs = [
                candidate
                for candidate in self.frozen_candidates
                if candidate.task_id == task_id
            ]
            if len(task_inputs) != 4:
                raise ValueError("P2b requires one P1 and three P2 inputs per task")
            if sum(item.source_phase == "p1" for item in task_inputs) != 1:
                raise ValueError("P2b requires exactly one P1 input per task")
            if sum(item.source_phase == "p2" for item in task_inputs) != 3:
                raise ValueError("P2b requires exactly three P2 inputs per task")
            if len({item.candidate_id for item in task_inputs}) != 4:
                raise ValueError("P2b frozen candidate ids must be unique per task")

    @property
    def execution_ready(self) -> bool:
        root = Path(self.artifact_root)
        return all(
            (root / candidate.frozen_path).is_file()
            and hashlib.sha256((root / candidate.frozen_path).read_bytes()).hexdigest()
            == candidate.source_sha256
            for candidate in self.frozen_candidates
        )

    @classmethod
    def build(
        cls,
        *,
        artifact_root: Path,
        source_artifact_root: Path,
        executor_model: str,
        frozen_candidates: tuple[FrozenCandidate, ...],
    ) -> "P2bPlan":
        artifact_root = artifact_root.resolve()
        source_artifact_root = source_artifact_root.resolve()
        if "/.claude-manager/worktrees/" in f"{artifact_root}/":
            raise ValueError("P2b artifacts must not be stored inside a worktree")
        artifact_root.mkdir(parents=True, exist_ok=True)

        copied: list[FrozenCandidate] = []
        for candidate in frozen_candidates:
            source = Path(candidate.source_path).resolve()
            if not source.is_relative_to(source_artifact_root) or not source.is_file():
                raise ValueError("frozen candidate source escapes source artifact root")
            actual_hash = hashlib.sha256(source.read_bytes()).hexdigest()
            if actual_hash != candidate.source_sha256:
                raise ValueError("frozen candidate source hash changed")
            relative = Path(
                "frozen_inputs",
                candidate.task_id,
                f"{candidate.candidate_id}.py",
            )
            destination = artifact_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists():
                if hashlib.sha256(destination.read_bytes()).hexdigest() != actual_hash:
                    raise ValueError("frozen P2b input is already bound to different content")
            else:
                shutil.copyfile(source, destination)
            copied.append(
                FrozenCandidate(
                    task_id=candidate.task_id,
                    source_phase=candidate.source_phase,
                    candidate_id=candidate.candidate_id,
                    source_path=str(source),
                    source_sha256=candidate.source_sha256,
                    speedup=candidate.speedup,
                    frozen_path=relative.as_posix(),
                )
            )

        lanes: list[P2bLanePlan] = []
        for task_id in ACTIVE_TASK_IDS:
            task_inputs = [item for item in copied if item.task_id == task_id]
            p1 = next(item for item in task_inputs if item.source_phase == "p1")
            p2 = sorted(
                (item for item in task_inputs if item.source_phase == "p2"),
                key=lambda item: item.candidate_id,
            )
            best_p2 = max(p2, key=lambda item: item.speedup)
            all_ids = tuple(item.candidate_id for item in (p1, *p2))
            for strategy in P2B_STRATEGIES:
                if strategy == "architecture_reset":
                    start_id = "reference"
                    start_score = 1.0
                    allowed = (p1.candidate_id, best_p2.candidate_id)
                elif strategy == "recombinant_frontier":
                    start_id = best_p2.candidate_id
                    start_score = best_p2.speedup
                    allowed = all_ids
                else:
                    start_id = best_p2.candidate_id
                    start_score = best_p2.speedup
                    allowed = (p1.candidate_id, best_p2.candidate_id)
                lanes.append(
                    P2bLanePlan(
                        lane_id=f"p2b:{task_id}:{strategy}",
                        task_id=task_id,
                        strategy=strategy,
                        history_scope=f"lineages/{task_id}/{strategy}",
                        starting_candidate_id=start_id,
                        starting_score=start_score,
                        allowed_frozen_candidate_ids=allowed,
                    )
                )
        return cls(
            artifact_root=str(artifact_root),
            source_artifact_root=str(source_artifact_root),
            executor_model=executor_model,
            frozen_candidates=tuple(copied),
            lanes=tuple(lanes),
        )

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["execution_ready"] = self.execution_ready
        return data

    def write(self, path: Path) -> None:
        _write_atomic(
            path,
            json.dumps(self.to_dict(), ensure_ascii=False, indent=2, sort_keys=True)
            + "\n",
        )

    @classmethod
    def read(cls, path: Path) -> "P2bPlan":
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("P2b plan must be a JSON object")
        data.pop("execution_ready", None)
        candidates = tuple(FrozenCandidate(**item) for item in data.pop("frozen_candidates"))
        lanes = tuple(
            P2bLanePlan(
                **{
                    **item,
                    "allowed_frozen_candidate_ids": tuple(
                        item["allowed_frozen_candidate_ids"]
                    ),
                    "mandatory_structural_rounds": tuple(
                        item["mandatory_structural_rounds"]
                    ),
                }
            )
            for item in data.pop("lanes")
        )
        return cls(frozen_candidates=candidates, lanes=lanes, **data)


def frozen_candidates_from_p2_artifacts(source_root: Path) -> tuple[FrozenCandidate, ...]:
    """Select the frozen P1 equal-budget best and each P2 lineage best."""
    source_root = source_root.resolve()
    ledger = source_root / "ledger.jsonl"
    if not ledger.is_file():
        raise ValueError("P1/P2 source ledger is missing")
    events = [json.loads(line) for line in ledger.read_text(encoding="utf-8").splitlines() if line]
    if not any(
        event.get("event_type") == "phase_changed"
        and event.get("payload", {}).get("phase") == "P2"
        and event.get("payload", {}).get("status") == "completed"
        for event in events
    ):
        raise ValueError("P2 source campaign is not completed and frozen")

    generated: dict[str, dict[str, Any]] = {
        str(event["payload"]["candidate_id"]): event["payload"]
        for event in events
        if event.get("event_type") == "candidate_generated"
    }
    feedback: dict[str, dict[str, Any]] = {}
    lane_by_candidate: dict[str, str] = {}
    for event in events:
        if event.get("event_type") in {
            "lane_candidate_completed",
            "p2_candidate_completed",
            "candidate_evaluation_corrected",
        }:
            payload = event.get("payload", {})
            card = payload.get("feedback", {})
            candidate_id = str(card.get("candidate_id", ""))
            if candidate_id:
                feedback[candidate_id] = card
                if payload.get("lane_id"):
                    lane_by_candidate[candidate_id] = str(payload["lane_id"])

    selected: list[tuple[str, str, str, float]] = []
    for task_id in ACTIVE_TASK_IDS:
        p1_options = []
        for candidate_id, card in feedback.items():
            lane = lane_by_candidate.get(candidate_id, "")
            if (
                lane == f"p1:{task_id}:equal_budget_general"
                and card.get("correct")
                and card.get("speedup_vs_eager") is not None
            ):
                p1_options.append((float(card["speedup_vs_eager"]), candidate_id))
        if not p1_options:
            raise ValueError(f"no correct equal-budget P1 candidate for {task_id}")
        p1_score, p1_id = max(p1_options)
        selected.append((task_id, "p1", p1_id, p1_score))

        completions = [
            event["payload"]
            for event in events
            if event.get("event_type") == "p2_lineage_completed"
            and event.get("payload", {}).get("task_id") == task_id
        ]
        if len(completions) != 3:
            raise ValueError(f"expected three frozen P2 lineages for {task_id}")
        for completion in sorted(completions, key=lambda item: item["lineage_id"]):
            candidate_id = str(completion["best_candidate_id"])
            selected.append(
                (task_id, "p2", candidate_id, float(completion["best_speedup"]))
            )

    result = []
    for task_id, phase, candidate_id, speedup in selected:
        event = generated.get(candidate_id)
        if event is None:
            raise ValueError(f"frozen source candidate was not archived: {candidate_id}")
        source = Path(event["archive"]["candidate_path"]).resolve()
        if not source.is_relative_to(source_root) or not source.is_file():
            raise ValueError("frozen source candidate path escapes P1/P2 artifacts")
        sha = hashlib.sha256(source.read_bytes()).hexdigest()
        if sha != event.get("candidate_sha256"):
            raise ValueError("frozen source candidate hash does not match the ledger")
        result.append(
            FrozenCandidate(
                task_id=task_id,
                source_phase=phase,
                candidate_id=candidate_id,
                source_path=str(source),
                source_sha256=sha,
                speedup=speedup,
            )
        )
    return tuple(result)


def _write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise
