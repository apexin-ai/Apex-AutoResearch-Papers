from __future__ import annotations

from pathlib import Path
from typing import Any


FALLBACK_MARKERS = ("fallback", "fallback_used")
DECISION_CONTAINERS = ("decisions", "decision_history")
RAW_RESPONSE_PATTERNS = (
    "qwen_raw*",  # Legacy experiment artifact name.
    "model_raw*",
    "agent_raw*",
    "raw_response*",
)
ERROR_ARTIFACT_PATTERNS = ("qwen_error*", "model_error*", "agent_error*")
MODEL_PROVENANCE_KEYS = (
    "model",
    "model_id",
    "model_name",
    "model_path",
    "agent_model",
    "checkpoint",
    "checkpoint_path",
)
RUN_DIRECTORY_KEYS = ("run_dir", "result_dir", "output_dir")
MODEL_IDENTIFIER_ALIAS_GROUPS = (
    {"qwen38b"},
    {"qwen332b"},
    {"gemma22b", "gemma22bit"},
    {"llama318b", "llama318binstruct", "metallama318binstruct"},
    {"deepseekr1qwen14b", "deepseekr1distillqwen14b"},
    {"phi4", "phi414b"},
)
EMBEDDED_RAW_RESPONSE_KEYS = (
    "raw_response",
    "raw_text",
    "model_response",
    "agent_response",
    "response",
)


def _nonnegative_int(value: Any) -> int:
    if isinstance(value, bool):
        return 0
    if isinstance(value, (int, float)):
        return max(0, int(value))
    if isinstance(value, str):
        try:
            return max(0, int(float(value.strip())))
        except ValueError:
            return 0
    return 0


def _has_fallback_marker(value: Any) -> bool:
    if isinstance(value, dict):
        return any(value.get(key) is True for key in FALLBACK_MARKERS) or any(
            _has_fallback_marker(item) for item in value.values()
        )
    if isinstance(value, list):
        return any(_has_fallback_marker(item) for item in value)
    return False


def _container_fallback_count(value: Any) -> int:
    if isinstance(value, list):
        return sum(int(_has_fallback_marker(item)) for item in value)
    return int(_has_fallback_marker(value))


def fallback_count(payload: dict[str, Any]) -> int:
    """Return the strongest available fallback count for an experiment result."""
    explicit = _nonnegative_int(payload.get("fallback_decision_count"))
    nested = max(
        (
            _container_fallback_count(payload.get(container))
            for container in DECISION_CONTAINERS
        ),
        default=0,
    )
    return max(explicit, nested)


def intervention_trace(
    payload: dict[str, Any], expected_interventions: int = 5
) -> tuple[list[dict[str, Any]], str]:
    """Return an exact baseline-plus-intervention trace and its schema."""
    expected_length = expected_interventions + 1
    history = payload.get("history")
    if isinstance(history, list):
        explicit = [
            item
            for item in history
            if isinstance(item, dict)
            and (
                item.get("kind") == "baseline"
                or str(item.get("kind", "")).startswith("intervention_")
            )
        ]
        if len(explicit) == expected_length:
            return explicit, "explicit_history"
        if len(history) == expected_length and all(
            isinstance(item, dict) for item in history
        ):
            return history, "native_history"
    chunks = payload.get("chunk_summaries")
    if isinstance(chunks, list) and len(chunks) == expected_length and all(
        isinstance(item, dict) for item in chunks
    ):
        return chunks, "chunk_summaries"
    raise ValueError(
        f"expected baseline plus {expected_interventions} intervention trace"
    )


def decision_count(
    payload: dict[str, Any],
    trace: list[dict[str, Any]],
    expected_interventions: int = 5,
) -> tuple[int, bool]:
    """Return the recorded decision count and whether it was inferred."""
    for key in DECISION_CONTAINERS:
        value = payload.get(key)
        if isinstance(value, list):
            return len(value), False
    for key in ("decisions_made", "agent_decisions_made", "strict_decision_count"):
        value = payload.get(key)
        if isinstance(value, bool):
            continue
        if isinstance(value, (int, float)):
            return int(value), False
        if isinstance(value, str):
            try:
                return int(float(value.strip())), False
            except ValueError:
                pass
    if (
        len(trace) == expected_interventions + 1
        and payload.get("strict_serial_protocol") is True
    ):
        return expected_interventions, True
    return 0, False


def result_artifact_roots(
    result_path: Path, payload: dict[str, Any]
) -> list[Path]:
    task_dir = result_path.parent
    roots: list[Path] = []
    for key in RUN_DIRECTORY_KEYS:
        value = payload.get(key)
        if not isinstance(value, str) or not value.strip():
            continue
        path = Path(value)
        candidate = path if path.is_absolute() else task_dir / path
        if candidate.exists():
            roots.append(candidate)
    run_id = payload.get("run_id")
    if isinstance(run_id, str) and run_id.strip():
        candidate = task_dir / "runs" / run_id
        if candidate.exists():
            roots.append(candidate)
    if not roots:
        roots.append(task_dir)
    return list(dict.fromkeys(path.resolve() for path in roots))


def _artifact_files(roots: list[Path], patterns: tuple[str, ...]) -> list[Path]:
    files = {
        path.resolve()
        for root in roots
        for pattern in patterns
        for path in root.rglob(pattern)
        if path.is_file()
    }
    return sorted(files)


def raw_response_files(result_path: Path, payload: dict[str, Any]) -> list[Path]:
    """Locate current-run local-model response artifacts."""
    return _artifact_files(
        result_artifact_roots(result_path, payload), RAW_RESPONSE_PATTERNS
    )


def embedded_raw_responses(payload: dict[str, Any]) -> list[str]:
    """Return at most one explicit raw model response per recorded decision."""
    decisions: list[Any] = []
    for key in DECISION_CONTAINERS:
        value = payload.get(key)
        if isinstance(value, list):
            decisions = value
            break
    responses: list[str] = []
    for decision in decisions:
        if not isinstance(decision, dict):
            continue
        containers = [decision]
        metadata = decision.get("metadata")
        if isinstance(metadata, dict):
            containers.append(metadata)
        response = next(
            (
                container[key].strip()
                for container in containers
                for key in EMBEDDED_RAW_RESPONSE_KEYS
                if isinstance(container.get(key), str) and container[key].strip()
            ),
            None,
        )
        if (
            response is None
            and isinstance(metadata, dict)
            and metadata.get("direct_prompt") is True
            and isinstance(decision.get("reasoning"), str)
            and decision["reasoning"].strip()
        ):
            # Older direct-generation adapters stored the exact decoded output
            # in reasoning and marked that schema explicitly.
            response = decision["reasoning"].strip()
        if response is not None:
            responses.append(response)
    return responses


def raw_response_count(result_path: Path, payload: dict[str, Any]) -> int:
    """Count logical responses without double-counting JSON and file artifacts."""
    embedded_count = len(embedded_raw_responses(payload))
    recorded_decisions = next(
        (
            len(payload[key])
            for key in DECISION_CONTAINERS
            if isinstance(payload.get(key), list)
        ),
        0,
    )
    if recorded_decisions and embedded_count == recorded_decisions:
        return embedded_count
    file_count = sum(
        path.stat().st_size > 0 for path in raw_response_files(result_path, payload)
    )
    return max(embedded_count, file_count)


def artifact_integrity_issues(
    result_path: Path, payload: dict[str, Any]
) -> list[str]:
    """Return current-run agent artifact failures omitted from result JSON."""
    roots = result_artifact_roots(result_path, payload)
    error_files = [
        path
        for path in _artifact_files(roots, ERROR_ARTIFACT_PATTERNS)
        if path.stat().st_size > 0
    ]
    raw_files = _artifact_files(roots, RAW_RESPONSE_PATTERNS)
    issues = []
    if error_files:
        issues.append(f"nonempty model-error files: {len(error_files)}")
    empty_raw = sum(path.stat().st_size == 0 for path in raw_files)
    if empty_raw:
        issues.append(f"empty raw-response files: {empty_raw}")
    return issues


def _has_nonempty_value(value: Any) -> bool:
    if value is None or value is False:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return bool(value)
    return True


def _normalized_identifier(value: Any) -> str:
    return "".join(character for character in str(value).lower() if character.isalnum())


def _model_identifier_variants(value: Any) -> set[str]:
    normalized = _normalized_identifier(value)
    variants = {normalized} if normalized else set()
    for aliases in MODEL_IDENTIFIER_ALIAS_GROUPS:
        if normalized in aliases:
            variants.update(aliases)
    return variants


def _model_identifier_matches(expected_model: str, candidate: Any) -> bool:
    expected_variants = _model_identifier_variants(expected_model)
    candidate_variants = _model_identifier_variants(candidate)
    return any(
        expected == candidate
        or expected in candidate
        or candidate in expected
        for expected in expected_variants
        for candidate in candidate_variants
    )


def model_provenance_matches(
    result_path: Path, payload: dict[str, Any], expected_model: str
) -> bool:
    """Prefer explicit model metadata, with run identifiers as a legacy fallback."""
    explicit_values: list[Any] = [
        payload.get(key) for key in MODEL_PROVENANCE_KEYS
    ]
    for container_name in ("metadata", "provenance", "agent"):
        container = payload.get(container_name)
        if isinstance(container, dict):
            explicit_values.extend(
                container.get(key) for key in MODEL_PROVENANCE_KEYS
            )
    explicit_values = [
        value for value in explicit_values if _has_nonempty_value(value)
    ]
    if explicit_values:
        return any(
            _model_identifier_matches(expected_model, value)
            for value in explicit_values
        )

    legacy_values = (
        payload.get("run_id"),
        payload.get("strict_serial_worker"),
        result_path,
    )
    return any(
        _model_identifier_matches(expected_model, value)
        for value in legacy_values
        if _has_nonempty_value(value)
    )


def protocol_integrity_issues(
    payload: dict[str, Any],
    *,
    expected_interventions: int = 5,
    expected_seed: int | None = None,
    require_seed: bool = True,
) -> list[str]:
    """Validate the shared sequential protocol for one final result."""
    issues: list[str] = []
    trace: list[dict[str, Any]] = []
    try:
        trace, _ = intervention_trace(payload, expected_interventions)
    except ValueError as exc:
        issues.append(str(exc))

    decisions, _ = decision_count(payload, trace, expected_interventions)
    if decisions != expected_interventions:
        issues.append(
            f"expected {expected_interventions} decisions, got {decisions}"
        )

    fallbacks = fallback_count(payload)
    if fallbacks:
        issues.append(f"fallback decisions: {fallbacks}")

    for key in ("error", "task_error", "execution_error", "failure_reason"):
        if _has_nonempty_value(payload.get(key)):
            issues.append(f"nonempty task-level {key}")
    for key in ("success", "agent_success"):
        if key in payload and payload[key] is False:
            issues.append(f"{key}=false")

    replicate_seed = payload.get("replicate_seed")
    if expected_seed is not None:
        try:
            recorded_seed = int(replicate_seed)
        except (TypeError, ValueError):
            if require_seed:
                issues.append("missing or invalid replicate_seed")
        else:
            if recorded_seed != expected_seed:
                issues.append(
                    f"replicate seed mismatch: expected {expected_seed}, got {recorded_seed}"
                )
    return issues


def local_model_integrity_issues(
    result_path: Path,
    payload: dict[str, Any],
    *,
    expected_interventions: int = 5,
    expected_seed: int | None = None,
    expected_model: str | None = None,
    require_seed: bool = True,
    require_raw_responses: bool = True,
    check_artifacts: bool = True,
) -> list[str]:
    """Validate the protocol and local-model provenance for one final result."""
    issues = protocol_integrity_issues(
        payload,
        expected_interventions=expected_interventions,
        expected_seed=expected_seed,
        require_seed=require_seed,
    )
    if check_artifacts:
        issues.extend(artifact_integrity_issues(result_path, payload))
    if require_raw_responses:
        nonempty_raw = raw_response_count(result_path, payload)
        if nonempty_raw != expected_interventions:
            issues.append(
                f"expected {expected_interventions} nonempty raw responses, got {nonempty_raw}"
            )

    if expected_model and not model_provenance_matches(
        result_path, payload, expected_model
    ):
        issues.append(f"configured model provenance not found: {expected_model}")
    return issues
