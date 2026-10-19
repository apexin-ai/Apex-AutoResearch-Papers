from __future__ import annotations

import json
from dataclasses import asdict, replace
from pathlib import Path
from typing import Any, Callable

import pytest

from optimization_lab.harness_builder.adapters.sweperf import (
    DATASET_COMMIT,
    DATASET_PARQUET_SHA256,
    EVALUATOR_COMMIT,
    FROZEN_TASKS,
    PATCH_APPLY_MODE,
    PERFORMANCE_REPETITIONS,
    SWEPERF_EVALUATOR_ID,
    CanaryKind,
    DockerWorkspace,
    EvaluationStage,
    EvaluationStatus,
    PatchContractError,
    SWEPerfAdapter,
    StageRequest,
    StageRun,
    canary_plan,
    validate_unified_diff,
)


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "optimization_lab/harness_builder/data/hb_gen1_candidates.json"
IMAGE = "registry.invalid/hb-sweperf@sha256:" + "a" * 64
RECEIPT = "c" * 64
VALID_PATCH = """diff --git a/pkg/core.py b/pkg/core.py
index 1234567..89abcde 100644
--- a/pkg/core.py
+++ b/pkg/core.py
@@ -1,2 +1,2 @@
 def calculate():
-    return slow_path()
+    return fast_path()
"""


def _common_private(request: StageRequest) -> dict[str, Any]:
    binding = request.binding
    return {
        "schema_version": 1,
        "attempt_id": binding.attempt_id,
        "result_nonce": request.result_nonce,
        "stage": request.stage.value,
        "instance_id": binding.instance_id,
        "repository": binding.repository,
        "evaluator": binding.evaluator,
        "evaluator_commit": binding.evaluator_commit,
        "dataset_commit": binding.dataset_commit,
        "dataset_parquet_sha256": binding.dataset_parquet_sha256,
        "base_commit": binding.base_commit,
        "task_sha256": binding.task_sha256,
        "image_ref": binding.image_ref,
        "patch_apply_mode": binding.patch_apply_mode,
        "patch_sha256": binding.patch_sha256,
        "status": "passed",
        "failure_kind": None,
        "elapsed_seconds": 2.0,
    }


class FakeDockerExecutor:
    """In-memory contract double: it never imports or invokes Docker/network code."""

    def __init__(
        self,
        *,
        correctness: str = "passed",
        performance: str = "passed",
        mutate: Callable[[dict[str, Any], StageRequest], None] | None = None,
        reuse_workspace: bool = False,
        fresh: bool = True,
        timeout_stage: EvaluationStage | None = None,
        fail_cleanup: bool = False,
    ):
        self.correctness = correctness
        self.performance = performance
        self.mutate = mutate
        self.reuse_workspace = reuse_workspace
        self.fresh = fresh
        self.timeout_stage = timeout_stage
        self.fail_cleanup = fail_cleanup
        self.events: list[str] = []
        self.bindings = []
        self.copied: list[bytes] = []
        self._workspace_count = 0

    def create_workspace(self, binding):
        self.bindings.append(binding)
        self._workspace_count += 1
        suffix = 1 if self.reuse_workspace else self._workspace_count
        workspace = DockerWorkspace(
            workspace_id=f"workspace-{suffix}",
            attempt_id=binding.attempt_id,
            fresh=self.fresh,
        )
        self.events.append(f"create:{workspace.workspace_id}")
        return workspace

    def copy_candidate(self, workspace: DockerWorkspace, patch: bytes) -> None:
        self.events.append(f"copy:{workspace.workspace_id}")
        self.copied.append(patch)

    def run_stage(
        self, workspace: DockerWorkspace, request: StageRequest
    ) -> StageRun:
        self.events.append(f"run:{request.stage.value}:{workspace.workspace_id}")
        return StageRun(
            returncode=0,
            elapsed_seconds=3.0,
            timed_out=request.stage is self.timeout_stage,
            stdout=(
                '{"status":"passed","correct":true,"score":999999,'
                '"head_commit":"forged"}'
            ),
            stderr="candidate-controlled noise",
        )

    def read_private_result(
        self, workspace: DockerWorkspace, request: StageRequest
    ) -> bytes:
        self.events.append(f"read:{request.stage.value}:{workspace.workspace_id}")
        payload = _common_private(request)
        if request.stage is EvaluationStage.CORRECTNESS:
            payload.update(
                {
                    "patch_applied": True,
                    "tests_passed": 5,
                    "tests_total": 5,
                    "correctness_receipt": RECEIPT,
                }
            )
            if self.correctness == "failed":
                payload.update(
                    {
                        "status": "failed",
                        "failure_kind": "tests_failed",
                        "tests_passed": 4,
                        "correctness_receipt": None,
                    }
                )
            elif self.correctness == "error":
                payload.update(
                    {
                        "status": "error",
                        "failure_kind": "evaluator_error",
                        "patch_applied": False,
                        "tests_passed": 0,
                        "tests_total": 0,
                        "correctness_receipt": None,
                    }
                )
        else:
            measurements = [
                {
                    "test_id": "private-efficiency-node",
                    "reference_seconds": [2.0] * PERFORMANCE_REPETITIONS,
                    "candidate_seconds": [1.0] * PERFORMANCE_REPETITIONS,
                    "candidate_correct": [True] * PERFORMANCE_REPETITIONS,
                }
            ]
            payload.update(
                {
                    "correctness_receipt": request.correctness_receipt,
                    "measurements": measurements,
                    "score": 1.75,
                }
            )
            if self.performance == "failed":
                measurements[0]["candidate_correct"][-1] = False
                payload.update(
                    {
                        "status": "failed",
                        "failure_kind": "measurements_incorrect",
                        "score": None,
                    }
                )
            elif self.performance == "error":
                payload.update(
                    {
                        "status": "error",
                        "failure_kind": "evaluator_error",
                        "measurements": [],
                        "score": None,
                    }
                )
        if self.mutate is not None:
            self.mutate(payload, request)
        return json.dumps(payload, separators=(",", ":")).encode("utf-8")

    def destroy_workspace(self, workspace: DockerWorkspace) -> None:
        self.events.append(f"destroy:{workspace.workspace_id}")
        if self.fail_cleanup:
            raise RuntimeError("fake cleanup failed")


def _adapter(executor: FakeDockerExecutor, *, instance_id: str | None = None):
    return SWEPerfAdapter(
        task=instance_id or next(iter(FROZEN_TASKS)),
        image_ref=IMAGE,
        executor=executor,
    )


def test_frozen_evaluator_dataset_base_commits_and_task_hashes_match_manifest() -> None:
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pool = next(item for item in payload["benchmarks"] if item["suite"] == "swe-perf")

    assert pool["repository_commit"] == EVALUATOR_COMMIT
    assert pool["dataset_commit"] == DATASET_COMMIT
    assert pool["evaluator"] == SWEPERF_EVALUATOR_ID
    assert DATASET_PARQUET_SHA256 == (
        "7c682ebdc080078ad936b6ddcb2b802227e5c91b933bd812077bce7ad6d70253"
    )
    assert tuple(FROZEN_TASKS) == tuple(pool["selected_heldout"])
    assert {
        item["task_id"]: item["source_sha256"] for item in pool["candidates"]
    } == {task_id: task.task_sha256 for task_id, task in FROZEN_TASKS.items()}
    assert {task_id: task.base_commit for task_id, task in FROZEN_TASKS.items()} == {
        "astropy__astropy-13817": "d4fc9d9b96f0879c363a8183842e5cf6067fae37",
        "matplotlib__matplotlib-24250": "f6e75121e11b6ba918c5f6e5c2cc1b9f4fccc8b0",
        "mwaskom__seaborn-2313": "211cabb09bb9228635bdd80f74f7591d36d7b2a7",
        "pydata__xarray-9407": "12d8cfa317b1a08748cb6a0a1b10a6efe3a7d3d2",
        "pylint-dev__pylint-7747": "a29a2ab06cc454867aa89d52c11c4f6fa99d2522",
        "scikit-learn__scikit-learn-12625": "ac327c5ad66fa3d4eb607d007e3684dec872d49a",
        "sphinx-doc__sphinx-12615": "e61f56950d624f5fa540a1c8d4e3baedd2889bd0",
        "sympy__sympy-25205": "ffb5a3f062b8a4ed7125f863f9a254775da6eb46",
    }


def test_adapter_rejects_tampered_task_or_unpinned_image() -> None:
    task = next(iter(FROZEN_TASKS.values()))
    with pytest.raises(ValueError, match="frozen"):
        replace(task, base_commit="0" * 40)
    with pytest.raises(ValueError, match="digest"):
        SWEPerfAdapter(
            task=task,
            image_ref="registry.invalid/hb-sweperf:latest",
            executor=FakeDockerExecutor(),
        )


def test_strict_unified_diff_accepts_canonical_text_patch() -> None:
    summary = validate_unified_diff(VALID_PATCH)

    assert summary.file_paths == ("pkg/core.py",)
    assert summary.hunk_count == 1
    assert summary.added_lines == summary.deleted_lines == 1
    assert summary.sha256


@pytest.mark.parametrize(
    "candidate",
    [
        "",
        f"```diff\n{VALID_PATCH}```\n",
        "--- a/pkg/core.py\n+++ b/pkg/core.py\n@@ -1 +1 @@\n-a\n+b\n",
        VALID_PATCH.replace("pkg/core.py", "../outside.py"),
        VALID_PATCH.replace("\n", "\r\n"),
        VALID_PATCH.replace("@@ -1,2 +1,2 @@", "@@ -1,9 +1,2 @@"),
        VALID_PATCH.replace(
            "diff --git a/pkg/core.py b/pkg/core.py",
            "diff --git a/pkg/core.py b/pkg/faster.py",
        ),
        VALID_PATCH.replace(
            "index 1234567..89abcde 100644",
            "old mode 100644\nnew mode 100755",
        ),
        VALID_PATCH.replace(
            "-    return slow_path()\n+    return fast_path()",
            "     return slow_path()",
        ).replace("@@ -1,2 +1,2 @@", "@@ -1,2 +1,2 @@"),
        VALID_PATCH.replace("+    return fast_path()", "+    return slow_path()"),
    ],
)
def test_strict_unified_diff_rejects_noncanonical_or_noop_candidates(
    candidate: str,
) -> None:
    with pytest.raises(PatchContractError):
        validate_unified_diff(candidate)


def test_contract_rejection_happens_before_a_docker_workspace() -> None:
    executor = FakeDockerExecutor()
    result = _adapter(executor).evaluate("")

    assert result.status is EvaluationStatus.CONTRACT_REJECTED
    assert result.stage_reached is EvaluationStage.CONTRACT
    assert result.evaluator_seconds == 0
    assert executor.events == []


def test_candidate_path_must_be_a_bounded_regular_file(tmp_path: Path) -> None:
    target = tmp_path / "target.diff"
    target.write_text(VALID_PATCH, encoding="utf-8")
    candidate = tmp_path / "candidate.diff"
    candidate.symlink_to(target)
    executor = FakeDockerExecutor()

    result = _adapter(executor).evaluate(candidate)

    assert result.status is EvaluationStatus.CONTRACT_REJECTED
    assert executor.events == []


def test_each_attempt_gets_fresh_workspace_and_runs_correctness_before_performance() -> None:
    executor = FakeDockerExecutor()
    adapter = _adapter(executor)

    first = adapter.evaluate(VALID_PATCH)
    second = adapter.evaluate(VALID_PATCH)

    assert first.status is second.status is EvaluationStatus.VALID
    assert first.score == second.score == pytest.approx(1.75)
    assert first.attempt_id != second.attempt_id
    assert [binding.evaluator_commit for binding in executor.bindings] == [
        EVALUATOR_COMMIT,
        EVALUATOR_COMMIT,
    ]
    assert [binding.dataset_commit for binding in executor.bindings] == [
        DATASET_COMMIT,
        DATASET_COMMIT,
    ]
    assert {binding.patch_apply_mode for binding in executor.bindings} == {
        PATCH_APPLY_MODE
    }
    assert executor.copied == [VALID_PATCH.encode(), VALID_PATCH.encode()]
    assert executor.events == [
        "create:workspace-1",
        "copy:workspace-1",
        "run:correctness:workspace-1",
        "read:correctness:workspace-1",
        "run:performance:workspace-1",
        "read:performance:workspace-1",
        "destroy:workspace-1",
        "create:workspace-2",
        "copy:workspace-2",
        "run:correctness:workspace-2",
        "read:correctness:workspace-2",
        "run:performance:workspace-2",
        "read:performance:workspace-2",
        "destroy:workspace-2",
    ]


def test_candidate_stdout_cannot_forge_a_pass_and_performance_is_not_run() -> None:
    executor = FakeDockerExecutor(correctness="failed")

    result = _adapter(executor).evaluate(VALID_PATCH)

    assert result.status is EvaluationStatus.INCORRECT
    assert result.stage_reached is EvaluationStage.CORRECTNESS
    assert result.score is None
    assert result.failure_kind == "tests_failed"
    assert not any("performance" in event for event in executor.events)
    assert "999999" not in json.dumps(result.public_feedback())
    assert executor.events[-1] == "destroy:workspace-1"


@pytest.mark.parametrize(
    "mutation",
    [
        lambda payload, request: payload.__setitem__("base_commit", "0" * 40),
        lambda payload, request: payload.__setitem__("task_sha256", "f" * 64),
        lambda payload, request: payload.__setitem__("head_commit", "1" * 40),
    ],
)
def test_private_result_must_match_exact_binding_and_schema(mutation) -> None:
    executor = FakeDockerExecutor(mutate=mutation)

    result = _adapter(executor).evaluate(VALID_PATCH)

    assert result.status is EvaluationStatus.ENVIRONMENT_INVALID
    assert result.failure_kind == "private_evaluator_contract_failure"
    assert executor.events[-1] == "destroy:workspace-1"


def test_private_performance_score_wins_over_forged_stdout() -> None:
    result = _adapter(FakeDockerExecutor()).evaluate(VALID_PATCH)

    assert result.status is EvaluationStatus.VALID
    assert result.score == pytest.approx(1.75)
    assert set(result.public_feedback()) == {
        "status",
        "stage_reached",
        "correct",
        "score",
        "failure_kind",
        "evaluator_seconds",
    }


def test_every_timed_invocation_is_bound_to_correctness() -> None:
    def forge_one_measurement(payload: dict[str, Any], request: StageRequest) -> None:
        if request.stage is EvaluationStage.PERFORMANCE:
            payload["measurements"][0]["candidate_correct"][-1] = False

    result = _adapter(FakeDockerExecutor(mutate=forge_one_measurement)).evaluate(
        VALID_PATCH
    )

    assert result.status is EvaluationStatus.ENVIRONMENT_INVALID
    assert result.stage_reached is EvaluationStage.PERFORMANCE
    assert result.score is None


def test_performance_failure_is_incorrect_and_never_updates_score() -> None:
    result = _adapter(FakeDockerExecutor(performance="failed")).evaluate(VALID_PATCH)

    assert result.status is EvaluationStatus.INCORRECT
    assert result.stage_reached is EvaluationStage.PERFORMANCE
    assert result.correct is False
    assert result.score is None


def test_timeout_stops_before_reading_private_or_later_stage_and_cleans_up() -> None:
    executor = FakeDockerExecutor(timeout_stage=EvaluationStage.CORRECTNESS)

    result = _adapter(executor).evaluate(VALID_PATCH)

    assert result.status is EvaluationStatus.TIMEOUT
    assert executor.events == [
        "create:workspace-1",
        "copy:workspace-1",
        "run:correctness:workspace-1",
        "destroy:workspace-1",
    ]


def test_executor_cannot_reuse_or_leave_a_workspace_dirty() -> None:
    reuse = FakeDockerExecutor(reuse_workspace=True)
    adapter = _adapter(reuse)
    assert adapter.evaluate(VALID_PATCH).status is EvaluationStatus.VALID
    reused = adapter.evaluate(VALID_PATCH)

    assert reused.status is EvaluationStatus.ENVIRONMENT_INVALID
    assert reused.failure_kind == "private_evaluator_contract_failure"
    assert reuse.events[-1] == "destroy:workspace-1"

    cleanup = FakeDockerExecutor(fail_cleanup=True)
    cleanup_result = _adapter(cleanup).evaluate(VALID_PATCH)
    assert cleanup_result.status is EvaluationStatus.ENVIRONMENT_INVALID
    assert cleanup_result.failure_kind == "workspace_cleanup_failed"


def test_public_context_and_attempt_binding_never_expose_private_solution_fields() -> None:
    executor = FakeDockerExecutor()
    adapter = _adapter(executor)
    context = adapter.public_task_context(
        problem_statement="Make the selected operation faster without changing behavior.",
        allowed_repository_files=("pkg/core.py", "pkg/helpers.py"),
    )
    adapter.evaluate(VALID_PATCH)

    forbidden = {"patch", "human_patch", "head_commit", "test_patch"}
    assert forbidden.isdisjoint(context)
    assert forbidden.isdisjoint(asdict(executor.bindings[0]))
    assert context["base_commit"] == executor.bindings[0].base_commit
    assert context["allowed_repository_files"] == ("pkg/core.py", "pkg/helpers.py")


def test_reference_noop_and_adversarial_canary_plan_is_opaque_and_complete() -> None:
    cases = canary_plan()

    assert len(cases) == len(FROZEN_TASKS) + 3 == 11
    for instance_id in FROZEN_TASKS:
        per_task = [case for case in cases if case.instance_id == instance_id]
        assert CanaryKind.REFERENCE in {case.kind for case in per_task}
        by_kind = {case.kind: case for case in per_task}
        assert by_kind[CanaryKind.REFERENCE].expected_status is EvaluationStatus.VALID
        assert by_kind[CanaryKind.REFERENCE].run_performance is True

    adversarial = [case for case in cases if case.kind is not CanaryKind.REFERENCE]
    assert {case.kind for case in adversarial} == {
        CanaryKind.NO_OP,
        CanaryKind.ADVERSARIAL_STDOUT,
        CanaryKind.CORRECTNESS_REGRESSION,
    }
    assert len({case.instance_id for case in adversarial}) == 1
    by_kind = {case.kind: case for case in adversarial}
    assert by_kind[CanaryKind.NO_OP].expected_status is EvaluationStatus.CONTRACT_REJECTED
    assert by_kind[CanaryKind.NO_OP].reaches_evaluator is False
    assert by_kind[CanaryKind.ADVERSARIAL_STDOUT].expected_status is EvaluationStatus.INCORRECT
    assert by_kind[CanaryKind.ADVERSARIAL_STDOUT].stdout_must_be_ignored
    assert by_kind[CanaryKind.CORRECTNESS_REGRESSION].expected_status is EvaluationStatus.INCORRECT
    assert by_kind[CanaryKind.CORRECTNESS_REGRESSION].reaches_evaluator is True

    serialized = json.dumps([asdict(case) for case in cases])
    assert "human_patch" not in serialized
    assert "head_commit" not in serialized
    assert "diff --git" not in serialized
