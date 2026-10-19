from __future__ import annotations

import hashlib
import json
import os
import stat
from types import SimpleNamespace
from pathlib import Path

import pytest

from optimization_lab.harness_builder.adapters.sweperf import (
    DATASET_COMMIT,
    DATASET_PARQUET_SHA256,
    EVALUATOR_COMMIT,
    FROZEN_TASKS,
    PATCH_APPLY_MODE,
    PERFORMANCE_REPETITIONS,
    SWEPERF_EVALUATOR_ID,
)
from optimization_lab.harness_builder.adapters.sweperf_docker import (
    SecurityLimits,
)
from optimization_lab.harness_builder.sweperf_wrapper import (
    IMAGE_RESOURCE_LIMITS_SHA256_LABEL,
    IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL,
    IMAGE_TASK_MANIFEST_SHA256_LABEL,
    IMAGE_UPSTREAM_REF_SHA256_LABEL,
    WrapperSourceLock,
    WrapperTaskManifest,
    prepare_wrapper_build_contexts,
    result_channel_capability_verdict,
)
from optimization_lab.harness_builder.sweperf_wrapper.supervisor import (
    QuiescenceViolation,
    UnattestableCandidateOutcome,
    _run_worker_command,
    atomic_private_result,
    canonical_sha256,
    correctness_receipt,
    enforce_worker_quiescence,
    exact_apply_argv,
)


UPSTREAM_IMAGE = "registry.invalid/sweperf-base@sha256:" + "a" * 64
WRAPPER_IMAGE = "registry.invalid/hb-sweperf@sha256:" + "b" * 64


def _task_payload(instance_id: str) -> dict[str, object]:
    task = FROZEN_TASKS[instance_id]
    return {
        "schema_version": 1,
        "instance_id": task.instance_id,
        "repository": task.repository,
        "base_commit": task.base_commit,
        "task_sha256": task.task_sha256,
        "evaluator": SWEPERF_EVALUATOR_ID,
        "evaluator_commit": EVALUATOR_COMMIT,
        "dataset_commit": DATASET_COMMIT,
        "dataset_parquet_sha256": DATASET_PARQUET_SHA256,
        "patch_apply_mode": PATCH_APPLY_MODE,
        "upstream_image_ref": UPSTREAM_IMAGE,
        "repository_path": "/testbed",
        "allowed_patch_paths": ["pkg/core.py"],
        "correctness": {
            "argv": [
                "/opt/miniconda3/bin/conda",
                "run",
                "--no-capture-output",
                "-n",
                "testbed",
                "python",
                "-m",
                "pytest",
                "--json-report",
                "--json-report-file={report_path}",
                "pkg/tests/test_core.py::test_calculate",
            ],
            "timeout_seconds": 240,
            "expected_test_ids": ["pkg/tests/test_core.py::test_calculate"],
        },
        "performance": {
            "argv": [
                "/opt/miniconda3/bin/conda",
                "run",
                "--no-capture-output",
                "-n",
                "testbed",
                "python",
                "-m",
                "pytest",
                "--json-report",
                "--json-report-file={report_path}",
                "pkg/tests/test_core.py::test_calculate",
            ],
            "timeout_seconds": 120,
            "expected_test_ids": ["pkg/tests/test_core.py::test_calculate"],
            "warmup_repetitions": 3,
            "measurement_repetitions": PERFORMANCE_REPETITIONS,
            "score_formula": "geomean-median-speedup-v1",
        },
        "worker_uid": 65534,
        "resource_limits": {
            "cpus": 10,
            "memory_bytes": 32 * 1024**3,
            "pids": 512,
        },
    }


def _source_lock_payload() -> dict[str, object]:
    return {
        "schema_version": 1,
        "evaluator_commit": EVALUATOR_COMMIT,
        "dataset_commit": DATASET_COMMIT,
        "dataset_parquet_sha256": DATASET_PARQUET_SHA256,
        "tasks": [_task_payload(instance_id) for instance_id in FROZEN_TASKS],
    }


def test_resource_envelope_is_frozen_to_ten_cpu_32_gib_and_512_pids() -> None:
    limits = SecurityLimits()
    assert limits.cpus == 10
    assert limits.memory_bytes == 32 * 1024**3
    assert limits.pids == 512
    with pytest.raises(ValueError, match="resource envelope"):
        SecurityLimits(cpus=8)

    manifest = WrapperTaskManifest.from_dict(_task_payload(next(iter(FROZEN_TASKS))))
    assert manifest.resource_limits.to_dict() == {
        "cpus": 10,
        "memory_bytes": 32 * 1024**3,
        "pids": 512,
    }


@pytest.mark.parametrize(
    ("mutate", "message"),
    [
        (
            lambda payload: payload.__setitem__(
                "upstream_image_ref", "registry.invalid/base:latest"
            ),
            "digest",
        ),
        (
            lambda payload: payload["correctness"].__setitem__(
                "argv", ["/bin/bash", "-c", "pytest"]
            ),
            "shell",
        ),
        (
            lambda payload: payload["performance"].__setitem__(
                "argv", ["/usr/bin/curl", "https://example.invalid"]
            ),
            "network",
        ),
        (
            lambda payload: payload["resource_limits"].__setitem__("cpus", 8),
            "resource",
        ),
        (
            lambda payload: payload["performance"].__setitem__(
                "measurement_repetitions", 19
            ),
            "repetition",
        ),
    ],
)
def test_task_manifest_rejects_mutable_or_unsafe_runtime_contracts(
    mutate, message: str
) -> None:
    payload = _task_payload(next(iter(FROZEN_TASKS)))
    mutate(payload)
    with pytest.raises(ValueError, match=message):
        WrapperTaskManifest.from_dict(payload)


def test_prepare_contexts_is_offline_content_addressed_and_label_bound(
    tmp_path: Path,
) -> None:
    source_lock = WrapperSourceLock.from_dict(_source_lock_payload())
    prepared = prepare_wrapper_build_contexts(
        source_lock=source_lock,
        output_root=tmp_path / "contexts",
    )

    assert tuple(item.instance_id for item in prepared) == tuple(FROZEN_TASKS)
    first = prepared[0]
    dockerfile = (first.context_dir / "Dockerfile").read_text(encoding="utf-8")
    assert f"FROM {UPSTREAM_IMAGE}\n" in dockerfile
    assert "--network" not in dockerfile
    assert "curl" not in dockerfile
    assert "wget" not in dockerfile
    assert "apt-get" not in dockerfile
    assert "pip install" not in dockerfile
    assert "patch --" not in dockerfile
    assert "\n+" not in dockerfile
    assert "USER 0:0" in dockerfile
    assert 'ENTRYPOINT ["/opt/hb-sweperf/bin/evaluate-stage"]' in dockerfile

    manifest_raw = (first.context_dir / "task-manifest.json").read_bytes()
    assert hashlib.sha256(manifest_raw).hexdigest() == first.task_manifest_sha256
    assert first.labels[IMAGE_TASK_MANIFEST_SHA256_LABEL] == (
        first.task_manifest_sha256
    )
    assert first.labels[IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL] == (
        first.supervisor_bundle_sha256
    )
    assert first.labels[IMAGE_UPSTREAM_REF_SHA256_LABEL] == hashlib.sha256(
        UPSTREAM_IMAGE.encode("ascii")
    ).hexdigest()
    assert first.labels[IMAGE_RESOURCE_LIMITS_SHA256_LABEL] == hashlib.sha256(
        b'{"cpus":10,"memory_bytes":34359738368,"pids":512}'
    ).hexdigest()

    context_receipt = json.loads(
        (first.context_dir / "build-context.json").read_text(encoding="utf-8")
    )
    assert context_receipt["network_mode"] == "none"
    assert context_receipt["pull_policy"] == "never"
    assert context_receipt["upstream_image_ref"] == UPSTREAM_IMAGE
    assert set(context_receipt["file_sha256"]) == {
        "Dockerfile",
        "evaluate-stage",
        "supervisor.py",
        "trusted_result.py",
        "task-manifest.json",
        "task-manifest.sha256",
    }

    entrypoint = first.context_dir / "evaluate-stage"
    assert stat.S_IMODE(entrypoint.stat().st_mode) == 0o555
    assert entrypoint.read_text(encoding="utf-8").startswith("#!/usr/bin/python3\n")


def test_source_lock_requires_all_and_only_the_frozen_eight_tasks() -> None:
    payload = _source_lock_payload()
    payload["tasks"] = payload["tasks"][:-1]
    with pytest.raises(ValueError, match="exact frozen SWE-Perf task set"):
        WrapperSourceLock.from_dict(payload)


def test_receipt_binds_manifest_request_patch_state_and_evidence() -> None:
    request_binding = {
        "attempt_id": "attempt-1",
        "instance_id": next(iter(FROZEN_TASKS)),
        "patch_sha256": "1" * 64,
        "task_sha256": "2" * 64,
    }
    receipt = correctness_receipt(
        task_manifest_sha256="3" * 64,
        request_binding=request_binding,
        correctness_nonce="4" * 64,
        patch_sha256="1" * 64,
        candidate_state_sha256="5" * 64,
        correctness_evidence_sha256="6" * 64,
    )
    assert len(receipt) == 64
    assert receipt == correctness_receipt(
        task_manifest_sha256="3" * 64,
        request_binding=request_binding,
        correctness_nonce="4" * 64,
        patch_sha256="1" * 64,
        candidate_state_sha256="5" * 64,
        correctness_evidence_sha256="6" * 64,
    )
    assert receipt != correctness_receipt(
        task_manifest_sha256="3" * 64,
        request_binding=request_binding,
        correctness_nonce="4" * 64,
        patch_sha256="1" * 64,
        candidate_state_sha256="5" * 64,
        correctness_evidence_sha256="7" * 64,
    )


def test_quiescence_guard_kills_residual_workers_and_fails_closed() -> None:
    killed: list[int] = []
    rounds = iter(((101, 102), (102,), ()))

    with pytest.raises(QuiescenceViolation, match="not quiescent"):
        enforce_worker_quiescence(
            worker_pids=lambda: next(rounds),
            kill_pid=killed.append,
            wait_once=lambda: None,
            max_rounds=3,
        )

    assert killed == [101, 102, 102]


def test_exact_apply_never_uses_patch_or_fuzz() -> None:
    check = exact_apply_argv(
        git_binary="/usr/bin/git",
        patch_path="/run/hb-private/candidate.patch",
        check=True,
    )
    apply = exact_apply_argv(
        git_binary="/usr/bin/git",
        patch_path="/run/hb-private/candidate.patch",
        check=False,
    )
    assert check == (
        "/usr/bin/git",
        "apply",
        "--check",
        "--whitespace=error-all",
        "/run/hb-private/candidate.patch",
    )
    assert apply == (
        "/usr/bin/git",
        "apply",
        "--whitespace=error-all",
        "/run/hb-private/candidate.patch",
    )
    assert "fuzz" not in " ".join(check + apply)
    assert all(item != "patch" for item in check + apply)


def test_private_result_is_atomic_owner_only_and_stdout_is_not_an_input(
    tmp_path: Path,
) -> None:
    result = {
        "status": "failed",
        "failure_kind": "tests_failed",
        "trusted": True,
    }
    destination = tmp_path / "private" / "result.json"
    digest = atomic_private_result(destination, result)

    assert stat.S_IMODE(destination.stat().st_mode) == 0o600
    assert destination.read_bytes() == (
        json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")
    assert digest == canonical_sha256(result)
    assert "stdout" not in result
    assert not list(destination.parent.glob("*.tmp"))


def test_worker_authored_pytest_json_cannot_be_promoted_to_trusted_evidence(
    tmp_path: Path, monkeypatch
) -> None:
    """A candidate shares the pytest process and can author a perfect report.

    File ownership after the command is irrelevant: uid 65534 controls the
    report bytes while the command runs.  The supervisor must reject this
    topology before it launches the worker, not parse the forged payload.
    """

    repository = tmp_path / "repository"
    repository.mkdir()
    report_path = tmp_path / "reports" / "correctness.json"
    launched = False

    def forge_passing_report(*args, **kwargs):
        nonlocal launched
        launched = True
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            json.dumps(
                {
                    "tests": [
                        {
                            "nodeid": "tests/test_candidate.py::test_behavior",
                            "outcome": "passed",
                            "call": {"duration": 0.000001},
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(
        "optimization_lab.harness_builder.sweperf_wrapper.supervisor.subprocess.run",
        forge_passing_report,
    )
    monkeypatch.setattr(
        "optimization_lab.harness_builder.sweperf_wrapper.supervisor.enforce_worker_quiescence",
        lambda **kwargs: None,
    )
    monkeypatch.setattr(
        "optimization_lab.harness_builder.sweperf_wrapper.supervisor.CACHE_ROOT",
        tmp_path / "cache",
    )
    command = {
        "argv": [
            "/opt/miniconda3/bin/python",
            "-m",
            "pytest",
            "--json-report",
            "--json-report-file={report_path}",
            "tests/test_candidate.py::test_behavior",
        ],
        "timeout_seconds": 30,
        "expected_test_ids": ["tests/test_candidate.py::test_behavior"],
    }

    with pytest.raises(UnattestableCandidateOutcome, match="same trust domain"):
        _run_worker_command(
            command,
            repository=repository,
            report_path=report_path,
        )

    assert launched is False
    assert not report_path.exists()


def test_result_channel_capability_verdict_is_content_addressed_and_blocked() -> None:
    payload = result_channel_capability_verdict().to_dict()
    content_id = payload.pop("content_id")

    assert payload["status"] == "blocked"
    assert payload["reason_code"] == "in_process_candidate_outcome_unattestable"
    assert payload["frozen_topology"][
        "candidate_and_pytest_reporter_share_process"
    ] is True
    assert payload["semantics_preserving_channel_implemented"] is False
    assert payload["signals_not_derivable_by_trusted_root"] == [
        "per_test_outcome",
        "per_test_call_duration",
    ]
    assert content_id == hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()
