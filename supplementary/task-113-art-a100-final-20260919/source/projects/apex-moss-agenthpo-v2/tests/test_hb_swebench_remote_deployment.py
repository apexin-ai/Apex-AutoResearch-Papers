from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import pytest

from optimization_lab.harness_builder import swebench_remote_deployment as deployment
from optimization_lab.harness_builder.adapters.swebench_verified_worker import (
    SWEBENCH_SOURCE_COMMIT,
)
from scripts import prepare_hb_swebench_remote_deployment as deployment_cli


REMOTE_PROJECT = "/remote/runtime/Moss-clean"
REMOTE_PYTHON = "/remote/swebench/venv/bin/python"
REMOTE_SWEBENCH = "/remote/swebench/SWE-bench"


def _git(repo: Path, *arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout.strip()


def _project(tmp_path: Path) -> tuple[Path, str, bytes]:
    root = tmp_path / "Moss"
    worker = root / deployment.SWEBENCH_WORKER_RELATIVE_PATH
    worker.parent.mkdir(parents=True)
    worker_bytes = b"# frozen worker\nVALUE = 1\n"
    worker.write_bytes(worker_bytes)
    executable = root / "scripts" / "run.py"
    executable.parent.mkdir()
    executable.write_text("#!/usr/bin/env python3\n", encoding="utf-8")
    executable.chmod(0o755)
    (root / "CLAUDE.md").write_text("instructions\n", encoding="utf-8")
    (root / "AGENTS.md").symlink_to("CLAUDE.md")
    _git(root, "init")
    _git(root, "config", "user.name", "Fixture")
    _git(root, "config", "user.email", "fixture@example.invalid")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "fixture")
    return root, _git(root, "rev-parse", "HEAD"), worker_bytes


def _python_identity() -> dict[str, object]:
    return {
        "requested_path": REMOTE_PYTHON,
        "sys_executable": REMOTE_PYTHON,
        "real_executable": "/usr/bin/python3.10",
        "executable_sha256": "a" * 64,
        "implementation": "cpython",
        "python_version": "3.10.12",
        "version_info": [3, 10, 12, "final", 0],
        "cache_tag": "cpython-310",
        "prefix": "/remote/swebench/venv",
        "base_prefix": "/usr",
        "byteorder": "little",
    }


def _probe_response(
    request: dict[str, object], *, hostname: str = "worker-a100"
) -> dict[str, object]:
    worker_entry = next(
        item
        for item in request["tracked_entries"]
        if item["path"] == deployment.SWEBENCH_WORKER_RELATIVE_PATH
    )
    assert worker_entry["mode"] == "100644"
    return {
        "schema_version": 1,
        "kind": "swebench_remote_deployment_probe_result",
        "remote_hostname": hostname,
        "remote_project_root": REMOTE_PROJECT,
        "remote_swebench_source_root": REMOTE_SWEBENCH,
        "moss_tracked_manifest_sha256": request[
            "moss_tracked_manifest_sha256"
        ],
        "moss_tracked_file_count": len(request["tracked_entries"]),
        "worker_sha256": hashlib.sha256(b"# frozen worker\nVALUE = 1\n").hexdigest(),
        "swebench_source_commit": SWEBENCH_SOURCE_COMMIT,
        "swebench_source_clean": True,
        "remote_python": _python_identity(),
    }


def _arguments(root: Path, revision: str) -> dict[str, object]:
    return {
        "project_root": root,
        "expected_code_revision": revision,
        "host_alias": "a100jump",
        "remote_project_root": REMOTE_PROJECT,
        "remote_python": REMOTE_PYTHON,
        "remote_swebench_source_root": REMOTE_SWEBENCH,
    }


def test_prepare_and_verify_content_addressed_remote_deployment_receipt(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, revision, worker_bytes = _project(tmp_path)
    calls: list[dict[str, object]] = []

    def probe(**kwargs: object) -> dict[str, object]:
        request = kwargs["request"]
        assert isinstance(request, dict)
        calls.append(request)
        return _probe_response(request)

    monkeypatch.setattr(deployment, "_run_remote_probe", probe)
    receipt_path = deployment.prepare_swebench_remote_deployment_receipt(
        output_root=tmp_path / "receipts",
        **_arguments(root, revision),
    )
    raw = receipt_path.read_bytes()
    receipt = json.loads(raw)

    assert receipt_path.name == f"{hashlib.sha256(raw).hexdigest()}.json"
    assert receipt["moss_clean_revision"] == revision
    assert receipt["moss_tracked_file_count"] == 4
    assert receipt["worker_sha256"] == hashlib.sha256(worker_bytes).hexdigest()
    assert receipt["swebench_source_commit"] == SWEBENCH_SOURCE_COMMIT
    assert receipt["remote_python"] == _python_identity()
    assert receipt["model_calls_started"] == 0
    assert receipt["evaluator_transactions_started"] == 0
    assert len(calls) == 1
    assert calls[0]["moss_clean_revision"] == revision
    assert calls[0]["swebench_source_commit"] == SWEBENCH_SOURCE_COMMIT

    verified = deployment.verify_swebench_remote_deployment_receipt(
        receipt_path,
        **_arguments(root, revision),
    )
    assert verified == receipt
    assert len(calls) == 1


def test_verifier_reprobes_and_rejects_changed_remote_identity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, revision, _worker_bytes = _project(tmp_path)

    def first_probe(**kwargs: object) -> dict[str, object]:
        request = kwargs["request"]
        assert isinstance(request, dict)
        return _probe_response(request)

    monkeypatch.setattr(deployment, "_run_remote_probe", first_probe)
    receipt_path = deployment.prepare_swebench_remote_deployment_receipt(
        output_root=tmp_path / "receipts",
        **_arguments(root, revision),
    )

    def changed_probe(**kwargs: object) -> dict[str, object]:
        request = kwargs["request"]
        assert isinstance(request, dict)
        return _probe_response(request, hostname="different-host")

    monkeypatch.setattr(deployment, "_run_remote_probe", changed_probe)
    with pytest.raises(ValueError, match="live remote deployment identity differs"):
        deployment.verify_swebench_remote_deployment_receipt(
            receipt_path,
            reprobe=True,
            **_arguments(root, revision),
        )


def test_receipt_requires_content_addressed_name_and_clean_local_revision(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, revision, _worker_bytes = _project(tmp_path)

    def probe(**kwargs: object) -> dict[str, object]:
        request = kwargs["request"]
        assert isinstance(request, dict)
        return _probe_response(request)

    monkeypatch.setattr(deployment, "_run_remote_probe", probe)
    receipt_path = deployment.prepare_swebench_remote_deployment_receipt(
        output_root=tmp_path / "receipts",
        **_arguments(root, revision),
    )
    renamed = tmp_path / "renamed.json"
    renamed.write_bytes(receipt_path.read_bytes())
    with pytest.raises(ValueError, match="not content-addressed"):
        deployment.verify_swebench_remote_deployment_receipt(
            renamed,
            **_arguments(root, revision),
        )

    worker = root / deployment.SWEBENCH_WORKER_RELATIVE_PATH
    worker.write_text("changed\n", encoding="utf-8")
    with pytest.raises(ValueError, match="clean full Git revision"):
        deployment.verify_swebench_remote_deployment_receipt(
            receipt_path,
            **_arguments(root, revision),
        )


def test_probe_response_cannot_substitute_worker_or_python(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, revision, _worker_bytes = _project(tmp_path)

    def wrong_worker(**kwargs: object) -> dict[str, object]:
        request = kwargs["request"]
        assert isinstance(request, dict)
        response = _probe_response(request)
        response["worker_sha256"] = "b" * 64
        return response

    monkeypatch.setattr(deployment, "_run_remote_probe", wrong_worker)
    with pytest.raises(ValueError, match="deployment binding differs"):
        deployment.prepare_swebench_remote_deployment_receipt(
            output_root=tmp_path / "receipts-worker",
            **_arguments(root, revision),
        )

    def wrong_python(**kwargs: object) -> dict[str, object]:
        request = kwargs["request"]
        assert isinstance(request, dict)
        response = _probe_response(request)
        response["remote_python"]["sys_executable"] = "/other/python"
        return response

    monkeypatch.setattr(deployment, "_run_remote_probe", wrong_python)
    with pytest.raises(ValueError, match="remote Python identity differs"):
        deployment.prepare_swebench_remote_deployment_receipt(
            output_root=tmp_path / "receipts-python",
            **_arguments(root, revision),
        )


def test_prepare_cli_is_explicit_and_reports_zero_paid_operations(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    receipt = {
        "moss_clean_revision": "c" * 40,
        "worker_sha256": "d" * 64,
        "swebench_source_commit": SWEBENCH_SOURCE_COMMIT,
        "remote_python": _python_identity(),
    }
    receipt_path = tmp_path / "fixture.json"
    receipt_path.write_text(json.dumps(receipt), encoding="utf-8")

    def prepare(**_kwargs: object) -> Path:
        return receipt_path

    monkeypatch.setattr(
        deployment_cli,
        "prepare_swebench_remote_deployment_receipt",
        prepare,
    )
    base = [
        "prepare",
        "--expected-code-revision",
        "c" * 40,
        "--remote-project-root",
        REMOTE_PROJECT,
        "--remote-python",
        REMOTE_PYTHON,
        "--remote-swebench-source-root",
        REMOTE_SWEBENCH,
        "--output-root",
        str(tmp_path / "receipts"),
    ]
    with pytest.raises(SystemExit):
        deployment_cli.main(base)
    assert deployment_cli.main([*base, "--execute"]) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["model_calls_started"] == 0
    assert output["evaluator_transactions_started"] == 0
    assert output["moss_clean_revision"] == "c" * 40
