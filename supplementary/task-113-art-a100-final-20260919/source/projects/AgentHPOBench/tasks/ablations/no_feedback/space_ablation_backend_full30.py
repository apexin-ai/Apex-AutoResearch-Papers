from __future__ import annotations

import copy
import math
from typing import Any


CORE_PRIORITY = [
    "learning_rate",
    "lr",
    "actor_lr",
    "weight_decay",
    "batch_size",
    "dropout",
    "temperature",
    "warmup_ratio",
    "label_smoothing",
    "entropy_coef",
    "entropy_coeff",
    "kl_loss_coef",
    "c",
]

STRUCTURAL_DISCRETE_KEYS = {
    "patch_size",
    "patch_len",
    "period_len",
    "n_heads",
    "down_sampling_window",
    "window_size",
    "rollout_n",
}

BOUNDED_ZERO_ONE_TOKENS = (
    "dropout",
    "ratio",
    "smoothing",
    "top_p",
    "momentum",
    "eta",
)

LOG_RANGE_TOKENS = (
    "learning_rate",
    "actor_lr",
    "weight_decay",
    "scale",
    "coef",
    "coeff",
)


def _choices(spec: Any) -> list[Any]:
    if isinstance(spec, dict) and "choices" in spec:
        return list(spec.get("choices") or [])
    if isinstance(spec, (list, tuple)):
        return list(spec)
    return []


def _wrap_like(spec: Any, values: list[Any]) -> Any:
    if isinstance(spec, dict) and "choices" in spec:
        result = dict(spec)
        result["choices"] = values
        return result
    return values


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def _same(left: Any, right: Any) -> bool:
    if _is_number(left) and _is_number(right):
        return math.isclose(float(left), float(right), rel_tol=1e-12, abs_tol=1e-12)
    return left == right


def _dedupe(values: list[Any]) -> list[Any]:
    result: list[Any] = []
    for value in values:
        if not any(_same(value, previous) for previous in result):
            result.append(value)
    return result


def _baseline_choice(values: list[Any], baseline: Any) -> Any:
    for value in values:
        if _same(value, baseline):
            return value
    numeric = [value for value in values if _is_number(value)]
    if _is_number(baseline) and numeric:
        return min(numeric, key=lambda value: abs(float(value) - float(baseline)))
    return values[0]


def _distance(left: Any, right: Any) -> float:
    if _is_number(left) and _is_number(right):
        a, b = float(left), float(right)
        if a > 0 and b > 0:
            return abs(math.log(a) - math.log(b))
        return abs(a - b)
    return 0.0 if _same(left, right) else 1.0


def _narrow_space(search_space: dict[str, Any], base_config: dict[str, Any]) -> dict[str, Any]:
    keys = list(search_space)
    priority = {name: index for index, name in enumerate(CORE_PRIORITY)}
    ranked = sorted(
        enumerate(keys),
        key=lambda item: (priority.get(item[1].lower(), len(priority) + item[0]), item[0]),
    )
    tunable = {key for _, key in ranked[: min(3, len(ranked))]}
    result: dict[str, Any] = {}
    for key, spec in search_space.items():
        values = _choices(spec)
        if not values:
            result[key] = copy.deepcopy(spec)
            continue
        baseline = _baseline_choice(values, base_config.get(key))
        if key not in tunable or len(values) == 1:
            narrowed = [baseline]
        else:
            alternatives = [value for value in values if not _same(value, baseline)]
            nearest = min(alternatives, key=lambda value: _distance(value, baseline)) if alternatives else baseline
            narrowed = _dedupe([baseline, nearest])
        result[key] = _wrap_like(spec, narrowed)
    return result


def _cast_numeric(value: float, original_values: list[Any]) -> int | float:
    numeric = [item for item in original_values if _is_number(item)]
    if numeric and all(isinstance(item, int) and not isinstance(item, bool) for item in numeric):
        return int(round(value))
    return float(f"{value:.12g}")


def _midpoint_additions(key: str, values: list[Any]) -> list[Any]:
    if key.lower() in STRUCTURAL_DISCRETE_KEYS:
        return []
    numeric = sorted({float(value) for value in values if _is_number(value)})
    additions: list[Any] = []
    for left, right in zip(numeric, numeric[1:]):
        midpoint = (left + right) / 2.0
        candidate = _cast_numeric(midpoint, values)
        if float(candidate) > left and float(candidate) < right:
            additions.append(candidate)
    return additions


def _range_additions(key: str, values: list[Any]) -> list[Any]:
    numeric = sorted({float(value) for value in values if _is_number(value)})
    if not numeric:
        return []
    lower_key = key.lower()
    minimum, maximum = numeric[0], numeric[-1]
    additions: list[float] = []

    if lower_key == "batch_size":
        if minimum >= 2:
            additions.append(max(1.0, minimum / 2.0))
    elif lower_key == "c" or any(token in lower_key for token in LOG_RANGE_TOKENS):
        if minimum > 0:
            additions.append(minimum / 2.0)
        if maximum > 0:
            additions.append(maximum * 2.0)
    elif any(token in lower_key for token in BOUNDED_ZERO_ONE_TOKENS):
        low_step = numeric[1] - minimum if len(numeric) > 1 else max(minimum, 0.1)
        high_step = maximum - numeric[-2] if len(numeric) > 1 else max(maximum, 0.1)
        additions.extend([max(0.0, minimum - low_step), min(1.0, maximum + high_step)])
    elif lower_key == "temperature":
        low_step = numeric[1] - minimum if len(numeric) > 1 else max(minimum, 0.1)
        high_step = maximum - numeric[-2] if len(numeric) > 1 else max(maximum, 0.1)
        additions.extend([max(0.0, minimum - low_step), maximum + high_step])
    elif lower_key == "cfg" or lower_key.endswith("_weight"):
        low_step = numeric[1] - minimum if len(numeric) > 1 else max(minimum, 0.5)
        high_step = maximum - numeric[-2] if len(numeric) > 1 else max(maximum, 0.5)
        additions.extend([max(0.0, minimum - low_step), maximum + high_step])

    return [_cast_numeric(value, values) for value in additions]


def _wide_space(search_space: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, spec in search_space.items():
        values = _choices(spec)
        additions = _midpoint_additions(key, values) + _range_additions(key, values)
        result[key] = _wrap_like(spec, _dedupe(values + additions))
    return result


def apply_space_variant(
    task_name: str,
    search_space: dict[str, Any],
    base_config: dict[str, Any],
    variant: str,
) -> dict[str, Any]:
    del task_name
    normalized = str(variant or "original").strip().lower()
    if normalized in {"original", "orig", "default"}:
        return copy.deepcopy(search_space)
    if normalized == "narrow":
        return _narrow_space(search_space, base_config)
    if normalized in {"wide", "expanded"}:
        return _wide_space(search_space)
    raise ValueError(f"Unknown space variant: {variant!r}")
