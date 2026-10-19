from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from optimization_lab.p2b_plan import (
    P2B_STRATEGIES,
    FrozenCandidate,
    P2bPlan,
)


TASKS = ("kernelbench_layernorm", "kernelbench_matmul_sigmoid_sum")


def _frozen_inputs(source_root: Path) -> tuple[FrozenCandidate, ...]:
    candidates = []
    for task in TASKS:
        for phase, suffix, speedup in (
            ("p1", "p1-best", 2.0),
            ("p2", "p2-r00", 3.0),
            ("p2", "p2-r01", 4.0),
            ("p2", "p2-r02", 3.5),
        ):
            candidate_id = f"{task.removeprefix('kernelbench_')}-{suffix}"
            path = source_root / f"{candidate_id}.py"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f"class ModelNew:\n    source = {candidate_id!r}\n",
                encoding="utf-8",
            )
            candidates.append(
                FrozenCandidate(
                    task_id=task,
                    source_phase=phase,
                    candidate_id=candidate_id,
                    source_path=str(path),
                    source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    speedup=speedup,
                )
            )
    return tuple(candidates)


def test_p2b_plan_freezes_eight_distinct_lanes_and_source_hashes(
    tmp_path: Path,
) -> None:
    source_root = tmp_path / "p2-source"
    frozen = _frozen_inputs(source_root)

    plan = P2bPlan.build(
        artifact_root=tmp_path / "p2b-artifacts",
        source_artifact_root=source_root,
        executor_model="fixed-model",
        frozen_candidates=frozen,
    )

    assert len(plan.lanes) == 8
    assert {lane.strategy for lane in plan.lanes} == set(P2B_STRATEGIES)
    assert {lane.task_id for lane in plan.lanes} == set(TASKS)
    assert len({lane.history_scope for lane in plan.lanes}) == 8
    assert all(lane.max_rounds == 8 for lane in plan.lanes)
    assert all(lane.model_call_cap == 15 for lane in plan.lanes)
    assert all(lane.gpu_seconds_cap == 3600.0 for lane in plan.lanes)
    assert plan.global_model_call_cap == 120
    assert plan.global_gpu_seconds_cap == 14_400.0
    assert plan.execution_ready

    artifact_root = Path(plan.artifact_root)
    for candidate in plan.frozen_candidates:
        copied = artifact_root / candidate.frozen_path
        assert copied.is_file()
        assert hashlib.sha256(copied.read_bytes()).hexdigest() == candidate.source_sha256
        assert not Path(candidate.frozen_path).is_absolute()

    profile_lanes = [lane for lane in plan.lanes if lane.strategy == "profile_exploit"]
    assert all(lane.starting_candidate_id.endswith("p2-r01") for lane in profile_lanes)
    reset_lanes = [lane for lane in plan.lanes if lane.strategy == "architecture_reset"]
    assert {lane.starting_candidate_id for lane in reset_lanes} == {"reference"}
    recombinant = [
        lane for lane in plan.lanes if lane.strategy == "recombinant_frontier"
    ]
    assert all(len(lane.allowed_frozen_candidate_ids) == 4 for lane in recombinant)

    path = artifact_root / "p2b_plan.json"
    plan.write(path)
    assert P2bPlan.read(path) == plan


def test_p2b_plan_rejects_worktree_artifacts_and_changed_sources(tmp_path: Path) -> None:
    source_root = tmp_path / "p2-source"
    frozen = list(_frozen_inputs(source_root))

    with pytest.raises(ValueError, match="worktree"):
        P2bPlan.build(
            artifact_root=tmp_path / ".claude-manager/worktrees/task/artifacts",
            source_artifact_root=source_root,
            executor_model="fixed-model",
            frozen_candidates=tuple(frozen),
        )

    changed = Path(frozen[0].source_path)
    changed.write_text("class ModelNew: pass\n", encoding="utf-8")
    with pytest.raises(ValueError, match="hash"):
        P2bPlan.build(
            artifact_root=tmp_path / "p2b-artifacts",
            source_artifact_root=source_root,
            executor_model="fixed-model",
            frozen_candidates=tuple(frozen),
        )
