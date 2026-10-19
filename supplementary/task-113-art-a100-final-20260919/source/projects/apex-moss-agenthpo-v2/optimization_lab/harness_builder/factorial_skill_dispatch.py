"""Zero-call authority for post-v001 ``S-reflection-skill`` updates.

This module derives immutable update and prompt receipts from exact factorial
scoring slots.  It has deliberately no provider, evaluator, callback, budget
governor, subprocess, or filesystem entry point.  Consequently every object
created here carries ``NOT_GRANTED`` execution authority and zero entitlement.

The S arm freezes the complete v001 Harness decision.  Only a task/seed-local
typed Skill may change, using the immediately preceding sealed round's narrow
public projection.  The Skill is injected after trusted Harness compilation;
it is never represented as a Harness component or decision mutation.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, fields
import hashlib
import json
import math
import re
from typing import Any, Sequence

from .compile_receipts import HarnessCompileReceipt
from .factorial_coverage import (
    AttemptCoverageRow,
    ExactFactorialAttemptMatrix,
    FactorialScoringSlot,
    SHARED_V001_ARM_ID,
    TYPED_SCORE_UNBOUND,
)
from .factorial_formal_dispatch import (
    FactorialV001FormalCompileOrchestrator,
    FactorialV001TrustedCompileResult,
)
from .factorial_policies import (
    EMPTY_TASK_LOCAL_SKILL_SHA256,
    HARNESS_AXES,
    S_REFLECTION_SKILL,
    SkillUpdateReceipt,
    TaskLocalSkillRecord,
    solver_skill_projection,
)
from .factorial_precheck import FactorialFormalZeroCallPlan
from .factorial_task_authority import (
    ExactTaskSeedAuthorityBundle,
    FactorialTaskArtifactAuthority,
)
from .factorial_trunk import TaskSeedKey
from .operators import HarnessContext
from .schema import HarnessDecision


ZERO_SHA256 = "0" * 64
EXECUTION_AUTHORITY = "NOT_GRANTED"
_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_VERSION = re.compile(r"v([0-9]{3})")
_PRIVATE_TEXT = re.compile(
    r"(?:/home/|/root/|/data\d*/|file://|(?:^|[^A-Za-z0-9])"
    r"(?:private|secret|token|hidden[_ -]?evidence|gold|reference[_ -]?answer)"
    r"(?:$|[^A-Za-z0-9]))",
    re.IGNORECASE,
)
_PUBLIC_OUTCOMES = {"VALID", "INVALID"}
_ENTITLEMENT = {
    "cpu_evaluator_seconds": 0,
    "evaluator_transactions": 0,
    "gpu_exclusive_seconds": 0,
    "model_calls": 0,
}


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
    except (TypeError, ValueError, UnicodeError) as exc:
        raise ValueError("Skill-dispatch payload is not canonical JSON") from exc


def _digest(payload: object) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _sha(value: object, label: str, *, allow_zero: bool = False) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"invalid {label}")
    if not allow_zero and value == ZERO_SHA256:
        raise ValueError(f"empty {label}")
    return value


def _safe(value: object, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise ValueError(f"unsafe {label}")
    return value


def _version_number(value: object, label: str) -> int:
    if not isinstance(value, str) or (match := _VERSION.fullmatch(value)) is None:
        raise ValueError(f"invalid {label}")
    return int(match.group(1))


def _decode_content(cls: type[Any], encoded: bytes, expected_sha256: str) -> Any:
    _sha(expected_sha256, "expected content sha256")
    if not isinstance(encoded, bytes):
        raise TypeError("content must be bytes")

    def reject_constant(value: str) -> None:
        raise ValueError(f"JSON contains forbidden constant {value}")

    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"JSON repeats field {key!r}")
            result[key] = value
        return result

    try:
        payload = json.loads(
            encoded.decode("utf-8", errors="strict"),
            object_pairs_hook=reject_duplicates,
            parse_constant=reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("Skill-dispatch JSON is invalid") from exc
    if not isinstance(payload, dict) or _canonical_bytes(payload) != encoded:
        raise ValueError("Skill-dispatch content is not a canonical object")
    expected = {item.name for item in fields(cls)} | {
        "schema_version",
        "execution_authority",
        "execution_entitlement",
    }
    if set(payload) != expected:
        raise ValueError("Skill-dispatch content fields differ")
    if (
        payload.pop("schema_version") != 1
        or payload.pop("execution_authority") != EXECUTION_AUTHORITY
        or payload.pop("execution_entitlement") != _ENTITLEMENT
    ):
        raise ValueError("Skill-dispatch content grants or changes authority")
    if "public_summary" in payload:
        payload["public_summary"] = tuple(payload["public_summary"])
    item = cls(**payload)
    if item.canonical_bytes != encoded or item.sha256 != expected_sha256:
        raise ValueError("Skill-dispatch content replay differs")
    return item


class _ContentAddressed:
    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            **asdict(self),
            "execution_authority": EXECUTION_AUTHORITY,
            "execution_entitlement": dict(_ENTITLEMENT),
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


def frozen_axis_projection(decision: HarnessDecision) -> dict[str, Any]:
    """Canonical seven-axis projection; membership axes ignore ordering."""

    if type(decision) is not HarnessDecision:
        raise TypeError("exact frozen Harness decision is required")
    projection = {
        "role_graph": sorted(decision.role_graph),
        "memory_views": sorted(decision.memory_views),
        "tools": sorted(decision.tools),
        "parent_strategy": decision.parent_strategy,
        "workflow": list(decision.workflow),
        "scheduler_mode": decision.scheduler_mode,
        "recovery_mode": decision.recovery_mode,
    }
    if tuple(projection) != HARNESS_AXES:
        raise ValueError("frozen Harness axis coverage differs")
    return projection


@dataclass(frozen=True)
class SourcePublicFeedback(_ContentAddressed):
    """The complete and only allowlist visible to the Skill updater."""

    source_slot_sha256: str
    source_attempt_id: str
    source_terminal_receipt_sha256: str
    candidate_artifact_sha256: str
    outcome: str
    valid: bool
    correct: bool | None
    raw_score: float | None
    public_reason_code: str
    structural_signature: str
    public_summary: tuple[str, ...]

    def __post_init__(self) -> None:
        for value, label in (
            (self.source_slot_sha256, "source slot sha256"),
            (self.source_terminal_receipt_sha256, "source terminal receipt sha256"),
        ):
            _sha(value, label)
        _sha(self.candidate_artifact_sha256, "candidate artifact sha256", allow_zero=True)
        _safe(self.source_attempt_id, "source attempt id")
        _safe(self.public_reason_code, "public reason code")
        _safe(self.structural_signature, "structural signature")
        if self.outcome not in _PUBLIC_OUTCOMES or type(self.valid) is not bool:
            raise ValueError("public feedback outcome differs")
        if self.correct is not None and type(self.correct) is not bool:
            raise ValueError("public feedback correctness differs")
        if self.raw_score is not None and (
            isinstance(self.raw_score, bool)
            or not isinstance(self.raw_score, (int, float))
            or not math.isfinite(self.raw_score)
        ):
            raise ValueError("public feedback score must be finite")
        if self.valid != (self.outcome == "VALID"):
            raise ValueError("public feedback validity/outcome differs")
        if self.valid:
            if self.raw_score is None or self.public_reason_code != "NONE":
                raise ValueError("valid public feedback score/reason differs")
        elif self.raw_score is not None or self.public_reason_code == "NONE":
            raise ValueError("invalid public feedback score/reason differs")
        if (
            not isinstance(self.public_summary, tuple)
            or not 1 <= len(self.public_summary) <= 8
        ):
            raise ValueError("public feedback summary must contain 1-8 items")
        for item in self.public_summary:
            if (
                not isinstance(item, str)
                or not item.strip()
                or len(item) > 512
                or "\x00" in item
                or _PRIVATE_TEXT.search(item)
            ):
                raise ValueError("public feedback contains private or unsafe text")

    def to_dict(self) -> dict[str, Any]:
        payload = super().to_dict()
        payload["public_summary"] = list(self.public_summary)
        return payload

    @classmethod
    def from_bytes(cls, encoded: bytes, *, expected_sha256: str) -> "SourcePublicFeedback":
        item = _decode_content(cls, encoded, expected_sha256)
        return cls(**{**asdict(item), "public_summary": tuple(item.public_summary)})

    @classmethod
    def from_typed_coverage(
        cls,
        *,
        source_slot: FactorialScoringSlot,
        coverage_row: AttemptCoverageRow,
        source_terminal_receipt_sha256: str,
        candidate_artifact_sha256: str,
        correct: bool | None,
        structural_signature: str,
        public_summary: tuple[str, ...],
    ) -> "SourcePublicFeedback":
        """Project only allowlisted fields from an exact typed ITT row."""

        if type(source_slot) is not FactorialScoringSlot or type(
            coverage_row
        ) is not AttemptCoverageRow:
            raise TypeError("typed source slot and coverage row are required")
        try:
            coverage_row.verify_against_slot(
                matrix_sha256=coverage_row.matrix_sha256, slot=source_slot
            )
        except (TypeError, ValueError) as exc:
            raise ValueError("public feedback coverage binding differs") from exc
        if coverage_row.coverage_state != TYPED_SCORE_UNBOUND:
            raise ValueError("public feedback source is not a typed terminal score")
        valid = coverage_row.valid is True
        return cls(
            source_slot_sha256=source_slot.sha256,
            source_attempt_id=source_slot.attempt_id,
            source_terminal_receipt_sha256=source_terminal_receipt_sha256,
            candidate_artifact_sha256=candidate_artifact_sha256,
            outcome="VALID" if valid else "INVALID",
            valid=valid,
            correct=correct,
            raw_score=coverage_row.itt_raw_score if valid else None,
            public_reason_code=(
                "NONE" if valid else str(coverage_row.invalid_reason)
            ),
            structural_signature=structural_signature,
            public_summary=public_summary,
        )


def _verify_adjacent_slots(target: FactorialScoringSlot, source: FactorialScoringSlot) -> None:
    if type(target) is not FactorialScoringSlot or type(source) is not FactorialScoringSlot:
        raise TypeError("exact typed scoring slots are required")
    target_version = _version_number(target.version, "target version")
    source_version = _version_number(source.version, "source version")
    if (
        target.shared_v001
        or target.arm_id != S_REFLECTION_SKILL
        or target_version < 2
        or not target.update_operation_expected
        or source_version != target_version - 1
    ):
        raise ValueError("S Skill target/source round is not adjacent")
    if target_version == 2:
        if not source.shared_v001 or source.arm_id != SHARED_V001_ARM_ID:
            raise ValueError("S v002 must derive from the shared v001 slot")
    elif source.shared_v001 or source.arm_id != S_REFLECTION_SKILL:
        raise ValueError("S v003+ must derive from the prior S slot")
    identity_fields = (
        "factorial_plan_sha256",
        "task_authority_bundle_sha256",
        "factorial_contract_sha256",
        "task_seed_key_sha256",
        "benchmark_id",
        "instance_id",
        "seed",
    )
    if any(getattr(target, name) != getattr(source, name) for name in identity_fields):
        raise ValueError("S Skill source crosses a task, seed, plan, or authority")


def _updater_prompt(
    *,
    target: FactorialScoringSlot,
    source: FactorialScoringSlot,
    public_feedback: SourcePublicFeedback,
    parent_skill_sha256: str,
    frozen_decision_sha256: str,
    frozen_operational_fingerprint: str,
) -> bytes:
    payload = {
        "instruction": (
            "Return exactly one canonical task_local_reflection_skill_v1 JSON object. "
            "Use only the supplied previous-round public feedback. Do not alter Harness architecture."
        ),
        "output_bindings": {
            "arm_id": S_REFLECTION_SKILL,
            "cell_id": target.cell_id,
            "evidence_attempt_ids": [source.attempt_id],
            "frozen_decision_sha256": frozen_decision_sha256,
            "frozen_operational_fingerprint": frozen_operational_fingerprint,
            "instance_id": target.instance_id,
            "parent_skill_sha256": parent_skill_sha256,
            "source_round_sha256": public_feedback.sha256,
            "suite": target.benchmark_id,
            "version": target.version,
        },
        "public_feedback": public_feedback.to_dict(),
        "schema_fields": [
            "schema_version", "record_kind", "cell_id", "suite", "instance_id",
            "arm_id", "version", "parent_skill_sha256", "source_round_sha256",
            "frozen_decision_sha256", "frozen_operational_fingerprint",
            "evidence_attempt_ids", "diagnosis", "preserve", "avoid", "next_actions",
        ],
        "source_slot_sha256": source.sha256,
        "target_slot_sha256": target.sha256,
    }
    return _canonical_bytes(payload)


class FactorialSkillAuthority:
    """Pinned-source trust boundary for zero-call S-arm artifact validation."""

    def __init__(
        self,
        *,
        task_authority: FactorialTaskArtifactAuthority,
        task_authority_bundle: ExactTaskSeedAuthorityBundle,
        plan: FactorialFormalZeroCallPlan,
    ) -> None:
        if type(task_authority) is not FactorialTaskArtifactAuthority:
            raise TypeError("pinned task authority is required")
        self.task_authority = task_authority
        self.bundle = task_authority.verify_exact_bundle(task_authority_bundle)
        self.plan = FactorialFormalZeroCallPlan.from_bytes(
            plan.canonical_bytes,
            task_authority=task_authority,
            task_authority_bundle=self.bundle,
            expected_sha256=plan.sha256,
        )
        self.matrix = ExactFactorialAttemptMatrix.from_verified_sources(
            plan=self.plan,
            bundle=self.bundle,
            task_authority=task_authority,
        )
        self.compiler = FactorialV001FormalCompileOrchestrator(
            task_authority=task_authority,
            task_authority_bundle=self.bundle,
            plan=self.plan,
        )

    def _replay(
        self,
    ) -> tuple[ExactTaskSeedAuthorityBundle, ExactFactorialAttemptMatrix]:
        bundle = self.task_authority.verify_exact_bundle(self.bundle)
        plan = FactorialFormalZeroCallPlan.from_bytes(
            self.plan.canonical_bytes,
            task_authority=self.task_authority,
            task_authority_bundle=bundle,
            expected_sha256=self.plan.sha256,
        )
        matrix = ExactFactorialAttemptMatrix.from_verified_sources(
            plan=plan,
            bundle=bundle,
            task_authority=self.task_authority,
        )
        if bundle != self.bundle or plan != self.plan or matrix != self.matrix:
            raise ValueError("S Skill pinned-source replay differs")
        return bundle, matrix

    def _slots(
        self, *, key: TaskSeedKey, version: str
    ) -> tuple[FactorialScoringSlot, FactorialScoringSlot]:
        bundle, matrix = self._replay()
        verified_key = next(
            (item for item in bundle.task_seed_keys if item.sha256 == key.sha256),
            None,
        )
        if verified_key != key:
            raise ValueError("S Skill key is outside pinned source authority")
        target = tuple(
            item
            for item in matrix.slots
            if item.task_seed_key_sha256 == key.sha256
            and item.arm_id == S_REFLECTION_SKILL
            and item.version == version
        )
        source_version = f"v{_version_number(version, 'target version') - 1:03d}"
        source = tuple(
            item
            for item in matrix.slots
            if item.task_seed_key_sha256 == key.sha256
            and item.version == source_version
            and (
                (version == "v002" and item.shared_v001)
                or (version != "v002" and item.arm_id == S_REFLECTION_SKILL)
            )
        )
        if len(target) != 1 or len(source) != 1:
            raise ValueError("S Skill version is outside the exact formal matrix")
        return target[0], source[0]

    def create_intent(
        self,
        *,
        key: TaskSeedKey,
        version: str,
        source_coverage_row: AttemptCoverageRow,
        source_terminal_receipt_sha256: str,
        candidate_artifact_sha256: str,
        correct: bool | None,
        structural_signature: str,
        public_summary: tuple[str, ...],
        frozen_decision: HarnessDecision,
        v001_compile_result: FactorialV001TrustedCompileResult,
        parent_skill: TaskLocalSkillRecord | None = None,
        parent_update_receipt: SkillUpdateReceipt | None = None,
    ) -> tuple["SReflectionUpdateIntent", SourcePublicFeedback]:
        target, source = self._slots(key=key, version=version)
        if type(source_coverage_row) is not AttemptCoverageRow:
            raise TypeError("typed source coverage row is required")
        source_coverage_row.verify_against_slot(
            matrix_sha256=self.matrix.sha256, slot=source
        )
        trusted_v001 = self.compiler.verify_trusted_result(
            key=key,
            decision=frozen_decision,
            candidate=v001_compile_result,
        )
        frozen_receipt = dict(trusted_v001.arm_compile_receipts)[
            S_REFLECTION_SKILL
        ]
        if (
            frozen_receipt.decision_sha256 != frozen_decision.sha256
            or frozen_receipt.operational_fingerprint
            != frozen_decision.operational_fingerprint
        ):
            raise ValueError("S Skill frozen v001 Harness binding differs")
        feedback = SourcePublicFeedback.from_typed_coverage(
            source_slot=source,
            coverage_row=source_coverage_row,
            source_terminal_receipt_sha256=source_terminal_receipt_sha256,
            candidate_artifact_sha256=candidate_artifact_sha256,
            correct=correct,
            structural_signature=structural_signature,
            public_summary=public_summary,
        )
        intent = SReflectionUpdateIntent.create(
            target_slot=target,
            source_slot=source,
            exact_matrix_sha256=self.matrix.sha256,
            expected_factorial_plan_sha256=self.plan.sha256,
            expected_task_authority_bundle_sha256=self.bundle.sha256,
            source_terminal_receipt_sha256=source_terminal_receipt_sha256,
            public_feedback=feedback,
            frozen_decision=frozen_decision,
            parent_skill=parent_skill,
            parent_update_receipt=parent_update_receipt,
        )
        return intent, feedback

    def verify_frozen_compile_for_solution(
        self,
        *,
        intent: "SReflectionUpdateIntent",
        context: HarnessContext,
        frozen_decision: HarnessDecision,
        v001_compile_result: FactorialV001TrustedCompileResult,
        prior_compile_receipts: Sequence[HarnessCompileReceipt],
    ) -> tuple[str, HarnessCompileReceipt]:
        """Recompile the exact frozen v001 Harness in the target-round context."""

        bundle, matrix = self._replay()
        slot = next(
            (item for item in matrix.slots if item.sha256 == intent.target_slot_sha256),
            None,
        )
        key = next(
            (
                item
                for item in bundle.task_seed_keys
                if item.sha256 == intent.task_seed_key_sha256
            ),
            None,
        )
        if slot is None or key is None:
            raise ValueError("S Skill prompt intent is outside exact authority")
        trusted_v001 = self.compiler.verify_trusted_result(
            key=key,
            decision=frozen_decision,
            candidate=v001_compile_result,
        )
        prior = tuple(prior_compile_receipts)
        if not prior or any(
            type(item) is not HarnessCompileReceipt for item in prior
        ):
            raise TypeError("typed frozen S-arm compile lineage is required")
        v001_receipt = dict(trusted_v001.arm_compile_receipts)[
            S_REFLECTION_SKILL
        ]
        expected_versions = tuple(
            f"v{index:03d}"
            for index in range(1, _version_number(intent.version, "intent version"))
        )
        if (
            tuple(item.version for item in prior) != expected_versions
            or prior[0] != v001_receipt
            or any(
                item.cell_id != intent.cell_id
                or item.suite != intent.benchmark_id
                or item.instance_id != intent.instance_id
                or item.variant_id != S_REFLECTION_SKILL
                or item.adaptation_policy != "conditional_any_v1"
                or item.decision_sha256 != frozen_decision.sha256
                or item.operational_fingerprint
                != frozen_decision.operational_fingerprint
                or (
                    index > 0
                    and item.previous_receipt_sha256 != prior[index - 1].sha256
                )
                for index, item in enumerate(prior)
            )
        ):
            raise ValueError("S Skill frozen compile lineage differs")
        source_context = self.task_authority.derived_contexts()[
            (intent.benchmark_id, intent.instance_id)
        ]
        if (
            type(context) is not HarnessContext
            or context.instance_id != source_context.instance_id
            or context.suite != source_context.suite
            or context.task_card != source_context.task_card
            or context.reference_artifact_id != source_context.reference_artifact_id
            or context.reference_artifact != source_context.reference_artifact
            or context.public_observations != source_context.public_observations
            or context.round_index != _version_number(intent.version, "intent version")
            or context.cross_instance_records
            or context.cross_instance_memory_grant is not None
            or context.stream_index is not None
            or context.builder_meta_prior is not None
        ):
            raise ValueError("S Skill target-round Harness context differs")
        compiled = self.compiler.operator_registry.compile(
            frozen_decision,
            variant=self.compiler.variants[S_REFLECTION_SKILL],
            context=context,
            previous_decision=frozen_decision,
        )
        if (
            frozen_axis_projection(frozen_decision)
            != frozen_axis_projection(
                HarnessDecision.from_dict(asdict(frozen_decision))
            )
            or compiled.decision_sha256 != v001_receipt.decision_sha256
            or compiled.operational_fingerprint
            != v001_receipt.operational_fingerprint
        ):
            raise ValueError("S Skill Harness architecture is not frozen to v001")
        target_receipt = HarnessCompileReceipt.create(
            cell_id=intent.cell_id,
            suite=intent.benchmark_id,
            instance_id=intent.instance_id,
            variant_id=S_REFLECTION_SKILL,
            version=intent.version,
            adaptation_policy="conditional_any_v1",
            previous_receipt_sha256=prior[-1].sha256,
            previous_decision_sha256=frozen_decision.sha256,
            compiled=compiled,
            decision=frozen_decision,
            previous_decision=frozen_decision,
        )
        if any(target_receipt.change_map.values()):
            raise ValueError("S Skill target compile changed a frozen Harness axis")
        return compiled.solution_prompt, target_receipt


@dataclass(frozen=True)
class SReflectionUpdateIntent(_ContentAddressed):
    factorial_plan_sha256: str
    exact_matrix_sha256: str
    task_authority_bundle_sha256: str
    factorial_contract_sha256: str
    target_slot_sha256: str
    source_slot_sha256: str
    task_seed_key_sha256: str
    benchmark_id: str
    instance_id: str
    seed: int
    cell_id: str
    version: str
    source_version: str
    source_attempt_id: str
    source_terminal_receipt_sha256: str
    public_input_projection_sha256: str
    update_operation_id: str
    parent_skill_sha256: str
    parent_update_receipt_sha256: str
    frozen_decision_sha256: str
    frozen_operational_fingerprint: str
    frozen_axis_projection_sha256: str
    updater_prompt_sha256: str

    def __post_init__(self) -> None:
        for value, label, allow_zero in (
            (self.factorial_plan_sha256, "factorial plan sha256", False),
            (self.exact_matrix_sha256, "exact matrix sha256", False),
            (self.task_authority_bundle_sha256, "authority bundle sha256", False),
            (self.factorial_contract_sha256, "factorial contract sha256", False),
            (self.target_slot_sha256, "target slot sha256", False),
            (self.source_slot_sha256, "source slot sha256", False),
            (self.task_seed_key_sha256, "task/seed key sha256", False),
            (self.source_terminal_receipt_sha256, "source terminal receipt sha256", False),
            (self.public_input_projection_sha256, "public projection sha256", False),
            (self.parent_skill_sha256, "parent Skill sha256", True),
            (self.parent_update_receipt_sha256, "parent update receipt sha256", True),
            (self.frozen_decision_sha256, "frozen decision sha256", False),
            (self.frozen_operational_fingerprint, "frozen fingerprint", False),
            (self.frozen_axis_projection_sha256, "frozen axis projection sha256", False),
            (self.updater_prompt_sha256, "updater prompt sha256", False),
        ):
            _sha(value, label, allow_zero=allow_zero)
        for value, label in (
            (self.benchmark_id, "benchmark id"),
            (self.instance_id, "instance id"),
            (self.cell_id, "cell id"),
            (self.version, "version"),
            (self.source_version, "source version"),
            (self.source_attempt_id, "source attempt id"),
            (self.update_operation_id, "update operation id"),
        ):
            _safe(value, label)
        if type(self.seed) is not int or self.seed < 0:
            raise ValueError("S Skill seed differs")
        version_number = _version_number(self.version, "version")
        if version_number < 2 or _version_number(self.source_version, "source version") != version_number - 1:
            raise ValueError("S Skill intent versions are not adjacent")
        expected_prefix = f"factorial-round:{self.task_seed_key_sha256}:{S_REFLECTION_SKILL}:{self.version}"
        if (
            self.cell_id != f"factorial-cell:{self.task_seed_key_sha256}:{S_REFLECTION_SKILL}"
            or self.update_operation_id != expected_prefix + ":update"
        ):
            raise ValueError("S Skill intent operation identity differs")
        genesis = version_number == 2
        if genesis != (
            self.parent_skill_sha256 == ZERO_SHA256
            and self.parent_update_receipt_sha256 == ZERO_SHA256
        ):
            raise ValueError("S Skill genesis/parent binding differs")

    @classmethod
    def create(
        cls,
        *,
        target_slot: FactorialScoringSlot,
        source_slot: FactorialScoringSlot,
        exact_matrix_sha256: str,
        expected_factorial_plan_sha256: str,
        expected_task_authority_bundle_sha256: str,
        source_terminal_receipt_sha256: str,
        public_feedback: SourcePublicFeedback,
        frozen_decision: HarnessDecision,
        parent_skill: TaskLocalSkillRecord | None = None,
        parent_update_receipt: SkillUpdateReceipt | None = None,
    ) -> "SReflectionUpdateIntent":
        _verify_adjacent_slots(target_slot, source_slot)
        _sha(exact_matrix_sha256, "exact matrix sha256")
        if (
            target_slot.factorial_plan_sha256 != expected_factorial_plan_sha256
            or target_slot.task_authority_bundle_sha256
            != expected_task_authority_bundle_sha256
        ):
            raise ValueError("S Skill exact plan/authority binding differs")
        _sha(source_terminal_receipt_sha256, "source terminal receipt sha256")
        if type(public_feedback) is not SourcePublicFeedback or (
            public_feedback.source_slot_sha256 != source_slot.sha256
            or public_feedback.source_attempt_id != source_slot.attempt_id
            or public_feedback.source_terminal_receipt_sha256
            != source_terminal_receipt_sha256
        ):
            raise ValueError("S Skill public feedback/source binding differs")
        if type(frozen_decision) is not HarnessDecision:
            raise TypeError("exact frozen decision is required")
        version_number = _version_number(target_slot.version, "target version")
        if version_number == 2:
            if parent_skill is not None or parent_update_receipt is not None:
                raise ValueError("S v002 is the zero-parent genesis")
            parent_skill_sha = parent_receipt_sha = ZERO_SHA256
        else:
            if type(parent_skill) is not TaskLocalSkillRecord or type(
                parent_update_receipt
            ) is not SkillUpdateReceipt:
                raise ValueError("S v003+ requires the immediately prior typed parent")
            if (
                parent_skill.version != source_slot.version
                or parent_skill.cell_id != target_slot.cell_id
                or parent_skill.suite != target_slot.benchmark_id
                or parent_skill.instance_id != target_slot.instance_id
                or parent_skill.frozen_decision_sha256 != frozen_decision.sha256
                or parent_skill.frozen_operational_fingerprint
                != frozen_decision.operational_fingerprint
                or parent_update_receipt.version != source_slot.version
                or parent_update_receipt.cell_id != target_slot.cell_id
                or parent_update_receipt.skill_sha256 != parent_skill.sha256
                or parent_update_receipt.operation_id != source_slot.update_operation_id
                or parent_update_receipt.frozen_decision_sha256
                != frozen_decision.sha256
                or parent_update_receipt.frozen_operational_fingerprint
                != frozen_decision.operational_fingerprint
            ):
                raise ValueError("S Skill parent is not the prior task/seed round")
            parent_skill_sha = parent_skill.sha256
            parent_receipt_sha = parent_update_receipt.sha256
        axis_projection_sha = _digest(frozen_axis_projection(frozen_decision))
        prompt = _updater_prompt(
            target=target_slot,
            source=source_slot,
            public_feedback=public_feedback,
            parent_skill_sha256=parent_skill_sha,
            frozen_decision_sha256=frozen_decision.sha256,
            frozen_operational_fingerprint=frozen_decision.operational_fingerprint,
        )
        return cls(
            factorial_plan_sha256=target_slot.factorial_plan_sha256,
            exact_matrix_sha256=exact_matrix_sha256,
            task_authority_bundle_sha256=target_slot.task_authority_bundle_sha256,
            factorial_contract_sha256=target_slot.factorial_contract_sha256,
            target_slot_sha256=target_slot.sha256,
            source_slot_sha256=source_slot.sha256,
            task_seed_key_sha256=target_slot.task_seed_key_sha256,
            benchmark_id=target_slot.benchmark_id,
            instance_id=target_slot.instance_id,
            seed=target_slot.seed,
            cell_id=target_slot.cell_id,
            version=target_slot.version,
            source_version=source_slot.version,
            source_attempt_id=source_slot.attempt_id,
            source_terminal_receipt_sha256=source_terminal_receipt_sha256,
            public_input_projection_sha256=public_feedback.sha256,
            update_operation_id=target_slot.update_operation_id,
            parent_skill_sha256=parent_skill_sha,
            parent_update_receipt_sha256=parent_receipt_sha,
            frozen_decision_sha256=frozen_decision.sha256,
            frozen_operational_fingerprint=frozen_decision.operational_fingerprint,
            frozen_axis_projection_sha256=axis_projection_sha,
            updater_prompt_sha256=hashlib.sha256(prompt).hexdigest(),
        )

    @classmethod
    def from_bytes(cls, encoded: bytes, *, expected_sha256: str) -> "SReflectionUpdateIntent":
        return _decode_content(cls, encoded, expected_sha256)

    def verify_exact_replay(self, **create_arguments: Any) -> None:
        expected = type(self).create(**create_arguments)
        if self != expected or self.canonical_bytes != expected.canonical_bytes:
            raise ValueError("S Skill intent differs from exact-slot replay")


def accept_skill_update(
    *,
    intent: SReflectionUpdateIntent,
    raw_skill: bytes,
    operation_result_artifact_sha256: str,
    prior_skills: Sequence[TaskLocalSkillRecord] = (),
) -> tuple[TaskLocalSkillRecord, SkillUpdateReceipt]:
    """Validate an already-produced result; never invokes an updater/provider."""

    if type(intent) is not SReflectionUpdateIntent:
        raise TypeError("typed S Skill intent is required")
    prior = tuple(prior_skills)
    if any(type(item) is not TaskLocalSkillRecord for item in prior):
        raise TypeError("typed prior Skills are required")
    target_number = _version_number(intent.version, "intent version")
    if len(prior) != target_number - 2 or any(
        item.version != f"v{index + 2:03d}"
        or item.cell_id != intent.cell_id
        or item.suite != intent.benchmark_id
        or item.instance_id != intent.instance_id
        or item.parent_skill_sha256
        != (ZERO_SHA256 if index == 0 else prior[index - 1].sha256)
        for index, item in enumerate(prior)
    ) or (prior and prior[-1].sha256 != intent.parent_skill_sha256):
        raise ValueError("S Skill lineage does not match the intent parent")
    skill = TaskLocalSkillRecord.from_bytes(
        raw_skill,
        expected_cell_id=intent.cell_id,
        expected_suite=intent.benchmark_id,
        expected_instance_id=intent.instance_id,
        expected_version=intent.version,
        expected_parent_skill_sha256=intent.parent_skill_sha256,
        expected_source_version=intent.source_version,
        expected_source_round_sha256=intent.public_input_projection_sha256,
        expected_frozen_decision_sha256=intent.frozen_decision_sha256,
        expected_frozen_operational_fingerprint=intent.frozen_operational_fingerprint,
        expected_source_attempt_id=intent.source_attempt_id,
        sealed_attempt_ids={intent.source_attempt_id},
    )
    if skill.evidence_attempt_ids != (intent.source_attempt_id,):
        raise ValueError("formal S Skill must cite exactly the adjacent source attempt")
    receipt = SkillUpdateReceipt.create(
        skill=skill,
        operation_id=intent.update_operation_id,
        operation_result_artifact_sha256=operation_result_artifact_sha256,
        updater_prompt_sha256=intent.updater_prompt_sha256,
        public_input_projection_sha256=intent.public_input_projection_sha256,
        prior_skill_sha256s=tuple(item.sha256 for item in prior),
    )
    return skill, receipt


def compose_solution_prompt(base_solution_prompt: str, skill: TaskLocalSkillRecord) -> str:
    if not isinstance(base_solution_prompt, str) or not base_solution_prompt.strip() or "\x00" in base_solution_prompt:
        raise ValueError("base solution prompt differs")
    projection = solver_skill_projection(skill)
    encoded = _canonical_bytes(projection).decode("utf-8").rstrip("\n")
    return (
        base_solution_prompt.rstrip()
        + "\n\nTASK-LOCAL REFLECTION SKILL (advisory; Harness architecture is frozen):\n"
        + encoded
        + "\n"
    )


@dataclass(frozen=True)
class SReflectionSolutionPromptReceipt(_ContentAddressed):
    intent_sha256: str
    target_slot_sha256: str
    task_seed_key_sha256: str
    version: str
    trusted_compile_receipt_sha256: str
    frozen_decision_sha256: str
    frozen_operational_fingerprint: str
    frozen_axis_projection_sha256: str
    skill_sha256: str
    skill_update_receipt_sha256: str
    base_solution_prompt_sha256: str
    solver_skill_projection_sha256: str
    final_solution_prompt_sha256: str

    def __post_init__(self) -> None:
        for field_name, value in asdict(self).items():
            if field_name == "version":
                _safe(value, "prompt receipt version")
            else:
                _sha(value, field_name)
        if _version_number(self.version, "prompt receipt version") < 2:
            raise ValueError("S prompt receipts start after v001")

    @classmethod
    def create(
        cls,
        *,
        intent: SReflectionUpdateIntent,
        skill: TaskLocalSkillRecord,
        skill_update_receipt: SkillUpdateReceipt,
        authority: FactorialSkillAuthority,
        context: HarnessContext,
        frozen_decision: HarnessDecision,
        v001_compile_result: FactorialV001TrustedCompileResult,
        prior_compile_receipts: Sequence[HarnessCompileReceipt],
        base_solution_prompt: str,
    ) -> "SReflectionSolutionPromptReceipt":
        if type(intent) is not SReflectionUpdateIntent or type(skill) is not TaskLocalSkillRecord or type(
            skill_update_receipt
        ) is not SkillUpdateReceipt:
            raise TypeError("typed S prompt inputs are required")
        if (
            skill.sha256 != skill_update_receipt.skill_sha256
            or skill.version != intent.version
            or skill_update_receipt.version != intent.version
            or skill_update_receipt.operation_id != intent.update_operation_id
            or skill_update_receipt.updater_prompt_sha256 != intent.updater_prompt_sha256
            or skill_update_receipt.public_input_projection_sha256
            != intent.public_input_projection_sha256
            or skill.frozen_decision_sha256 != intent.frozen_decision_sha256
            or skill.frozen_operational_fingerprint
            != intent.frozen_operational_fingerprint
        ):
            raise ValueError("S prompt Skill/update/intent binding differs")
        if type(authority) is not FactorialSkillAuthority:
            raise TypeError("pinned S Skill authority is required")
        trusted_base_prompt, trusted_compile_receipt = (
            authority.verify_frozen_compile_for_solution(
                intent=intent,
                context=context,
                frozen_decision=frozen_decision,
                v001_compile_result=v001_compile_result,
                prior_compile_receipts=prior_compile_receipts,
            )
        )
        if base_solution_prompt != trusted_base_prompt:
            raise ValueError("S prompt base differs from trusted frozen compilation")
        projection = solver_skill_projection(skill)
        final_prompt = compose_solution_prompt(base_solution_prompt, skill)
        return cls(
            intent_sha256=intent.sha256,
            target_slot_sha256=intent.target_slot_sha256,
            task_seed_key_sha256=intent.task_seed_key_sha256,
            version=intent.version,
            trusted_compile_receipt_sha256=trusted_compile_receipt.sha256,
            frozen_decision_sha256=intent.frozen_decision_sha256,
            frozen_operational_fingerprint=intent.frozen_operational_fingerprint,
            frozen_axis_projection_sha256=intent.frozen_axis_projection_sha256,
            skill_sha256=skill.sha256,
            skill_update_receipt_sha256=skill_update_receipt.sha256,
            base_solution_prompt_sha256=hashlib.sha256(base_solution_prompt.encode()).hexdigest(),
            solver_skill_projection_sha256=_digest(projection),
            final_solution_prompt_sha256=hashlib.sha256(final_prompt.encode()).hexdigest(),
        )

    @classmethod
    def from_bytes(cls, encoded: bytes, *, expected_sha256: str) -> "SReflectionSolutionPromptReceipt":
        return _decode_content(cls, encoded, expected_sha256)


__all__ = [
    "EXECUTION_AUTHORITY",
    "FactorialSkillAuthority",
    "SReflectionSolutionPromptReceipt",
    "SReflectionUpdateIntent",
    "SourcePublicFeedback",
    "accept_skill_update",
    "compose_solution_prompt",
    "frozen_axis_projection",
]
