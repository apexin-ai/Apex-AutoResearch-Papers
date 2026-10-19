from __future__ import annotations

import hashlib
import json
import os
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ACTIVE_TASK_IDS = (
    "kernelbench_layernorm",
    "kernelbench_matmul_sigmoid_sum",
)
BASELINE_KINDS = (
    "generic_zero_shot",
    "equal_budget_general",
    "manual_naive",
)
P1_ROUNDS = {
    "generic_zero_shot": 1,
    "equal_budget_general": 8,
    "manual_naive": 2,
}
SEED_ROOT = Path("optimization_lab/harnesses/seeds")
BASELINE_SEEDS = {
    kind: SEED_ROOT / f"{kind}.md" for kind in BASELINE_KINDS
}
SPECIALIST_SEED = SEED_ROOT / "specialist_v001.md"


@dataclass(frozen=True)
class BaselineLane:
    lane_id: str
    task_id: str
    kind: str
    harness_path: str
    harness_sha256: str
    workflow: tuple[str, ...]
    history_scope: str
    allow_harness_mutation: bool
    model_call_cap: int | None
    gpu_seconds_cap: float | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class LineagePlan:
    lineage_id: str
    task_id: str
    seed_path: str
    seed_sha256: str
    history_scope: str
    max_rounds: int
    allow_harness_mutation: bool
    model_call_cap: int | None
    gpu_seconds_cap: float | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CampaignPlan:
    artifact_root: str
    executor_model: str | None
    model_call_cap_per_lane: int | None
    gpu_seconds_cap_per_lane: float | None
    api_dollar_cap: float | None
    gpu_dollar_cap: float | None
    p0_clean_confirmed: bool
    baselines: tuple[BaselineLane, ...]
    lineages: tuple[LineagePlan, ...]
    schema_version: int = 1

    @classmethod
    def build(
        cls,
        *,
        project_root: Path,
        artifact_root: Path,
        executor_model: str | None = None,
        model_call_cap_per_lane: int | None = None,
        gpu_seconds_cap_per_lane: float | None = None,
        api_dollar_cap: float | None = None,
        gpu_dollar_cap: float | None = None,
        p0_clean_confirmed: bool = False,
    ) -> "CampaignPlan":
        project_root = project_root.resolve()
        artifact_root = artifact_root.resolve()
        if "/.claude-manager/worktrees/" in f"{artifact_root}/":
            raise ValueError("campaign artifacts must not be stored inside a worktree")
        if model_call_cap_per_lane is not None and model_call_cap_per_lane < 1:
            raise ValueError("model-call cap must be positive")
        if gpu_seconds_cap_per_lane is not None and gpu_seconds_cap_per_lane <= 0:
            raise ValueError("GPU-seconds cap must be positive")
        if api_dollar_cap is not None and api_dollar_cap <= 0:
            raise ValueError("API dollar cap must be positive")
        if gpu_dollar_cap is not None and gpu_dollar_cap <= 0:
            raise ValueError("GPU dollar cap must be positive")
        if executor_model is not None and not executor_model.strip():
            raise ValueError("executor model cannot be blank")

        baseline_workflows = {
            "generic_zero_shot": (
                "read_reference",
                "generate_candidate",
                "evaluate_once",
                "stop",
            ),
            "equal_budget_general": (
                "read_reference",
                "generate_candidate",
                "evaluate",
                "revise_candidate_without_mutating_harness",
            ),
            "manual_naive": (
                "read_reference",
                "generate_candidate",
                "check_correctness",
                "measure_if_correct",
                "revise_once",
                "stop",
            ),
        }
        baselines = []
        for task_id in ACTIVE_TASK_IDS:
            for kind in BASELINE_KINDS:
                seed = BASELINE_SEEDS[kind]
                baselines.append(
                    BaselineLane(
                        lane_id=f"p1:{task_id}:{kind}",
                        task_id=task_id,
                        kind=kind,
                        harness_path=seed.as_posix(),
                        harness_sha256=_file_sha(project_root / seed),
                        workflow=baseline_workflows[kind],
                        history_scope=f"baselines/{task_id}/{kind}",
                        allow_harness_mutation=False,
                        model_call_cap=model_call_cap_per_lane,
                        gpu_seconds_cap=gpu_seconds_cap_per_lane,
                    )
                )

        specialist_sha = _file_sha(project_root / SPECIALIST_SEED)
        lineages = []
        for task_id in ACTIVE_TASK_IDS:
            for index in range(3):
                lineage_id = f"r{index:02d}"
                lineages.append(
                    LineagePlan(
                        lineage_id=lineage_id,
                        task_id=task_id,
                        seed_path=SPECIALIST_SEED.as_posix(),
                        seed_sha256=specialist_sha,
                        history_scope=f"lineages/{task_id}/{lineage_id}",
                        max_rounds=8,
                        allow_harness_mutation=True,
                        model_call_cap=model_call_cap_per_lane,
                        gpu_seconds_cap=gpu_seconds_cap_per_lane,
                    )
                )

        plan = cls(
            artifact_root=str(artifact_root),
            executor_model=executor_model,
            model_call_cap_per_lane=model_call_cap_per_lane,
            gpu_seconds_cap_per_lane=gpu_seconds_cap_per_lane,
            api_dollar_cap=api_dollar_cap,
            gpu_dollar_cap=gpu_dollar_cap,
            p0_clean_confirmed=p0_clean_confirmed,
            baselines=tuple(baselines),
            lineages=tuple(lineages),
        )
        plan.validate()
        return plan

    @property
    def blockers(self) -> tuple[str, ...]:
        blockers = []
        if not self.p0_clean_confirmed:
            blockers.append("p0_clean_confirmation_missing")
        if self.executor_model is None:
            blockers.append("executor_model_missing")
        if self.model_call_cap_per_lane is None:
            blockers.append("model_call_cap_missing")
        if self.gpu_seconds_cap_per_lane is None:
            blockers.append("gpu_seconds_cap_missing")
        if self.api_dollar_cap is None:
            blockers.append("api_dollar_cap_missing")
        if self.gpu_dollar_cap is None:
            blockers.append("gpu_dollar_cap_missing")
        return tuple(blockers)

    @property
    def execution_ready(self) -> bool:
        return not self.blockers

    def validate(self) -> None:
        for task_id in ACTIVE_TASK_IDS:
            task_baselines = [lane for lane in self.baselines if lane.task_id == task_id]
            if {lane.kind for lane in task_baselines} != set(BASELINE_KINDS):
                raise ValueError(f"baseline matrix is incomplete for {task_id}")
            if any(lane.allow_harness_mutation for lane in task_baselines):
                raise ValueError("P1 baseline harnesses must remain frozen")
            task_lineages = [lane for lane in self.lineages if lane.task_id == task_id]
            if len(task_lineages) != 3:
                raise ValueError(f"exactly three P2 lineages are required for {task_id}")
            if len({lane.seed_sha256 for lane in task_lineages}) != 1:
                raise ValueError("P2 lineages must start from byte-identical seeds")
            if len({lane.history_scope for lane in task_lineages}) != 3:
                raise ValueError("P2 lineage histories must be isolated")
            if any(lane.max_rounds != 8 for lane in task_lineages):
                raise ValueError("P2 lineages have a frozen eight-round cap")
        scopes = [lane.history_scope for lane in (*self.baselines, *self.lineages)]
        if len(scopes) != len(set(scopes)):
            raise ValueError("campaign history scopes must be globally unique")

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "artifact_root": self.artifact_root,
            "executor_model": self.executor_model,
            "model_call_cap_per_lane": self.model_call_cap_per_lane,
            "gpu_seconds_cap_per_lane": self.gpu_seconds_cap_per_lane,
            "api_dollar_cap": self.api_dollar_cap,
            "gpu_dollar_cap": self.gpu_dollar_cap,
            "p0_clean_confirmed": self.p0_clean_confirmed,
            "execution_ready": self.execution_ready,
            "blockers": list(self.blockers),
            "model_calls_consumed": 0,
            "gpu_seconds_consumed": 0.0,
            "baselines": [lane.to_dict() for lane in self.baselines],
            "lineages": [lane.to_dict() for lane in self.lineages],
        }

    def write(self, path: Path) -> None:
        path = path.resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, name = tempfile.mkstemp(dir=path.parent, suffix=".campaign.tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(self.to_dict(), handle, ensure_ascii=False, indent=2)
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            Path(name).replace(path)
        except Exception:
            Path(name).unlink(missing_ok=True)
            raise

    @classmethod
    def read(cls, path: Path) -> "CampaignPlan":
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("schema_version") != 1:
            raise ValueError("unsupported campaign plan schema")
        plan = cls(
            artifact_root=str(data["artifact_root"]),
            executor_model=data.get("executor_model"),
            model_call_cap_per_lane=data.get("model_call_cap_per_lane"),
            gpu_seconds_cap_per_lane=data.get("gpu_seconds_cap_per_lane"),
            api_dollar_cap=data.get("api_dollar_cap"),
            gpu_dollar_cap=data.get("gpu_dollar_cap"),
            p0_clean_confirmed=data.get("p0_clean_confirmed") is True,
            baselines=tuple(
                BaselineLane(**{**lane, "workflow": tuple(lane["workflow"])})
                for lane in data["baselines"]
            ),
            lineages=tuple(LineagePlan(**lane) for lane in data["lineages"]),
            schema_version=1,
        )
        plan.validate()
        return plan


def _file_sha(path: Path) -> str:
    if not path.is_file():
        raise ValueError(f"missing frozen harness seed: {path}")
    return hashlib.sha256(path.read_bytes()).hexdigest()
