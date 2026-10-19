"""Pure policy checks for the four-arm wide-Harness factorial experiment.

This module is deliberately side-effect free.  It neither calls a model nor
reads or writes artifacts.  The formal orchestrator may use it to validate an
already parsed Harness transition and to parse the task-local reflection Skill
used by the ``S-reflection-skill`` control arm.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from types import MappingProxyType
from typing import Any, Collection, Mapping, Sequence

from .schema import HarnessDecision


A_FIXED_FEEDBACK = "A-fixed-feedback"
S_REFLECTION_SKILL = "S-reflection-skill"
B_TARGETED = "B-targeted"
B_FROZEN_WIDE = "B-frozen-wide"
ARM_IDS = (
    A_FIXED_FEEDBACK,
    S_REFLECTION_SKILL,
    B_TARGETED,
    B_FROZEN_WIDE,
)
HARNESS_AXES = (
    "role_graph",
    "memory_views",
    "tools",
    "parent_strategy",
    "workflow",
    "scheduler_mode",
    "recovery_mode",
)

_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_VERSION = re.compile(r"v(\d{3})")
_PRIVATE_TEXT = re.compile(
    r"(?:/home/|/root/|/data\d*/|file://|"
    r"(?:^|[^A-Za-z0-9])(?:private(?:[_ -](?:path|log|evaluator))?|"
    r"secret|token|hidden[_ -]?evidence)(?:$|[^A-Za-z0-9]))",
    re.IGNORECASE,
)
_MAX_SKILL_BYTES = 16 * 1024
_SKILL_FIELDS = frozenset(
    {
        "schema_version",
        "record_kind",
        "cell_id",
        "suite",
        "instance_id",
        "arm_id",
        "version",
        "parent_skill_sha256",
        "source_round_sha256",
        "frozen_decision_sha256",
        "frozen_operational_fingerprint",
        "evidence_attempt_ids",
        "diagnosis",
        "preserve",
        "avoid",
        "next_actions",
    }
)
_SKILL_RECEIPT_FIELDS = frozenset(
    {
        "schema_version",
        "cell_id",
        "suite",
        "instance_id",
        "arm_id",
        "version",
        "operation_id",
        "operation_result_artifact_sha256",
        "updater_prompt_sha256",
        "public_input_projection_sha256",
        "parent_skill_sha256",
        "source_round_sha256",
        "frozen_decision_sha256",
        "frozen_operational_fingerprint",
        "skill_sha256",
        "skill_lineage_prefix_sha256",
    }
)


def _reject_json_constant(value: str) -> None:
    raise ValueError(f"JSON contains forbidden constant {value}")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"JSON repeats field {key!r}")
        result[key] = value
    return result


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
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
        raise ValueError("payload is not canonical JSON") from exc


# The first post-v001 Skill has no predecessor.  A literal zero digest makes
# that absence unambiguous; it is not the digest of a synthetic Skill object.
EMPTY_TASK_LOCAL_SKILL_SHA256 = "0" * 64


def _parse_canonical_object(raw: bytes, *, label: str, maximum: int) -> dict[str, Any]:
    if not isinstance(raw, bytes) or not raw or len(raw) > maximum:
        raise ValueError(f"{label} byte length is invalid")
    try:
        payload = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_json_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} is not strict UTF-8 JSON") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{label} must be an object")
    if _canonical_bytes(payload) != raw:
        raise ValueError(f"{label} bytes are not canonical")
    return payload


def _require_exact_fields(
    payload: Mapping[str, Any], expected: frozenset[str], label: str
) -> None:
    actual = frozenset(payload)
    if actual != expected:
        raise ValueError(
            f"{label} fields differ: missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}"
        )


def _safe_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise ValueError(f"unsafe {label}")
    if _PRIVATE_TEXT.search(value):
        raise ValueError(f"{label} contains private, secret, or hidden evidence text")
    return value


def _sha(value: Any, label: str, *, allow_zero: bool = True) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"invalid {label}")
    if not allow_zero and value == EMPTY_TASK_LOCAL_SKILL_SHA256:
        raise ValueError(f"empty {label}")
    return value


def _version_number(value: Any, label: str) -> int:
    if not isinstance(value, str):
        raise ValueError(f"invalid {label}")
    match = _VERSION.fullmatch(value)
    if match is None:
        raise ValueError(f"invalid {label}")
    number = int(match.group(1))
    if not 1 <= number <= 999:
        raise ValueError(f"invalid {label}")
    return number


def _text_items(value: Any, label: str) -> tuple[str, ...]:
    if not isinstance(value, list) or len(value) > 8:
        raise ValueError(f"{label} must be an array with at most eight items")
    result: list[str] = []
    for item in value:
        if (
            not isinstance(item, str)
            or not item.strip()
            or len(item) > 512
            or "\x00" in item
        ):
            raise ValueError(f"{label} contains empty, NUL, or overlong text")
        if _PRIVATE_TEXT.search(item):
            raise ValueError(f"{label} contains private, secret, or hidden evidence text")
        result.append(item)
    return tuple(result)


def _id_array(value: Any, label: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not 1 <= len(value) <= 64:
        raise ValueError(f"{label} must be a non-empty bounded array")
    result = tuple(_safe_id(item, label) for item in value)
    if len(result) != len(set(result)):
        raise ValueError(f"{label} contains duplicates")
    return result


@dataclass(frozen=True)
class ArmPolicySpec:
    arm_id: str
    update_policy: str
    architecture_frozen: bool
    update_kind: str
    minimum_material_axis_changes: int
    require_lineage_unique: bool

    def __post_init__(self) -> None:
        if self.arm_id not in ARM_IDS:
            raise ValueError("unknown factorial arm id")
        _safe_id(self.update_policy, "arm update policy")
        if self.update_kind not in {"none", "reflection_skill", "harness_builder"}:
            raise ValueError("unknown factorial update kind")
        if self.minimum_material_axis_changes not in {0, 1, 7}:
            raise ValueError("invalid minimum Harness-axis change count")


ARM_POLICY_SPECS: Mapping[str, ArmPolicySpec] = MappingProxyType(
    {
        A_FIXED_FEEDBACK: ArmPolicySpec(
            A_FIXED_FEEDBACK, "fixed_feedback_v1", True, "none", 0, False
        ),
        S_REFLECTION_SKILL: ArmPolicySpec(
            S_REFLECTION_SKILL,
            "reflection_skill_only_v1",
            True,
            "reflection_skill",
            0,
            False,
        ),
        B_TARGETED: ArmPolicySpec(
            B_TARGETED,
            "targeted_any_change_v1",
            False,
            "harness_builder",
            1,
            False,
        ),
        B_FROZEN_WIDE: ArmPolicySpec(
            B_FROZEN_WIDE,
            "wide_all_fields_recompile_v1",
            False,
            "harness_builder",
            7,
            True,
        ),
    }
)


def resolve_arm_policy(policy: str | ArmPolicySpec) -> ArmPolicySpec:
    if isinstance(policy, ArmPolicySpec):
        canonical = ARM_POLICY_SPECS.get(policy.arm_id)
        if canonical != policy:
            raise ValueError("factorial arm policy differs from the frozen policy")
        return policy
    if not isinstance(policy, str):
        raise ValueError("factorial arm policy must be an id or ArmPolicySpec")
    if policy in ARM_POLICY_SPECS:
        return ARM_POLICY_SPECS[policy]
    for spec in ARM_POLICY_SPECS.values():
        if policy == spec.update_policy:
            return spec
    raise ValueError("unknown factorial arm policy")


def _lineage_fingerprints(
    lineage: Sequence[HarnessDecision | str],
) -> tuple[str, ...]:
    if not isinstance(lineage, Sequence) or isinstance(lineage, (str, bytes)):
        raise ValueError("Harness lineage must be a sequence")
    values: list[str] = []
    for item in lineage:
        if isinstance(item, HarnessDecision):
            values.append(item.operational_fingerprint)
        else:
            values.append(_sha(item, "Harness lineage operational fingerprint"))
    return tuple(values)


def validate_arm_transition(
    policy: str | ArmPolicySpec,
    previous: HarnessDecision,
    current: HarnessDecision,
    lineage: Sequence[HarnessDecision | str] = (),
) -> dict[str, bool]:
    """Validate one accepted post-v001 transition under a frozen arm policy.

    ``lineage`` is the prefix *before* ``current``.  Role, memory, and tool
    collections are memberships, so reordering them cannot satisfy either
    structural arm.  Workflow order remains executable and therefore counts.
    """

    spec = resolve_arm_policy(policy)
    if not isinstance(previous, HarnessDecision) or not isinstance(
        current, HarnessDecision
    ):
        raise ValueError("Harness transition requires typed decisions")
    change_map = current.operational_change_map_from(previous)
    if tuple(change_map) != HARNESS_AXES:
        raise ValueError("Harness transition axis coverage differs")
    if spec.architecture_frozen:
        if current.sha256 != previous.sha256:
            raise ValueError(f"{spec.arm_id} must keep the frozen Harness decision")
        return change_map
    changed = sum(change_map.values())
    if changed < spec.minimum_material_axis_changes:
        raise ValueError(
            f"{spec.arm_id} requires at least "
            f"{spec.minimum_material_axis_changes} material Harness-axis changes"
        )
    fingerprints = _lineage_fingerprints(lineage)
    if spec.require_lineage_unique:
        if not fingerprints or fingerprints[-1] != previous.operational_fingerprint:
            raise ValueError("wide Harness lineage is not bound to the previous decision")
        if len(fingerprints) != len(set(fingerprints)):
            raise ValueError("wide Harness lineage already reuses a fingerprint")
        if current.operational_fingerprint in fingerprints:
            raise ValueError("wide Harness transition reuses a lineage fingerprint")
    return change_map


@dataclass(frozen=True)
class TaskLocalSkillRecord:
    schema_version: int
    record_kind: str
    cell_id: str
    suite: str
    instance_id: str
    arm_id: str
    version: str
    parent_skill_sha256: str
    source_round_sha256: str
    frozen_decision_sha256: str
    frozen_operational_fingerprint: str
    evidence_attempt_ids: tuple[str, ...]
    diagnosis: tuple[str, ...]
    preserve: tuple[str, ...]
    avoid: tuple[str, ...]
    next_actions: tuple[str, ...]

    def __post_init__(self) -> None:
        if (
            type(self.schema_version) is not int
            or self.schema_version != 1
            or self.record_kind != "task_local_reflection_skill_v1"
        ):
            raise ValueError("unsupported task-local Skill schema or kind")
        for value, label in (
            (self.cell_id, "Skill cell id"),
            (self.suite, "Skill suite"),
            (self.instance_id, "Skill instance id"),
            (self.version, "Skill version"),
        ):
            _safe_id(value, label)
        if self.arm_id != S_REFLECTION_SKILL:
            raise ValueError("task-local Skill belongs only to S-reflection-skill")
        if _version_number(self.version, "Skill version") < 2:
            raise ValueError("task-local Skill updates start after v001")
        _sha(self.parent_skill_sha256, "parent Skill sha256")
        for value, label in (
            (self.source_round_sha256, "source round sha256"),
            (self.frozen_decision_sha256, "frozen decision sha256"),
            (
                self.frozen_operational_fingerprint,
                "frozen operational fingerprint",
            ),
        ):
            _sha(value, label, allow_zero=False)
        if (
            not isinstance(self.evidence_attempt_ids, tuple)
            or not 1 <= len(self.evidence_attempt_ids) <= 64
            or len(self.evidence_attempt_ids) != len(set(self.evidence_attempt_ids))
        ):
            raise ValueError("Skill evidence attempt ids differ")
        for attempt_id in self.evidence_attempt_ids:
            _safe_id(attempt_id, "Skill evidence attempt id")
        text_fields = (self.diagnosis, self.preserve, self.avoid, self.next_actions)
        if any(not isinstance(items, tuple) or len(items) > 8 for items in text_fields):
            raise ValueError("Skill text arrays differ")
        if sum(len(items) for items in text_fields) < 1:
            raise ValueError("task-local Skill must contain at least one text item")
        for field_name, items in zip(
            ("diagnosis", "preserve", "avoid", "next actions"), text_fields
        ):
            for item in items:
                if (
                    not isinstance(item, str)
                    or not item.strip()
                    or len(item) > 512
                    or "\x00" in item
                    or _PRIVATE_TEXT.search(item)
                ):
                    raise ValueError(f"Skill {field_name} contains unsafe text")
        if len(self.canonical_bytes) > _MAX_SKILL_BYTES:
            raise ValueError("task-local Skill exceeds 16 KiB")

    @classmethod
    def from_bytes(
        cls,
        raw: bytes,
        *,
        expected_cell_id: str,
        expected_suite: str,
        expected_instance_id: str,
        expected_version: str,
        expected_parent_skill_sha256: str,
        expected_source_version: str,
        expected_source_round_sha256: str,
        expected_frozen_decision_sha256: str,
        expected_frozen_operational_fingerprint: str,
        expected_source_attempt_id: str,
        sealed_attempt_ids: Collection[str],
    ) -> "TaskLocalSkillRecord":
        payload = _parse_canonical_object(
            raw, label="task-local Skill", maximum=_MAX_SKILL_BYTES
        )
        _require_exact_fields(payload, _SKILL_FIELDS, "task-local Skill")
        text = {
            name: _text_items(payload[name], f"Skill {name}")
            for name in ("diagnosis", "preserve", "avoid", "next_actions")
        }
        item = cls(
            schema_version=payload["schema_version"],
            record_kind=payload["record_kind"],
            cell_id=payload["cell_id"],
            suite=payload["suite"],
            instance_id=payload["instance_id"],
            arm_id=payload["arm_id"],
            version=payload["version"],
            parent_skill_sha256=payload["parent_skill_sha256"],
            source_round_sha256=payload["source_round_sha256"],
            frozen_decision_sha256=payload["frozen_decision_sha256"],
            frozen_operational_fingerprint=payload[
                "frozen_operational_fingerprint"
            ],
            evidence_attempt_ids=_id_array(
                payload["evidence_attempt_ids"], "Skill evidence attempt id"
            ),
            diagnosis=text["diagnosis"],
            preserve=text["preserve"],
            avoid=text["avoid"],
            next_actions=text["next_actions"],
        )
        expected_bindings = {
            "cell_id": expected_cell_id,
            "suite": expected_suite,
            "instance_id": expected_instance_id,
            "version": expected_version,
            "parent_skill_sha256": expected_parent_skill_sha256,
            "source_round_sha256": expected_source_round_sha256,
            "frozen_decision_sha256": expected_frozen_decision_sha256,
            "frozen_operational_fingerprint": expected_frozen_operational_fingerprint,
        }
        for field_name, expected in expected_bindings.items():
            if getattr(item, field_name) != expected:
                raise ValueError(f"task-local Skill {field_name} binding differs")
        if _version_number(item.version, "Skill version") != _version_number(
            expected_source_version, "source version"
        ) + 1:
            raise ValueError("task-local Skill source round is not immediately prior")
        sealed = frozenset(sealed_attempt_ids)
        if (
            not sealed
            or _safe_id(expected_source_attempt_id, "source attempt id")
            not in item.evidence_attempt_ids
            or not set(item.evidence_attempt_ids) <= sealed
        ):
            raise ValueError("task-local Skill cites an unsealed evidence attempt")
        return item

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        for name in (
            "evidence_attempt_ids",
            "diagnosis",
            "preserve",
            "avoid",
            "next_actions",
        ):
            payload[name] = list(payload[name])
        return payload

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


def solver_skill_projection(skill: TaskLocalSkillRecord | None) -> dict[str, Any]:
    """Return the only Skill fields visible to the S-arm solution call."""

    if skill is None:
        return {
            "skill_kind": "NONE",
            "skill_sha256": None,
            "diagnosis": [],
            "preserve": [],
            "avoid": [],
            "next_actions": [],
        }
    if not isinstance(skill, TaskLocalSkillRecord):
        raise ValueError("solver Skill projection requires a typed task-local Skill")
    return {
        "skill_kind": skill.record_kind,
        "skill_sha256": skill.sha256,
        "diagnosis": list(skill.diagnosis),
        "preserve": list(skill.preserve),
        "avoid": list(skill.avoid),
        "next_actions": list(skill.next_actions),
    }


@dataclass(frozen=True)
class SkillUpdateReceipt:
    schema_version: int
    cell_id: str
    suite: str
    instance_id: str
    arm_id: str
    version: str
    operation_id: str
    operation_result_artifact_sha256: str
    updater_prompt_sha256: str
    public_input_projection_sha256: str
    parent_skill_sha256: str
    source_round_sha256: str
    frozen_decision_sha256: str
    frozen_operational_fingerprint: str
    skill_sha256: str
    skill_lineage_prefix_sha256: str

    def __post_init__(self) -> None:
        if (
            type(self.schema_version) is not int
            or self.schema_version != 1
            or self.arm_id != S_REFLECTION_SKILL
        ):
            raise ValueError("unsupported Skill update receipt schema or arm")
        for value, label in (
            (self.cell_id, "Skill receipt cell id"),
            (self.suite, "Skill receipt suite"),
            (self.instance_id, "Skill receipt instance id"),
            (self.version, "Skill receipt version"),
            (self.operation_id, "Skill receipt operation id"),
        ):
            _safe_id(value, label)
        if _version_number(self.version, "Skill receipt version") < 2:
            raise ValueError("Skill update receipts start after v001")
        for value, label in (
            (
                self.operation_result_artifact_sha256,
                "operation result artifact sha256",
            ),
            (self.updater_prompt_sha256, "updater prompt sha256"),
            (
                self.public_input_projection_sha256,
                "public input projection sha256",
            ),
            (self.source_round_sha256, "source round sha256"),
            (self.frozen_decision_sha256, "frozen decision sha256"),
            (
                self.frozen_operational_fingerprint,
                "frozen operational fingerprint",
            ),
            (self.skill_sha256, "Skill sha256"),
            (self.skill_lineage_prefix_sha256, "Skill lineage prefix sha256"),
        ):
            _sha(value, label, allow_zero=False)
        _sha(self.parent_skill_sha256, "parent Skill sha256")

    @classmethod
    def create(
        cls,
        *,
        skill: TaskLocalSkillRecord,
        operation_id: str,
        operation_result_artifact_sha256: str,
        updater_prompt_sha256: str,
        public_input_projection_sha256: str,
        prior_skill_sha256s: Sequence[str],
    ) -> "SkillUpdateReceipt":
        if not isinstance(skill, TaskLocalSkillRecord):
            raise ValueError("Skill update receipt requires a typed Skill")
        if not isinstance(prior_skill_sha256s, Sequence) or isinstance(
            prior_skill_sha256s, (str, bytes)
        ):
            raise ValueError("prior Skill lineage must be a sequence")
        prior = tuple(_sha(value, "prior Skill sha256") for value in prior_skill_sha256s)
        if len(prior) != len(set(prior)) or skill.sha256 in prior:
            raise ValueError("Skill lineage reuses a content hash")
        if prior:
            if prior[-1] != skill.parent_skill_sha256:
                raise ValueError("Skill parent does not match the lineage head")
        elif skill.parent_skill_sha256 != EMPTY_TASK_LOCAL_SKILL_SHA256:
            raise ValueError("first Skill parent must be the zero sha256")
        lineage = (*prior, skill.sha256)
        lineage_sha = hashlib.sha256(
            json.dumps(list(lineage), sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        return cls(
            schema_version=1,
            cell_id=skill.cell_id,
            suite=skill.suite,
            instance_id=skill.instance_id,
            arm_id=skill.arm_id,
            version=skill.version,
            operation_id=operation_id,
            operation_result_artifact_sha256=operation_result_artifact_sha256,
            updater_prompt_sha256=updater_prompt_sha256,
            public_input_projection_sha256=public_input_projection_sha256,
            parent_skill_sha256=skill.parent_skill_sha256,
            source_round_sha256=skill.source_round_sha256,
            frozen_decision_sha256=skill.frozen_decision_sha256,
            frozen_operational_fingerprint=skill.frozen_operational_fingerprint,
            skill_sha256=skill.sha256,
            skill_lineage_prefix_sha256=lineage_sha,
        )

    @classmethod
    def from_bytes(
        cls,
        raw: bytes,
        *,
        skill: TaskLocalSkillRecord,
        prior_skill_sha256s: Sequence[str],
        expected_operation_id: str,
        expected_operation_result_artifact_sha256: str,
        expected_updater_prompt_sha256: str,
        expected_public_input_projection_sha256: str,
    ) -> "SkillUpdateReceipt":
        payload = _parse_canonical_object(
            raw, label="Skill update receipt", maximum=_MAX_SKILL_BYTES
        )
        _require_exact_fields(payload, _SKILL_RECEIPT_FIELDS, "Skill update receipt")
        expected = cls.create(
            skill=skill,
            operation_id=expected_operation_id,
            operation_result_artifact_sha256=expected_operation_result_artifact_sha256,
            updater_prompt_sha256=expected_updater_prompt_sha256,
            public_input_projection_sha256=expected_public_input_projection_sha256,
            prior_skill_sha256s=prior_skill_sha256s,
        )
        if payload != expected.to_dict():
            raise ValueError("Skill update receipt binding differs")
        return expected

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()
