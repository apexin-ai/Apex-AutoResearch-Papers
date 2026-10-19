from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from dataclasses import asdict
from pathlib import Path
from typing import Any

from optimization_lab.generation import GenerationResult

from .events import (
    OperationJournal,
    OperationStateError,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
    verify_operation_journal,
)
from .model_gateway import (
    TRUSTED_CAPABILITY_HOLDER,
    IsolatedModelGateway,
    TransportFactory,
)
from .prepare import _SOURCES
from .runtime import parse_harness_decision
from .schema import HarnessDecision


FROZEN_MODEL = "gpt-5.6-sol"
FROZEN_REASONING_EFFORT = "high"
FROZEN_CLIENT_VERSION = "codex-cli-0.144.6"
FROZEN_TRANSPORT = "codex-exec-chatgpt-login"
FROZEN_PROVIDER = "codex_chatgpt"
CANARY_CELL_ID = "canary:model-route"
_COMMIT = re.compile(r"[0-9a-f]{40}")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_USAGE_FIELDS = {
    "cached_input_tokens",
    "input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
}


EXPECTED_HARNESS_DECISION = HarnessDecision.from_dict(
    {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["task_analyst", "generator", "verifier"],
        "memory_views": ["current"],
        "tools": ["task_semantics", "static_structure"],
        "parent_strategy": "reference",
        "workflow": ["analyze", "generate", "verify_contract"],
        "scheduler_mode": "single_candidate",
        "recovery_mode": "repair_then_reset",
        "kernel_directive": (
            "Generate one bounded candidate only after restating the public contract."
        ),
    }
)
_EXPECTED_DECISION_DICT = asdict(EXPECTED_HARNESS_DECISION)
_EXPECTED_DECISION_JSON = json.dumps(
    _EXPECTED_DECISION_DICT,
    ensure_ascii=False,
    allow_nan=False,
    sort_keys=True,
    separators=(",", ":"),
)
MODEL_ROUTE_CANARY_PROMPT = (
    "HB-GEN-1 model-route canary v1. Return exactly one bare strict JSON object "
    "and no prose or Markdown. The parsed HarnessDecision must equal this object:"
    "\n" + _EXPECTED_DECISION_JSON
)
FROZEN_PROMPT_SHA256 = hashlib.sha256(
    MODEL_ROUTE_CANARY_PROMPT.encode("utf-8")
).hexdigest()
EXPECTED_DECISION_SHA256 = hashlib.sha256(
    _EXPECTED_DECISION_JSON.encode("utf-8")
).hexdigest()


class ModelRouteCanaryBlocked(RuntimeError):
    """The frozen route, staging binding, recovery state, or budget is invalid."""


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _write_once(path: Path, content: bytes) -> None:
    if path.exists():
        if path.read_bytes() != content:
            raise ModelRouteCanaryBlocked(
                f"refusing to overwrite different model-route artifact: {path.name}"
            )
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".model-route.tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _resource_caps(payload: Any, label: str) -> ResourceCaps:
    try:
        vector = ResourceVector.from_dict(payload)
    except Exception as exc:
        raise ModelRouteCanaryBlocked(f"invalid {label}") from exc
    return ResourceCaps(**vector.to_dict())


def _legacy_canary_receipts(
    roots: tuple[Path, ...], *, current_code_revision: str
) -> tuple[dict[str, Any], ...]:
    """Verify obsolete v0 canaries for charging only, never for reuse."""

    receipts: dict[str, dict[str, Any]] = {}
    for raw_root in roots:
        root = Path(raw_root).resolve()
        staging_path = root / "staging_plan.json"
        summary_path = root / "model-canary" / "summary.json"
        ledger_path = root / "model-canary" / "journal" / "operation_ledger.jsonl"
        anchor_path = root / "model-canary" / "trusted-head.json"
        if not all(path.is_file() for path in (staging_path, summary_path, ledger_path, anchor_path)):
            raise ModelRouteCanaryBlocked("obsolete model canary segment is incomplete")
        try:
            staging = json.loads(staging_path.read_text(encoding="utf-8"))
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ModelRouteCanaryBlocked("obsolete model canary metadata is invalid") from exc
        replay = verify_operation_journal(ledger_path, anchor_path=anchor_path)
        operation_id = summary.get("operation_id") if isinstance(summary, dict) else None
        operation = replay.operations.get(operation_id) if isinstance(operation_id, str) else None
        code_revision = staging.get("code_revision") if isinstance(staging, dict) else None
        model_signature = staging.get("model_signature") if isinstance(staging, dict) else None
        expected_staging_signature = {
            "executor_model": FROZEN_MODEL,
            "reasoning_effort": FROZEN_REASONING_EFFORT,
            "transport": FROZEN_TRANSPORT,
            "client_version": FROZEN_CLIENT_VERSION,
        }
        if (
            not isinstance(summary, dict)
            or not isinstance(code_revision, str)
            or _COMMIT.fullmatch(code_revision) is None
            or model_signature != expected_staging_signature
            or summary.get("status") != "passed"
            or summary.get("model") != FROZEN_MODEL
            or summary.get("reasoning_effort") != FROZEN_REASONING_EFFORT
            or summary.get("client_version") != FROZEN_CLIENT_VERSION
            or summary.get("provider") != FROZEN_PROVIDER
            or operation is None
            or operation.cell_id != CANARY_CELL_ID
            or operation.operation_kind != "planner_call"
            or operation.state != "completed"
            or operation.committed_usage.model_calls != 1
            or replay.event_count != summary.get("operation_event_count")
            or replay.head_sha256 != summary.get("operation_journal_head_sha256")
            or operation.event_for("operation_completed").payload["artifact_sha256"]
            != summary.get("result_artifact_sha256")
        ):
            raise ModelRouteCanaryBlocked("obsolete model canary receipt differs")
        summary_sha = _sha256(summary_path)
        receipts[summary_sha] = {
            "schema_version": 1,
            "code_revision": code_revision,
            "staging_plan_sha256": _sha256(staging_path),
            "summary_sha256": summary_sha,
            "operation_journal_head_sha256": replay.head_sha256,
            "model_calls": 1,
            "same_code_revision": code_revision == current_code_revision,
            "reusable": False,
        }
    return tuple(receipts[key] for key in sorted(receipts))


class ModelRouteCanaryRunner:
    """Run or recover one signed HB-GEN-1 model-route sentinel.

    Every staging/code/prompt signature gets a content-addressed segment.  All
    segments share one operation journal, so an obsolete segment remains
    auditable and continues to consume its non-transferable canary entitlement.
    """

    def __init__(
        self,
        *,
        project_root: Path,
        artifact_root: Path,
        observed_code_revision: str,
        observed_client_version: str,
        transport_factory: TransportFactory,
        signing_key: bytes,
        prior_canary_artifact_roots: tuple[Path, ...] = (),
    ) -> None:
        self.project_root = Path(project_root).resolve()
        self.artifact_root = Path(artifact_root).resolve()
        self.staging_path = self.artifact_root / "staging_plan.json"
        if not self.staging_path.is_file():
            raise ModelRouteCanaryBlocked("staging plan is missing")
        self.staging_bytes = self.staging_path.read_bytes()
        self.staging_plan_sha256 = hashlib.sha256(self.staging_bytes).hexdigest()
        try:
            staging = json.loads(self.staging_bytes)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ModelRouteCanaryBlocked("staging plan is invalid") from exc
        if not isinstance(staging, dict):
            raise ModelRouteCanaryBlocked("staging plan must be an object")
        self.staging = staging
        self._validate_staging(
            observed_code_revision=observed_code_revision,
            observed_client_version=observed_client_version,
        )
        self.code_revision = observed_code_revision
        self.prompt = MODEL_ROUTE_CANARY_PROMPT
        self.prompt_sha256 = FROZEN_PROMPT_SHA256
        self.model_signature = {
            "model": FROZEN_MODEL,
            "reasoning_effort": FROZEN_REASONING_EFFORT,
            "client_version": FROZEN_CLIENT_VERSION,
            "transport": FROZEN_TRANSPORT,
            "provider": FROZEN_PROVIDER,
        }
        self.prior_canary_receipts = _legacy_canary_receipts(
            tuple(prior_canary_artifact_roots),
            current_code_revision=self.code_revision,
        )
        self.prior_model_calls = sum(
            receipt["model_calls"] for receipt in self.prior_canary_receipts
        )
        binding_core = {
            "schema_version": 1,
            "phase_id": staging["phase_id"],
            "code_revision": self.code_revision,
            "staging_plan_sha256": self.staging_plan_sha256,
            "source_hashes": staging["source_hashes"],
            "prompt_sha256": self.prompt_sha256,
            "expected_decision_sha256": EXPECTED_DECISION_SHA256,
            "model_signature": self.model_signature,
            "prior_canary_segments": list(self.prior_canary_receipts),
        }
        self.segment_id = hashlib.sha256(_canonical_bytes(binding_core)).hexdigest()
        self.binding = {**binding_core, "segment_id": self.segment_id}
        self.canary_root = self.artifact_root / "model-route-canary"
        self.segment_root = self.canary_root / "segments" / f"segment-{self.segment_id}"
        self.binding_path = self.segment_root / "binding.json"
        self.result_path = self.segment_root / "result.json"
        _write_once(self.binding_path, _canonical_bytes(self.binding))
        self.operation_id = f"canary:model-route:{self.segment_id}"
        frozen_canary_caps = _resource_caps(
            staging["cell_entitlements"][CANARY_CELL_ID],
            "model-route canary entitlement",
        )
        if self.prior_model_calls > frozen_canary_caps.model_calls:
            raise ModelRouteCanaryBlocked(
                "obsolete model canaries exceed the frozen entitlement"
            )
        canary_caps = ResourceCaps(
            model_calls=frozen_canary_caps.model_calls - self.prior_model_calls
        )
        self.frozen_canary_model_call_entitlement = frozen_canary_caps.model_calls
        self.governor = ResourceGovernor(
            journal=OperationJournal(
                self.canary_root / "journal",
                anchor_path=self.canary_root / "trusted-head.json",
            ),
            global_caps=canary_caps,
            cell_caps={CANARY_CELL_ID: canary_caps},
        )
        self.gateway = IsolatedModelGateway(
            artifact_root=self.canary_root / "gateway",
            governor=self.governor,
            transport_factory=transport_factory,
            signing_key=signing_key,
        )

    def _validate_staging(
        self, *, observed_code_revision: str, observed_client_version: str
    ) -> None:
        if (
            not isinstance(observed_code_revision, str)
            or _COMMIT.fullmatch(observed_code_revision) is None
            or self.staging.get("code_revision") != observed_code_revision
        ):
            raise ModelRouteCanaryBlocked(
                "clean full code revision differs from the staging plan"
            )
        expected_signature = {
            "executor_model": FROZEN_MODEL,
            "reasoning_effort": FROZEN_REASONING_EFFORT,
            "transport": FROZEN_TRANSPORT,
            "client_version": FROZEN_CLIENT_VERSION,
        }
        if (
            observed_client_version != FROZEN_CLIENT_VERSION
            or self.staging.get("model_signature") != expected_signature
        ):
            raise ModelRouteCanaryBlocked("frozen model signature differs")
        source_hashes = self.staging.get("source_hashes")
        if not isinstance(source_hashes, dict) or set(source_hashes) != set(_SOURCES):
            raise ModelRouteCanaryBlocked("staging source hash set differs")
        for source_id, relative in _SOURCES.items():
            path = self.project_root / relative
            if (
                not path.is_file()
                or not isinstance(source_hashes[source_id], str)
                or _SHA256.fullmatch(source_hashes[source_id]) is None
                or _sha256(path) != source_hashes[source_id]
            ):
                raise ModelRouteCanaryBlocked(
                    f"staging source hash differs: {source_id}"
                )
        entitlements = self.staging.get("cell_entitlements")
        expected_canary = {
            "model_calls": 2,
            "evaluator_transactions": 0,
            "gpu_exclusive_seconds": 0.0,
            "cpu_evaluator_seconds": 0.0,
        }
        if (
            not isinstance(entitlements, dict)
            or entitlements.get(CANARY_CELL_ID) != expected_canary
        ):
            raise ModelRouteCanaryBlocked(
                "model-route canary entitlement differs from the frozen plan"
            )

    def _gateway_result_path(self) -> Path:
        digest = hashlib.sha256(self.operation_id.encode("utf-8")).hexdigest()
        return self.gateway.operations_root / f"op-{digest}" / "result.json"

    def _load_stored_result(self) -> dict[str, Any]:
        try:
            stored = json.loads(self.result_path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ModelRouteCanaryBlocked("stored canary result is invalid") from exc
        expected = self._result_from_gateway(
            self.gateway.replay_completed(
                operation_id=self.operation_id,
                expected_prompt_sha256=self.prompt_sha256,
            )
        )
        if stored != expected or self.result_path.read_bytes() != _canonical_bytes(expected):
            raise ModelRouteCanaryBlocked("stored canary result differs from trusted replay")
        return stored

    def _recover_started_gateway_artifact(self) -> GenerationResult:
        path = self._gateway_result_path()
        if not path.is_file():
            raise ModelRouteCanaryBlocked(
                "started model-route operation without artifact is abandoned"
            )
        encoded = path.read_bytes()
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ModelRouteCanaryBlocked("started gateway artifact is invalid") from exc
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
            or payload["schema_version"] != 1
            or payload["operation_id"] != self.operation_id
            or payload["cell_id"] != CANARY_CELL_ID
            or payload["operation_kind"] != "planner_call"
            or payload["prompt_sha256"] != self.prompt_sha256
            or payload["model"] != FROZEN_MODEL
            or payload["output_mode"] != "plain_text"
        ):
            raise ModelRouteCanaryBlocked("started gateway artifact binding differs")
        artifact_sha = hashlib.sha256(encoded).hexdigest()
        self.governor.complete(
            self.operation_id,
            actual_usage=ResourceVector(model_calls=1),
            artifact_sha256=artifact_sha,
        )
        return self.gateway.replay_completed(
            operation_id=self.operation_id,
            expected_prompt_sha256=self.prompt_sha256,
        )

    def _result_from_gateway(self, generated: GenerationResult) -> dict[str, Any]:
        decision: HarnessDecision | None = None
        reason_code: str | None = None
        if generated.provider != FROZEN_PROVIDER:
            reason_code = "provider_drift"
        elif (
            set(generated.usage) != _USAGE_FIELDS
            or any(
                isinstance(value, bool) or not isinstance(value, int) or value < 0
                for value in generated.usage.values()
            )
            or generated.usage["input_tokens"] <= 0
            or generated.usage["output_tokens"] <= 0
        ):
            reason_code = "usage_drift"
        else:
            try:
                decision = parse_harness_decision(generated.raw_response)
            except ValueError:
                reason_code = "harness_decision_structure_drift"
            else:
                if decision != EXPECTED_HARNESS_DECISION:
                    reason_code = "harness_decision_mismatch"
        replay = self.governor.journal.replay()
        operation = replay.operations.get(self.operation_id)
        if operation is None or operation.state != "completed":
            raise ModelRouteCanaryBlocked("model-route operation is not completed")
        terminal = operation.event_for("operation_completed")
        return {
            "schema_version": 1,
            "status": "passed" if reason_code is None else "failed",
            "reason_code": reason_code,
            "segment_id": self.segment_id,
            "operation_id": self.operation_id,
            "operation_state": operation.state,
            "operation_terminal_sequence": terminal.sequence,
            "operation_terminal_event_sha256": terminal.event_sha256,
            "gateway_result_artifact_sha256": terminal.payload["artifact_sha256"],
            "staging_plan_sha256": self.staging_plan_sha256,
            "source_hashes": self.staging["source_hashes"],
            "code_revision": self.code_revision,
            "prompt_sha256": self.prompt_sha256,
            "expected_decision_sha256": EXPECTED_DECISION_SHA256,
            "decision": (
                None
                if decision is None
                else json.loads(
                    json.dumps(
                        asdict(decision),
                        ensure_ascii=False,
                        allow_nan=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    )
                )
            ),
            "model_signature": self.model_signature,
            "provider": generated.provider,
            "usage": generated.usage,
            "api_cost_usd": generated.api_cost_usd,
        }

    def preflight(self) -> dict[str, Any]:
        replay = self.governor.journal.replay()
        snapshot = self.governor.snapshot()
        current_used = snapshot.cell_committed[CANARY_CELL_ID].model_calls
        used = self.prior_model_calls + current_used
        cap = self.frozen_canary_model_call_entitlement
        remaining = cap - used
        blockers: list[str] = []
        operation = replay.operations.get(self.operation_id)
        terminal_result: dict[str, Any] | None = None
        if self.result_path.exists():
            terminal_result = self._load_stored_result()
            if terminal_result["status"] != "passed":
                blockers.append(terminal_result["reason_code"])
        elif operation is None:
            if remaining < 1:
                blockers.append("model_route_canary_call_entitlement_exhausted")
        elif operation.state == "started":
            if not self._gateway_result_path().is_file():
                blockers.append("started_without_artifact_is_abandoned")
        elif operation.state == "failed":
            blockers.append("model_route_operation_failed_terminally")
        elif operation.state == "completed":
            try:
                self.gateway.replay_completed(
                    operation_id=self.operation_id,
                    expected_prompt_sha256=self.prompt_sha256,
                )
            except OperationStateError:
                blockers.append("completed_gateway_artifact_invalid")
        return {
            "schema_version": 1,
            "status": (
                terminal_result["status"]
                if terminal_result is not None
                else ("blocked" if blockers else "ready")
            ),
            "blockers": blockers,
            "segment_id": self.segment_id,
            "operation_id": self.operation_id,
            "code_revision": self.code_revision,
            "staging_plan_sha256": self.staging_plan_sha256,
            "source_hashes": self.staging["source_hashes"],
            "prompt_sha256": self.prompt_sha256,
            "expected_decision_sha256": EXPECTED_DECISION_SHA256,
            "model_signature": self.model_signature,
            "canary_model_call_entitlement": cap,
            "prior_segment_model_calls": self.prior_model_calls,
            "committed_model_calls": used,
            "remaining_model_calls": remaining,
            "operation_state": None if operation is None else operation.state,
            "result_path": str(self.result_path),
        }

    def execute(self) -> dict[str, Any]:
        if self.result_path.exists():
            return self._load_stored_result()
        report = self.preflight()
        if report["blockers"]:
            blockers = ", ".join(report["blockers"])
            if "started_without_artifact_is_abandoned" in report["blockers"]:
                raise ModelRouteCanaryBlocked(
                    "started model-route operation is abandoned and cannot be resent"
                )
            raise ModelRouteCanaryBlocked(blockers)
        operation = self.governor.journal.replay().operations.get(self.operation_id)
        if operation is not None and operation.state == "completed":
            generated = self.gateway.replay_completed(
                operation_id=self.operation_id,
                expected_prompt_sha256=self.prompt_sha256,
            )
        elif operation is not None and operation.state == "started":
            generated = self._recover_started_gateway_artifact()
        else:
            capability = self.gateway.issue_capability(
                holder=TRUSTED_CAPABILITY_HOLDER,
                operation_id=self.operation_id,
                cell_id=CANARY_CELL_ID,
                operation_kind="planner_call",
                prompt=self.prompt,
                model=FROZEN_MODEL,
                output_mode="plain_text",
            )
            generated = self.gateway.invoke(
                capability,
                prompt=self.prompt,
                presented_by=TRUSTED_CAPABILITY_HOLDER,
            )
        result = self._result_from_gateway(generated)
        _write_once(self.result_path, _canonical_bytes(result))
        return result


__all__ = [
    "CANARY_CELL_ID",
    "EXPECTED_DECISION_SHA256",
    "EXPECTED_HARNESS_DECISION",
    "FROZEN_CLIENT_VERSION",
    "FROZEN_MODEL",
    "FROZEN_PROMPT_SHA256",
    "FROZEN_PROVIDER",
    "FROZEN_REASONING_EFFORT",
    "FROZEN_TRANSPORT",
    "MODEL_ROUTE_CANARY_PROMPT",
    "ModelRouteCanaryBlocked",
    "ModelRouteCanaryRunner",
]
