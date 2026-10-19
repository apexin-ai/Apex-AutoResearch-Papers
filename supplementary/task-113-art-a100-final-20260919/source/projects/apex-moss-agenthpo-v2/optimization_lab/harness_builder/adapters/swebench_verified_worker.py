from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import types
from importlib import resources
from pathlib import Path, PurePosixPath
from typing import Any, Sequence

from .sweperf import validate_unified_diff


SWEBENCH_VERIFIED_EVALUATOR_ID = "swebench-verified-standard-harness-v1"
SWEBENCH_SOURCE_COMMIT = "f7bbbb2ccdf479001d6467c9e34af59e44a840f9"
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:+-]{0,191}\Z")
_REQUEST_FIELDS = {
    "schema_version",
    "attempt_id",
    "instance_id",
    "candidate_sha256",
    "dataset_sha256",
    "task_sha256",
    "locked_image_ref",
    "mutable_image_ref",
    "instance",
    "timeout_seconds",
}
_INSTANCE_FIELDS = {
    "repo",
    "instance_id",
    "base_commit",
    "patch",
    "test_patch",
    "problem_statement",
    "hints_text",
    "created_at",
    "version",
    "FAIL_TO_PASS",
    "PASS_TO_PASS",
    "environment_setup_commit",
    "difficulty",
}
_RESULT_FIELDS = {
    "schema_version",
    "evaluator_id",
    "swebench_source_commit",
    "attempt_id",
    "instance_id",
    "candidate_sha256",
    "dataset_sha256",
    "task_sha256",
    "image_manifest_sha256",
    "status",
    "valid_scored",
    "resolved",
    "fail_to_pass_passed",
    "fail_to_pass_total",
    "pass_to_pass_passed",
    "pass_to_pass_total",
    "score",
    "evaluator_seconds",
    "error_type",
    "error_summary",
    "trust_grade",
}


def _install_minimal_harness_imports() -> None:
    """Load only the official harness modules used by the evaluator.

    The pinned upstream ``swebench.harness.__init__`` eagerly imports dataset,
    inference, Modal, and reporting stacks that are irrelevant to one frozen
    evaluation.  A namespace package plus an exact small projection of the
    three ``utils`` helpers used by ``test_spec`` keeps the production worker
    bounded without changing its test-script or grading implementation.
    """

    swebench_root = next(
        (
            Path(entry).resolve() / "swebench"
            for entry in sys.path
            if (Path(entry).resolve() / "swebench" / "harness").is_dir()
        ),
        None,
    )
    if swebench_root is None:
        raise RuntimeError("pinned SWE-bench source package is missing")
    swebench = types.ModuleType("swebench")
    swebench.__path__ = [str(swebench_root)]  # type: ignore[attr-defined]
    swebench.__package__ = "swebench"
    swebench.__file__ = str(swebench_root / "__init__.py")
    sys.modules["swebench"] = swebench
    import swebench.resources as swebench_resources
    from unidiff import PatchSet

    harness_root = swebench_root / "harness"
    if not harness_root.is_dir():
        raise RuntimeError("pinned SWE-bench harness package is missing")
    package = types.ModuleType("swebench.harness")
    package.__path__ = [str(harness_root)]  # type: ignore[attr-defined]
    package.__package__ = "swebench.harness"
    sys.modules["swebench.harness"] = package
    setattr(swebench, "harness", package)

    utilities = types.ModuleType("swebench.harness.utils")

    def get_modified_files(patch: str) -> list[str]:
        files = [
            item.source_file for item in PatchSet(patch) if item.source_file != "/dev/null"
        ]
        return [value[2:] for value in files if value.startswith("a/")]

    def get_new_files(patch: str) -> list[str]:
        files: list[str] = []
        for item in PatchSet(patch):
            if item.source_file == "/dev/null":
                target = item.target_file
                files.append(target[2:] if target.startswith("b/") else target)
        return files

    def ansi_escape(text: str) -> str:
        return re.compile(r"\x1B(?:[@-Z\\-_]|\\[[0-?]*[ -/]*[@-~])").sub("", text)

    def load_cached_environment_yml(instance_id: str) -> str | None:
        try:
            repo, number = instance_id.rsplit("-", 1)
        except ValueError:
            return None
        try:
            return (
                resources.files(swebench_resources)
                .joinpath(f"swebench-og/{repo}/{number}/environment.yml")
                .read_text()
            )
        except FileNotFoundError:
            return None

    utilities.get_modified_files = get_modified_files  # type: ignore[attr-defined]
    utilities.get_new_files = get_new_files  # type: ignore[attr-defined]
    utilities.ansi_escape = ansi_escape  # type: ignore[attr-defined]
    utilities.load_cached_environment_yml = load_cached_environment_yml  # type: ignore[attr-defined]
    sys.modules["swebench.harness.utils"] = utilities


def _canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_request(path: Path, candidate_path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or set(payload) != _REQUEST_FIELDS:
        raise ValueError("SWE-bench worker request fields differ")
    instance = payload["instance"]
    if not isinstance(instance, dict) or set(instance) != _INSTANCE_FIELDS:
        raise ValueError("SWE-bench instance fields differ")
    if (
        payload["schema_version"] != 1
        or not isinstance(payload["attempt_id"], str)
        or _SAFE_ID.fullmatch(payload["attempt_id"]) is None
        or payload["instance_id"] != instance["instance_id"]
        or _SAFE_ID.fullmatch(payload["instance_id"]) is None
        or _SHA256.fullmatch(payload["candidate_sha256"]) is None
        or payload["candidate_sha256"] != _sha(candidate_path)
        or _SHA256.fullmatch(payload["dataset_sha256"]) is None
        or _SHA256.fullmatch(payload["task_sha256"]) is None
        or payload["task_sha256"]
        != hashlib.sha256(_canonical_bytes(instance)).hexdigest()
        or not isinstance(payload["timeout_seconds"], int)
        or not 60 <= payload["timeout_seconds"] <= 3600
    ):
        raise ValueError("SWE-bench worker request binding differs")
    locked = payload["locked_image_ref"]
    mutable = payload["mutable_image_ref"]
    if (
        not isinstance(locked, str)
        or not re.fullmatch(r"[^\s@]+@sha256:[0-9a-f]{64}", locked)
        or not isinstance(mutable, str)
        or not re.fullmatch(r"[^\s@]+:[A-Za-z0-9._-]+", mutable)
    ):
        raise ValueError("SWE-bench image binding is invalid")
    validate_unified_diff(candidate_path)
    return payload


def _image_digest(reference: str) -> str:
    return reference.rsplit("@sha256:", 1)[1]


def _load_locked_local_image(
    client: Any,
    locked_reference: str,
    *,
    image_not_found_error: type[BaseException],
) -> Any:
    """Resolve only the already-materialized immutable image.

    Formal evaluation is offline. A missing digest is an environment failure,
    never authority to use a mutable tag or pull from a registry.
    """

    try:
        image = client.images.get(locked_reference)
    except image_not_found_error as exc:
        expected_digest = _image_digest(locked_reference)
        try:
            local_images = client.images.list(all=True)
        except (AttributeError, image_not_found_error) as list_exc:
            raise RuntimeError(
                "locked SWE-bench image is not locally materialized"
            ) from list_exc
        matches = [
            candidate
            for candidate in local_images
            if any(
                value.endswith("@sha256:" + expected_digest)
                for value in candidate.attrs.get("RepoDigests", [])
            )
        ]
        if not matches:
            raise RuntimeError(
                "locked SWE-bench image is not locally materialized"
            ) from exc
        if len(matches) != 1:
            raise RuntimeError(
                "locked SWE-bench image is not uniquely materialized"
            ) from exc
        image = matches[0]
    expected_digest = _image_digest(locked_reference)
    repo_digests = image.attrs.get("RepoDigests", [])
    if not any(value.endswith("@sha256:" + expected_digest) for value in repo_digests):
        raise RuntimeError("local SWE-bench image digest differs")
    return image


def _container_network_options() -> dict[str, Any]:
    """Keep the evaluator offline while preserving its loopback dependency."""

    return {
        "network_mode": "none",
        "extra_hosts": {"localhost": "127.0.0.1"},
    }


def _require_loopback_preflight(exit_code: int) -> None:
    if exit_code != 0:
        raise RuntimeError("isolated SWE-bench container loopback is unavailable")


def _result(
    request: dict[str, Any],
    *,
    status: str,
    valid_scored: bool,
    resolved: bool,
    f2p_passed: int,
    f2p_total: int,
    p2p_passed: int,
    p2p_total: int,
    score: float | None,
    evaluator_seconds: float,
    error_type: str = "",
    error_summary: str = "",
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "evaluator_id": SWEBENCH_VERIFIED_EVALUATOR_ID,
        "swebench_source_commit": SWEBENCH_SOURCE_COMMIT,
        "attempt_id": request["attempt_id"],
        "instance_id": request["instance_id"],
        "candidate_sha256": request["candidate_sha256"],
        "dataset_sha256": request["dataset_sha256"],
        "task_sha256": request["task_sha256"],
        "image_manifest_sha256": _image_digest(request["locked_image_ref"]),
        "status": status,
        "valid_scored": valid_scored,
        "resolved": resolved,
        "fail_to_pass_passed": f2p_passed,
        "fail_to_pass_total": f2p_total,
        "pass_to_pass_passed": p2p_passed,
        "pass_to_pass_total": p2p_total,
        "score": score,
        "evaluator_seconds": evaluator_seconds,
        "error_type": error_type,
        "error_summary": error_summary,
        "trust_grade": "official_standard_candidate_visible_test_process",
    }


def _write_once(path: Path, payload: dict[str, Any]) -> None:
    content = _canonical_bytes(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != content:
            raise RuntimeError("refusing to overwrite another SWE-bench worker result")
        return
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, suffix=".swebench")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary).replace(path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def _replay_worker_result(path: Path, request: dict[str, Any]) -> int | None:
    if not path.is_file():
        return None
    raw = path.read_bytes()
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("existing SWE-bench worker result is invalid JSON") from exc
    if (
        not isinstance(payload, dict)
        or set(payload) != _RESULT_FIELDS
        or _canonical_bytes(payload) != raw
        or payload["schema_version"] != 1
        or payload["evaluator_id"] != SWEBENCH_VERIFIED_EVALUATOR_ID
        or payload["swebench_source_commit"] != SWEBENCH_SOURCE_COMMIT
        or payload["attempt_id"] != request["attempt_id"]
        or payload["instance_id"] != request["instance_id"]
        or payload["candidate_sha256"] != request["candidate_sha256"]
        or payload["dataset_sha256"] != request["dataset_sha256"]
        or payload["task_sha256"] != request["task_sha256"]
        or payload["image_manifest_sha256"]
        != _image_digest(request["locked_image_ref"])
        or payload["trust_grade"]
        != "official_standard_candidate_visible_test_process"
    ):
        raise RuntimeError("existing SWE-bench worker result binding differs")
    status = payload["status"]
    if status == "valid":
        return 0
    if status == "contract_rejected":
        return 2
    if status == "environment_invalid":
        return 3
    raise RuntimeError("existing SWE-bench worker result status differs")


def run_worker(
    *, request_path: Path, candidate_path: Path, result_path: Path, work_root: Path
) -> int:
    request = _load_request(request_path, candidate_path)
    replay_exit = _replay_worker_result(result_path, request)
    if replay_exit is not None:
        return replay_exit
    started = time.monotonic()
    container = None
    test_log = work_root / request["attempt_id"] / "test-output.txt"
    test_log.parent.mkdir(parents=True, exist_ok=True)
    try:
        import docker

        _install_minimal_harness_imports()
        from swebench.harness.constants import (
            DOCKER_PATCH,
            DOCKER_USER,
            DOCKER_WORKDIR,
            END_TEST_OUTPUT,
            KEY_INSTANCE_ID,
            KEY_MODEL,
            KEY_PREDICTION,
            START_TEST_OUTPUT,
        )
        from swebench.harness.docker_utils import (
            cleanup_container,
            copy_to_container,
            exec_run_with_timeout,
        )
        from swebench.harness.grading import get_eval_report
        from swebench.harness.test_spec.test_spec import make_test_spec

        client = docker.from_env()
        image = _load_locked_local_image(
            client,
            request["locked_image_ref"],
            image_not_found_error=docker.errors.ImageNotFound,
        )
        mutable_repository, mutable_tag = request["mutable_image_ref"].rsplit(":", 1)
        image.tag(mutable_repository, mutable_tag)

        test_spec = make_test_spec(
            request["instance"],
            namespace="swebench",
            instance_image_tag=mutable_tag,
            env_image_tag="latest",
        )
        container_name = (
            "hb3-" + hashlib.sha256(request["attempt_id"].encode()).hexdigest()[:24]
        )
        container = client.containers.create(
            image=image.id,
            name=container_name,
            user=DOCKER_USER,
            detach=True,
            command="tail -f /dev/null",
            platform="linux/amd64",
            mem_limit="32g",
            pids_limit=512,
            nano_cpus=10_000_000_000,
            **_container_network_options(),
        )
        container.start()
        loopback = container.exec_run(
            [
                "/opt/miniconda3/envs/testbed/bin/python",
                "-c",
                (
                    "import socket; "
                    "sock = socket.socket(); "
                    "sock.bind(('localhost', 0)); "
                    "sock.close()"
                ),
            ],
            user=DOCKER_USER,
        )
        _require_loopback_preflight(loopback.exit_code)
        copy_to_container(container, candidate_path, PurePosixPath(DOCKER_PATCH))
        checked = container.exec_run(
            f"git apply --check {DOCKER_PATCH}",
            workdir=DOCKER_WORKDIR,
            user=DOCKER_USER,
        )
        if checked.exit_code != 0:
            result = _result(
                request,
                status="contract_rejected",
                valid_scored=False,
                resolved=False,
                f2p_passed=0,
                f2p_total=0,
                p2p_passed=0,
                p2p_total=0,
                score=None,
                evaluator_seconds=min(time.monotonic() - started, 3600.0),
                error_type="patch_apply_failed",
                error_summary="candidate patch did not apply exactly to the frozen base",
            )
            _write_once(result_path, result)
            return 2
        applied = container.exec_run(
            f"git apply {DOCKER_PATCH}", workdir=DOCKER_WORKDIR, user=DOCKER_USER
        )
        if applied.exit_code != 0:
            raise RuntimeError("SWE-bench strict apply changed after apply-check")

        eval_script = test_log.parent / "eval.sh"
        eval_script.write_text(test_spec.eval_script, encoding="utf-8")
        copy_to_container(container, eval_script, PurePosixPath("/eval.sh"))
        output, timed_out, _runtime = exec_run_with_timeout(
            container, "/bin/bash /eval.sh", request["timeout_seconds"]
        )
        if timed_out:
            raise TimeoutError("SWE-bench evaluation timed out")
        test_log.write_text(output, encoding="utf-8")
        if START_TEST_OUTPUT not in output or END_TEST_OUTPUT not in output:
            raise RuntimeError("SWE-bench test output markers are absent")
        prediction = {
            KEY_INSTANCE_ID: request["instance_id"],
            KEY_MODEL: request["candidate_sha256"],
            KEY_PREDICTION: candidate_path.read_text(encoding="utf-8"),
        }
        report = get_eval_report(
            test_spec=test_spec,
            prediction=prediction,
            test_log_path=str(test_log),
            include_tests_status=True,
        )[request["instance_id"]]
        statuses = report.get("tests_status")
        if not isinstance(statuses, dict):
            raise RuntimeError("SWE-bench report lacks per-test status evidence")
        f2p = statuses["FAIL_TO_PASS"]
        p2p = statuses["PASS_TO_PASS"]
        f2p_passed = len(f2p["success"])
        f2p_total = f2p_passed + len(f2p["failure"])
        p2p_passed = len(p2p["success"])
        p2p_total = p2p_passed + len(p2p["failure"])
        total = f2p_total + p2p_total
        passed = f2p_passed + p2p_passed
        if total <= 0:
            raise RuntimeError("SWE-bench task has no scored tests")
        score = (passed + 1.0) / (total + 1.0)
        resolved = bool(report.get("resolved"))
        if resolved != (passed == total):
            raise RuntimeError("SWE-bench resolved flag and test counts disagree")
        result = _result(
            request,
            status="valid",
            valid_scored=True,
            resolved=resolved,
            f2p_passed=f2p_passed,
            f2p_total=f2p_total,
            p2p_passed=p2p_passed,
            p2p_total=p2p_total,
            score=score,
            evaluator_seconds=min(time.monotonic() - started, 3600.0),
        )
        _write_once(result_path, result)
        return 0
    except Exception as exc:
        result = _result(
            request,
            status="environment_invalid",
            valid_scored=False,
            resolved=False,
            f2p_passed=0,
            f2p_total=0,
            p2p_passed=0,
            p2p_total=0,
            score=None,
            evaluator_seconds=min(time.monotonic() - started, 3600.0),
            error_type=type(exc).__name__,
            error_summary=str(exc)[:500],
        )
        _write_once(result_path, result)
        return 3
    finally:
        if container is not None:
            try:
                container.remove(force=True)
            except Exception:
                pass


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--work-root", type=Path, required=True)
    args = parser.parse_args(argv)
    return run_worker(
        request_path=args.request.resolve(strict=True),
        candidate_path=args.candidate.resolve(strict=True),
        result_path=args.result.absolute(),
        work_root=args.work_root.resolve(),
    )


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "SWEBENCH_SOURCE_COMMIT",
    "SWEBENCH_VERIFIED_EVALUATOR_ID",
    "_load_locked_local_image",
    "run_worker",
]
