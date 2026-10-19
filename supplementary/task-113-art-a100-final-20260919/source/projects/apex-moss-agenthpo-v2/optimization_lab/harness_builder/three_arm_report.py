from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import fmean
from typing import Mapping, Sequence

from .three_arm import THREE_ARM_VALIDITY_POLICY


ARMS = ("A", "B-frozen", "B-online")
ROUNDS_PER_ARM = 8
MIN_VALID_ROUNDS_PER_ARM = 4
MIN_PAIRED_LEARNING_TASKS = 5
RELATIVE_EPSILON = 1e-12
COMPOSITION_KIND = "three_arm_composition_manifest"
COMPOSITION_SCHEMA_VERSION = 1
COMPOSITION_PREFIX_LENGTH = 6


def _has_numeric_score(point: dict[str, object]) -> bool:
    value = point.get("score")
    return bool(
        point.get("correct") is True
        and isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _read_json_object(path: Path, *, description: str) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"invalid {description}: {path}") from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"{description} must be a JSON object")
    return payload


def _load_sealed_task(
    receipt_path: Path,
    *,
    expected_stream_index: int,
    source_segment: str | None = None,
    expected_receipt_sha256: str | None = None,
    require_arm_hashes: bool = False,
) -> tuple[dict[str, object], int]:
    actual_receipt_sha256 = _sha256_file(receipt_path)
    if (
        expected_receipt_sha256 is not None
        and actual_receipt_sha256 != expected_receipt_sha256
    ):
        raise RuntimeError(
            f"instance receipt hash mismatch at stream index {expected_stream_index}"
        )
    receipt = _read_json_object(receipt_path, description="instance receipt")
    item = receipt.get("stream_item")
    if not isinstance(item, dict):
        raise RuntimeError("instance receipt is missing stream_item")
    if item.get("stream_index") != expected_stream_index:
        raise RuntimeError("three-arm report stream is not contiguous")

    try:
        task_result: dict[str, object] = {
            "stream_index": item["stream_index"],
            "suite": item["suite"],
            "task_index": int(item["block_index"]) + 1,
            "task_id": item["task_id"],
            "instance_id": item["instance_id"],
            "learning_mode": item["learning_mode"],
        }
    except (KeyError, TypeError, ValueError) as exc:
        raise RuntimeError("instance receipt has an invalid stream_item") from exc
    if source_segment is not None:
        task_result["source_segment"] = source_segment
        task_result["instance_receipt_sha256"] = actual_receipt_sha256

    expected_arm_hashes = receipt.get("arm_receipt_sha256s")
    if require_arm_hashes:
        if not isinstance(expected_arm_hashes, dict) or set(expected_arm_hashes) != set(
            ARMS
        ):
            raise RuntimeError("instance receipt must bind exactly three arm receipts")

    round_total = 0
    for arm in ARMS:
        arm_path = receipt_path.parent / "arms" / f"{arm}.json"
        if not arm_path.is_file():
            raise RuntimeError("three-arm campaign is not fully sealed")
        if require_arm_hashes:
            expected_arm_hash = expected_arm_hashes.get(arm)
            if (
                not isinstance(expected_arm_hash, str)
                or len(expected_arm_hash) != 64
                or _sha256_file(arm_path) != expected_arm_hash
            ):
                raise RuntimeError(
                    f"arm receipt hash mismatch at stream index {expected_stream_index}: {arm}"
                )
        payload = _read_json_object(arm_path, description="arm receipt")
        curve = payload.get("curve")
        rounds = curve.get("rounds") if isinstance(curve, dict) else None
        if not isinstance(rounds, list) or len(rounds) != ROUNDS_PER_ARM:
            raise RuntimeError("each sealed arm must contain exactly eight rounds")
        if not all(isinstance(point, dict) for point in rounds):
            raise RuntimeError("each round must be a JSON object")
        values = [float(point["score"]) for point in rounds if _has_numeric_score(point)]
        valid_rounds = len(values)
        sufficient = valid_rounds >= MIN_VALID_ROUNDS_PER_ARM
        task_result[f"{arm}_valid_rounds"] = valid_rounds
        task_result[f"{arm}_invalid_rounds"] = ROUNDS_PER_ARM - valid_rounds
        task_result[f"{arm}_validity_status"] = (
            "sufficient_validity" if sufficient else "insufficient_validity"
        )
        task_result[f"{arm}_valid_mean"] = fmean(values) if values else None
        task_result[f"{arm}_best_score"] = max(values) if values else None
        round_total += len(rounds)

    frozen = task_result["B-frozen_valid_mean"]
    online = task_result["B-online_valid_mean"]
    paired_sufficient = (
        task_result["B-frozen_validity_status"] == "sufficient_validity"
        and task_result["B-online_validity_status"] == "sufficient_validity"
    )
    if paired_sufficient and isinstance(frozen, float) and isinstance(online, float):
        advantage = online - frozen
        task_result["online_minus_frozen"] = advantage
        task_result["relative_online_advantage"] = (
            advantage / abs(frozen) if abs(frozen) > RELATIVE_EPSILON else None
        )
    else:
        task_result["online_minus_frozen"] = None
        task_result["relative_online_advantage"] = None
    return task_result, round_total


def _load_task_results(artifact_root: Path) -> list[dict[str, object]]:
    task_results: list[dict[str, object]] = []
    instance_root = artifact_root.resolve(strict=True) / "formal" / "instances"
    receipt_paths = sorted(instance_root.glob("*/instance_receipt.json"))
    if len(receipt_paths) != 24:
        raise RuntimeError(
            "three-arm campaign is not fully sealed at 24 tasks x 3 arms x 8 rounds"
        )

    round_total = 0
    for expected_stream_index, receipt_path in enumerate(receipt_paths):
        task_result, task_round_total = _load_sealed_task(
            receipt_path, expected_stream_index=expected_stream_index
        )
        round_total += task_round_total
        task_results.append(task_result)

    if round_total != 576:
        raise RuntimeError(
            "three-arm campaign is not fully sealed at 24 tasks x 3 arms x 8 rounds"
        )
    return task_results


def _resolve_segment_file(root: Path, relative_path: object) -> Path:
    if not isinstance(relative_path, str) or not relative_path:
        raise RuntimeError("composition receipt relative_path must be a non-empty string")
    relative = Path(relative_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise RuntimeError("composition receipt path must remain inside its segment root")
    resolved_root = root.resolve(strict=True)
    try:
        resolved = (resolved_root / relative).resolve(strict=True)
        resolved.relative_to(resolved_root)
    except (FileNotFoundError, ValueError) as exc:
        raise RuntimeError("composition receipt path is missing or escapes its segment") from exc
    if not resolved.is_file():
        raise RuntimeError("composition receipt path must identify a file")
    return resolved


def _load_composition_manifest(
    composition_manifest_path: Path,
    *,
    segment_roots: Mapping[str, Path],
) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, object]]:
    manifest_path = composition_manifest_path.resolve(strict=True)
    manifest = _read_json_object(manifest_path, description="composition manifest")
    if manifest.get("schema_version") != COMPOSITION_SCHEMA_VERSION:
        raise RuntimeError("unsupported composition manifest schema_version")
    if manifest.get("kind") != COMPOSITION_KIND:
        raise RuntimeError("invalid composition manifest kind")
    if manifest.get("prefix_length") != COMPOSITION_PREFIX_LENGTH:
        raise RuntimeError("composition manifest must bind a six-instance prefix")

    segments = manifest.get("segments")
    if not isinstance(segments, list) or len(segments) != 2:
        raise RuntimeError("composition manifest must declare exactly two segments")
    role_to_segment: dict[str, str] = {}
    for segment in segments:
        if not isinstance(segment, dict) or set(segment) != {"segment_id", "role"}:
            raise RuntimeError("composition segment declaration is invalid")
        segment_id = segment.get("segment_id")
        role = segment.get("role")
        if (
            not isinstance(segment_id, str)
            or not segment_id
            or role not in {"source_prefix", "successor_suffix"}
            or role in role_to_segment
        ):
            raise RuntimeError("composition segment declaration is invalid")
        role_to_segment[str(role)] = segment_id
    if set(role_to_segment) != {"source_prefix", "successor_suffix"}:
        raise RuntimeError("composition manifest must bind source and successor roles")
    if set(segment_roots) != set(role_to_segment.values()):
        raise RuntimeError("segment roots must exactly match composition segment IDs")
    resolved_roots = {
        segment_id: Path(root).resolve(strict=True)
        for segment_id, root in segment_roots.items()
    }
    if len(set(resolved_roots.values())) != 2:
        raise RuntimeError("source and successor segment roots must be distinct")

    entries = manifest.get("instances")
    if not isinstance(entries, list) or len(entries) != 24:
        raise RuntimeError("composition manifest must reference exactly 24 instances")
    task_results: list[dict[str, object]] = []
    seen_receipts: set[tuple[str, Path]] = set()
    seen_instance_ids: set[str] = set()
    round_total = 0
    for expected_stream_index, entry in enumerate(entries):
        if not isinstance(entry, dict) or set(entry) != {
            "stream_index",
            "source_segment",
            "instance_receipt",
        }:
            raise RuntimeError(
                "composition entries may contain only receipt references, not copied artifacts"
            )
        if entry.get("stream_index") != expected_stream_index:
            raise RuntimeError("composition stream must be contiguous from zero through 23")
        expected_role = (
            "source_prefix"
            if expected_stream_index < COMPOSITION_PREFIX_LENGTH
            else "successor_suffix"
        )
        source_segment = entry.get("source_segment")
        if source_segment != role_to_segment[expected_role]:
            raise RuntimeError("composition source/successor boundary is invalid")
        receipt_ref = entry.get("instance_receipt")
        if not isinstance(receipt_ref, dict) or set(receipt_ref) != {
            "relative_path",
            "sha256",
        }:
            raise RuntimeError("composition instance_receipt must be a path/hash reference")
        expected_sha256 = receipt_ref.get("sha256")
        if not isinstance(expected_sha256, str) or len(expected_sha256) != 64:
            raise RuntimeError("composition instance receipt sha256 is invalid")
        receipt_path = _resolve_segment_file(
            resolved_roots[str(source_segment)], receipt_ref.get("relative_path")
        )
        if receipt_path.name != "instance_receipt.json":
            raise RuntimeError("composition references must identify instance receipts")
        receipt_identity = (str(source_segment), receipt_path)
        if receipt_identity in seen_receipts:
            raise RuntimeError("composition must not reference an instance receipt twice")
        seen_receipts.add(receipt_identity)
        task_result, task_round_total = _load_sealed_task(
            receipt_path,
            expected_stream_index=expected_stream_index,
            source_segment=str(source_segment),
            expected_receipt_sha256=expected_sha256,
            require_arm_hashes=True,
        )
        instance_id = str(task_result["instance_id"])
        if instance_id in seen_instance_ids:
            raise RuntimeError("composition instance IDs must be unique")
        seen_instance_ids.add(instance_id)
        task_result["instance_receipt_relative_path"] = str(
            receipt_ref["relative_path"]
        )
        task_results.append(task_result)
        round_total += task_round_total

    if round_total != 576:
        raise RuntimeError(
            "three-arm composition is not fully sealed at 24 tasks x 3 arms x 8 rounds"
        )

    excluded = manifest.get("excluded_consumed_tail", [])
    if not isinstance(excluded, list) or not all(
        isinstance(item, dict) for item in excluded
    ):
        raise RuntimeError("excluded_consumed_tail must be a list of audit objects")
    excluded_audit: list[dict[str, object]] = []
    for item in excluded:
        if item.get("learning_import") is not False or item.get(
            "performance_import"
        ) is not False:
            raise RuntimeError(
                "excluded consumed tail must be barred from learning and performance"
            )
        source_segment = item.get("source_segment")
        if source_segment not in resolved_roots:
            raise RuntimeError("excluded consumed tail has an unknown source segment")
        excluded_audit.append(dict(item))

    provenance = {
        "schema_version": COMPOSITION_SCHEMA_VERSION,
        "manifest_sha256": _sha256_file(manifest_path),
        "prefix_length": COMPOSITION_PREFIX_LENGTH,
        "source_prefix_segment": role_to_segment["source_prefix"],
        "successor_suffix_segment": role_to_segment["successor_suffix"],
        "receipt_materialization": "references_only_no_copy",
    }
    return task_results, excluded_audit, provenance


def _slope(points: list[tuple[int, float]]) -> float:
    if len(points) < 2:
        raise ValueError("a growth slope requires at least two tasks")
    x_mean = fmean(point[0] for point in points)
    y_mean = fmean(point[1] for point in points)
    numerator = sum(
        (index - x_mean) * (value - y_mean) for index, value in points
    )
    denominator = sum((index - x_mean) ** 2 for index, _value in points)
    return numerator / denominator


def _phase_summary(
    rows: list[dict[str, object]], *, minimum_paired_tasks: int
) -> dict[str, object]:
    paired = [
        row for row in rows if isinstance(row["online_minus_frozen"], float)
    ]
    sufficient = len(paired) >= minimum_paired_tasks
    base: dict[str, object] = {
        "task_count": len(rows),
        "paired_valid_task_count": len(paired),
        "minimum_paired_task_count": minimum_paired_tasks,
        "validity_status": (
            "sufficient_validity" if sufficient else "insufficient_validity"
        ),
    }
    empty_metrics = {
        "B-frozen_valid_mean_across_tasks": None,
        "B-online_valid_mean_across_tasks": None,
        "mean_online_minus_frozen": None,
        "first_task_online_minus_frozen": None,
        "last_task_online_minus_frozen": None,
        "online_advantage_slope_per_task": None,
        "first_to_last_advantage_change": None,
        "mean_relative_online_advantage": None,
        "relative_online_advantage_slope_per_task": None,
    }
    if not sufficient:
        return {**base, **empty_metrics}

    advantages = [float(row["online_minus_frozen"]) for row in paired]
    advantage_points = [
        (int(row["task_index"]), float(row["online_minus_frozen"]))
        for row in paired
    ]
    numeric_relative = [
        (int(row["task_index"]), float(row["relative_online_advantage"]))
        for row in paired
        if isinstance(row["relative_online_advantage"], float)
    ]
    first_advantage = rows[0]["online_minus_frozen"]
    last_advantage = rows[-1]["online_minus_frozen"]
    metrics = {
        "B-frozen_valid_mean_across_tasks": fmean(
            float(row["B-frozen_valid_mean"]) for row in paired
        ),
        "B-online_valid_mean_across_tasks": fmean(
            float(row["B-online_valid_mean"]) for row in paired
        ),
        "mean_online_minus_frozen": fmean(advantages),
        "first_task_online_minus_frozen": first_advantage,
        "last_task_online_minus_frozen": last_advantage,
        "online_advantage_slope_per_task": _slope(advantage_points),
        "first_to_last_advantage_change": (
            float(last_advantage) - float(first_advantage)
            if isinstance(first_advantage, float)
            and isinstance(last_advantage, float)
            else None
        ),
        "mean_relative_online_advantage": (
            fmean(value for _index, value in numeric_relative)
            if numeric_relative
            else None
        ),
        "relative_online_advantage_slope_per_task": (
            _slope(numeric_relative) if len(numeric_relative) >= 2
            else None
        ),
    }
    return {**base, **metrics}


def _benchmark_summaries(
    task_results: list[dict[str, object]],
) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    suite_order: list[str] = []
    for row in task_results:
        suite = str(row["suite"])
        if suite not in grouped:
            suite_order.append(suite)
        grouped[suite].append(row)

    if len(suite_order) != 3:
        raise RuntimeError("three-arm report requires exactly three benchmarks")
    summaries: list[dict[str, object]] = []
    for suite in suite_order:
        rows = sorted(grouped[suite], key=lambda row: int(row["task_index"]))
        if [int(row["task_index"]) for row in rows] != list(range(1, 9)):
            raise RuntimeError("each benchmark must contain task positions one through eight")
        if [row["learning_mode"] for row in rows] != ["online"] * 6 + ["sealed"] * 2:
            raise RuntimeError("each benchmark must use six learning then two sealed tasks")
        learning = _phase_summary(
            rows[:6], minimum_paired_tasks=MIN_PAIRED_LEARNING_TASKS
        )
        learning["first_learning_task_online_minus_frozen"] = learning.pop(
            "first_task_online_minus_frozen"
        )
        learning["sixth_learning_task_online_minus_frozen"] = learning.pop(
            "last_task_online_minus_frozen"
        )
        learning["first_to_sixth_advantage_change"] = learning.pop(
            "first_to_last_advantage_change"
        )
        sealed = _phase_summary(rows[6:], minimum_paired_tasks=1)
        sealed["seventh_task_online_minus_frozen"] = sealed.pop(
            "first_task_online_minus_frozen"
        )
        sealed["eighth_task_online_minus_frozen"] = sealed.pop(
            "last_task_online_minus_frozen"
        )
        sealed["seventh_to_eighth_advantage_change"] = sealed.pop(
            "first_to_last_advantage_change"
        )
        summaries.append(
            {
                "suite": suite,
                "learning": learning,
                "sealed_holdout": sealed,
            }
        )
    return summaries


def _write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )


def _write_results_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _format(value: object) -> str:
    return f"{float(value):.6f}" if isinstance(value, (int, float)) else "n/a"


def _suite_svg(rows: list[dict[str, object]]) -> str:
    width, height = 900, 360
    left, right, top, bottom = 72, 25, 25, 55
    values = [
        float(row[f"{arm}_valid_mean"])
        for row in rows
        for arm in ARMS
        if row[f"{arm}_validity_status"] == "sufficient_validity"
        and isinstance(row[f"{arm}_valid_mean"], float)
    ]
    if not values:
        return (
            '<svg viewBox="0 0 900 120" role="img" '
            'aria-label="No comparable valid task metrics">'
            '<text x="450" y="65" text-anchor="middle">'
            "No arm met the 4/8 validity threshold</text></svg>"
        )
    low, high = min(values), max(values)
    padding = max((high - low) * 0.08, abs(high) * 0.02, 0.05)
    low -= padding
    high += padding
    span = high - low

    def x(task_index: int) -> float:
        return left + (task_index - 1) * (width - left - right) / 7

    def y(value: float) -> float:
        return top + (high - value) * (height - top - bottom) / span

    colors = {"A": "#64748b", "B-frozen": "#2563eb", "B-online": "#dc2626"}
    parts = [f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="Eight-round task means">']
    for tick in range(5):
        value = low + span * tick / 4
        yp = y(value)
        parts.append(f'<line x1="{left}" y1="{yp:.1f}" x2="{width-right}" y2="{yp:.1f}" stroke="#e2e8f0"/>')
        parts.append(f'<text x="{left-9}" y="{yp+4:.1f}" text-anchor="end">{value:.3f}</text>')
    boundary = (x(6) + x(7)) / 2
    parts.append(f'<line x1="{boundary:.1f}" y1="{top}" x2="{boundary:.1f}" y2="{height-bottom}" stroke="#0f172a" stroke-dasharray="6 5"/>')
    for task_index in range(1, 9):
        parts.append(f'<text x="{x(task_index):.1f}" y="{height-22}" text-anchor="middle">T{task_index}</text>')
    for arm in ARMS:
        arm_points = [
            (int(row["task_index"]), float(row[f"{arm}_valid_mean"]))
            for row in rows
            if row[f"{arm}_validity_status"] == "sufficient_validity"
            and isinstance(row[f"{arm}_valid_mean"], float)
        ]
        if len(arm_points) >= 2:
            points = " ".join(
                f"{x(task_index):.1f},{y(value):.1f}"
                for task_index, value in arm_points
            )
            parts.append(
                f'<polyline points="{points}" fill="none" '
                f'stroke="{colors[arm]}" stroke-width="4"/>'
            )
        for task_index, value in arm_points:
            parts.append(
                f'<circle cx="{x(task_index):.1f}" cy="{y(value):.1f}" '
                f'r="5" fill="{colors[arm]}"/>'
            )
    parts.append("</svg>")
    return "".join(parts)


def _summary_markdown(summary: dict[str, object]) -> str:
    lines = [
        "# Harness Builder three-arm benchmark summary",
        "",
        "Each task/arm gets eight attempts. Mean and best use only valid numeric rounds and are comparable only with at least 4/8 valid rounds. Below that threshold the task/arm is `insufficient_validity`. Raw score scales are never pooled across benchmarks.",
        "",
        "| Benchmark | Learning B-frozen mean | Learning B-online mean | Mean B-online − B-frozen | Advantage slope/task | T6 − T1 advantage | Mean relative advantage | Sealed mean advantage |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for benchmark in summary["benchmarks"]:
        learning = benchmark["learning"]
        sealed = benchmark["sealed_holdout"]
        lines.append(
            "| "
            + str(benchmark["suite"])
            + " | "
            + " | ".join(
                _format(value)
                for value in (
                    learning["B-frozen_valid_mean_across_tasks"],
                    learning["B-online_valid_mean_across_tasks"],
                    learning["mean_online_minus_frozen"],
                    learning["online_advantage_slope_per_task"],
                    learning["first_to_sixth_advantage_change"],
                    learning["mean_relative_online_advantage"],
                    sealed["mean_online_minus_frozen"],
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "The first six tasks are test-then-learn. Tasks seven and eight are score-only sealed holdouts. Cross-benchmark comparison uses only each benchmark's relative B-online advantage; raw benchmark scores remain separate.",
            "",
        ]
    )
    return "\n".join(lines)


def _html_document(
    summary: dict[str, object], task_results: list[dict[str, object]]
) -> str:
    by_suite: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in task_results:
        by_suite[str(row["suite"])].append(row)
    sections: list[str] = []
    for benchmark in summary["benchmarks"]:
        suite = str(benchmark["suite"])
        rows = sorted(by_suite[suite], key=lambda row: int(row["task_index"]))
        learning = benchmark["learning"]
        row_html = "".join(
            "<tr>"
            f'<td>{int(row["task_index"])}</td>'
            f'<td>{html.escape(str(row["task_id"]))}</td>'
            f'<td>{html.escape(str(row["learning_mode"]))}</td>'
            f'<td>{_format(row["A_valid_mean"])}</td>'
            f'<td>{_format(row["A_best_score"])}</td>'
            f'<td>{_format(row["B-frozen_valid_mean"])}</td>'
            f'<td>{_format(row["B-frozen_best_score"])}</td>'
            f'<td>{_format(row["B-online_valid_mean"])}</td>'
            f'<td>{_format(row["B-online_best_score"])}</td>'
            f'<td>{int(row["B-frozen_valid_rounds"])}/8; '
            f'{html.escape(str(row["B-frozen_validity_status"]))}</td>'
            f'<td>{int(row["B-online_valid_rounds"])}/8; '
            f'{html.escape(str(row["B-online_validity_status"]))}</td>'
            f'<td>{_format(row["online_minus_frozen"])}</td>'
            "</tr>"
            for row in rows
        )
        sections.append(
            f'<section><h2>{html.escape(suite)}</h2>'
            f'<p>Learning-task mean advantage: {_format(learning["mean_online_minus_frozen"])}; '
            f'growth slope/task: {_format(learning["online_advantage_slope_per_task"])}; '
            f'T6 − T1 advantage: {_format(learning["first_to_sixth_advantage_change"])}.</p>'
            + _suite_svg(rows)
            + '<p class="legend"><span class="a">A</span> <span class="frozen">B-frozen</span> <span class="online">B-online</span>; dashed line separates learning from sealed holdout.</p>'
            + '<table><thead><tr><th>Task</th><th>ID</th><th>Mode</th><th>A mean</th><th>A best</th><th>B-frozen mean</th><th>B-frozen best</th><th>B-online mean</th><th>B-online best</th><th>B-frozen validity</th><th>B-online validity</th><th>Difference</th></tr></thead><tbody>'
            + row_html
            + "</tbody></table></section>"
        )
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>HB three-arm benchmark curves</title>
<style>body{{font:16px system-ui;max-width:1100px;margin:40px auto;color:#0f172a}}section{{margin:42px 0}}svg{{width:100%;height:auto}}table{{border-collapse:collapse;width:100%}}td,th{{padding:7px 10px;border:1px solid #cbd5e1;text-align:right}}td:nth-child(2),td:nth-child(3),th:nth-child(2),th:nth-child(3){{text-align:left}}.legend span{{font-weight:700;margin-right:14px}}.a{{color:#64748b}}.frozen{{color:#2563eb}}.online{{color:#dc2626}}</style></head>
<body><h1>Harness Builder three-arm benchmark curves</h1>
<p>Each plotted point is the valid-only mean for a task/arm that met the 4/8 threshold. Invalid rounds remain in reliability counts but never enter performance means. Raw score axes are benchmark-specific.</p>
{''.join(sections)}
<p>Primary comparison: B-online minus B-frozen across the first six test-then-learn tasks. Tasks seven and eight are score-only holdouts.</p>
</body></html>"""


def _validate_benchmark_inventory(
    task_results: list[dict[str, object]],
) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    suite_order: list[str] = []
    for row in task_results:
        suite = str(row["suite"])
        if suite not in grouped:
            suite_order.append(suite)
        grouped[suite].append(row)
    if len(suite_order) != 3:
        raise RuntimeError("three-arm report requires exactly three benchmarks")
    inventories: list[dict[str, object]] = []
    for suite in suite_order:
        rows = sorted(grouped[suite], key=lambda row: int(row["task_index"]))
        if [int(row["task_index"]) for row in rows] != list(range(1, 9)):
            raise RuntimeError("each benchmark must contain task positions one through eight")
        if [row["learning_mode"] for row in rows] != ["online"] * 6 + [
            "sealed"
        ] * 2:
            raise RuntimeError("each benchmark must use six learning then two sealed tasks")
        inventories.append(
            {
                "suite": suite,
                "task_count": 8,
                "learning_task_count": 6,
                "sealed_task_count": 2,
                "within_benchmark_task_aggregation": "none",
            }
        )
    return inventories


def _arm_result_rows(
    task_results: list[dict[str, object]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for task in task_results:
        for arm in ARMS:
            valid_rounds = int(task[f"{arm}_valid_rounds"])
            rows.append(
                {
                    "stream_index": task["stream_index"],
                    "suite": task["suite"],
                    "task_index": task["task_index"],
                    "task_id": task["task_id"],
                    "instance_id": task["instance_id"],
                    "learning_mode": task["learning_mode"],
                    "source_segment": task["source_segment"],
                    "instance_receipt_sha256": task["instance_receipt_sha256"],
                    "arm": arm,
                    "valid_mean": task[f"{arm}_valid_mean"],
                    "best_score": task[f"{arm}_best_score"],
                    "compliant_rounds": valid_rounds,
                    "compliant_rounds_display": f"{valid_rounds}/{ROUNDS_PER_ARM}",
                    "invalid_rounds": task[f"{arm}_invalid_rounds"],
                    "validity_status": task[f"{arm}_validity_status"],
                    "performance_eligible": task[f"{arm}_validity_status"]
                    == "sufficient_validity",
                }
            )
    return rows


def _composite_summary_markdown(summary: dict[str, object]) -> str:
    lines = [
        "# Harness Builder three-arm composite report",
        "",
        "This report references sealed receipts from the source prefix and successor suffix; it does not copy either segment's artifacts. Every row is one benchmark instance/arm. Means and maxima use valid numeric rounds only. Rows below 4/8 remain descriptively visible but are `insufficient_validity` and ineligible for inferential comparison.",
        "",
        "| Benchmark | Instance | Arm | Mean | Best | Compliant rounds | Validity | Source segment |",
        "|---|---|---|---:|---:|---:|---|---|",
    ]
    for row in summary["arm_results"]:
        lines.append(
            "| "
            + " | ".join(
                (
                    str(row["suite"]),
                    str(row["task_id"]),
                    str(row["arm"]),
                    _format(row["valid_mean"]),
                    _format(row["best_score"]),
                    str(row["compliant_rounds_display"]),
                    str(row["validity_status"]),
                    str(row["source_segment"]),
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "No raw scores are averaged across tasks within a benchmark or across benchmarks.",
            "",
            "## Excluded consumed tail",
            "",
        ]
    )
    excluded = summary["excluded_consumed_tail"]
    if not excluded:
        lines.append("None.")
    else:
        lines.extend(
            [
                "| Instance/operation | Reason | Model calls | Evaluator transactions | Learning import | Performance import |",
                "|---|---|---:|---:|---|---|",
            ]
        )
        for item in excluded:
            identity = item.get("instance_id", item.get("operation_id", "n/a"))
            lines.append(
                "| "
                + " | ".join(
                    (
                        str(identity),
                        str(item.get("reason", "excluded")),
                        str(item.get("model_calls", item.get("charged_usage", "n/a"))),
                        str(item.get("evaluator_transactions", "n/a")),
                        str(item.get("learning_import")),
                        str(item.get("performance_import")),
                    )
                )
                + " |"
            )
    lines.append("")
    return "\n".join(lines)


def _composite_html_document(summary: dict[str, object]) -> str:
    by_suite: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in summary["arm_results"]:
        by_suite[str(row["suite"])].append(row)
    sections: list[str] = []
    for benchmark in summary["benchmarks"]:
        suite = str(benchmark["suite"])
        rows = sorted(
            by_suite[suite],
            key=lambda row: (int(row["task_index"]), ARMS.index(str(row["arm"]))),
        )
        row_html = "".join(
            "<tr>"
            f'<td>{int(row["task_index"])}</td>'
            f'<td>{html.escape(str(row["task_id"]))}</td>'
            f'<td>{html.escape(str(row["arm"]))}</td>'
            f'<td>{_format(row["valid_mean"])}</td>'
            f'<td>{_format(row["best_score"])}</td>'
            f'<td>{html.escape(str(row["compliant_rounds_display"]))}</td>'
            f'<td>{html.escape(str(row["validity_status"]))}</td>'
            f'<td>{html.escape(str(row["source_segment"]))}</td>'
            "</tr>"
            for row in rows
        )
        sections.append(
            f'<section><h2>{html.escape(suite)}</h2>'
            '<table><thead><tr><th>Task</th><th>ID</th><th>Arm</th><th>Mean</th><th>Best</th><th>Compliant rounds</th><th>Validity</th><th>Source segment</th></tr></thead><tbody>'
            + row_html
            + "</tbody></table></section>"
        )
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>HB three-arm composite report</title>
<style>body{{font:16px system-ui;max-width:1200px;margin:40px auto;color:#0f172a}}section{{margin:42px 0}}table{{border-collapse:collapse;width:100%}}td,th{{padding:7px 10px;border:1px solid #cbd5e1;text-align:right}}td:nth-child(2),td:nth-child(3),td:nth-child(7),td:nth-child(8),th:nth-child(2),th:nth-child(3),th:nth-child(7),th:nth-child(8){{text-align:left}}</style></head>
<body><h1>Harness Builder three-arm composite report</h1>
<p>Each row is one instance/arm. Values below 4/8 remain descriptive and are marked insufficient. Source receipts are referenced by hash and are not copied. No within-benchmark or cross-benchmark raw-score average is reported.</p>
{''.join(sections)}
</body></html>"""


def generate_three_arm_report(*, artifact_root: Path, output_root: Path) -> dict[str, object]:
    task_results = _load_task_results(artifact_root)
    benchmarks = _benchmark_summaries(task_results)
    relative_benchmark_means = [
        float(benchmark["learning"]["mean_relative_online_advantage"])
        for benchmark in benchmarks
        if isinstance(benchmark["learning"]["mean_relative_online_advantage"], float)
    ]
    summary: dict[str, object] = {
        "schema_version": 3,
        "task_count": 24,
        "arm_count": 3,
        "rounds_per_arm": ROUNDS_PER_ARM,
        "task_mean_definition": {
            "attempts_per_arm": ROUNDS_PER_ARM,
            "valid_only": True,
            "invalid_incorrect_missing_or_non_numeric_score": "excluded_from_performance_mean",
            "descriptive_values_below_validity_threshold": True,
            "inferential_eligibility_requires_minimum_valid_rounds": MIN_VALID_ROUNDS_PER_ARM,
        },
        "validity_policy": dict(THREE_ARM_VALIDITY_POLICY),
        "learning_policy": "balanced_interleaved_score_then_distill_B-online_before_next_unseen_task",
        "sealed_holdout_policy": "tasks_seven_and_eight_per_suite_score_only_no_learning",
        "primary_comparison": "B-online_valid_mean_minus_B-frozen_valid_mean_for_paired_tasks_meeting_4_of_8",
        "benchmarks": benchmarks,
        "cross_benchmark": {
            "raw_scores_combined": False,
            "comparison_metric": "relative_online_advantage",
            "relative_online_advantage_definition": "(B-online_valid_mean - B-frozen_valid_mean) / abs(B-frozen_valid_mean)",
            "undefined_when_abs_frozen_at_most": RELATIVE_EPSILON,
            "macro_mean_learning_relative_advantage": (
                fmean(relative_benchmark_means) if relative_benchmark_means else None
            ),
        },
        "task_results": task_results,
    }
    curve_payload = {
        "schema_version": 2,
        "point_definition": "valid-only descriptive mean and best; plotted comparison points require at least four of eight valid attempts",
        "invalid_round_score": "excluded_from_performance_mean",
        "validity_policy": dict(THREE_ARM_VALIDITY_POLICY),
        "benchmarks": [
            {
                "suite": benchmark["suite"],
                "learning_growth": benchmark["learning"],
                "points": [
                    row for row in task_results if row["suite"] == benchmark["suite"]
                ],
            }
            for benchmark in benchmarks
        ],
    }

    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    _write_results_csv(output_root / "results.csv", task_results)
    _write_json(output_root / "score_curve.json", curve_payload)
    _write_json(output_root / "summary.json", summary)
    (output_root / "summary.md").write_text(
        _summary_markdown(summary), encoding="utf-8"
    )
    (output_root / "score_curve.html").write_text(
        _html_document(summary, task_results), encoding="utf-8"
    )
    return summary


def generate_three_arm_composite_report(
    *,
    composition_manifest_path: Path,
    segment_roots: Mapping[str, Path],
    output_root: Path,
) -> dict[str, object]:
    """Generate one report from immutable source/successor receipt references.

    ``segment_roots`` is deliberately supplied out-of-band.  The content-addressed
    composition manifest contains only segment identifiers and relative paths, so
    it remains portable and does not disclose host paths.
    """

    task_results, excluded_tail, provenance = _load_composition_manifest(
        composition_manifest_path, segment_roots=segment_roots
    )
    benchmarks = _validate_benchmark_inventory(task_results)
    arm_results = _arm_result_rows(task_results)
    if len(arm_results) != 72:
        raise RuntimeError("three-arm composition must contain exactly 72 arm results")
    summary: dict[str, object] = {
        "schema_version": 4,
        "report_kind": "three_arm_successor_composite",
        "task_count": 24,
        "arm_count": 3,
        "arm_result_count": 72,
        "rounds_per_arm": ROUNDS_PER_ARM,
        "total_round_count": 576,
        "task_mean_definition": {
            "attempts_per_arm": ROUNDS_PER_ARM,
            "valid_only": True,
            "invalid_incorrect_missing_or_non_numeric_score": "excluded_from_descriptive_mean_and_best",
            "descriptive_values_below_validity_threshold": True,
            "inferential_eligibility_requires_minimum_valid_rounds": MIN_VALID_ROUNDS_PER_ARM,
        },
        "validity_policy": dict(THREE_ARM_VALIDITY_POLICY),
        "benchmark_aggregation": {
            "within_benchmark_task_means": False,
            "cross_benchmark_raw_score_means": False,
            "reporting_unit": "instance_arm",
        },
        "benchmarks": benchmarks,
        "composition": provenance,
        "excluded_consumed_tail": excluded_tail,
        "task_results": task_results,
        "arm_results": arm_results,
    }
    curve_payload = {
        "schema_version": 3,
        "report_kind": "three_arm_successor_composite",
        "point_definition": "valid-only descriptive instance/arm values; comparison eligibility requires four of eight valid rounds",
        "within_benchmark_task_aggregation": "none",
        "composition": provenance,
        "benchmarks": [
            {
                "suite": benchmark["suite"],
                "points": [
                    row
                    for row in task_results
                    if row["suite"] == benchmark["suite"]
                ],
            }
            for benchmark in benchmarks
        ],
    }

    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    _write_results_csv(output_root / "results.csv", arm_results)
    _write_json(output_root / "score_curve.json", curve_payload)
    _write_json(output_root / "summary.json", summary)
    (output_root / "summary.md").write_text(
        _composite_summary_markdown(summary), encoding="utf-8"
    )
    (output_root / "score_curve.html").write_text(
        _composite_html_document(summary), encoding="utf-8"
    )
    return summary


def _parse_segment_roots(values: Sequence[str]) -> dict[str, Path]:
    roots: dict[str, Path] = {}
    for value in values:
        segment_id, separator, raw_path = value.partition("=")
        if not separator or not segment_id or not raw_path or segment_id in roots:
            raise ValueError("--segment-root must be a unique SEGMENT_ID=PATH binding")
        roots[segment_id] = Path(raw_path)
    return roots


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate sealed three-arm benchmark curves")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--artifact-root", type=Path)
    source.add_argument("--composition-manifest", type=Path)
    parser.add_argument(
        "--segment-root",
        action="append",
        default=[],
        metavar="SEGMENT_ID=PATH",
        help="out-of-band root binding for a composition segment (repeat twice)",
    )
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.composition_manifest is not None:
        try:
            segment_roots = _parse_segment_roots(args.segment_root)
        except ValueError as exc:
            parser.error(str(exc))
        generate_three_arm_composite_report(
            composition_manifest_path=args.composition_manifest,
            segment_roots=segment_roots,
            output_root=args.output_root,
        )
    else:
        if args.segment_root:
            parser.error("--segment-root requires --composition-manifest")
        generate_three_arm_report(
            artifact_root=args.artifact_root, output_root=args.output_root
        )
    print(args.output_root.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
