from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import stat
import tempfile
from contextlib import ExitStack, contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

from optimization_lab.harness_evolution import HarnessArchive
from optimization_lab.p2b_policy import P2bPolicyArchive, initial_policy

from .meta_train import (
    MetaTrainContract,
    MetaTrainTrajectory,
    MetaTrainTrajectoryArchive,
)


HISTORICAL_POLICY_ID = "hb-gen1-kernelbench-historical-all-lanes-v1"
_SHA256 = re.compile(r"[0-9a-f]{64}")
_VERSION = re.compile(r"v\d{3}")
_PRIVATE_TEXT = re.compile(
    r"(?:/home/|/data\d*/|private[_ -](?:evaluator|log)|raw[_ -]response)",
    re.IGNORECASE,
)
_P2B_POLICY_FIELDS = (
    "mode",
    "base_candidate_id",
    "diagnostic_level",
    "mutation_scope",
    "enabled_skills",
    "tool_plan",
    "memory_views",
    "force_restart",
    "structural_change",
)
_PROFILE_FIELDS = (
    "status",
    "level",
    "structural_signature",
    "structure",
    "kernel_count",
    "launch_count",
    "registers_per_thread",
    "register_spills",
    "shared_memory_bytes",
    "num_warps",
    "num_stages",
    "theoretical_occupancy_pct",
    "achieved_occupancy_pct",
    "dram_throughput_pct",
    "l2_hit_rate_pct",
    "warp_stall_summary",
    "timeline_summary",
    "compiler_summary",
    "missing_metrics",
)


class HistoricalImportBlocked(RuntimeError):
    """A public, reason-coded failure to prove the frozen historical source."""

    def __init__(self, code: str):
        if not re.fullmatch(r"[a-z0-9_]+", code):
            raise ValueError("historical import blocker code is invalid")
        super().__init__(code)
        self.code = code


def _blocked(code: str) -> None:
    raise HistoricalImportBlocked(code)


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


def _sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _strict_json(content: bytes, blocker: str) -> Any:
    try:
        return json.loads(
            content.decode("utf-8"),
            parse_constant=lambda _value: (_ for _ in ()).throw(ValueError()),
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError):
        _blocked(blocker)


def _strict_bool(value: Any, blocker: str) -> bool:
    if type(value) is not bool:
        _blocked(blocker)
    return value


def _text_tuple(value: Any, blocker: str) -> tuple[str, ...]:
    if (
        not isinstance(value, list)
        or not value
        or not all(isinstance(item, str) and item for item in value)
        or len(set(value)) != len(value)
    ):
        _blocked(blocker)
    return tuple(value)


def _require_sha(value: Any, blocker: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        _blocked(blocker)
    return value


@dataclass(frozen=True)
class HistoricalFrozenSource:
    ledger_filename: str
    ledger_sha256: str
    event_count: int
    plan_filename: str
    plan_sha256: str
    terminal_event_ids: tuple[str, ...]

    @classmethod
    def from_dict(cls, payload: Any) -> "HistoricalFrozenSource":
        if not isinstance(payload, dict) or set(payload) != {
            "event_count",
            "ledger_filename",
            "ledger_sha256",
            "plan_filename",
            "plan_sha256",
            "terminal_event_ids",
        }:
            _blocked("historical_source_manifest_fields_differ")
        event_count = payload["event_count"]
        if not isinstance(event_count, int) or isinstance(event_count, bool) or event_count <= 0:
            _blocked("historical_source_event_count_invalid")
        ledger_filename = payload["ledger_filename"]
        plan_filename = payload["plan_filename"]
        if (
            not isinstance(ledger_filename, str)
            or not isinstance(plan_filename, str)
            or Path(ledger_filename).name != ledger_filename
            or Path(plan_filename).name != plan_filename
        ):
            _blocked("historical_source_filename_invalid")
        return cls(
            ledger_filename=ledger_filename,
            ledger_sha256=_require_sha(
                payload["ledger_sha256"], "historical_source_ledger_hash_invalid"
            ),
            event_count=event_count,
            plan_filename=plan_filename,
            plan_sha256=_require_sha(
                payload["plan_sha256"], "historical_source_plan_hash_invalid"
            ),
            terminal_event_ids=_text_tuple(
                payload["terminal_event_ids"],
                "historical_source_terminal_events_invalid",
            ),
        )


@dataclass(frozen=True)
class HistoricalTaskBinding:
    legacy_task_id: str
    source_instance_id: str
    source_sha256: str
    instance_descriptor: tuple[str, ...]
    p1_lane_ids: tuple[str, ...]
    p2_lane_ids: tuple[str, ...]
    p2b_lane_ids: tuple[str, ...]
    expected_terminal_summary_counts: dict[str, int]

    @classmethod
    def from_dict(cls, payload: Any) -> "HistoricalTaskBinding":
        if not isinstance(payload, dict) or set(payload) != {
            "expected_terminal_summary_counts",
            "instance_descriptor",
            "legacy_task_id",
            "p1_lane_ids",
            "p2_lane_ids",
            "p2b_lane_ids",
            "source_instance_id",
            "source_sha256",
        }:
            _blocked("historical_task_manifest_fields_differ")
        legacy_task_id = payload["legacy_task_id"]
        source_instance_id = payload["source_instance_id"]
        if (
            not isinstance(legacy_task_id, str)
            or not legacy_task_id.startswith("kernelbench_")
            or not isinstance(source_instance_id, str)
            or not source_instance_id.startswith("kernelbench:level")
        ):
            _blocked("historical_task_identity_invalid")
        lane_groups = {
            "P1": _text_tuple(payload["p1_lane_ids"], "historical_p1_lanes_invalid"),
            "P2": _text_tuple(payload["p2_lane_ids"], "historical_p2_lanes_invalid"),
            "P2B": _text_tuple(
                payload["p2b_lane_ids"], "historical_p2b_lanes_invalid"
            ),
        }
        prefixes = {"P1": "p1:", "P2": "p2:", "P2B": "p2b:"}
        for phase, lanes in lane_groups.items():
            if any(
                not lane.startswith(f"{prefixes[phase]}{legacy_task_id}:")
                for lane in lanes
            ):
                _blocked("historical_lane_task_binding_invalid")
        counts = payload["expected_terminal_summary_counts"]
        if (
            not isinstance(counts, dict)
            or set(counts) != {"P1", "P2", "P2B"}
            or any(
                not isinstance(value, int)
                or isinstance(value, bool)
                or value <= 0
                for value in counts.values()
            )
        ):
            _blocked("historical_terminal_summary_counts_invalid")
        return cls(
            legacy_task_id=legacy_task_id,
            source_instance_id=source_instance_id,
            source_sha256=_require_sha(
                payload["source_sha256"], "historical_task_source_hash_invalid"
            ),
            instance_descriptor=_text_tuple(
                payload["instance_descriptor"],
                "historical_instance_descriptor_invalid",
            ),
            p1_lane_ids=lane_groups["P1"],
            p2_lane_ids=lane_groups["P2"],
            p2b_lane_ids=lane_groups["P2B"],
            expected_terminal_summary_counts=dict(counts),
        )


@dataclass(frozen=True)
class HistoricalImportContract:
    policy_id: str
    manifest_sha256: str
    source_order: tuple[str, ...]
    winner_selection: bool
    pilot: HistoricalFrozenSource
    p2b: HistoricalFrozenSource
    tasks: tuple[HistoricalTaskBinding, ...]

    @classmethod
    def from_json(cls, path: Path) -> "HistoricalImportContract":
        try:
            content = Path(path).read_bytes()
        except OSError:
            _blocked("historical_source_manifest_missing")
        payload = _strict_json(content, "historical_source_manifest_invalid")
        if not isinstance(payload, dict) or set(payload) != {
            "policy_id",
            "schema_version",
            "selection_policy",
            "sources",
            "tasks",
        }:
            _blocked("historical_source_manifest_fields_differ")
        if payload["schema_version"] != 1 or payload["policy_id"] != HISTORICAL_POLICY_ID:
            _blocked("historical_source_policy_changed")
        selection = payload["selection_policy"]
        if not isinstance(selection, dict) or set(selection) != {
            "aggregate_unit",
            "include_terminal_artifact_failures",
            "source_order",
            "terminal_fact_policy",
            "winner_selection",
        }:
            _blocked("historical_selection_policy_fields_differ")
        source_order = _text_tuple(
            selection["source_order"], "historical_source_order_invalid"
        )
        if (
            source_order != ("pilot:P1", "pilot:P2", "p2b:P2B")
            or selection["aggregate_unit"]
            != "one_all_lanes_trajectory_per_task"
            or selection["terminal_fact_policy"]
            != "all_public_terminal_attempts_and_rounds_in_append_only_ledger_order"
            or _strict_bool(
                selection["include_terminal_artifact_failures"],
                "historical_artifact_failure_policy_invalid",
            )
            is not True
            or _strict_bool(
                selection["winner_selection"],
                "historical_winner_selection_invalid",
            )
            is not False
        ):
            _blocked("historical_source_policy_changed")
        sources = payload["sources"]
        if not isinstance(sources, dict) or set(sources) != {"pilot", "p2b"}:
            _blocked("historical_sources_invalid")
        tasks_payload = payload["tasks"]
        if not isinstance(tasks_payload, list) or len(tasks_payload) != 2:
            _blocked("historical_tasks_invalid")
        tasks = tuple(HistoricalTaskBinding.from_dict(item) for item in tasks_payload)
        if (
            len({task.legacy_task_id for task in tasks}) != 2
            or len({task.source_instance_id for task in tasks}) != 2
            or len(
                {
                    lane
                    for task in tasks
                    for lane in (*task.p1_lane_ids, *task.p2_lane_ids, *task.p2b_lane_ids)
                }
            )
            != sum(
                len(task.p1_lane_ids) + len(task.p2_lane_ids) + len(task.p2b_lane_ids)
                for task in tasks
            )
        ):
            _blocked("historical_task_or_lane_duplicates")
        return cls(
            policy_id=payload["policy_id"],
            manifest_sha256=_sha256_bytes(content),
            source_order=source_order,
            winner_selection=False,
            pilot=HistoricalFrozenSource.from_dict(sources["pilot"]),
            p2b=HistoricalFrozenSource.from_dict(sources["p2b"]),
            tasks=tasks,
        )

    def bind_meta_train(self, contract: MetaTrainContract) -> None:
        if (
            contract.historical_policy_id != self.policy_id
            or contract.historical_source_manifest_sha256 != self.manifest_sha256
            or contract.historical_source_manifest
            != "optimization_lab/harness_builder/data/"
            "historical_trajectory_sources_v1.json"
        ):
            _blocked("historical_meta_train_manifest_binding_differs")
        expected = tuple(source.instance_id for source in contract.historical_sources)
        if tuple(task.source_instance_id for task in self.tasks) != expected:
            _blocked("historical_meta_train_source_order_differs")
        by_id = {source.instance_id: source for source in contract.historical_sources}
        if any(
            by_id[task.source_instance_id].source_sha256 != task.source_sha256
            for task in self.tasks
        ):
            _blocked("historical_meta_train_source_hash_differs")

    def source_facts(self) -> dict[str, Any]:
        return {
            "pilot": {
                "ledger_sha256": self.pilot.ledger_sha256,
                "event_count": self.pilot.event_count,
                "plan_sha256": self.pilot.plan_sha256,
            },
            "p2b": {
                "ledger_sha256": self.p2b.ledger_sha256,
                "event_count": self.p2b.event_count,
                "plan_sha256": self.p2b.plan_sha256,
            },
        }


@dataclass(frozen=True)
class _Event:
    index: int
    event_id: str
    event_type: str
    payload: dict[str, Any]


@dataclass(frozen=True)
class _BuiltSummary:
    primary_index: int
    summary: dict[str, Any]
    event_indices: tuple[int, ...]


@dataclass(frozen=True)
class _PilotCandidateFact:
    task_id: str
    candidate_id: str
    candidate_sha256: str
    correct: bool
    speedup: float | None


@dataclass(frozen=True)
class HistoricalImportResult:
    trajectories: tuple[MetaTrainTrajectory, ...]
    phase_counts: dict[str, dict[str, int]]


@dataclass(frozen=True)
class HistoricalPrepareOutcome:
    report: dict[str, Any]
    report_sha256: str
    report_relative_path: str
    trajectories: tuple[MetaTrainTrajectory, ...]


def _parse_ledger(content: bytes, expected_count: int, blocker: str) -> tuple[_Event, ...]:
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        _blocked(blocker)
    lines = text.splitlines()
    if len(lines) != expected_count or any(not line.strip() for line in lines):
        _blocked(blocker)
    events: list[_Event] = []
    seen: set[str] = set()
    for index, line in enumerate(lines):
        payload = _strict_json(line.encode("utf-8"), blocker)
        if not isinstance(payload, dict) or set(payload) != {
            "event_id",
            "event_type",
            "payload",
            "recorded_at",
        }:
            _blocked(blocker)
        event_id = payload["event_id"]
        event_type = payload["event_type"]
        if (
            not isinstance(event_id, str)
            or not event_id
            or event_id in seen
            or not isinstance(event_type, str)
            or not event_type
            or not isinstance(payload["payload"], dict)
        ):
            _blocked(blocker)
        seen.add(event_id)
        events.append(_Event(index, event_id, event_type, payload["payload"]))
    return tuple(events)


def _events_of(events: tuple[_Event, ...], event_type: str) -> tuple[_Event, ...]:
    return tuple(event for event in events if event.event_type == event_type)


def _one(items: list[Any] | tuple[Any, ...], blocker: str) -> Any:
    if len(items) != 1:
        _blocked(blocker)
    return items[0]


def _safe_relative(value: Any, blocker: str) -> Path:
    if not isinstance(value, str):
        _blocked(blocker)
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        _blocked(blocker)
    return path


def _regular_file(path: Path, root: Path, blocker: str) -> Path:
    try:
        if path.is_symlink():
            _blocked(blocker)
        resolved = path.resolve(strict=True)
        if not resolved.is_relative_to(root.resolve()):
            _blocked(blocker)
        mode = resolved.stat().st_mode
        if not stat.S_ISREG(mode):
            _blocked(blocker)
        return resolved
    except OSError:
        _blocked(blocker)


def _artifact_from_value(value: Any, root: Path, blocker: str) -> Path:
    if not isinstance(value, str) or not value:
        _blocked(blocker)
    path = Path(value)
    if not path.is_absolute():
        path = root / _safe_relative(value, blocker)
    return _regular_file(path, root, blocker)


def _verify_artifact(
    value: Any,
    root: Path,
    expected_sha256: Any,
    blocker: str,
) -> Path:
    expected = _require_sha(expected_sha256, blocker)
    path = _artifact_from_value(value, root, blocker)
    try:
        actual = _sha256_bytes(path.read_bytes())
    except OSError:
        _blocked(blocker)
    if actual != expected:
        _blocked(blocker)
    return path


@contextmanager
def _exclusive_lock(path: Path, blocker: str) -> Iterator[None]:
    try:
        if path.is_symlink():
            _blocked(blocker)
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(path, flags)
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            os.close(fd)
            _blocked(blocker)
    except OSError:
        _blocked(blocker)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            _blocked(blocker)
        yield
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def _read_source_file(root: Path, filename: str, blocker: str) -> bytes:
    path = _regular_file(root / filename, root, blocker)
    try:
        return path.read_bytes()
    except OSError:
        _blocked(blocker)


def _public_guard(payload: Any) -> None:
    encoded = json.dumps(payload, ensure_ascii=False, allow_nan=False, sort_keys=True)
    if _PRIVATE_TEXT.search(encoded):
        _blocked("historical_public_payload_contains_private_text")


def _structure_item(payload: dict[str, Any]) -> str:
    _public_guard(payload)
    return json.dumps(
        payload, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
    )


def _version_from_candidate(candidate_id: str, blocker: str) -> str:
    match = re.search(r"-(v\d{3})$", candidate_id)
    if match is None:
        _blocked(blocker)
    return match.group(1)


def _feedback_public(feedback: Any, blocker: str) -> dict[str, Any]:
    if not isinstance(feedback, dict):
        _blocked(blocker)
    correct = feedback.get("correct")
    if type(correct) is not bool:
        _blocked(blocker)
    speedup = feedback.get("speedup_vs_eager")
    if speedup is not None and (
        not isinstance(speedup, (int, float))
        or isinstance(speedup, bool)
        or float(speedup) <= 0
    ):
        _blocked(blocker)
    outcome = feedback.get("outcome")
    if outcome not in {"valid", "incorrect", "policy_rejected", "environment_invalid"}:
        _blocked(blocker)
    if correct and (outcome != "valid" or speedup is None):
        _blocked(blocker)
    if not correct and speedup is not None:
        _blocked(blocker)
    gpu_seconds = feedback.get("gpu_seconds")
    if (
        not isinstance(gpu_seconds, (int, float))
        or isinstance(gpu_seconds, bool)
        or float(gpu_seconds) < 0
    ):
        _blocked(blocker)
    result = {
        "compiled": bool(feedback.get("compiled")),
        "correct": correct,
        "speedup": float(speedup) if speedup is not None else None,
        "outcome": outcome,
        "failure_reason": "none" if correct else outcome,
        "stage_reached": feedback.get("stage_reached"),
        "gpu_seconds": float(gpu_seconds),
    }
    if not isinstance(result["stage_reached"], str) or not result["stage_reached"]:
        _blocked(blocker)
    return result


def _resource_cost(
    *, model_calls: int, gpu_seconds: float, api_cost_usd: float = 0.0
) -> dict[str, Any]:
    if model_calls < 0 or gpu_seconds < 0 or api_cost_usd < 0:
        _blocked("historical_resource_cost_invalid")
    return {
        "model_calls": model_calls,
        "gpu_seconds": float(gpu_seconds),
        "api_cost_usd": float(api_cost_usd),
    }


def _event_ids(events: tuple[_Event, ...]) -> tuple[str, ...]:
    ordered = sorted(events, key=lambda item: item.index)
    if len({event.event_id for event in ordered}) != len(ordered):
        _blocked("historical_summary_provenance_duplicates")
    return tuple(event.event_id for event in ordered)


def _close_float(left: Any, right: Any) -> bool:
    if left is None or right is None:
        return left is right
    if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
        return False
    return abs(float(left) - float(right)) <= 1e-12 * max(1.0, abs(float(left)))


def _json_equal(left: Any, right: Any) -> bool:
    try:
        return json.dumps(
            left, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
        ) == json.dumps(
            right, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
        )
    except (TypeError, ValueError):
        return False


class HistoricalTrajectoryImporter:
    """Build the two frozen all-lanes public trajectories without external calls."""

    def __init__(
        self,
        *,
        project_root: Path,
        pilot_root: Path,
        p2b_root: Path,
        meta_train_contract: MetaTrainContract,
        source_contract: HistoricalImportContract,
    ) -> None:
        self.project_root = Path(project_root).resolve()
        self.pilot_root = Path(pilot_root).resolve()
        self.p2b_root = Path(p2b_root).resolve()
        if (
            not self.project_root.is_dir()
            or not self.pilot_root.is_dir()
            or not self.p2b_root.is_dir()
            or self.pilot_root == self.p2b_root
        ):
            _blocked("historical_source_root_invalid")
        self.meta_train_contract = meta_train_contract
        self.source_contract = source_contract
        source_contract.bind_meta_train(meta_train_contract)
        self.task_by_legacy = {
            task.legacy_task_id: task for task in source_contract.tasks
        }

    def build(self) -> HistoricalImportResult:
        with ExitStack() as stack:
            stack.enter_context(
                _exclusive_lock(
                    self.pilot_root / ".ledger.lock", "pilot_writer_lock_unavailable"
                )
            )
            stack.enter_context(
                _exclusive_lock(
                    self.p2b_root / ".p2b-runner.lock",
                    "p2b_runner_lock_unavailable",
                )
            )
            stack.enter_context(
                _exclusive_lock(
                    self.p2b_root / ".ledger.lock", "p2b_ledger_lock_unavailable"
                )
            )
            first = self._read_frozen_sources()
            pilot_events = _parse_ledger(
                first["pilot_ledger"],
                self.source_contract.pilot.event_count,
                "pilot_ledger_invalid",
            )
            p2b_events = _parse_ledger(
                first["p2b_ledger"],
                self.source_contract.p2b.event_count,
                "p2b_ledger_invalid",
            )
            campaign = _strict_json(first["pilot_plan"], "campaign_plan_invalid")
            p2b_plan = _strict_json(first["p2b_plan"], "p2b_plan_invalid")
            self._validate_terminal_sources(pilot_events, p2b_events)
            campaign_lanes = self._validate_campaign_plan(campaign)
            p2b_lanes = self._validate_p2b_plan_shape(p2b_plan)
            pilot_summaries, pilot_facts = self._build_pilot(
                events=pilot_events,
                campaign_lanes=campaign_lanes,
            )
            self._validate_p2b_frozen_candidates(p2b_plan, pilot_facts)
            p2b_summaries = self._build_p2b(
                events=p2b_events,
                p2b_lanes=p2b_lanes,
            )
            initial = self._initial_structures(campaign_lanes, p2b_lanes)
            second = self._read_frozen_sources()
            if any(first[name] != second[name] for name in first):
                _blocked("historical_source_changed_during_import")

        trajectories: list[MetaTrainTrajectory] = []
        phase_counts: dict[str, dict[str, int]] = {}
        for task in self.source_contract.tasks:
            summaries = [
                *pilot_summaries[task.legacy_task_id],
                *p2b_summaries[task.legacy_task_id],
            ]
            by_phase = {
                phase: sum(item.summary["phase"] == phase for item in summaries)
                for phase in ("P1", "P2", "P2B")
            }
            if by_phase != task.expected_terminal_summary_counts:
                _blocked("historical_terminal_summary_count_differs")
            all_indices: dict[tuple[str, int], str] = {}
            for item in summaries:
                source_name = "pilot" if item.summary["phase"] in {"P1", "P2"} else "p2b"
                for event_id, event_index in zip(
                    item.summary["event_ids"], item.event_indices, strict=True
                ):
                    key = (source_name, event_index)
                    existing = all_indices.get(key)
                    if existing is not None and existing != event_id:
                        _blocked("historical_provenance_event_rebound")
                    all_indices[key] = event_id
            source_rank = {"pilot": 0, "p2b": 1}
            provenance = tuple(
                event_id
                for (source_name, _index), event_id in sorted(
                    all_indices.items(), key=lambda item: (source_rank[item[0][0]], item[0][1])
                )
            )
            public_summaries = tuple(item.summary for item in summaries)
            _public_guard(public_summaries)
            trajectory = MetaTrainTrajectory.create(
                source_instance_id=task.source_instance_id,
                source_sha256=task.source_sha256,
                instance_descriptor=task.instance_descriptor,
                initial_harness_structure=initial[task.legacy_task_id],
                provenance_event_ids=provenance,
                round_summaries=public_summaries,
                sealed=True,
            )
            trajectories.append(trajectory)
            phase_counts[task.source_instance_id] = by_phase
        return HistoricalImportResult(tuple(trajectories), phase_counts)

    def _read_frozen_sources(self) -> dict[str, bytes]:
        bindings = {
            "pilot_ledger": (
                self.pilot_root,
                self.source_contract.pilot.ledger_filename,
                self.source_contract.pilot.ledger_sha256,
            ),
            "pilot_plan": (
                self.pilot_root,
                self.source_contract.pilot.plan_filename,
                self.source_contract.pilot.plan_sha256,
            ),
            "p2b_ledger": (
                self.p2b_root,
                self.source_contract.p2b.ledger_filename,
                self.source_contract.p2b.ledger_sha256,
            ),
            "p2b_plan": (
                self.p2b_root,
                self.source_contract.p2b.plan_filename,
                self.source_contract.p2b.plan_sha256,
            ),
        }
        result: dict[str, bytes] = {}
        for name, (root, filename, expected_sha) in bindings.items():
            content = _read_source_file(root, filename, f"{name}_missing")
            if _sha256_bytes(content) != expected_sha:
                _blocked(f"{name}_hash_differs")
            result[name] = content
        return result

    def _validate_terminal_sources(
        self,
        pilot_events: tuple[_Event, ...],
        p2b_events: tuple[_Event, ...],
    ) -> None:
        pilot_by_id = {event.event_id: event for event in pilot_events}
        for event_id in self.source_contract.pilot.terminal_event_ids:
            event = pilot_by_id.get(event_id)
            if (
                event is None
                or event.event_type != "phase_changed"
                or event.payload.get("status") != "completed"
                or event.payload.get("phase") not in {"P1", "P2"}
            ):
                _blocked("pilot_terminal_phase_missing")
        if pilot_by_id["phase:P1:completed"].index >= pilot_by_id["phase:P2:completed"].index:
            _blocked("pilot_phase_order_invalid")
        p2b_by_id = {event.event_id: event for event in p2b_events}
        for event_id in self.source_contract.p2b.terminal_event_ids:
            event = p2b_by_id.get(event_id)
            if (
                event is None
                or event.event_type != "p2b_phase_changed"
                or event.payload.get("phase") != "P2B"
                or event.payload.get("status") != "completed"
            ):
                _blocked("p2b_terminal_phase_missing")
        if p2b_events[-1].event_id != self.source_contract.p2b.terminal_event_ids[-1]:
            _blocked("p2b_terminal_phase_not_ledger_tail")

    def _validate_campaign_plan(self, payload: Any) -> dict[str, dict[str, Any]]:
        if not isinstance(payload, dict) or payload.get("schema_version") != 1:
            _blocked("campaign_plan_invalid")
        try:
            if Path(payload["artifact_root"]).resolve() != self.pilot_root:
                _blocked("campaign_plan_artifact_root_differs")
        except (KeyError, TypeError):
            _blocked("campaign_plan_artifact_root_differs")
        if payload.get("execution_ready") is not True:
            _blocked("campaign_plan_not_execution_ready")
        baselines = payload.get("baselines")
        lineages = payload.get("lineages")
        if not isinstance(baselines, list) or not isinstance(lineages, list):
            _blocked("campaign_plan_lanes_invalid")
        expected_p1 = {
            lane for task in self.source_contract.tasks for lane in task.p1_lane_ids
        }
        expected_p2 = {
            lane for task in self.source_contract.tasks for lane in task.p2_lane_ids
        }
        result: dict[str, dict[str, Any]] = {}
        for item in baselines:
            if not isinstance(item, dict):
                _blocked("campaign_baseline_invalid")
            lane_id = item.get("lane_id")
            task_id = item.get("task_id")
            if lane_id not in expected_p1 or task_id not in self.task_by_legacy:
                _blocked("campaign_baseline_binding_differs")
            if lane_id in result:
                _blocked("campaign_lane_duplicate")
            harness_path = _safe_relative(
                item.get("harness_path"), "campaign_harness_path_invalid"
            )
            _verify_artifact(
                str(harness_path),
                self.project_root,
                item.get("harness_sha256"),
                "campaign_harness_hash_differs",
            )
            workflow = item.get("workflow")
            if not isinstance(workflow, list) or not all(
                isinstance(value, str) and value for value in workflow
            ):
                _blocked("campaign_workflow_invalid")
            result[lane_id] = item
        for item in lineages:
            if not isinstance(item, dict):
                _blocked("campaign_lineage_invalid")
            task_id = item.get("task_id")
            lineage_id = item.get("lineage_id")
            lane_id = f"p2:{task_id}:{lineage_id}"
            if lane_id not in expected_p2 or task_id not in self.task_by_legacy:
                _blocked("campaign_lineage_binding_differs")
            if lane_id in result:
                _blocked("campaign_lane_duplicate")
            seed_path = _safe_relative(item.get("seed_path"), "campaign_seed_path_invalid")
            _verify_artifact(
                str(seed_path),
                self.project_root,
                item.get("seed_sha256"),
                "campaign_seed_hash_differs",
            )
            result[lane_id] = {**item, "lane_id": lane_id}
        if set(result) != expected_p1 | expected_p2:
            _blocked("campaign_lane_set_differs")
        return result

    def _validate_p2b_plan_shape(self, payload: Any) -> dict[str, dict[str, Any]]:
        if not isinstance(payload, dict) or payload.get("schema_version") != 1:
            _blocked("p2b_plan_invalid")
        try:
            if (
                Path(payload["artifact_root"]).resolve() != self.p2b_root
                or Path(payload["source_artifact_root"]).resolve() != self.pilot_root
            ):
                _blocked("p2b_plan_artifact_root_differs")
        except (KeyError, TypeError):
            _blocked("p2b_plan_artifact_root_differs")
        if payload.get("execution_ready") is not True:
            _blocked("p2b_plan_not_execution_ready")
        lanes = payload.get("lanes")
        if not isinstance(lanes, list):
            _blocked("p2b_plan_lanes_invalid")
        expected = {
            lane for task in self.source_contract.tasks for lane in task.p2b_lane_ids
        }
        result: dict[str, dict[str, Any]] = {}
        for lane in lanes:
            if not isinstance(lane, dict):
                _blocked("p2b_plan_lane_invalid")
            lane_id = lane.get("lane_id")
            task_id = lane.get("task_id")
            if lane_id not in expected or task_id not in self.task_by_legacy:
                _blocked("p2b_plan_lane_binding_differs")
            if lane_id in result:
                _blocked("p2b_plan_lane_duplicate")
            history_scope = _safe_relative(
                lane.get("history_scope"), "p2b_history_scope_invalid"
            )
            if lane.get("max_rounds") != 8 or not isinstance(lane.get("strategy"), str):
                _blocked("p2b_plan_lane_contract_differs")
            result[lane_id] = {**lane, "history_scope": str(history_scope)}
        if set(result) != expected:
            _blocked("p2b_plan_lane_set_differs")
        return result

    def _validate_candidate_artifact(
        self,
        event: _Event,
        *,
        root: Path,
        p2b: bool,
        history_scope: str | None = None,
    ) -> Path:
        payload = event.payload
        candidate_id = payload.get("candidate_id")
        candidate_sha = _require_sha(
            payload.get("candidate_sha256"), "historical_candidate_hash_invalid"
        )
        if not isinstance(candidate_id, str) or not candidate_id:
            _blocked("historical_candidate_id_invalid")
        if p2b:
            candidate_path_value = payload.get("candidate_path")
            if history_scope is None:
                _blocked("p2b_candidate_history_scope_missing")
            metadata_path = (
                root
                / _safe_relative(history_scope, "p2b_candidate_history_scope_invalid")
                / "metadata"
                / f"{candidate_id}.json"
            )
        else:
            archive = payload.get("archive")
            if not isinstance(archive, dict):
                _blocked("pilot_candidate_archive_invalid")
            candidate_path_value = archive.get("candidate_path")
            metadata_path = _artifact_from_value(
                archive.get("metadata_path"), root, "pilot_candidate_metadata_invalid"
            )
        candidate_path = _verify_artifact(
            candidate_path_value,
            root,
            candidate_sha,
            "historical_candidate_artifact_hash_differs",
        )
        metadata_path = _regular_file(
            metadata_path, root, "historical_candidate_metadata_invalid"
        )
        metadata = _strict_json(
            metadata_path.read_bytes(), "historical_candidate_metadata_invalid"
        )
        if not isinstance(metadata, dict):
            _blocked("historical_candidate_metadata_invalid")
        if (
            metadata.get("candidate_id") != candidate_id
            or metadata.get("candidate_sha256") != candidate_sha
        ):
            _blocked("historical_candidate_metadata_binding_differs")
        bound_path = _artifact_from_value(
            metadata.get("candidate_path"), root, "historical_candidate_metadata_path_invalid"
        )
        if bound_path != candidate_path:
            _blocked("historical_candidate_metadata_path_differs")
        return candidate_path

    def _validate_task_payload(self, payload: Any, task: HistoricalTaskBinding) -> None:
        if not isinstance(payload, dict):
            _blocked("historical_task_payload_invalid")
        if (
            payload.get("task_id") != task.legacy_task_id
            or payload.get("task_sha256") != task.source_sha256
            or payload.get("repository_commit")
            != self.meta_train_contract.repository_commit
        ):
            _blocked("historical_task_payload_binding_differs")

    def _feedback_for_pilot_candidate(
        self,
        *,
        generated: _Event,
        evaluation: _Event,
        completion: _Event,
        correction: _Event | None,
        task: HistoricalTaskBinding,
    ) -> tuple[dict[str, Any], tuple[_Event, ...]]:
        candidate_id = generated.payload["candidate_id"]
        candidate_sha = generated.payload["candidate_sha256"]
        if evaluation.payload.get("candidate_sha256") != candidate_sha:
            _blocked("pilot_evaluation_candidate_hash_differs")
        self._validate_task_payload(evaluation.payload.get("task"), task)
        base_feedback = evaluation.payload.get("feedback")
        completion_feedback = completion.payload.get("feedback")
        if not isinstance(base_feedback, dict) or not isinstance(completion_feedback, dict):
            _blocked("pilot_feedback_invalid")
        for card in (base_feedback, completion_feedback):
            if (
                card.get("candidate_id") != candidate_id
                or card.get("task_id") != task.legacy_task_id
            ):
                _blocked("pilot_feedback_candidate_binding_differs")
        if _feedback_public(base_feedback, "pilot_feedback_invalid") != _feedback_public(
            completion_feedback, "pilot_feedback_invalid"
        ):
            _blocked("pilot_completion_feedback_differs")
        events = [generated, evaluation, completion]
        final_feedback = base_feedback
        if correction is not None:
            payload = correction.payload
            if (
                payload.get("supersedes_event_id") != evaluation.event_id
                or payload.get("candidate_id") != candidate_id
                or payload.get("candidate_sha256") != candidate_sha
                or payload.get("task_id") != task.legacy_task_id
                or payload.get("lane_id") != generated.payload.get("lane_id")
            ):
                _blocked("pilot_correction_binding_differs")
            final_feedback = payload.get("feedback")
            if not isinstance(final_feedback, dict):
                _blocked("pilot_correction_feedback_invalid")
            events.append(correction)
        public = _feedback_public(final_feedback, "pilot_feedback_invalid")
        if not public["correct"] and public["outcome"] == "environment_invalid":
            _blocked("pilot_terminal_environment_result_unresolved")
        return public, tuple(events)

    def _build_pilot(
        self,
        *,
        events: tuple[_Event, ...],
        campaign_lanes: dict[str, dict[str, Any]],
    ) -> tuple[
        dict[str, list[_BuiltSummary]],
        dict[str, _PilotCandidateFact],
    ]:
        p1_lanes = {
            lane: task
            for task in self.source_contract.tasks
            for lane in task.p1_lane_ids
        }
        p2_lanes = {
            lane: task
            for task in self.source_contract.tasks
            for lane in task.p2_lane_ids
        }
        relevant_lanes = set(p1_lanes) | set(p2_lanes)
        generated: dict[str, _Event] = {}
        for event in _events_of(events, "candidate_generated"):
            lane_id = event.payload.get("lane_id")
            if lane_id not in relevant_lanes:
                continue
            candidate_id = event.payload.get("candidate_id")
            if not isinstance(candidate_id, str) or candidate_id in generated:
                _blocked("pilot_candidate_generation_duplicate")
            task = (p1_lanes | p2_lanes)[lane_id]
            if event.payload.get("task_id") != task.legacy_task_id:
                _blocked("pilot_candidate_generation_task_differs")
            self._validate_candidate_artifact(event, root=self.pilot_root, p2b=False)
            generated[candidate_id] = event
        evaluations: dict[str, _Event] = {}
        for event in _events_of(events, "candidate_evaluated"):
            feedback = event.payload.get("feedback")
            candidate_id = feedback.get("candidate_id") if isinstance(feedback, dict) else None
            if candidate_id not in generated:
                continue
            if candidate_id in evaluations:
                _blocked("pilot_candidate_evaluation_duplicate")
            evaluations[candidate_id] = event
        corrections: dict[str, _Event] = {}
        for event in _events_of(events, "candidate_evaluation_corrected"):
            candidate_id = event.payload.get("candidate_id")
            if candidate_id not in generated:
                continue
            if candidate_id in corrections:
                _blocked("pilot_candidate_correction_duplicate")
            corrections[candidate_id] = event
        p2_candidate_completions: dict[str, _Event] = {}
        for event in _events_of(events, "p2_candidate_completed"):
            lane_id = event.payload.get("lane_id")
            if lane_id not in p2_lanes:
                continue
            candidate_id = event.payload.get("candidate_id")
            if (
                not isinstance(candidate_id, str)
                or candidate_id in p2_candidate_completions
            ):
                _blocked("pilot_p2_candidate_completion_duplicate")
            p2_candidate_completions[candidate_id] = event
        harness_events: dict[tuple[str, str], _Event] = {}
        for event in _events_of(events, "harness_generated"):
            lane_id = event.payload.get("lane_id")
            if lane_id not in p2_lanes:
                continue
            version_id = event.payload.get("harness_version_id")
            key = (lane_id, version_id)
            if not isinstance(version_id, str) or key in harness_events:
                _blocked("pilot_harness_generation_duplicate")
            harness_events[key] = event

        summaries = {task.legacy_task_id: [] for task in self.source_contract.tasks}
        facts: dict[str, _PilotCandidateFact] = {}
        represented: set[str] = set()
        used_harness_events: set[tuple[str, str]] = set()
        used_p2_candidate_completions: set[str] = set()
        for completion in events:
            if completion.event_type not in {
                "lane_candidate_completed",
                "p2_lineage_round_completed",
            }:
                continue
            lane_id = completion.payload.get("lane_id")
            if completion.event_type == "lane_candidate_completed":
                if lane_id not in p1_lanes:
                    continue
                phase = "P1"
                task = p1_lanes[lane_id]
            else:
                if lane_id not in p2_lanes:
                    continue
                phase = "P2"
                task = p2_lanes[lane_id]
            candidate_id = completion.payload.get("candidate_id")
            if not isinstance(candidate_id, str) or candidate_id in represented:
                _blocked("pilot_terminal_candidate_duplicate")
            generated_event = generated.get(candidate_id)
            evaluation = evaluations.get(candidate_id)
            if generated_event is None or evaluation is None:
                _blocked("pilot_terminal_candidate_artifact_missing")
            if (
                generated_event.payload.get("lane_id") != lane_id
                or generated_event.payload.get("task_id") != task.legacy_task_id
            ):
                _blocked("pilot_terminal_candidate_lane_differs")
            candidate_sha = generated_event.payload["candidate_sha256"]
            if completion.payload.get("candidate_sha256", candidate_sha) != candidate_sha:
                _blocked("pilot_terminal_candidate_hash_differs")
            feedback, proof_events = self._feedback_for_pilot_candidate(
                generated=generated_event,
                evaluation=evaluation,
                completion=completion,
                correction=corrections.get(candidate_id),
                task=task,
            )
            if phase == "P2":
                candidate_completion = p2_candidate_completions.get(candidate_id)
                if candidate_completion is None:
                    _blocked("pilot_p2_candidate_completion_missing")
                if (
                    candidate_completion.payload.get("lane_id") != lane_id
                    or candidate_completion.payload.get("task_id")
                    != task.legacy_task_id
                    or candidate_completion.payload.get("candidate_sha256")
                    != candidate_sha
                    or _feedback_public(
                        candidate_completion.payload.get("feedback"),
                        "pilot_p2_candidate_completion_feedback_invalid",
                    )
                    != feedback
                ):
                    _blocked("pilot_p2_candidate_completion_binding_differs")
                proof_events = (*proof_events, candidate_completion)
                used_p2_candidate_completions.add(candidate_id)
            version_id = _version_from_candidate(
                candidate_id, "pilot_candidate_version_invalid"
            )
            plan_lane = campaign_lanes[lane_id]
            decision_events: tuple[_Event, ...] = ()
            if phase == "P1":
                decision = {
                    "kind": str(plan_lane.get("kind")),
                    "harness_sha256": _require_sha(
                        plan_lane.get("harness_sha256"), "pilot_harness_hash_invalid"
                    ),
                    "workflow": list(plan_lane.get("workflow", [])),
                    "allow_harness_mutation": False,
                }
                model_calls = 1
            else:
                round_number = completion.payload.get("round_number")
                if round_number != int(version_id[1:]):
                    _blocked("pilot_p2_round_version_differs")
                scope_root = self.pilot_root / _safe_relative(
                    plan_lane.get("history_scope"), "pilot_p2_history_scope_invalid"
                )
                try:
                    version = HarnessArchive(scope_root).load(version_id)
                except (OSError, ValueError):
                    _blocked("pilot_p2_harness_artifact_invalid")
                expected_parent = (
                    None
                    if version_id == "v001"
                    else f"v{int(version_id[1:]) - 1:03d}"
                )
                if (
                    version.parent_version_id != expected_parent
                    or version.sha256 != completion.payload.get("harness_sha256")
                    or completion.payload.get("harness_version_id") != version_id
                    or candidate_completion.payload.get("harness_sha256")
                    != version.sha256
                    or candidate_completion.payload.get("harness_version_id")
                    != version_id
                ):
                    _blocked("pilot_p2_harness_binding_differs")
                if version_id == "v001":
                    if version.sha256 != plan_lane.get("seed_sha256"):
                        _blocked("pilot_p2_seed_binding_differs")
                    model_calls = 1
                else:
                    harness_event = harness_events.get((lane_id, version_id))
                    if harness_event is None:
                        _blocked("pilot_p2_harness_event_missing")
                    if (
                        harness_event.payload.get("task_id") != task.legacy_task_id
                        or harness_event.payload.get("harness_sha256") != version.sha256
                        or harness_event.payload.get("parent_version_id") != expected_parent
                    ):
                        _blocked("pilot_p2_harness_event_binding_differs")
                    decision_events = (harness_event,)
                    used_harness_events.add((lane_id, version_id))
                    model_calls = 2
                decision = {
                    "kind": "task_specialist_harness",
                    "harness_sha256": version.sha256,
                    "parent_version_id": expected_parent,
                }
            api_cost = float(generated_event.payload.get("api_cost_usd", 0.0))
            for event in decision_events:
                api_cost += float(event.payload.get("api_cost_usd", 0.0))
            all_events = tuple(
                sorted(
                    (*proof_events, *decision_events),
                    key=lambda item: item.index,
                )
            )
            event_ids = _event_ids(all_events)
            summary = {
                "phase": phase,
                "lane_id": lane_id,
                "version": version_id,
                "event_ids": list(event_ids),
                "candidate_id": candidate_id,
                "candidate_sha256": candidate_sha,
                "decision": decision,
                "compiled": feedback["compiled"],
                "correct": feedback["correct"],
                "score": feedback["speedup"],
                "outcome": feedback["outcome"],
                "failure_reason": feedback["failure_reason"],
                "stage_reached": feedback["stage_reached"],
                "resource_cost": _resource_cost(
                    model_calls=model_calls,
                    gpu_seconds=feedback["gpu_seconds"],
                    api_cost_usd=api_cost,
                ),
            }
            _public_guard(summary)
            summaries[task.legacy_task_id].append(
                _BuiltSummary(
                    completion.index,
                    summary,
                    tuple(event.index for event in all_events),
                )
            )
            represented.add(candidate_id)
            facts[candidate_id] = _PilotCandidateFact(
                task_id=task.legacy_task_id,
                candidate_id=candidate_id,
                candidate_sha256=candidate_sha,
                correct=feedback["correct"],
                speedup=feedback["speedup"],
            )

        recoveries = [
            event
            for event in _events_of(events, "p2_lineage_recovery_stopped")
            if event.payload.get("lane_id") in p2_lanes
        ]
        for recovery in recoveries:
            lane_id = recovery.payload["lane_id"]
            task = p2_lanes[lane_id]
            round_number = recovery.payload.get("next_round_number")
            version_id = f"v{round_number:03d}" if isinstance(round_number, int) else ""
            if (
                not _VERSION.fullmatch(version_id)
                or recovery.payload.get("reason")
                != "incomplete_harness_generation_preserved"
            ):
                _blocked("pilot_p2_recovery_binding_invalid")
            starts = [
                event
                for event in _events_of(events, "generation_started")
                if event.payload.get("lane_id") == lane_id
                and event.payload.get("generation_kind") == "harness"
                and event.payload.get("harness_version_id") == version_id
            ]
            start = _one(starts, "pilot_p2_recovery_start_missing")
            scope_root = self.pilot_root / _safe_relative(
                campaign_lanes[lane_id].get("history_scope"),
                "pilot_p2_history_scope_invalid",
            )
            if (scope_root / "harness_metadata" / f"{version_id}.json").exists():
                _blocked("pilot_p2_failed_harness_artifact_unexpectedly_exists")
            parent_version = f"v{round_number - 1:03d}"
            try:
                parent = HarnessArchive(scope_root).load(parent_version)
            except (OSError, ValueError):
                _blocked("pilot_p2_recovery_parent_invalid")
            proof_events = tuple(sorted((start, recovery), key=lambda item: item.index))
            summary = {
                "phase": "P2",
                "lane_id": lane_id,
                "version": version_id,
                "event_ids": list(_event_ids(proof_events)),
                "candidate_id": None,
                "candidate_sha256": None,
                "decision": {
                    "kind": "task_specialist_harness_generation",
                    "parent_version_id": parent_version,
                    "parent_harness_sha256": parent.sha256,
                },
                "compiled": False,
                "correct": None,
                "score": None,
                "outcome": "artifact_failure",
                "failure_reason": "incomplete_harness_artifact",
                "stage_reached": "harness_generation",
                "resource_cost": _resource_cost(model_calls=1, gpu_seconds=0.0),
            }
            _public_guard(summary)
            summaries[task.legacy_task_id].append(
                _BuiltSummary(
                    recovery.index,
                    summary,
                    tuple(event.index for event in proof_events),
                )
            )

        if set(generated) != represented or set(evaluations) != represented:
            _blocked("pilot_terminal_attempt_coverage_differs")
        if set(corrections) - represented:
            _blocked("pilot_correction_without_terminal_attempt")
        if set(p2_candidate_completions) != used_p2_candidate_completions:
            _blocked("pilot_p2_candidate_completion_coverage_differs")
        if set(harness_events) != used_harness_events:
            _blocked("pilot_p2_harness_event_coverage_differs")
        completed_lanes = {
            event.payload.get("lane_id")
            for event in _events_of(events, "p2_lineage_completed")
            if event.payload.get("lane_id") in p2_lanes
        }
        if completed_lanes != set(p2_lanes):
            _blocked("pilot_p2_terminal_lane_set_differs")
        for values in summaries.values():
            values.sort(key=lambda item: item.primary_index)
        return summaries, facts

    def _validate_p2b_frozen_candidates(
        self,
        payload: dict[str, Any],
        pilot_facts: dict[str, _PilotCandidateFact],
    ) -> None:
        candidates = payload.get("frozen_candidates")
        lanes = payload.get("lanes")
        if not isinstance(candidates, list) or not isinstance(lanes, list):
            _blocked("p2b_frozen_candidates_invalid")
        frozen: dict[str, dict[str, Any]] = {}
        for item in candidates:
            if not isinstance(item, dict):
                _blocked("p2b_frozen_candidate_invalid")
            candidate_id = item.get("candidate_id")
            task_id = item.get("task_id")
            source_sha = _require_sha(
                item.get("source_sha256"), "p2b_frozen_candidate_hash_invalid"
            )
            if (
                not isinstance(candidate_id, str)
                or candidate_id in frozen
                or task_id not in self.task_by_legacy
            ):
                _blocked("p2b_frozen_candidate_binding_invalid")
            fact = pilot_facts.get(candidate_id)
            if (
                fact is None
                or not fact.correct
                or fact.task_id != task_id
                or fact.candidate_sha256 != source_sha
                or not _close_float(fact.speedup, item.get("speedup"))
            ):
                _blocked("p2b_frozen_candidate_pilot_fact_differs")
            _verify_artifact(
                item.get("source_path"),
                self.pilot_root,
                source_sha,
                "p2b_frozen_candidate_source_hash_differs",
            )
            _verify_artifact(
                item.get("frozen_path"),
                self.p2b_root,
                source_sha,
                "p2b_frozen_candidate_copy_hash_differs",
            )
            expected_phase = "p1" if candidate_id.startswith("p1-") else "p2"
            if item.get("source_phase") != expected_phase:
                _blocked("p2b_frozen_candidate_phase_differs")
            frozen[candidate_id] = item
        for lane in lanes:
            if not isinstance(lane, dict):
                _blocked("p2b_plan_lane_invalid")
            task_id = lane.get("task_id")
            start = lane.get("starting_candidate_id")
            allowed = lane.get("allowed_frozen_candidate_ids")
            if not isinstance(allowed, list) or len(set(allowed)) != len(allowed):
                _blocked("p2b_lane_frozen_candidate_set_invalid")
            for candidate_id in allowed:
                item = frozen.get(candidate_id)
                if item is None or item.get("task_id") != task_id:
                    _blocked("p2b_lane_frozen_candidate_binding_differs")
            if start != "reference":
                item = frozen.get(start)
                if (
                    item is None
                    or item.get("task_id") != task_id
                    or start not in allowed
                    or not _close_float(item.get("speedup"), lane.get("starting_score"))
                ):
                    _blocked("p2b_lane_starting_candidate_binding_differs")
            elif not _close_float(lane.get("starting_score"), 1.0):
                _blocked("p2b_reference_starting_score_differs")

    def _policy_public(self, policy: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(policy, dict) or any(field not in policy for field in _P2B_POLICY_FIELDS):
            _blocked("p2b_public_policy_fields_missing")
        result = json.loads(
            json.dumps(
                {field: policy[field] for field in _P2B_POLICY_FIELDS},
                ensure_ascii=False,
                allow_nan=False,
                sort_keys=True,
            )
        )
        _public_guard(result)
        return result

    def _profile_public(self, profile: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(profile, dict) or any(field not in profile for field in _PROFILE_FIELDS):
            _blocked("p2b_public_profile_fields_missing")
        result = {field: profile[field] for field in _PROFILE_FIELDS}
        _public_guard(result)
        return result

    def _build_p2b(
        self,
        *,
        events: tuple[_Event, ...],
        p2b_lanes: dict[str, dict[str, Any]],
    ) -> dict[str, list[_BuiltSummary]]:
        lane_tasks = {
            lane: task
            for task in self.source_contract.tasks
            for lane in task.p2b_lane_ids
        }
        generated: dict[str, _Event] = {}
        for event in _events_of(events, "p2b_candidate_generated"):
            lane_id = event.payload.get("lane_id")
            if lane_id not in lane_tasks:
                continue
            candidate_id = event.payload.get("candidate_id")
            if not isinstance(candidate_id, str) or candidate_id in generated:
                _blocked("p2b_candidate_generation_duplicate")
            task = lane_tasks[lane_id]
            lane = p2b_lanes[lane_id]
            if event.payload.get("task_id") != task.legacy_task_id:
                _blocked("p2b_candidate_generation_task_differs")
            self._validate_candidate_artifact(
                event,
                root=self.p2b_root,
                p2b=True,
                history_scope=lane["history_scope"],
            )
            generated[candidate_id] = event
        evaluations: dict[str, _Event] = {}
        for event in _events_of(events, "candidate_evaluated"):
            feedback = event.payload.get("feedback")
            candidate_id = feedback.get("candidate_id") if isinstance(feedback, dict) else None
            if candidate_id not in generated:
                continue
            if candidate_id in evaluations:
                _blocked("p2b_candidate_evaluation_duplicate")
            evaluations[candidate_id] = event
        round_events: dict[str, _Event] = {}
        for event in _events_of(events, "p2b_round_completed"):
            lane_id = event.payload.get("lane_id")
            if lane_id not in lane_tasks:
                continue
            candidate_id = event.payload.get("candidate_id")
            if not isinstance(candidate_id, str) or candidate_id in round_events:
                _blocked("p2b_round_terminal_duplicate")
            round_events[candidate_id] = event
        policy_events: dict[tuple[str, str], _Event] = {}
        for event in _events_of(events, "p2b_policy_generated"):
            lane_id = event.payload.get("lane_id")
            if lane_id not in lane_tasks:
                continue
            version_id = event.payload.get("policy_version_id")
            key = (lane_id, version_id)
            if not isinstance(version_id, str) or key in policy_events:
                _blocked("p2b_policy_generation_duplicate")
            policy_events[key] = event
        profile_events: dict[str, _Event] = {}
        for event in _events_of(events, "p2b_profile_completed"):
            lane_id = event.payload.get("lane_id")
            if lane_id not in lane_tasks:
                continue
            candidate_id = event.payload.get("candidate_id")
            if not isinstance(candidate_id, str) or candidate_id in profile_events:
                _blocked("p2b_profile_terminal_duplicate")
            profile_events[candidate_id] = event
        profile_starts: dict[str, _Event] = {}
        for event in _events_of(events, "p2b_profile_started"):
            lane_id = event.payload.get("lane_id")
            if lane_id not in lane_tasks:
                continue
            candidate_id = event.payload.get("candidate_id")
            if not isinstance(candidate_id, str) or candidate_id in profile_starts:
                _blocked("p2b_profile_start_duplicate")
            profile_starts[candidate_id] = event
        recovery_by_lane = {
            event.payload.get("lane_id"): event
            for event in _events_of(events, "p2b_lane_recovery_stopped")
            if event.payload.get("lane_id") in lane_tasks
        }
        if len(recovery_by_lane) != len(
            [
                event
                for event in _events_of(events, "p2b_lane_recovery_stopped")
                if event.payload.get("lane_id") in lane_tasks
            ]
        ):
            _blocked("p2b_lane_recovery_duplicate")

        summaries = {task.legacy_task_id: [] for task in self.source_contract.tasks}
        used_policy_events: set[tuple[str, str]] = set()
        used_completed_profiles: set[str] = set()
        used_incomplete_profiles: set[str] = set()
        represented: set[str] = set()
        successful_call_ids: set[str] = set()
        for candidate_id, generated_event in sorted(
            generated.items(), key=lambda item: item[1].index
        ):
            lane_id = generated_event.payload["lane_id"]
            lane = p2b_lanes[lane_id]
            task = lane_tasks[lane_id]
            evaluation = evaluations.get(candidate_id)
            if evaluation is None:
                _blocked("p2b_candidate_terminal_evaluation_missing")
            candidate_sha = generated_event.payload["candidate_sha256"]
            if evaluation.payload.get("candidate_sha256") != candidate_sha:
                _blocked("p2b_evaluation_candidate_hash_differs")
            self._validate_task_payload(evaluation.payload.get("task"), task)
            feedback_payload = evaluation.payload.get("feedback")
            if (
                not isinstance(feedback_payload, dict)
                or feedback_payload.get("candidate_id") != candidate_id
                or feedback_payload.get("task_id") != task.legacy_task_id
            ):
                _blocked("p2b_feedback_candidate_binding_differs")
            feedback = _feedback_public(feedback_payload, "p2b_feedback_invalid")
            if feedback["outcome"] == "environment_invalid":
                _blocked("p2b_terminal_environment_result_unresolved")
            version_id = generated_event.payload.get("policy_version_id")
            round_number = generated_event.payload.get("round_number")
            if (
                not isinstance(version_id, str)
                or not _VERSION.fullmatch(version_id)
                or round_number != int(version_id[1:])
                or _version_from_candidate(candidate_id, "p2b_candidate_version_invalid")
                != version_id
            ):
                _blocked("p2b_candidate_policy_version_differs")
            scope_root = self.p2b_root / _safe_relative(
                lane["history_scope"], "p2b_history_scope_invalid"
            )
            try:
                version = P2bPolicyArchive(scope_root).load(version_id)
            except (OSError, ValueError):
                _blocked("p2b_policy_artifact_invalid")
            expected_parent = None if version_id == "v001" else f"v{round_number - 1:03d}"
            if (
                version.parent_version_id != expected_parent
                or version.sha256 != generated_event.payload.get("policy_sha256")
            ):
                _blocked("p2b_policy_parent_or_hash_differs")
            decision_events: list[_Event] = []
            if version_id == "v001":
                try:
                    expected_seed = initial_policy(
                        strategy=lane["strategy"],
                        starting_candidate_id=lane["starting_candidate_id"],
                    )
                except ValueError:
                    _blocked("p2b_seed_policy_invalid")
                if version != expected_seed:
                    _blocked("p2b_seed_policy_binding_differs")
                model_calls = 1
            else:
                policy_event = policy_events.get((lane_id, version_id))
                if policy_event is None:
                    _blocked("p2b_policy_event_missing")
                if (
                    policy_event.payload.get("task_id") != task.legacy_task_id
                    or policy_event.payload.get("round_number") != round_number
                    or policy_event.payload.get("policy_sha256") != version.sha256
                    or not _json_equal(
                        policy_event.payload.get("policy"), version.policy.to_dict()
                    )
                ):
                    _blocked("p2b_policy_event_binding_differs")
                decision_events.append(policy_event)
                used_policy_events.add((lane_id, version_id))
                successful_call_ids.add(str(policy_event.payload.get("call_id")))
                model_calls = 2
            allowed_bases = {
                "reference",
                *lane.get("allowed_frozen_candidate_ids", []),
                *(
                    item.payload["candidate_id"]
                    for item in generated.values()
                    if item.payload.get("lane_id") == lane_id
                    and isinstance(item.payload.get("round_number"), int)
                    and item.payload["round_number"] < round_number
                ),
            }
            if version.policy.base_candidate_id not in allowed_bases:
                _blocked("p2b_policy_base_candidate_outside_lane")
            round_event = round_events.get(candidate_id)
            profile_event = profile_events.get(candidate_id)
            proof_events: list[_Event] = [generated_event, evaluation, *decision_events]
            profile_public: dict[str, Any] | None = None
            profile_gpu = 0.0
            score_trend: Any = None
            novelty: Any = None
            terminal_status = "round_sealed"
            failure_reason = feedback["failure_reason"]
            if round_event is not None:
                payload = round_event.payload
                if (
                    payload.get("lane_id") != lane_id
                    or payload.get("task_id") != task.legacy_task_id
                    or payload.get("round_number") != round_number
                    or payload.get("candidate_sha256") != candidate_sha
                    or payload.get("policy_version_id") != version_id
                    or payload.get("policy_sha256") != version.sha256
                    or not _json_equal(payload.get("policy"), version.policy.to_dict())
                    or _feedback_public(payload.get("feedback"), "p2b_round_feedback_invalid")
                    != feedback
                ):
                    _blocked("p2b_round_binding_differs")
                round_profile = payload.get("profile")
                if round_profile is None:
                    if profile_event is not None:
                        _blocked("p2b_unexpected_profile_event")
                else:
                    profile_start = profile_starts.get(candidate_id)
                    if (
                        profile_event is None
                        or profile_start is None
                        or profile_event.payload.get("summary") != round_profile
                    ):
                        _blocked("p2b_profile_event_binding_differs")
                    if (
                        profile_event.payload.get("lane_id") != lane_id
                        or profile_event.payload.get("task_id") != task.legacy_task_id
                        or profile_event.payload.get("candidate_sha256") != candidate_sha
                        or profile_event.payload.get("candidate_id") != candidate_id
                        or profile_start.payload.get("lane_id") != lane_id
                        or profile_start.payload.get("task_id") != task.legacy_task_id
                        or profile_start.payload.get("candidate_sha256") != candidate_sha
                        or profile_start.payload.get("candidate_id") != candidate_id
                        or profile_start.payload.get("call_id")
                        != generated_event.payload.get("call_id")
                        or profile_event.payload.get("call_id")
                        != profile_start.payload.get("call_id")
                    ):
                        _blocked("p2b_profile_candidate_binding_differs")
                    if (
                        round_profile.get("candidate_id") != candidate_id
                        or round_profile.get("candidate_sha256") != candidate_sha
                        or round_profile.get("task_id") != task.legacy_task_id
                        or not _close_float(round_profile.get("speedup"), feedback["speedup"])
                        or not _close_float(
                            round_profile.get("gpu_seconds"),
                            profile_event.payload.get("gpu_seconds"),
                        )
                    ):
                        _blocked("p2b_profile_summary_binding_differs")
                    profile_public = self._profile_public(round_profile)
                    profile_gpu = float(round_profile.get("gpu_seconds", 0.0))
                    proof_events.append(profile_event)
                    used_completed_profiles.add(candidate_id)
                score_trend = payload.get("score_trend")
                novelty = payload.get("novelty")
                _public_guard({"score_trend": score_trend, "novelty": novelty})
                proof_events.append(round_event)
            else:
                recovery = recovery_by_lane.get(lane_id)
                profile_start = profile_starts.get(candidate_id)
                if (
                    recovery is None
                    or profile_start is None
                    or profile_event is not None
                    or recovery.payload.get("task_id") != task.legacy_task_id
                    or profile_start.payload.get("lane_id") != lane_id
                    or profile_start.payload.get("task_id") != task.legacy_task_id
                    or profile_start.payload.get("candidate_id") != candidate_id
                    or profile_start.payload.get("candidate_sha256") != candidate_sha
                    or profile_start.payload.get("call_id")
                    != generated_event.payload.get("call_id")
                ):
                    _blocked("p2b_unsealed_attempt_recovery_binding_differs")
                reserved = profile_start.payload.get("reserved_gpu_seconds")
                if (
                    not isinstance(reserved, (int, float))
                    or isinstance(reserved, bool)
                    or float(reserved) < 0
                ):
                    _blocked("p2b_unsealed_profile_reservation_invalid")
                profile_gpu = float(reserved)
                terminal_status = "attempt_scored_round_unsealed"
                failure_reason = "incomplete_profile_artifact"
                proof_events.extend((profile_start, recovery))
                used_incomplete_profiles.add(candidate_id)
            api_cost = float(generated_event.payload.get("api_cost_usd", 0.0)) + sum(
                float(event.payload.get("api_cost_usd", 0.0))
                for event in decision_events
            )
            successful_call_ids.add(str(generated_event.payload.get("call_id")))
            proof_events = sorted(proof_events, key=lambda item: item.index)
            summary = {
                "phase": "P2B",
                "lane_id": lane_id,
                "version": version_id,
                "event_ids": list(_event_ids(tuple(proof_events))),
                "candidate_id": candidate_id,
                "candidate_sha256": candidate_sha,
                "decision": {
                    "kind": "profiler_guided_policy",
                    "policy_sha256": version.sha256,
                    "parent_version_id": expected_parent,
                    "policy": self._policy_public(version.policy.to_dict()),
                },
                "compiled": feedback["compiled"],
                "correct": feedback["correct"],
                "score": feedback["speedup"],
                "outcome": feedback["outcome"],
                "failure_reason": failure_reason,
                "stage_reached": feedback["stage_reached"],
                "terminal_status": terminal_status,
                "score_trend": score_trend,
                "novelty": novelty,
                "profile": profile_public,
                "resource_cost": _resource_cost(
                    model_calls=model_calls,
                    gpu_seconds=feedback["gpu_seconds"] + profile_gpu,
                    api_cost_usd=api_cost,
                ),
            }
            _public_guard(summary)
            summaries[task.legacy_task_id].append(
                _BuiltSummary(
                    evaluation.index,
                    summary,
                    tuple(event.index for event in proof_events),
                )
            )
            represented.add(candidate_id)

        policy_failures = [
            event
            for event in _events_of(events, "p2b_policy_generation_failed")
            if event.payload.get("lane_id") in lane_tasks
        ]
        stop_events = [
            event
            for event in _events_of(events, "p2b_lane_model_artifact_stopped")
            if event.payload.get("lane_id") in lane_tasks
        ]
        stopped_by_lane = {
            event.payload.get("lane_id"): event
            for event in stop_events
        }
        if (
            len(stopped_by_lane) != len(stop_events)
            or len(stopped_by_lane) != len(policy_failures)
        ):
            _blocked("p2b_artifact_failure_stop_set_differs")
        starts_by_call = {
            event.payload.get("call_id"): event
            for event in _events_of(events, "p2b_model_call_started")
            if event.payload.get("lane_id") in lane_tasks
        }
        if len(starts_by_call) != len(
            [
                event
                for event in _events_of(events, "p2b_model_call_started")
                if event.payload.get("lane_id") in lane_tasks
            ]
        ):
            _blocked("p2b_model_call_start_duplicate")
        failed_call_ids: set[str] = set()
        for failure in policy_failures:
            lane_id = failure.payload["lane_id"]
            task = lane_tasks[lane_id]
            lane = p2b_lanes[lane_id]
            round_number = failure.payload.get("round_number")
            version_id = f"v{round_number:03d}" if isinstance(round_number, int) else ""
            call_id = failure.payload.get("call_id")
            start = starts_by_call.get(call_id)
            stopped = stopped_by_lane.get(lane_id)
            if (
                not _VERSION.fullmatch(version_id)
                or round_number <= 1
                or start is None
                or stopped is None
                or start.payload.get("call_kind") != "policy"
                or start.payload.get("task_id") != task.legacy_task_id
                or stopped.payload.get("task_id") != task.legacy_task_id
            ):
                _blocked("p2b_artifact_failure_binding_differs")
            scope_root = self.p2b_root / _safe_relative(
                lane["history_scope"], "p2b_history_scope_invalid"
            )
            if (scope_root / "policy_metadata" / f"{version_id}.json").exists():
                _blocked("p2b_failed_policy_artifact_unexpectedly_exists")
            parent_version = f"v{round_number - 1:03d}"
            try:
                parent = P2bPolicyArchive(scope_root).load(parent_version)
            except (OSError, ValueError):
                _blocked("p2b_artifact_failure_parent_invalid")
            proof_events = tuple(sorted((start, failure, stopped), key=lambda item: item.index))
            summary = {
                "phase": "P2B",
                "lane_id": lane_id,
                "version": version_id,
                "event_ids": list(_event_ids(proof_events)),
                "candidate_id": None,
                "candidate_sha256": None,
                "decision": {
                    "kind": "profiler_guided_policy_generation",
                    "parent_version_id": parent_version,
                    "parent_policy_sha256": parent.sha256,
                },
                "compiled": False,
                "correct": None,
                "score": None,
                "outcome": "artifact_failure",
                "failure_reason": "invalid_policy_artifact",
                "stage_reached": "policy_generation",
                "terminal_status": "lane_stopped",
                "score_trend": None,
                "novelty": None,
                "profile": None,
                "resource_cost": _resource_cost(model_calls=1, gpu_seconds=0.0),
            }
            _public_guard(summary)
            summaries[task.legacy_task_id].append(
                _BuiltSummary(
                    failure.index,
                    summary,
                    tuple(event.index for event in proof_events),
                )
            )
            failed_call_ids.add(str(call_id))

        if set(generated) != represented or set(evaluations) != represented:
            _blocked("p2b_terminal_attempt_coverage_differs")
        if set(round_events) - represented:
            _blocked("p2b_round_without_terminal_attempt")
        completed_profile_ids = set(profile_events)
        if completed_profile_ids != used_completed_profiles:
            _blocked("p2b_profile_coverage_differs")
        if set(policy_events) != used_policy_events:
            _blocked("p2b_policy_event_coverage_differs")
        all_terminal_call_ids = successful_call_ids | failed_call_ids
        if set(starts_by_call) != all_terminal_call_ids:
            _blocked("p2b_model_call_terminal_coverage_differs")
        completed_lanes = {
            event.payload.get("lane_id")
            for event in _events_of(events, "p2b_lane_completed")
            if event.payload.get("lane_id") in lane_tasks
        }
        if completed_lanes != set(lane_tasks):
            _blocked("p2b_terminal_lane_set_differs")
        expected_incomplete_profile_ids = {
            candidate_id for candidate_id in represented if candidate_id not in round_events
        }
        if (
            used_incomplete_profiles != expected_incomplete_profile_ids
            or set(profile_starts)
            != completed_profile_ids | expected_incomplete_profile_ids
        ):
            _blocked("p2b_profile_start_terminal_coverage_differs")
        for values in summaries.values():
            values.sort(key=lambda item: item.primary_index)
        return summaries

    def _initial_structures(
        self,
        campaign_lanes: dict[str, dict[str, Any]],
        p2b_lanes: dict[str, dict[str, Any]],
    ) -> dict[str, tuple[str, ...]]:
        result: dict[str, tuple[str, ...]] = {}
        for task in self.source_contract.tasks:
            structures: list[str] = []
            for lane_id in task.p1_lane_ids:
                lane = campaign_lanes[lane_id]
                structures.append(
                    _structure_item(
                        {
                            "phase": "P1",
                            "lane_id": lane_id,
                            "kind": lane["kind"],
                            "harness_sha256": lane["harness_sha256"],
                            "workflow": lane["workflow"],
                            "allow_harness_mutation": False,
                        }
                    )
                )
            for lane_id in task.p2_lane_ids:
                lane = campaign_lanes[lane_id]
                scope_root = self.pilot_root / _safe_relative(
                    lane["history_scope"], "pilot_p2_history_scope_invalid"
                )
                try:
                    seed = HarnessArchive(scope_root).load("v001")
                except (OSError, ValueError):
                    _blocked("pilot_p2_seed_artifact_invalid")
                if seed.parent_version_id is not None or seed.sha256 != lane["seed_sha256"]:
                    _blocked("pilot_p2_seed_binding_differs")
                structures.append(
                    _structure_item(
                        {
                            "phase": "P2",
                            "lane_id": lane_id,
                            "lineage_id": lane["lineage_id"],
                            "seed_version_id": "v001",
                            "seed_sha256": seed.sha256,
                            "allow_harness_mutation": True,
                        }
                    )
                )
            for lane_id in task.p2b_lane_ids:
                lane = p2b_lanes[lane_id]
                scope_root = self.p2b_root / _safe_relative(
                    lane["history_scope"], "p2b_history_scope_invalid"
                )
                try:
                    seed = P2bPolicyArchive(scope_root).load("v001")
                    expected = initial_policy(
                        strategy=lane["strategy"],
                        starting_candidate_id=lane["starting_candidate_id"],
                    )
                except (OSError, ValueError):
                    _blocked("p2b_seed_policy_invalid")
                if seed != expected:
                    _blocked("p2b_seed_policy_binding_differs")
                structures.append(
                    _structure_item(
                        {
                            "phase": "P2B",
                            "lane_id": lane_id,
                            "route": lane["strategy"],
                            "starting_candidate_id": lane["starting_candidate_id"],
                            "starting_score": lane["starting_score"],
                            "seed_version_id": "v001",
                            "seed_policy_sha256": seed.sha256,
                            "seed_policy": self._policy_public(seed.policy.to_dict()),
                        }
                    )
                )
            if len(set(structures)) != len(structures):
                _blocked("historical_initial_structure_duplicates")
            result[task.legacy_task_id] = tuple(structures)
        return result


def _write_once(path: Path, content: bytes) -> None:
    if path.exists():
        try:
            if path.read_bytes() != content:
                _blocked("historical_output_binding_conflict")
            return
        except OSError:
            _blocked("historical_output_unreadable")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".historical-import.tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise


def _source_snapshot_payload(contract: HistoricalImportContract) -> dict[str, Any]:
    return {
        "policy_id": contract.policy_id,
        "source_manifest_sha256": contract.manifest_sha256,
        "source_order": list(contract.source_order),
        "winner_selection": False,
        "source_facts": contract.source_facts(),
        "tasks": [
            {
                "source_instance_id": task.source_instance_id,
                "source_sha256": task.source_sha256,
                "p1_lane_ids": list(task.p1_lane_ids),
                "p2_lane_ids": list(task.p2_lane_ids),
                "p2b_lane_ids": list(task.p2b_lane_ids),
                "expected_terminal_summary_counts": task.expected_terminal_summary_counts,
            }
            for task in contract.tasks
        ],
    }


def prepare_historical_trajectories(
    *,
    project_root: Path,
    pilot_root: Path,
    p2b_root: Path,
    output_root: Path,
    meta_train_contract: MetaTrainContract,
    source_contract: HistoricalImportContract,
) -> HistoricalPrepareOutcome:
    """Prepare public objects or one content-addressed blocked report; never call services."""

    output_root = Path(output_root).resolve()
    pilot_root = Path(pilot_root).resolve()
    p2b_root = Path(p2b_root).resolve()
    if output_root == pilot_root or output_root == p2b_root:
        _blocked("historical_output_overlaps_frozen_source")
    if output_root.is_relative_to(pilot_root) or output_root.is_relative_to(p2b_root):
        _blocked("historical_output_overlaps_frozen_source")
    snapshot_payload = _source_snapshot_payload(source_contract)
    snapshot_sha = _sha256_bytes(_canonical_bytes(snapshot_payload))
    trajectories: tuple[MetaTrainTrajectory, ...] = ()
    phase_counts: dict[str, dict[str, int]] = {}
    blockers: list[str] = []
    try:
        result = HistoricalTrajectoryImporter(
            project_root=project_root,
            pilot_root=pilot_root,
            p2b_root=p2b_root,
            meta_train_contract=meta_train_contract,
            source_contract=source_contract,
        ).build()
        trajectories = result.trajectories
        phase_counts = result.phase_counts
        archive = MetaTrainTrajectoryArchive(output_root / "trajectories")
        for trajectory in trajectories:
            archive.store(trajectory)
    except HistoricalImportBlocked as exc:
        blockers.append(exc.code)
        trajectories = ()
        phase_counts = {}
    except (KeyError, OSError, TypeError, ValueError):
        blockers.append("historical_source_validation_failed")
        trajectories = ()
        phase_counts = {}
    report = {
        "schema_version": 1,
        "phase": "hb-gen1-historical-meta-train-import",
        "policy_id": source_contract.policy_id,
        "status": "blocked" if blockers else "ready",
        "blockers": sorted(set(blockers)),
        "source_manifest_sha256": source_contract.manifest_sha256,
        "source_snapshot_sha256": snapshot_sha,
        "source_facts": source_contract.source_facts(),
        "phase_counts": phase_counts,
        "trajectory_sha256s": {
            trajectory.source_instance_id: trajectory.sha256
            for trajectory in trajectories
        },
        "model_calls_started": 0,
        "evaluator_transactions_started": 0,
        "gpu_seconds_started": 0.0,
        "network_requests_started": 0,
    }
    _public_guard(report)
    content = _canonical_bytes(report)
    report_sha = _sha256_bytes(content)
    relative = f"prepares/{report_sha}.json"
    _write_once(output_root / relative, content)
    return HistoricalPrepareOutcome(
        report=report,
        report_sha256=report_sha,
        report_relative_path=relative,
        trajectories=trajectories,
    )
