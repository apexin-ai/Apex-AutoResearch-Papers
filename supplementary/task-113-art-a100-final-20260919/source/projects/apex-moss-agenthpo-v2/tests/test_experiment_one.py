from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path

import pytest

from optimization_lab.harness_builder.solutions import SolutionContractError

from optimization_lab.harness_builder.dual_harness import (
    TaskHarnessArtifact,
    TaskHarnessNode,
    TaskHarnessSpec,
)
from optimization_lab.harness_builder.experiment_one import (
    CallLedgerEvidence,
    CrossMatrixRunner,
    ExperimentOneManifest,
    FreezeReceipt,
    HarnessTransferProvenance,
    H0BaselineReceipt,
    LineageRoundResult,
    LineageRunner,
    ModelConfiguration,
    OfficialEvaluationResult,
    TargetBinding,
    TaskExecutionResult,
    select_best_round,
)


def _sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _harness(prompt: str = "Solve the supplied task carefully: {task}") -> TaskHarnessArtifact:
    return TaskHarnessArtifact(
        schema_version=1,
        version=1,
        parent_sha256=None,
        spec=TaskHarnessSpec(
            schema_version=1,
            nodes=(
                TaskHarnessNode(
                    node_id="solve",
                    kind="model_call",
                    role="solver",
                    prompt=prompt,
                ),
                TaskHarnessNode(node_id="emit", kind="emit"),
            ),
        ),
    )


def _model_config(**changes: object) -> ModelConfiguration:
    payload: dict[str, object] = {
        "provider": "openai-compatible",
        "api_family": "responses",
        "transport": "https",
        "model": "gpt-5.6-sol",
        "reasoning_effort": "high",
        "max_output_tokens": 8192,
        "sampling_parameters": {},
        "tool_permission_policy": {"mode": "allowlist", "tools": []},
    }
    payload.update(changes)
    return ModelConfiguration(**payload)


def _target(position: str) -> TargetBinding:
    return TargetBinding(
        position=position,
        task_id=f"official-task-{position}",
        task=f"Public statement for target {position}",
        submission_path=f"submissions/{position}/solution.py",
        evaluator_contract_sha256=_sha(f"evaluator-{position}"),
        score_direction="maximize",
    )


def _manifest(*, h0: TaskHarnessArtifact | None = None) -> ExperimentOneManifest:
    config = _model_config()
    return ExperimentOneManifest(
        schema_version=1,
        experiment_id="edgebench-specialization",
        benchmark="edgebench",
        seed_id="S1",
        rounds=8,
        h0=h0 or _harness(),
        targets=tuple(_target(position) for position in "ABC"),
        builder_model_configuration=config,
        solver_model_configuration=config,
        moss_revision_sha256=_sha("moss-revision"),
        tracked_tree_sha256=_sha("clean-tree"),
        source_revision_sha256=_sha("official-source"),
        task_data_revision_sha256=_sha("official-data"),
        image_digest_sha256=_sha("judge-image"),
        api_base_host_sha256=_sha("api-host"),
    )


def _advance_harness(request, *, suffix: str = "") -> TaskHarnessArtifact:
    current = request.workspace.current()
    child = TaskHarnessArtifact(
        schema_version=1,
        version=current.version + 1,
        parent_sha256=current.sha256,
        spec=TaskHarnessSpec(
            schema_version=1,
            nodes=(
                TaskHarnessNode(
                    node_id="solve",
                    kind="model_call",
                    role="solver",
                    prompt=(
                        "Use a generic bounded search and verify the emitted artifact. "
                        f"Iteration {request.round_index}{suffix}: {{task}}"
                    ),
                ),
                TaskHarnessNode(node_id="emit", kind="emit"),
            ),
        ),
    )
    request.workspace.commit(child)
    return child


def _round_result(request, *, score: float | None = None, valid: bool = True):
    current_sha = request.workspace.current().sha256
    child = _advance_harness(request)
    round_score = float(request.round_index) if score is None else score
    return LineageRoundResult(
        evaluated_harness_sha256=current_sha,
        next_harness_sha256=child.sha256,
        candidate_sha256=_sha(f"candidate-{request.position}-{request.round_index}"),
        official_score=round_score,
        official_score_valid=valid,
        public_feedback="public aggregate only",
        evaluator_receipt_sha256=_sha(f"eval-{request.position}-{request.round_index}"),
        private_evidence_sha256=_sha(f"private-{request.position}-{request.round_index}"),
        audit_ledger_sha256=_sha(f"audit-{request.position}-{request.round_index}"),
    )


def _round_factory(executor):
    return lambda _position, _lineage_root: executor


def _execution(request, candidate: str) -> TaskExecutionResult:
    return TaskExecutionResult(
        candidate=candidate,
        candidate_sha256=_sha(candidate),
        candidate_archive_sha256=_sha(f"archive-{candidate}"),
        call_ledger=CallLedgerEvidence(
            operation_id=request.operation_id,
            builder_constructed_count=0,
            builder_call_count=0,
            solver_call_count=1,
            memory_read_count=0,
            audit_ledger_sha256=_sha(f"audit-{request.operation_id}"),
        ),
    )


def _cell_factories(solve, evaluate):
    return {
        "task_executor_factory": lambda _root, _operation_id: solve,
        "evaluator_factory": lambda _root, _operation_id: evaluate,
    }


def _tamper_enveloped_field(path: Path, field_name: str, value: object) -> None:
    envelope = json.loads(path.read_text(encoding="utf-8"))
    envelope["payload"][field_name] = value
    encoded_payload = json.dumps(
        envelope["payload"],
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    envelope["payload_sha256"] = hashlib.sha256(encoded_payload).hexdigest()
    path.write_text(
        json.dumps(
            envelope,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
        encoding="utf-8",
    )


def test_manifest_requires_the_frozen_three_target_eight_round_model_contract() -> None:
    manifest = _manifest()
    assert tuple(target.position for target in manifest.targets) == ("A", "B", "C")
    assert manifest.rounds == 8
    assert manifest.builder_model_configuration.sha256 == manifest.solver_model_configuration.sha256

    with pytest.raises(ValueError, match="exactly A, B, and C"):
        replace(manifest, targets=manifest.targets[:2])
    with pytest.raises(ValueError, match="eight rounds"):
        replace(manifest, rounds=7)
    with pytest.raises(ValueError, match="gpt-5.6-sol"):
        replace(manifest, solver_model_configuration=_model_config(model="other"))
    with pytest.raises(ValueError, match="identical"):
        replace(manifest, solver_model_configuration=_model_config(max_output_tokens=4096))


def test_initialize_all_creates_isolated_byte_identical_h0_workspaces(tmp_path: Path) -> None:
    manifest = _manifest()
    runners = LineageRunner.initialize_all(
        manifest=manifest,
        experiment_root=tmp_path,
        round_executor_factory=_round_factory(lambda request: _round_result(request)),
    )

    assert tuple(runners) == ("A", "B", "C")
    roots = [runner.workspace.root for runner in runners.values()]
    assert len(set(roots)) == 3
    h0_paths = [runner.workspace.artifact_path(manifest.h0.sha256) for runner in runners.values()]
    assert len({path.read_bytes() for path in h0_paths}) == 1
    assert all(runner.workspace.current().sha256 == manifest.h0.sha256 for runner in runners.values())


def test_each_isolated_lineage_consumes_exactly_eight_rounds(tmp_path: Path) -> None:
    calls: list[tuple[str, int, Path]] = []

    def execute(request):
        calls.append((request.position, request.round_index, request.workspace.root))
        return _round_result(request)

    runners = LineageRunner.initialize_all(
        manifest=_manifest(), experiment_root=tmp_path, round_executor_factory=_round_factory(execute)
    )
    receipts = {position: runner.run() for position, runner in runners.items()}

    assert len(calls) == 24
    for position in "ABC":
        assert [item.round_index for item in receipts[position]] == list(range(1, 9))
        assert all(item.position == position for item in receipts[position])
        assert len({item.operation_id for item in receipts[position]}) == 8
    assert len({root for _, _, root in calls}) == 3


def test_best_harness_selection_uses_score_then_earliest_round_then_sha(tmp_path: Path) -> None:
    runner = LineageRunner.initialize_all(
        manifest=_manifest(),
        experiment_root=tmp_path,
        round_executor_factory=_round_factory(lambda request: _round_result(request)),
    )["A"]
    receipts = list(runner.run())
    high = replace(receipts[0], official_score=10.0, harness_sha256="f" * 64)
    later = replace(receipts[1], official_score=10.0, harness_sha256="0" * 64)
    lexical = replace(high, harness_sha256="0" * 64)

    assert select_best_round((receipts[2], high, later)).round_index == 1
    assert select_best_round((high, lexical)).harness_sha256 == "0" * 64
    assert select_best_round((receipts[2], later)).official_score == 10.0


def test_freeze_requires_a_valid_finite_numeric_official_score(tmp_path: Path) -> None:
    runner = LineageRunner.initialize_all(
        manifest=_manifest(),
        experiment_root=tmp_path,
        round_executor_factory=_round_factory(
            lambda request: _round_result(request, score=None, valid=False)
        ),
    )["A"]
    runner.run()

    with pytest.raises(ValueError, match="valid numeric official score"):
        runner.freeze()


def test_freeze_is_immutable_and_binds_complete_harness_ancestry(tmp_path: Path) -> None:
    runner = LineageRunner.initialize_all(
        manifest=_manifest(),
        experiment_root=tmp_path,
        round_executor_factory=_round_factory(lambda request: _round_result(request)),
    )["A"]
    runner.run()
    receipt = runner.freeze()

    assert isinstance(receipt, FreezeReceipt)
    assert receipt.valid is True
    assert receipt.ancestry_sha256s[0] == runner.manifest.h0.sha256
    assert receipt.ancestry_sha256s[-1] == receipt.harness_sha256
    assert runner.freeze() == receipt
    freeze_path = runner.root / "freeze_receipt.json"
    payload = json.loads(freeze_path.read_text(encoding="utf-8"))
    payload["official_score"] = -999
    freeze_path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="integrity|overwrite|receipt"):
        runner.freeze()


def test_started_without_result_is_abandoned_and_operation_id_is_never_reissued(tmp_path: Path) -> None:
    calls: list[str] = []

    def crash(request):
        calls.append(request.operation_id)
        if request.round_index == 1:
            raise KeyboardInterrupt("simulated process death")
        return _round_result(request)

    runner = LineageRunner.initialize_all(
        manifest=_manifest(), experiment_root=tmp_path, round_executor_factory=_round_factory(crash)
    )["A"]
    with pytest.raises(KeyboardInterrupt):
        runner.run()

    resumed = LineageRunner(
        manifest=runner.manifest,
        position="A",
        root=runner.root,
        round_executor_factory=_round_factory(crash),
    )
    receipts = resumed.run()

    assert receipts[0].status == "abandoned"
    assert receipts[0].consumed_budget is True
    assert calls.count(receipts[0].operation_id) == 1
    assert len(receipts) == 8


def test_public_solution_contract_failure_is_recorded_with_its_specific_reason(
    tmp_path: Path,
) -> None:
    def reject_candidate(request):
        raise SolutionContractError(
            "ALE-Bench response must be exactly one fenced source file"
        )

    runner = LineageRunner.initialize_all(
        manifest=_manifest(),
        experiment_root=tmp_path,
        round_executor_factory=_round_factory(reject_candidate),
    )["A"]

    receipt = runner.run()[0]

    assert receipt.status == "abandoned"
    assert receipt.public_feedback == (
        "terminal abandonment: SolutionContractError: "
        "ALE-Bench response must be exactly one fenced source file"
    )


def test_started_round_rolls_back_a_committed_child_before_resuming(tmp_path: Path) -> None:
    manifest = _manifest()
    crashed_child_sha256: list[str] = []
    resumed_round_starts: dict[int, str] = {}

    def crash_after_commit(request):
        resumed_round_starts[request.round_index] = request.workspace.current().sha256
        if request.round_index == 1:
            crashed_child_sha256.append(_advance_harness(request, suffix="-crashed").sha256)
            raise KeyboardInterrupt("simulated death after Harness commit")
        return _round_result(request)

    runner = LineageRunner.initialize_all(
        manifest=manifest,
        experiment_root=tmp_path,
        round_executor_factory=_round_factory(crash_after_commit),
    )["A"]
    with pytest.raises(KeyboardInterrupt):
        runner.run()
    assert runner.workspace.current().sha256 == crashed_child_sha256[0]

    resumed = LineageRunner(
        manifest=manifest,
        position="A",
        root=runner.root,
        round_executor_factory=_round_factory(crash_after_commit),
    )
    receipts = resumed.run()
    freeze = resumed.freeze()

    assert receipts[0].status == "abandoned"
    assert receipts[0].harness_sha256 == manifest.h0.sha256
    assert receipts[0].next_harness_sha256 == manifest.h0.sha256
    assert resumed_round_starts[2] == manifest.h0.sha256
    assert crashed_child_sha256[0] not in freeze.ancestry_sha256s
    assert all(
        receipt.harness_sha256 != crashed_child_sha256[0]
        and receipt.next_harness_sha256 != crashed_child_sha256[0]
        for receipt in receipts[1:]
    )


def test_lineage_factory_creates_one_executor_per_isolated_root(tmp_path: Path) -> None:
    factory_calls: list[tuple[str, Path, object]] = []

    def factory(position: str, lineage_root: Path):
        identity = object()
        factory_calls.append((position, lineage_root, identity))

        def execute(request):
            assert request.position == position
            assert request.lineage_root == lineage_root
            return _round_result(request)

        return execute

    runners = LineageRunner.initialize_all(
        manifest=_manifest(),
        experiment_root=tmp_path,
        round_executor_factory=factory,
    )
    for runner in runners.values():
        runner.run()

    assert [position for position, _, _ in factory_calls] == list("ABC")
    assert len({root for _, root, _ in factory_calls}) == 3
    assert len({id(identity) for _, _, identity in factory_calls}) == 3


def _frozen_triplet(tmp_path: Path, manifest: ExperimentOneManifest):
    runners = LineageRunner.initialize_all(
        manifest=manifest,
        experiment_root=tmp_path / "evolution",
        round_executor_factory=_round_factory(lambda request: _round_result(request)),
    )
    freezes = {}
    harnesses = {}
    freeze_paths = {}
    provenance = {}
    for position, runner in runners.items():
        runner.run()
        freezes[position] = runner.freeze()
        harnesses[position] = runner.workspace.load_artifact(freezes[position].harness_sha256)
        freeze_paths[position] = runner.root / "freeze_receipt.json"
        provenance[position] = HarnessTransferProvenance.cleared(
            source_position=position,
            harness=harnesses[position],
        )
    return freezes, harnesses, freeze_paths, provenance


def test_cross_matrix_is_nine_one_shot_no_builder_cells_without_source_state(
    tmp_path: Path,
) -> None:
    manifest = _manifest()
    freezes, harnesses, freeze_paths, provenance = _frozen_triplet(tmp_path, manifest)
    solver_requests = []
    evaluated_candidates: list[str] = []

    def solve(request):
        solver_requests.append(request)
        assert request.history == ()
        assert dict(request.memory) == {}
        assert not hasattr(request, "source_candidate")
        assert not hasattr(request, "source_score")
        assert not hasattr(request, "source_feedback")
        candidate = f"opaque-candidate-{request.source_position}-{request.target.position}"
        return _execution(request, candidate)

    def evaluate(request):
        evaluated_candidates.append(request.candidate.candidate)
        return OfficialEvaluationResult(
            score=1.0,
            valid=True,
            public_feedback="valid aggregate",
            evaluator_receipt_sha256=_sha(f"eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    runner = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    )
    receipts = runner.run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )

    assert len(receipts) == 9
    assert len(solver_requests) == len(evaluated_candidates) == 9
    assert {(item.source_position, item.target_position) for item in receipts} == {
        (source, target) for source in "ABC" for target in "ABC"
    }
    assert all(item.builder_constructed_count == 0 for item in receipts)
    assert all(item.builder_call_count == 0 for item in receipts)
    assert all(item.solver_call_count == 1 for item in receipts)
    assert all(item.official_evaluator_call_count == 1 for item in receipts)
    assert "opaque-candidate" not in json.dumps([item.to_dict() for item in receipts])

    replay = runner.run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )
    assert replay == receipts
    assert len(solver_requests) == len(evaluated_candidates) == 9


def test_cross_solver_failure_is_a_terminal_audit_without_score_or_retry(
    tmp_path: Path,
) -> None:
    manifest = _manifest()
    freezes, harnesses, freeze_paths, provenance = _frozen_triplet(tmp_path, manifest)
    solver_calls: list[str] = []
    evaluator_calls: list[str] = []

    def solve(request):
        solver_calls.append(request.operation_id)
        if request.source_position == "A" and request.target.position == "B":
            raise RuntimeError("solver provider unavailable")
        return _execution(request, f"candidate-{request.operation_id}")

    def evaluate(request):
        evaluator_calls.append(request.operation_id)
        return OfficialEvaluationResult(
            score=0.5,
            valid=True,
            public_feedback="valid",
            evaluator_receipt_sha256=_sha(f"eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    runner = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    )
    receipts = runner.run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )
    failed = next(
        item for item in receipts if item.source_position == "A" and item.target_position == "B"
    )
    failed_root = tmp_path / "cross" / "cross_matrix" / "A-to-B"
    error = json.loads((failed_root / "error.evidence.json").read_text(encoding="utf-8"))
    error = error["payload"]
    assert failed.status == "invalid"
    assert failed.official_score is None
    assert failed.official_score_valid is False
    assert failed.evaluator_receipt_sha256 is None
    assert failed.candidate_sha256 is None
    assert failed_root.joinpath("receipt.json").is_file()
    assert not failed_root.joinpath("evaluation.evidence.json").exists()
    assert error["failure_stage"] == "solver"
    assert error["error_type"] == "RuntimeError"
    assert error["official_score"] is None
    assert error["retry"] is False
    assert failed.operation_journal_head_sha256
    assert len(evaluator_calls) == 8

    replay = runner.run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )
    assert replay == receipts
    assert solver_calls.count("S1-cross-A-to-B") == 1
    assert "S1-cross-A-to-B" not in evaluator_calls


def test_cross_solver_failure_receipt_preserves_partial_audit_ledger(
    tmp_path: Path,
) -> None:
    manifest = _manifest()
    freezes, harnesses, freeze_paths, provenance = _frozen_triplet(tmp_path, manifest)

    def solve(request):
        if request.source_position == "A" and request.target.position == "B":
            ledger = request.cell_root / "audit" / "solver_model_calls.jsonl"
            ledger.parent.mkdir(parents=True, exist_ok=True)
            ledger.write_text(
                json.dumps(
                    {
                        "event": "start",
                        "operation_id": f"{request.operation_id}-solver-0000",
                    }
                )
                + "\n"
                + json.dumps(
                    {
                        "event": "error",
                        "operation_id": f"{request.operation_id}-solver-0000",
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            raise RuntimeError("solver provider unavailable")
        return _execution(request, f"candidate-{request.operation_id}")

    def evaluate(request):
        return OfficialEvaluationResult(
            score=0.5,
            valid=True,
            public_feedback="valid",
            evaluator_receipt_sha256=_sha(f"eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    runner = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    )
    receipts = runner.run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )

    failed = next(
        item for item in receipts if item.source_position == "A" and item.target_position == "B"
    )
    ledger_path = tmp_path / "cross" / "cross_matrix" / "A-to-B" / "audit" / "solver_model_calls.jsonl"
    error = json.loads(
        (tmp_path / "cross" / "cross_matrix" / "A-to-B" / "error.evidence.json").read_text(
            encoding="utf-8"
        )
    )["payload"]

    assert failed.solver_call_count == 1
    assert failed.audit_ledger_sha256 == hashlib.sha256(ledger_path.read_bytes()).hexdigest()
    assert error["solver_call_count"] == 1
    assert error["audit_ledger_sha256"] == failed.audit_ledger_sha256


def test_cross_and_h0_cells_have_independent_factories_roots_and_freeze_authorization(
    tmp_path: Path,
) -> None:
    manifest = _manifest()
    freezes, harnesses, freeze_paths, provenance = _frozen_triplet(tmp_path, manifest)
    executor_factories: list[tuple[Path, str, object]] = []
    evaluator_factories: list[tuple[Path, str, object]] = []

    def executor_factory(cell_root: Path, operation_id: str):
        identity = object()
        executor_factories.append((cell_root, operation_id, identity))

        def solve(request):
            assert request.cell_root == cell_root
            assert request.operation_id == operation_id
            return _execution(request, f"candidate-{operation_id}")

        return solve

    def evaluator_factory(cell_root: Path, operation_id: str):
        identity = object()
        evaluator_factories.append((cell_root, operation_id, identity))

        def evaluate(request):
            assert request.cell_root == cell_root
            assert request.operation_id == operation_id
            if "-cross-" in operation_id:
                position = request.freeze_lineage_position
                assert request.private_eval_allowed is True
                assert position in "ABC"
                assert request.freeze_receipt_path == freeze_paths[position].resolve()
                assert request.freeze_receipt_sha256 == freezes[position].sha256
                assert request.freeze_candidate_sha256 == freezes[position].candidate_sha256
                assert request.freeze_public_score == freezes[position].official_score
            else:
                assert request.private_eval_allowed is False
                assert request.freeze_receipt_path is None
                assert request.freeze_receipt_sha256 is None
                assert request.freeze_lineage_position is None
                assert request.freeze_candidate_sha256 is None
                assert request.freeze_public_score is None
            return OfficialEvaluationResult(
                score=1.0,
                valid=True,
                public_feedback="valid",
                evaluator_receipt_sha256=_sha(f"eval-{operation_id}"),
                private_evidence_sha256=_sha(f"private-{operation_id}"),
            )

        return evaluate

    runner = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        task_executor_factory=executor_factory,
        evaluator_factory=evaluator_factory,
    )
    runner.run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )
    runner.run_h0_baselines()

    assert len(executor_factories) == len(evaluator_factories) == 12
    assert len({root for root, _, _ in executor_factories}) == 12
    assert len({operation_id for _, operation_id, _ in executor_factories}) == 12
    assert len({id(identity) for _, _, identity in executor_factories}) == 12
    assert len({id(identity) for _, _, identity in evaluator_factories}) == 12
    assert [(root, operation_id) for root, operation_id, _ in executor_factories] == [
        (root, operation_id) for root, operation_id, _ in evaluator_factories
    ]


@pytest.mark.parametrize(
    "ledger_changes",
    (
        {"builder_constructed_count": 1},
        {"builder_call_count": 1},
        {"solver_call_count": 2},
        {"memory_read_count": 1},
    ),
)
def test_invalid_frozen_call_ledger_marks_only_that_cell_invalid_and_continues(
    tmp_path: Path, ledger_changes: dict[str, int]
) -> None:
    manifest = _manifest()
    freezes, harnesses, freeze_paths, provenance = _frozen_triplet(tmp_path, manifest)
    evaluator_calls: list[str] = []

    def solve(request):
        result = _execution(request, f"candidate-{request.operation_id}")
        if request.operation_id.endswith("cross-A-to-A"):
            ledger = {
                "operation_id": request.operation_id,
                "builder_constructed_count": 0,
                "builder_call_count": 0,
                "solver_call_count": 1,
                "memory_read_count": 0,
                "audit_ledger_sha256": _sha(f"audit-{request.operation_id}"),
            }
            ledger.update(ledger_changes)
            return replace(result, call_ledger=CallLedgerEvidence(**ledger))
        return result

    def evaluate(request):
        evaluator_calls.append(request.operation_id)
        return OfficialEvaluationResult(
            score=1.0,
            valid=True,
            public_feedback="valid",
            evaluator_receipt_sha256=_sha(f"eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    receipts = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    ).run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )

    assert len(receipts) == 9
    assert receipts[0].status == "invalid"
    assert receipts[0].official_score_valid is False
    assert all(receipt.status == "completed" for receipt in receipts[1:])
    assert len(evaluator_calls) == 8


def test_invalid_evaluator_result_writes_terminal_receipt_and_continues_matrix(
    tmp_path: Path,
) -> None:
    manifest = _manifest()
    freezes, harnesses, freeze_paths, provenance = _frozen_triplet(tmp_path, manifest)

    def solve(request):
        return _execution(request, f"candidate-{request.operation_id}")

    def evaluate(request):
        if request.operation_id.endswith("cross-A-to-A"):
            return object()
        return OfficialEvaluationResult(
            score=1.0,
            valid=True,
            public_feedback="valid",
            evaluator_receipt_sha256=_sha(f"eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    receipts = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    ).run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )

    assert len(receipts) == 9
    assert receipts[0].status == "invalid"
    assert all(receipt.status == "completed" for receipt in receipts[1:])


def test_cross_started_without_result_is_abandoned_without_reissuing_operation(
    tmp_path: Path,
) -> None:
    manifest = _manifest()
    freezes, harnesses, freeze_paths, provenance = _frozen_triplet(tmp_path, manifest)
    calls: list[str] = []

    def solve(request):
        calls.append(request.operation_id)
        if request.operation_id.endswith("cross-A-to-A"):
            raise KeyboardInterrupt("simulated cell process death")
        return _execution(request, f"candidate-{request.operation_id}")

    def evaluate(request):
        return OfficialEvaluationResult(
            score=1.0,
            valid=True,
            public_feedback="valid",
            evaluator_receipt_sha256=_sha(f"eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    root = tmp_path / "cross"
    first = CrossMatrixRunner(
        manifest=manifest,
        root=root,
        **_cell_factories(solve, evaluate),
    )
    with pytest.raises(KeyboardInterrupt):
        first.run(
            freeze_receipts=freezes,
            frozen_harnesses=harnesses,
            freeze_receipt_paths=freeze_paths,
            transfer_provenance=provenance,
        )

    resumed = CrossMatrixRunner(
        manifest=manifest,
        root=root,
        **_cell_factories(solve, evaluate),
    )
    receipts = resumed.run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )

    assert len(receipts) == 9
    assert receipts[0].status == "abandoned"
    assert all(receipt.status == "completed" for receipt in receipts[1:])
    assert calls.count("S1-cross-A-to-A") == 1
    assert (root / "cross_matrix" / "A-to-A" / "operation.abandoned.json").is_file()


@pytest.mark.parametrize(
    "field_name",
    (
        "source_revision_sha256",
        "task_data_revision_sha256",
        "image_digest_sha256",
        "api_base_host_sha256",
        "evaluator_contract_sha256",
        "task_sha256",
        "harness_sha256",
        "solver_model_configuration_sha256",
        "candidate_sha256",
        "evaluator_receipt_sha256",
        "private_evidence_sha256",
        "audit_ledger_sha256",
    ),
)
def test_cross_replay_rejects_rehashed_tampering_of_all_bound_evidence(
    tmp_path: Path, field_name: str
) -> None:
    manifest = _manifest()
    freezes, harnesses, freeze_paths, provenance = _frozen_triplet(tmp_path, manifest)

    def solve(request):
        return _execution(request, f"candidate-{request.operation_id}")

    def evaluate(request):
        return OfficialEvaluationResult(
            score=1.0,
            valid=True,
            public_feedback="valid",
            evaluator_receipt_sha256=_sha(f"eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    runner = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    )
    runner.run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )
    receipt_path = tmp_path / "cross" / "cross_matrix" / "A-to-A" / "receipt.json"
    _tamper_enveloped_field(receipt_path, field_name, _sha(f"tampered-{field_name}"))

    with pytest.raises(
        ValueError,
        match="replay evidence|execution evidence|evaluation evidence",
    ):
        runner.run(
            freeze_receipts=freezes,
            frozen_harnesses=harnesses,
            freeze_receipt_paths=freeze_paths,
            transfer_provenance=provenance,
        )


def test_target_binding_is_separate_and_target_material_is_rejected_from_harness(
    tmp_path: Path,
) -> None:
    manifest = _manifest()
    freezes, harnesses, freeze_paths, provenance = _frozen_triplet(tmp_path, manifest)
    observed = []

    def solve(request):
        observed.append(request)
        assert request.harness.to_json().find(request.target.task_id) == -1
        assert request.harness.to_json().find(request.target.submission_path) == -1
        return _execution(request, "answer")

    def evaluate(request):
        return OfficialEvaluationResult(
            score=0.0,
            valid=True,
            public_feedback="valid zero",
            evaluator_receipt_sha256=_sha(request.operation_id),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    ).run(
        freeze_receipts=freezes,
        frozen_harnesses=harnesses,
        freeze_receipt_paths=freeze_paths,
        transfer_provenance=provenance,
    )
    assert len(observed) == 9

    with pytest.raises(ValueError, match="source-private"):
        replace(
            provenance["A"],
            source_private_material_sha256s=(_sha("source candidate"),),
        )

    forged_provenance = dict(provenance)
    forged_provenance["A"] = replace(
        provenance["A"],
        cleared_private_state_sha256=_sha("not-cleared"),
    )
    with pytest.raises(ValueError, match="transfer provenance"):
        CrossMatrixRunner(
            manifest=manifest,
            root=tmp_path / "poisoned",
            **_cell_factories(solve, evaluate),
        ).run(
            freeze_receipts=freezes,
            frozen_harnesses=harnesses,
            freeze_receipt_paths=freeze_paths,
            transfer_provenance=forged_provenance,
        )


def test_h0_baselines_use_fresh_roots_and_exact_zero_one_one_call_ledger(
    tmp_path: Path,
) -> None:
    manifest = _manifest()
    solver_calls = []
    evaluator_calls = []

    def solve(request):
        solver_calls.append(request)
        assert request.harness.sha256 == manifest.h0.sha256
        return _execution(request, f"baseline-{request.target.position}")

    def evaluate(request):
        evaluator_calls.append(request)
        return OfficialEvaluationResult(
            score=0.0,
            valid=True,
            public_feedback="valid zero",
            evaluator_receipt_sha256=_sha(f"baseline-eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"baseline-private-{request.operation_id}"),
        )

    runner = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    )
    receipts = runner.run_h0_baselines()

    assert len(receipts) == 3
    assert len(solver_calls) == len(evaluator_calls) == 3
    assert all(isinstance(item, H0BaselineReceipt) for item in receipts)
    assert all(item.builder_constructed_count == 0 for item in receipts)
    assert all(item.builder_call_count == 0 for item in receipts)
    assert all(item.solver_call_count == 1 for item in receipts)
    assert all(item.official_evaluator_call_count == 1 for item in receipts)
    assert all(
        item.upper_model_configuration_sha256
        == item.lower_model_configuration_sha256
        == manifest.builder_model_configuration.sha256
        for item in receipts
    )
    for receipt in receipts:
        payload = receipt.upper_model_configuration
        assert payload["model"] == "gpt-5.6-sol"
        assert payload["reasoning_effort"] == "high"
        assert not ({"prompt", "harness", "operation_id", "task_binding"} & set(payload))
        assert receipt.fresh_root_proof_sha256


def test_h0_invalid_evaluator_result_is_terminal_and_other_baselines_continue(
    tmp_path: Path,
) -> None:
    manifest = _manifest()

    def solve(request):
        return _execution(request, f"baseline-{request.target.position}")

    def evaluate(request):
        if request.operation_id.endswith("h0-A"):
            return object()
        return OfficialEvaluationResult(
            score=0.0,
            valid=True,
            public_feedback="valid",
            evaluator_receipt_sha256=_sha(f"eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    receipts = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    ).run_h0_baselines()

    assert [receipt.status for receipt in receipts] == ["invalid", "completed", "completed"]


def test_h0_replay_rejects_rehashed_audit_ledger_tampering(tmp_path: Path) -> None:
    manifest = _manifest()

    def solve(request):
        return _execution(request, f"baseline-{request.target.position}")

    def evaluate(request):
        return OfficialEvaluationResult(
            score=0.0,
            valid=True,
            public_feedback="valid",
            evaluator_receipt_sha256=_sha(f"eval-{request.operation_id}"),
            private_evidence_sha256=_sha(f"private-{request.operation_id}"),
        )

    runner = CrossMatrixRunner(
        manifest=manifest,
        root=tmp_path / "cross",
        **_cell_factories(solve, evaluate),
    )
    runner.run_h0_baselines()
    receipt_path = tmp_path / "cross" / "h0_baselines" / "A" / "receipt.json"
    _tamper_enveloped_field(receipt_path, "audit_ledger_sha256", _sha("tampered-audit"))

    with pytest.raises(ValueError, match="execution evidence"):
        runner.run_h0_baselines()


def test_h0_baseline_refuses_a_preexisting_unowned_root(tmp_path: Path) -> None:
    root = tmp_path / "cross"
    occupied = root / "h0_baselines" / "A"
    occupied.mkdir(parents=True)
    (occupied / "unrelated.txt").write_text("not fresh", encoding="utf-8")
    runner = CrossMatrixRunner(
        manifest=_manifest(),
        root=root,
        **_cell_factories(
            lambda request: pytest.fail("must not execute"),
            lambda request: pytest.fail("must not evaluate"),
        ),
    )

    with pytest.raises(ValueError, match="fresh root"):
        runner.run_h0_baselines()
