"""Offline preparation and independent verification for the KernelBench meta canary.

The ten-seat canary is deliberately split into two phases.  This module may
materialize immutable candidate bytes without an entitlement or GPU.  A
separate controller must reserve/start each evaluator operation before invoking
the production adapter.  Formal activation is minted only by independently
replaying that controller journal and the content-addressed result artifacts.
"""

from __future__ import annotations

import ast
import fcntl
import hashlib
import json
import math
import os
import re
import stat
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Protocol

from optimization_lab.adapters.base import EvaluationResult, EvaluationStatus

from .adapters.kernel_candidate_policy import (
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
    RestrictedKernelCandidateError,
    RestrictedKernelCandidatePolicy,
)
from .adapters.kernelbench_meta import (
    KERNELBENCH_META_CANARY_TASKS,
    KERNELBENCH_META_PROTOCOL_SHA256,
    KERNELBENCH_META_REPOSITORY_COMMIT,
    KERNELBENCH_META_TASK_HASHES,
    KERNELBENCH_META_TASK_SET_SHA256,
    KernelBenchMetaTask,
    MetaCanaryEvaluation,
)
from .events import (
    OperationJournal,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
    verify_operation_journal,
)
from .solutions import KernelBenchSolutionCodec


CANARY_CELL_ID = "canary:kernelbench-meta"
CANARY_EVALUATOR_TRANSACTIONS = 10
CANARY_GPU_EXCLUSIVE_SECONDS = 6000.0
CANARY_OPERATION_GPU_SECONDS = 600.0
_MAX_TASK_BYTES = 2 * 1024 * 1024
_SHA256 = re.compile(r"[0-9a-f]{64}")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_ZERO_SHA256 = "0" * 64
_CANARY_CASE_KEYS = {
    "ordinal",
    "canary_id",
    "task_id",
    "task_sha256",
    "candidate_object",
    "candidate_sha256",
    "candidate_policy_sha256",
    "policy_state",
    "policy_reason",
    "policy_report_sha256",
    "expected_stage",
    "expected_status",
}
_RESULT_ARTIFACT_KEYS = {
    "schema_version",
    "artifact_kind",
    "operation_id",
    "canary_id",
    "ordinal",
    "task_id",
    "task_sha256",
    "candidate_sha256",
    "candidate_policy_sha256",
    "expected_stage",
    "expected_status",
    "observed",
    "private_evidence_sha256",
    "code_revision",
    "staging_plan_sha256",
    "canary_plan_sha256",
    "authorization_receipt_sha256",
    "scorer_bundle_sha256",
    "protocol_sha256",
}
_PUBLIC_EVALUATION_KEYS = {
    "status",
    "compiled",
    "correct",
    "candidate_runtime_ms",
    "reference_runtime_ms",
    "error_summary",
    "elapsed_seconds",
    "gpu_exclusive_seconds",
    "hardware",
    "speedup",
    "correctness_passed",
    "timing_trials_completed",
    "timing_outputs_correct",
}

_EXPECTED_STATUS = {
    **{
        canary_id: EvaluationStatus.VALID.value
        for canary_id in KERNELBENCH_META_CANARY_TASKS
        if canary_id.startswith("reference-")
    },
    "adversarial-wrong": EvaluationStatus.INCORRECT.value,
    "adversarial-first5-timing-wrong": EvaluationStatus.INCORRECT.value,
    "adversarial-fake-stdout": EvaluationStatus.POLICY_REJECTED.value,
    "adversarial-private-overwrite": EvaluationStatus.POLICY_REJECTED.value,
}
_EXPECTED_STAGE = {
    canary_id: (
        "policy_preflight"
        if canary_id in {
            "adversarial-fake-stdout",
            "adversarial-private-overwrite",
        }
        else "trusted_gpu_evaluator"
    )
    for canary_id in KERNELBENCH_META_CANARY_TASKS
}
_EXPECTED_PROTOCOL_COUNTS = {
    **{
        canary_id: (5, 100, 100)
        for canary_id in KERNELBENCH_META_CANARY_TASKS
        if canary_id.startswith("reference-")
    },
    "adversarial-wrong": (0, 0, 0),
    "adversarial-first5-timing-wrong": (5, 1, 0),
    "adversarial-fake-stdout": (0, 0, 0),
    "adversarial-private-overwrite": (0, 0, 0),
}


class KernelBenchMetaCanaryError(RuntimeError):
    """The immutable canary plan or evidence is incomplete or inconsistent."""


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _write_once(path: Path, content: bytes, *, mode: int = 0o600) -> None:
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        metadata = None
    if metadata is not None:
        if (
            stat.S_ISLNK(metadata.st_mode)
            or not stat.S_ISREG(metadata.st_mode)
            or metadata.st_uid != os.geteuid()
            or stat.S_IMODE(metadata.st_mode) != mode
            or path.read_bytes() != content
        ):
            raise KernelBenchMetaCanaryError(
                f"refusing to overwrite different canary artifact: {path.name}"
            )
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent, suffix=".kernelbench-meta-canary.tmp"
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(mode)
        temporary.replace(path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def _git_output(repository: Path, *arguments: str) -> str:
    process = subprocess.run(
        ("git", "-C", str(repository), *arguments),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        timeout=30,
        check=False,
    )
    if process.returncode != 0:
        raise KernelBenchMetaCanaryError("cannot inspect frozen KernelBench checkout")
    return process.stdout.strip()


def _read_task(repository: Path, task_id: str) -> bytes:
    path = repository / "KernelBench" / task_id
    try:
        metadata = path.lstat()
    except OSError as exc:
        raise KernelBenchMetaCanaryError(f"missing frozen task: {task_id}") from exc
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise KernelBenchMetaCanaryError("frozen task must be a regular non-symlink")
    raw = path.read_bytes()
    if not raw or len(raw) > _MAX_TASK_BYTES:
        raise KernelBenchMetaCanaryError("frozen task source size is invalid")
    expected = KERNELBENCH_META_TASK_HASHES[task_id]
    if hashlib.sha256(raw).hexdigest() != expected:
        raise KernelBenchMetaCanaryError(f"frozen task digest differs: {task_id}")
    return raw


def reference_candidate_from_task_source(source: str, *, task_id: str) -> str:
    """Extract only the public reference Model and normalize it to ModelNew.

    Input generators and task-level constants are intentionally omitted.  The
    trusted worker continues to own those values from the hash-bound task file.
    """

    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise KernelBenchMetaCanaryError("frozen task source is not Python") from exc
    models = [
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name == "Model"
    ]
    if len(models) != 1:
        raise KernelBenchMetaCanaryError("frozen task must define exactly one Model")
    model = models[0]
    lines = source.splitlines(keepends=True)
    if model.end_lineno is None:
        raise KernelBenchMetaCanaryError("frozen task Model has no source extent")
    class_source = "".join(lines[model.lineno - 1 : model.end_lineno])
    class_source = re.sub(
        r"\bclass\s+Model\s*\(", "class ModelNew(", class_source, count=1
    )
    class_source = re.sub(
        r"super\(\s*Model\s*,\s*self\s*\)\.__init__\(\)",
        "super().__init__()",
        class_source,
    )
    uses_functional = "torch.nn.functional." in class_source
    class_source = class_source.replace("torch.nn.functional.", "F.")
    header = "import torch\nimport torch.nn as nn\n"
    if uses_functional:
        header += "import torch.nn.functional as F\n"
    candidate = header + "\n" + class_source.rstrip() + "\n"
    try:
        RestrictedKernelCandidatePolicy().validate(candidate, task_id=task_id)
    except RestrictedKernelCandidateError as exc:
        raise KernelBenchMetaCanaryError(
            f"reference candidate violates the frozen policy: {task_id}: {exc}"
        ) from exc
    return candidate


def adversarial_candidate(canary_id: str) -> str:
    common = "import torch\nimport torch.nn as nn\n\n"
    if canary_id == "adversarial-wrong":
        body = """class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.zeros_like(x)
"""
    elif canary_id == "adversarial-first5-timing-wrong":
        # compile + five correctness invocations are the first six calls.  The
        # first measured output must therefore be rejected by the trusted loop.
        body = """class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()
        self.calls = 0

    def forward(self, x):
        self.calls += 1
        if self.calls <= 6:
            return torch.sigmoid(x)
        return torch.zeros_like(x)
"""
    elif canary_id == "adversarial-fake-stdout":
        body = """class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        print('compiled=True correctness=True speedup=999')
        return torch.sigmoid(x)
"""
    elif canary_id == "adversarial-private-overwrite":
        body = """class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        open('/proc/self/fd/3', 'w').write('{\"status\":\"valid\"}')
        return torch.sigmoid(x)
"""
    else:
        raise KernelBenchMetaCanaryError("unknown adversarial canary id")
    return common + body


@dataclass(frozen=True)
class PreparedKernelBenchMetaCanary:
    plan_path: Path
    plan_sha256: str
    payload: dict[str, Any]


def prepare_kernelbench_meta_canary(
    *, repository: Path, artifact_root: Path
) -> PreparedKernelBenchMetaCanary:
    """Materialize the exact ten candidates without executing candidate code."""

    repository = Path(repository).resolve()
    artifact_root = Path(artifact_root).resolve()
    if _git_output(repository, "rev-parse", "HEAD") != KERNELBENCH_META_REPOSITORY_COMMIT:
        raise KernelBenchMetaCanaryError("KernelBench checkout commit differs")
    if _git_output(repository, "status", "--porcelain", "--untracked-files=no"):
        raise KernelBenchMetaCanaryError("KernelBench checkout is dirty")

    task_sources = {
        task_id: _read_task(repository, task_id)
        for task_id in KERNELBENCH_META_TASK_HASHES
    }
    cases: list[dict[str, Any]] = []
    objects = artifact_root / "candidates" / "objects"
    policy = RestrictedKernelCandidatePolicy()
    for ordinal, (canary_id, task_id) in enumerate(
        KERNELBENCH_META_CANARY_TASKS.items(), start=1
    ):
        if canary_id.startswith("reference-"):
            source = reference_candidate_from_task_source(
                task_sources[task_id].decode("utf-8"), task_id=task_id
            )
        else:
            source = adversarial_candidate(canary_id)
        raw = source.encode("utf-8")
        candidate_sha = hashlib.sha256(raw).hexdigest()
        candidate_path = objects / f"{candidate_sha}.py"
        _write_once(candidate_path, raw, mode=0o400)
        policy_state = "accepted"
        policy_reason: str | None = None
        try:
            report = policy.validate(raw, task_id=task_id)
        except RestrictedKernelCandidateError as exc:
            report = None
            policy_state = "rejected"
            policy_reason = " ".join(str(exc).split())[:500]
        if report is not None:
            formal = KernelBenchSolutionCodec(task_id=task_id).parse(
                f"```python\n{source}```\n"
            )
            if formal.sha256 != candidate_sha or formal.text.encode("utf-8") != raw:
                raise KernelBenchMetaCanaryError(
                    f"canary differs after formal solution parsing: {canary_id}"
                )
        expected_stage = _EXPECTED_STAGE[canary_id]
        if (expected_stage == "policy_preflight") != (policy_state == "rejected"):
            raise KernelBenchMetaCanaryError(
                f"canary policy stage differs: {canary_id}"
            )
        cases.append(
            {
                "ordinal": ordinal,
                "canary_id": canary_id,
                "task_id": task_id,
                "task_sha256": KERNELBENCH_META_TASK_HASHES[task_id],
                "candidate_object": (
                    f"candidates/objects/{candidate_sha}.py"
                ),
                "candidate_sha256": candidate_sha,
                "candidate_policy_sha256": RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
                "policy_state": policy_state,
                "policy_reason": policy_reason,
                "policy_report_sha256": (
                    None
                    if report is None
                    else hashlib.sha256(
                        _canonical_bytes(
                            {
                                "source_sha256": report.source_sha256,
                                "policy_sha256": report.policy_sha256,
                                "imports": list(report.imports),
                                "triton_kernels": list(report.triton_kernels),
                                "model_methods": list(report.model_methods),
                                "ast_node_count": report.ast_node_count,
                                "task_id": report.task_id,
                            }
                        )
                    ).hexdigest()
                ),
                "expected_stage": expected_stage,
                "expected_status": _EXPECTED_STATUS[canary_id],
            }
        )
    payload: dict[str, Any] = {
        "schema_version": 1,
        "plan_id": "hb-gen1-kernelbench-meta-canary-v1",
        "repository_commit": KERNELBENCH_META_REPOSITORY_COMMIT,
        "task_hashes": dict(KERNELBENCH_META_TASK_HASHES),
        "candidate_policy_sha256": RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
        "cell_id": CANARY_CELL_ID,
        "evaluator_transaction_cap": CANARY_EVALUATOR_TRANSACTIONS,
        "gpu_exclusive_seconds_cap": CANARY_GPU_EXCLUSIVE_SECONDS,
        "cases": cases,
    }
    encoded = _canonical_bytes(payload)
    plan_sha = hashlib.sha256(encoded).hexdigest()
    plan_path = artifact_root / "plans" / f"{plan_sha}.json"
    _write_once(plan_path, encoded, mode=0o600)
    return PreparedKernelBenchMetaCanary(
        plan_path=plan_path, plan_sha256=plan_sha, payload=payload
    )


class KernelBenchMetaCanaryEvaluator(Protocol):
    authorization_receipt_sha256: str

    def evaluate_canary(
        self,
        task: KernelBenchMetaTask,
        candidate_path: Path,
        private_log_dir: Path,
        *,
        canary_id: str,
    ) -> MetaCanaryEvaluation: ...


def _load_object(path: Path, *, label: str) -> tuple[dict[str, Any], bytes]:
    try:
        metadata = path.lstat()
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise OSError
        raw = path.read_bytes()
        payload = json.loads(raw)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise KernelBenchMetaCanaryError(f"{label} is invalid") from exc
    if not isinstance(payload, dict):
        raise KernelBenchMetaCanaryError(f"{label} must be one JSON object")
    return payload, raw


def _load_canonical_object(path: Path, *, label: str) -> tuple[dict[str, Any], bytes]:
    payload, raw = _load_object(path, label=label)
    if raw != _canonical_bytes(payload):
        raise KernelBenchMetaCanaryError(f"{label} is not canonical JSON")
    return payload, raw


def _case_operation_id(case: Mapping[str, Any]) -> str:
    return (
        "canary:kernelbench-meta:"
        f"{int(case['ordinal']):02d}:{case['canary_id']}"
    )


def _public_evaluation(evaluation: MetaCanaryEvaluation) -> dict[str, Any]:
    result = evaluation.result
    if (
        type(result.gpu_seconds) not in (int, float)
        or not math.isfinite(float(result.gpu_seconds))
        or not 0 <= float(result.gpu_seconds) <= CANARY_OPERATION_GPU_SECONDS
    ):
        raise KernelBenchMetaCanaryError("trusted GPU usage exceeded reservation")
    return {
        "status": result.status.value,
        "compiled": result.compiled,
        "correct": result.correct,
        "candidate_runtime_ms": result.candidate_runtime_ms,
        "reference_runtime_ms": result.reference_runtime_ms,
        "error_summary": " ".join(result.error_summary.split())[:500],
        "elapsed_seconds": result.elapsed_seconds,
        "gpu_exclusive_seconds": result.gpu_seconds,
        "hardware": " ".join(result.hardware.split())[:256],
        "speedup": result.speedup_vs_eager,
        "correctness_passed": evaluation.correctness_passed,
        "timing_trials_completed": evaluation.timing_trials_completed,
        "timing_outputs_correct": evaluation.timing_outputs_correct,
    }


def _private_evidence_sha(evaluation: MetaCanaryEvaluation) -> str | None:
    result = evaluation.result
    if not result.raw_log_path:
        return None
    path = Path(result.raw_log_path)
    try:
        metadata = path.lstat()
        raw = path.read_bytes()
    except OSError:
        return None
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        return None
    return hashlib.sha256(raw).hexdigest()


@dataclass(frozen=True)
class VerifiedKernelBenchMetaCanary:
    evidence_path: Path
    evidence_sha256: str
    payload: dict[str, Any]


class KernelBenchMetaCanaryController:
    """Reserve, run and recover the frozen canary without an automatic next phase."""

    def __init__(
        self,
        *,
        artifact_root: Path,
        staging_plan: Path,
        canary_plan: Path,
        code_revision: str,
        scorer_bundle_sha256: str,
        authorization_receipt: Path | None = None,
    ) -> None:
        self.artifact_root = Path(artifact_root).resolve()
        self.root = self.artifact_root / "kernelbench-meta-canary"
        self.staging_path = Path(staging_plan).resolve()
        self.plan_path = Path(canary_plan).resolve()
        if not _COMMIT.fullmatch(code_revision):
            raise KernelBenchMetaCanaryError("canary code revision is invalid")
        if not _SHA256.fullmatch(scorer_bundle_sha256):
            raise KernelBenchMetaCanaryError("canary scorer digest is invalid")
        self.code_revision = code_revision
        self.scorer_bundle_sha256 = scorer_bundle_sha256
        self.staging, self.staging_bytes = _load_object(
            self.staging_path, label="staging plan"
        )
        self.staging_sha256 = hashlib.sha256(self.staging_bytes).hexdigest()
        self.plan, self.plan_bytes = _load_canonical_object(
            self.plan_path, label="KernelBench meta canary plan"
        )
        self.plan_sha256 = hashlib.sha256(self.plan_bytes).hexdigest()
        if self.plan_path.name != f"{self.plan_sha256}.json":
            raise KernelBenchMetaCanaryError("canary plan is not content addressed")
        self._validate_contracts()
        self.journal = OperationJournal(
            self.root / "journal",
            anchor_path=self.root / "trusted-head.json",
        )
        caps = ResourceCaps(
            evaluator_transactions=CANARY_EVALUATOR_TRANSACTIONS,
            gpu_exclusive_seconds=CANARY_GPU_EXCLUSIVE_SECONDS,
        )
        self.governor = ResourceGovernor(
            journal=self.journal,
            global_caps=caps,
            cell_caps={CANARY_CELL_ID: caps},
        )
        self.authorization_receipt: Path | None = None
        self.authorization_receipt_sha256: str | None = None
        if authorization_receipt is not None:
            (
                self.authorization_receipt,
                self.authorization_receipt_sha256,
            ) = self._validate_authorization_receipt(Path(authorization_receipt))

    def _validate_contracts(self) -> None:
        entitlement = {
            "model_calls": 0,
            "evaluator_transactions": CANARY_EVALUATOR_TRANSACTIONS,
            "gpu_exclusive_seconds": CANARY_GPU_EXCLUSIVE_SECONDS,
            "cpu_evaluator_seconds": 0.0,
        }
        if self.staging.get("code_revision") != self.code_revision:
            raise KernelBenchMetaCanaryError("staging code revision differs")
        if (
            not isinstance(self.staging.get("cell_entitlements"), dict)
            or self.staging["cell_entitlements"].get(CANARY_CELL_ID) != entitlement
        ):
            raise KernelBenchMetaCanaryError(
                "KernelBench meta canary entitlement is missing or changed"
            )
        if (
            self.plan.get("schema_version") != 1
            or self.plan.get("plan_id") != "hb-gen1-kernelbench-meta-canary-v1"
            or self.plan.get("repository_commit")
            != KERNELBENCH_META_REPOSITORY_COMMIT
            or self.plan.get("task_hashes") != dict(KERNELBENCH_META_TASK_HASHES)
            or self.plan.get("candidate_policy_sha256")
            != RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256
            or self.plan.get("cell_id") != CANARY_CELL_ID
            or self.plan.get("evaluator_transaction_cap")
            != CANARY_EVALUATOR_TRANSACTIONS
            or self.plan.get("gpu_exclusive_seconds_cap")
            != CANARY_GPU_EXCLUSIVE_SECONDS
        ):
            raise KernelBenchMetaCanaryError("canary plan contract differs")
        cases = self.plan.get("cases")
        if not isinstance(cases, list) or len(cases) != CANARY_EVALUATOR_TRANSACTIONS:
            raise KernelBenchMetaCanaryError("canary plan must contain ten cases")
        if [case.get("canary_id") for case in cases] != list(
            KERNELBENCH_META_CANARY_TASKS
        ):
            raise KernelBenchMetaCanaryError("canary case order differs")
        for ordinal, case in enumerate(cases, start=1):
            if (
                not isinstance(case, dict)
                or set(case) != _CANARY_CASE_KEYS
                or case.get("ordinal") != ordinal
                or case.get("task_id")
                != KERNELBENCH_META_CANARY_TASKS[case["canary_id"]]
                or case.get("expected_status") != _EXPECTED_STATUS[case["canary_id"]]
                or case.get("expected_stage") != _EXPECTED_STAGE[case["canary_id"]]
            ):
                raise KernelBenchMetaCanaryError("canary case binding differs")
            candidate_object = case.get("candidate_object")
            if (
                not isinstance(candidate_object, str)
                or candidate_object
                != f"candidates/objects/{case['candidate_sha256']}.py"
            ):
                raise KernelBenchMetaCanaryError("canary object path differs")
            candidate = self.plan_path.parent.parent / candidate_object
            try:
                candidate_metadata = candidate.lstat()
            except OSError as exc:
                raise KernelBenchMetaCanaryError(
                    "canary candidate binding differs"
                ) from exc
            if (
                stat.S_ISLNK(candidate_metadata.st_mode)
                or not stat.S_ISREG(candidate_metadata.st_mode)
                or candidate.name != f"{case['candidate_sha256']}.py"
                or hashlib.sha256(candidate.read_bytes()).hexdigest()
                != case["candidate_sha256"]
            ):
                raise KernelBenchMetaCanaryError("canary candidate binding differs")

    def expected_authorization_payload(self) -> dict[str, Any]:
        """Return bytes an external trusted issuer must approve and sign by placement."""

        return {
            "schema_version": 1,
            "authorization_type": "hb-gen1-kernelbench-meta-canary-v1",
            "scorer_bundle_sha256": self.scorer_bundle_sha256,
            "protocol_sha256": KERNELBENCH_META_PROTOCOL_SHA256,
            "repository_commit": KERNELBENCH_META_REPOSITORY_COMMIT,
            "task_set_sha256": KERNELBENCH_META_TASK_SET_SHA256,
            "code_revision": self.code_revision,
            "ledger_head_sha256": _ZERO_SHA256,
            "staging_plan_sha256": self.staging_sha256,
            "canary_plan_sha256": self.plan_sha256,
            "canary_ids": list(KERNELBENCH_META_CANARY_TASKS),
            "max_evaluator_transactions": CANARY_EVALUATOR_TRANSACTIONS,
            "max_gpu_exclusive_seconds": int(CANARY_GPU_EXCLUSIVE_SECONDS),
            "canary_evidence_sha256": None,
        }

    def _validate_authorization_receipt(self, path: Path) -> tuple[Path, str]:
        absolute = path.absolute()
        try:
            absolute.relative_to(self.root)
        except ValueError:
            pass
        else:
            raise KernelBenchMetaCanaryError(
                "external canary authorization must be outside the run root"
            )
        payload, raw = _load_canonical_object(
            absolute, label="externally issued canary authorization receipt"
        )
        receipt_sha = hashlib.sha256(raw).hexdigest()
        metadata = absolute.lstat()
        if (
            absolute.name != f"{receipt_sha}.json"
            or metadata.st_uid != os.geteuid()
            or stat.S_IMODE(metadata.st_mode) != 0o600
            or payload != self.expected_authorization_payload()
        ):
            raise KernelBenchMetaCanaryError("external canary authorization differs")
        return absolute.resolve(strict=True), receipt_sha

    def _artifact_path(self, artifact_sha256: str) -> Path:
        return self.root / "results" / "objects" / f"{artifact_sha256}.json"

    def _load_result_artifact(
        self, operation_id: str, artifact_sha256: str
    ) -> dict[str, Any]:
        path = self._artifact_path(artifact_sha256)
        payload, raw = _load_canonical_object(path, label="canary result artifact")
        if (
            hashlib.sha256(raw).hexdigest() != artifact_sha256
            or payload.get("operation_id") != operation_id
        ):
            raise KernelBenchMetaCanaryError("canary result artifact binding differs")
        return payload

    def preflight(self) -> dict[str, Any]:
        replay = self.journal.replay()
        snapshot = self.governor.snapshot()
        blockers: list[str] = []
        if self.authorization_receipt is None:
            blockers.append("authorization_receipt_missing")
        completed = 0
        for case in self.plan["cases"]:
            operation_id = _case_operation_id(case)
            operation = replay.operations.get(operation_id)
            if operation is None or operation.state == "reserved":
                continue
            if operation.state == "started":
                blockers.append(f"abandoned:{case['canary_id']}")
            elif operation.state == "failed":
                blockers.append(f"failed:{case['canary_id']}")
            elif operation.state == "completed":
                terminal = operation.event_for("operation_completed")
                artifact_sha = terminal.payload["artifact_sha256"]
                if artifact_sha is None:
                    blockers.append(f"missing_artifact:{case['canary_id']}")
                else:
                    self._load_result_artifact(operation_id, artifact_sha)
                    completed += 1
        return {
            "schema_version": 1,
            "status": (
                "passed"
                if completed == CANARY_EVALUATOR_TRANSACTIONS and not blockers
                else ("blocked" if blockers else "ready")
            ),
            "blockers": blockers,
            "code_revision": self.code_revision,
            "staging_plan_sha256": self.staging_sha256,
            "canary_plan_sha256": self.plan_sha256,
            "authorization_receipt_present": self.authorization_receipt is not None,
            "completed_cases": completed,
            "committed_evaluator_transactions": (
                snapshot.global_committed.evaluator_transactions
            ),
            "committed_gpu_exclusive_seconds": (
                snapshot.global_committed.gpu_exclusive_seconds
            ),
            "formal_execution_started": False,
        }

    def execute(
        self, evaluator: KernelBenchMetaCanaryEvaluator
    ) -> VerifiedKernelBenchMetaCanary:
        lock_path = self.root / ".execute.lock"
        flags = os.O_RDWR | os.O_CREAT | getattr(os, "O_CLOEXEC", 0)
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        try:
            descriptor = os.open(lock_path, flags, 0o600)
        except OSError as exc:
            raise KernelBenchMetaCanaryError("cannot open canary execute lock") from exc
        try:
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as exc:
                raise KernelBenchMetaCanaryError(
                    "another canary controller holds the execute lock"
                ) from exc
            return self._execute_locked(evaluator)
        finally:
            os.close(descriptor)

    def _execute_locked(
        self, evaluator: KernelBenchMetaCanaryEvaluator
    ) -> VerifiedKernelBenchMetaCanary:
        report = self.preflight()
        if report["blockers"]:
            raise KernelBenchMetaCanaryError(
                "terminal canary blocker: " + ", ".join(report["blockers"])
            )
        if (
            self.authorization_receipt is None
            or self.authorization_receipt_sha256 is None
            or evaluator.authorization_receipt_sha256
            != self.authorization_receipt_sha256
        ):
            raise KernelBenchMetaCanaryError(
                "evaluator capability does not hold the approved receipt"
            )
        replay = self.journal.replay()
        for case in self.plan["cases"]:
            operation_id = _case_operation_id(case)
            operation = replay.operations.get(operation_id)
            if operation is not None and operation.state == "completed":
                continue
            if operation is None:
                self.governor.reserve(
                    operation_id=operation_id,
                    cell_id=CANARY_CELL_ID,
                    operation_kind="evaluator_transaction",
                    reservation=ResourceVector(
                        evaluator_transactions=1,
                        gpu_exclusive_seconds=CANARY_OPERATION_GPU_SECONDS,
                    ),
                )
            self.governor.start(operation_id)
            task = KernelBenchMetaTask.from_task_id(case["task_id"])
            evaluation = evaluator.evaluate_canary(
                task,
                self.plan_path.parent.parent / case["candidate_object"],
                self.root / "private-evaluator" / case["canary_id"],
                canary_id=case["canary_id"],
            )
            public = _public_evaluation(evaluation)
            result_payload = {
                "schema_version": 1,
                "artifact_kind": "hb-gen1-kernelbench-meta-canary-result-v1",
                "operation_id": operation_id,
                "canary_id": case["canary_id"],
                "ordinal": case["ordinal"],
                "task_id": case["task_id"],
                "task_sha256": case["task_sha256"],
                "candidate_sha256": case["candidate_sha256"],
                "candidate_policy_sha256": case["candidate_policy_sha256"],
                "expected_stage": case["expected_stage"],
                "expected_status": case["expected_status"],
                "observed": public,
                "private_evidence_sha256": _private_evidence_sha(evaluation),
                "code_revision": self.code_revision,
                "staging_plan_sha256": self.staging_sha256,
                "canary_plan_sha256": self.plan_sha256,
                "authorization_receipt_sha256": self.authorization_receipt_sha256,
                "scorer_bundle_sha256": self.scorer_bundle_sha256,
                "protocol_sha256": KERNELBENCH_META_PROTOCOL_SHA256,
            }
            result_raw = _canonical_bytes(result_payload)
            result_sha = hashlib.sha256(result_raw).hexdigest()
            _write_once(self._artifact_path(result_sha), result_raw, mode=0o600)
            actual = ResourceVector(
                evaluator_transactions=1,
                gpu_exclusive_seconds=public["gpu_exclusive_seconds"],
            )
            if evaluation.result.status.value == case["expected_status"]:
                self.governor.complete(
                    operation_id,
                    actual_usage=actual,
                    artifact_sha256=result_sha,
                )
            else:
                self.governor.fail(
                    operation_id,
                    reason_code="canary_status_mismatch",
                    actual_usage=actual,
                    artifact_sha256=result_sha,
                )
                raise KernelBenchMetaCanaryError(
                    f"canary status mismatch: {case['canary_id']}"
                )
            replay = self.journal.replay()
        return verify_kernelbench_meta_canary(
            root=self.root,
            staging_plan_sha256=self.staging_sha256,
            canary_plan=self.plan_path,
            code_revision=self.code_revision,
            scorer_bundle_sha256=self.scorer_bundle_sha256,
            authorization_receipt=self.authorization_receipt,
        )


def verify_kernelbench_meta_canary(
    *,
    root: Path,
    staging_plan_sha256: str,
    canary_plan: Path,
    code_revision: str,
    scorer_bundle_sha256: str,
    authorization_receipt: Path,
) -> VerifiedKernelBenchMetaCanary:
    """Independently replay the journal and mint evidence, never formal authority."""

    root = Path(root).resolve()
    if (
        not _SHA256.fullmatch(staging_plan_sha256)
        or not _COMMIT.fullmatch(code_revision)
        or not _SHA256.fullmatch(scorer_bundle_sha256)
    ):
        raise KernelBenchMetaCanaryError("independent verifier binding is invalid")
    plan, plan_raw = _load_canonical_object(
        Path(canary_plan), label="independent canary plan"
    )
    plan_sha = hashlib.sha256(plan_raw).hexdigest()
    if Path(canary_plan).name != f"{plan_sha}.json":
        raise KernelBenchMetaCanaryError("independent canary plan is not addressed")
    receipt, receipt_raw = _load_canonical_object(
        Path(authorization_receipt), label="independent authorization receipt"
    )
    receipt_sha = hashlib.sha256(receipt_raw).hexdigest()
    receipt_metadata = Path(authorization_receipt).lstat()
    if (
        Path(authorization_receipt).name != f"{receipt_sha}.json"
        or receipt_metadata.st_uid != os.geteuid()
        or stat.S_IMODE(receipt_metadata.st_mode) != 0o600
    ):
        raise KernelBenchMetaCanaryError("authorization receipt is not addressed")
    expected_receipt = {
        "schema_version": 1,
        "authorization_type": "hb-gen1-kernelbench-meta-canary-v1",
        "scorer_bundle_sha256": scorer_bundle_sha256,
        "protocol_sha256": KERNELBENCH_META_PROTOCOL_SHA256,
        "repository_commit": KERNELBENCH_META_REPOSITORY_COMMIT,
        "task_set_sha256": KERNELBENCH_META_TASK_SET_SHA256,
        "code_revision": code_revision,
        "ledger_head_sha256": _ZERO_SHA256,
        "staging_plan_sha256": staging_plan_sha256,
        "canary_plan_sha256": plan_sha,
        "canary_ids": list(KERNELBENCH_META_CANARY_TASKS),
        "max_evaluator_transactions": CANARY_EVALUATOR_TRANSACTIONS,
        "max_gpu_exclusive_seconds": int(CANARY_GPU_EXCLUSIVE_SECONDS),
        "canary_evidence_sha256": None,
    }
    if receipt != expected_receipt:
        raise KernelBenchMetaCanaryError("authorization receipt binding differs")
    replay = verify_operation_journal(
        root / "journal" / "operation_ledger.jsonl",
        anchor_path=root / "trusted-head.json",
    )
    cases = plan.get("cases")
    if (
        set(plan)
        != {
            "schema_version",
            "plan_id",
            "repository_commit",
            "task_hashes",
            "candidate_policy_sha256",
            "cell_id",
            "evaluator_transaction_cap",
            "gpu_exclusive_seconds_cap",
            "cases",
        }
        or plan.get("schema_version") != 1
        or plan.get("plan_id") != "hb-gen1-kernelbench-meta-canary-v1"
        or plan.get("repository_commit") != KERNELBENCH_META_REPOSITORY_COMMIT
        or plan.get("task_hashes") != dict(KERNELBENCH_META_TASK_HASHES)
        or plan.get("candidate_policy_sha256")
        != RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256
        or plan.get("cell_id") != CANARY_CELL_ID
        or plan.get("evaluator_transaction_cap")
        != CANARY_EVALUATOR_TRANSACTIONS
        or plan.get("gpu_exclusive_seconds_cap")
        != CANARY_GPU_EXCLUSIVE_SECONDS
        or not isinstance(cases, list)
        or len(cases) != CANARY_EVALUATOR_TRANSACTIONS
    ):
        raise KernelBenchMetaCanaryError("independent canary case count differs")
    if [case.get("canary_id") for case in cases] != list(
        KERNELBENCH_META_CANARY_TASKS
    ):
        raise KernelBenchMetaCanaryError("independent canary order differs")
    plan_root = Path(canary_plan).parent.parent
    for ordinal, case in enumerate(cases, start=1):
        if (
            not isinstance(case, dict)
            or set(case) != _CANARY_CASE_KEYS
            or case.get("ordinal") != ordinal
            or case.get("task_id")
            != KERNELBENCH_META_CANARY_TASKS[case["canary_id"]]
            or case.get("task_sha256")
            != KERNELBENCH_META_TASK_HASHES[case["task_id"]]
            or case.get("candidate_policy_sha256")
            != RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256
            or case.get("expected_stage") != _EXPECTED_STAGE[case["canary_id"]]
            or case.get("expected_status") != _EXPECTED_STATUS[case["canary_id"]]
            or case.get("candidate_object")
            != f"candidates/objects/{case['candidate_sha256']}.py"
        ):
            raise KernelBenchMetaCanaryError("independent canary binding differs")
        candidate = plan_root / case["candidate_object"]
        try:
            candidate_metadata = candidate.lstat()
        except OSError as exc:
            raise KernelBenchMetaCanaryError(
                "independent candidate object differs"
            ) from exc
        if stat.S_ISLNK(candidate_metadata.st_mode) or not stat.S_ISREG(
            candidate_metadata.st_mode
        ):
            raise KernelBenchMetaCanaryError("independent candidate object differs")
        candidate_raw = candidate.read_bytes()
        if hashlib.sha256(candidate_raw).hexdigest() != case["candidate_sha256"]:
            raise KernelBenchMetaCanaryError("independent candidate object differs")
        try:
            RestrictedKernelCandidatePolicy().validate(
                candidate_raw, task_id=case["task_id"]
            )
        except RestrictedKernelCandidateError as exc:
            observed_policy = "rejected"
            observed_reason: str | None = " ".join(str(exc).split())[:500]
        else:
            observed_policy = "accepted"
            observed_reason = None
            formal = KernelBenchSolutionCodec(task_id=case["task_id"]).parse(
                f"```python\n{candidate_raw.decode('utf-8')}```\n"
            )
            if formal.sha256 != case["candidate_sha256"]:
                raise KernelBenchMetaCanaryError("independent formal codec differs")
        if (
            observed_policy != case["policy_state"]
            or observed_reason != case["policy_reason"]
            or (case["expected_stage"] == "policy_preflight")
            != (observed_policy == "rejected")
        ):
            raise KernelBenchMetaCanaryError("independent policy projection differs")
    if len(replay.operations) != CANARY_EVALUATOR_TRANSACTIONS:
        raise KernelBenchMetaCanaryError("independent journal operation count differs")
    results: list[dict[str, Any]] = []
    gpu_total = 0.0
    for case in cases:
        operation_id = _case_operation_id(case)
        operation = replay.operations.get(operation_id)
        if operation is None or operation.state != "completed":
            raise KernelBenchMetaCanaryError("canary operation is not completed")
        if operation.reservation != ResourceVector(
            evaluator_transactions=1,
            gpu_exclusive_seconds=CANARY_OPERATION_GPU_SECONDS,
        ):
            raise KernelBenchMetaCanaryError("canary reservation differs")
        terminal = operation.event_for("operation_completed")
        artifact_sha = terminal.payload["artifact_sha256"]
        if not isinstance(artifact_sha, str) or not _SHA256.fullmatch(artifact_sha):
            raise KernelBenchMetaCanaryError("canary terminal artifact is missing")
        artifact_path = root / "results" / "objects" / f"{artifact_sha}.json"
        artifact, artifact_raw = _load_canonical_object(
            artifact_path, label="independent canary result"
        )
        if hashlib.sha256(artifact_raw).hexdigest() != artifact_sha:
            raise KernelBenchMetaCanaryError("canary result digest differs")
        observed = artifact.get("observed")
        expected_bindings = {
            "operation_id": operation_id,
            "canary_id": case["canary_id"],
            "ordinal": case["ordinal"],
            "task_id": case["task_id"],
            "task_sha256": case["task_sha256"],
            "candidate_sha256": case["candidate_sha256"],
            "candidate_policy_sha256": case["candidate_policy_sha256"],
            "expected_stage": case["expected_stage"],
            "expected_status": case["expected_status"],
            "code_revision": code_revision,
            "staging_plan_sha256": staging_plan_sha256,
            "canary_plan_sha256": plan_sha,
            "authorization_receipt_sha256": receipt_sha,
            "scorer_bundle_sha256": scorer_bundle_sha256,
            "protocol_sha256": KERNELBENCH_META_PROTOCOL_SHA256,
        }
        if (
            set(artifact) != _RESULT_ARTIFACT_KEYS
            or artifact.get("schema_version") != 1
            or artifact.get("artifact_kind")
            != "hb-gen1-kernelbench-meta-canary-result-v1"
            or any(artifact.get(key) != value for key, value in expected_bindings.items())
            or not isinstance(observed, dict)
            or set(observed) != _PUBLIC_EVALUATION_KEYS
            or observed.get("status") != case["expected_status"]
            or type(observed.get("correct")) is not bool
            or type(observed.get("compiled")) is not bool
        ):
            raise KernelBenchMetaCanaryError("canary result semantic binding differs")
        expected_counts = _EXPECTED_PROTOCOL_COUNTS[case["canary_id"]]
        observed_counts = (
            observed["correctness_passed"],
            observed["timing_trials_completed"],
            observed["timing_outputs_correct"],
        )
        if observed_counts != expected_counts or any(
            type(value) is not int for value in observed_counts
        ):
            raise KernelBenchMetaCanaryError("canary protocol counts differ")
        if case["expected_status"] == EvaluationStatus.VALID.value:
            if not observed["correct"] or not observed["compiled"]:
                raise KernelBenchMetaCanaryError("reference canary did not pass")
            if any(
                type(observed[key]) not in (int, float)
                or not math.isfinite(float(observed[key]))
                or float(observed[key]) <= 0
                for key in (
                    "candidate_runtime_ms",
                    "reference_runtime_ms",
                    "speedup",
                )
            ):
                raise KernelBenchMetaCanaryError("reference timing is invalid")
        elif observed["correct"]:
            raise KernelBenchMetaCanaryError("adversarial canary was accepted")
        elif case["expected_status"] == EvaluationStatus.INCORRECT.value and not observed[
            "compiled"
        ]:
            raise KernelBenchMetaCanaryError("incorrect canary did not compile")
        if case["expected_stage"] == "policy_preflight" and (
            observed["compiled"] or observed["gpu_exclusive_seconds"] != 0.0
        ):
            raise KernelBenchMetaCanaryError("static canary crossed the GPU boundary")
        private_sha = artifact["private_evidence_sha256"]
        if private_sha is not None and (
            not isinstance(private_sha, str) or not _SHA256.fullmatch(private_sha)
        ):
            raise KernelBenchMetaCanaryError("private evidence digest is invalid")
        observed_gpu = observed["gpu_exclusive_seconds"]
        if (
            type(observed_gpu) not in (int, float)
            or not math.isfinite(float(observed_gpu))
            or not 0 <= float(observed_gpu) <= CANARY_OPERATION_GPU_SECONDS
        ):
            raise KernelBenchMetaCanaryError("observed GPU usage is invalid")
        usage = operation.committed_usage
        if (
            usage.evaluator_transactions != 1
            or usage.gpu_exclusive_seconds
            != float(observed_gpu)
        ):
            raise KernelBenchMetaCanaryError("canary usage binding differs")
        gpu_total += usage.gpu_exclusive_seconds
        results.append(
            {
                "ordinal": case["ordinal"],
                "canary_id": case["canary_id"],
                "status": observed["status"],
                "result_artifact_sha256": artifact_sha,
                "terminal_event_sha256": terminal.event_sha256,
            }
        )
    if gpu_total > CANARY_GPU_EXCLUSIVE_SECONDS:
        raise KernelBenchMetaCanaryError("canary GPU cap is exceeded")
    evidence = {
        "schema_version": 1,
        "evidence_type": "hb-gen1-kernelbench-meta-canary-evidence-v1",
        "status": "passed",
        "formal_activation_minted": False,
        "code_revision": code_revision,
        "staging_plan_sha256": staging_plan_sha256,
        "canary_plan_sha256": plan_sha,
        "authorization_receipt_sha256": receipt_sha,
        "scorer_bundle_sha256": scorer_bundle_sha256,
        "protocol_sha256": KERNELBENCH_META_PROTOCOL_SHA256,
        "repository_commit": KERNELBENCH_META_REPOSITORY_COMMIT,
        "task_set_sha256": KERNELBENCH_META_TASK_SET_SHA256,
        "journal_event_count": replay.event_count,
        "journal_head_sha256": replay.head_sha256,
        "evaluator_transactions": CANARY_EVALUATOR_TRANSACTIONS,
        "gpu_exclusive_seconds": gpu_total,
        "results": results,
    }
    evidence_raw = _canonical_bytes(evidence)
    evidence_sha = hashlib.sha256(evidence_raw).hexdigest()
    evidence_path = root / "evidence" / f"{evidence_sha}.json"
    _write_once(evidence_path, evidence_raw, mode=0o600)
    return VerifiedKernelBenchMetaCanary(
        evidence_path=evidence_path,
        evidence_sha256=evidence_sha,
        payload=evidence,
    )


__all__ = [
    "CANARY_CELL_ID",
    "CANARY_EVALUATOR_TRANSACTIONS",
    "CANARY_GPU_EXCLUSIVE_SECONDS",
    "CANARY_OPERATION_GPU_SECONDS",
    "KernelBenchMetaCanaryController",
    "KernelBenchMetaCanaryError",
    "KernelBenchMetaCanaryEvaluator",
    "PreparedKernelBenchMetaCanary",
    "VerifiedKernelBenchMetaCanary",
    "adversarial_candidate",
    "prepare_kernelbench_meta_canary",
    "reference_candidate_from_task_source",
    "verify_kernelbench_meta_canary",
]
