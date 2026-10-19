"""Content-addressed, arm-independent v001 trunk contracts.

This module is deliberately a data/archival layer.  It does not call a model,
compile a Harness, submit a candidate, or invoke an evaluator.  A controller
must first seal one task/seed intent, prove that the canonical compilation and
all four arm projections are semantically identical, and only then seal the
common outcome and arm-specific fork references.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, fields, is_dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from ._safe_artifacts import (
    lexical_absolute,
    read_safe_regular_file,
    safe_regular_file_exists,
    write_once_safe_regular_file,
)
from .compile_receipts import HarnessCompileReceipt
from .operators import CompiledHarness, HarnessContext, TrustedOperatorRegistry
from .schema import HarnessDecision


ZERO_SHA256 = "0" * 64
FACTORIAL_ARMS = (
    "A-fixed-feedback",
    "S-reflection-skill",
    "B-targeted",
    "B-frozen-wide",
)
_ARM_ADAPTATION_POLICIES = {
    "A-fixed-feedback": "conditional_any_v1",
    "S-reflection-skill": "conditional_any_v1",
    "B-targeted": "targeted_any_change_v1",
    "B-frozen-wide": "wide_all_fields_recompile_v1",
}
TRUNK_STATUSES = (
    "SUCCESS",
    "SOLUTION_CONTRACT_REJECTED",
    "OPERATION_INTERRUPTED",
    "COMMON_TRUNK_FAILURE",
    "ENVIRONMENT_INVALID",
)

_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_UINT64_MAX = (1 << 64) - 1


def _canonical_bytes(payload: object) -> bytes:
    try:
        return (
            json.dumps(
                payload,
                allow_nan=False,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ValueError("factorial trunk payload is not canonical JSON") from exc


def _reject_constant(value: str) -> None:
    raise ValueError(f"factorial trunk JSON contains {value}")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"factorial trunk JSON repeats field {key!r}")
        result[key] = value
    return result


def _decode(encoded: bytes, *, label: str) -> Any:
    if not isinstance(encoded, bytes):
        raise TypeError(f"{label} must be bytes")
    try:
        payload = json.loads(
            encoded,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} JSON is invalid") from exc
    if _canonical_bytes(payload) != encoded:
        raise ValueError(f"{label} is not canonical")
    return payload


def _safe(value: str, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise ValueError(f"unsafe factorial trunk {label}")
    return value


def _sha(value: str, label: str, *, allow_zero: bool = True) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"invalid factorial trunk {label}")
    if not allow_zero and value == ZERO_SHA256:
        raise ValueError(f"empty factorial trunk {label}")
    return value


def _digest(payload: object) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _exact_fields(payload: Any, expected: set[str], label: str) -> dict[str, Any]:
    if not isinstance(payload, dict) or set(payload) != expected:
        raise ValueError(f"{label} fields differ")
    return payload


def _content_from_bytes(cls: type[Any], encoded: bytes, *, expected_sha256: str) -> Any:
    _sha(expected_sha256, "expected content sha256", allow_zero=False)
    payload = _decode(encoded, label=cls.__name__)
    expected = {field.name for field in fields(cls)} | {"schema_version"}
    _exact_fields(payload, expected, cls.__name__)
    if payload.pop("schema_version") != 1:
        raise ValueError(f"{cls.__name__} schema differs")
    item = cls(**payload)
    if item.canonical_bytes != encoded:
        raise ValueError(f"{cls.__name__} is not canonical")
    if item.sha256 != expected_sha256:
        raise ValueError(f"{cls.__name__} hash differs")
    return item


def _content_value(value: Any) -> Any:
    """Project frozen dataclasses and read-only mappings to canonical JSON values.

    ``dataclasses.asdict`` deep-copies every leaf and therefore cannot serialize
    ``MappingProxyType``.  Walking the values explicitly keeps receipt mappings
    immutable in memory without changing their stable JSON representation.
    """

    if is_dataclass(value) and not isinstance(value, type):
        return {
            field.name: _content_value(getattr(value, field.name))
            for field in fields(value)
        }
    if isinstance(value, Mapping):
        return {str(key): _content_value(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return tuple(_content_value(item) for item in value)
    if isinstance(value, list):
        return [_content_value(item) for item in value]
    return value


class _ContentAddressed:
    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            **{
                field.name: _content_value(getattr(self, field.name))
                for field in fields(self)
            },
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.core_payload())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class TaskSeedKey(_ContentAddressed):
    """Complete immutable identity of one shared-v001 experimental unit."""

    suite: str
    instance_id: str
    seed: int
    task_binding_sha256: str
    factorial_contract_sha256: str
    context_binding_sha256: str

    def __post_init__(self) -> None:
        _safe(self.suite, "suite")
        _safe(self.instance_id, "instance id")
        if type(self.seed) is not int or not 0 <= self.seed <= _UINT64_MAX:
            raise ValueError("factorial trunk seed must be uint64")
        _sha(self.task_binding_sha256, "task binding sha256", allow_zero=False)
        _sha(
            self.factorial_contract_sha256,
            "factorial contract sha256",
            allow_zero=False,
        )
        _sha(self.context_binding_sha256, "context binding sha256", allow_zero=False)

    def operation_id(self, operation: str) -> str:
        operation = _safe(operation, "operation stage")
        return f"factorial-v001:{self.sha256}:{operation}"

    def arm_cell_id(self, arm_id: str) -> str:
        if arm_id not in FACTORIAL_ARMS:
            raise ValueError("factorial trunk arm differs")
        return f"factorial-cell:{self.sha256}:{arm_id}"

    @classmethod
    def create(
        cls,
        *,
        context: HarnessContext,
        seed: int,
        task_binding_sha256: str,
        factorial_contract_sha256: str,
    ) -> "TaskSeedKey":
        """Create the key from the exact public v001 context and source binding.

        ``task_binding_sha256`` is the trusted nonzero digest of the frozen task
        source or task-manifest binding.  Keeping it explicit prevents a caller
        from treating the context hash alone as proof of source identity.
        """

        if not isinstance(context, HarnessContext):
            raise TypeError("Harness context is required")
        if context.round_index != 1:
            raise ValueError("factorial trunk TaskSeedKey requires a v001 context")
        _sha(task_binding_sha256, "task binding sha256", allow_zero=False)
        _sha(
            factorial_contract_sha256,
            "factorial contract sha256",
            allow_zero=False,
        )
        return cls(
            suite=context.suite,
            instance_id=context.instance_id,
            seed=seed,
            task_binding_sha256=task_binding_sha256,
            factorial_contract_sha256=factorial_contract_sha256,
            context_binding_sha256=(
                TrustedOperatorRegistry.context_binding_sha256(context)
            ),
        )

    def verify_against_context(
        self,
        *,
        context: HarnessContext,
        seed: int,
        task_binding_sha256: str,
        factorial_contract_sha256: str,
    ) -> None:
        """Revalidate a persisted key against its typed public inputs."""

        expected = type(self).create(
            context=context,
            seed=seed,
            task_binding_sha256=task_binding_sha256,
            factorial_contract_sha256=factorial_contract_sha256,
        )
        if self != expected:
            raise ValueError("factorial trunk task/seed context binding differs")

    @classmethod
    def from_bytes(cls, encoded: bytes, *, expected_sha256: str) -> "TaskSeedKey":
        return _content_from_bytes(cls, encoded, expected_sha256=expected_sha256)


def _compiled_semantic_projection(compiled: CompiledHarness) -> dict[str, Any]:
    if not isinstance(compiled, CompiledHarness):
        raise TypeError("compiled Harness is required")
    projection: dict[str, Any] = asdict(compiled)
    seen = {field.name for field in fields(compiled)}
    if "adaptation_policy" not in seen or "solution_prompt" not in seen:
        raise ValueError("CompiledHarness schema lacks canonical projection fields")
    prompt = projection.pop("solution_prompt")
    projection.pop("adaptation_policy")
    if not isinstance(prompt, str) or not prompt:
        raise ValueError("compiled Harness solution prompt is empty")
    projection["solution_prompt_sha256"] = hashlib.sha256(
        prompt.encode("utf-8")
    ).hexdigest()
    return projection


def compiled_harness_semantic_sha256(compiled: CompiledHarness) -> str:
    """Hash every CompiledHarness field except its arm policy label.

    The complete prompt participates through its SHA256 rather than by copying
    potentially large prompt text into receipts.  Adding a future dataclass
    field automatically adds it to this projection, preventing a stale manual
    allowlist from silently weakening equivalence.
    """

    return _digest(_compiled_semantic_projection(compiled))


def _compiled_semantic_evidence(compiled: CompiledHarness) -> str:
    """Return the complete canonical semantic projection carried by v001.

    This is audit evidence, not compiler provenance.  A formal orchestrator
    must still reload the canonical decision/context/variant/Registry and run
    the trusted compiler; an internally consistent projection can otherwise be
    replaced and fully rehashed by whoever controls the archive inputs.
    """

    return _canonical_bytes(_compiled_semantic_projection(compiled)).decode("utf-8")


def _decode_compiled_semantic_evidence(
    canonical_json: str,
    *,
    expected_sha256: str,
) -> dict[str, Any]:
    if (
        not isinstance(canonical_json, str)
        or not canonical_json
        or len(canonical_json) > 4_194_304
    ):
        raise ValueError("canonical compiled Harness semantic evidence differs")
    projection = _decode(
        canonical_json.encode("utf-8"),
        label="canonical compiled Harness semantic evidence",
    )
    expected_fields = {
        field.name for field in fields(CompiledHarness)
    } - {"adaptation_policy", "solution_prompt"}
    expected_fields.add("solution_prompt_sha256")
    _exact_fields(
        projection,
        expected_fields,
        "canonical compiled Harness semantic evidence",
    )
    if _digest(projection) != expected_sha256:
        raise ValueError("canonical compiled Harness semantic evidence hash differs")
    return projection


def _json_value_digest(value: Any) -> str:
    """Match the digest representation frozen by HarnessCompileReceipt.create."""

    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _verify_compile_receipt_semantics(
    receipt: HarnessCompileReceipt,
    projection: Mapping[str, Any],
) -> None:
    """Bind every receipt field derived from the compiled Harness projection."""

    rule_trace = projection["rule_decision_trace"]
    if not isinstance(rule_trace, dict):
        raise ValueError("compiled Harness rule decision trace differs")
    expected = {
        "context_binding_sha256": projection["context_binding_sha256"],
        "decision_sha256": projection["decision_sha256"],
        "operational_fingerprint": projection["operational_fingerprint"],
        "change_map": projection["change_map"],
        "rule_registry_sha256": rule_trace.get("rule_registry_sha256"),
        "component_catalog_sha256": projection["component_catalog_sha256"],
        "component_instances": tuple(projection["component_instances"]),
        "axis_effect_sha256s": projection["axis_effect_sha256s"],
        "axis_configuration_sha256s": projection[
            "axis_configuration_sha256s"
        ],
        "selected_parent_ids": tuple(projection["selected_parent_ids"]),
        "memory_sha256": _json_value_digest(projection["memory"]),
        "tool_outputs_sha256": _json_value_digest(projection["tool_outputs"]),
        "workflow_sha256": _json_value_digest(projection["execution_steps"]),
        "scheduler_sha256": _json_value_digest(projection["scheduler_phase"]),
        "solution_prompt_sha256": projection["solution_prompt_sha256"],
        "builder_meta_prior_sha256": projection["builder_meta_prior_sha256"],
    }
    if any(getattr(receipt, field) != value for field, value in expected.items()):
        raise ValueError(
            "arm-specific v001 typed compile receipt semantic projection differs"
        )


@dataclass(frozen=True)
class V001CanonicalCompileContract(_ContentAddressed):
    task_seed_key_sha256: str
    context_binding_sha256: str
    decision_sha256: str
    operational_fingerprint: str
    compiled_harness_semantic_sha256: str
    solution_prompt_sha256: str
    component_catalog_sha256: str
    builder_meta_prior_sha256: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.context_binding_sha256, "context binding sha256"),
            (self.decision_sha256, "decision sha256"),
            (self.operational_fingerprint, "operational fingerprint"),
            (
                self.compiled_harness_semantic_sha256,
                "compiled Harness semantic sha256",
            ),
            (self.solution_prompt_sha256, "solution prompt sha256"),
            (self.component_catalog_sha256, "component catalog sha256"),
        ):
            _sha(value, label, allow_zero=False)
        _sha(self.builder_meta_prior_sha256, "Builder meta-prior sha256")

    @classmethod
    def create(
        cls,
        key: TaskSeedKey,
        decision: HarnessDecision,
        compiled: CompiledHarness,
    ) -> "V001CanonicalCompileContract":
        if not isinstance(key, TaskSeedKey):
            raise TypeError("TaskSeedKey is required")
        if not isinstance(decision, HarnessDecision):
            raise TypeError("Harness decision is required")
        if compiled.context_binding_sha256 != key.context_binding_sha256:
            raise ValueError("canonical compile context binding differs")
        if compiled.decision_sha256 != decision.sha256:
            raise ValueError("canonical compile decision binding differs")
        if compiled.operational_fingerprint != decision.operational_fingerprint:
            raise ValueError("canonical compile operational fingerprint differs")
        prompt_sha = hashlib.sha256(compiled.solution_prompt.encode("utf-8")).hexdigest()
        return cls(
            task_seed_key_sha256=key.sha256,
            context_binding_sha256=key.context_binding_sha256,
            decision_sha256=decision.sha256,
            operational_fingerprint=decision.operational_fingerprint,
            compiled_harness_semantic_sha256=compiled_harness_semantic_sha256(
                compiled
            ),
            solution_prompt_sha256=prompt_sha,
            component_catalog_sha256=compiled.component_catalog_sha256,
            builder_meta_prior_sha256=compiled.builder_meta_prior_sha256,
        )

    @classmethod
    def from_bytes(
        cls, encoded: bytes, *, expected_sha256: str
    ) -> "V001CanonicalCompileContract":
        return _content_from_bytes(cls, encoded, expected_sha256=expected_sha256)


@dataclass(frozen=True)
class V001TrunkIntent(_ContentAddressed):
    task_seed_key_sha256: str
    suite: str
    instance_id: str
    seed: int
    task_binding_sha256: str
    factorial_contract_sha256: str
    context_binding_sha256: str
    builder_operation_id: str
    solution_operation_id: str
    evaluator_operation_id: str

    def __post_init__(self) -> None:
        key = TaskSeedKey(
            suite=self.suite,
            instance_id=self.instance_id,
            seed=self.seed,
            task_binding_sha256=self.task_binding_sha256,
            factorial_contract_sha256=self.factorial_contract_sha256,
            context_binding_sha256=self.context_binding_sha256,
        )
        if self.task_seed_key_sha256 != key.sha256:
            raise ValueError("factorial trunk intent task/seed binding differs")
        expected = {
            "builder": key.operation_id("builder"),
            "solution": key.operation_id("solution"),
            "evaluator": key.operation_id("evaluator"),
        }
        actual = {
            "builder": self.builder_operation_id,
            "solution": self.solution_operation_id,
            "evaluator": self.evaluator_operation_id,
        }
        if actual != expected or len(set(actual.values())) != 3:
            raise ValueError("factorial trunk intent operation ids differ")

    @classmethod
    def create(cls, key: TaskSeedKey) -> "V001TrunkIntent":
        if not isinstance(key, TaskSeedKey):
            raise TypeError("TaskSeedKey is required")
        return cls(
            task_seed_key_sha256=key.sha256,
            suite=key.suite,
            instance_id=key.instance_id,
            seed=key.seed,
            task_binding_sha256=key.task_binding_sha256,
            factorial_contract_sha256=key.factorial_contract_sha256,
            context_binding_sha256=key.context_binding_sha256,
            builder_operation_id=key.operation_id("builder"),
            solution_operation_id=key.operation_id("solution"),
            evaluator_operation_id=key.operation_id("evaluator"),
        )

    @property
    def task_seed_key(self) -> TaskSeedKey:
        return TaskSeedKey(
            suite=self.suite,
            instance_id=self.instance_id,
            seed=self.seed,
            task_binding_sha256=self.task_binding_sha256,
            factorial_contract_sha256=self.factorial_contract_sha256,
            context_binding_sha256=self.context_binding_sha256,
        )

    @classmethod
    def from_bytes(cls, encoded: bytes, *, expected_sha256: str) -> "V001TrunkIntent":
        return _content_from_bytes(cls, encoded, expected_sha256=expected_sha256)


@dataclass(frozen=True)
class V001CompileEquivalenceReceipt(_ContentAddressed):
    task_seed_key_sha256: str
    canonical_compile_contract_sha256: str
    canonical_compiled_harness_semantic_sha256: str
    canonical_compiled_harness_semantic_canonical_json: str
    arm_compile_contract_sha256s: dict[str, str]
    arm_compile_receipt_sha256s: dict[str, str]
    arm_compile_receipt_canonical_jsons: dict[str, str]
    arm_compiled_harness_semantic_sha256s: dict[str, str]

    def __post_init__(self) -> None:
        _sha(self.task_seed_key_sha256, "task/seed key sha256", allow_zero=False)
        _sha(
            self.canonical_compile_contract_sha256,
            "canonical compile contract sha256",
            allow_zero=False,
        )
        semantic = _sha(
            self.canonical_compiled_harness_semantic_sha256,
            "canonical compiled Harness semantic sha256",
            allow_zero=False,
        )
        projection = _decode_compiled_semantic_evidence(
            self.canonical_compiled_harness_semantic_canonical_json,
            expected_sha256=semantic,
        )
        for mapping, label in (
            (self.arm_compile_contract_sha256s, "arm compile contracts"),
            (self.arm_compile_receipt_sha256s, "arm compile receipts"),
            (
                self.arm_compiled_harness_semantic_sha256s,
                "arm compiled Harness semantics",
            ),
        ):
            if not isinstance(mapping, Mapping) or set(mapping) != set(FACTORIAL_ARMS):
                raise ValueError(f"factorial trunk {label} coverage differs")
            for value in mapping.values():
                _sha(value, label, allow_zero=False)
        if (
            not isinstance(self.arm_compile_receipt_canonical_jsons, Mapping)
            or set(self.arm_compile_receipt_canonical_jsons) != set(FACTORIAL_ARMS)
        ):
            raise ValueError("factorial trunk arm compile receipt evidence coverage differs")
        for arm_id in FACTORIAL_ARMS:
            canonical_json = self.arm_compile_receipt_canonical_jsons[arm_id]
            if (
                not isinstance(canonical_json, str)
                or not canonical_json
                or len(canonical_json) > 1_048_576
            ):
                raise ValueError("factorial trunk arm compile receipt evidence differs")
            receipt = HarnessCompileReceipt.from_bytes(
                canonical_json.encode("utf-8"),
                expected_sha256=self.arm_compile_receipt_sha256s[arm_id],
            )
            expected_cell_id = f"factorial-cell:{self.task_seed_key_sha256}:{arm_id}"
            if (
                receipt.cell_id != expected_cell_id
                or receipt.variant_id != arm_id
                or receipt.version != "v001"
                or receipt.adaptation_policy != _ARM_ADAPTATION_POLICIES[arm_id]
                or receipt.previous_receipt_sha256 != ZERO_SHA256
                or receipt.previous_decision_sha256 != ZERO_SHA256
            ):
                raise ValueError("arm-specific v001 typed compile receipt identity differs")
            _verify_compile_receipt_semantics(receipt, projection)
        if set(self.arm_compiled_harness_semantic_sha256s.values()) != {semantic}:
            raise ValueError("arm v001 compiled Harness semantics differ from canonical")
        if set(self.arm_compile_contract_sha256s.values()) != {
            self.canonical_compile_contract_sha256
        }:
            raise ValueError("arm v001 compile contracts differ from canonical")
        if len(set(self.arm_compile_receipt_sha256s.values())) != len(FACTORIAL_ARMS):
            raise ValueError("arm-specific v001 compile receipts must be distinct")
        object.__setattr__(
            self,
            "arm_compile_contract_sha256s",
            MappingProxyType(dict(self.arm_compile_contract_sha256s)),
        )
        object.__setattr__(
            self,
            "arm_compile_receipt_sha256s",
            MappingProxyType(dict(self.arm_compile_receipt_sha256s)),
        )
        object.__setattr__(
            self,
            "arm_compile_receipt_canonical_jsons",
            MappingProxyType(dict(self.arm_compile_receipt_canonical_jsons)),
        )
        object.__setattr__(
            self,
            "arm_compiled_harness_semantic_sha256s",
            MappingProxyType(dict(self.arm_compiled_harness_semantic_sha256s)),
        )

    @classmethod
    def create(
        cls,
        *,
        key: TaskSeedKey,
        decision: HarnessDecision,
        canonical_compiled: CompiledHarness,
        arm_compiled: Mapping[str, CompiledHarness],
        arm_compile_receipts: Mapping[str, HarnessCompileReceipt],
    ) -> "V001CompileEquivalenceReceipt":
        if set(arm_compiled) != set(FACTORIAL_ARMS) or set(
            arm_compile_receipts
        ) != set(FACTORIAL_ARMS):
            raise ValueError("four-arm v001 compilation coverage differs")
        canonical = V001CanonicalCompileContract.create(
            key, decision, canonical_compiled
        )
        contracts: dict[str, str] = {}
        semantics: dict[str, str] = {}
        receipt_sha256s: dict[str, str] = {}
        receipt_jsons: dict[str, str] = {}
        for arm_id in FACTORIAL_ARMS:
            compiled = arm_compiled[arm_id]
            contract = V001CanonicalCompileContract.create(key, decision, compiled)
            contracts[arm_id] = contract.sha256
            semantics[arm_id] = contract.compiled_harness_semantic_sha256
            if semantics[arm_id] != canonical.compiled_harness_semantic_sha256:
                raise ValueError("arm v001 compiled Harness semantics differ from canonical")
            receipt = arm_compile_receipts[arm_id]
            if not isinstance(receipt, HarnessCompileReceipt):
                raise TypeError("typed arm compile receipt is required")
            expected_receipt = HarnessCompileReceipt.create(
                cell_id=key.arm_cell_id(arm_id),
                suite=key.suite,
                instance_id=key.instance_id,
                variant_id=arm_id,
                version="v001",
                adaptation_policy=_ARM_ADAPTATION_POLICIES[arm_id],
                previous_receipt_sha256=ZERO_SHA256,
                previous_decision_sha256=ZERO_SHA256,
                compiled=compiled,
                decision=decision,
            )
            if receipt != expected_receipt:
                raise ValueError(
                    f"{arm_id} typed compile receipt differs from trusted compilation"
                )
            if receipt.context_binding_sha256 != key.context_binding_sha256:
                raise ValueError("arm v001 compile receipt context binding differs")
            receipt_sha256s[arm_id] = receipt.sha256
            receipt_jsons[arm_id] = receipt.canonical_bytes.decode("utf-8")
        return cls(
            task_seed_key_sha256=key.sha256,
            canonical_compile_contract_sha256=canonical.sha256,
            canonical_compiled_harness_semantic_sha256=(
                canonical.compiled_harness_semantic_sha256
            ),
            canonical_compiled_harness_semantic_canonical_json=(
                _compiled_semantic_evidence(canonical_compiled)
            ),
            arm_compile_contract_sha256s=contracts,
            arm_compile_receipt_sha256s=receipt_sha256s,
            arm_compile_receipt_canonical_jsons=receipt_jsons,
            arm_compiled_harness_semantic_sha256s=semantics,
        )

    def verify_against_key_and_contract(
        self,
        *,
        key: TaskSeedKey,
        contract: V001CanonicalCompileContract,
    ) -> None:
        """Rebind embedded typed receipts to the task/seed and canonical compile."""

        if not isinstance(key, TaskSeedKey) or not isinstance(
            contract, V001CanonicalCompileContract
        ):
            raise TypeError("task/seed key and canonical compile contract are required")
        if (
            self.task_seed_key_sha256 != key.sha256
            or self.canonical_compile_contract_sha256 != contract.sha256
            or contract.task_seed_key_sha256 != key.sha256
            or contract.context_binding_sha256 != key.context_binding_sha256
        ):
            raise ValueError("v001 compile equivalence task/seed binding differs")
        projection = _decode_compiled_semantic_evidence(
            self.canonical_compiled_harness_semantic_canonical_json,
            expected_sha256=contract.compiled_harness_semantic_sha256,
        )
        for arm_id in FACTORIAL_ARMS:
            receipt = HarnessCompileReceipt.from_bytes(
                self.arm_compile_receipt_canonical_jsons[arm_id].encode("utf-8"),
                expected_sha256=self.arm_compile_receipt_sha256s[arm_id],
            )
            if (
                receipt.cell_id != key.arm_cell_id(arm_id)
                or receipt.suite != key.suite
                or receipt.instance_id != key.instance_id
                or receipt.context_binding_sha256 != key.context_binding_sha256
                or receipt.decision_sha256 != contract.decision_sha256
                or receipt.operational_fingerprint != contract.operational_fingerprint
                or receipt.component_catalog_sha256
                != contract.component_catalog_sha256
                or receipt.solution_prompt_sha256 != contract.solution_prompt_sha256
                or receipt.builder_meta_prior_sha256
                != contract.builder_meta_prior_sha256
            ):
                raise ValueError("arm-specific v001 typed compile receipt binding differs")
            _verify_compile_receipt_semantics(receipt, projection)

    @classmethod
    def from_bytes(
        cls, encoded: bytes, *, expected_sha256: str
    ) -> "V001CompileEquivalenceReceipt":
        return _content_from_bytes(cls, encoded, expected_sha256=expected_sha256)


@dataclass(frozen=True)
class V001TrunkReceipt(_ContentAddressed):
    task_seed_key_sha256: str
    intent_sha256: str
    canonical_compile_contract_sha256: str
    compile_equivalence_receipt_sha256: str
    trunk_status: str
    version: str
    decision_sha256: str
    operational_fingerprint: str
    compiled_harness_semantic_sha256: str
    solution_prompt_sha256: str
    solution_artifact_sha256: str
    attempt_artifact_sha256: str
    evaluation_artifact_sha256: str

    def __post_init__(self) -> None:
        _sha(self.task_seed_key_sha256, "task/seed key sha256", allow_zero=False)
        _sha(self.intent_sha256, "intent sha256", allow_zero=False)
        if self.trunk_status not in TRUNK_STATUSES:
            raise ValueError("factorial trunk status differs")
        if self.version != "v001":
            raise ValueError("factorial trunk version must be v001")
        compile_hashes = (
            self.canonical_compile_contract_sha256,
            self.compile_equivalence_receipt_sha256,
            self.decision_sha256,
            self.operational_fingerprint,
            self.compiled_harness_semantic_sha256,
            self.solution_prompt_sha256,
        )
        result_hashes = (
            self.solution_artifact_sha256,
            self.attempt_artifact_sha256,
            self.evaluation_artifact_sha256,
        )
        for value in (*compile_hashes, *result_hashes):
            _sha(value, "trunk artifact sha256")
        compile_complete = all(value != ZERO_SHA256 for value in compile_hashes)
        compile_empty = all(value == ZERO_SHA256 for value in compile_hashes)
        if not (compile_complete or compile_empty):
            raise ValueError("factorial trunk compile artifact prefix is inconsistent")
        expected_result_presence = {
            "SUCCESS": (True, True, True),
            "SOLUTION_CONTRACT_REJECTED": (True, True, False),
            "OPERATION_INTERRUPTED": (False, False, False),
            "COMMON_TRUNK_FAILURE": (False, False, False),
            "ENVIRONMENT_INVALID": (False, False, False),
        }[self.trunk_status]
        observed_result_presence = tuple(
            value != ZERO_SHA256 for value in result_hashes
        )
        if observed_result_presence != expected_result_presence:
            raise ValueError("factorial trunk terminal artifacts differ")
        if self.trunk_status in {"SUCCESS", "SOLUTION_CONTRACT_REJECTED"}:
            if not compile_complete:
                raise ValueError("terminal factorial trunk lacks its compilation")
        elif self.trunk_status == "ENVIRONMENT_INVALID":
            if not compile_empty:
                raise ValueError("environment-invalid factorial trunk carries artifacts")
        elif self.trunk_status in {"OPERATION_INTERRUPTED", "COMMON_TRUNK_FAILURE"}:
            # These broad pre-controller statuses may occur either before or after
            # compilation, but never after a solution/evaluation artifact exists.
            if not (compile_empty or compile_complete):  # pragma: no cover
                raise ValueError("failed factorial trunk compilation differs")

    @classmethod
    def create(
        cls,
        *,
        intent: V001TrunkIntent,
        trunk_status: str,
        canonical_compile_contract: V001CanonicalCompileContract | None = None,
        compile_equivalence_receipt: V001CompileEquivalenceReceipt | None = None,
        solution_artifact_sha256: str = ZERO_SHA256,
        attempt_artifact_sha256: str = ZERO_SHA256,
        evaluation_artifact_sha256: str = ZERO_SHA256,
    ) -> "V001TrunkReceipt":
        if not isinstance(intent, V001TrunkIntent):
            raise TypeError("v001 trunk intent is required")
        contract = canonical_compile_contract
        equivalence = compile_equivalence_receipt
        if (contract is None) != (equivalence is None):
            raise ValueError("canonical compile and equivalence must be paired")
        if equivalence is not None and (
            equivalence.task_seed_key_sha256 != intent.task_seed_key_sha256
            or equivalence.canonical_compile_contract_sha256 != contract.sha256
            or equivalence.canonical_compiled_harness_semantic_sha256
            != contract.compiled_harness_semantic_sha256
        ):
            raise ValueError("factorial trunk compile equivalence binding differs")
        if contract is not None and (
            contract.task_seed_key_sha256 != intent.task_seed_key_sha256
            or contract.context_binding_sha256
            != intent.context_binding_sha256
        ):
            raise ValueError("factorial trunk canonical compile identity differs")
        return cls(
            task_seed_key_sha256=intent.task_seed_key_sha256,
            intent_sha256=intent.sha256,
            canonical_compile_contract_sha256=(
                ZERO_SHA256 if contract is None else contract.sha256
            ),
            compile_equivalence_receipt_sha256=(
                ZERO_SHA256 if equivalence is None else equivalence.sha256
            ),
            trunk_status=trunk_status,
            version="v001",
            decision_sha256=ZERO_SHA256 if contract is None else contract.decision_sha256,
            operational_fingerprint=(
                ZERO_SHA256 if contract is None else contract.operational_fingerprint
            ),
            compiled_harness_semantic_sha256=(
                ZERO_SHA256
                if contract is None
                else contract.compiled_harness_semantic_sha256
            ),
            solution_prompt_sha256=(
                ZERO_SHA256 if contract is None else contract.solution_prompt_sha256
            ),
            solution_artifact_sha256=solution_artifact_sha256,
            attempt_artifact_sha256=attempt_artifact_sha256,
            evaluation_artifact_sha256=evaluation_artifact_sha256,
        )

    @classmethod
    def from_bytes(cls, encoded: bytes, *, expected_sha256: str) -> "V001TrunkReceipt":
        return _content_from_bytes(cls, encoded, expected_sha256=expected_sha256)


@dataclass(frozen=True)
class V001ArmForkReceipt(_ContentAddressed):
    task_seed_key_sha256: str
    trunk_receipt_sha256: str
    arm_id: str
    arm_cell_id: str
    arm_variant_sha256: str
    arm_contract_sha256: str
    arm_compile_receipt_sha256: str
    trunk_status: str
    version: str
    shared_decision_sha256: str
    shared_operational_fingerprint: str
    shared_compiled_harness_semantic_sha256: str
    shared_solution_prompt_sha256: str
    shared_solution_artifact_sha256: str
    shared_attempt_artifact_sha256: str
    shared_evaluation_artifact_sha256: str

    def __post_init__(self) -> None:
        _sha(self.task_seed_key_sha256, "task/seed key sha256", allow_zero=False)
        _sha(self.trunk_receipt_sha256, "trunk receipt sha256", allow_zero=False)
        if self.arm_id not in FACTORIAL_ARMS:
            raise ValueError("factorial trunk fork arm differs")
        expected_cell = f"factorial-cell:{self.task_seed_key_sha256}:{self.arm_id}"
        if self.arm_cell_id != expected_cell:
            raise ValueError("factorial trunk fork arm cell differs")
        for value, label in (
            (self.arm_variant_sha256, "arm variant sha256"),
            (self.arm_contract_sha256, "arm contract sha256"),
            (self.arm_compile_receipt_sha256, "arm compile receipt sha256"),
        ):
            _sha(value, label, allow_zero=False)
        if self.trunk_status not in TRUNK_STATUSES:
            raise ValueError("factorial trunk fork status differs")
        if self.trunk_status not in {"SUCCESS", "SOLUTION_CONTRACT_REJECTED"}:
            raise ValueError("non-result trunk cannot fork")
        if self.version != "v001":
            raise ValueError("factorial trunk fork version must be v001")
        for value in (
            self.shared_decision_sha256,
            self.shared_operational_fingerprint,
            self.shared_compiled_harness_semantic_sha256,
            self.shared_solution_prompt_sha256,
            self.shared_solution_artifact_sha256,
            self.shared_attempt_artifact_sha256,
            self.shared_evaluation_artifact_sha256,
        ):
            _sha(value, "shared trunk artifact sha256")
        shared_compile_hashes = (
            self.shared_decision_sha256,
            self.shared_operational_fingerprint,
            self.shared_compiled_harness_semantic_sha256,
            self.shared_solution_prompt_sha256,
        )
        shared_result_hashes = (
            self.shared_solution_artifact_sha256,
            self.shared_attempt_artifact_sha256,
            self.shared_evaluation_artifact_sha256,
        )
        if self.trunk_status == "SUCCESS" and any(
            value == ZERO_SHA256 for value in (*shared_compile_hashes, *shared_result_hashes)
        ):
            raise ValueError("successful factorial trunk fork is incomplete")
        if self.trunk_status == "SOLUTION_CONTRACT_REJECTED" and (
            any(value == ZERO_SHA256 for value in shared_compile_hashes)
            or self.shared_solution_artifact_sha256 == ZERO_SHA256
            or self.shared_attempt_artifact_sha256 == ZERO_SHA256
            or self.shared_evaluation_artifact_sha256 != ZERO_SHA256
        ):
            raise ValueError("contract-rejected factorial trunk fork artifacts differ")
        if self.trunk_status in {"OPERATION_INTERRUPTED", "COMMON_TRUNK_FAILURE"} and all(
            value != ZERO_SHA256 for value in (*shared_compile_hashes, *shared_result_hashes)
        ):
            raise ValueError("failed factorial trunk fork is indistinguishable from success")

    @classmethod
    def create(
        cls,
        *,
        key: TaskSeedKey,
        trunk: V001TrunkReceipt,
        arm_id: str,
        arm_variant_sha256: str,
        arm_contract_sha256: str,
        arm_compile_receipt_sha256: str,
    ) -> "V001ArmForkReceipt":
        if trunk.task_seed_key_sha256 != key.sha256:
            raise ValueError("factorial trunk fork task/seed binding differs")
        return cls(
            task_seed_key_sha256=key.sha256,
            trunk_receipt_sha256=trunk.sha256,
            arm_id=arm_id,
            arm_cell_id=key.arm_cell_id(arm_id),
            arm_variant_sha256=arm_variant_sha256,
            arm_contract_sha256=arm_contract_sha256,
            arm_compile_receipt_sha256=arm_compile_receipt_sha256,
            trunk_status=trunk.trunk_status,
            version="v001",
            shared_decision_sha256=trunk.decision_sha256,
            shared_operational_fingerprint=trunk.operational_fingerprint,
            shared_compiled_harness_semantic_sha256=(
                trunk.compiled_harness_semantic_sha256
            ),
            shared_solution_prompt_sha256=trunk.solution_prompt_sha256,
            shared_solution_artifact_sha256=trunk.solution_artifact_sha256,
            shared_attempt_artifact_sha256=trunk.attempt_artifact_sha256,
            shared_evaluation_artifact_sha256=trunk.evaluation_artifact_sha256,
        )

    @classmethod
    def from_bytes(cls, encoded: bytes, *, expected_sha256: str) -> "V001ArmForkReceipt":
        return _content_from_bytes(cls, encoded, expected_sha256=expected_sha256)


class FactorialTrunkArchive:
    """Symlink-safe write-once objects plus task/seed identity bindings."""

    def __init__(
        self,
        root: Path,
        *,
        expected_factorial_contract_sha256: str | None = None,
        expected_arm_variant_sha256s: Mapping[str, str] | None = None,
    ) -> None:
        self.root = lexical_absolute(root)
        if (expected_factorial_contract_sha256 is None) != (
            expected_arm_variant_sha256s is None
        ):
            raise ValueError(
                "factorial trunk formal fork bindings must be supplied together"
            )
        if expected_factorial_contract_sha256 is None:
            self._expected_factorial_contract_sha256: str | None = None
            self._expected_arm_variant_sha256s: Mapping[str, str] | None = None
        else:
            self._expected_factorial_contract_sha256 = _sha(
                expected_factorial_contract_sha256,
                "expected factorial contract sha256",
                allow_zero=False,
            )
            if (
                not isinstance(expected_arm_variant_sha256s, Mapping)
                or tuple(expected_arm_variant_sha256s) != FACTORIAL_ARMS
            ):
                raise ValueError(
                    "factorial trunk expected arm variant coverage or order differs"
                )
            variants = {
                arm_id: _sha(
                    expected_arm_variant_sha256s[arm_id],
                    "expected arm variant sha256",
                    allow_zero=False,
                )
                for arm_id in FACTORIAL_ARMS
            }
            self._expected_arm_variant_sha256s = MappingProxyType(variants)

    def _object_path(self, kind: str, sha256: str) -> Path:
        return self.root / "objects" / kind / f"{sha256}.json"

    def _store_object(self, kind: str, item: _ContentAddressed) -> Path:
        try:
            return write_once_safe_regular_file(
                self._object_path(kind, item.sha256),
                item.canonical_bytes,
                label=f"factorial trunk {kind} object",
                temporary_suffix=f".{kind}.tmp",
            )
        except ValueError as exc:
            if "refusing to overwrite" in str(exc):
                raise ValueError(f"factorial trunk {kind} content-address collision") from exc
            raise

    def _binding_path(self, kind: str, key_sha256: str, arm_id: str | None = None) -> Path:
        suffix = f"/{arm_id}.json" if arm_id is not None else ".json"
        return self.root / "bindings" / kind / f"{key_sha256}{suffix}"

    def _store_binding(
        self,
        kind: str,
        key_sha256: str,
        object_sha256: str,
        *,
        arm_id: str | None = None,
    ) -> Path:
        payload: dict[str, Any] = {
            "schema_version": 1,
            "kind": kind,
            "task_seed_key_sha256": key_sha256,
            "object_sha256": object_sha256,
        }
        if arm_id is not None:
            payload["arm_id"] = arm_id
        try:
            return write_once_safe_regular_file(
                self._binding_path(kind, key_sha256, arm_id),
                _canonical_bytes(payload),
                label=f"factorial trunk {kind} identity binding",
                temporary_suffix=f".{kind}-binding.tmp",
            )
        except ValueError as exc:
            if "refusing to overwrite" in str(exc):
                raise ValueError(f"factorial trunk {kind} identity binding differs") from exc
            raise

    def _load_binding(
        self, kind: str, key_sha256: str, *, arm_id: str | None = None
    ) -> str:
        _sha(key_sha256, "task/seed key sha256", allow_zero=False)
        if arm_id is not None and arm_id not in FACTORIAL_ARMS:
            raise ValueError("factorial trunk binding arm differs")
        path = self._binding_path(kind, key_sha256, arm_id)
        if not safe_regular_file_exists(path, label=f"factorial trunk {kind} identity binding"):
            raise ValueError(f"factorial trunk {kind} identity binding is missing")
        encoded = read_safe_regular_file(
            path, label=f"factorial trunk {kind} identity binding"
        )
        payload = _decode(encoded, label=f"factorial trunk {kind} identity binding")
        expected = {
            "schema_version",
            "kind",
            "task_seed_key_sha256",
            "object_sha256",
        }
        if arm_id is not None:
            expected.add("arm_id")
        _exact_fields(payload, expected, f"factorial trunk {kind} identity binding")
        if (
            payload["schema_version"] != 1
            or payload["kind"] != kind
            or payload["task_seed_key_sha256"] != key_sha256
            or (arm_id is not None and payload["arm_id"] != arm_id)
        ):
            raise ValueError(f"factorial trunk {kind} identity binding differs")
        return _sha(payload["object_sha256"], "bound object sha256", allow_zero=False)

    def _load_object(self, kind: str, sha256: str, cls: type[Any]) -> Any:
        path = self._object_path(kind, sha256)
        if not safe_regular_file_exists(path, label=f"factorial trunk {kind} object"):
            raise ValueError(f"factorial trunk {kind} object is missing")
        return cls.from_bytes(
            read_safe_regular_file(path, label=f"factorial trunk {kind} object"),
            expected_sha256=sha256,
        )

    def store_intent(self, intent: V001TrunkIntent) -> Path:
        self._store_object("intents", intent)
        return self._store_binding("intents", intent.task_seed_key_sha256, intent.sha256)

    def load_intent(self, key_sha256: str) -> V001TrunkIntent:
        object_sha = self._load_binding("intents", key_sha256)
        intent = self._load_object("intents", object_sha, V001TrunkIntent)
        if intent.task_seed_key_sha256 != key_sha256:
            raise ValueError("factorial trunk intent identity differs")
        return intent

    def store_canonical_compile(
        self, key: TaskSeedKey, contract: V001CanonicalCompileContract
    ) -> Path:
        intent = self.load_intent(key.sha256)
        if (
            intent.task_seed_key != key
            or contract.task_seed_key_sha256 != key.sha256
            or contract.context_binding_sha256 != key.context_binding_sha256
        ):
            raise ValueError("canonical compile task/seed identity differs")
        self._store_object("canonical-compiles", contract)
        return self._store_binding(
            "canonical-compiles", key.sha256, contract.sha256
        )

    def load_canonical_compile(
        self, key_sha256: str
    ) -> V001CanonicalCompileContract:
        intent = self.load_intent(key_sha256)
        object_sha = self._load_binding("canonical-compiles", key_sha256)
        contract = self._load_object(
            "canonical-compiles", object_sha, V001CanonicalCompileContract
        )
        if (
            contract.task_seed_key_sha256 != key_sha256
            or contract.context_binding_sha256
            != intent.context_binding_sha256
        ):
            raise ValueError("canonical compile task/seed binding differs")
        return contract

    def store_equivalence(
        self, key: TaskSeedKey, receipt: V001CompileEquivalenceReceipt
    ) -> Path:
        contract = self.load_canonical_compile(key.sha256)
        if (
            receipt.task_seed_key_sha256 != key.sha256
            or contract.task_seed_key_sha256 != key.sha256
            or contract.context_binding_sha256 != key.context_binding_sha256
            or receipt.canonical_compile_contract_sha256 != contract.sha256
            or receipt.canonical_compiled_harness_semantic_sha256
            != contract.compiled_harness_semantic_sha256
        ):
            raise ValueError("v001 compile equivalence identity differs")
        receipt.verify_against_key_and_contract(key=key, contract=contract)
        self._store_object("equivalence", receipt)
        return self._store_binding("equivalence", key.sha256, receipt.sha256)

    def load_equivalence(self, key_sha256: str) -> V001CompileEquivalenceReceipt:
        intent = self.load_intent(key_sha256)
        key = intent.task_seed_key
        contract = self.load_canonical_compile(key_sha256)
        object_sha = self._load_binding("equivalence", key_sha256)
        receipt = self._load_object(
            "equivalence", object_sha, V001CompileEquivalenceReceipt
        )
        if (
            receipt.task_seed_key_sha256 != key_sha256
            or contract.task_seed_key_sha256 != key_sha256
            or receipt.canonical_compile_contract_sha256 != contract.sha256
            or receipt.canonical_compiled_harness_semantic_sha256
            != contract.compiled_harness_semantic_sha256
        ):
            raise ValueError("v001 compile equivalence binding differs")
        receipt.verify_against_key_and_contract(key=key, contract=contract)
        return receipt

    def store_trunk(self, receipt: V001TrunkReceipt) -> Path:
        intent = self.load_intent(receipt.task_seed_key_sha256)
        if receipt.intent_sha256 != intent.sha256:
            raise ValueError("v001 trunk intent binding differs")
        self._verify_trunk_compile_bindings(receipt)
        self._store_object("trunks", receipt)
        return self._store_binding(
            "trunks", receipt.task_seed_key_sha256, receipt.sha256
        )

    def _verify_trunk_compile_bindings(self, receipt: V001TrunkReceipt) -> None:
        if receipt.canonical_compile_contract_sha256 == ZERO_SHA256:
            if receipt.compile_equivalence_receipt_sha256 != ZERO_SHA256:
                raise ValueError("v001 trunk has equivalence without canonical compile")
            return
        contract = self.load_canonical_compile(receipt.task_seed_key_sha256)
        equivalence = self.load_equivalence(receipt.task_seed_key_sha256)
        if (
            receipt.canonical_compile_contract_sha256 != contract.sha256
            or receipt.compile_equivalence_receipt_sha256 != equivalence.sha256
            or receipt.decision_sha256 != contract.decision_sha256
            or receipt.operational_fingerprint != contract.operational_fingerprint
            or receipt.compiled_harness_semantic_sha256
            != contract.compiled_harness_semantic_sha256
            or receipt.solution_prompt_sha256 != contract.solution_prompt_sha256
        ):
            raise ValueError("v001 trunk canonical compile binding differs")

    def load_trunk(self, key_sha256: str) -> V001TrunkReceipt:
        intent = self.load_intent(key_sha256)
        object_sha = self._load_binding("trunks", key_sha256)
        receipt = self._load_object("trunks", object_sha, V001TrunkReceipt)
        if receipt.task_seed_key_sha256 != key_sha256 or receipt.intent_sha256 != intent.sha256:
            raise ValueError("v001 trunk identity differs")
        self._verify_trunk_compile_bindings(receipt)
        return receipt

    @staticmethod
    def _verify_fork_against_trunk(
        fork: V001ArmForkReceipt, trunk: V001TrunkReceipt
    ) -> None:
        expected = {
            "task_seed_key_sha256": trunk.task_seed_key_sha256,
            "trunk_receipt_sha256": trunk.sha256,
            "trunk_status": trunk.trunk_status,
            "version": trunk.version,
            "shared_decision_sha256": trunk.decision_sha256,
            "shared_operational_fingerprint": trunk.operational_fingerprint,
            "shared_compiled_harness_semantic_sha256": (
                trunk.compiled_harness_semantic_sha256
            ),
            "shared_solution_prompt_sha256": trunk.solution_prompt_sha256,
            "shared_solution_artifact_sha256": trunk.solution_artifact_sha256,
            "shared_attempt_artifact_sha256": trunk.attempt_artifact_sha256,
            "shared_evaluation_artifact_sha256": trunk.evaluation_artifact_sha256,
        }
        if any(getattr(fork, key) != value for key, value in expected.items()):
            raise ValueError("v001 arm fork shared trunk binding differs")

    def _verify_fork_variant_contract_bindings(
        self,
        fork: V001ArmForkReceipt,
        intent: V001TrunkIntent,
    ) -> None:
        """Rebind formal fork metadata to the trusted caller-supplied manifest.

        A generic archive deliberately has no opinion about which experiment
        manifest produced a fork.  A formal archive must therefore receive the
        immutable contract and complete per-arm variant mapping explicitly;
        merely carrying any nonzero hashes in a content-addressed fork is not
        evidence of that provenance.
        """

        if fork.arm_contract_sha256 != intent.factorial_contract_sha256:
            raise ValueError("v001 arm fork variant/contract binding differs")
        if self._expected_factorial_contract_sha256 is None:
            return
        assert self._expected_arm_variant_sha256s is not None
        if (
            intent.factorial_contract_sha256
            != self._expected_factorial_contract_sha256
            or fork.arm_contract_sha256
            != self._expected_factorial_contract_sha256
            or fork.arm_variant_sha256
            != self._expected_arm_variant_sha256s[fork.arm_id]
        ):
            raise ValueError("v001 arm fork variant/contract binding differs")

    def store_fork(self, receipt: V001ArmForkReceipt) -> Path:
        intent = self.load_intent(receipt.task_seed_key_sha256)
        trunk = self.load_trunk(receipt.task_seed_key_sha256)
        self._verify_fork_against_trunk(receipt, trunk)
        self._verify_fork_variant_contract_bindings(receipt, intent)
        equivalence = self.load_equivalence(receipt.task_seed_key_sha256)
        if (
            receipt.arm_compile_receipt_sha256
            != equivalence.arm_compile_receipt_sha256s[receipt.arm_id]
        ):
            raise ValueError("v001 arm fork compile receipt binding differs")
        for other_arm in FACTORIAL_ARMS:
            if other_arm == receipt.arm_id:
                continue
            other_path = self._binding_path(
                "forks", receipt.task_seed_key_sha256, other_arm
            )
            if safe_regular_file_exists(
                other_path, label="factorial trunk forks identity binding"
            ):
                other = self.load_fork(receipt.task_seed_key_sha256, other_arm)
                if other.sha256 == receipt.sha256:
                    raise ValueError("v001 arm fork receipts must be distinct")
        self._store_object("forks", receipt)
        return self._store_binding(
            "forks",
            receipt.task_seed_key_sha256,
            receipt.sha256,
            arm_id=receipt.arm_id,
        )

    def load_fork(self, key_sha256: str, arm_id: str) -> V001ArmForkReceipt:
        intent = self.load_intent(key_sha256)
        trunk = self.load_trunk(key_sha256)
        equivalence = self.load_equivalence(key_sha256)
        object_sha = self._load_binding("forks", key_sha256, arm_id=arm_id)
        receipt = self._load_object("forks", object_sha, V001ArmForkReceipt)
        if receipt.arm_id != arm_id or receipt.task_seed_key_sha256 != key_sha256:
            raise ValueError("v001 arm fork identity differs")
        self._verify_fork_against_trunk(receipt, trunk)
        self._verify_fork_variant_contract_bindings(receipt, intent)
        if (
            receipt.arm_compile_receipt_sha256
            != equivalence.arm_compile_receipt_sha256s[arm_id]
        ):
            raise ValueError("v001 arm fork compile receipt binding differs")
        return receipt
