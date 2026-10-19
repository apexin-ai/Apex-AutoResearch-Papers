from __future__ import annotations

import hashlib
import hmac
import json
import os
import secrets
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from optimization_lab.generation import CandidateGenerator, GenerationResult

from .events import (
    OperationStateError,
    ResourceGovernor,
    ResourceVector,
)


TRUSTED_CAPABILITY_HOLDER = "trusted_controller"
_OUTPUT_MODES = {"plain_text", "python_candidate"}
_OPERATION_KINDS = {
    "planner_call",
    "sham_planner_call",
    "solution_call",
    "distillation_call",
}


class CapabilityError(RuntimeError):
    """A one-shot model capability was forged, rebound, or reused."""


@dataclass(frozen=True)
class ModelCapability:
    holder: str
    operation_id: str
    cell_id: str
    operation_kind: str
    prompt_sha256: str
    model: str
    output_mode: str
    nonce: str
    signature: str

    def binding(self) -> dict[str, str]:
        return {
            "holder": self.holder,
            "operation_id": self.operation_id,
            "cell_id": self.cell_id,
            "operation_kind": self.operation_kind,
            "prompt_sha256": self.prompt_sha256,
            "model": self.model,
            "output_mode": self.output_mode,
            "nonce": self.nonce,
        }


TransportFactory = Callable[[Path, str], CandidateGenerator]


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _write_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".model-gateway.tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise


class IsolatedModelGateway:
    """Trusted holder of one-shot model capabilities.

    Capability bytes never enter a prompt, transport environment, artifact, or
    journal. The untrusted planner/solution model receives only the prompt.
    """

    def __init__(
        self,
        *,
        artifact_root: Path,
        governor: ResourceGovernor,
        transport_factory: TransportFactory,
        signing_key: bytes,
    ) -> None:
        if not isinstance(signing_key, bytes) or len(signing_key) < 32:
            raise ValueError("model capability signing key must contain at least 32 bytes")
        self.artifact_root = artifact_root.resolve()
        self.operations_root = self.artifact_root / "operations"
        self.operations_root.mkdir(parents=True, exist_ok=True)
        self.governor = governor
        self.transport_factory = transport_factory
        self._signing_key = signing_key
        self._used_signatures: set[str] = set()

    def issue_capability(
        self,
        *,
        holder: str,
        operation_id: str,
        cell_id: str,
        operation_kind: str,
        prompt: str,
        model: str,
        output_mode: str,
    ) -> ModelCapability:
        if holder != TRUSTED_CAPABILITY_HOLDER:
            raise CapabilityError("only the trusted controller may hold model capabilities")
        if operation_kind not in _OPERATION_KINDS:
            raise CapabilityError("model operation kind is not allowlisted")
        if output_mode not in _OUTPUT_MODES:
            raise CapabilityError("model output mode is not allowlisted")
        if not isinstance(prompt, str) or not prompt.strip() or not model.strip():
            raise CapabilityError("model prompt and model are required")
        nonce = secrets.token_hex(16)
        binding = {
            "holder": holder,
            "operation_id": operation_id,
            "cell_id": cell_id,
            "operation_kind": operation_kind,
            "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            "model": model,
            "output_mode": output_mode,
            "nonce": nonce,
        }
        signature = hmac.new(
            self._signing_key, _canonical_bytes(binding), hashlib.sha256
        ).hexdigest()
        return ModelCapability(**binding, signature=signature)

    def _verify(
        self,
        capability: ModelCapability,
        *,
        prompt: str,
        presented_by: str,
    ) -> None:
        if capability.holder != TRUSTED_CAPABILITY_HOLDER or presented_by != capability.holder:
            raise CapabilityError("model capability holder does not match")
        expected = hmac.new(
            self._signing_key,
            _canonical_bytes(capability.binding()),
            hashlib.sha256,
        ).hexdigest()
        if not hmac.compare_digest(expected, capability.signature):
            raise CapabilityError("model capability signature is invalid")
        prompt_sha = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        if prompt_sha != capability.prompt_sha256:
            raise CapabilityError("model capability prompt binding does not match")
        if capability.signature in self._used_signatures:
            raise CapabilityError("model capability was already used")

    def _operation_root(self, operation_id: str) -> Path:
        digest = hashlib.sha256(operation_id.encode("utf-8")).hexdigest()
        return self.operations_root / f"op-{digest}"

    def result_artifact_exists(self, operation_id: str) -> bool:
        """Return whether recovery has a persisted provider result to validate."""

        return (self._operation_root(operation_id) / "result.json").is_file()

    def invoke(
        self,
        capability: ModelCapability,
        *,
        prompt: str,
        presented_by: str,
    ) -> GenerationResult:
        self._verify(capability, prompt=prompt, presented_by=presented_by)
        self._used_signatures.add(capability.signature)

        replay = self.governor.journal.replay()
        existing = replay.operations.get(capability.operation_id)
        if existing is not None:
            if existing.state == "started":
                result_path = (
                    self._operation_root(capability.operation_id) / "result.json"
                )
                if not result_path.is_file():
                    raise OperationStateError(
                        "operation is abandoned; use a new explicit operation id rather than retry"
                    )
                result, artifact_sha = self._load_result_artifact(
                    operation_id=capability.operation_id,
                    expected_prompt_sha256=capability.prompt_sha256,
                    expected_cell_id=capability.cell_id,
                    expected_operation_kind=capability.operation_kind,
                    expected_model=capability.model,
                    expected_output_mode=capability.output_mode,
                )
                self.governor.complete(
                    capability.operation_id,
                    actual_usage=ResourceVector(model_calls=1),
                    artifact_sha256=artifact_sha,
                )
                return result
            if existing.state == "completed":
                return self.replay_completed(
                    operation_id=capability.operation_id,
                    expected_prompt_sha256=capability.prompt_sha256,
                    expected_cell_id=capability.cell_id,
                    expected_operation_kind=capability.operation_kind,
                    expected_model=capability.model,
                    expected_output_mode=capability.output_mode,
                )
            if existing.state == "failed":
                raise OperationStateError("failed model operation is terminal")
        else:
            self.governor.reserve(
                operation_id=capability.operation_id,
                cell_id=capability.cell_id,
                operation_kind=capability.operation_kind,
                reservation=ResourceVector(model_calls=1),
            )

        self.governor.start(capability.operation_id)
        operation_root = self._operation_root(capability.operation_id)
        operation_root.mkdir(parents=True, exist_ok=True)
        _write_atomic(operation_root / "prompt.txt", prompt.encode("utf-8"))
        try:
            transport = self.transport_factory(operation_root, capability.output_mode)
            result = transport.generate(prompt, model=capability.model)
            payload = {
                "schema_version": 1,
                "operation_id": capability.operation_id,
                "cell_id": capability.cell_id,
                "operation_kind": capability.operation_kind,
                "prompt_sha256": capability.prompt_sha256,
                "model": capability.model,
                "output_mode": capability.output_mode,
                "raw_response": result.raw_response,
                "api_cost_usd": result.api_cost_usd,
                "provider": result.provider,
                "usage": result.usage,
                "audit_log_name": self._audit_log_name(
                    result.audit_log_path, operation_root
                ),
            }
            encoded = _canonical_bytes(payload) + b"\n"
            artifact_sha = hashlib.sha256(encoded).hexdigest()
            _write_atomic(operation_root / "result.json", encoded)
            self.governor.complete(
                capability.operation_id,
                actual_usage=ResourceVector(model_calls=1),
                artifact_sha256=artifact_sha,
            )
            return result
        except Exception:
            self.governor.fail(
                capability.operation_id,
                reason_code="provider_or_transport_error",
            )
            raise

    @staticmethod
    def _audit_log_name(value: str, operation_root: Path) -> str:
        if not value:
            return ""
        try:
            path = Path(value).resolve()
        except OSError:
            return ""
        return path.name if path.is_relative_to(operation_root.resolve()) else ""

    def replay_completed(
        self,
        *,
        operation_id: str,
        expected_prompt_sha256: str,
        expected_cell_id: str | None = None,
        expected_operation_kind: str | None = None,
        expected_model: str | None = None,
        expected_output_mode: str | None = None,
    ) -> GenerationResult:
        operation = self.governor.journal.replay().operations.get(operation_id)
        if operation is None or operation.state != "completed":
            raise OperationStateError("model operation is not completed")
        result, artifact_sha = self._load_result_artifact(
            operation_id=operation_id,
            expected_prompt_sha256=expected_prompt_sha256,
            expected_cell_id=expected_cell_id or operation.cell_id,
            expected_operation_kind=expected_operation_kind or operation.operation_kind,
            expected_model=expected_model,
            expected_output_mode=expected_output_mode,
        )
        terminal_sha = operation.event_for("operation_completed").payload[
            "artifact_sha256"
        ]
        if artifact_sha != terminal_sha:
            raise OperationStateError("completed model operation artifact hash differs")
        return result

    def _load_result_artifact(
        self,
        *,
        operation_id: str,
        expected_prompt_sha256: str,
        expected_cell_id: str,
        expected_operation_kind: str,
        expected_model: str | None,
        expected_output_mode: str | None,
    ) -> tuple[GenerationResult, str]:
        result_path = self._operation_root(operation_id) / "result.json"
        if not result_path.is_file():
            raise OperationStateError("model operation result artifact is missing")
        encoded = result_path.read_bytes()
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise OperationStateError("model operation artifact is invalid") from exc
        expected_keys = {
            "schema_version",
            "operation_id",
            "cell_id",
            "operation_kind",
            "prompt_sha256",
            "model",
            "output_mode",
            "raw_response",
            "api_cost_usd",
            "provider",
            "usage",
            "audit_log_name",
        }
        if (
            not isinstance(payload, dict)
            or set(payload) != expected_keys
            or _canonical_bytes(payload) + b"\n" != encoded
        ):
            raise OperationStateError("completed model operation fields differ")
        if (
            payload["schema_version"] != 1
            or payload["operation_id"] != operation_id
            or payload["prompt_sha256"] != expected_prompt_sha256
            or payload["cell_id"] != expected_cell_id
            or payload["operation_kind"] != expected_operation_kind
            or (expected_model is not None and payload["model"] != expected_model)
            or (
                expected_output_mode is not None
                and payload["output_mode"] != expected_output_mode
            )
        ):
            raise OperationStateError("model operation binding differs")
        audit_name = payload["audit_log_name"]
        if not isinstance(audit_name, str) or Path(audit_name).name != audit_name:
            raise OperationStateError("model operation audit-log binding is invalid")
        audit_path = (
            str(self._operation_root(operation_id) / audit_name) if audit_name else ""
        )
        return (
            GenerationResult(
                raw_response=payload["raw_response"],
                api_cost_usd=payload["api_cost_usd"],
                provider=payload["provider"],
                usage=payload["usage"],
                audit_log_path=audit_path,
            ),
            hashlib.sha256(encoded).hexdigest(),
        )


class GatewayGenerator:
    """Bind one CandidateGenerator call to one trusted gateway operation."""

    def __init__(
        self,
        *,
        gateway: IsolatedModelGateway,
        operation_id: str,
        cell_id: str,
        operation_kind: str,
        output_mode: str,
    ) -> None:
        self.gateway = gateway
        self.operation_id = operation_id
        self.cell_id = cell_id
        self.operation_kind = operation_kind
        self.output_mode = output_mode

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        capability = self.gateway.issue_capability(
            holder=TRUSTED_CAPABILITY_HOLDER,
            operation_id=self.operation_id,
            cell_id=self.cell_id,
            operation_kind=self.operation_kind,
            prompt=prompt,
            model=model,
            output_mode=self.output_mode,
        )
        return self.gateway.invoke(
            capability,
            prompt=prompt,
            presented_by=TRUSTED_CAPABILITY_HOLDER,
        )
