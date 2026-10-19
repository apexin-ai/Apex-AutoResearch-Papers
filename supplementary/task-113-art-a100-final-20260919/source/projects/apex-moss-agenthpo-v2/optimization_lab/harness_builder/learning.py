from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from optimization_lab.generation import CandidateGenerator, GenerationResult

from .experience import ExperienceRecord, promotion_level
from .stream import ARMS, PrequentialState


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_PRIVATE_TEXT = re.compile(
    r"(?:/home/|/data\d*/|private[_ -]evaluator|private[_ -]log)", re.IGNORECASE
)
_JSON_FENCE = re.compile(r"\s*```(?:json)?\s*\n(.*?)```\s*", re.DOTALL | re.IGNORECASE)


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _write_once(path: Path, content: bytes) -> None:
    if path.exists():
        if path.read_bytes() != content:
            raise ValueError("refusing to overwrite a different content-addressed artifact")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".hb-learning.tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise


@dataclass(frozen=True)
class ExperienceBankSnapshot:
    bank_id: str
    parent_sha256: str | None
    records: tuple[ExperienceRecord, ...]

    @classmethod
    def create(
        cls,
        *,
        bank_id: str,
        parent_sha256: str | None,
        records: tuple[ExperienceRecord, ...],
    ) -> "ExperienceBankSnapshot":
        if not _SAFE_ID.fullmatch(bank_id):
            raise ValueError("unsafe Experience Bank id")
        if parent_sha256 is not None and not _SHA256.fullmatch(parent_sha256):
            raise ValueError("invalid parent Experience Bank sha256")
        if len({record.record_id for record in records}) != len(records):
            raise ValueError("Experience Record ids must be unique")
        return cls(bank_id=bank_id, parent_sha256=parent_sha256, records=records)

    def core_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "bank_id": self.bank_id,
            "parent_sha256": self.parent_sha256,
            "records": [record.to_dict() for record in self.records],
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.core_payload())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    def extend(
        self,
        records: tuple[ExperienceRecord, ...],
        *,
        bank_id: str,
    ) -> "ExperienceBankSnapshot":
        if not records:
            raise ValueError("an Experience Bank update cannot be empty")
        existing = {record.record_id: record for record in self.records}
        for record in records:
            if record.record_id in existing:
                raise ValueError("Experience record id is already bound")
        return self.create(
            bank_id=bank_id,
            parent_sha256=self.sha256,
            records=self.records + records,
        )

    def promotion_for(self, rule_id: str) -> str | None:
        sources = {
            record.source_instance_id
            for record in self.records
            if record.evolution_rule == rule_id
        }
        if not sources:
            return None
        suites = {source.split(":", 1)[0] for source in sources}
        return promotion_level(
            instance_count=len(sources), benchmark_count=len(suites)
        )

    def retrieve(
        self,
        *,
        instance_id: str,
        instance_descriptors: tuple[str, ...],
        limit: int = 8,
    ) -> tuple[dict[str, str], ...]:
        """Return bounded, deterministic public experience for an unseen instance.

        Promotion is derived from other sealed instances at retrieval time; source
        records remain immutable single-instance observations.
        """

        if not _SAFE_ID.fullmatch(instance_id):
            raise ValueError("unsafe retrieval instance id")
        if (
            not instance_descriptors
            or not all(isinstance(item, str) and item.strip() for item in instance_descriptors)
        ):
            raise ValueError("retrieval descriptors must be non-empty text")
        if not isinstance(limit, int) or isinstance(limit, bool) or not 1 <= limit <= 32:
            raise ValueError("retrieval limit must be between one and 32")

        query = {item.casefold() for item in instance_descriptors}
        eligible = tuple(
            record for record in self.records if record.source_instance_id != instance_id
        )
        support: dict[str, tuple[int, int]] = {}
        for rule_id in {record.evolution_rule for record in eligible}:
            sources = {
                record.source_instance_id
                for record in eligible
                if record.evolution_rule == rule_id
            }
            suites = {source.split(":", 1)[0] for source in sources}
            support[rule_id] = (len(sources), len(suites))

        promotion_rank = {
            "single_instance_observation": 0,
            "within_benchmark_replicated": 1,
            "cross_benchmark_replicated": 2,
            "trusted_default_prior": 3,
        }

        def derived_scope(record: ExperienceRecord) -> str:
            instances, benchmarks = support[record.evolution_rule]
            return promotion_level(
                instance_count=instances, benchmark_count=benchmarks
            )

        def rank(record: ExperienceRecord) -> tuple[float, int, int, float, str]:
            descriptors = {item.casefold() for item in record.instance_descriptor}
            overlap = len(query & descriptors) / len(query | descriptors)
            scope = derived_scope(record)
            return (
                -overlap,
                -promotion_rank[scope],
                -int(record.correctness),
                -abs(record.outcome_delta),
                record.record_id,
            )

        selected = sorted(eligible, key=rank)[:limit]
        return tuple(
            {
                "record_id": record.record_id,
                "source_instance_id": record.source_instance_id,
                "scope": derived_scope(record),
                "summary": (
                    f"descriptors={','.join(record.instance_descriptor)}; "
                    f"initial_harness={','.join(record.initial_harness_structure)}; "
                    f"evolution_rule={record.evolution_rule}; "
                    f"trigger={' | '.join(record.trigger_evidence)}; "
                    f"outcome_delta={record.outcome_delta:+.6f}; "
                    f"correctness={str(record.correctness).lower()}; "
                    f"counterexamples={' | '.join(record.counterexamples)}"
                )[:4000],
            }
            for record in selected
        )


class ExperienceBankArchive:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()

    def store(self, snapshot: ExperienceBankSnapshot) -> Path:
        path = self.root / f"{snapshot.sha256}.json"
        _write_once(path, snapshot.canonical_bytes)
        return path


@dataclass(frozen=True)
class BuilderCheckpoint:
    parent_checkpoint_sha256: str
    experience_bank_sha256: str
    rule_registry_sha256: str
    learned_through_instance: str
    stream_index: int

    def __post_init__(self) -> None:
        for value, label in (
            (self.parent_checkpoint_sha256, "parent checkpoint"),
            (self.experience_bank_sha256, "Experience Bank"),
            (self.rule_registry_sha256, "Rule Registry"),
        ):
            if not _SHA256.fullmatch(value):
                raise ValueError(f"invalid {label} sha256")
        if not _SAFE_ID.fullmatch(self.learned_through_instance):
            raise ValueError("unsafe learned-through instance id")
        if self.stream_index < 0:
            raise ValueError("stream index cannot be negative")

    def core_payload(self) -> dict[str, Any]:
        return {"schema_version": 1, **asdict(self)}

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.core_payload())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


class BuilderCheckpointArchive:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()

    def store(self, checkpoint: BuilderCheckpoint) -> Path:
        path = self.root / f"{checkpoint.sha256}.json"
        _write_once(path, checkpoint.canonical_bytes)
        return path


@dataclass(frozen=True)
class SealedInstanceTrajectory:
    instance_id: str
    suite: str
    builder_checkpoint_sha256: str
    arm_event_ids: dict[str, tuple[str, ...]]
    public_summary: dict[str, dict[str, Any]]
    sealed: bool

    def __post_init__(self) -> None:
        if not _SAFE_ID.fullmatch(self.instance_id) or not _SAFE_ID.fullmatch(self.suite):
            raise ValueError("unsafe sealed trajectory identity")
        if not _SHA256.fullmatch(self.builder_checkpoint_sha256):
            raise ValueError("sealed trajectory checkpoint must be content addressed")
        if self.sealed is not True:
            raise ValueError("trajectory must be sealed")
        arm_ids = frozenset(self.arm_event_ids)
        allowed_arm_sets = {frozenset(ARMS), frozenset({"B-online"})}
        if (
            arm_ids not in allowed_arm_sets
            or arm_ids != set(self.public_summary)
        ):
            raise ValueError("sealed trajectory arm bindings differ")
        if any(not ids for ids in self.arm_event_ids.values()):
            raise ValueError("each sealed arm requires provenance events")
        serialized = json.dumps(
            {"arm_event_ids": self.arm_event_ids, "public_summary": self.public_summary},
            ensure_ascii=False,
        )
        if _PRIVATE_TEXT.search(serialized):
            raise ValueError("sealed public trajectory contains private evaluator data")

    @property
    def provenance_event_ids(self) -> frozenset[str]:
        return frozenset(
            event_id for event_ids in self.arm_event_ids.values() for event_id in event_ids
        )

    def public_payload(self) -> dict[str, Any]:
        return {
            "instance_id": self.instance_id,
            "suite": self.suite,
            "builder_checkpoint_sha256": self.builder_checkpoint_sha256,
            "arm_event_ids": {key: list(value) for key, value in self.arm_event_ids.items()},
            "public_summary": self.public_summary,
            "sealed": True,
        }


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def parse_distillation_records(raw_response: str) -> tuple[ExperienceRecord, ...]:
    if not isinstance(raw_response, str) or not raw_response.strip():
        raise ValueError("distillation response cannot be empty")
    if len(raw_response) > 256_000:
        raise ValueError("distillation response is too large")
    stripped = raw_response.strip()
    fenced = _JSON_FENCE.fullmatch(stripped)
    if fenced:
        stripped = fenced.group(1).strip()
    elif not (stripped.startswith("{") and stripped.endswith("}")):
        raise ValueError("distillation JSON must occupy the whole response")
    try:
        payload = json.loads(stripped, object_pairs_hook=_unique_object)
    except json.JSONDecodeError as exc:
        raise ValueError("distillation response is not strict JSON") from exc
    if not isinstance(payload, dict) or set(payload) != {"records"}:
        raise ValueError("distillation response must contain only records")
    if not isinstance(payload["records"], list) or not payload["records"]:
        raise ValueError("distillation requires at least one Experience Record")
    return tuple(ExperienceRecord.from_dict(record) for record in payload["records"])


@dataclass(frozen=True)
class ContinualUpdateResult:
    bank: ExperienceBankSnapshot
    checkpoint: BuilderCheckpoint
    generation_result: GenerationResult


class ContinualUpdater:
    def __init__(
        self,
        *,
        bank_archive: ExperienceBankArchive,
        checkpoint_archive: BuilderCheckpointArchive,
        distiller: CandidateGenerator,
        model: str,
        rule_registry_sha256: str,
    ) -> None:
        if not model.strip() or not _SHA256.fullmatch(rule_registry_sha256):
            raise ValueError("continual updater model and Rule Registry are required")
        self.bank_archive = bank_archive
        self.checkpoint_archive = checkpoint_archive
        self.distiller = distiller
        self.model = model
        self.rule_registry_sha256 = rule_registry_sha256

    def update(
        self,
        *,
        state: PrequentialState,
        trajectory: SealedInstanceTrajectory,
        bank: ExperienceBankSnapshot,
    ) -> ContinualUpdateResult:
        if not state.ready_for_distillation:
            raise ValueError("current instance must be fully sealed before distillation")
        current = state.current
        if trajectory.instance_id != current.instance_id:
            raise ValueError("trajectory does not match the current sealed instance")
        example_record = {
            "record_id": f"exp-{current.stream_index:03d}-001",
            "source_instance_id": current.instance_id,
            "builder_version": trajectory.builder_checkpoint_sha256,
            "instance_descriptor": ["one public task characteristic"],
            "initial_harness_structure": ["one initial role or workflow element"],
            "evolution_rule": "discipline",
            "trigger_evidence": ["one observation from the public trajectory"],
            "outcome_delta": 0.0,
            "correctness": True,
            "resource_cost": {"model_calls": 0.0},
            "counterexamples": ["none observed in this sealed trajectory"],
            "scope": "single_instance_observation",
            "provenance_event_ids": [sorted(trajectory.provenance_event_ids)[0]],
            "sealed": True,
        }
        response_template = json.dumps(
            {"records": [example_record]},
            ensure_ascii=False,
            indent=2,
        )
        prompt = (
            "Distill the fully sealed first-encounter trajectory into one or more strict "
            "Experience Records. Capture both the initial Harness structure and the evidence-"
            "matched evolution direction. Use only supplied public event IDs. Each record scope "
            "must be single_instance_observation. Return one bare JSON object with only a "
            "records array. Every record must contain exactly these 14 keys and no others: "
            "record_id, source_instance_id, builder_version, instance_descriptor, "
            "initial_harness_structure, evolution_rule, trigger_evidence, outcome_delta, "
            "correctness, resource_cost, counterexamples, scope, provenance_event_ids, sealed. "
            "Do not substitute suite, instance_id, builder_checkpoint_sha256, observation, "
            "evidence_event_ids, or any other aliases for those keys. Keep the exact "
            "source_instance_id, builder_version, scope, provenance event vocabulary, and JSON "
            "types shown below; replace only the descriptive example content with facts supported "
            "by the supplied public trajectory.\n\n"
            "Required response template:\n"
            + response_template
            + "\n\nSealed public trajectory:\n"
            + json.dumps(trajectory.public_payload(), ensure_ascii=False, indent=2, sort_keys=True)
        )
        generation = self.distiller.generate(prompt, model=self.model)
        records = parse_distillation_records(generation.raw_response)
        for record in records:
            if record.source_instance_id != current.instance_id:
                raise ValueError("Experience Record does not describe the current sealed instance")
            if record.scope != "single_instance_observation":
                raise ValueError("one instance cannot self-promote an Experience Record")
            if not set(record.provenance_event_ids).issubset(
                trajectory.provenance_event_ids
            ):
                raise ValueError("Experience Record cites unbound provenance events")

        updated = bank.extend(
            records,
            # Keep the identifier bounded across the full 24-instance stream.  The
            # parent hash, not an ever-growing human label, is the authoritative
            # lineage pointer.
            bank_id=f"hb-gen1-online-stream-{current.stream_index:03d}",
        )
        self.bank_archive.store(updated)
        checkpoint = BuilderCheckpoint(
            parent_checkpoint_sha256=state.online_checkpoint_sha256,
            experience_bank_sha256=updated.sha256,
            rule_registry_sha256=self.rule_registry_sha256,
            learned_through_instance=current.instance_id,
            stream_index=current.stream_index,
        )
        self.checkpoint_archive.store(checkpoint)
        state.apply_distillation(checkpoint.sha256)
        return ContinualUpdateResult(
            bank=updated,
            checkpoint=checkpoint,
            generation_result=generation,
        )
