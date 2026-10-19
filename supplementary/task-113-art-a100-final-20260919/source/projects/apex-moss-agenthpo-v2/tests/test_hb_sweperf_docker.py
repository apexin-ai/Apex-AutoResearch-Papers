from __future__ import annotations

import hashlib
import json
import os
import stat
import subprocess
from dataclasses import asdict
from pathlib import Path
from typing import Sequence

import pytest

from optimization_lab.harness_builder.adapters.sweperf import (
    DATASET_COMMIT,
    DATASET_PARQUET_SHA256,
    EVALUATOR_COMMIT,
    PATCH_APPLY_MODE,
    SWEPERF_EVALUATOR_ID,
    AttemptBinding,
    EvaluationStage,
    StageRequest,
)
from optimization_lab.harness_builder.adapters.sweperf_docker import (
    CANDIDATE_WORKER_UID,
    DockerCommandResult,
    IMAGE_CONTRACT_LABEL,
    IMAGE_CONTRACT_NAME,
    IMAGE_CONTRACT_SHA256,
    IMAGE_CONTRACT_SHA256_LABEL,
    IMAGE_CONTRACT_VERSION,
    IMAGE_CONTRACT_VERSION_LABEL,
    IMAGE_DATASET_COMMIT_LABEL,
    IMAGE_ENTRYPOINT_LABEL,
    IMAGE_EVALUATOR_COMMIT_LABEL,
    IMAGE_INSTANCE_ID_LABEL,
    IMAGE_PRIVATE_CHANNEL_LABEL,
    IMAGE_RESOURCE_LIMITS_SHA256_LABEL,
    IMAGE_SUPERVISOR_UID_LABEL,
    IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL,
    IMAGE_TASK_MANIFEST_SHA256_LABEL,
    IMAGE_TASK_SHA256_LABEL,
    IMAGE_UPSTREAM_REF_SHA256_LABEL,
    IMAGE_WORKER_CAPABILITIES_LABEL,
    IMAGE_WORKER_UID_LABEL,
    ImageContractNotVerifiedError,
    ProductionSWEPerfDockerExecutor,
    SecurityLimits,
    TRUSTED_STAGE_COMMAND,
    WrapperImageIdentity,
)


IMAGE = "registry.invalid/hb-sweperf@sha256:" + "a" * 64
PATCH = b"""diff --git a/pkg/core.py b/pkg/core.py
index 1234567..89abcde 100644
--- a/pkg/core.py
+++ b/pkg/core.py
@@ -1,2 +1,2 @@
 def calculate():
-    return slow_path()
+    return fast_path()
"""
RECEIPT = "c" * 64
WRAPPER_IDENTITY = WrapperImageIdentity(
    instance_id="astropy__astropy-13817",
    task_sha256="55aa75150fd32ebadac1ad0e761433ec090e0be0ca583974f2736f5e637a8da4",
    task_manifest_sha256="d" * 64,
    supervisor_bundle_sha256="e" * 64,
    upstream_ref_sha256="f" * 64,
    resource_limits_sha256="1" * 64,
)


def _binding(attempt_id: str = "attempt-001") -> AttemptBinding:
    return AttemptBinding(
        attempt_id=attempt_id,
        instance_id="astropy__astropy-13817",
        repository="astropy/astropy",
        evaluator=SWEPERF_EVALUATOR_ID,
        evaluator_commit=EVALUATOR_COMMIT,
        dataset_commit=DATASET_COMMIT,
        dataset_parquet_sha256=DATASET_PARQUET_SHA256,
        base_commit="d4fc9d9b96f0879c363a8183842e5cf6067fae37",
        task_sha256=(
            "55aa75150fd32ebadac1ad0e761433ec090e0be0ca583974f2736f5e637a8da4"
        ),
        image_ref=IMAGE,
        patch_apply_mode=PATCH_APPLY_MODE,
        patch_sha256=hashlib.sha256(PATCH).hexdigest(),
    )


def _common_result(request: dict[str, object]) -> dict[str, object]:
    binding = request["binding"]
    assert isinstance(binding, dict)
    return {
        "schema_version": 1,
        **binding,
        "result_nonce": request["result_nonce"],
        "stage": request["stage"],
        "status": "passed",
        "failure_kind": None,
        "elapsed_seconds": 2.0,
    }


class FakeDockerRunner:
    """Docker CLI double that emulates only daemon-owned control responses."""

    def __init__(
        self,
        *,
        wait_timeout: bool = False,
        image_contract_mutation=None,
        result_mode: int = 0o600,
        image_available: bool = True,
    ):
        self.commands: list[tuple[tuple[str, ...], float]] = []
        self.private_volume_by_container: dict[str, str] = {}
        self.request_by_container: dict[str, dict[str, object]] = {}
        self.wait_timeout = wait_timeout
        self.start_hook = None
        self.image_contract_mutation = image_contract_mutation
        self.result_mode = result_mode
        self.image_available = image_available

    @staticmethod
    def _option(argv: Sequence[str], prefix: str) -> str:
        return next(item[len(prefix) :] for item in argv if item.startswith(prefix))

    def run(self, argv: Sequence[str], *, timeout_seconds: float) -> DockerCommandResult:
        command = tuple(argv)
        self.commands.append((command, timeout_seconds))
        operation = command[1]
        if operation == "image":
            assert command[2] == "inspect"
            if not self.image_available:
                return DockerCommandResult(returncode=1, stderr=b"image unavailable")
            payload = {
                "id": "sha256:" + "b" * 64,
                "repo_digests": [IMAGE],
                "entrypoint": [TRUSTED_STAGE_COMMAND],
                "labels": {
                    IMAGE_CONTRACT_LABEL: IMAGE_CONTRACT_NAME,
                    IMAGE_CONTRACT_VERSION_LABEL: IMAGE_CONTRACT_VERSION,
                    IMAGE_CONTRACT_SHA256_LABEL: IMAGE_CONTRACT_SHA256,
                    IMAGE_ENTRYPOINT_LABEL: TRUSTED_STAGE_COMMAND,
                    IMAGE_SUPERVISOR_UID_LABEL: "0",
                    IMAGE_WORKER_UID_LABEL: str(CANDIDATE_WORKER_UID),
                    IMAGE_WORKER_CAPABILITIES_LABEL: "none",
                    IMAGE_PRIVATE_CHANNEL_LABEL: "root-0700-files-0600-v1",
                    IMAGE_EVALUATOR_COMMIT_LABEL: EVALUATOR_COMMIT,
                    IMAGE_DATASET_COMMIT_LABEL: DATASET_COMMIT,
                    IMAGE_TASK_MANIFEST_SHA256_LABEL: (
                        WRAPPER_IDENTITY.task_manifest_sha256
                    ),
                    IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL: (
                        WRAPPER_IDENTITY.supervisor_bundle_sha256
                    ),
                    IMAGE_UPSTREAM_REF_SHA256_LABEL: (
                        WRAPPER_IDENTITY.upstream_ref_sha256
                    ),
                    IMAGE_RESOURCE_LIMITS_SHA256_LABEL: (
                        WRAPPER_IDENTITY.resource_limits_sha256
                    ),
                    IMAGE_INSTANCE_ID_LABEL: WRAPPER_IDENTITY.instance_id,
                    IMAGE_TASK_SHA256_LABEL: WRAPPER_IDENTITY.task_sha256,
                },
            }
            if self.image_contract_mutation is not None:
                self.image_contract_mutation(payload)
            return DockerCommandResult(
                returncode=0,
                stdout=json.dumps(payload, separators=(",", ":")).encode() + b"\n",
            )
        if operation == "volume":
            if command[2] == "create":
                return DockerCommandResult(
                    returncode=0, stdout=command[-1].encode() + b"\n"
                )
            if command[2] == "rm":
                return DockerCommandResult(returncode=0)
            raise AssertionError(f"unexpected volume operation: {command}")
        if operation == "create":
            name = command[command.index("--name") + 1]
            private_mount = next(
                item
                for item in command
                if item.startswith("--mount=type=volume,")
                and "dst=/run/hb-private" in item
            )
            source = self._option((private_mount,), "--mount=type=volume,src=").split(
                ",dst=", 1
            )[0]
            self.private_volume_by_container[name] = source
            return DockerCommandResult(returncode=0, stdout=b"d" * 64 + b"\n")
        if operation == "cp":
            source, destination = command[-2:]
            if ":" in destination:
                container, path = destination.split(":", 1)
                assert path == "/run/hb-private/request.json"
                self.request_by_container[container] = json.loads(
                    Path(source).read_text(encoding="utf-8")
                )
                return DockerCommandResult(returncode=0)
            container, path = source.split(":", 1)
            request = self.request_by_container[container]
            assert path == f"/run/hb-private/result-{request['result_nonce']}.json"
            result = _common_result(request)
            if request["stage"] == "correctness":
                result.update(
                    {
                        "patch_applied": True,
                        "tests_passed": 5,
                        "tests_total": 5,
                        "correctness_receipt": RECEIPT,
                    }
                )
            else:
                result.update(
                    {
                        "correctness_receipt": RECEIPT,
                        "measurements": [
                            {
                                "test_id": "private-performance-node",
                                "reference_seconds": [2.0] * 20,
                                "candidate_seconds": [1.0] * 20,
                                "candidate_correct": [True] * 20,
                            }
                        ],
                        "score": 2.0,
                    }
                )
            destination_path = Path(destination)
            destination_path.write_text(
                json.dumps(result, separators=(",", ":")), encoding="utf-8"
            )
            destination_path.chmod(self.result_mode)
            return DockerCommandResult(returncode=0)
        if operation == "start":
            hook, self.start_hook = self.start_hook, None
            if hook is not None:
                hook()
            return DockerCommandResult(returncode=0, stdout=b"daemon-started\n")
        if operation == "wait":
            if self.wait_timeout:
                raise subprocess.TimeoutExpired(command, timeout_seconds)
            return DockerCommandResult(
                returncode=0,
                stdout=b"0\n",
                stderr=b'candidate says {"score":999999,"status":"passed"}',
            )
        if operation in {"kill", "rm"}:
            return DockerCommandResult(returncode=0)
        raise AssertionError(f"unexpected Docker operation: {operation}")


@pytest.fixture
def seccomp_profile(tmp_path: Path) -> Path:
    profile = tmp_path / "seccomp.json"
    profile.write_text('{"defaultAction":"SCMP_ACT_ERRNO"}\n', encoding="utf-8")
    profile.chmod(0o600)
    return profile


def _executor(
    tmp_path: Path,
    seccomp_profile: Path,
    runner: FakeDockerRunner,
) -> ProductionSWEPerfDockerExecutor:
    return ProductionSWEPerfDockerExecutor(
        workspace_root=tmp_path / "attempts",
        image_ref=IMAGE,
        wrapper_identity=WRAPPER_IDENTITY,
        seccomp_profile=seccomp_profile,
        runner=runner,
        limits=SecurityLimits(
            tmpfs_bytes=512 * 1024**2,
            correctness_timeout_seconds=300.0,
            performance_timeout_seconds=3300.0,
        ),
    )


def _correctness_request(binding: AttemptBinding, nonce: str = "1" * 64):
    return StageRequest(
        binding=binding,
        stage=EvaluationStage.CORRECTNESS,
        result_nonce=nonce,
    )


def _performance_request(binding: AttemptBinding, nonce: str = "2" * 64):
    return StageRequest(
        binding=binding,
        stage=EvaluationStage.PERFORMANCE,
        result_nonce=nonce,
        correctness_receipt=RECEIPT,
    )


def test_create_uses_a_digest_pinned_fresh_locked_down_container(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner()
    executor = _executor(tmp_path, seccomp_profile, runner)
    binding = _binding()

    workspace = executor.create_workspace(binding)

    inspect_command = runner.commands[0][0]
    assert inspect_command[:3] == ("docker", "image", "inspect")
    assert inspect_command[-1] == IMAGE
    command = next(command for command, _ in runner.commands if command[1] == "create")
    assert command[:2] == ("docker", "create")
    assert "--network=none" in command
    assert "--read-only" in command
    assert "--cap-drop=ALL" in command
    assert set(part for part in command if part.startswith("--cap-add=")) == {
        "--cap-add=SETUID",
        "--cap-add=SETGID",
    }
    assert "--security-opt=no-new-privileges=true" in command
    assert f"--security-opt=seccomp={seccomp_profile.resolve()}" in command
    assert "--pids-limit=512" in command
    assert "--cpus=10" in command
    assert "--memory=34359738368" in command
    assert "--memory-swap=34359738368" in command
    assert "--log-driver=none" in command
    assert "--user=0:0" in command
    assert any(item.startswith("--tmpfs=/tmp:") for item in command)
    assert any(item.startswith("--tmpfs=/var/tmp:") for item in command)
    assert command[command.index("--entrypoint") + 1] == TRUSTED_STAGE_COMMAND
    assert command[-1] == IMAGE
    assert not any("/var/run/docker.sock" in item for item in command)
    private_mount = next(item for item in command if "dst=/run/hb-private" in item)
    assert private_mount.startswith("--mount=type=volume,")
    assert str(tmp_path / "attempts") not in private_mount
    assert workspace.fresh is True
    assert workspace.attempt_id == binding.attempt_id

    attempt_root = tmp_path / "attempts" / workspace.workspace_id
    assert stat.S_IMODE(attempt_root.stat().st_mode) == 0o700
    assert stat.S_IMODE((attempt_root / "private").stat().st_mode) == 0o700
    assert (attempt_root / "scratch").is_dir()
    assert (attempt_root / "cache").is_dir()


def test_candidate_and_private_nonce_channels_are_separate_and_stdout_is_dropped(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner()
    executor = _executor(tmp_path, seccomp_profile, runner)
    binding = _binding()
    workspace = executor.create_workspace(binding)
    executor.copy_candidate(workspace, PATCH)
    request = _correctness_request(binding)

    stage = executor.run_stage(workspace, request)
    raw = executor.read_private_result(workspace, request)

    attempt_root = tmp_path / "attempts" / workspace.workspace_id
    candidate_path = attempt_root / "scratch" / "candidate.patch"
    assert candidate_path.read_bytes() == PATCH
    assert stat.S_IMODE(candidate_path.stat().st_mode) == 0o444
    assert stage.returncode == 0
    assert stage.timed_out is False
    assert stage.stdout == stage.stderr == ""
    assert json.loads(raw)["correctness_receipt"] == RECEIPT
    assert json.loads(raw)["result_nonce"] == request.result_nonce

    request_path = attempt_root / "private" / "request.json"
    result_path = attempt_root / "private" / f"result-{request.result_nonce}.json"
    assert stat.S_IMODE(request_path.stat().st_mode) == 0o600
    assert stat.S_IMODE(result_path.stat().st_mode) == 0o600
    assert not any(
        request.result_nonce in part
        for command, _ in runner.commands
        if command[1] in {"create", "start", "wait"}
        for part in command
    )
    assert not (attempt_root / "scratch" / result_path.name).exists()
    create_command = next(
        command for command, _ in runner.commands if command[1] == "create"
    )
    assert not any(str(attempt_root / "private") in item for item in create_command)


def test_stage_order_requires_a_read_and_valid_correctness_receipt(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner()
    executor = _executor(tmp_path, seccomp_profile, runner)
    binding = _binding()
    workspace = executor.create_workspace(binding)
    executor.copy_candidate(workspace, PATCH)

    with pytest.raises(RuntimeError, match="correctness"):
        executor.run_stage(workspace, _performance_request(binding))

    correctness = _correctness_request(binding)
    executor.run_stage(workspace, correctness)
    with pytest.raises(RuntimeError, match="read"):
        executor.run_stage(workspace, _performance_request(binding))
    executor.read_private_result(workspace, correctness)

    performance = _performance_request(binding)
    run = executor.run_stage(workspace, performance)
    assert run.returncode == 0
    assert json.loads(executor.read_private_result(workspace, performance))["score"] == 2.0

    request_path = (
        tmp_path
        / "attempts"
        / workspace.workspace_id
        / "private"
        / "request.json"
    )
    stages = [json.loads(request_path.read_text())["stage"]]
    assert stages == ["performance"]


def test_stage_is_reserved_before_the_first_docker_side_effect(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner()
    executor = _executor(tmp_path, seccomp_profile, runner)
    binding = _binding()
    workspace = executor.create_workspace(binding)
    executor.copy_candidate(workspace, PATCH)
    request = _correctness_request(binding)

    def reenter() -> None:
        with pytest.raises(RuntimeError, match="already run"):
            executor.run_stage(workspace, request)

    runner.start_hook = reenter
    assert executor.run_stage(workspace, request).returncode == 0


def test_each_attempt_has_distinct_container_scratch_cache_and_is_destroyed(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner()
    executor = _executor(tmp_path, seccomp_profile, runner)
    first = executor.create_workspace(_binding("attempt-001"))
    second = executor.create_workspace(_binding("attempt-002"))

    assert first.workspace_id != second.workspace_id
    create_commands = [command for command, _ in runner.commands if command[1] == "create"]
    first_name = create_commands[0][create_commands[0].index("--name") + 1]
    second_name = create_commands[1][create_commands[1].index("--name") + 1]
    assert first_name != second_name
    first_mounts = {part for part in create_commands[0] if part.startswith("--mount=")}
    second_mounts = {part for part in create_commands[1] if part.startswith("--mount=")}
    assert first_mounts.isdisjoint(second_mounts)

    first_root = tmp_path / "attempts" / first.workspace_id
    executor.destroy_workspace(first)
    assert not first_root.exists()
    assert any(command[1:3] == ("rm", "--force") for command, _ in runner.commands)


def test_timeout_kills_container_and_never_fabricates_a_result(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner(wait_timeout=True)
    executor = _executor(tmp_path, seccomp_profile, runner)
    binding = _binding()
    workspace = executor.create_workspace(binding)
    executor.copy_candidate(workspace, PATCH)
    request = _correctness_request(binding)

    result = executor.run_stage(workspace, request)

    assert result.timed_out is True
    assert result.returncode == 124
    assert result.stdout == result.stderr == ""
    assert any(command[1] == "kill" for command, _ in runner.commands)
    with pytest.raises(RuntimeError, match="not available"):
        executor.read_private_result(workspace, request)


def test_rejects_unpinned_image_unsafe_seccomp_and_wrong_patch(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner()
    with pytest.raises(ValueError, match="digest"):
        ProductionSWEPerfDockerExecutor(
            workspace_root=tmp_path / "attempts",
            image_ref="registry.invalid/hb-sweperf:latest",
            wrapper_identity=WRAPPER_IDENTITY,
            seccomp_profile=seccomp_profile,
            runner=runner,
        )
    symlink = tmp_path / "seccomp-link.json"
    symlink.symlink_to(seccomp_profile)
    with pytest.raises(ValueError, match="seccomp"):
        ProductionSWEPerfDockerExecutor(
            workspace_root=tmp_path / "attempts-2",
            image_ref=IMAGE,
            wrapper_identity=WRAPPER_IDENTITY,
            seccomp_profile=symlink,
            runner=runner,
        )

    executor = _executor(tmp_path, seccomp_profile, runner)
    binding = _binding()
    workspace = executor.create_workspace(binding)
    with pytest.raises(ValueError, match="hash"):
        executor.copy_candidate(
            workspace, PATCH.replace(b"fast_path", b"faster_path")
        )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda payload: payload["repo_digests"].clear(),
        lambda payload: payload.__setitem__("entrypoint", ["/bin/sh"]),
        lambda payload: payload["labels"].pop(IMAGE_ENTRYPOINT_LABEL),
        lambda payload: payload["labels"].__setitem__(
            IMAGE_WORKER_UID_LABEL, "1000"
        ),
        lambda payload: payload["labels"].__setitem__(
            IMAGE_PRIVATE_CHANNEL_LABEL, "shared-with-candidate"
        ),
        lambda payload: payload["labels"].__setitem__(
            IMAGE_CONTRACT_SHA256_LABEL, "0" * 64
        ),
        lambda payload: payload["labels"].__setitem__(
            IMAGE_TASK_MANIFEST_SHA256_LABEL, "0" * 64
        ),
        lambda payload: payload["labels"].pop(
            IMAGE_SUPERVISOR_BUNDLE_SHA256_LABEL
        ),
    ],
)
def test_unverified_wrapper_image_contract_fails_closed_before_workspace_creation(
    tmp_path: Path, seccomp_profile: Path, mutation
) -> None:
    runner = FakeDockerRunner(image_contract_mutation=mutation)
    executor = _executor(tmp_path, seccomp_profile, runner)

    with pytest.raises(ImageContractNotVerifiedError, match="image-contract"):
        executor.create_workspace(_binding())

    assert not any(command[1] == "create" for command, _ in runner.commands)
    assert not any(command[1] == "volume" for command, _ in runner.commands)


def test_missing_production_wrapper_is_named_as_unverified_image_contract(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner(image_available=False)
    executor = _executor(tmp_path, seccomp_profile, runner)

    with pytest.raises(
        ImageContractNotVerifiedError,
        match="SWE-Perf image-contract not verified",
    ):
        executor.create_workspace(_binding())

    assert [command[1] for command, _ in runner.commands] == ["image"]


def test_private_result_must_be_regular_owner_only_and_bound_to_the_request(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner(result_mode=0o644)
    executor = _executor(tmp_path, seccomp_profile, runner)
    binding = _binding()
    workspace = executor.create_workspace(binding)
    executor.copy_candidate(workspace, PATCH)
    request = _correctness_request(binding)
    executor.run_stage(workspace, request)

    with pytest.raises(RuntimeError, match="permissions"):
        executor.read_private_result(workspace, request)


def test_container_request_contains_only_the_exact_stage_binding(
    tmp_path: Path, seccomp_profile: Path
) -> None:
    runner = FakeDockerRunner()
    executor = _executor(tmp_path, seccomp_profile, runner)
    binding = _binding()
    workspace = executor.create_workspace(binding)
    executor.copy_candidate(workspace, PATCH)
    request = _correctness_request(binding)
    executor.run_stage(workspace, request)

    request_payload = json.loads(
        (
            tmp_path
            / "attempts"
            / workspace.workspace_id
            / "private"
            / "request.json"
        ).read_text(encoding="utf-8")
    )
    assert request_payload == {
        "schema_version": 1,
        "binding": asdict(binding),
        "stage": "correctness",
        "result_nonce": request.result_nonce,
        "correctness_receipt": None,
        "candidate_path": "/hb/work/candidate.patch",
        "scratch_path": "/hb/work",
        "cache_path": "/hb/cache",
    }
    assert "result_path" not in request_payload
    assert "docker_socket" not in request_payload
