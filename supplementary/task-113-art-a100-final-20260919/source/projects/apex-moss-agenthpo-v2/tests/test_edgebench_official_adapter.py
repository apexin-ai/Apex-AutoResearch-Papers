from __future__ import annotations

import json
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

from optimization_lab.harness_builder.dual_runtime import EvaluationResult
from optimization_lab.harness_builder.official_solutions import (
    EdgeBenchBundleCodec,
    OfficialSolutionArchive,
)
from optimization_lab.harness_builder.adapters.edgebench_official import (
    EDGE_BENCH_DATASET_REVISION,
    EDGE_BENCH_SOURCE_COMMIT,
    EdgeBenchContract,
    EdgeBenchOfficialAdapter,
    ObservedEdgeBenchIdentity,
)
from optimization_lab.harness_builder.adapters import edgebench_official as edge_module

EDGE_IMAGE = "seededge/edgebench.judge.apple_incremental_game:16968d8ec7f2"
EDGE_DIGEST = "sha256:ca50e0754abb5dd1efd8387714206b8958fa7a4902ffadc03abad63139e26051"
EDGE_TASK_SHA = "19021ddcbcaf966d7d43300b439862290a5c6c283aa6e6641f96efa07b34a25c"


def _artifact():
    return EdgeBenchBundleCodec().parse(
        json.dumps(
            {
                "schema_version": 1,
                "files": [
                    {
                        "path": "solution.py",
                        "type": "file",
                        "content": "print(0)\n",
                    }
                ],
            }
        )
    )


def _contract(tmp_path: Path) -> EdgeBenchContract:
    return EdgeBenchContract(
        source_root=tmp_path / "edge-source",
        dataset_root=tmp_path / "edge-data",
        sforge_executable=tmp_path / "edge-venv" / "bin" / "sforge",
        source_commit=EDGE_BENCH_SOURCE_COMMIT,
        dataset_revision=EDGE_BENCH_DATASET_REVISION,
        task_id="apple_incremental_game",
        docker_image_reference=EDGE_IMAGE,
        docker_image_digest=EDGE_DIGEST,
        timeout_seconds=600,
        score_direction="maximize",
        evaluator_command=("sforge", "eval"),
    )


def _real_edge_layout(contract: EdgeBenchContract) -> None:
    contract.source_root.mkdir(parents=True)
    executable = contract.sforge_executable
    executable.parent.mkdir(parents=True)
    executable.write_text("#!/bin/sh\n", encoding="utf-8")
    download = contract.dataset_root / ".cache" / "huggingface" / "download"
    download.mkdir(parents=True)
    (download / f"{contract.task_id}.json.metadata").write_text(
        EDGE_BENCH_DATASET_REVISION + "\n", encoding="utf-8"
    )
    (contract.dataset_root / f"{contract.task_id}.json").write_text(
        json.dumps({"task_id": contract.task_id, "judge": {"image_tag": "16968d8ec7f2", "eval_timeout": 600, "score_direction": "maximize"}}),
        encoding="utf-8",
    )


def _observed(contract: EdgeBenchContract) -> ObservedEdgeBenchIdentity:
    return ObservedEdgeBenchIdentity(
        source_commit=contract.source_commit,
        dataset_revision=contract.dataset_revision,
        task_id=contract.task_id,
        docker_image_digest=contract.docker_image_digest,
        timeout_seconds=contract.timeout_seconds,
        score_direction=contract.score_direction,
        evaluator_command=contract.evaluator_command,
        task_json_sha256=EDGE_TASK_SHA,
        sforge_executable=contract.sforge_executable.as_posix(),
        sforge_module_path=(contract.source_root / "sforge" / "__init__.py").resolve().as_posix(),
        direct_url_source=contract.source_root.as_uri(),
    )


def _report_path(
    argv: list[str], contract: EdgeBenchContract, kwargs: dict[str, object]
) -> Path:
    env = kwargs["env"]
    assert isinstance(env, dict)
    log_root = Path(env["SFORGE_LOG_DIR"])
    run_id = argv[argv.index("--run-id") + 1]
    return (
        log_root
        / "runs"
        / run_id
        / contract.task_id
        / "submissions"
        / "manual-1"
        / "report.json"
    )


def test_edge_passes_path_overrides_via_environment_for_sforge_path_types(
    tmp_path: Path,
) -> None:
    contract = _contract(tmp_path)

    def runner(argv: list[str], **kwargs: object) -> SimpleNamespace:
        assert "--log-dir" not in argv
        assert "--tasks-dir" not in argv
        env = kwargs["env"]
        assert isinstance(env, dict)
        assert env["SFORGE_LOG_DIR"] == str(tmp_path / "attempts" / "edge-path-env" / "logs")
        assert env["SFORGE_TASKS_DIR"] == str(contract.dataset_root)
        report_path = (
            Path(env["SFORGE_LOG_DIR"])
            / "runs"
            / "edge-path-env"
            / contract.task_id
            / "submissions"
            / "manual-1"
            / "report.json"
        )
        report_path.parent.mkdir(parents=True)
        report_path.write_text(
            json.dumps(
                {
                    "task_id": contract.task_id,
                    "submission_id": "edge-path-env",
                    "score": 1.0,
                    "valid": True,
                    "timed_out": False,
                }
            ),
            encoding="utf-8",
        )
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    result = EdgeBenchOfficialAdapter(
        contract=contract,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        attempt_root=tmp_path / "attempts",
        private_evidence_root=tmp_path / "private",
        runner=runner,
        identity_probe=lambda _: _observed(contract),
    ).evaluate(_artifact(), operation_id="edge-path-env")

    assert result.public.score == 1.0


def test_edge_uses_fresh_attempt_argv_and_authoritative_report(tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    calls: list[tuple[list[str], dict[str, object]]] = []

    def runner(argv: list[str], **kwargs: object) -> SimpleNamespace:
        calls.append((argv, kwargs))
        assert isinstance(argv, list)
        assert "--log-dir" not in argv
        assert "--tasks-dir" not in argv
        env = kwargs["env"]
        assert isinstance(env, dict)
        assert env["SFORGE_TASKS_DIR"] == str(contract.dataset_root)
        assert argv[argv.index("--task") + 1] == contract.task_id
        assert argv[argv.index("--timeout") + 1] == "600"
        assert Path(argv[argv.index("--archive") + 1]).is_file()
        report_path = _report_path(argv, contract, kwargs)
        report_path.parent.mkdir(parents=True)
        report_path.write_text(
            json.dumps(
                {
                    "task_id": contract.task_id,
                    "submission_id": "edge-op-1",
                    "score": 0.0,
                    "valid": True,
                    "timed_out": False,
                    "summary": "PRIVATE_CASE_NAME should stay private",
                    "pass_rate": 1.0,
                    "test_details": [{"name": "PRIVATE_CASE_NAME"}],
                }
            ),
            encoding="utf-8",
        )
        return SimpleNamespace(
            returncode=0,
            stdout='human log\n{"score": 999999}',
            stderr="PRIVATE_STDERR",
        )

    adapter = EdgeBenchOfficialAdapter(
        contract=contract,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        attempt_root=tmp_path / "attempts",
        private_evidence_root=tmp_path / "private",
        runner=runner,
        identity_probe=lambda _: _observed(contract),
    )

    result = adapter.evaluate(_artifact(), operation_id="edge-op-1")

    assert isinstance(result, EvaluationResult)
    assert result.public.score == 0.0
    feedback = json.loads(result.public.feedback)
    assert set(feedback) == {"status", "reason", "aggregate_score", "validity"}
    assert feedback["aggregate_score"] == 0.0
    assert feedback["validity"] is True
    assert "PRIVATE" not in result.public.feedback
    assert "pass_rate" not in result.public.feedback
    assert calls[0][1]["shell"] is False
    assert calls[0][1]["check"] is False
    assert calls[0][1]["timeout"] == 630
    evidence_path = Path(result.private["evidence_path"])
    assert evidence_path.is_file()
    evidence = evidence_path.read_text(encoding="utf-8")
    assert "PRIVATE_CASE_NAME" in evidence
    assert "PRIVATE_STDERR" in evidence
    assert (tmp_path / "attempts" / "edge-op-1" / "bundle" / "solution.py").is_file()

    with pytest.raises(ValueError, match="attempt already exists"):
        adapter.evaluate(_artifact(), operation_id="edge-op-1")


def test_edge_normalizes_completed_failed_report_without_score_to_zero(
    tmp_path: Path,
) -> None:
    contract = _contract(tmp_path)

    def runner(argv: list[str], **kwargs: object) -> SimpleNamespace:
        report_path = _report_path(argv, contract, kwargs)
        report_path.parent.mkdir(parents=True)
        report_path.write_text(
            json.dumps(
                {
                    "task_id": contract.task_id,
                    "submission_id": "edge-null-score",
                    "total_tests": 1,
                    "passed": 0,
                    "failed": 1,
                    "errors": 0,
                    "pass_rate": 0.0,
                    "score": None,
                    "score_0_100": None,
                    "valid": True,
                    "timed_out": False,
                }
            ),
            encoding="utf-8",
        )
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    result = EdgeBenchOfficialAdapter(
        contract=contract,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        attempt_root=tmp_path / "attempts",
        private_evidence_root=tmp_path / "private",
        runner=runner,
        identity_probe=lambda _: _observed(contract),
    ).evaluate(_artifact(), operation_id="edge-null-score")

    assert result.public.score == 0.0
    assert json.loads(result.public.feedback) == {
        "aggregate_score": 0.0,
        "reason": "official_evaluation_completed",
        "status": "COMPLETED",
        "validity": True,
    }


def test_edge_rejects_null_score_without_completed_failure_evidence(
    tmp_path: Path,
) -> None:
    contract = _contract(tmp_path)

    def runner(argv: list[str], **kwargs: object) -> SimpleNamespace:
        report_path = _report_path(argv, contract, kwargs)
        report_path.parent.mkdir(parents=True)
        report_path.write_text(
            json.dumps(
                {
                    "task_id": contract.task_id,
                    "submission_id": "edge-empty-null-score",
                    "total_tests": 0,
                    "passed": 0,
                    "failed": 0,
                    "errors": 0,
                    "pass_rate": 0.0,
                    "score": None,
                    "score_0_100": None,
                    "valid": True,
                    "timed_out": False,
                }
            ),
            encoding="utf-8",
        )
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    with pytest.raises(RuntimeError, match="official report score is invalid"):
        EdgeBenchOfficialAdapter(
            contract=contract,
            solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
            attempt_root=tmp_path / "attempts",
            private_evidence_root=tmp_path / "private",
            runner=runner,
            identity_probe=lambda _: _observed(contract),
        ).evaluate(_artifact(), operation_id="edge-empty-null-score")


def test_edge_report_json_not_stdout_is_score_authority(tmp_path: Path) -> None:
    contract = _contract(tmp_path)

    def runner(argv: list[str], **kwargs: object) -> SimpleNamespace:
        report_path = _report_path(argv, contract, kwargs)
        report_path.parent.mkdir(parents=True)
        report_path.write_text(
            json.dumps(
                {
                    "task_id": contract.task_id,
                    "submission_id": "edge-op-2",
                    "score": 17.0,
                    "valid": True,
                    "timed_out": False,
                    "summary": "done",
                }
            ),
            encoding="utf-8",
        )
        return SimpleNamespace(returncode=0, stdout='{"score": 999.0}', stderr="")

    result = EdgeBenchOfficialAdapter(
        contract=contract,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        attempt_root=tmp_path / "attempts",
        private_evidence_root=tmp_path / "private",
        runner=runner,
        identity_probe=lambda _: _observed(contract),
    ).evaluate(_artifact(), operation_id="edge-op-2")

    assert result.public.score == 17.0


def test_edge_identity_mismatch_fails_before_evaluator_call(tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    calls = 0

    def runner(*_: object, **__: object) -> SimpleNamespace:
        nonlocal calls
        calls += 1
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    wrong = _observed(contract)
    wrong = ObservedEdgeBenchIdentity(
        **{**wrong.__dict__, "dataset_revision": "0" * 40}
    )
    adapter = EdgeBenchOfficialAdapter(
        contract=contract,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        attempt_root=tmp_path / "attempts",
        private_evidence_root=tmp_path / "private",
        runner=runner,
        identity_probe=lambda _: wrong,
    )

    with pytest.raises(RuntimeError, match="identity differs"):
        adapter.evaluate(_artifact(), operation_id="edge-op-3")
    assert calls == 0


def test_edge_rejects_report_bound_to_another_task(tmp_path: Path) -> None:
    contract = _contract(tmp_path)

    def runner(argv: list[str], **kwargs: object) -> SimpleNamespace:
        report_path = _report_path(argv, contract, kwargs)
        report_path.parent.mkdir(parents=True)
        report_path.write_text(
            json.dumps(
                {
                    "task_id": "molecular_self_assembly",
                    "submission_id": "edge-op-4",
                    "score": 4.0,
                    "valid": True,
                    "timed_out": False,
                }
            ),
            encoding="utf-8",
        )
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    adapter = EdgeBenchOfficialAdapter(
        contract=contract,
        solution_archive=OfficialSolutionArchive(tmp_path / "solutions"),
        attempt_root=tmp_path / "attempts",
        private_evidence_root=tmp_path / "private",
        runner=runner,
        identity_probe=lambda _: _observed(contract),
    )

    with pytest.raises(RuntimeError, match="report binding differs"):
        adapter.evaluate(_artifact(), operation_id="edge-op-4")


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_commit", "0" * 40),
        ("dataset_revision", "0" * 40),
        ("task_id", "unknown"),
        ("timeout_seconds", 601),
        ("score_direction", "minimize"),
        ("evaluator_command", ("python", "fake_eval.py")),
        ("docker_image_digest", "not-a-digest"),
    ],
)
def test_edge_contract_fails_closed_on_unpinned_identity(
    tmp_path: Path, field: str, value: object
) -> None:
    values = _contract(tmp_path).__dict__.copy()
    values[field] = value
    with pytest.raises(ValueError):
        EdgeBenchContract(**values)


def test_edge_default_probe_reads_hf_metadata_and_real_task(monkeypatch, tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    _real_edge_layout(contract)
    monkeypatch.setattr(edge_module, "_sha256_file", lambda _: EDGE_TASK_SHA)
    package_json = json.dumps({"module": (contract.source_root / "sforge" / "__init__.py").as_posix(), "direct_url": contract.source_root.as_uri()})
    monkeypatch.setattr(edge_module, "_run_identity_command", lambda command, **_: EDGE_BENCH_SOURCE_COMMIT if command[:2] == ("git", "rev-parse") else "" if command[:2] == ("git", "status") else package_json if "import importlib.metadata" in " ".join(command) else EDGE_DIGEST)
    observed = edge_module._probe_identity(contract)
    assert observed.dataset_revision == EDGE_BENCH_DATASET_REVISION
    assert observed.task_json_sha256 == EDGE_TASK_SHA
    assert observed.sforge_executable == contract.sforge_executable.as_posix()


def test_edge_task_json_sha_mismatch_fails(monkeypatch, tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    _real_edge_layout(contract)
    monkeypatch.setattr(edge_module, "_sha256_file", lambda _: "0" * 64)
    package_json = json.dumps({"module": (contract.source_root / "sforge" / "__init__.py").as_posix(), "direct_url": contract.source_root.as_uri()})
    monkeypatch.setattr(edge_module, "_run_identity_command", lambda command, **_: EDGE_BENCH_SOURCE_COMMIT if command[:2] == ("git", "rev-parse") else "" if command[:2] == ("git", "status") else package_json)
    with pytest.raises(RuntimeError, match="task data digest"):
        edge_module._probe_identity(contract)


def test_edge_dirty_source_fails(monkeypatch, tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    _real_edge_layout(contract)
    monkeypatch.setattr(edge_module, "_sha256_file", lambda _: EDGE_TASK_SHA)
    monkeypatch.setattr(edge_module, "_run_identity_command", lambda command, **_: EDGE_BENCH_SOURCE_COMMIT if command[:2] == ("git", "rev-parse") else " M file.py")
    with pytest.raises(RuntimeError, match="source checkout is dirty"):
        edge_module._probe_identity(contract)


def test_edge_wrong_sforge_origin_fails(tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    contract.source_root.mkdir(parents=True)
    with pytest.raises(RuntimeError, match="sforge executable"):
        edge_module._probe_identity(contract)


def test_edge_image_tag_digest_binding_is_frozen(tmp_path: Path) -> None:
    values = _contract(tmp_path).__dict__.copy()
    values["docker_image_digest"] = "sha256:" + "f" * 64
    with pytest.raises(ValueError, match="Docker image identity differs"):
        EdgeBenchContract(**values)


def test_edge_subprocess_timeout_is_infrastructure_failure(tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    def runner(argv: list[str], **_: object):
        raise subprocess.TimeoutExpired(argv, 630)
    adapter = EdgeBenchOfficialAdapter(contract=contract, solution_archive=OfficialSolutionArchive(tmp_path / "solutions"), attempt_root=tmp_path / "attempts", private_evidence_root=tmp_path / "private", runner=runner, identity_probe=lambda _: _observed(contract))
    with pytest.raises(RuntimeError, match="infrastructure timeout"):
        adapter.evaluate(_artifact(), operation_id="edge-timeout")
