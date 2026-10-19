"""Exact ITT floor binding for the wide-Harness factorial experiment.

The frozen policy requires every reserved attempt to contribute once the
formal reservation/evaluator ledger is connected.  For a supplied typed score
receipt, a valid observation keeps its benchmark-native raw score and an
invalid observation is imputed at that benchmark's frozen native minimum.  The
positive affine utility is carried only for a future verified optimizer sink
and is deliberately absent from the strict public report row.

This module is an offline artifact boundary.  It grants no execution
authority and invokes no model, evaluator, benchmark, or resource provider.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from .factorial_contract import DEFAULT_FACTORIAL_MANIFEST
from .factorial_score import (
    EvaluationScoreReceipt,
    ScoreContractError,
    canonical_score_bytes,
    score_contract_for,
)


_SHA256 = re.compile(r"[0-9a-f]{64}")
_VALID_POLICY = "OBSERVED_BENCHMARK_NATIVE_RAW"
_INVALID_POLICY = "BENCHMARK_NATIVE_RAW_MINIMUM"
_REPORTING_METRIC = "ITT_NATIVE_RAW_SCORE_ONLY"
_UTILITY_SCOPE = "OPTIMIZATION_INTERNAL_ONLY"
_INVALID_SCOPE = (
    "TYPED_INVALID_SCORE_RECEIPT_ALL_RESERVED_ATTEMPT_COVERAGE_NOT_READY"
)


class FactorialITTError(ValueError):
    """An ITT policy or score differs from its frozen bindings."""


def _sha(value: object, label: str) -> str:
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise FactorialITTError(f"invalid {label}")
    return value


def _finite(value: object, label: str) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
    ):
        raise FactorialITTError(f"{label} must be a finite number")
    normalized = float(value)
    return 0.0 if normalized == 0.0 else normalized


def _exact(payload: Mapping[str, Any], expected: set[str], label: str) -> None:
    if set(payload) != expected:
        raise FactorialITTError(
            f"{label} keys differ: missing={sorted(expected - set(payload))}, "
            f"extra={sorted(set(payload) - expected)}"
        )


def _reject_constant(value: str) -> None:
    raise FactorialITTError(f"ITT JSON contains non-finite constant {value}")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise FactorialITTError(f"ITT JSON repeats field {key!r}")
        result[key] = value
    return result


def _load_canonical(raw: bytes, label: str) -> dict[str, Any]:
    if not isinstance(raw, bytes):
        raise FactorialITTError(f"{label} must be bytes")
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            parse_constant=_reject_constant,
            object_pairs_hook=_reject_duplicate_keys,
        )
    except FactorialITTError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FactorialITTError(f"invalid {label} JSON") from exc
    if not isinstance(payload, dict) or canonical_score_bytes(payload) != raw:
        raise FactorialITTError(f"{label} is not canonical JSON")
    return payload


def _verified_factorial(manifest_path: Path) -> Mapping[str, Any]:
    """Load only a manifest accepted by the complete frozen contract verifier."""

    from .factorial_contract import verify_factorial_contract

    try:
        return verify_factorial_contract(manifest_path)
    except (OSError, TypeError, ValueError) as exc:
        raise FactorialITTError("factorial contract verification failed") from exc


_POLICY_KEYS = {
    "benchmark_id",
    "factorial_contract_sha256",
    "invalid_reason_scope",
    "invalid_score_policy",
    "raw_floor",
    "reporting_metric",
    "schema_version",
    "score_contract_sha256",
    "utility_floor",
    "utility_scope",
    "valid_score_policy",
}


@dataclass(frozen=True)
class FactorialITTPolicy:
    """Content-addressed native-floor policy for one factorial benchmark."""

    schema_version: int
    factorial_contract_sha256: str
    benchmark_id: str
    score_contract_sha256: str
    raw_floor: float
    utility_floor: float
    valid_score_policy: str
    invalid_score_policy: str
    invalid_reason_scope: str
    reporting_metric: str
    utility_scope: str

    def __post_init__(self) -> None:
        if isinstance(self.schema_version, bool) or self.schema_version != 1:
            raise FactorialITTError("ITT policy requires schema_version 1")
        _sha(self.factorial_contract_sha256, "factorial contract sha256")
        contract = score_contract_for(self.benchmark_id)
        if self.score_contract_sha256 != contract.sha256:
            raise FactorialITTError("ITT policy score contract sha256 differs")
        raw_floor = _finite(self.raw_floor, "ITT raw floor")
        utility_floor = _finite(self.utility_floor, "ITT utility floor")
        if raw_floor != contract.raw_min or utility_floor != contract.utility_min:
            raise FactorialITTError("ITT floor differs from native score contract")
        if contract.utility_from_raw(raw_floor) != utility_floor:
            raise FactorialITTError("ITT raw and utility floors disagree")
        if self.valid_score_policy != _VALID_POLICY:
            raise FactorialITTError("ITT valid-score policy differs")
        if self.invalid_score_policy != _INVALID_POLICY:
            raise FactorialITTError("ITT invalid-score policy differs")
        if self.invalid_reason_scope != _INVALID_SCOPE:
            raise FactorialITTError("ITT invalid-reason scope differs")
        if self.reporting_metric != _REPORTING_METRIC:
            raise FactorialITTError("ITT reports must use native raw score only")
        if self.utility_scope != _UTILITY_SCOPE:
            raise FactorialITTError("ITT utility must remain optimizer-internal")
        object.__setattr__(self, "raw_floor", raw_floor)
        object.__setattr__(self, "utility_floor", utility_floor)

    @classmethod
    def from_verified_manifest(
        cls,
        *,
        benchmark_id: str,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    ) -> "FactorialITTPolicy":
        """Derive the policy through the complete frozen manifest verifier."""

        factorial = _verified_factorial(manifest_path)
        digest = _sha(
            factorial.get("contract_digest"), "factorial contract sha256"
        )
        try:
            score_boundary = factorial["main_experiment"]["score_boundary"]
            declared_sha = score_boundary["contract_sha256s"][benchmark_id]
            declared_benchmarks = {
                item["benchmark_id"]
                for item in factorial["main_experiment"]["benchmarks"]
            }
        except (KeyError, TypeError) as exc:
            raise FactorialITTError("factorial score-boundary binding is missing") from exc
        if benchmark_id not in declared_benchmarks:
            raise FactorialITTError("benchmark is absent from factorial main experiment")
        contract = score_contract_for(benchmark_id)
        if declared_sha != contract.sha256:
            raise FactorialITTError("factorial score contract sha256 differs")
        return cls(
            schema_version=1,
            factorial_contract_sha256=digest,
            benchmark_id=benchmark_id,
            score_contract_sha256=contract.sha256,
            raw_floor=contract.raw_min,
            utility_floor=contract.utility_min,
            valid_score_policy=_VALID_POLICY,
            invalid_score_policy=_INVALID_POLICY,
            invalid_reason_scope=_INVALID_SCOPE,
            reporting_metric=_REPORTING_METRIC,
            utility_scope=_UTILITY_SCOPE,
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "FactorialITTPolicy":
        if not isinstance(payload, Mapping):
            raise FactorialITTError("ITT policy must be an object")
        _exact(payload, _POLICY_KEYS, "ITT policy")
        return cls(**dict(payload))

    def to_dict(self) -> dict[str, Any]:
        return {
            "benchmark_id": self.benchmark_id,
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "invalid_reason_scope": self.invalid_reason_scope,
            "invalid_score_policy": self.invalid_score_policy,
            "raw_floor": self.raw_floor,
            "reporting_metric": self.reporting_metric,
            "schema_version": self.schema_version,
            "score_contract_sha256": self.score_contract_sha256,
            "utility_floor": self.utility_floor,
            "utility_scope": self.utility_scope,
            "valid_score_policy": self.valid_score_policy,
        }

    def canonical_bytes(self) -> bytes:
        return canonical_score_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()

    @classmethod
    def from_canonical_bytes(
        cls,
        raw: bytes,
        *,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    ) -> "FactorialITTPolicy":
        item = cls.from_dict(_load_canonical(raw, "ITT policy"))
        expected = cls.from_verified_manifest(
            benchmark_id=item.benchmark_id,
            manifest_path=manifest_path,
        )
        if item != expected:
            raise FactorialITTError("ITT policy differs from factorial contract")
        return item

    def verify_against_manifest(
        self, *, manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST
    ) -> "FactorialITTPolicy":
        """Reverify this object at every trusted optimizer/report boundary."""

        if type(self) is not FactorialITTPolicy:
            raise FactorialITTError("exact typed ITT policy is required")
        expected = type(self).from_verified_manifest(
            benchmark_id=self.benchmark_id,
            manifest_path=manifest_path,
        )
        if self != expected:
            raise FactorialITTError("ITT policy differs from exact manifest")
        return self


_SCORE_KEYS = {
    "benchmark_id",
    "evaluation_id",
    "floor_imputed",
    "invalid_reason",
    "observation_sha256",
    "policy_sha256",
    "raw_itt_score",
    "reporting_metric",
    "schema_version",
    "score_receipt_sha256",
    "utility_itt_score",
    "utility_scope",
    "valid",
}


@dataclass(frozen=True)
class FactorialITTScore:
    """One observation projected to the preregistered ITT outcome."""

    schema_version: int
    policy_sha256: str
    score_receipt_sha256: str
    observation_sha256: str
    evaluation_id: str
    benchmark_id: str
    valid: bool
    floor_imputed: bool
    invalid_reason: str | None
    raw_itt_score: float
    utility_itt_score: float
    reporting_metric: str
    utility_scope: str

    def __post_init__(self) -> None:
        if isinstance(self.schema_version, bool) or self.schema_version != 1:
            raise FactorialITTError("ITT score requires schema_version 1")
        _sha(self.policy_sha256, "ITT policy sha256")
        _sha(self.score_receipt_sha256, "score receipt sha256")
        _sha(self.observation_sha256, "score observation sha256")
        if not isinstance(self.evaluation_id, str) or not self.evaluation_id:
            raise FactorialITTError("ITT evaluation id is required")
        contract = score_contract_for(self.benchmark_id)
        raw = _finite(self.raw_itt_score, "ITT raw score")
        utility = _finite(self.utility_itt_score, "ITT utility score")
        try:
            expected_utility = contract.utility_from_raw(raw)
        except ScoreContractError as exc:
            raise FactorialITTError("ITT raw score is outside its contract") from exc
        if utility != expected_utility:
            raise FactorialITTError("ITT raw and utility scores disagree")
        if not isinstance(self.valid, bool) or not isinstance(self.floor_imputed, bool):
            raise FactorialITTError("ITT validity fields must be boolean")
        if self.valid:
            if self.floor_imputed or self.invalid_reason is not None:
                raise FactorialITTError("valid ITT score cannot be floor-imputed")
        else:
            if not self.floor_imputed:
                raise FactorialITTError("invalid ITT score must be floor-imputed")
            if (
                not isinstance(self.invalid_reason, str)
                or not self.invalid_reason.strip()
                or len(self.invalid_reason) > 256
            ):
                raise FactorialITTError("invalid ITT score requires an invalid reason")
            if raw != contract.raw_min or utility != contract.utility_min:
                raise FactorialITTError("invalid ITT score differs from native floor")
        if self.reporting_metric != _REPORTING_METRIC:
            raise FactorialITTError("ITT reports must use native raw score only")
        if self.utility_scope != _UTILITY_SCOPE:
            raise FactorialITTError("ITT utility must remain optimizer-internal")
        object.__setattr__(self, "raw_itt_score", raw)
        object.__setattr__(self, "utility_itt_score", utility)

    @classmethod
    def from_score_receipt(
        cls,
        *,
        policy: FactorialITTPolicy,
        score_receipt: EvaluationScoreReceipt,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    ) -> "FactorialITTScore":
        if type(policy) is not FactorialITTPolicy:
            raise FactorialITTError("exact typed ITT policy is required")
        policy.verify_against_manifest(manifest_path=manifest_path)
        if type(score_receipt) is not EvaluationScoreReceipt:
            raise FactorialITTError("exact typed score receipt is required")
        observation = score_receipt.observation()
        if observation.benchmark_id != policy.benchmark_id:
            raise FactorialITTError("ITT policy and score receipt benchmark differ")
        if observation.score_contract_sha256 != policy.score_contract_sha256:
            raise FactorialITTError("ITT policy and observation score contract differ")
        if observation.valid:
            if observation.raw_score is None or observation.utility_score is None:
                raise FactorialITTError("valid observation lacks its bound score")
            raw = observation.raw_score
            utility = observation.utility_score
        else:
            raw = policy.raw_floor
            utility = policy.utility_floor
        return cls(
            schema_version=1,
            policy_sha256=policy.sha256,
            score_receipt_sha256=score_receipt.sha256,
            observation_sha256=observation.sha256,
            evaluation_id=score_receipt.evaluation_id,
            benchmark_id=policy.benchmark_id,
            valid=observation.valid,
            floor_imputed=not observation.valid,
            invalid_reason=observation.invalid_reason,
            raw_itt_score=raw,
            utility_itt_score=utility,
            reporting_metric=_REPORTING_METRIC,
            utility_scope=_UTILITY_SCOPE,
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "FactorialITTScore":
        if not isinstance(payload, Mapping):
            raise FactorialITTError("ITT score must be an object")
        _exact(payload, _SCORE_KEYS, "ITT score")
        return cls(**dict(payload))

    def to_dict(self) -> dict[str, Any]:
        return {
            "benchmark_id": self.benchmark_id,
            "evaluation_id": self.evaluation_id,
            "floor_imputed": self.floor_imputed,
            "invalid_reason": self.invalid_reason,
            "observation_sha256": self.observation_sha256,
            "policy_sha256": self.policy_sha256,
            "raw_itt_score": self.raw_itt_score,
            "reporting_metric": self.reporting_metric,
            "schema_version": self.schema_version,
            "score_receipt_sha256": self.score_receipt_sha256,
            "utility_itt_score": self.utility_itt_score,
            "utility_scope": self.utility_scope,
            "valid": self.valid,
        }

    def canonical_bytes(self) -> bytes:
        return canonical_score_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()

    @classmethod
    def from_canonical_bytes(
        cls,
        raw: bytes,
        *,
        policy: FactorialITTPolicy,
        score_receipt: EvaluationScoreReceipt,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    ) -> "FactorialITTScore":
        item = cls.from_dict(_load_canonical(raw, "ITT score"))
        expected = cls.from_score_receipt(
            policy=policy,
            score_receipt=score_receipt,
            manifest_path=manifest_path,
        )
        if item != expected:
            raise FactorialITTError("ITT score differs from policy or score receipt")
        return item

    def verified_utility_for_optimization(
        self,
        *,
        policy: FactorialITTPolicy,
        score_receipt: EvaluationScoreReceipt,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    ) -> float:
        verified = type(self).from_canonical_bytes(
            self.canonical_bytes(),
            policy=policy,
            score_receipt=score_receipt,
            manifest_path=manifest_path,
        )
        return verified.utility_itt_score


_REPORT_KEYS = {
    "benchmark_id",
    "evaluation_id",
    "factorial_contract_sha256",
    "floor_imputed",
    "invalid_reason",
    "itt_raw_score",
    "itt_score_sha256",
    "policy_sha256",
    "reporting_metric",
    "schema_version",
    "score_receipt_sha256",
    "valid",
}


@dataclass(frozen=True)
class VerifiedITTReportRow:
    """Strict public raw-only DTO; trusted writers must call ``seal``/replay."""

    schema_version: int
    factorial_contract_sha256: str
    policy_sha256: str
    score_receipt_sha256: str
    itt_score_sha256: str
    evaluation_id: str
    benchmark_id: str
    valid: bool
    floor_imputed: bool
    invalid_reason: str | None
    itt_raw_score: float
    reporting_metric: str

    def __post_init__(self) -> None:
        if isinstance(self.schema_version, bool) or self.schema_version != 1:
            raise FactorialITTError("ITT report row requires schema_version 1")
        for value, label in (
            (self.factorial_contract_sha256, "factorial contract"),
            (self.policy_sha256, "ITT policy"),
            (self.score_receipt_sha256, "score receipt"),
            (self.itt_score_sha256, "ITT score"),
        ):
            _sha(value, f"report {label} sha256")
        if not isinstance(self.evaluation_id, str) or not self.evaluation_id:
            raise FactorialITTError("ITT report evaluation id is required")
        if not isinstance(self.valid, bool) or not isinstance(self.floor_imputed, bool):
            raise FactorialITTError("ITT report validity fields must be boolean")
        raw = _finite(self.itt_raw_score, "ITT report raw score")
        contract = score_contract_for(self.benchmark_id)
        try:
            contract.utility_from_raw(raw)
        except ScoreContractError as exc:
            raise FactorialITTError("ITT report raw score is outside contract") from exc
        if self.valid:
            if self.floor_imputed or self.invalid_reason is not None:
                raise FactorialITTError("valid ITT report row cannot be imputed")
        elif (
            not self.floor_imputed
            or not isinstance(self.invalid_reason, str)
            or not self.invalid_reason.strip()
            or raw != contract.raw_min
        ):
            raise FactorialITTError("invalid ITT report row must use native floor")
        if self.reporting_metric != _REPORTING_METRIC:
            raise FactorialITTError("ITT report row must expose native raw score only")
        object.__setattr__(self, "itt_raw_score", raw)

    @classmethod
    def seal(
        cls,
        *,
        policy: FactorialITTPolicy,
        score_receipt: EvaluationScoreReceipt,
        itt_score: FactorialITTScore,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    ) -> "VerifiedITTReportRow":
        if type(itt_score) is not FactorialITTScore:
            raise FactorialITTError("exact typed ITT score is required")
        verified = FactorialITTScore.from_canonical_bytes(
            itt_score.canonical_bytes(),
            policy=policy,
            score_receipt=score_receipt,
            manifest_path=manifest_path,
        )
        return cls(
            schema_version=1,
            factorial_contract_sha256=policy.factorial_contract_sha256,
            policy_sha256=policy.sha256,
            score_receipt_sha256=score_receipt.sha256,
            itt_score_sha256=verified.sha256,
            evaluation_id=verified.evaluation_id,
            benchmark_id=verified.benchmark_id,
            valid=verified.valid,
            floor_imputed=verified.floor_imputed,
            invalid_reason=verified.invalid_reason,
            itt_raw_score=verified.raw_itt_score,
            reporting_metric=_REPORTING_METRIC,
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "VerifiedITTReportRow":
        if not isinstance(payload, Mapping):
            raise FactorialITTError("ITT report row must be an object")
        _exact(payload, _REPORT_KEYS, "ITT report row")
        return cls(**dict(payload))

    def to_dict(self) -> dict[str, Any]:
        return {
            "benchmark_id": self.benchmark_id,
            "evaluation_id": self.evaluation_id,
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "floor_imputed": self.floor_imputed,
            "invalid_reason": self.invalid_reason,
            "itt_raw_score": self.itt_raw_score,
            "itt_score_sha256": self.itt_score_sha256,
            "policy_sha256": self.policy_sha256,
            "reporting_metric": self.reporting_metric,
            "schema_version": self.schema_version,
            "score_receipt_sha256": self.score_receipt_sha256,
            "valid": self.valid,
        }

    def canonical_bytes(self) -> bytes:
        return canonical_score_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()

    @classmethod
    def from_canonical_bytes(
        cls,
        raw: bytes,
        *,
        policy: FactorialITTPolicy,
        score_receipt: EvaluationScoreReceipt,
        itt_score: FactorialITTScore,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    ) -> "VerifiedITTReportRow":
        item = cls.from_dict(_load_canonical(raw, "ITT report row"))
        expected = cls.seal(
            policy=policy,
            score_receipt=score_receipt,
            itt_score=itt_score,
            manifest_path=manifest_path,
        )
        if item != expected:
            raise FactorialITTError("ITT report row differs from verified artifacts")
        return item


__all__ = [
    "FactorialITTError",
    "FactorialITTPolicy",
    "FactorialITTScore",
    "VerifiedITTReportRow",
]
