"""Frozen score boundary for the wide-Harness factorial experiments.

Benchmark-native raw scores are the only values that may be reported.  A
positive affine utility is stored alongside each valid raw score solely so the
optimizer can use one common maximization convention.  Observations and
receipts bind both values, the exact transform, and the frozen contract hash;
none of those fields may be reconstructed loosely at reporting time.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Mapping


_SHA256 = re.compile(r"[0-9a-f]{64}")
_ZERO_SHA256 = "0" * 64
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/+-]{0,255}")
_REPORTING_METRIC = "RAW_SCORE_ONLY"
_UTILITY_SCOPE = "OPTIMIZATION_INTERNAL_ONLY"


class ScoreContractError(ValueError):
    """A score, transform, observation, or receipt violates the frozen contract."""


def _reject_json_constant(value: str) -> None:
    raise ScoreContractError(f"score JSON contains non-finite constant {value}")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ScoreContractError(f"score JSON repeats field {key!r}")
        value[key] = item
    return value


def _require_exact_keys(
    payload: Mapping[str, Any], expected: set[str], label: str
) -> None:
    actual = set(payload)
    if actual != expected:
        raise ScoreContractError(
            f"{label} keys differ: missing={sorted(expected - actual)}, "
            f"extra={sorted(actual - expected)}"
        )


def _finite_number(value: object, label: str) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(value)
    ):
        raise ScoreContractError(f"{label} must be a finite number")
    normalized = float(value)
    # Do not permit two serialized representations for signed zero.
    return 0.0 if normalized == 0.0 else normalized


def _bounded_number(
    value: object, *, lower: float, upper: float, label: str
) -> float:
    normalized = _finite_number(value, label)
    if normalized < lower or normalized > upper:
        raise ScoreContractError(
            f"{label} {normalized!r} is outside [{lower!r}, {upper!r}]"
        )
    return normalized


def _sha256_value(value: object, label: str) -> str:
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise ScoreContractError(f"invalid {label}")
    return value


def _safe_identifier(value: object, label: str) -> str:
    if (
        not isinstance(value, str)
        or not _SAFE_ID.fullmatch(value)
        or ".." in value
        or "//" in value
        or value.endswith("/")
    ):
        raise ScoreContractError(f"unsafe {label}")
    return value


def canonical_score_bytes(payload: object) -> bytes:
    """Return the sole JSON serialization accepted for score artifacts."""

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
        raise ScoreContractError("score payload is not canonical JSON") from exc


def score_sha256(payload: object) -> str:
    """Hash canonical score bytes."""

    return hashlib.sha256(canonical_score_bytes(payload)).hexdigest()


def _load_canonical_object(raw: bytes, label: str) -> dict[str, Any]:
    if not isinstance(raw, bytes):
        raise ScoreContractError(f"{label} must be bytes")
    try:
        payload = json.loads(
            raw.decode("utf-8"),
            parse_constant=_reject_json_constant,
            object_pairs_hook=_reject_duplicate_keys,
        )
    except ScoreContractError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ScoreContractError(f"invalid {label} JSON") from exc
    if not isinstance(payload, dict):
        raise ScoreContractError(f"{label} must be a JSON object")
    if canonical_score_bytes(payload) != raw:
        raise ScoreContractError(f"{label} bytes are not canonical")
    return payload


@dataclass(frozen=True)
class AffineScoreTransform:
    """A named, immutable affine transform: ``utility = scale * raw + offset``."""

    transform_id: str
    kind: str
    scale: float
    offset: float

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "transform_id", _safe_identifier(self.transform_id, "transform id")
        )
        if self.kind != "AFFINE_V1":
            raise ScoreContractError("only AFFINE_V1 score transforms are supported")
        scale = _finite_number(self.scale, "transform scale")
        if scale <= 0.0:
            raise ScoreContractError("transform scale must be positive")
        object.__setattr__(self, "scale", scale)
        object.__setattr__(self, "offset", _finite_number(self.offset, "transform offset"))

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "AffineScoreTransform":
        if not isinstance(payload, Mapping):
            raise ScoreContractError("score transform must be an object")
        _require_exact_keys(
            payload, {"transform_id", "kind", "scale", "offset"}, "score transform"
        )
        return cls(
            transform_id=payload["transform_id"],
            kind=payload["kind"],
            scale=payload["scale"],
            offset=payload["offset"],
        )

    def to_dict(self) -> dict[str, str | float]:
        return {
            "kind": self.kind,
            "offset": self.offset,
            "scale": self.scale,
            "transform_id": self.transform_id,
        }

    def apply(self, raw_score: float) -> float:
        result = self.scale * raw_score + self.offset
        return _finite_number(result, "derived utility score")

    def invert(self, utility_score: float) -> float:
        result = (utility_score - self.offset) / self.scale
        return _finite_number(result, "derived raw score")


@dataclass(frozen=True)
class ScoreContract:
    """Frozen native range, optimizer transform, and reporting boundary."""

    schema_version: int
    benchmark_id: str
    raw_min: float
    raw_max: float
    utility_min: float
    utility_max: float
    transform: AffineScoreTransform
    reporting_metric: str = _REPORTING_METRIC
    utility_scope: str = _UTILITY_SCOPE

    def __post_init__(self) -> None:
        if isinstance(self.schema_version, bool) or self.schema_version != 1:
            raise ScoreContractError("score contract requires schema_version 1")
        object.__setattr__(
            self, "benchmark_id", _safe_identifier(self.benchmark_id, "benchmark id")
        )
        for name in ("raw_min", "raw_max", "utility_min", "utility_max"):
            object.__setattr__(self, name, _finite_number(getattr(self, name), name))
        if self.raw_min >= self.raw_max or self.utility_min >= self.utility_max:
            raise ScoreContractError("score contract ranges must be increasing")
        if not isinstance(self.transform, AffineScoreTransform):
            raise ScoreContractError("score contract requires an affine transform")
        if self.reporting_metric != _REPORTING_METRIC:
            raise ScoreContractError("factorial reports must use raw score only")
        if self.utility_scope != _UTILITY_SCOPE:
            raise ScoreContractError("utility score must remain optimizer-internal")
        if (
            self.transform.apply(self.raw_min) != self.utility_min
            or self.transform.apply(self.raw_max) != self.utility_max
        ):
            raise ScoreContractError("score ranges do not match the frozen transform")

    @property
    def raw_range(self) -> tuple[float, float]:
        return (self.raw_min, self.raw_max)

    @property
    def utility_range(self) -> tuple[float, float]:
        return (self.utility_min, self.utility_max)

    def to_dict(self) -> dict[str, Any]:
        return {
            "benchmark_id": self.benchmark_id,
            "raw_range": [self.raw_min, self.raw_max],
            "reporting_metric": self.reporting_metric,
            "schema_version": self.schema_version,
            "transform": self.transform.to_dict(),
            "utility_range": [self.utility_min, self.utility_max],
            "utility_scope": self.utility_scope,
        }

    def canonical_bytes(self) -> bytes:
        return canonical_score_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()

    def utility_from_raw(self, raw_score: object) -> float:
        raw = _bounded_number(
            raw_score, lower=self.raw_min, upper=self.raw_max, label="raw score"
        )
        utility = self.transform.apply(raw)
        return _bounded_number(
            utility,
            lower=self.utility_min,
            upper=self.utility_max,
            label="derived utility score",
        )

    def raw_from_utility(self, utility_score: object) -> float:
        utility = _bounded_number(
            utility_score,
            lower=self.utility_min,
            upper=self.utility_max,
            label="utility score",
        )
        raw = self.transform.invert(utility)
        return _bounded_number(
            raw, lower=self.raw_min, upper=self.raw_max, label="derived raw score"
        )


AGENTHPOBENCH_SCORE_CONTRACT = ScoreContract(
    schema_version=1,
    benchmark_id="agenthpobench",
    raw_min=-1.0,
    raw_max=1.0,
    utility_min=1.0,
    utility_max=3.0,
    transform=AffineScoreTransform(
        transform_id="agenthpobench_raw_plus_2_v1",
        kind="AFFINE_V1",
        scale=1.0,
        offset=2.0,
    ),
)

GDPEVO_SCORE_CONTRACT = ScoreContract(
    schema_version=1,
    benchmark_id="gdpevo",
    raw_min=0.0,
    raw_max=1.0,
    utility_min=1.0,
    utility_max=2.0,
    transform=AffineScoreTransform(
        transform_id="gdpevo_raw_plus_1_v1",
        kind="AFFINE_V1",
        scale=1.0,
        offset=1.0,
    ),
)

_SCORE_CONTRACTS: Mapping[str, ScoreContract] = MappingProxyType(
    {
        AGENTHPOBENCH_SCORE_CONTRACT.benchmark_id: AGENTHPOBENCH_SCORE_CONTRACT,
        GDPEVO_SCORE_CONTRACT.benchmark_id: GDPEVO_SCORE_CONTRACT,
    }
)


def score_contract_for(benchmark_id: str) -> ScoreContract:
    """Return the only frozen contract for a supported benchmark."""

    try:
        return _SCORE_CONTRACTS[benchmark_id]
    except (KeyError, TypeError) as exc:
        raise ScoreContractError(f"unsupported benchmark score contract: {benchmark_id!r}") from exc


_OBSERVATION_KEYS = {
    "benchmark_id",
    "evaluation_evidence_sha256",
    "invalid_reason",
    "raw_score",
    "reporting_metric",
    "schema_version",
    "score_contract_sha256",
    "transform",
    "utility_scope",
    "utility_score",
    "valid",
}


@dataclass(frozen=True)
class EvaluationScoreObservation:
    """One evaluator observation with an inseparable raw/utility binding."""

    schema_version: int
    benchmark_id: str
    valid: bool
    raw_score: float | None
    utility_score: float | None
    invalid_reason: str | None
    transform: AffineScoreTransform
    score_contract_sha256: str
    evaluation_evidence_sha256: str
    reporting_metric: str = _REPORTING_METRIC
    utility_scope: str = _UTILITY_SCOPE

    def __post_init__(self) -> None:
        if isinstance(self.schema_version, bool) or self.schema_version != 1:
            raise ScoreContractError("score observation requires schema_version 1")
        contract = score_contract_for(self.benchmark_id)
        if not isinstance(self.valid, bool):
            raise ScoreContractError("observation valid must be boolean")
        if self.transform != contract.transform:
            raise ScoreContractError("observation transform differs from frozen contract")
        if self.score_contract_sha256 != contract.sha256:
            raise ScoreContractError("observation score contract sha256 mismatch")
        evidence_sha256 = _sha256_value(
            self.evaluation_evidence_sha256, "evaluation evidence sha256"
        )
        if self.reporting_metric != _REPORTING_METRIC:
            raise ScoreContractError("factorial reports must use raw score only")
        if self.utility_scope != _UTILITY_SCOPE:
            raise ScoreContractError("utility score must remain optimizer-internal")
        if self.valid:
            if evidence_sha256 == _ZERO_SHA256:
                raise ScoreContractError(
                    "valid observation requires nonzero evaluation evidence sha256"
                )
            if self.invalid_reason is not None:
                raise ScoreContractError("valid observation cannot have invalid_reason")
            if self.raw_score is None or self.utility_score is None:
                raise ScoreContractError("valid observation requires raw and utility scores")
            raw = _bounded_number(
                self.raw_score,
                lower=contract.raw_min,
                upper=contract.raw_max,
                label="observation raw score",
            )
            utility = _bounded_number(
                self.utility_score,
                lower=contract.utility_min,
                upper=contract.utility_max,
                label="observation utility score",
            )
            if utility != contract.utility_from_raw(raw):
                raise ScoreContractError("observation raw and utility scores disagree")
            # Binary floats do not guarantee bit-identical round trips through
            # an affine offset (for example 0.1 -> 2.1 ->
            # 0.10000000000000009).  The forward transform above is the
            # canonical stored binding; the inverse remains range checked and
            # is available to consumers without imposing an invalid exactness
            # invariant here.
            contract.raw_from_utility(utility)
            object.__setattr__(self, "raw_score", raw)
            object.__setattr__(self, "utility_score", utility)
        else:
            if self.raw_score is not None or self.utility_score is not None:
                raise ScoreContractError("invalid observation cannot expose any score")
            if (
                not isinstance(self.invalid_reason, str)
                or not self.invalid_reason.strip()
                or len(self.invalid_reason) > 256
            ):
                raise ScoreContractError("invalid observation requires a concise invalid_reason")

    @classmethod
    def create(
        cls,
        *,
        benchmark_id: str,
        valid: bool,
        raw_score: object | None,
        evaluation_evidence_sha256: str,
        invalid_reason: str | None = None,
    ) -> "EvaluationScoreObservation":
        contract = score_contract_for(benchmark_id)
        if not isinstance(valid, bool):
            raise ScoreContractError("observation valid must be boolean")
        utility: float | None = None
        normalized_raw: float | None = None
        if valid:
            if raw_score is None:
                raise ScoreContractError("valid observation requires raw score")
            normalized_raw = _bounded_number(
                raw_score,
                lower=contract.raw_min,
                upper=contract.raw_max,
                label="raw score",
            )
            utility = contract.utility_from_raw(normalized_raw)
        elif raw_score is not None:
            raise ScoreContractError("invalid observation cannot expose raw score")
        return cls(
            schema_version=1,
            benchmark_id=contract.benchmark_id,
            valid=valid,
            raw_score=normalized_raw,
            utility_score=utility,
            invalid_reason=invalid_reason,
            transform=contract.transform,
            score_contract_sha256=contract.sha256,
            evaluation_evidence_sha256=evaluation_evidence_sha256,
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "EvaluationScoreObservation":
        if not isinstance(payload, Mapping):
            raise ScoreContractError("score observation must be an object")
        _require_exact_keys(payload, _OBSERVATION_KEYS, "score observation")
        transform = AffineScoreTransform.from_dict(payload["transform"])
        return cls(
            schema_version=payload["schema_version"],
            benchmark_id=payload["benchmark_id"],
            valid=payload["valid"],
            raw_score=payload["raw_score"],
            utility_score=payload["utility_score"],
            invalid_reason=payload["invalid_reason"],
            transform=transform,
            score_contract_sha256=payload["score_contract_sha256"],
            evaluation_evidence_sha256=payload["evaluation_evidence_sha256"],
            reporting_metric=payload["reporting_metric"],
            utility_scope=payload["utility_scope"],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "benchmark_id": self.benchmark_id,
            "evaluation_evidence_sha256": self.evaluation_evidence_sha256,
            "invalid_reason": self.invalid_reason,
            "raw_score": self.raw_score,
            "reporting_metric": self.reporting_metric,
            "schema_version": self.schema_version,
            "score_contract_sha256": self.score_contract_sha256,
            "transform": self.transform.to_dict(),
            "utility_scope": self.utility_scope,
            "utility_score": self.utility_score,
            "valid": self.valid,
        }

    def canonical_bytes(self) -> bytes:
        return canonical_score_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()

    @classmethod
    def from_canonical_bytes(cls, raw: bytes) -> "EvaluationScoreObservation":
        payload = _load_canonical_object(raw, "score observation")
        item = cls.from_dict(payload)
        if item.canonical_bytes() != raw:
            raise ScoreContractError("score observation is not in canonical typed form")
        return item

    def utility_for_optimization(self) -> float | None:
        return self.utility_score

    def report_value(self, metric: str) -> float | None:
        if metric != "raw_score":
            raise ScoreContractError("factorial reports may expose raw score only")
        return self.raw_score

    def report_projection(self) -> dict[str, Any]:
        return {
            "benchmark_id": self.benchmark_id,
            "invalid_reason": self.invalid_reason,
            "raw_score": self.raw_score,
            "reporting_metric": self.reporting_metric,
            "valid": self.valid,
        }


_RECEIPT_KEYS = _OBSERVATION_KEYS | {"evaluation_id", "observation_sha256"}


@dataclass(frozen=True)
class EvaluationScoreReceipt:
    """Sealed repetition of an observation's complete score binding."""

    schema_version: int
    evaluation_id: str
    benchmark_id: str
    valid: bool
    raw_score: float | None
    utility_score: float | None
    invalid_reason: str | None
    transform: AffineScoreTransform
    score_contract_sha256: str
    evaluation_evidence_sha256: str
    observation_sha256: str
    reporting_metric: str = _REPORTING_METRIC
    utility_scope: str = _UTILITY_SCOPE

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "evaluation_id", _safe_identifier(self.evaluation_id, "evaluation id")
        )
        observation = self.observation()
        if self.observation_sha256 != observation.sha256:
            raise ScoreContractError("receipt observation sha256 mismatch")

    @classmethod
    def seal(
        cls, *, evaluation_id: str, observation: EvaluationScoreObservation
    ) -> "EvaluationScoreReceipt":
        if not isinstance(observation, EvaluationScoreObservation):
            raise ScoreContractError("receipt requires a verified score observation")
        return cls(
            schema_version=observation.schema_version,
            evaluation_id=evaluation_id,
            benchmark_id=observation.benchmark_id,
            valid=observation.valid,
            raw_score=observation.raw_score,
            utility_score=observation.utility_score,
            invalid_reason=observation.invalid_reason,
            transform=observation.transform,
            score_contract_sha256=observation.score_contract_sha256,
            evaluation_evidence_sha256=observation.evaluation_evidence_sha256,
            observation_sha256=observation.sha256,
            reporting_metric=observation.reporting_metric,
            utility_scope=observation.utility_scope,
        )

    def observation(self) -> EvaluationScoreObservation:
        return EvaluationScoreObservation(
            schema_version=self.schema_version,
            benchmark_id=self.benchmark_id,
            valid=self.valid,
            raw_score=self.raw_score,
            utility_score=self.utility_score,
            invalid_reason=self.invalid_reason,
            transform=self.transform,
            score_contract_sha256=self.score_contract_sha256,
            evaluation_evidence_sha256=self.evaluation_evidence_sha256,
            reporting_metric=self.reporting_metric,
            utility_scope=self.utility_scope,
        )

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "EvaluationScoreReceipt":
        if not isinstance(payload, Mapping):
            raise ScoreContractError("score receipt must be an object")
        _require_exact_keys(payload, _RECEIPT_KEYS, "score receipt")
        return cls(
            schema_version=payload["schema_version"],
            evaluation_id=payload["evaluation_id"],
            benchmark_id=payload["benchmark_id"],
            valid=payload["valid"],
            raw_score=payload["raw_score"],
            utility_score=payload["utility_score"],
            invalid_reason=payload["invalid_reason"],
            transform=AffineScoreTransform.from_dict(payload["transform"]),
            score_contract_sha256=payload["score_contract_sha256"],
            evaluation_evidence_sha256=payload["evaluation_evidence_sha256"],
            observation_sha256=payload["observation_sha256"],
            reporting_metric=payload["reporting_metric"],
            utility_scope=payload["utility_scope"],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **self.observation().to_dict(),
            "evaluation_id": self.evaluation_id,
            "observation_sha256": self.observation_sha256,
        }

    def canonical_bytes(self) -> bytes:
        return canonical_score_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()

    @classmethod
    def from_canonical_bytes(cls, raw: bytes) -> "EvaluationScoreReceipt":
        payload = _load_canonical_object(raw, "score receipt")
        item = cls.from_dict(payload)
        if item.canonical_bytes() != raw:
            raise ScoreContractError("score receipt is not in canonical typed form")
        return item

    def report_projection(self) -> dict[str, Any]:
        return {
            **self.observation().report_projection(),
            "evaluation_id": self.evaluation_id,
        }


__all__ = [
    "AGENTHPOBENCH_SCORE_CONTRACT",
    "GDPEVO_SCORE_CONTRACT",
    "AffineScoreTransform",
    "EvaluationScoreObservation",
    "EvaluationScoreReceipt",
    "ScoreContract",
    "ScoreContractError",
    "canonical_score_bytes",
    "score_contract_for",
    "score_sha256",
]
