from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path

import pytest

from optimization_lab.harness_builder.adapters.swebench_verified import (
    SWEBENCH_VERIFIED_DATASET_SHA256,
    SWEBenchVerifiedRemoteAdapter,
    SWEBenchVerifiedResult,
    SWEBenchVerifiedTask,
)
from optimization_lab.harness_builder.adapters.swebench_verified_worker import (
    SWEBENCH_SOURCE_COMMIT,
    SWEBENCH_VERIFIED_EVALUATOR_ID,
    _container_network_options,
    _load_locked_local_image,
    _load_request,
    _require_loopback_preflight,
    _replay_worker_result,
)
from optimization_lab.harness_builder.adapters.sweperf import (
    PatchContractError,
    validate_unified_diff,
)
from optimization_lab.harness_builder.solutions import (
    SWEBenchVerifiedSolutionCodec,
)
from optimization_lab.harness_builder.swebench_verified_canary import (
    _canonicalize_official_gold_patch,
    _gold_canary_result_passed,
)


INSTANCE_ID = "django__django-14500"
PATCH = """diff --git a/django/core/example.py b/django/core/example.py
index 1111111..2222222 100644
--- a/django/core/example.py
+++ b/django/core/example.py
@@ -1 +1 @@
-old = 1
+new = 2
"""

OFFICIAL_GOLD_WITHOUT_INDEX = """diff --git a/django/core/example.py b/django/core/example.py
--- a/django/core/example.py
+++ b/django/core/example.py
@@ -1 +1 @@
-old = 1
+new = 2
diff --git a/django/core/second.py b/django/core/second.py
--- a/django/core/second.py
+++ b/django/core/second.py
@@ -2 +2 @@
-before = True
+after = True
"""

NEW_FILE_WITHOUT_INDEX = """diff --git a/django/core/new_module.py b/django/core/new_module.py
new file mode 100644
--- /dev/null
+++ b/django/core/new_module.py
@@ -0,0 +1 @@
+VALUE = 1
"""


def _canonical(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode()


def _instance() -> dict[str, object]:
    return {
        "repo": "django/django",
        "instance_id": INSTANCE_ID,
        "base_commit": "8c3bd0b708b488a1f6e8bd8cc6b96569904605be",
        "patch": "private gold patch",
        "test_patch": "private tests",
        "problem_statement": "Fix the migration behavior.",
        "hints_text": "",
        "created_at": "2022-01-01",
        "version": "4.0",
        "FAIL_TO_PASS": '["test_target"]',
        "PASS_TO_PASS": '["test_regression"]',
        "environment_setup_commit": "",
        "difficulty": "1 hour",
    }


def _task() -> SWEBenchVerifiedTask:
    instance = _instance()
    return SWEBenchVerifiedTask(
        instance=instance,
        task_sha256=hashlib.sha256(_canonical(instance)).hexdigest(),
        locked_image_ref=(
            "docker.io/swebench/example@sha256:" + "a" * 64
        ),
        mutable_image_ref="docker.io/swebench/example:latest",
    )


def test_swebench_verified_codec_and_worker_request_are_task_bound(
    tmp_path: Path,
) -> None:
    artifact = SWEBenchVerifiedSolutionCodec().parse(f"```diff\n{PATCH}```")
    candidate_path = tmp_path / "candidate.patch"
    candidate_path.write_text(artifact.text, encoding="utf-8")
    task = _task()
    request = {
        "schema_version": 1,
        "attempt_id": "swev-" + "b" * 64,
        "instance_id": INSTANCE_ID,
        "candidate_sha256": artifact.sha256,
        "dataset_sha256": SWEBENCH_VERIFIED_DATASET_SHA256,
        "task_sha256": task.task_sha256,
        "locked_image_ref": task.locked_image_ref,
        "mutable_image_ref": task.mutable_image_ref,
        "instance": dict(task.instance),
        "timeout_seconds": 1800,
    }
    request_path = tmp_path / "request.json"
    request_path.write_bytes(_canonical(request))

    assert _load_request(request_path, candidate_path) == request

    request["candidate_sha256"] = "c" * 64
    request_path.write_bytes(_canonical(request))
    with pytest.raises(ValueError, match="binding"):
        _load_request(request_path, candidate_path)


def test_official_gold_canary_adds_only_deterministic_index_metadata() -> None:
    with pytest.raises(PatchContractError, match="index line"):
        validate_unified_diff(OFFICIAL_GOLD_WITHOUT_INDEX)

    normalized = _canonicalize_official_gold_patch(OFFICIAL_GOLD_WITHOUT_INDEX)

    assert normalized == _canonicalize_official_gold_patch(
        OFFICIAL_GOLD_WITHOUT_INDEX
    )
    summary = validate_unified_diff(normalized)
    assert summary.file_paths == (
        "django/core/example.py",
        "django/core/second.py",
    )
    assert summary.hunk_count == 2
    assert [
        line for line in normalized.splitlines() if not line.startswith("index ")
    ] == OFFICIAL_GOLD_WITHOUT_INDEX.splitlines()


def test_formal_swebench_codec_applies_the_same_safe_index_normalization() -> None:
    artifact = SWEBenchVerifiedSolutionCodec().parse(OFFICIAL_GOLD_WITHOUT_INDEX)

    assert artifact.raw_response == OFFICIAL_GOLD_WITHOUT_INDEX
    assert artifact.text == _canonicalize_official_gold_patch(
        OFFICIAL_GOLD_WITHOUT_INDEX
    )
    assert artifact.compatibility_trace is not None
    assert artifact.compatibility_trace["policy_id"] == (
        "swebench-verified-official-diff-compat-v1"
    )
    assert artifact.compatibility_trace["inserted_index_lines"] == 2
    assert artifact.compatibility_trace["semantic_content_changed"] is False
    assert validate_unified_diff(artifact.text).file_paths == (
        "django/core/example.py",
        "django/core/second.py",
    )


def test_swebench_compatibility_normalization_does_not_relax_patch_security() -> None:
    unsafe = OFFICIAL_GOLD_WITHOUT_INDEX.replace(
        "a/django/core/example.py b/django/core/example.py",
        "a/../outside.py b/../outside.py",
        1,
    ).replace("--- a/django/core/example.py", "--- a/../outside.py", 1).replace(
        "+++ b/django/core/example.py", "+++ b/../outside.py", 1
    )

    with pytest.raises(ValueError, match="path"):
        SWEBenchVerifiedSolutionCodec().parse(unsafe)


def test_swebench_compatibility_normalizes_new_regular_file_metadata() -> None:
    artifact = SWEBenchVerifiedSolutionCodec().parse(NEW_FILE_WITHOUT_INDEX)

    assert "index 0000000000000000000000000000000000000000.." in artifact.text
    assert artifact.compatibility_trace is not None
    assert artifact.compatibility_trace["inserted_index_lines"] == 1
    assert validate_unified_diff(artifact.text).file_paths == (
        "django/core/new_module.py",
    )


def test_gold_canary_uses_the_swebench_terminal_result_contract() -> None:
    result = SWEBenchVerifiedResult(
        schema_version=1,
        evaluator_id=SWEBENCH_VERIFIED_EVALUATOR_ID,
        swebench_source_commit=SWEBENCH_SOURCE_COMMIT,
        attempt_id="swev-" + "b" * 64,
        instance_id=INSTANCE_ID,
        candidate_sha256="c" * 64,
        dataset_sha256=SWEBENCH_VERIFIED_DATASET_SHA256,
        task_sha256="d" * 64,
        image_manifest_sha256="a" * 64,
        status="valid",
        valid_scored=True,
        resolved=True,
        fail_to_pass_passed=1,
        fail_to_pass_total=1,
        pass_to_pass_passed=2,
        pass_to_pass_total=2,
        score=1.0,
        evaluator_seconds=10.0,
        error_type="",
        error_summary="",
        trust_grade="official_standard_candidate_visible_test_process",
    )

    assert not hasattr(result, "correct")
    assert _gold_canary_result_passed(result)
    assert not _gold_canary_result_passed(replace(result, valid_scored=False))
    assert not _gold_canary_result_passed(replace(result, resolved=False))
    assert not _gold_canary_result_passed(replace(result, score=0.5))


def test_swebench_verified_remote_result_requires_exact_binding() -> None:
    task = _task()
    adapter = SWEBenchVerifiedRemoteAdapter(
        task=task,
        host_alias="a100jump",
        remote_python="/data/runtime/bin/python",
        remote_project_root="/data/runtime/Moss",
        remote_swebench_source_root="/data/runtime/SWE-bench",
        remote_attempt_root="/data/runtime/attempts",
    )
    attempt_id = "swev-" + "b" * 64
    candidate_sha = "c" * 64
    payload = {
        "schema_version": 1,
        "evaluator_id": SWEBENCH_VERIFIED_EVALUATOR_ID,
        "swebench_source_commit": SWEBENCH_SOURCE_COMMIT,
        "attempt_id": attempt_id,
        "instance_id": INSTANCE_ID,
        "candidate_sha256": candidate_sha,
        "dataset_sha256": SWEBENCH_VERIFIED_DATASET_SHA256,
        "task_sha256": task.task_sha256,
        "image_manifest_sha256": "a" * 64,
        "status": "valid",
        "valid_scored": True,
        "resolved": False,
        "fail_to_pass_passed": 0,
        "fail_to_pass_total": 1,
        "pass_to_pass_passed": 1,
        "pass_to_pass_total": 1,
        "score": 2 / 3,
        "evaluator_seconds": 42.0,
        "error_type": "",
        "error_summary": "",
        "trust_grade": "official_standard_candidate_visible_test_process",
    }
    result = adapter._parse_result(
        _canonical(payload),
        expected_attempt_id=attempt_id,
        expected_candidate_sha256=candidate_sha,
    )
    assert result.valid_scored is True
    assert result.resolved is False

    payload["resolved"] = True
    with pytest.raises(RuntimeError, match="inconsistent"):
        adapter._parse_result(
            _canonical(payload),
            expected_attempt_id=attempt_id,
            expected_candidate_sha256=candidate_sha,
        )


def test_swebench_worker_replays_a_bound_terminal_result(tmp_path: Path) -> None:
    task = _task()
    request = {
        "schema_version": 1,
        "attempt_id": "swev-" + "b" * 64,
        "instance_id": INSTANCE_ID,
        "candidate_sha256": "c" * 64,
        "dataset_sha256": SWEBENCH_VERIFIED_DATASET_SHA256,
        "task_sha256": task.task_sha256,
        "locked_image_ref": task.locked_image_ref,
        "mutable_image_ref": task.mutable_image_ref,
        "instance": dict(task.instance),
        "timeout_seconds": 1800,
    }
    result = {
        "schema_version": 1,
        "evaluator_id": SWEBENCH_VERIFIED_EVALUATOR_ID,
        "swebench_source_commit": SWEBENCH_SOURCE_COMMIT,
        "attempt_id": request["attempt_id"],
        "instance_id": INSTANCE_ID,
        "candidate_sha256": request["candidate_sha256"],
        "dataset_sha256": SWEBENCH_VERIFIED_DATASET_SHA256,
        "task_sha256": task.task_sha256,
        "image_manifest_sha256": "a" * 64,
        "status": "valid",
        "valid_scored": True,
        "resolved": True,
        "fail_to_pass_passed": 1,
        "fail_to_pass_total": 1,
        "pass_to_pass_passed": 1,
        "pass_to_pass_total": 1,
        "score": 1.0,
        "evaluator_seconds": 10.0,
        "error_type": "",
        "error_summary": "",
        "trust_grade": "official_standard_candidate_visible_test_process",
    }
    path = tmp_path / "result.json"
    path.write_bytes(_canonical(result))

    assert _replay_worker_result(path, request) == 0
    result["candidate_sha256"] = "d" * 64
    path.write_bytes(_canonical(result))
    with pytest.raises(RuntimeError, match="binding"):
        _replay_worker_result(path, request)


def test_swebench_worker_preserves_network_isolation_with_loopback() -> None:
    assert _container_network_options() == {
        "network_mode": "none",
        "extra_hosts": {"localhost": "127.0.0.1"},
    }

    _require_loopback_preflight(0)
    with pytest.raises(RuntimeError, match="loopback"):
        _require_loopback_preflight(1)


def test_swebench_worker_never_falls_back_or_pulls_when_locked_image_is_absent() -> None:
    class ImageNotFound(Exception):
        pass

    class Images:
        def __init__(self) -> None:
            self.requests: list[str] = []

        def get(self, reference: str):
            self.requests.append(reference)
            raise ImageNotFound(reference)

        def pull(self, reference: str):  # pragma: no cover - forbidden path
            raise AssertionError(f"worker attempted a network pull: {reference}")

    class Client:
        images = Images()

    locked = "docker.io/swebench/example@sha256:" + "a" * 64
    with pytest.raises(RuntimeError, match="not locally materialized"):
        _load_locked_local_image(
            Client(),
            locked,
            image_not_found_error=ImageNotFound,
        )
    assert Client.images.requests == [locked]


def test_swebench_worker_rejects_wrong_digest_on_local_image() -> None:
    class ImageNotFound(Exception):
        pass

    class Image:
        attrs = {"RepoDigests": ["docker.io/swebench/example@sha256:" + "b" * 64]}

    class Images:
        @staticmethod
        def get(_reference: str):
            return Image()

    class Client:
        images = Images()

    with pytest.raises(RuntimeError, match="digest differs"):
        _load_locked_local_image(
            Client(),
            "docker.io/swebench/example@sha256:" + "a" * 64,
            image_not_found_error=ImageNotFound,
        )


def test_swebench_worker_accepts_one_local_alias_with_the_locked_digest() -> None:
    class ImageNotFound(Exception):
        pass

    digest = "a" * 64

    class Image:
        attrs = {"RepoDigests": ["127.0.0.1:5056/import@sha256:" + digest]}

    class Images:
        @staticmethod
        def get(_reference: str):
            raise ImageNotFound

        @staticmethod
        def list(*, all: bool):
            assert all is True
            return [Image()]

    class Client:
        images = Images()

    assert (
        _load_locked_local_image(
            Client(),
            "docker.io/swebench/example@sha256:" + digest,
            image_not_found_error=ImageNotFound,
        ).attrs
        == Image.attrs
    )


def test_swebench_worker_rejects_ambiguous_local_digest_aliases() -> None:
    class ImageNotFound(Exception):
        pass

    digest = "a" * 64

    class Image:
        attrs = {"RepoDigests": ["127.0.0.1:5056/import@sha256:" + digest]}

    class Images:
        @staticmethod
        def get(_reference: str):
            raise ImageNotFound

        @staticmethod
        def list(*, all: bool):
            assert all is True
            return [Image(), Image()]

    class Client:
        images = Images()

    with pytest.raises(RuntimeError, match="uniquely"):
        _load_locked_local_image(
            Client(),
            "docker.io/swebench/example@sha256:" + digest,
            image_not_found_error=ImageNotFound,
        )
