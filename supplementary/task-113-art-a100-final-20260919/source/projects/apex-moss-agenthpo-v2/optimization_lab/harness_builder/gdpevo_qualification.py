"""Static, zero-entitlement qualification contract for GDPevo.

This module is intentionally incapable of launching an evaluator.  It binds a
small qualification slice to an upstream Git tree, validates candidate-file
provenance, and projects already-produced evaluator JSON through a narrow
public boundary.  Container execution and the 180 planned canary transactions
require a separately reviewed authority that does not exist in this contract.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import stat
from typing import Any, Mapping, Sequence


DEFAULT_GDPEVO_QUALIFICATION_MANIFEST = (
    Path(__file__).with_name("data") / "gdpevo_qualification_canary_v1.json"
)

_HEX = set("0123456789abcdef")
_Q_GROUP_ORDER = (
    "task_group_006",
    "task_group_024",
    "task_group_015",
    "task_group_007",
    "task_group_001",
    "task_group_014",
)
_GROUP_TREES = {
    "task_group_001": {
        "env_tree": "4f102c7ba5b9949a83e05b07575616ec4f89974d",
        "group_tree": "c29a7931b8dc4d7ee7b1b56f01beb1f016b52b0c",
        "test_tasks_tree": "85efbc731dfaad7c8bd1ac26dd235e51420d54d7",
    },
    "task_group_006": {
        "env_tree": "1055712612a837101278a4755d75a0023751bd50",
        "group_tree": "14ae5eff6d9d9a356b5d49673f1d742c10731fb4",
        "test_tasks_tree": "db73b876f27e42c62c914f26ebfbe32814675c13",
    },
    "task_group_007": {
        "env_tree": "ca8a41152c19b6d47e1fb2c7cc81070bbecec66c",
        "group_tree": "a100b1ede8b6c0839549b5f9816b0d84d4c703f9",
        "test_tasks_tree": "a3b7c5f93c4142ecd1fc98d3a8a7d5381e128f1a",
    },
    "task_group_014": {
        "env_tree": "439812c36a1632099999b19981d47dc8ae05a903",
        "group_tree": "940f35104ca37b407846553e691e1a97514a3a58",
        "test_tasks_tree": "a47e3794d5bfb84147ecd2d6d6c747b9c42f2b63",
    },
    "task_group_015": {
        "env_tree": "6b98a0ad8da2a395b66c239f18493f478b1a4c97",
        "group_tree": "541e130c30f79b521aadae4c2899acd50b83ac5d",
        "test_tasks_tree": "c822793843928fde0d0c682416509b0e060e4d90",
    },
    "task_group_024": {
        "env_tree": "2a9adc4f84f7a7d73593220eeee3c93a72b09153",
        "group_tree": "9403255853f26b9b50c89035312d2d30cf6f9728",
        "test_tasks_tree": "6e79b4da5420ec4ce50195e9414b1eee51fe25ad",
    },
}
_FILE_MANIFESTS = {
    "control_plane": {
        "byte_count": 2_364_717,
        "file_count": 234,
        "sha256": "f119fc1e3f09affa94f22c14c310eb238b6c7add047440949e9c8996b7bcd86a",
    },
    "environment": {
        "byte_count": 1_739_394,
        "file_count": 108,
        "sha256": "0befc37814b414ca7ebf8675a17f90add1ecc7446c44e5fa1b3033df29fa209a",
    },
    "evaluator_template_gold": {
        "byte_count": 544_234,
        "file_count": 120,
        "sha256": "41cd3e50fe83ead610908bbea20ca9b21a86f3e38a0303cb873bfaba328f77b0",
    },
    "task_group_yaml": {
        "byte_count": 81_089,
        "file_count": 6,
        "sha256": "91ec78a1b46a1081512b717462cdd0ccd0ab7cd89186cdf7a32e02829ba79fd8",
    },
}
_ZERO_ENTITLEMENT = {
    "cpu_evaluator_seconds": 0,
    "evaluator_transactions": 0,
    "max_parallel": 0,
    "model_calls": 0,
}
_BLOCKERS = (
    "docker_or_podman_runtime_unavailable",
    "minimum_2_cpu_capacity_unverified",
    "minimum_8_gib_memory_capacity_unverified",
    "disk_capacity_insufficient",
    "evaluator_runtime_isolation_canary_pending",
)
_SCORED_GROUP_FIELDS = {
    "task_group_001": "total_score",
    "task_group_006": "score",
    "task_group_007": "score",
    "task_group_014": "score",
    "task_group_015": "score",
    "task_group_024": "score",
}
_PUBLIC_FIELDS = (
    "normalized_score",
    "validity",
    "coarse_reason_codes",
)


class GDPevoQualificationError(ValueError):
    """The GDPevo qualification artifact is unsafe or has drifted."""


@dataclass(frozen=True)
class GDPevoAdapterResult:
    """Narrow public projection plus controller-private evaluator evidence."""

    public_projection: Mapping[str, object]
    private_evidence: Mapping[str, object]


def _reject_constant(value: str) -> None:
    raise GDPevoQualificationError(f"evaluator JSON contains {value}")


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    payload: dict[str, Any] = {}
    for key, value in pairs:
        if key in payload:
            raise GDPevoQualificationError(
                f"JSON repeats top-level or nested field {key!r}"
            )
        payload[key] = value
    return payload


def canonical_gdpevo_qualification_bytes(payload: object) -> bytes:
    """Return the only accepted on-disk encoding for the static contract."""

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
        raise GDPevoQualificationError(
            "GDPevo qualification payload is not canonical JSON"
        ) from exc


def _expected_contract() -> dict[str, object]:
    groups = []
    for group_id in _Q_GROUP_ORDER:
        score_mode: dict[str, object] = {
            "metric_field": _SCORED_GROUP_FIELDS[group_id],
            "mode": "normalized_numeric_field_direct_no_renormalization",
            "range": [0.0, 1.0],
        }
        if group_id == "task_group_024":
            score_mode["points_max_score_use"] = (
                "optional_consistency_check_only"
            )
        groups.append(
            {
                "group_id": group_id,
                "score_contract": score_mode,
                "test_task_count": 5,
                "trees": _GROUP_TREES[group_id],
            }
        )
    return {
        "adapter_contract": {
            "group_order": list(_Q_GROUP_ORDER),
            "input_encoding": "strict_single_json_object_v1",
            "private_evidence_fields": [
                "details",
                "error",
                "parse_error",
                "points",
                "raw_evaluator_output",
                "scoring_points",
            ],
            "public_projection_fields": list(_PUBLIC_FIELDS),
        },
        "canary_plan": {
            "candidate_count_by_kind": {
                "blank": 30,
                "gold": 30,
                "template": 30,
            },
            "deterministic_repeat_count": 2,
            "expected_normalized_score_by_kind": {
                "blank": 0.0,
                "gold": 1.0,
                "template": 0.0,
            },
            "future_gate_only": True,
            "planned_evaluator_transactions": 180,
        },
        "candidate_contract": {
            "forbidden_source_subtrees": ["eval", "output"],
            "hash_binding": "sha256_content_before_adapter",
            "path_binding": "explicit_absolute_realpath",
            "required_format": "single_json_file",
            "symlinks": "FORBIDDEN",
        },
        "capability": {
            "blockers": list(_BLOCKERS),
            "execution_ready": False,
            "status": "BLOCKED_CAPABILITY",
        },
        "contract_id": "moss-gdpevo-qualification-canary-v1",
        "execution_authority": "NOT_GRANTED",
        "execution_entitlement": dict(_ZERO_ENTITLEMENT),
        "file_manifests": _FILE_MANIFESTS,
        "qualification_groups": groups,
        "schema_version": 1,
        "source_lock": {
            "git_commit": "0999c0d1e6f59b1cb8464cac4e5ed856b5dcb9e4",
            "repository": "https://github.com/Prism-Shadow/GDPevo",
            "root_tree": "983742f806f4bf6c4043d5ebea62dc4095be4c0d",
            "task_groups_tree": "2949144b022e5028ee8b48f4bb27355496df19de",
        },
    }


def _load_contract(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise GDPevoQualificationError(
            f"cannot read GDPevo qualification contract: {exc}"
        ) from exc
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_reject_duplicates,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise GDPevoQualificationError(
            "GDPevo qualification contract is not strict JSON"
        ) from exc
    if not isinstance(payload, dict):
        raise GDPevoQualificationError("qualification contract must be an object")
    if raw != canonical_gdpevo_qualification_bytes(payload):
        raise GDPevoQualificationError(
            "GDPevo qualification contract is not canonically encoded"
        )
    return payload


def _require_exact_observation(
    label: str,
    observed: Mapping[str, object],
    expected: Mapping[str, object],
) -> None:
    if dict(observed) != dict(expected):
        raise GDPevoQualificationError(f"observed {label} drifted from source lock")


def verify_gdpevo_qualification(
    manifest_path: str | Path = DEFAULT_GDPEVO_QUALIFICATION_MANIFEST,
    *,
    observed_source_lock: Mapping[str, object] | None = None,
    observed_file_manifests: Mapping[str, object] | None = None,
    request_execution: bool = False,
) -> dict[str, Any]:
    """Verify the checked-in contract without granting or consuming resources."""

    payload = _load_contract(Path(manifest_path))
    expected = _expected_contract()
    if payload != expected:
        raise GDPevoQualificationError(
            "GDPevo qualification fields or source bindings differ"
        )
    if observed_source_lock is not None:
        _require_exact_observation(
            "source lock", observed_source_lock, expected["source_lock"]  # type: ignore[arg-type]
        )
    if observed_file_manifests is not None:
        _require_exact_observation(
            "file manifests",
            observed_file_manifests,
            expected["file_manifests"],  # type: ignore[arg-type]
        )
    if request_execution:
        raise GDPevoQualificationError(
            "GDPevo contract has no execution authority or entitlement"
        )
    return payload


def _valid_sha256(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and not (set(value) - _HEX)
    )


def _path_has_symlink(path: Path) -> bool:
    current = path
    while True:
        try:
            if stat.S_ISLNK(os.lstat(current).st_mode):
                return True
        except OSError as exc:
            raise GDPevoQualificationError(
                f"cannot inspect candidate path component {current}: {exc}"
            ) from exc
        parent = current.parent
        if parent == current:
            return False
        current = parent


def verify_candidate_artifact(
    candidate_path: str | Path | None,
    *,
    expected_sha256: str,
    forbidden_roots: Sequence[str | Path],
) -> dict[str, object]:
    """Bind an explicit candidate file while excluding evaluator and gold trees."""

    if candidate_path is None or str(candidate_path).strip() == "":
        raise GDPevoQualificationError("candidate path must be explicit")
    path = Path(candidate_path)
    if not path.is_absolute():
        raise GDPevoQualificationError("candidate path must be absolute")
    if path.suffix != ".json":
        raise GDPevoQualificationError("candidate must be one JSON file")
    if not _valid_sha256(expected_sha256):
        raise GDPevoQualificationError("candidate SHA256 binding is invalid")
    if _path_has_symlink(path):
        raise GDPevoQualificationError("candidate path may not contain symlinks")
    try:
        resolved = path.resolve(strict=True)
    except OSError as exc:
        raise GDPevoQualificationError(f"candidate path does not resolve: {exc}") from exc
    if resolved != path:
        raise GDPevoQualificationError("candidate path is not its explicit realpath")
    if not forbidden_roots:
        raise GDPevoQualificationError("gold/evaluator forbidden roots are required")
    for root_value in forbidden_roots:
        root = Path(root_value)
        if not root.is_absolute():
            raise GDPevoQualificationError("forbidden roots must be absolute")
        try:
            root_resolved = root.resolve(strict=True)
        except OSError as exc:
            raise GDPevoQualificationError(
                f"forbidden root does not resolve: {exc}"
            ) from exc
        if resolved == root_resolved or resolved.is_relative_to(root_resolved):
            raise GDPevoQualificationError(
                "candidate realpath is inside a gold or evaluator tree"
            )

    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(resolved, flags)
    except OSError as exc:
        raise GDPevoQualificationError(f"cannot open candidate safely: {exc}") from exc
    digest = hashlib.sha256()
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise GDPevoQualificationError("candidate is not a regular file")
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    finally:
        os.close(descriptor)
    observed = digest.hexdigest()
    if observed != expected_sha256:
        raise GDPevoQualificationError("candidate content hash drifted")
    return {
        "candidate_realpath": str(resolved),
        "candidate_sha256": observed,
        "size_bytes": metadata.st_size,
    }


def _strict_single_json_object(stdout: str) -> dict[str, Any]:
    if not isinstance(stdout, str) or not stdout.strip():
        raise GDPevoQualificationError("evaluator output is empty")
    decoder = json.JSONDecoder(
        object_pairs_hook=_reject_duplicates,
        parse_constant=_reject_constant,
    )
    try:
        payload, end = decoder.raw_decode(stdout.lstrip())
    except json.JSONDecodeError as exc:
        raise GDPevoQualificationError(
            "evaluator output is not one strict JSON object"
        ) from exc
    if stdout.lstrip()[end:].strip():
        raise GDPevoQualificationError(
            "evaluator output contains data after the single JSON object"
        )
    if not isinstance(payload, dict):
        raise GDPevoQualificationError("evaluator output must be a JSON object")
    return payload


def _coarse_errors(payload: Mapping[str, object]) -> list[str]:
    reasons = []
    if payload.get("error") not in (None, ""):
        reasons.append("evaluator_reported_error")
    if payload.get("parse_error") not in (None, ""):
        reasons.append("candidate_parse_error")
    return reasons


def adapt_gdpevo_evaluator_output(
    group_id: str,
    stdout: str,
) -> GDPevoAdapterResult:
    """Parse a completed evaluator result without exposing raw rubric details."""

    if group_id not in _Q_GROUP_ORDER:
        raise GDPevoQualificationError("group is outside the frozen Q6 slice")
    payload = _strict_single_json_object(stdout)

    metric_field = _SCORED_GROUP_FIELDS[group_id]
    value = payload.get(metric_field)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise GDPevoQualificationError(
            f"{group_id} requires numeric {metric_field}"
        )
    score = float(value)
    if not math.isfinite(score) or not 0.0 <= score <= 1.0:
        raise GDPevoQualificationError(
            f"{group_id} normalized score is outside finite [0,1]"
        )
    wrong_field = "score" if metric_field == "total_score" else "total_score"
    if wrong_field in payload:
        raise GDPevoQualificationError(
            f"{group_id} contains ambiguous top-level metric fields"
        )

    if group_id == "task_group_024":
        has_points = "points" in payload
        has_max = "max_score" in payload
        if has_points != has_max:
            raise GDPevoQualificationError(
                "task_group_024 points and max_score must appear together"
            )
        if has_points:
            points = payload["points"]
            max_score = payload["max_score"]
            if (
                isinstance(points, bool)
                or isinstance(max_score, bool)
                or not isinstance(points, (int, float))
                or not isinstance(max_score, (int, float))
                or not math.isfinite(float(points))
                or not math.isfinite(float(max_score))
                or float(max_score) <= 0.0
            ):
                raise GDPevoQualificationError(
                    "task_group_024 consistency fields must be finite with positive max_score"
                )
            if not math.isclose(
                score,
                float(points) / float(max_score),
                abs_tol=1e-6,
                rel_tol=1e-6,
            ):
                raise GDPevoQualificationError(
                    "task_group_024 score disagrees with points/max_score"
                )

    reasons = _coarse_errors(payload)
    public = {
        "normalized_score": score,
        "validity": "invalid" if reasons else "valid",
        "coarse_reason_codes": reasons,
    }

    if tuple(public) != _PUBLIC_FIELDS:
        raise AssertionError("public projection field order drifted")
    return GDPevoAdapterResult(
        public_projection=public,
        private_evidence={"raw_evaluator_output": payload},
    )


def verify_future_canary_results(
    normalized_scores: Mapping[str, Sequence[Sequence[float]]],
) -> dict[str, object]:
    """Validate, but never execute, the frozen 180-transaction canary gate."""

    expected_scores = {"blank": 0.0, "gold": 1.0, "template": 0.0}
    if set(normalized_scores) != set(expected_scores):
        raise GDPevoQualificationError(
            "future canary result kinds differ from gold/blank/template"
        )
    for kind, expected in expected_scores.items():
        candidates = normalized_scores[kind]
        if isinstance(candidates, (str, bytes)) or len(candidates) != 30:
            raise GDPevoQualificationError(
                f"future canary {kind} must contain exactly 30 candidates"
            )
        for index, repeats in enumerate(candidates):
            if isinstance(repeats, (str, bytes)) or len(repeats) != 2:
                raise GDPevoQualificationError(
                    f"future canary {kind}[{index}] must have two repeats"
                )
            values = []
            for value in repeats:
                if isinstance(value, bool) or not isinstance(value, (int, float)):
                    raise GDPevoQualificationError(
                        "future canary score must be numeric"
                    )
                numeric = float(value)
                if not math.isfinite(numeric) or not 0.0 <= numeric <= 1.0:
                    raise GDPevoQualificationError(
                        "future canary score must be finite [0,1]"
                    )
                values.append(numeric)
            if values[0] != values[1]:
                raise GDPevoQualificationError(
                    f"future canary {kind}[{index}] is nondeterministic"
                )
            if values[0] != expected:
                raise GDPevoQualificationError(
                    f"future canary {kind}[{index}] violates expected score"
                )
    return {
        "candidate_count": 90,
        "deterministic_repeat_count": 2,
        "evaluator_transaction_count": 180,
        "passed": True,
    }
